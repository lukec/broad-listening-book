#!/usr/bin/env python3
"""
English translation tooling for the manuscript.

Examples:
    python3 scripts/english.py list-sections
    python3 scripts/english.py translate-section --first --dry-run
    python3 scripts/english.py translate-section --section ch00_preface --model gpt-4o-mini
"""

import argparse
import hashlib
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

TRANSLATION_SYSTEM_PROMPT = """You translate Japanese manuscript markdown into natural, publication-quality English.

Hard requirements:
- Preserve markdown structure.
- Preserve heading levels, lists, tables, links, code fences, and footnote anchors.
- Keep image paths and URLs unchanged.
- Translate image alt text and normal prose.
- Return only translated markdown with no preface or code fences.
"""


def load_order_sections(order_file: Path) -> dict[str, list[str]]:
    sections: dict[str, list[str]] = {}
    current_section: str | None = None

    with open(order_file, "r", encoding="utf-8") as f:
        for raw_line in f:
            line = raw_line.strip()
            if not line or line.startswith("#"):
                continue

            section_match = re.match(r"^\[(.+)\]$", line)
            if section_match:
                current_section = section_match.group(1)
                sections.setdefault(current_section, [])
                continue

            if current_section is None:
                continue

            sections[current_section].append(line)

    return sections


def ensure_en_layout(source_order_file: Path, en_root: Path, overwrite_order: bool) -> None:
    en_root.mkdir(parents=True, exist_ok=True)
    (en_root / "metadata").mkdir(parents=True, exist_ok=True)

    en_order_file = en_root / "book_order.txt"
    if overwrite_order or not en_order_file.exists():
        en_order_file.write_text(source_order_file.read_text(encoding="utf-8"), encoding="utf-8")


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def load_manifest(manifest_path: Path) -> dict:
    if not manifest_path.exists():
        return {"entries": {}}
    return json.loads(manifest_path.read_text(encoding="utf-8"))


def save_manifest(manifest_path: Path, manifest: dict) -> None:
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def clean_model_output(text: str) -> str:
    stripped = text.strip()
    if stripped.startswith("```"):
        stripped = re.sub(r"^```[a-zA-Z0-9_-]*\n?", "", stripped)
        stripped = re.sub(r"\n?```$", "", stripped)
    return stripped.strip() + "\n"


def translate_markdown_with_openai(
    source_markdown: str,
    model: str,
    temperature: float,
) -> str:
    try:
        from openai import OpenAI
    except ModuleNotFoundError as exc:
        raise RuntimeError(
            "openai package is not installed. Install project dependencies first."
        ) from exc

    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY is not set.")

    client = OpenAI()
    response = client.chat.completions.create(
        model=model,
        temperature=temperature,
        messages=[
            {"role": "system", "content": TRANSLATION_SYSTEM_PROMPT},
            {"role": "user", "content": source_markdown},
        ],
    )
    content = response.choices[0].message.content or ""
    return clean_model_output(content)


def translate_file(
    source_path: Path,
    target_path: Path,
    model: str,
    temperature: float,
    dry_run: bool,
) -> tuple[str, str]:
    source_text = source_path.read_text(encoding="utf-8")
    source_hash = sha256_text(source_text)

    if dry_run:
        return source_hash, ""

    translated = translate_markdown_with_openai(
        source_markdown=source_text,
        model=model,
        temperature=temperature,
    )
    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(translated, encoding="utf-8")
    return source_hash, sha256_text(translated)


def cmd_list_sections(args: argparse.Namespace) -> int:
    sections = load_order_sections(args.order_file)
    if not sections:
        print(f"No sections found in {args.order_file}")
        return 1

    print("Sections:")
    for name, files in sections.items():
        print(f"- {name} ({len(files)} files)")
    return 0


def resolve_section_name(sections: dict[str, list[str]], section: str | None, first: bool) -> str:
    if section:
        if section not in sections:
            valid = ", ".join(sections.keys())
            raise ValueError(f"Section '{section}' not found. Valid sections: {valid}")
        return section

    if first:
        return next(iter(sections))

    raise ValueError("Specify --section <name> or pass --first.")


def cmd_translate_section(args: argparse.Namespace) -> int:
    sections = load_order_sections(args.order_file)
    if not sections:
        print(f"No sections found in {args.order_file}")
        return 1

    try:
        section_name = resolve_section_name(sections, args.section, args.first)
    except ValueError as exc:
        print(str(exc))
        return 1

    manifest_path = args.en_root / "metadata" / "manifest.json"
    if not args.dry_run:
        ensure_en_layout(args.order_file, args.en_root, args.overwrite_order)
        manifest = load_manifest(manifest_path)
    else:
        manifest = {"entries": {}}
    entries = manifest.setdefault("entries", {})

    files = sections[section_name]
    print(f"Translating section [{section_name}] with {len(files)} files")

    translated_count = 0
    skipped_count = 0

    for relative_path in files:
        source_path = args.source_root / relative_path
        target_path = args.en_root / relative_path

        if not source_path.exists():
            print(f"[WARN] Missing source file: {source_path}")
            continue

        if target_path.exists() and not args.overwrite:
            print(f"[SKIP] {relative_path} (already exists, use --overwrite to replace)")
            skipped_count += 1
            continue

        print(f"[TRANSLATE] {relative_path}")
        try:
            source_hash, target_hash = translate_file(
                source_path=source_path,
                target_path=target_path,
                model=args.model,
                temperature=args.temperature,
                dry_run=args.dry_run,
            )
        except RuntimeError as exc:
            print(f"[ERROR] {relative_path}: {exc}")
            return 1

        if args.dry_run:
            print(f"[DRY-RUN] Would write: {target_path}")
        else:
            translated_count += 1

        entries[relative_path] = {
            "source_path": relative_path,
            "target_path": str(target_path.relative_to(args.en_root)),
            "source_hash": source_hash,
            "target_hash": target_hash,
            "section": section_name,
            "model": args.model,
            "status": "translated" if not args.dry_run else "dry-run",
            "updated_at": datetime.now(timezone.utc).isoformat(),
        }

    manifest["last_section"] = section_name
    manifest["updated_at"] = datetime.now(timezone.utc).isoformat()
    if not args.dry_run:
        save_manifest(manifest_path, manifest)

    print(
        f"Done. translated={translated_count}, skipped={skipped_count}, "
        f"dry_run={'yes' if args.dry_run else 'no'}"
    )
    return 0


def build_parser() -> argparse.ArgumentParser:
    def add_common_args(target: argparse.ArgumentParser) -> None:
        target.add_argument(
            "--source-root",
            type=Path,
            default=Path(__file__).parent.parent,
            help="Repository root that contains Japanese source files",
        )
        target.add_argument(
            "--order-file",
            type=Path,
            default=Path(__file__).parent.parent / "book_order.txt",
            help="Order file used to define sections",
        )
        target.add_argument(
            "--en-root",
            type=Path,
            default=Path(__file__).parent.parent / "en",
            help="Output root for English markdown",
        )

    parser = argparse.ArgumentParser(description="English translation tooling")
    subparsers = parser.add_subparsers(dest="command", required=True)

    list_parser = subparsers.add_parser("list-sections", help="List section names from the order file")
    add_common_args(list_parser)

    translate_parser = subparsers.add_parser(
        "translate-section",
        help="Translate a section from Japanese markdown to English markdown",
    )
    add_common_args(translate_parser)
    translate_parser.add_argument("--section", help="Section name from [section] in book_order.txt")
    translate_parser.add_argument(
        "--first",
        action="store_true",
        help="Translate the first section from the order file",
    )
    translate_parser.add_argument(
        "--model",
        default="gpt-4o-mini",
        help="OpenAI model for translation",
    )
    translate_parser.add_argument(
        "--temperature",
        type=float,
        default=0.2,
        help="Sampling temperature for translation",
    )
    translate_parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing translated files",
    )
    translate_parser.add_argument(
        "--overwrite-order",
        action="store_true",
        help="Overwrite en/book_order.txt from source order file",
    )
    translate_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Plan translation without writing files or calling the API",
    )

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "list-sections":
        exit_code = cmd_list_sections(args)
    elif args.command == "translate-section":
        exit_code = cmd_translate_section(args)
    else:
        print(f"Unknown command: {args.command}")
        exit_code = 1

    if exit_code != 0:
        sys.exit(exit_code)


if __name__ == "__main__":
    main()
