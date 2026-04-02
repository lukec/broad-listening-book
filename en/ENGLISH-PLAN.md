# English Translation Plan

## Intent

- Japanese manuscript is the source of truth.
- English text is an LLM-first draft, then human-reviewed.
- Reviews are tracked by section, date, and Japanese-source commit.

## Workflow

1. Translate only target sections with `scripts/english.py` (`--model gpt-5.4`).
2. Apply term rules and style rules.
3. Human review by an English-native reviewer.
4. Refresh the rendered preview used for review.

## Translation Options

- **Team Mirai**: In this English edition, render as **Team Future** for readability and impact with English-native readers.
- First mention format: `Team Mirai (referred to as “Team Future” in this book)`.
- Note: **Team Future** is an editorial translation choice, not necessarily the official party name.
- **Bluesky**: In Chapter 2, add **Bluesky** after **Facebook** as an editorial choice for English audiences.

## Review Log

| Section | Scope | Reviewed Date | Source Commit (JP) | Status |
|---|---|---|---|---|
| ch00_preface | `00_preface.md` | 2026-04-01 | `c70f5ef` | Reviewed |
| ch00_endorsement | `00_endorsement_from_audrey_tang.md` | 2026-04-01 | `6f870e0` | Reviewed |
| ch01_broadlistening_overview | `01_what_is_broad_listening.md` | 2026-04-01 | `a62f4b9` | Reviewed (text passed) |
| ch02_broadlistening_vs_survey | `02_broad_listening_vs_surveys.md` | 2026-04-01 | `1444248` | Reviewed |
| ch02_column_word_cloud | `column/word_cloud_is_not_analysis.md` | 2026-04-01 | `4b29b9d` | Reviewed |
| ch03_digital_democracy_and_public_voice | `03_digital_democracy_and_new_public_voice.md` | 2026-04-01 | `e3aa55a` | Reviewed (text passed; image review tracked below) |
| ch03_column_safe_empathy | `column/safe_empathy.md` | 2026-04-01 | `e3aa55a` | Reviewed (absolutely amazing) |
| ch04_broadlistening_spread_in_japan | `04_spread_of_broad_listening_in_japan.md` | 2026-04-01 | `e3aa55a` | Reviewed (good) |
| ch04_01_takahiro_anno_initiatives | `04_01_takahiro_anno_initiatives.md` | 2026-04-02 | `3c85f5f` | Reviewed (good) |
| ch04_02_dpfp_parliamentary_questions | `04_02_dpfp_parliamentary_questions.md` | 2026-04-02 | `80d4912` | Reviewed (good) |
| ch04_03_ntv_election_special | `04_03_sumino_ntv_election_special.md` | 2026-04-02 | `01b2e1e` | Reviewed (good) |
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

## Image Review Log

| Section | Image | Status | Notes |
|---|---|---|---|
| ch01 | `01_broadlistening_three_types_en.png` | GOOD | Approved |
| ch01 | `01_jukugi_minshushugi_keifu_en.png` | NEEDS-WORK | Still not acceptable; requires further image cleanup/rework |
| ch01 | `01_broadlistening.png` | GOOD | Approved |
| ch01 | `01_anno_zyukugi_cycle_en.png` | PENDING REVIEW | Updated with a new English image; needs review |
| ch02 | `02_noisy_minority_en.png` | GOOD | Approved |
| ch02_column | `02_political_wordcloud.png` | GOOD | Approved |
| ch02_column | `02_rashomon_wordcloud.png` | GOOD | Approved |
| ch03 | `column/tool_double_diamond.png` | NEEDS-WORK | Third image in Chapter 3 did not pass review; requires further rework |
| ch04_01 | `04_01_broadlistening_concept.png` | GOOD | Approved |
| ch04_01 | `04_01_kiku-migaku-tsutaeru_en.png` | GOOD | Approved |
| ch04_01 | `04_01_anonymous_opinion_scatter_en.png` | GOOD | Approved |
| ch04_01 | `04_01_fullscreen_map.png` | GOOD | Approved |
| ch04_01 | `04_01_cluster_detail_en.png` | GOOD | Approved |
| ch04_01 | `04_01_comment_detail_en.png` | GOOD | Approved |
| ch04_02 | `04_02_kokumin_tttc_sanpuzu.png` | GOOD | Approved |
| ch04_02 | `04_02_kokumin_broadlistening_hikaku_en.png` | GOOD | Approved |
| ch04_02 | `04_02_kokumin_ai_process_en.png` | GOOD | Approved |
| ch04_03 | `ntv_scatter.png` | GOOD | Approved |
| ch04_03 | `04_03_ntv_cluster_example_en.png` | GOOD | Approved |
