# Output Data Dictionary

This document explains the core CSV and JSON outputs under `outputs/`. Its purpose is to prevent reviewers and independent reproducers from misreading file names or column names. Every output is generated from public election files, official NEC election-statistics HTML cache files, or reproducible scripts that process those materials.

## Common Terms

| Term | Meaning |
| --- | --- |
| Counting unit | The official result unit treated as one analytical row, usually an eup, myeon, dong, or comparable official counting-result unit. |
| In-district early voting | Early votes cast by voters inside their registered election district. |
| Out-of-district early voting | Early votes cast by voters outside their registered election district. |
| Actual first- and second-place candidates | The top two candidates determined by total votes within the same election, contest, and vote-type group, not necessarily the first two candidates listed in the file. |
| Vote pair | The ordered pair consisting of the actual first-place candidate's vote count and the actual second-place candidate's vote count. |
| Identical vote pair | A case where two different counting units have the same first-place candidate vote count and the same second-place candidate vote count simultaneously. |
| `collision_pairs` | The number of pairwise counting-unit collisions. If the same value appears in three units, it creates three pairwise collisions. |
| `duplicate_groups` | The number of repeated vote-pair value groups. If the same value appears in three units, it is still one duplicate group. |

## Core Outputs

| File | Row unit | Role in the paper | Key columns |
| --- | --- | --- | --- |
| `outputs/dataset_counts.csv` | One source file or election dataset | Confirms the size of historical baseline data from 2014 through 2025. | `dataset`, `rows` |
| `outputs/duplicate_summary.csv` | Election, office category, and vote-type group | Broad summary of the duplicate search. | `election`, `category`, `vote_class`, `units`, `top2_duplicate_groups`, `top2_duplicate_units` |
| `outputs/duplicate_groups.csv` | One repeated vote signature group | Shows where repeated groups occur by election and vote type. | `signature_type`, `election`, `category`, `contest`, `vote_class`, `signature`, `duplicate_units` |
| `outputs/duplicate_examples.csv` | One counting unit inside a duplicate group | Identifies concrete units and candidate names inside duplicate groups. | `signature_type`, `unit`, `candidate_names` |
| `outputs/governor_actual_top2_summary.csv` | One-row summary of the historical governor baseline | Core historical benchmark for the Gwangju-Jeonnam five-pair test. | `governor_contests`, `comparison_pairs`, `collision_pairs`, `duplicate_groups`, `max_duplicate_groups_in_contest`, `khat`, `n_for_probability`, `p_at_least_5` |
| `outputs/governor_actual_top2_by_contest.csv` | One historical governor contest | Checks duplicate counts across the 51 historical governor contests. | `election`, `contest`, `units`, `comparison_pairs`, `duplicate_groups`, `collision_pairs`, `candidate_1`, `candidate_2` |
| `outputs/governor_actual_top2_duplicates.csv` | One historical governor identical vote-pair group | Lists actual historical duplicate pairs and verifies the historical maximum. | `election`, `contest`, `candidate_1`, `candidate_2`, `signature`, `duplicate_units`, `collision_pairs` |
| `outputs/governor_bootstrap_summary.csv` | One resampling condition | Checks how often five or more pairs occur when sampling without replacement from historical actual vote pairs. | `sample_size`, `trials`, `threshold`, `exceedances`, `probability`, `rule_of_three_upper_95` |
| `outputs/governor_bootstrap_histogram.csv` | One observed duplicate-group count in resampling | Shows the shape of the resampling distribution. | `duplicate_groups`, `trials`, `share` |
| `outputs/probability_core.csv` | One probability scenario | Main Poisson-approximation probability table. | `n`, `k_space`, `threshold`, `lambda`, `probability`, `probability_percent`, `reciprocal` |
| `outputs/probability_exact_collision.csv` | One exact pair-collision scenario | Recomputes the same question as the Poisson approximation using an exact birthday-problem dynamic program. | `n`, `k_space`, `threshold`, `poisson_probability`, `exact_probability`, `exact_probability_percent`, `poisson_minus_exact`, `exact_reciprocal` |
| `outputs/probability_k_sensitivity.csv` | One effective pair-space assumption | Sensitivity analysis for changes in `K`. | `k_space`, `threshold`, `probability_percent`, `reciprocal` |
| `outputs/probability_n_sensitivity.csv` | One counting-unit count assumption | Sensitivity analysis for changes in `N`. | `n`, `threshold`, `probability_percent`, `reciprocal` |
| `outputs/nec_2026_gwangju_jeonnam_units.csv` | One 2026 Gwangju or Jeonnam in-district early-vote counting unit | Official-HTML basis for `N=393`. | `city`, `town`, `unit`, `vote_class`, `electors`, `turnout`, `source_file` |
| `outputs/nec_2026_gwangju_jeonnam_unit_counts.csv` | One city/town grouping | Counts Gwangju and Jeonnam in-district early-vote units. | `city`, `town`, `in_district_early_units`, `source_url` |
| `outputs/nec_2026_gwangju_jeonnam_unit_summary.json` | JSON summary | Summarizes the 2026 Gwangju-Jeonnam unit count and links output files. | `regions`, `towns`, `in_district_early_units`, `output_counts`, `output_units` |
| `outputs/nec_2026_reported_duplicate_cases.csv` | One 2026 event row | Checks whether the twelve event rows are reproduced from official HTML. | `pair_id`, `city`, `town`, `unit`, `candidate_1_votes`, `candidate_2_votes`, `electors`, `turnout`, `source_url` |
| `outputs/nec_2026_reported_duplicate_pairs.csv` | One 2026 identical vote pair | Checks whether the twelve event rows form six identical pairs. | `pair_id`, `candidate_1`, `candidate_1_votes`, `candidate_2`, `candidate_2_votes`, `units` |
| `outputs/nec_2026_fetch_manifest.json` | JSON metadata | Documents 2026 official HTML extraction settings and event counts. | `source`, `election_id`, `election_code`, `case_rows`, `duplicate_pairs`, `towns` |
| `outputs/songdo_official_rows.csv` | One Songdo counting unit | Compares final public values for Songdo 1-dong and Songdo 2-dong. | `unit`, `candidate_1_votes`, `candidate_2_votes`, `electors`, `turnout`, `invalid_votes`, `abstentions` |
| `outputs/songdo_probability_summary.csv` | One Songdo probability scenario | Calculates Songdo as a separate auxiliary audit signal. | `case`, `n_units`, `comparison_pairs`, `k_space`, `probability_percent`, `reciprocal` |
| `outputs/early_day_assembly_summary.csv` | One National Assembly election | Summarizes the auxiliary early-vote versus election-day vote-share pattern. | `election`, `districts`, `mean_early_minus_day_pp`, `dem_early_higher_count`, `sign_test_p_one_sided`, `max_abs_z` |
| `outputs/early_day_assembly_twoparty.csv` | One National Assembly constituency | Shows two-party Democratic-versus-conservative early/election-day vote-share differences by constituency. | `election`, `sido`, `district`, `early_dem_share`, `day_dem_share`, `early_minus_day_pp`, `z` |
| `outputs/core_claims_verification.csv` | One core verification claim | Spreadsheet-readable list of the 45 core values checked by `verify_core_claims.py`. | `claim`, `expected`, `actual`, `abs_tol`, `status` |
| `outputs/core_claims_verification.json` | JSON verification summary | Machine-readable verification result for the same 45 core values. | `status`, `check_count`, `scope`, `checks` |
| `outputs/pre_submission_audit.csv` | One pre-submission audit row | Spreadsheet-readable checks of final checklist completion, forbidden wording, privacy scan, English PDF/source translation, evidence-matrix reference, and core verification status. | `check`, `expected`, `actual`, `status` |
| `outputs/pre_submission_audit.json` | JSON audit summary | Machine-readable result of the 10 pre-submission audit checks. | `status`, `check_count`, `scope`, `checks` |
| `outputs/submission_integrity_report.md` | One integrity report | Human-readable final integrity summary for PDFs, core checks, audit checks, and key reproducible numbers. | Markdown sections |
| `outputs/submission_integrity_report.json` | JSON integrity report | Machine-readable final integrity summary excluding the final ZIP self-hash. | `status`, `core_claims_check_count`, `pre_submission_audit_check_count`, `korean_pdf`, `english_pdf`, `key_claims` |
| `outputs/checksums_sha256.csv` | One package file | Verifies integrity of submission-package files. | `path`, `bytes`, `sha256` |
| `dist/election_duplicate_ieie_submission.zip.sha256` | One submission ZIP | SHA256 sidecar for the submission ZIP itself. | `sha256  filename` |
| `dist/election_duplicate_ieie_submission_manifest.json` | JSON submission ZIP summary | Verifies the ZIP file's byte size, SHA256, and internal file count. | `package`, `bytes`, `sha256`, `file_count` |

## Column Interpretation Notes

1. `units` means the number of included counting units, not the number of voters.
2. `comparison_pairs` means the number of pairwise comparisons among counting units, generally `N(N-1)/2`.
3. `duplicate_groups` and `collision_pairs` are different. The first counts repeated value groups; the second counts actual pairwise unit collisions.
4. `khat` is not a natural constant. It is an empirical effective vote-pair space reverse-estimated from historical governor data.
5. `probability_percent` is `probability` multiplied by 100.
6. `sign_test_p_one_sided` is a simple sign-test value for one-directional early-vote advantage. It does not remove alternative explanations such as voter self-selection.

## Reproducible Claims and Corresponding Files

| Reproducible claim | Files to inspect |
| --- | --- |
| The twelve 2026 event rows are reproduced from official HTML. | `outputs/nec_2026_reported_duplicate_cases.csv`, `outputs/nec_2026_fetch_manifest.json` |
| The twelve event rows form six identical vote pairs. | `outputs/nec_2026_reported_duplicate_pairs.csv` |
| The Gwangju-Jeonnam in-district early-vote counting-unit count is 393. | `outputs/nec_2026_gwangju_jeonnam_units.csv`, `outputs/nec_2026_gwangju_jeonnam_unit_summary.json` |
| Across 51 historical governor contests, the maximum identical-pair count inside one contest is three. | `outputs/governor_actual_top2_summary.csv`, `outputs/governor_actual_top2_by_contest.csv`, `outputs/governor_actual_top2_duplicates.csv` |
| The Poisson approximation for five or more Gwangju-Jeonnam pairs is about 0.115%. | `outputs/probability_core.csv`, `outputs/governor_actual_top2_summary.csv` |
| The exact pair-collision probability under the same baseline is about 0.122%. | `outputs/probability_exact_collision.csv` |
| Historical actual-pair resampling produces zero five-or-more-pair trials in 200,000 trials. | `outputs/governor_bootstrap_summary.csv`, `outputs/governor_bootstrap_histogram.csv` |
| Songdo is a separate auxiliary audit signal, not part of the Gwangju-Jeonnam core test. | `outputs/songdo_official_rows.csv`, `outputs/songdo_probability_summary.csv` |
| In 2020 and 2024, every analyzable National Assembly constituency shows the same early-vote directional pattern. | `outputs/early_day_assembly_summary.csv`, `outputs/early_day_assembly_twoparty.csv` |
| The 45 core numerical claims in the manuscript match the current outputs. | `outputs/core_claims_verification.csv`, `outputs/core_claims_verification.json` |
| The final pre-submission audit checks pass. | `outputs/pre_submission_audit.csv`, `outputs/pre_submission_audit.json` |
| The final PDF and submission integrity summary are internally consistent. | `outputs/submission_integrity_report.md`, `outputs/submission_integrity_report.json` |
| The submission ZIP's SHA256 and internal file count are verified. | `dist/election_duplicate_ieie_submission.zip.sha256`, `dist/election_duplicate_ieie_submission_manifest.json` |

## Boundary Important for Reviewers

This data dictionary clarifies output meaning; it is not a causal finding document. The listed files are sufficient to reproduce the statistical anomaly and audit trigger. A legal conclusion about a specific act still requires original counting statements, first-pass sorter results, candidate-level reviewed-ballot allocation, and input/correction logs.
