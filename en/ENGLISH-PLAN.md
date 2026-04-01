# English Translation Tooling Plan

## Repository Review

The current repository shape is workable for an English pipeline, but the tooling should be designed around the manuscript as it actually exists today.

- The Japanese manuscript at the repo root should remain the canonical upstream source.
- [`book_order.txt`](/Users/lukec/src/broad-listening-book/book_order.txt) is already the authoritative publication order.
- `book_order.txt` currently includes 48 entries: 43 top level manuscript files and 5 column files.
- [`scripts/build_pdf.py`](/Users/lukec/src/broad-listening-book/scripts/build_pdf.py) already builds HTML and PDF from an order file, so it should be extended rather than replaced.
- There is already some English material in [`intro_en.md`](/Users/lukec/src/broad-listening-book/intro_en.md), which is useful as a seed for style and terminology.
- The image surface area is large: 152 files under `images/`, with 146 local Markdown image references across 34 Markdown files.
- Many chapters contain footnotes, author bylines, and long descriptive alt text. The English tooling must preserve those structures.
- There are a few broken local Markdown links today. The English pipeline should validate and normalize links instead of assuming the source is perfectly uniform.
- One implementation detail matters immediately: the current PDF builder resolves image paths from the repo root, not from each Markdown file's directory. That is fragile now and will break more often once English files live in a parallel tree.

## Goals

1. Produce an initial English translation quickly, so reviewers can start reading and correcting content early.
2. Support ongoing synchronization as the Japanese manuscript continues to change upstream.
3. Preserve manuscript structure: headings, lists, tables, footnotes, image references, and chapter order.
4. Keep the workflow CLI-first and scriptable with `uv run python`.
5. Separate "good enough for English review" from "final localized English edition", especially for images.

## Recommended Layout

Keep Japanese content where it is. Add a parallel English tree plus metadata.

```text
en/
  book_order.txt
  00_endorsement_from_Audrey.md
  00_序文.md
  01_ブロードリスニングとは何か？.md
  ...
  99_付録_公開事例一覧.md
  column/
    ...
  images/
    localized/
    notes/
  metadata/
    manifest.json
    segments.jsonl
    glossary.yml
    style.md
    translation_memory.jsonl
    review_status.yml
    image_manifest.json
```

Why this layout:

- It keeps Japanese and English clearly separated.
- It preserves a near 1:1 path mapping from source to translation.
- It allows reviewers to edit English Markdown directly without touching the Japanese source.
- It avoids inventing a second naming system for chapters.

## Core Design

### 1. Treat translation as synchronization, not one time generation

The English workflow should track both file level and segment level state.

- File level state answers: "Has this Japanese file changed since the last English sync?"
- Segment level state answers: "Which sections inside this file changed, and which English sections are now stale?"

Recommended segment boundary:

- Split by heading hierarchy first.
- Keep paragraphs, lists, blockquotes, tables, footnotes, and image blocks intact inside each section.
- Do not translate sentence by sentence unless a section is extremely large.

This gives a stable unit for retranslation without constantly overwriting reviewer edits.

### 2. Keep a small but explicit metadata layer

Recommended metadata fields:

- `manifest.json`: source path, english path, chapter id, source hash, last synced hash, status
- `segments.jsonl`: source path, section key, section hash, english hash, status, reviewer notes
- `glossary.yml`: canonical translations for product names, organization names, recurring terms
- `translation_memory.jsonl`: approved source and target segment pairs
- `review_status.yml`: draft, needs-review, reviewed, approved
- `image_manifest.json`: image source path, hash, referenced-by files, mode, localized asset path, alt text, status

This should stay sidecar-based rather than embedding sync markers into the manuscript unless patching later proves too fragile.

### 3. Preserve reviewer edits

Human reviewers should edit files in `en/` directly. Sync tooling should then:

- leave unchanged English sections alone
- only replace sections whose Japanese source changed
- flag ambiguous rewrites for manual review instead of silently rewriting them

If a Japanese section changes heavily, the tool should show:

- the old Japanese source excerpt
- the new Japanese source excerpt
- the current English section
- the proposed replacement

That is much safer than blind overwrite.

## CLI Surface

One script with subcommands is enough. Suggested path: `scripts/english.py`.

Suggested commands:

```bash
uv run python scripts/english.py inventory
uv run python scripts/english.py init
uv run python scripts/english.py translate --chapter 01
uv run python scripts/english.py translate --file 06_01_チームみらい.md
uv run python scripts/english.py translate --changed
uv run python scripts/english.py images --chapter 08_01
uv run python scripts/english.py review-report
uv run python scripts/english.py build --html
uv run python scripts/english.py build --pdf
```

Expected behavior:

- `inventory`: scan Japanese manuscript, refresh manifests, detect changed files and images
- `init`: create `en/` tree, seed `en/book_order.txt`, copy metadata templates
- `translate`: translate one chapter, one file, or all stale files
- `images`: refresh image inventory and optionally generate English image notes or localized image tasks
- `review-report`: show what changed, what is stale, and what still needs human review
- `build`: build English HTML or PDF using `en/book_order.txt`

The command surface should accept chapter ids like `01`, `04_02`, `column/...` so the user does not have to type Japanese filenames every time.

## Translation Workflow

### Phase A. Foundational setup

Build these first:

1. Inventory scanner for Markdown, columns, appendix, and images.
2. English directory bootstrapper.
3. Build pipeline fix so relative links and image paths resolve from each source file location, not from repo root.
4. Glossary and style guide seeding from [`intro_en.md`](/Users/lukec/src/broad-listening-book/intro_en.md).

### Phase B. First pass English reviewer edition

Goal: get readable English chapters into review quickly.

- Translate Markdown text into `en/`.
- Preserve headings, lists, tables, links, footnotes, image references, and blank-line structure where reasonable.
- Rewrite internal Markdown links from Japanese paths to English paths.
- Keep original image binaries for now unless an image is unreadable without localization.
- Translate image alt text and caption-like adjacent text.
- Mark files as `needs-review` after machine generation.

This is the fastest path to inviting English native reviewers into the process.

### Phase C. Incremental sync from upstream Japanese edits

For later upstream changes:

1. Run `inventory`.
2. Detect changed Japanese files by hash.
3. Re-segment only changed files.
4. Match unchanged sections by section key and content hash.
5. Retranslate only stale sections.
6. Emit a review report showing all touched English sections.

This lets English stay current without redoing already reviewed content.

## Image Strategy

Image handling should have two tracks.

### Track 1. Reviewer edition

Use this first.

- Keep original images in place.
- Translate alt text into English.
- Generate optional English image notes in `en/images/notes/`.
- Flag images whose embedded Japanese text is critical to understanding.

This is enough for many screenshots and photos, and it is much cheaper than full localization.

### Track 2. Localized figure edition

Use this only where English readers genuinely need localized visuals.

Each image gets a mode in `image_manifest.json`:

- `reuse`: keep original image
- `caption-only`: keep image, improve English alt text and nearby explanation
- `overlay`: OCR Japanese text, translate, and render an annotated English version
- `redraw`: recreate the figure in English from source data or a structured spec

Recommended output location:

- `en/images/localized/<same-stem>.<ext>`

The English Markdown should prefer localized assets when they exist, otherwise fall back to the original source image.

## Terminology and Style

Create `en/metadata/glossary.yml` early and treat it as mandatory input to the translation prompts.

It should cover at least:

- Broad Listening
- Koucho AI / 広聴AI
- Talk to the City
- Idobata / いどばた
- Baisoku Kaigi / 倍速会議
- party names, organization names, program names, and recurring civic-tech terms

Rules worth enforcing:

- preserve URLs and citations exactly
- preserve footnote numbering and anchors
- translate bylines consistently, for example `文責：` to `Author:` or `Written by:`
- keep established Japanese names in romaji or original form when English translation would be unnatural
- prefer consistency over local stylistic improvisation

[`intro_en.md`](/Users/lukec/src/broad-listening-book/intro_en.md) should become the initial style reference, but it should be normalized into a shorter `style.md` for prompts.

## Build and Validation

The existing builder can be extended to support English output.

Recommended improvements to [`scripts/build_pdf.py`](/Users/lukec/src/broad-listening-book/scripts/build_pdf.py):

- allow `--base-dir` so the builder can work against `en/`
- resolve images and local links relative to each Markdown file's own directory
- allow title and language overrides
- optionally validate missing files, missing localized images, and broken links before build

Suggested English build commands after implementation:

```bash
uv run python scripts/english.py build --html
uv run python scripts/english.py build --pdf
```

## Implementation Order

Recommended order of work:

1. Fix and extend the build pipeline for per-file path resolution and English output.
2. Add inventory and manifest generation.
3. Add glossary and style inputs.
4. Add chapter translation for first pass generation.
5. Add changed-section sync.
6. Add image inventory and image modes.
7. Add reviewer reports and validation checks.

This order gets useful output quickly while still building toward a maintainable sync workflow.

## Recommendation

The safest approach is not "translate the whole book once and hope it freezes." It is "maintain a parallel English manuscript that is continuously synced from Japanese, with hashes and section manifests doing the mechanical work and humans doing the editorial work."

That gives you:

- a fast initial English draft for reviewers
- a practical path for ongoing upstream edits
- a clean CLI workflow
- a way to defer expensive image localization until it is actually needed
