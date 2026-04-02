# English Translation Plan

## Intent

- Japanese manuscript is the source of truth.
- English text is an LLM-first draft, then human-reviewed.
- Reviews are tracked by section, date, and commit.

## Workflow

1. Translate only target sections with `scripts/english.py` (`--model gpt-5.4`).
2. Apply term rules and style rules.
3. Human review by an English-native reviewer.
4. Refresh the rendered preview used for review.

## Translation Options

- **Team Mirai**: In this English edition, render as **Team Future** for readability and impact with English-native readers.
- First mention format: `Team Mirai (referred to as “Team Future” in this book)`.
- Note: **Team Future** is an editorial translation choice, not necessarily the official party name.

## Review Log

| Section | Scope | Reviewed Date | Reviewed Commit | Status |
|---|---|---|---|---|
| ch00_preface | `00_preface.md` | 2026-04-01 | `b624c37` | Reviewed |
| ch00_endorsement | `00_endorsement_from_audrey_tang.md` | — | — | Not reviewed |
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
