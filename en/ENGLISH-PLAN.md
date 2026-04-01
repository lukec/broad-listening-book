# English Translation Plan (Concise)

## Intent

- Japanese manuscript is the source of truth.
- English is maintained as a parallel manuscript for international readers and reviewers.
- Translation quality is non-negotiable: LLM output is a draft, not the final text.

## Quality Policy

1. First pass: LLM translation.
2. Required second pass: human review by a native English speaker.
3. “Reviewed” status is only granted after human review.
4. Any translation faults are owned by the translator, not the original Japanese authors.

## Operating Rules

- Keep markdown structure intact (headings, lists, tables, links, footnotes, images).
- Apply glossary/term rules consistently.
- Do not add glossary expansions in headings.
- For upstream Japanese edits, only changed sections are retranslated, then re-reviewed.
- Publish English updates with commit-level traceability.

## CLI Workflow

```bash
# translate one section
python3 scripts/english.py translate-section --section <section_key> --model gpt-5.4

# build multilingual web output
python3 scripts/build_web_book.py
```

## Review Log

Baseline: as of `2026-04-01`, no section has been reviewed.

| Section | Scope | Reviewed Date | Reviewed Commit | Status |
|---|---|---|---|---|
| ch00_preface | `00_preface.md`, `00_endorsement_from_audrey_tang.md` | — | — | Not reviewed |
| ch01_broadlistening_overview | `01_what_is_broad_listening.md` | — | — | Not reviewed |
| ch02_broadlistening_vs_survey | `02_broad_listening_vs_surveys.md`, `column/word_cloud_is_not_analysis.md` | — | — | Not reviewed |
| ch03_digital_democracy_and_public_voice | `03_digital_democracy_and_new_public_voice.md`, `column/safe_empathy.md` | — | — | Not reviewed |
| ch04_broadlistening_spread_in_japan | `04_*` | — | — | Not reviewed |
| ch05_tokyo_shin_tokyo_2050 | `05_tokyo_shin_tokyo_2050_policy_shift.md` | — | — | Not reviewed |
| ch06_national_elections | `06_*` | — | — | Not reviewed |
| ch07_local_elections | `07_*` | — | — | Not reviewed |
| ch08_municipalities | `08_*` | — | — | Not reviewed |
| ch09_enterprise_and_npo | `09_*`, `column/testing_kocho_ai_through_review.md` | — | — | Not reviewed |
| ch10_broadlistening_business | `10_*`, `column/lessons_from_collecting_10000_voices.md`, `column/fujitsu_enterprise_ai_for_public_comments.md` | — | — | Not reviewed |
| ch11_broadlistening_overseas | `11_*` | — | — | Not reviewed |
| ch12_broadlistening_technology | `12_broad_listening_component_technologies.md` | — | — | Not reviewed |
| ch13_kocho_ai_tech_stack | `13_kocho_ai_tech_stack.md` | — | — | Not reviewed |
| ch99_appendix | `99_appendix_public_cases.md` | — | — | Not reviewed |

