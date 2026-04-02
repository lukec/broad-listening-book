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

- **Team Mirai**: Keep as **Team Mirai** in the English edition.
- First mention format: `Team Mirai (meaning “Team Future”)`.
- After the first mention in each chapter, continue using **Team Mirai**.
- **Bluesky**: In Chapter 2, add **Bluesky** after **Facebook** as an editorial choice for English audiences.

## Open Tasks

- TODO: Ensure every image in the English edition uses descriptive alt text beginning with `Figure: `. This is especially important for images that remain untranslated, where the alt text must clearly describe the figure's content in English.

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
| ch04_04_mapping_public_opinion_with_polis | `04_04_mapping_public_opinion_with_polis.md` | 2026-04-02 | `4adaddf` | Reviewed (good) |
| ch04_05_asahi_special_feature | `04_05_asahi_special_feature.md` | 2026-04-02 | `3cccb0b` | Reviewed (good; footnote 13 inaccurate, missing images tracked below) |
| ch05_tokyo_shin_tokyo_2050 | `05_tokyo_shin_tokyo_2050_policy_shift.md` | 2026-04-02 | `3c85f5f` | Reviewed (excellent; Conway part amazing) |
| ch06_national_elections_intro | `06_broad_listening_in_national_elections.md` | 2026-04-02 | `abd2321` | Reviewed (good) |
| ch06_01_team_mirai | `06_01_team_mirai.md` | 2026-04-02 | `4adaddf` | Reviewed (excellent; all images good) |
| ch06_02_team_mirai_2026_lower_house | `06_02_team_mirai_2026_house_of_representatives_election.md` | 2026-04-02 | `4e6c35c` | Reviewed (really good; all images approved) |
| ch06_03_nippon_ishin_no_kai | `06_03_nippon_ishin_no_kai.md` | 2026-04-02 | `3cccb0b` | Reviewed (good; all images approved) |
| ch06_04_democratic_party_for_the_people | `06_04_democratic_party_for_the_people.md` | — | — | Not reviewed |
| ch06_05_komeito | `06_05_komeito.md` | — | — | Not reviewed |
| ch07_local_elections | `07_use_in_local_elections.md`, `07_02_ryosuke_idei_case.md`, `07_03_saisei_no_michi_kazuya_obanayama.md` | — | — | Not reviewed |
| ch08_municipalities | `08_use_in_local_governments.md`, `08_01_ota_city_jibungotoka_meeting.md`, `08_02_hiroshima_case.md` | — | — | Not reviewed |
| ch09_enterprise_and_npo | `09_use_in_companies_and_npos.md`, `09_01_altius_link_interview.md`, `09_02_cybozu.md`, `column/testing_kocho_ai_through_review.md` | — | — | Not reviewed |
| ch10_broadlistening_business | `10_broad_listening_as_a_business.md`, `10_00_dd2030_kocho_ai_development.md`, `10_01_boots_inc.md`, `10_02_code_for_japan.md`, `10_03_plural_reality.md`, `10_04_democracy_x.md`, `10_05_litela_kai_tanaka.md`, `column/lessons_from_collecting_10000_voices.md`, `column/fujitsu_enterprise_ai_for_public_comments.md` | — | — | Not reviewed |
| ch11_broadlistening_overseas | `11_global_broad_listening_trends.md`, `11_01_taiwan.md`, `11_02_birth_of_polis.md`, `11_03_bowling_green.md`, `11_04_israel_palestine_remesh_case.md`, `11_05_harnessing_connective_action.md` | — | — | Not reviewed |
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
| ch04_04 | `04_04_polis_party_icons.png` | GOOD | Approved |
| ch04_04 | `04_04_polis_economic_map.png` | GOOD | Approved |
| ch05 | `05_tttc_all_clusters.png` | GOOD | Approved |
| ch05 | `05_shintokyo_2050_result.png` | GOOD | Approved |
| ch05 | `05_tokyo_2040_2021.png` | GOOD | Approved |
| ch05 | `05_tokyo_2040_2024.png` | GOOD | Approved |
| ch05 | `05_tttc_tourism.png` | GOOD | Approved |
| ch05 | `05_cluster_mapping_zure.png` | GOOD | Approved for now; may still be replaced later |
| ch06_01 | `06_01_tokyo_gov_manifesto.png` | GOOD | Approved |
| ch06_01 | `06_01_three_projects.png` | GOOD | Approved |
| ch06_01 | `06_01_manifesto_flow_en.png` | GOOD | Approved |
| ch06_01 | `06_01_pr_overview.png` | GOOD | Approved |
| ch06_01 | `06_01_opinion_flow_en.png` | GOOD | Approved |
| ch06_01 | `06_01_idobata_chat_structure.png` | GOOD | Approved |
| ch06_02 | `06_02_team_mirai_manifesto_top.png` | GOOD | Approved |
| ch06_02 | `06_02_quick_reply.png` | GOOD | Approved |
| ch06_02 | `06_02_topic_example.png` | GOOD | Approved |
| ch06_02 | `06_02_proposal_list.png` | GOOD | Approved |
| ch06_03 | `06_03_吉村代表X投稿.png` | GOOD | Approved |
| ch06_03 | `06_03_ishin_scatter_may.png` | GOOD | Approved |
| ch06_03 | `06_03_ishin_scatter_june.png` | GOOD | Approved |
| ch06_03 | `06_03_ishin_brolis_cluster_detail.png` | GOOD | Approved |
| ch04_05 | `04_04_消費税減税SNS散布図.png` | MISSING | Referenced in `04_05_asahi_special_feature.md` but not present in `images/`; broken in generated HTML |
| ch04_05 | `04_04_参院選SNS意見分布.png` | MISSING | Referenced in `04_05_asahi_special_feature.md` but not present in `images/`; broken in generated HTML |
| ch04_05 | `04_04_参院選投票日直前SNS意見分布.png` | MISSING | Referenced in `04_05_asahi_special_feature.md` but not present in `images/`; broken in generated HTML |
| ch04_05 | `04_04_万博SNS分析_前期.png` | MISSING | Referenced in `04_05_asahi_special_feature.md` but not present in `images/`; broken in generated HTML |
| ch04_05 | `04_04_万博SNS分析_後期.png` | MISSING | Referenced in `04_05_asahi_special_feature.md` but not present in `images/`; broken in generated HTML |
