# Evidence Matrix

## Purpose

This document separates the paper's main claims, the reproducible files supporting each claim, and the raw records still needed for causal or legal conclusions. It is intended as a quick cross-check for reviewers who ask: which claim is verified by which file?

## Evidence by Core Claim

| No. | Claim | Current evidence | Reproduction or check file | Current strength |
| ---: | --- | --- | --- | --- |
| 1 | The twelve 2026 event rows are reproducible from official NEC election-statistics page values. | Cached HTML and parsed CSV outputs match. | `data/nec_2026_official_html/`, `outputs/nec_2026_reported_duplicate_cases.csv` | Strong |
| 2 | The 2026 event rows form six identical top-two vote pairs. | Candidate vote-pair values group into two-unit identical pairs. | `outputs/nec_2026_reported_duplicate_pairs.csv` | Strong |
| 3 | Across 51 historical governor in-district early-vote contests, the maximum repeated-pair count within one contest is three. | Confirmed under the actual top-two candidate rule for the 2014, 2018, and 2022 local elections. | `outputs/governor_actual_top2_summary.csv`, `outputs/governor_actual_top2_by_contest.csv` | Strong |
| 4 | The historical benchmark contains no contest with five or more repeated pairs. | The contest-level duplicate count has maximum value three. | `outputs/governor_actual_top2_by_contest.csv` | Strong |
| 5 | At \(N=393, K=100,944.8\), \(P(C \geq 5)\) is about 0.115%. | Reproduced by the Poisson-approximation calculation. | `outputs/probability_core.csv` | Model-dependent but reproducible |
| 6 | Even with a conservative \(K=50,000\), \(P(C \geq 5)\) is about 2.05%. | Confirmed by effective-pair-space sensitivity analysis. | `outputs/probability_k_sensitivity.csv` | Model-dependent but reproducible |
| 7 | Even with \(N=450\), \(P(C \geq 5)\) remains below 0.4%. | Confirmed by counting-unit sensitivity analysis. | `outputs/probability_n_sensitivity.csv` | Model-dependent but reproducible |
| 8 | The conditional probability that the specific Songdo 1-dong and Songdo 2-dong units share the same top-two vote pair is about 0.000991%. | Calculated from the Yeonsu official HTML and the \(K=100,944.8\) baseline. | `outputs/songdo_probability_summary.csv`, `outputs/songdo_official_rows.csv` | Auxiliary audit signal |
| 9 | In 200,000 nonparametric samples from historical governor actual vote pairs, \(C \geq 5\) occurs zero times, with a rule-of-three 95% upper bound near 0.0015%. | Fixed-seed resampling result. | `outputs/governor_bootstrap_summary.csv`, `outputs/governor_bootstrap_histogram.csv` | Empirical robustness check |
| 10 | In the 2020 and 2024 National Assembly elections, the Democratic candidate's early-vote two-party share is higher than the election-day share in every analyzable constituency. | Confirmed from official National Assembly counting files. | `outputs/early_day_assembly_summary.csv`, `outputs/early_day_assembly_twoparty.csv` | Strong for direction; causal interpretation separate |

## Claims Not Established by Current Public Data Alone

| Claim | Current status | Additional records needed |
| --- | --- | --- |
| A specific actor or institution intentionally produced the vote values. | Not established by current public data. | Investigation or audit records, operator/time logs, original counting statements |
| The identical vote pairs were created during reviewed-ballot allocation. | A strong audit question in the Songdo case; still requires raw records for Gwangju-Jeonnam. | First-pass sorter results, reviewed-ballot candidate allocation records |
| A display or information-system error caused the equality. | Possible cause, not confirmed. | Public-system database source, original counting statements, log comparison |
| Voter self-selection alone explains all early-vote/election-day differences. | Possible, but not established by the sign test alone. | Age, gender, geography, party mobilization, early-vote encouragement, in-district/out-of-district split analyses |

## Raw-Data Audit Decision Table

| Raw record | Result weakening the ordinary-chance explanation | Result restoring the ordinary-chance or administrative explanation |
| --- | --- | --- |
| Original counting statements | They also show the twelve event rows and six identical pairs. | Original values differ from page values and the identical pairs disappear. |
| First-pass sorter outputs | First-pass values differ, but reviewed/combined totals become identical. | First-pass through final values are independently consistent. |
| Reviewed-ballot candidate allocation | Same-direction candidate adjustments recur across multiple pairs. | Reviewed-ballot allocation is unrelated to the final identical pairs. |
| Data-entry logs | Unusual correction or re-entry patterns concentrate around event rows. | Logs are chronological, internally consistent, and show no relevant corrections. |
| In-district/out-of-district split data | Identical-pair repetition concentrates in in-district early voting. | Comparable repetition appears in out-of-district and election-day rows as well. |
| Ballot-box and counting-batch chain-of-custody records | Affected batches concentrate in the same equipment, timestamp, review table, or batch flow. | Batch movement and handling are independent, chronological, and fully reconciled. |

## Submission-Ready Conclusion

The strongest conclusion supported by the current package is:

> Taken together, the NEC official page values and the historical official-data baseline indicate that the 2026 Gwangju-Jeonnam five-pair repetition is a statistical anomaly difficult to reconcile with the ordinary-randomness hypothesis, and it cannot be statistically closed without independent verification of original counting statements and first-pass sorter records.

This is not a sentence legally determining a specific cause. It is a reproducible statistical statement supporting public raw-data audit.
