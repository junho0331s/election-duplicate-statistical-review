# Reviewer Objection Response Memo

## Purpose

This memo anticipates the strongest objections to the paper, *Repeated Identical In-District Early-Vote Pairs That Overwhelm the Random-Chance Hypothesis*, and states which claims remain supported after each objection is applied. The purpose is not to make the result sound stronger than the evidence allows. The purpose is to preserve a defensible boundary: the current package supports a statistical audit trigger, not a final legal attribution of cause.

## Claim Strength Tiers

The paper's claims are divided into four tiers.

| Tier | Proposition | Current evidentiary status |
| --- | --- | --- |
| A | The twelve 2026 event rows and six identical vote pairs are reproducible from official NEC election-statistics HTML pages. | Verified by cached HTML and reproduction scripts |
| B | The Gwangju-Jeonnam five-pair cluster exceeds the historical maximum of three pairs observed in past governor in-district early-vote contests. | Verified from 51 constituency contests in 2014, 2018, and 2022 |
| C | Under the empirical baseline and Poisson approximation, five or more Gwangju-Jeonnam pairs is rare, about 0.115% at \(N=393, K=100,944.8\). | Reproducible from `outputs/probability_core.csv` |
| D | The event is a statistical anomaly requiring raw-data disclosure and independent audit. | Supported by A through C |

The paper does not prove, from the currently public data alone, that a specific actor, procedure, machine, or input step intentionally produced the result. Its strongest conclusion is tier D.

## Key Numerical Claims

| Item | Value | Reproduction file |
| --- | ---: | --- |
| Historical counting-unit rows | 81,701 | `outputs/dataset_counts.csv` |
| Governor constituency contests | 51 | `outputs/governor_actual_top2_summary.csv` |
| Actual top-two comparison pairs | 1,514,172 | `outputs/governor_actual_top2_summary.csv` |
| Historical identical vote pairs | 15 | `outputs/governor_actual_top2_summary.csv` |
| Historical maximum within one contest | 3 pairs | `outputs/governor_actual_top2_by_contest.csv` |
| 2026 official-page event rows | 12 | `outputs/nec_2026_reported_duplicate_cases.csv` |
| 2026 official-page identical pairs | 6 pairs | `outputs/nec_2026_reported_duplicate_pairs.csv` |
| \(P(C \geq 5)\), \(N=393, K=100,944.8\) | 0.115% | `outputs/probability_core.csv` |
| Conditional probability that all five Gwangju-Jeonnam pairings match when treated as pre-designated pairings | \(9.54\times10^{-26}\), about one in \(1.05\times10^{25}\) | `outputs/probability_designated_pairs.csv` |
| \(P(C \geq 5)\), \(N=450, K=100,944.8\) | 0.367% | `outputs/probability_n_sensitivity.csv` |
| \(P(C \geq 5)\), \(N=393, K=50,000\) | 2.055% | `outputs/probability_k_sensitivity.csv` |
| Conditional probability for the specific Songdo 1/Songdo 2 pair | 0.000991% | `outputs/songdo_probability_summary.csv` |
| Nonparametric resampling, 200,000 trials, \(C \geq 5\) | 0 hits, 95% upper bound about 0.0015% | `outputs/governor_bootstrap_summary.csv` |

The important point is not one exact probability value. It is that the Gwangju-Jeonnam five-pair cluster does not become common under the conservative benchmark, sensitivity checks, or empirical resampling.

## Main Objections and Responses

### 1. "A low probability is not impossibility."

Accepted. A low probability is not impossibility. The paper therefore does not infer a final legal conclusion from the probability alone.

The claim that remains is narrower: in election-integrity review, a structured low-probability anomaly increases the burden of explanation. When repeated pairs concentrate in the same contest environment, same candidate combination, and same vote type, raw-data disclosure and independent verification are reasonable institutional responses.

### 2. "This is a post-search result found after scanning many places."

Accepted in part. If the entire nationwide set of twelve places is used as one probability event without adjustment, the post-search problem is serious.

The paper therefore places its main test on the internal Gwangju-Jeonnam five-pair cluster. That cluster is narrowly defined by the same top-two candidate pair, same in-district early-vote category, and same metropolitan/provincial governor contest environment. The nationwide set is background; it is not the main probability denominator.

### 3. "Counting-unit size and regional preference violate independent-identical assumptions."

Partly correct. Eup, myeon, and dong vote pairs are not perfect independent and identically distributed draws.

For that reason, the paper does not use an arbitrary uniform model as the sole benchmark. It infers an effective pair-space \(K\) from actual historical governor-election in-district early-vote data, reports sensitivity to \(K\) and \(N\), and performs nonparametric resampling from actual historical vote pairs. A critic who claims that regional structure fully explains the event should provide a model that generates five-pair clusters at non-negligible frequency under the same event definition.

### 4. "Including 2014 makes historical duplicates more common."

Correct. Including 2014 increases historical identical pairs from the smaller later-period count to 15 and makes the 2026 event appear less rare.

This is a conservative choice. Even after including 2014, the maximum repeated-pair count within a historical governor contest is three, and no historical contest reaches five.

### 5. "If three historical pairs occurred, why is five special?"

Because the tail probabilities are different. Under the same \(N=393, K=100,945\) benchmark, the probability of three or more pairs is about 4.23%, while the probability of five or more pairs is about 0.115%. The five-pair event is therefore roughly 37 times rarer than the three-pair event under the same model.

The paper treats three pairs as the observed historical upper bound, not as proof of misconduct. It treats five pairs as an event beyond that bound.

### 6. "Without the official integrated XLSX or original counting statements, the analysis is invalid."

The analysis is not invalid, but its conclusion is bounded.

The package reproduces the twelve event rows and six identical pairs from official NEC election-statistics HTML pages. That is stronger than relying only on a media screenshot. However, final administrative or legal judgment requires the official integrated file, original counting statements, first-pass sorter results, reviewed-ballot allocation records, and input logs.

The conclusion is therefore: the current official-page data are sufficient to require raw-data audit. They are not sufficient to end the causal inquiry.

### 7. "If 0.115% is not astronomically small, couldn't this still be chance?"

The 0.115% value is the broad primary test. It counts success whenever any unit pairing, with any repeated vote-pair value, produces five or more identical vote-pair collisions among the 393 Gwangju-Jeonnam counting units. It is therefore not the probability of the exact observed five pairings all matching. It is a conservative broad-collision probability.

If the observed five Gwangju-Jeonnam pairings are instead treated as pre-designated pairings, then under the same \(K=100,944.8\) baseline the conditional probability that all five match is \((1/K)^5 \approx 9.54\times10^{-26}\), about one in \(1.05\times10^{25}\). The paper does not mix these two values. The broad primary test is 0.115%; the designated-five-pair conditional calculation is \(9.54\times10^{-26}\). The event definitions differ, but both make the Gwangju-Jeonnam five-pair repetition difficult to dismiss as ordinary chance.

### 8. "The Songdo pair is weak because it was found in a nationwide search."

The paper does not merge Songdo into the Gwangju-Jeonnam main test. It treats Songdo as a separate auxiliary case.

For the specific Songdo 1-dong and Songdo 2-dong pair, the conditional probability under \(K=100,944.8\) is about 0.000991%. This does not prove a nationwide conclusion. It supports a narrower audit question: how did different first-pass or auxiliary counts lead to the same final top-two pair, and can the review-ballot records reconcile that process?

### 9. "Early-vote and election-day differences can arise from voter self-selection."

Yes. The paper does not use the early-vote/election-day analysis as direct proof of misconduct.

The auxiliary point is that all 236 analyzable constituencies in 2020 and all 245 analyzable constituencies in 2024 show the same direction of Democratic early-vote two-party advantage. A self-selection explanation may be correct, but it must show that age, occupation, mobility, region, party mobilization, pandemic-era behavior, and other lawful variables remove the residual pattern.

### 10. "The Poisson approximation may be inaccurate."

Possible. The Poisson approximation is a first-order rare-collision model.

The conclusion does not rest on that approximation alone. It is supported by the historical maximum of three pairs, \(K\)- and \(N\)-sensitivity checks, zero \(C \geq 5\) hits in 200,000 nonparametric resampling trials, and the reproduction of the 2026 event rows from official NEC HTML pages.

## Falsification Conditions

The paper's conclusion should be weakened or revised if any of the following is shown:

1. The official integrated 2026 file or original counting statements show that the twelve event-row values differ from the currently archived official-page values.
2. The Gwangju-Jeonnam five-pair set is not actually a repeated pattern within the same top-two candidate combination, same vote type, and same contest environment.
3. Additional official in-district early-vote governor data under the same institutional regime show many contests with five or more identical top-two pairs.
4. For all five Gwangju-Jeonnam pairs, first-pass sorter outputs, reviewed-ballot allocation records, and input logs independently reconcile the final equalities as ordinary documented counting outcomes.

These falsification conditions are included to make clear that the paper's claim is a testable statistical proposition, not an unfalsifiable political assertion.

## Raw-Data Audit Criteria

If a reviewer asks what exactly must be checked, the answer can be limited to the following table.

| Raw material | Result strengthening the paper's audit claim | Result weakening the paper's audit claim |
| --- | --- | --- |
| Original counting statements | They match the official-page values and preserve the twelve rows and six pairs. | Original values differ and the identical pairs disappear. |
| First-pass sorter outputs | First-pass values differ, but final reviewed totals become identical. | First-pass and final values are independently consistent and documented. |
| Reviewed-ballot candidate allocations | Similar candidate-direction adjustments recur across pairs. | Reviewed-ballot allocation is unrelated to the final equal pairs. |
| Data-entry and correction logs | Unusual corrections or repeated-entry patterns concentrate around event rows. | Logs are chronological, internally consistent, and show no relevant corrections. |

This table does not predetermine the conclusion. It separates what can be concluded from public data now from what can only be concluded after raw records are released.

## Post-Disclosure Decision Tree

Once raw records are disclosed, the paper's judgment should be updated by the following conditional rule. First, if the original counting statements or official integrated file differ from the current official-page values and the twelve event rows or six identical pairs disappear, the event definition should be weakened or withdrawn. Second, if the values match but first-pass sorter results, reviewed-ballot allocations, input logs, and ballot-box or counting-batch custody records are chronological, internally consistent, and document each equal-pair formation, the event should be downgraded to an administratively explained event. Third, if first-pass values differ but reviewed-ballot, input, or batch-movement steps repeatedly create equal pairs in the same candidate direction, the claim should escalate from statistical anomaly to causal-investigation stage. Fourth, if original values match but logs or batch records are missing, inconsistent, or concentrated around corrections, the event remains an object of independent audit.

This decision tree does not fix the conclusion in advance. It brings the strongest possible reviewer objection, that raw records may explain the pattern, into the study design itself. The current conclusion is therefore a statistical audit signal before raw-record disclosure; the post-disclosure conclusion depends on which of the four conditions is documented.

## Submission Wording

Recommended wording:

> Taken together, the official NEC page values and historical official-data baseline indicate that the Gwangju-Jeonnam five-pair repetition is difficult to reconcile with the ordinary-randomness hypothesis and requires independent verification of original counting statements and first-pass sorter records.

Wording to avoid:

> The current public data identify a specific actor and method.

The package's strength is not an overextended causal claim. Its strength is that public data and reproducible code narrow the issue to a strong and auditable statistical anomaly.
