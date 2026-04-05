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
| ch06_04_democratic_party_for_the_people | `06_04_democratic_party_for_the_people.md` | 2026-04-02 | `3cccb0b` | Reviewed (good) |
| ch06_05_komeito | `06_05_komeito.md` | 2026-04-02 | `3cccb0b` | Reviewed (good; all images approved) |
| ch07_local_elections_intro | `07_use_in_local_elections.md` | 2026-04-02 | `49afeb5` | Reviewed (good) |
| ch07_02_ryosuke_idei_case | `07_02_ryosuke_idei_case.md` | 2026-04-02 | `5140272` | Reviewed (good; all images approved) |
| ch07_03_saisei_no_michi_kazuya_obanayama | `07_03_saisei_no_michi_kazuya_obanayama.md` | 2026-04-02 | `3c85f5f` | Reviewed (good; all images approved) |
| ch08_municipalities_intro | `08_use_in_local_governments.md` | 2026-04-02 | `49afeb5` | Reviewed (good) |
| ch08_01_ota_city_jibungotoka_meeting | `08_01_ota_city_jibungotoka_meeting.md` | 2026-04-02 | `215b438` | Reviewed (good; image review pending) |
| ch08_02_hiroshima_case | `08_02_hiroshima_case.md` | 2026-04-02 | `b373b1b` | Reviewed (good; image review pending) |
| ch09_enterprise_and_nonprofits_intro | `09_use_in_companies_and_npos.md` | 2026-04-02 | `49afeb5` | Reviewed (good) |
| ch09_01_altius_link_interview | `09_01_altius_link_interview.md` | 2026-04-02 | `e052afc` | Reviewed (good; all images approved) |
| ch09_02_cybozu | `09_02_cybozu.md` | 2026-04-02 | `e3aa55a` | Reviewed (good; images acceptable) |
| ch09_column_testing_kocho_ai_through_review | `column/testing_kocho_ai_through_review.md` | 2026-04-02 | `566736c` | Reviewed (passed) |
| ch10_broadlistening_business_intro | `10_broad_listening_as_a_business.md` | 2026-04-02 | `e3aa55a` | Reviewed (passed) |
| ch10_00_dd2030_kocho_ai_development | `10_00_dd2030_kocho_ai_development.md` | 2026-04-02 | `e3aa55a` | Reviewed (good; one image should be translated) |
| ch10_01_boots_inc | `10_01_boots_inc.md` | 2026-04-03 | `e3aa55a` | Reviewed (passed) |
| ch10_02_code_for_japan | `10_02_code_for_japan.md` | 2026-04-03 | `e3aa55a` | Reviewed (passed; file is still a placeholder) |
| ch10_04_democracy_x | `10_04_democracy_x.md` | 2026-04-03 | `e3aa55a` | Reviewed (passed) |
| ch10_05_litela_kai_tanaka | `10_05_litela_kai_tanaka.md` | 2026-04-03 | `e3aa55a` | Reviewed (passed; fourth image should be translated) |
| ch10_column_lessons_from_collecting_10000_voices | `column/lessons_from_collecting_10000_voices.md` | 2026-04-03 | `a05ec08` | Reviewed (passed; all images approved) |
| ch10_column_fujitsu_enterprise_ai_for_public_comments | `column/fujitsu_enterprise_ai_for_public_comments.md` | 2026-04-03 | `e3aa55a` | Reviewed (passed) |
| ch10_broadlistening_business_remaining | `10_03_plural_reality.md` | — | — | Not reviewed |
| ch11_global_broad_listening_trends | `11_global_broad_listening_trends.md` | 2026-04-03 | `e3aa55a` | Reviewed (looks good) |
| ch11_01_taiwan | `11_01_taiwan.md` | 2026-04-04 | `88a7270` | Reviewed (passed) |
| ch11_02_birth_of_polis | `11_02_birth_of_polis.md` | 2026-04-04 | `e063c72` | Reviewed (passed) |
| ch11_03_bowling_green | `11_03_bowling_green.md` | 2026-04-04 | `4036eb2` | Reviewed (passed; all images approved) |
| ch11_broadlistening_overseas | `11_04_israel_palestine_remesh_case.md`, `11_05_harnessing_connective_action.md` | — | — | Not reviewed |
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
| ch10_00 | `10_kouchouai_technical_genealogy.png` | NEEDS-WORK | Text review passed, but the figure should be translated into English |
| ch06_05 | `06_05_WeConnect_workflow.jpg` | GOOD | Approved |
| ch06_05 | `06_05_WeConnect_wordcloud.png` | GOOD | Approved |
| ch06_05 | `06_05_WeConnect_policy_issues.png` | GOOD | Approved |
| ch06_05 | `06_05_WeConnect_age_policy.png` | GOOD | Approved |
| ch06_05 | `06_05_WeConnect_survey2.png` | GOOD | Approved |
| ch06_05 | `06_05_WeConnect_gamma.png` | GOOD | Approved |
| ch07_02 | `07_02_いでい_広聴AI意見クラスタ.png` | GOOD | Approved |
| ch07_03 | `07_03_flow_chart.png` | GOOD | Approved |
| ch08_01 | `08_01_ota_jibungotoka_overview.jpeg` | PENDING REVIEW | Text reviewed; image approval not yet recorded |
| ch08_01 | `08_01_ota_baisoku_ui.png` | PENDING REVIEW | Text reviewed; image approval not yet recorded |
| ch08_01 | `08_01_ota_response_visualization.png` | PENDING REVIEW | Text reviewed; image approval not yet recorded |
| ch08_01 | `08_01_ota_jibungotoka_smartphone.png` | PENDING REVIEW | Text reviewed; image approval not yet recorded |
| ch08_01 | `08_01_ota_analysis_report_intro.png` | PENDING REVIEW | Text reviewed; image approval not yet recorded |
| ch08_01 | `08_01_ota_issue_extraction.png` | PENDING REVIEW | Text reviewed; image approval not yet recorded |
| ch08_01 | `08_01_ota_alignment_high.png` | PENDING REVIEW | Text reviewed; image approval not yet recorded |
| ch08_01 | `08_01_ota_alignment_low.png` | PENDING REVIEW | Text reviewed; image approval not yet recorded |
| ch08_01 | `08_01_ota_alignment_uncertainty.png` | PENDING REVIEW | Text reviewed; image approval not yet recorded |
| ch08_01 | `08_01_ota_sensemaker_high_agreement.png` | PENDING REVIEW | Text reviewed; image approval not yet recorded |
| ch08_01 | `08_01_ota_survey_satisfaction.png` | PENDING REVIEW | Text reviewed; image approval not yet recorded |
| ch08_01 | `08_01_ota_survey_safety.png` | PENDING REVIEW | Text reviewed; image approval not yet recorded |
| ch08_01 | `08_01_ota_survey_wordcloud.png` | PENDING REVIEW | Text reviewed; image approval not yet recorded |
| ch08_01 | `08_01_ota_sensemaker_overview.png` | PENDING REVIEW | Text reviewed; image approval not yet recorded |
| ch08_02 | `08_02_hiroshima_broadlistening_result.png` | PENDING REVIEW | Text reviewed; image approval not yet recorded |
| ch09_01 | `09_広聴AI_入力用構造化データ.png` | GOOD | Approved |
| ch09_01 | `09_広聴AI_散布図.png` | GOOD | Approved |
| ch09_01 | `09_広聴AI_クラスタ名-説明.png` | GOOD | Approved |
| ch09_01 | `09_BI画像_モザイク無し.png` | GOOD | Approved |
| ch09_02 | `10_03_cybozu_workshop.jpg` | GOOD | Approved |
| ch09_02 | `10_03_cybozu_fusennwork.jpg` | GOOD | Approved |
| ch09_02 | `10_03_cybozu_idobata_pc.jpg` | GOOD | Approved |
| ch09_02 | `09_03_shirokuro_kaigi_remote_work_debate.png` | GOOD | Approved |
| ch09_02 | `09_03_shirokuro_kaigi_youtube_comments.png` | GOOD | Approved |
| ch10_05 | `08_01_ota_facilitator_feedback.png` | GOOD | Approved |
| ch10_05 | `10_05_outward_visualization.png` | GOOD | Approved |
| ch10_05 | `10_05_recogra2.png` | GOOD | Approved |
| ch10_05 | `10_05_tawaramoto_flow.png` | NEEDS-WORK | Acceptable image, but should be translated into English |
| ch10_05 | `10_05_tomioka_illustration.png` | GOOD | Approved |
| ch10_column | `column_ai_anno_results.png` | GOOD | Approved |
| ch10_column | `column_idobata_concept.png` | GOOD | Approved |
| ch10_column | `column_baisoku_input.png` | GOOD | Approved |
| ch10_column | `column_baisoku_report.png` | GOOD | Approved |
| ch11_03 | `column_bg2050_stats.png` | GOOD | Approved |
| ch11_03 | `column_bg2050_topics.png` | GOOD | Approved |
| ch11_03 | `column_bg2050_topic_detail.png` | GOOD | Approved |
| ch11_03 | `column_bg2050_consensus.png` | GOOD | Approved |
| ch04_05 | `04_04_消費税減税SNS散布図.png` | MISSING | Referenced in `04_05_asahi_special_feature.md` but not present in `images/`; broken in generated HTML |
| ch04_05 | `04_04_参院選SNS意見分布.png` | MISSING | Referenced in `04_05_asahi_special_feature.md` but not present in `images/`; broken in generated HTML |
| ch04_05 | `04_04_参院選投票日直前SNS意見分布.png` | MISSING | Referenced in `04_05_asahi_special_feature.md` but not present in `images/`; broken in generated HTML |
| ch04_05 | `04_04_万博SNS分析_前期.png` | MISSING | Referenced in `04_05_asahi_special_feature.md` but not present in `images/`; broken in generated HTML |
| ch04_05 | `04_04_万博SNS分析_後期.png` | MISSING | Referenced in `04_05_asahi_special_feature.md` but not present in `images/`; broken in generated HTML |
