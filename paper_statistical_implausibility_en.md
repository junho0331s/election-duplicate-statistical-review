# Repeated Identical In-District Early-Vote Pairs That Overwhelm the Random-Chance Hypothesis: Statistical Anomalies in the 2026 Korean Local Election and the Need for Raw-Data Audit

**Author:** Junho Kim  
**Affiliation:** None  
**E-mail:** junhokim0331@gmail.com

## Abstract

This paper examines repeated identical vote-count pairs in in-district early-vote counting units reported after the June 3, 2026 Korean local election. The focal pattern is not a single equality in one small precinct. It is a set of repeated two-candidate vote pairs across distinct counting units, concentrated in the same election context and reproduced from the National Election Commission election-statistics HTML pages archived in this package. The Gwangju and Jeonnam case contains five repeated pairs among twelve reported rows; the Incheon Songdo case contains an additional exact pair with different electorate, invalid-vote, abstention, and lower-candidate counts.

Using official historical election data from 2014 through 2025 as a baseline, this paper estimates the empirical frequency of such repeated pairs in comparable in-district early-vote units. The historical governor-race benchmark contains 51 constituency-level contests and 1,514,172 actual top-two comparisons, but the largest within-contest repeated-pair count is three. Under the paper's conservative reference model with \(N=393\) Gwangju-Jeonnam units and an effective pair space \(K=100,944.8\), the probability of observing at least five repeated pairs is approximately 0.001148, or 0.115%. In a nonparametric bootstrap from historical actual top-two vote pairs, no simulation out of 200,000 trials reaches five repeated pairs.

The conclusion is deliberately statistical rather than legal. These results do not, by themselves, identify a perpetrator or prove criminal election manipulation. They do show that the random-chance explanation is not adequate without additional raw records. The proper institutional response is publication of the official integrated counting files, ballot-sorter first-pass records, recount/hand-count logs, and an independent audit trail sufficient to explain the anomaly.

## 1. Research Question

The research question is narrow:

> Are the repeated identical two-candidate vote pairs in the 2026 in-district early-vote results plausibly explained as ordinary random coincidences, when compared with official historical Korean election data?

The question is not whether statistical analysis alone can convict a person or institution. It cannot. The question is whether the observed pattern is sufficiently abnormal that the burden of explanation shifts from casual dismissal to raw-data disclosure and independent audit.

## 2. Event Definition

An event is defined as an exact equality of the two principal candidates' vote counts across two different in-district early-vote counting units. For example, if unit A and unit B both report candidate 1 with \(x\) votes and candidate 2 with \(y\) votes, then the ordered pair \((x,y)\) is a duplicate pair.

The main 2026 case consists of:

- 12 reported rows reproduced from the NEC election-statistics HTML pages.
- 6 duplicate pairs in total, including 5 in the Gwangju-Jeonnam case and 1 in the Incheon Songdo case.
- Different surrounding quantities in several pairs, such as different electorate counts, invalid votes, abstentions, and non-top-two candidate votes.

The statistical object is therefore not "one number appeared twice." It is "two top-candidate counts appeared together, repeatedly, across separate counting units."

## 3. Data

The public reproduction package includes:

- official historical election files from 2014 to 2025,
- cached NEC HTML pages for the 2026 counting-unit checks,
- parsed outputs under `outputs/`,
- scripts under `scripts/`,
- the Korean paper and this English paper.

The historical baseline used for the strongest comparison is the governor-race top-two in-district early-vote dataset. The key verified counts are:

| Quantity | Value |
|---|---:|
| Parsed historical rows | 81,701 |
| Historical governor constituency contests | 51 |
| Actual top-two comparisons | 1,514,172 |
| Actual top-two duplicate pairs | 15 |
| Largest within-contest repeated-pair count | 3 |
| Official 2026 Gwangju-Jeonnam in-district units | 393 |
| Rechecked 2026 event rows from NEC HTML | 12 |
| Rechecked 2026 duplicate pairs from NEC HTML | 6 |

## 4. Why One Pair and Five Pairs Are Different

The birthday-problem analogy is useful but often misunderstood. In a large set of counting units, one exact duplicate pair can occur by chance. A single duplicate is not, by itself, strong evidence of a systematic irregularity.

Five duplicate pairs in the same election context are different. The relevant question is not "can any duplicate occur?" but "how many duplicate pairs should occur in the same constituency-scale dataset under a reasonable chance model?"

If \(N\) units independently draw from an effective pair space of size \(K\), the expected number of matching unit pairs is approximately:

\[
E[C] = \binom{N}{2}/K.
\]

With \(N=393\) and \(K=100,944.8\),

\[
E[C] \approx 0.763.
\]

An expectation below one does not make five impossible, but it makes five an upper-tail event requiring explanation. The computed tail probabilities are:

| Threshold | Probability |
|---|---:|
| \(P(C \ge 3)\) | 0.042260772 |
| \(P(C \ge 4)\) | 0.007734837 |
| \(P(C \ge 5)\) | 0.001148406 |
| \(P(C \ge 6)\) | 0.000143224 |

Thus, under this conservative model, five repeated pairs is around 0.115%, and six is around 0.0143%.

## 5. Historical Benchmark

The historical governor-race benchmark is important because it avoids purely theoretical assumptions. It asks: when Korean in-district early-vote data are parsed from official records and compared within real contests, how often do repeated top-two vote pairs actually appear?

The observed answer is modest. Across 51 constituency-level governor contests, the largest within-contest repeated-pair count is three. The 2026 Gwangju-Jeonnam pattern of five repeated pairs therefore exceeds the observed historical maximum under the comparison rule used in this paper.

The nonparametric bootstrap reinforces this point. Drawing samples from the historical actual-pair distribution with \(N=393\), the simulation produced:

| Threshold | Hits in 200,000 trials |
|---|---:|
| \(C \ge 3\) | 77 |
| \(C \ge 4\) | 4 |
| \(C \ge 5\) | 0 |

Zero hits in 200,000 trials is not mathematical impossibility. It means the event is below the simulation resolution; the rule-of-three gives an approximate 95% upper bound near 0.0015%.

## 6. Incheon Songdo Case

The Incheon Songdo case is statistically distinct from the Gwangju-Jeonnam cluster because it concerns two named counting units in the same district. The official rows show the same top-two final vote pair, while the surrounding counts differ.

The reproduction script estimates:

- Yeonsu in-district early-vote units: 15.
- Probability of at least one duplicate pair among the 15 units: approximately 0.103963%, or about 1 in 962.
- Conditional probability that the specific Songdo 1 and Songdo 2 pair matches: approximately 0.0009906%, or about 1 in 100,945.

The Songdo case is not treated as proof of the same mechanism as the Gwangju-Jeonnam cluster. It is treated as a second abnormal observation that strengthens the need for a raw audit.

## 7. Interpretation

Three points matter.

First, the evidence is stronger than a screenshot or a media claim because the package reproduces the 2026 event rows from NEC election-statistics HTML and compares them with official historical data.

Second, the result is not a legal finding. Statistical abnormality can justify audit, disclosure, and further investigation; it cannot alone establish intent, actor, or criminal liability.

Third, the random-chance explanation is weak. A model calibrated from historical Korean election records does not naturally generate five repeated pairs in the relevant 2026 context. The observed result is therefore better described as an unresolved statistical anomaly than as ordinary noise.

## 8. Multiple-Comparison and Falsification Issues

The strongest predictable objection is the multiple-comparison objection: if one searches enough elections, candidates, offices, regions, and counting-unit definitions, rare-looking coincidences will eventually appear. This objection is valid in principle, so the paper does not treat the entire universe of possible coincidences as if it had been fixed in advance.

The analysis responds in three ways. First, the main claim is narrowed to the Gwangju-Jeonnam cluster: same election, same office type, same in-district early-vote category, same top-two candidate pair, and five repeated pairs within the officially counted unit set. Second, the historical benchmark uses actual Korean election data rather than a purely theoretical uniform model. Third, the paper separates the Songdo pair from the Gwangju-Jeonnam cluster instead of adding it mechanically into one inflated headline probability.

The result is also falsifiable. The anomaly would be substantially weakened if official raw records showed that the equal final pairs were produced by documented, independently verifiable recount or reclassification steps whose first-pass records, review logs, and final arithmetic reconcile unit by unit. It would also be weakened if an independently reproduced national baseline with the same event definition showed that five-pair clusters are common in comparable Korean in-district early-vote contests. Until such evidence is produced, the ordinary-randomness explanation remains statistically inadequate.

## 9. Required Audit Materials

To resolve the anomaly, the following materials should be released or independently inspected:

- official integrated counting-unit files for the 2026 local election,
- original counting statements for the affected units,
- ballot-sorter first-pass records,
- review/hand-count logs for disputed or reclassified ballots,
- chain-of-custody records for ballot boxes and counting-unit data,
- machine log files and hashable export records where available.

Without these records, public explanation remains incomplete.

## 10. Conclusion

The repeated identical in-district early-vote pairs in the 2026 Korean local election are not adequately explained by ordinary chance under the statistical tests reported here. The Gwangju-Jeonnam cluster is far above the historical pattern, and the Songdo case adds an independent low-probability exact match. These facts do not establish a legal conclusion of election fraud by themselves. They do establish a statistically serious anomaly requiring official raw-data disclosure and independent audit.
