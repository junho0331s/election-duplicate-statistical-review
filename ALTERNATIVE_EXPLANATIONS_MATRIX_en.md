# Alternative Explanations Evaluation Matrix

This document consolidates plausible benign explanations for the main anomaly studied in the paper. Its purpose is not to predetermine the conclusion, but to specify what each explanation can explain, what it still fails to explain, and what raw records or additional analyses would strengthen or weaken it.

The baseline conclusion of this document is narrow. The currently public materials and reproducible calculations cannot legally establish a specific cause. But benign explanations also do not prove themselves without raw records. The most defensible academic conclusion is therefore that official screen values and historical baselines define a statistical anomaly requiring independent raw-data audit.

## Evaluation Matrix

| Alternative explanation | What it can explain | What it does not explain | Required raw records or additional analysis | Assessment in this study |
| --- | --- | --- | --- | --- |
| Low-probability coincidence | It explains the general principle that rare events can occur in reality. | It does not adequately explain why the Gwangju-Jeonnam five-pair cluster exceeds the historical maximum of three pairs across 51 past governor contests and remains rare under both Poisson approximation and resampling. | Additional historical data under the same event definition, official integrated XLSX rechecking, independent resampling. | Not ruled out, but weak under the current record. |
| Nationwide post-search or multiple comparisons | It explains why using the nationwide twelve-case headline directly in a probability calculation could overstate the result. | It does not invalidate the paper's core test, which focuses on the internal Gwangju-Jeonnam five-pair cluster rather than the nationwide twelve cases. | Fixed event definition, documented search universe, repetition counts within the same candidate combination and vote type. | Important for the headline, but not sufficient to dismiss the core test. |
| Counting-unit size heterogeneity | It explains why vote pairs are not independent identically distributed samples. | It does not fully explain why five or more pairs do not appear in actual historical governor-pair resampling. | Elector counts, turnout, early-vote rates, urban/rural indicators, regional hierarchical modeling. | A valid request for model improvement, but not an automatic explanation of the anomaly. |
| Regional political preference | It explains why vote shares may be similar across some local units. | It does not by itself explain exact integer equality of both first- and second-place candidate vote counts across repeated pairs. | Elector counts, voter counts, full candidate distributions, historical comparisons in the same regions. | Useful background, but insufficient as a direct explanation of exact pair repetition. |
| Early-voter self-selection | It explains why early-vote and election-day vote shares can differ lawfully. | It does not directly explain the exact integer vote-pair collision problem. It also does not by itself explain the all-constituency same-direction pattern in 2020 and 2024 as sampling error. | Age, occupation, mobility, party mobilization, COVID-era voting behavior, separated in-district/out-of-district early-vote data. | Important for the auxiliary early/election-day analysis, but not a direct resolution of the identical-pair test. |
| Public display error | It explains the possibility that official or external screens displayed repeated numbers incorrectly. | Because this package reproduces the twelve event rows and six pairs from official NEC HTML, this explanation requires showing a discrepancy between original counting statements and screen values. | Original counting statements, integrated XLSX files, HTML generation logs, correction histories. | Possible, but not established without original-record comparison. |
| Data-entry or correction error | It explains the possibility that numbers were entered or corrected incorrectly. | It requires a documented error path to explain repeated two-candidate equality across several pairs. | Data-entry logs, correction timestamps, approval logs, pre-publication validation logs, original-to-input reconciliation. | A central audit explanation that must be checked with raw records. |
| Candidate allocation of reviewed ballots | It explains how final equality can emerge after first-pass results differ, as raised by the Songdo discussion. | It is unknown from public data whether the same process occurred in all Gwangju-Jeonnam pairs or whether allocation repeatedly moved toward identical pairs. | Candidate-level first-pass sorter results, reviewed-ballot counts, candidate-level reviewed-ballot allocation, review/aggregation desk records. | One of the most important audit targets; it could explain or strengthen the anomaly. |
| First-pass versus final aggregation difference | It explains that final numbers may reflect review and aggregation rather than only first-pass sorting. | Public final tables cannot show whether differences accumulated naturally or repeatedly favored a particular candidate direction. | Candidate-level first-pass/final differences, review reasons, unit-level correction records. | Essential for causal separation; currently unresolved. |
| Candidate or party matching error | It explains a possible analytical error in comparing the wrong candidate pair. | The paper uses actual first- and second-place candidates and directly checks the named 2026 candidate values. | Candidate total recomputation, candidate-ID matching, party-name transition checks. | Substantially weakened by the reproduction scripts and output files. |
| Press-defined event error | It explains the possibility that the initially reported twelve rows were summarized incorrectly. | The current package re-extracts the event rows from official NEC HTML rather than relying only on a report image. | NEC integrated XLSX, original counting statements, event-row official URLs or HTML cache comparison. | Important for early drafts, now narrowed to the limitation that official screen HTML has not yet been cross-checked against original counting statements. |
| COVID-era and period-specific voting behavior | It explains why early-vote behavior may have changed after 2020. | It does not directly explain the 2026 Gwangju-Jeonnam exact integer five-pair collision. | Election-by-election early-vote campaign materials, voter composition changes, local early-vote rates, in-district/out-of-district comparisons. | Relevant to the auxiliary early/election-day analysis, not a direct resolution of the main identical-pair event. |

## Explanations Weakened by Current Public Evidence

The following explanations are weakened by the currently available public record and reproduction outputs.

1. The claim that the study merely relies on a media screen no longer fits the current package. The 2026 event rows are extracted from official NEC election-statistics HTML and summarized in `outputs/nec_2026_reported_duplicate_cases.csv` and `outputs/nec_2026_reported_duplicate_pairs.csv`.
2. The claim that "one duplicate can happen" misdefines the event. The paper tests the concentration of five pairs inside Gwangju-Jeonnam, not the existence of one duplicate.
3. The claim that "duplicates existed in the past" is true but insufficient. The study includes 2014, acknowledges more historical duplicates, and still finds a maximum of three pairs inside one contest.
4. Early-voter self-selection is an alternative explanation for early/election-day vote-share gaps, not a direct explanation for five exact integer vote-pair repetitions.

## Explanations That Could Become Stronger With Raw Records

The following explanations could become stronger if additional raw records are disclosed.

1. If original counting statements differ from the official HTML screen values and the identical pairs disappear, a display or publication-system explanation becomes stronger.
2. If the candidate-level path from first-pass sorter results to final results is independently consistent and reviewed-ballot allocation is unrelated to pair creation, ordinary counting-process explanation becomes stronger.
3. If a hierarchical model using counting-unit size, voter count, and regional preference explains both historical data and 2026 while generating five-pair clusters at non-negligible frequency, the simple probability-model objection becomes stronger.
4. If similar repeated-pair levels appear across in-district early, out-of-district early, and election-day data, the in-district early-vote concentration becomes less distinctive.

## Explanations That Cannot Be Closed Without Raw Records

The following questions cannot be closed from final public tables and probability calculations alone.

1. How many votes moved between first-pass sorter results and final candidate totals.
2. How reviewed ballots were allocated by candidate and whether that allocation created identical pairs.
3. Whether official HTML screen values fully match original counting statements.
4. Whether input or correction logs show abnormal concentration in specific rows or time windows.
5. Whether identical-pair repetition is concentrated in in-district early voting or appears at comparable levels in other vote types.

## Reviewer-Response Summary

This study does not reject benign explanations by assertion. It states what evidence each explanation would require. The current public record cannot legally select one cause among coincidence, display error, data-entry error, reviewed-ballot allocation, voter self-selection, or misconduct. But none of those explanations is sufficiently established without raw records either. The conclusion is therefore not causal finality; it is an audit proposition that the observed pattern is a statistical anomaly requiring official raw-data disclosure and independent verification.
