# Repeated Identical In-District Early-Vote Pairs That Overwhelm the Random-Chance Hypothesis: Statistical Anomalies in the 2026 Korean Local Election and the Need for Raw-Data Audit

Junho Kim
No affiliation
junhokim0331@gmail.com

## Abstract

This paper examines whether the repeated identical vote-count pairs observed in in-district early-vote counting units after the June 3, 2026 Korean local election can be explained by ordinary chance. The starting point is the public report of identical vote counts in twelve places nationwide, including ten Gwangju-Jeonnam rows where the same two leading candidates received identical counts across paired counting units. This study rechecks the twelve event rows by extracting them directly from the National Election Commission election-statistics system's official counting-unit HTML pages. The Gwangju-Jeonnam case is defined as five repeated identical vote pairs within the same election, the same top-two candidate combination, and the same in-district early-vote category.

To build a historical baseline, this study parses 81,701 early-vote counting-unit rows from official National Election Commission and public-data files from 2014 through 2025. The primary benchmark is the actual top-two candidate vote-pair distribution in governor races. Across 51 governor constituency contests and approximately 1,514,172 actual comparison pairs, only 15 identical top-two vote pairs are observed, and the maximum repeated-pair count within any one constituency contest is three. Under the expanded benchmark, the probability of observing at least five repeated pairs in the 2026 Gwangju-Jeonnam setting is approximately 0.115% using a Poisson approximation with \(N=393\) and \(K=100,944.8\). In a nonparametric resampling test drawing 393 units without replacement from the historical governor top-two pair pool, no simulation among 200,000 trials produces five or more repeated pairs; the rule-of-three 95% upper bound is approximately 0.0015%.

This paper also checks the difference between early-vote and election-day two-party vote shares in the 2016, 2020, and 2024 National Assembly elections. In 2020 and 2024, every analyzable constituency shows a higher Democratic-party two-party share in early voting than on election day. This auxiliary test is not treated as direct proof of a specific misconduct mechanism, but it reinforces the need for a broader raw-data audit. The conclusion is not a legal finding that a specific act of misconduct has been proven. It is a narrower statistical conclusion: even under conservative assumptions, the public data contain anomalies that weaken the random-chance hypothesis and require independent access to raw counting records.

Keywords: in-district early voting, identical vote pair, election integrity, duplicate probability, Poisson approximation, early-vote deviation, raw-data audit

## 1. Introduction

After the 2026 Korean local election, several reports noted that two leading candidates received exactly the same vote counts in different in-district early-vote counting units. A TV Chosun report dated June 8, 2026 stated that identical vote counts appeared in twelve places nationwide, including ten Gwangju-Jeonnam rows where Democratic Party candidate Min Hyung-bae and People Power Party candidate Lee Jung-hyun received the same paired vote counts. The same report also presented the Incheon Songdo 1-dong and Songdo 2-dong case, where Democratic Party candidate Park Chan-dae received 3,030 votes and People Power Party candidate Yoo Jeong-bok received 1,440 votes in both units.

The subject of this paper is statistical rather than partisan. The questions are:

1. How often has a pattern of five or more identical top-two candidate vote pairs occurred in the same election, same candidate combination, and same in-district early-vote category in historical official data?
2. Under a simple duplicate-probability model, how likely is the observed repetition?
3. Can the observed pattern be closed as ordinary random coincidence, or does it constitute a statistical anomaly requiring raw-data verification?

This paper answers the third question cautiously. Statistical improbability is not a sufficient condition for proving misconduct. However, when the improbability is strong enough, an election-management institution cannot reasonably end the matter by merely saying "coincidence." It must produce the raw records that can either explain or falsify the anomaly.

### 1.1 Research Hypotheses

The primary test concerns repeated identical vote pairs.

- Null hypothesis \(H_0\): The five identical top-two candidate vote pairs observed in the 2026 Gwangju-Jeonnam in-district early-vote results are compatible with the duplicate-pair structure observed in past governor elections. In plain terms, the event is something that historical data would make plausible.
- Alternative hypothesis \(H_1\): The five identical top-two candidate vote pairs in the 2026 Gwangju-Jeonnam in-district early-vote results are difficult to reconcile with the historical empirical distribution. In plain terms, the event is an outlier relative to past official data.

The secondary test concerns the difference between early voting and election-day voting.

- Null hypothesis \(H_0'\): The vote-share difference between early voting and election-day voting is explainable within ordinary constituency-level voter self-selection and voting-behavior differences.
- Alternative hypothesis \(H_1'\): The early-vote and election-day vote-share difference repeats in the same direction across many constituencies and remains insufficiently explained without additional covariates or raw-data verification.

Both \(H_1\) and \(H_1'\) are treated as statistical audit triggers, not legal judgments.

## 2. Definition of the Observed Event

The event analyzed in this paper is defined as follows:

- Election: the 9th nationwide local election held in 2026.
- Vote type: in-district early voting.
- Comparison unit: eup, myeon, or dong counting-unit results within the same metropolitan or provincial governor race.
- Candidate rule: the principal first- and second-place candidates in the relevant race.
- Event: two different counting units report the same first-candidate vote count and the same second-candidate vote count simultaneously.

The reported Gwangju-Jeonnam case is summarized as five pairs. This study re-extracts and checks these values from the official NEC election-statistics counting-unit pages.

| Pair | Counting unit A | Counting unit B | Min Hyung-bae | Lee Jung-hyun |
| ---: | --- | --- | ---: | ---: |
| 1 | Songjeong 1-dong, Gwangsan-gu, Gwangju | Geumsan-myeon, Goheung-gun | 1,401 | 120 |
| 2 | Haui-myeon, Sinan-gun | Samil-dong, Yeosu-si | 506 | 42 |
| 3 | Iyang-myeon, Hwasun-gun | Byeongyeong-myeon, Gangjin-gun | 444 | 46 |
| 4 | Eomda-myeon, Hampyeong-gun | Bukha-myeon, Jangseong-gun | 606 | 57 |
| 5 | Nodong-myeon, Boseong-gun | Palgeum-myeon, Sinan-gun | 356 | 42 |

The Incheon Songdo case is treated separately because it belongs to another contest.

| Counting unit A | Counting unit B | Park Chan-dae | Yoo Jeong-bok |
| --- | --- | ---: | ---: |
| Songdo 1-dong | Songdo 2-dong | 3,030 | 1,440 |

The paper therefore separates two levels:

- Internal Gwangju-Jeonnam event: five pairs in one contest environment.
- Nationwide reported event: six pairs across more than one contest.

The stronger statistical target is the internal Gwangju-Jeonnam event. The nationwide six-pair set is more exposed to post-search and multiple-comparison objections because it was found after scanning across contests.

## 3. Data and Reproduction Method

### 3.1 Historical Baseline Data

The study uses public National Election Commission and public-data election counting files from 2014 through 2025.

| Election | Parsed rows |
| --- | ---: |
| 2014 local | 25,600 |
| 2016 National Assembly | 3,661 |
| 2017 presidential | 3,684 |
| 2018 local | 22,926 |
| 2020 National Assembly | 3,681 |
| 2022 presidential | 3,703 |
| 2022 local | 10,942 |
| 2024 National Assembly | 3,754 |
| 2025 presidential | 3,750 |
| Total | 81,701 |

Aggregate rows, subtotal rows, shipboard/residential special votes, overseas votes, and out-of-country categories are excluded from the main comparison. In-district early voting and out-of-district early voting are separated, and the central analysis uses in-district early-vote rows.

At the time this paper was prepared, the official integrated XLSX file for the 2026 local election was not available in the same public-data format used for the historical baseline. However, the NEC election-statistics system was providing counting-unit results for the 9th nationwide local election. This study saves and parses the relevant POST-response HTML from the official "counting-unit result" pages and rechecks the twelve event rows. The procedure is implemented in `scripts/fetch_nec_2026_duplicate_cases.py`, with outputs in `outputs/nec_2026_reported_duplicate_cases.csv` and `outputs/nec_2026_reported_duplicate_pairs.csv`. Thus the 2026 event values no longer depend only on a media screenshot. When the official integrated XLSX file or original counting statements become available, the same event definition should be re-applied.

### 3.2 Inclusion and Exclusion Criteria

The 2014 local election is included to increase baseline reliability. It is the first nationwide local election after the introduction of the nationwide early-voting system, and the public counting files distinguish in-district and out-of-district early voting. The 2010 local election and the 2012 presidential/National Assembly elections are excluded from the main baseline because they do not belong to the same in-district early-voting institutional regime.

This choice does not bias the result in favor of anomaly detection. Including the 2014 local election increases the number of historical duplicate pairs and therefore weakens the apparent rarity of the 2026 event. Even after this broader inclusion, the 2026 Gwangju-Jeonnam five-pair repetition exceeds the historical maximum.

### 3.3 Actual First- and Second-Place Candidate Rule

A naive analysis might compare the first two candidates listed in each file. That does not always match the reported meaning of "first and second place." This paper therefore uses the following procedure:

1. Group counting units by election, office type, constituency, and vote type.
2. Compute total votes for each candidate within the group.
3. Select the actual first- and second-place candidates by total votes.
4. For each eup, myeon, or dong in-district early-vote counting unit, form the ordered vote pair for these two candidates.
5. Count whether the same vote pair appears in two or more different units.

This is the rule closest to the reported event.

### 3.4 Mapping Claims to Verification Files

This paper separates statistically reproducible claims from administrative or legal claims that require additional raw records. Without this separation, a critic can attack the weakest part of a broad claim and dismiss the entire analysis. The reproducible claims in this package are:

1. The twelve 2026 event rows are reproduced from official NEC election-statistics HTML pages.
2. Those twelve rows form six identical vote pairs.
3. In the 51 historical governor in-district early-vote contests, the maximum repeated-pair count within a single contest is three.
4. With \(N=393\) and \(K=100,944.8\), the Poisson-tail probability for five or more repeated pairs in Gwangju-Jeonnam is approximately 0.115%.
5. In 200,000 nonparametric trials sampling 393 units without replacement from the historical governor actual-pair pool, five or more repeated pairs occur zero times.
6. In the 2020 and 2024 National Assembly elections, the Democratic candidate's early-vote two-party share is higher than the election-day two-party share in every analyzable constituency.

The unresolved causal claim is different: whether the identical pairs were produced by natural counting processes, data-entry or display errors, review/reclassification procedures, or another cause. That question requires original counting statements, ballot-sorter first-pass outputs, review-ballot allocation records, and input logs. The detailed claim-to-file mapping is provided in `evidence_matrix_ko.md`.

The completed conclusion of this study is therefore not "the cause has been proven." It is: "official page values and historical baselines are sufficient to define a statistical anomaly requiring raw-data audit."

## 4. Empirical Baseline

### 4.1 Historical Governor Elections

The closest comparison class for the 2026 Gwangju-Jeonnam case is past governor elections because the observed event occurred in a metropolitan/provincial governor race and in the in-district early-vote category.

Reanalysis of the 2014, 2018, and 2022 governor-election in-district early-vote data under the actual top-two candidate rule gives:

| Quantity | Value |
| --- | ---: |
| Governor constituency contests | 51 |
| Total comparison pairs | 1,514,172 |
| Identical vote pairs | 15 |
| Constituency contests with at least one identical pair | 9 |
| Maximum identical pairs within one contest | 3 |
| Constituency contests with five or more pairs | 0 |

The observed historical identical pairs are:

| Election | Constituency | First-place candidate | Second-place candidate | Identical vote pair | Units |
| --- | --- | --- | --- | ---: | --- |
| 2014 local | Gangwon | Choi Moon-soon | Choi Heung-jip | 49, 80 | Duchon-myeon, Gimsatgat-myeon |
| 2014 local | Gangwon | Choi Moon-soon | Choi Heung-jip | 57, 95 | Buron-myeon, Mukho-dong |
| 2014 local | Gyeongnam | Hong Joon-pyo | Kim Kyung-soo | 293, 83 | Bugok-myeon, Ungyang-myeon |
| 2014 local | Gyeongbuk | Kim Kwan-yong | Oh Joong-gi | 160, 23 | Chojeon-myeon, Hyeondong-myeon |
| 2014 local | Gyeongbuk | Kim Kwan-yong | Oh Joong-gi | 186, 28 | Jisan-dong, Andeok-myeon |
| 2014 local | Gyeongbuk | Kim Kwan-yong | Oh Joong-gi | 342, 43 | Pyeonghwa-dong, Bongyang-myeon |
| 2014 local | Jeonnam | Lee Nak-yon | Lee Seong-su | 124, 18 | Nam-myeon, Eomda-myeon |
| 2014 local | Jeonnam | Lee Nak-yon | Lee Seong-su | 190, 33 | Bugil-myeon, Heuksan-myeon |
| 2014 local | Jeonbuk | Song Ha-jin | Park Cheol-gon | 145, 41 | Ungpo-myeon, Boan-myeon |
| 2014 local | Jeonbuk | Song Ha-jin | Park Cheol-gon | 174, 27 | Ipyeong-myeon, Ibaek-myeon |
| 2014 local | Jeonbuk | Song Ha-jin | Park Cheol-gon | 174, 50 | Seosu-myeon, Jungang-dong |
| 2014 local | Chungnam | Ahn Hee-jung | Chung Jin-suk | 54, 61 | Sicho-myeon, Munsan-myeon |
| 2018 local | Daegu | Kwon Young-jin | Im Dae-yoon | 674, 559 | Gwaneum-dong, Hyeonpung-myeon |
| 2022 local | Jeonnam | Kim Young-rok | Lee Jung-hyun | 377, 90 | Dongbok-myeon, Jangsan-myeon |
| 2022 local | Chungbuk | Kim Young-hwan | Noh Young-min | 319, 158 | Yangsan-myeon, Naebuk-myeon |

The point is not that historical duplicate pairs never occur. They do. In particular, including the 2014 local election increases the historical duplicate count. But no historical governor contest in the expanded baseline has five repeated pairs within one contest. The historical maximum is three.

A predictable objection is that if three pairs occurred historically, five pairs should not be treated as special. That objection confuses a maximum observation with a tail probability. Three pairs is the upper end observed after pooling 51 historical governor contests. Five pairs exceeds that observed upper end by two additional repeated pairs. Under \(N=393\) and \(K=100,945\), three or more pairs has a probability near 4.23%; five or more pairs has a probability near 0.115%. This paper therefore does not argue that "three pairs are already proof, so five pairs are proof." It accepts three as an observed rare historical upper value and treats five as an event beyond that upper value.

### 4.2 Empirical Estimate of the Effective Vote-Pair Space

The historical governor dataset contains 1,514,172 total comparison pairs and 15 observed identical vote pairs. If the effective number of possible first-second vote pairs is denoted by \(K\), then the expected number of collisions is roughly:

\[
E(C) \approx \frac{N(N-1)}{2K}.
\]

Solving backward from the historical governor data gives:

\[
\hat{K} \approx \frac{1,514,172}{15} \approx 100,945.
\]

This is not a strict structural parameter. Real election data are not generated from identical independent draws; unit size, geography, party support, and turnout matter. But \(K\) is an empirical reference value reflecting how often actual Korean governor-election top-two vote pairs collided in official data.

## 5. Probability Calculation

### 5.1 Poisson Approximation

Suppose one constituency-level contest contains \(N\) in-district early-vote counting units, and each unit produces a top-two vote pair from an effective pair space of size \(K\). Let \(C\) be the number of identical vote-pair collisions among distinct unit pairs. For rare collision events, \(C\) can be approximated by:

\[
C \sim \mathrm{Poisson}(\lambda),
\]

with

\[
\lambda = \frac{N(N-1)}{2K}.
\]

The probability of interest is:

\[
P(C \geq 5),
\]

which corresponds to at least five identical vote-pair repetitions within the Gwangju-Jeonnam setting.

### 5.2 Baseline with \(N=393\) and \(K=100,945\)

Here \(N\) is not the number of already reported rows. It is the number of potential in-district early-vote counting units that could have produced identical pairs within the same contest environment. This means the eup, myeon, and dong level units in the same candidate combination and vote type.

This study does not estimate \(N\) from administrative intuition. It counts \(N\) directly from the NEC VCCP08 official HTML pages. After parsing all governor counting-unit pages for the five Gwangju districts and the twenty-two Jeonnam cities/counties, and counting rows that are in-district early-vote rows rather than aggregate rows, the output `outputs/nec_2026_gwangju_jeonnam_unit_counts.csv` gives 96 Gwangju units and 297 Jeonnam units, for a total of 393. Therefore the baseline calculation uses \(N=393\).

\(K=100,945\) is also not arbitrary. In the historical governor baseline, there are 1,514,172 actual top-two comparison pairs and 15 observed identical vote pairs. Reversing the rare-collision formula gives \(K\) near 100,945.

\[
\hat{K} \approx \frac{1,514,172}{15} \approx 100,945
\]

Thus \(N=393\) and \(K=100,945\) are not numbers inserted for convenience. They combine the Gwangju-Jeonnam in-district early-vote unit count measured from official NEC pages with the empirically inferred effective pair space from historical governor data.

Using these values:

\[
\lambda = \frac{393 \times 392}{2 \times 100,945} \approx 0.76307.
\]

The computed probabilities are:

| Event | Probability | Reciprocal interpretation |
| --- | ---: | ---: |
| At least 5 pairs | about 0.115% | about 1 in 871 |
| At least 6 pairs | about 0.0143% | about 1 in 6,982 |

In this calculation, five pairs refers to the internal Gwangju-Jeonnam event. Six pairs is a simplified reference value for the nationwide reported event. The nationwide six-pair figure requires additional multiple-search adjustment because it was found after looking across more than one contest.

### 5.3 Sensitivity to the Effective Pair Space

The probability changes depending on how the effective pair space \(K\) is set. With \(N=393\), the sensitivity calculation is:

| Effective pair space \(K\) | \(P(C \geq 5)\) | \(P(C \geq 6)\) |
| ---: | ---: | ---: |
| 50,000 | 2.0550% | 0.5056% |
| 100,000 | 0.1197% | 0.0151% |
| 100,945 | 0.1148% | 0.0143% |
| 200,000 | 0.0051% | 0.00033% |
| 337,354 | 0.00043% | 0.000016% |
| 500,000 | 0.000064% | 0.0000016% |

Even under a highly conservative \(K=50,000\) assumption, which makes duplicate pairs much easier to produce, the probability of at least five pairs is about 2.05%. That is not impossibility, but it remains a low-tail event. Under the expanded historical governor benchmark, \(K=100,945\), the probability is about 0.115%. This is sufficiently rare to function as an audit trigger even after including the smaller early-vote scale of 2014 in the historical baseline.

### 5.4 Sensitivity to the Number of Counting Units

The official HTML-based baseline is \(N=393\). To check whether the conclusion depends narrowly on that value, the paper also holds \(K=100,945\) fixed and varies \(N\) from 350 to 450.

| In-district early-vote units \(N\) | \(\lambda\) | \(P(C \geq 5)\) | Reciprocal interpretation |
| ---: | ---: | ---: | ---: |
| 350 | 0.6050 | 0.0410% | about 1 in 2,441 |
| 390 | 0.7515 | 0.1074% | about 1 in 931 |
| 393 | 0.7631 | 0.1148% | about 1 in 871 |
| 400 | 0.7905 | 0.1340% | about 1 in 746 |
| 430 | 0.9137 | 0.2500% | about 1 in 400 |
| 450 | 1.0008 | 0.3672% | about 1 in 272 |

The table shows that the assumed unit count changes the exact probability but not the direction of the conclusion. Even at \(N=450\), at least five repeated pairs remains below 0.4%. The Gwangju-Jeonnam five-pair result therefore does not depend only on the single \(N=393\) baseline.

### 5.5 Nonparametric Resampling Test

The Poisson approximation is useful because it is easy to interpret, but it still contains the model assumption of an effective pair space \(K\). To reduce model dependence, this paper directly resamples actual historical top-two vote pairs from governor in-district early-vote data.

The procedure is:

1. Build the pool of 10,322 actual top-two candidate vote pairs from the 2014, 2018, and 2022 governor in-district early-vote data.
2. Draw 393 units without replacement.
3. Count the number of repeated vote pairs in the draw.
4. Repeat this procedure 200,000 times with a fixed random seed.

Sampling without replacement prevents artificial duplicates caused by drawing the same historical unit more than once. The test directly asks: if 393 units are drawn from actual past governor early-vote units, how often do five or more repeated pairs appear?

The observed simulation results are:

| Threshold | Hits in 200,000 trials | Empirical probability |
| --- | ---: | ---: |
| \(C \geq 3\) | 77 | 0.000385 |
| \(C \geq 4\) | 4 | 0.000020 |
| \(C \geq 5\) | 0 | 0 at simulation resolution |

Zero hits in 200,000 trials does not prove mathematical impossibility. It means that the event is below the simulation resolution. The observable resolution is \(1/200,000=0.0005\%\), and a conservative plus-one estimate is \(1/200,001\), also about 0.0005%. Applying the rule of three gives a rough 95% upper bound of about \(3/200,000 = 0.000015\), or 0.0015%.

This result is stronger than the Poisson approximation, but the paper does not rely on it alone. The main point is convergence across approaches: the historical maximum is three pairs, the Poisson approximation gives 0.115% for five or more pairs, and direct resampling yields zero occurrences in 200,000 trials. All three checks reject the interpretation that the Gwangju-Jeonnam five-pair cluster is an ordinary event.

## 6. Why One Pair and Five Pairs Are Different

The most common misunderstanding in identical-vote-pair discussions is a linear comparison: if one pair can occur, then several pairs can also occur. But the event tested here is not whether at least one identical pair exists. The tested event is how many identical pairs accumulate within the same contest, same candidate combination, and same in-district early-vote category. The former is a broad collision event. The latter is an upper-tail repetition event.

When the number of counting units is large, one identical pair can easily appear because the number of possible unit-to-unit comparisons grows quickly.

\[
\binom{N}{2} = \frac{N(N-1)}{2}
\]

For \(N=393\), there are 77,028 unit pairs. In a comparison space that large, one matching vote pair somewhere is not by itself an anomaly. This paper therefore does not treat one identical pair as suspicious by itself.

Five pairs are a different object. If \(C\) is the number of identical vote-pair collisions in the contest environment, the relevant question is not \(C \ge 1\), but \(C \ge 5\). In the Poisson approximation, the probability of at least \(m\) repeated pairs is:

\[
P(C \ge m) = 1 - e^{-\lambda}\sum_{c=0}^{m-1}\frac{\lambda^c}{c!}
\]

As \(m\) rises from 1 to 3, 4, and 5, the probability does not decline in a merely linear way. It moves rapidly into the tail.

The distinction is visible in the numbers. Under the baseline model, \(P(C \geq 3)\) is about 4.23%, while \(P(C \geq 5)\) is about 0.115%. Both are below the center of the distribution, but five is roughly 37 times rarer than three under the same assumptions. Historical data also show this difference: three pairs occurred as the historical maximum; five did not occur in any historical governor contest in the baseline.

| Threshold | Probability | Intuitive frequency | Interpretation |
| --- | ---: | ---: | --- |
| \(C \ge 1\) | about 53.37% | about 1 in 1.9 | one pair is plausible |
| \(C \ge 2\) | about 17.88% | about 1 in 5.6 | uncommon but unsurprising |
| \(C \ge 3\) | about 4.23% | about 1 in 23.7 | observed historical upper end |
| \(C \ge 4\) | about 0.773% | about 1 in 129 | strong audit signal |
| \(C \ge 5\) | about 0.115% | about 1 in 871 | event above the historical maximum |

Thus the difference between three pairs and five pairs is not merely "two more pairs." Under the same baseline, at least five pairs is about 37 times rarer than at least three pairs. More importantly, three pairs is the rare upper end actually observed in the historical governor data, whereas five pairs exceeds that upper end.

This distinction matters for rebuttal. Saying "if three pairs occurred historically, five pairs are also fine" is like saying that because 38 degrees Celsius has occurred historically, 40 degrees must be the same kind of event. The numeric difference may look small, but exceeding the historical maximum changes the statistical interpretation. In the same way, three pairs set the observed benchmark, while five pairs test and exceed it.

Another key issue is post-search scope. If one searches all elections, all offices, all candidates, all vote types, and all regions, then a rare-looking coincidence will eventually be found. This paper therefore places the main claim on the Gwangju-Jeonnam internal five-pair cluster rather than the entire nationwide set. The Gwangju-Jeonnam cluster is defined by the same office, same top-two candidate pair, same in-district early-vote category, and the same contest environment.

In conclusion, this paper does not say that one identical pair is suspicious by itself. One pair is possible. Three pairs are also acknowledged as a rare historical upper end. The problem is that five pairs are concentrated in the same structure and exceed both the historical maximum and the tail-probability benchmark.

## 7. Specificity of the Incheon Songdo Case

The Incheon Songdo case is not simply another row to be mechanically added to the Gwangju-Jeonnam cluster. It belongs to a different contest and should be analyzed separately.

Reports state that Songdo 1-dong and Songdo 2-dong had the same final in-district early-vote result for the two leading candidates: Park Chan-dae 3,030 votes and Yoo Jeong-bok 1,440 votes. However, the electorate counts, third-candidate votes, invalid votes, and abstentions differed. Public election-management explanations also stated that the first-pass ballot-sorter results were not identical, and that the final equality emerged only after reviewed ballots were hand-counted and added.

The reported first-pass results were:

| Unit | Park Chan-dae first pass | Yoo Jeong-bok first pass | Reviewed ballots |
| --- | ---: | ---: | ---: |
| Songdo 1-dong | 3,016 | 1,427 | 44 |
| Songdo 2-dong | 3,011 | 1,429 | 53 |

The final result was:

| Unit | Park Chan-dae final | Yoo Jeong-bok final |
| --- | ---: | ---: |
| Songdo 1-dong | 3,030 | 1,440 |
| Songdo 2-dong | 3,030 | 1,440 |

The statistical specificity of Songdo can be viewed in two ways. First, using the same \(K=100,944.8\) benchmark, Yeonsu-gu has 15 in-district early-vote units in the official HTML parsing. The number of unit comparisons is \(\binom{15}{2}=105\), and:

\[
\lambda_{\text{Yeonsu}} = \frac{105}{100,944.8} \approx 0.001040
\]

Therefore the probability that at least one identical vote pair appears somewhere inside the 15 Yeonsu in-district early-vote units is:

\[
P(C \ge 1) \approx 1-e^{-0.001040} \approx 0.104\%
\]

This is about 1 in 962.

Second, if Songdo 1-dong and Songdo 2-dong are treated as the already specified pair of interest, the conditional probability that those two units have the same top-two vote pair is:

\[
\frac{1}{K} \approx \frac{1}{100,944.8} \approx 0.000991\%
\]

This is about 1 in 100,945. That number is appropriate only when the two Songdo units are treated as pre-specified. If the event is instead defined after searching nationwide, post-search adjustment is required.

The Songdo case is therefore not part of the same primary test as the Gwangju-Jeonnam five-pair cluster, but it is a strong auxiliary audit signal. The key question is not only whether final numbers can happen to match. It is how different first-pass results and reviewed-ballot pools produced the same final top-two vote pair.

The same fact can be read in two directions. From the election-management perspective, different first-pass results and reviewed-ballot counts can be offered as an explanation that the final equality was not a simple copy or display error. From an audit perspective, the same explanation makes the reviewed-ballot candidate allocation records essential.

The core verification material for Songdo is therefore not the final published table alone. It is the candidate-by-candidate allocation of the reviewed ballots.

## 8. Statistical Anomaly Versus Evidence of Misconduct

The results of this study support the following proposition:

> The Gwangju-Jeonnam five-pair identical-vote event is a very low-probability event under the random-chance hypothesis.

They do not automatically support the stronger proposition:

> The Gwangju-Jeonnam five-pair identical-vote event is, by itself, proof of election fraud.

The word "evidence" must therefore be used in two layers. First, repeated identical vote pairs are statistical evidence that weakens the ordinary-randomness explanation. Second, they are not direct evidence that a specific person manipulated the count in a specific way. Both three-pair repetition and five-pair repetition are worth examining in the first sense, but their strength differs. Three pairs are a rare historical upper value observed inside the historical data; five pairs exceed that observed upper value. Calling both three pairs and five pairs a legal conclusion would overstate the evidence. Calling both of them meaningless coincidence would discard statistical information.

A statistical anomaly creates a question about cause. Several causes are possible:

1. a very low-probability coincidence;
2. an original counting-statement preparation or data-entry error;
3. a display error in the public system;
4. systematic skew in the reviewed-ballot processing stage;
5. actual misconduct.

The currently public materials cannot select one of these five explanations conclusively. However, explanation 1, pure coincidence, is statistically weak. Raw-data disclosure and audit are therefore required.

## 9. Raw Materials Required for Verification

To transform the statistical question into administrative or legal evidence, the following records are needed:

1. original counting statements for all twelve event rows;
2. candidate-by-candidate first-pass ballot-sorter results for each affected counting unit;
3. the number of reviewed ballots in each affected counting unit;
4. candidate-by-candidate final allocation of the reviewed ballots;
5. invalid votes, abstentions, and third-candidate vote counts;
6. counting-division, sorter, review/aggregation desk, data-entry operator, and time logs;
7. reconciliation between the NEC public-system values and original counting statements;
8. whether party- or candidate-recommended observers raised objections.

The especially important comparison is the difference between first-pass results and final results. If the Gwangju-Jeonnam five pairs, like the Songdo case, had different first-pass results but became identical only through reviewed ballots or final aggregation, that would be a stronger audit trigger than simple coincidence.

## 10. Limitations

This paper has the following limitations.

First, the official integrated XLSX counting file for the 2026 local election from the public-data portal has not yet been parsed directly. However, the 2026 event values were checked by saving and parsing the NEC election-statistics system's official counting-unit HTML pages. The present limitation is therefore not "the paper used only press-reported values." It is more precise to say: "official screen values have been checked, but the integrated XLSX file and original counting statements have not yet been obtained." A final administrative or legal judgment requires comparison against the NEC integrated file, original counting statements, and first-pass sorter results.

This limitation does not discard the current analysis. It defines the scope of the conclusion. Under the official screen values, the twelve event rows and six identical pairs are reproducible. Once the integrated XLSX file is released, the event definition and reproduction scripts in this paper can be applied directly to recompute the number of repeated identical vote pairs.

Second, the Poisson approximation is a simplified model. Real eup, myeon, and dong vote pairs are not independently generated under identical conditions. Regional preference, voter count, number of candidates, urban/rural structure, and early-vote turnout all matter.

Third, the effective vote-pair space \(K\) is not a directly observed natural constant. This paper estimates it empirically from historical governor-election data. Conservative sensitivity analyses are provided, but a final study should also be strengthened through repeated resampling of historical data or a hierarchical model that reflects regional size differences.

Fourth, the nationwide twelve cases were found after scanning multiple contests and regions, so they are exposed to a post-search problem. The statistically strongest object in this paper is the five-pair repetition inside the Gwangju-Jeonnam contest environment.

## 11. Early-Vote Versus Election-Day Vote-Share Difference

Separate from repeated identical vote pairs, this study uses early-vote versus election-day vote-share differences as an auxiliary test. The purpose is to check whether early voting reflects the same direction and scale of political choice as election-day voting. For a given constituency, let \(p_E\) be a candidate's early-vote share, \(p_D\) the same candidate's election-day vote share, \(n_E\) the early-vote count, and \(n_D\) the election-day vote count. Under a null hypothesis that the two vote groups are random samples from the same underlying support rate \(p\), the standard two-proportion z statistic is:

\[
z = \frac{p_E - p_D}{\sqrt{\hat{p}(1-\hat{p})(1/n_E + 1/n_D)}}
\]

where \(\hat{p}\) is the pooled candidate vote share. When sample sizes are in the thousands or tens of thousands, the denominator becomes small. Therefore even several percentage-point differences can produce very large z values. This is why "large vote-share differences in large samples" are difficult to explain by ordinary sampling error alone.

This test has an important assumption: early voters and election-day voters must be random samples from the same voter population. In real elections, this assumption may fail. Early voters may self-select by age, occupation, mobility, party preference, campaign mobilization, and other factors. Therefore a large early-vote/election-day difference alone does not prove misconduct.

Still, the test is not meaningless. Suspicion becomes stronger when:

1. the early/election-day difference repeats in the same party direction across many constituencies;
2. the difference suddenly becomes larger than in earlier elections in the same country;
3. large residual differences remain after accounting for age, gender, region, urban/rural structure, and early-vote rates;
4. in-district and out-of-district early-vote patterns differ from each other;
5. the same election or region also shows separate anomalies such as identical vote pairs, ballot shortages, or counting-statement inconsistencies.

This paper therefore treats early-vote versus election-day vote-share differences as an auxiliary test. Identical vote-pair repetition is a discrete count-collision problem; early/election-day vote-share difference is a two-sample proportion problem. They have different statistical structures. But if both appear in the same election environment, a single ordinary-randomness explanation becomes weaker.

### 11.1 Check Against Official National Assembly Data

This study directly parses official counting data for the 2016, 2020, and 2024 National Assembly elections. The analyzed constituencies are those in which both a Democratic-party candidate and a conservative-party candidate are present. The conservative party is defined as Saenuri Party in 2016, United Future Party in 2020, and People Power Party in 2024.

For each constituency, the script computes:

\[
\Delta = p_E - p_D
\]

where \(p_E\) is the Democratic candidate's share of Democratic-plus-conservative two-party votes in early voting, and \(p_D\) is the same two-party share in election-day voting. Early voting combines in-district and out-of-district early votes. Election-day voting includes only election-day polling-station votes. Residential/shipboard, overseas, subtotal, and aggregate rows are excluded.

Direct calculation gives:

| Election | Constituencies | Mean early-day difference | Median | Democratic early advantage | Democratic early disadvantage | Absolute z > 5 | Absolute z > 10 | Max absolute z |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 2016 National Assembly | 229 | +3.90%p | +3.43%p | 211 | 18 | 158 | 88 | 31.94 |
| 2020 National Assembly | 236 | +10.88%p | +11.21%p | 236 | 0 | 236 | 234 | 55.77 |
| 2024 National Assembly | 245 | +10.35%p | +10.80%p | 245 | 0 | 245 | 245 | 60.92 |

These results show two things at once.

First, the simplified claim that "the law of large numbers held perfectly in 2016 and broke only from 2020" does not fit the official data. In 2016, the Democratic candidate's early-vote two-party share was also higher than the election-day share by an average of 3.90 percentage points, and 211 of 229 constituencies showed a Democratic early-vote advantage.

Second, the 2020 and 2024 patterns are much stronger than 2016. In 2020, all 236 analyzable constituencies showed a Democratic early-vote advantage. In 2024, all 245 analyzable constituencies showed the same direction. The average difference also expanded to roughly 10 to 11 percentage points.

The defensible claim from the direct calculation is therefore:

> A Democratic early-vote advantage already existed in 2016, but in 2020 and 2024 the direction expanded to every analyzable constituency and the average magnitude grew to about three times the 2016 level.

This claim is statistically strong. It is still not direct proof of misconduct. Alternative explanations such as voter self-selection, party-specific early-vote mobilization, age, occupation, regional mobility, and COVID-era voting behavior must be evaluated. However, the 2020 and 2024 all-constituency directional pattern is difficult to explain as ordinary sampling error alone, and it is a valid target for independent audit or additional statistical modeling.

The directionality issue is often described as a "law of large numbers" issue. More precisely, the question is whether the same-direction pattern would arise from sampling error if early votes and election-day votes were samples from the same underlying electorate. This paper uses it only as an auxiliary test, with detailed assumptions and results also summarized in Appendix B.

### 11.2 Connection to the 2026 Local Election

The twelve reported identical-vote rows in the June 3, 2026 local election are separate from the early/election-day vote-share difference issue. But both phenomena arise in early-vote data.

This paper focuses on the June 3 local election for the following reasons:

1. the Songdo 1-dong/Songdo 2-dong identical pair occurred in in-district early voting;
2. the ten Gwangju-Jeonnam rows, or five identical pairs, also occurred in in-district early voting;
3. in past official governor data, the maximum identical-pair repetition within one contest was three pairs;
4. the June 3 reported case reaches five pairs within one contest environment, exceeding the expanded historical benchmark;
5. in the 2020 and 2024 National Assembly elections, early voting also showed systematic directionality relative to election-day voting.

Therefore the June 3 identical-vote-pair problem should not be treated as an isolated coincidence without further checking. Combined with the systematic early-vote deviations observed in 2020 and 2024, it points to a broader audit question: repeated statistical anomalies are appearing in early-vote data, and official raw records are needed to separate lawful voter behavior from administrative or counting-process explanations.

## 12. Expected Objections and Responses

This section anticipates objections that a skeptical reviewer may raise and defines the range within which the paper's conclusion remains valid.

### 12.1 "With many counting units, identical vote pairs can always appear."

Correct. This study does not treat the occurrence of a single identical vote pair as anomalous. When there are many counting units, the number of possible comparisons grows quickly, so one identical vote pair can occur naturally. The target of this study is not "the existence of an identical vote pair," but the concentration of five repeated identical top-two vote pairs inside the same contest, vote type, and candidate combination. In the expanded historical benchmark, the maximum repetition inside any one of 51 past governor contests was three pairs. The Gwangju-Jeonnam five-pair event should therefore be treated as an event exceeding the historical empirical upper bound, not as a mere duplicate.

### 12.2 "If 2014 is included, historical duplicates become more common."

Correct. When the 2014 local election is added, governor-election identical vote pairs increase from 3 to 15, and the estimated probability is relaxed from about 0.0004% to about 0.115%. This revision is unfavorable to this paper's thesis. Even so, the maximum repetition inside one contest in the expanded benchmark remains three pairs, and no case of five or more pairs is observed. Therefore, even under the conservative benchmark that includes 2014, the 2026 Gwangju-Jeonnam five-pair repetition lies outside the historical empirical distribution.

### 12.3 "If three historical pairs are acceptable, five should also be acceptable."

No. This objection arises from comparing three pairs and five pairs linearly. Repeated identical vote pairs are tail events whose probability falls rapidly as one additional pair is added. Under this paper's conservative benchmark, three or more pairs have probability about 4.23%, which is rare but within the range that can be observed once across 51 historical contests. Five or more pairs have probability about 0.115%, about 37 times rarer than three or more. The historical maximum of three pairs is therefore a baseline for how much repetition has actually been observed naturally; the 2026 Gwangju-Jeonnam five-pair event exceeds that baseline.

This study also does not hide or exclude the three-pair case. On the contrary, it includes 2014 and acknowledges more historical duplicates, then shows that five or more pairs still do not appear. That is a conservative test that includes evidence unfavorable to the researcher.

### 12.4 "Unit sizes and regional preferences invalidate the simple probability calculation."

Correct in part. Eup, myeon, and dong vote pairs are not fully independent and do not follow the same distribution. For that reason, this paper does not invent an arbitrary theoretical range under a uniform distribution. It uses an empirical \(K\) reverse-estimated from actual historical governor in-district early-vote data. It also presents a sensitivity analysis with a smaller effective pair space such as \(K=50,000\). Even in that case, the probability of five or more pairs is about 2.05%, which is still not a common event.

### 12.5 "The nationwide twelve cases were found after searching, so the probability is overstated."

Correct. The nationwide twelve cases were found after scanning multiple elections and regions, so the post-search problem is real. That is why this paper does not use the nationwide six pairs as the core test. The core test is the internal Gwangju-Jeonnam five-pair event. Because it is concentrated in the same candidate combination, same in-district early-vote category, and same metropolitan/provincial contest environment, the post-search objection is much smaller. The nationwide twelve cases are contextual, not the probability target of this paper.

### 12.6 "The 2026 data are not yet from an official integrated file."

This objection was valid against the earliest draft, but it no longer applies in that form. This study extracts the 2026 twelve event rows directly from the NEC election-statistics system's counting-unit result HTML. The reproduction script `scripts/fetch_nec_2026_duplicate_cases.py` performs POST queries with election ID `0020260603`, menu `VCCP08`, and election type `metropolitan/provincial governor election`, then parses candidate vote counts from in-district early-vote rows. The result is `outputs/nec_2026_reported_duplicate_cases.csv` for the twelve event rows and `outputs/nec_2026_reported_duplicate_pairs.csv` for the six identical vote pairs.

The remaining limitation is therefore not "press-report based." It is "based on official screen HTML extraction, but not yet cross-checked against the integrated XLSX file and original counting statements." This clarifies the level of the conclusion rather than weakening it. The identical vote-pair repetition is reproducible from official NEC election-statistics screen values. A legal conclusion about a specific misconduct mechanism still requires original counting statements, first-pass sorter results, reviewed-ballot allocation records, and input logs.

### 12.7 "Early-vote and election-day differences can be caused by voter self-selection."

Partly yes. For that reason, this paper does not use the early/election-day vote-share analysis as independent proof of misconduct. It is an auxiliary test. However, the fact that every analyzable constituency in the 2020 and 2024 National Assembly elections moves in the same direction is difficult to explain as simple sampling error. For the voter self-selection hypothesis to be sufficient, it must show that the remaining difference disappears after age, occupation, regional mobility, party-specific early-vote mobilization, COVID-era effects, and similar variables are accounted for.

### 12.8 "Rare events do sometimes occur."

Correct. Low probability does not mean impossibility. This paper therefore does not infer specific misconduct from low probability alone. In election-integrity settings, however, a low-probability structural anomaly is a reasonable trigger for raw-data audit. The conclusion of this study is not punishment or invalidation. It is an audit proposition: original counting statements, first-pass sorter results, reviewed-ballot allocation records, and data-entry logs should be disclosed.

### 12.9 "How can the claim be falsified?"

The claim is falsifiable. The conclusion should be weakened or withdrawn if any of the following is confirmed:

1. the reported values for the twelve 2026 identical-vote rows differ from the official original counting statements;
2. the Gwangju-Jeonnam five pairs were not in the same contest, same candidate combination, and same in-district early-vote category;
3. many cases of five or more repeated pairs inside one contest are found in comparable in-district early-vote governor data outside 2014, 2018, and 2022;
4. for all five 2026 pairs, first-pass sorter results, reviewed-ballot allocation, and input logs are independently consistent and document that the identical final values arose naturally through the counting process.

These falsification conditions are stated to make clear that this study is a testable statistical claim, not a political assertion.

## 13. Raw-Data Audit Decision Criteria

Whether a statistical anomaly connects to an actual administrative or counting-process cause cannot be determined from public screen values alone. The practical proposal of this study is therefore not a vague allegation, but a comparison of the following raw materials under the same event definition.

| Raw material | Question to answer | Result weakening the chance explanation | Result restoring the chance explanation |
| --- | --- | --- | --- |
| Original counting statements | Are the official screen values for the twelve event rows identical to the originals? | The originals also show the same twelve event rows and six identical pairs | The screen values differ from the originals and the identical pairs disappear |
| First-pass sorter results | Did the final identical pairs exist from the first sorting stage? | The first-pass results differed, but review/aggregation produced identical pairs | The values are independently consistent from first pass to final publication |
| Candidate allocation of reviewed ballots | Were reviewed ballots repeatedly allocated in a particular candidate direction? | Multiple pairs show repeated adjustment in the same candidate direction | Reviewed-ballot allocation is random-like and unrelated to the creation of identical pairs |
| Data-entry logs | Are input/correction timing and operator flows natural? | Abnormal correction or re-entry patterns concentrate in identical-pair rows | Logs are chronological and show no correction irregularity |
| Separated in-district/out-of-district data | Are identical pairs concentrated only in in-district early voting? | Identical pairs for the same candidate combination concentrate in in-district early voting | Similar repetition appears in in-district, out-of-district, and election-day data |

The purpose of this decision table is not to predetermine the conclusion. It also states what evidence would weaken this study. For example, if the original counting statements differ from the official screen values, or if the Gwangju-Jeonnam five pairs are not in the same candidate combination and in-district early-vote category, the core conclusion must be revised. Conversely, if the original records match the current screen values and the changes between first-pass results and final results repeatedly move toward identical pairs, the present statistical anomaly conclusion would be strengthened into a causal investigation.

The audit requested here is therefore not a total and abstract political audit. A limited disclosure for the twelve event rows, especially the Gwangju-Jeonnam five pairs, would narrow which explanation remains among coincidence, display error, reviewed-ballot allocation, and data-entry problems.

## 14. Conclusion

The repeated identical in-district early-vote pairs reported in the 2026 local election are statistically highly implausible. In particular, the report that five identical vote pairs appeared inside the Gwangju-Jeonnam contest environment, with the same candidate combination and same in-district early-vote category, is a strong anomaly under both the historical governor-election empirical distribution and the duplicate-probability model.

Across 51 past governor-election contests, the maximum observed number of repeated identical pairs inside one contest was three. The reported Gwangju-Jeonnam event has five pairs. When the effective vote-pair space is estimated from historical data, the Poisson approximation gives about 0.115% for such an event. In a separate nonparametric resampling test, zero out of 200,000 trials produced five or more pairs, and the rule-of-three 95% upper bound was about 0.0015%. This makes the simple coincidence explanation statistically very weak.

However, statistical improbability is not direct evidence of a specific act of misconduct. The event should be characterized as a statistical anomaly that is difficult to explain under the random-chance hypothesis, not as a final legal judgment. This distinction is not meant to weaken the conclusion. Even under the most skeptical interpretation, the currently public data do not provide a sufficient chance explanation. If election-management authorities wish to close the matter as mere coincidence or visual illusion, they must prove that explanation with raw records. To resolve the issue, the NEC or relevant institutions should disclose the original counting statements for all twelve rows, first-pass sorter results, candidate-by-candidate reviewed-ballot allocation records, and data-entry logs.

The core conclusion of the paper can be summarized in one sentence:

> The twelve 2026 in-district early-vote identical-pair rows, especially the five-pair repetition in Gwangju-Jeonnam, are too low-probability to be statistically closed as coincidence without raw-data disclosure and independent verification.

## 15. Data and Code Availability

The historical baseline analysis in this study is based on public National Election Commission and public-data portal records. The raw files used in the analysis, parsing scripts, probability scripts, and output CSVs are organized inside the submission package. The core outputs can be reproduced by following the procedure in `README.md`.

The 2026 local-election identical-vote-pair event values were checked by direct extraction from the NEC election-statistics system's counting-unit result HTML. The original HTML cache is included in `data/nec_2026_official_html/`, and parsed results are included in `outputs/nec_2026_reported_duplicate_cases.csv` and `outputs/nec_2026_reported_duplicate_pairs.csv`. Once the public-data portal's official integrated XLSX counting file or original counting statements are released, the scripts in this study should be applied under the same event definition to recompute the event values and repetition counts.

## 16. Research Ethics and Conflict of Interest

This study uses only public election data and public reports, and does not analyze personally identifying information or nonpublic personal data. The author does not assert the legal responsibility of any specific candidate, party, or election-management institution. The purpose of the study is to define the scope of raw-data disclosure and independent verification required when a low-probability repeated pattern is found.

The conclusion of this study is not "misconduct has been legally proven." It is the testable proposition that "the currently public data do not provide a sufficient chance explanation, and an official raw-data audit is required." This distinction is important for research ethics. The study should neither exaggerate a statistical anomaly into direct criminal evidence nor reduce a statistical anomaly to meaningless coincidence.

## Appendix A. Intuitive Meaning of Key Terms

| Term | Intuitive meaning |
| --- | --- |
| Null hypothesis | The default assumption that the observed pattern could arise by chance |
| Alternative hypothesis | The competing assumption that the pattern is difficult to treat as ordinary chance and requires another explanation |
| Poisson approximation | A standard approximation used to calculate how often rare events repeat |
| Counting unit | The smallest official result row used for comparison, such as an eup, myeon, or dong in-district early-vote row |
| In-district early voting | Early votes cast by voters within their registered district |
| Identical vote pair | Two counting units have the same first-candidate count and same second-candidate count |
| Effective pair space \(K\) | The practical range of first- and second-place candidate vote-count combinations that can actually appear in in-district early voting |
| Sensitivity analysis | A check of whether the conclusion remains similar when assumptions such as \(K\) or \(N\) are changed |
| Nonparametric resampling without replacement | A simulation that draws actual historical counting units without drawing the same unit twice |
| Rule of three | A conservative rule of thumb: if an event is observed zero times in \(n\) trials, its rough 95% upper bound is \(3/n\) |
| Tail probability | The probability of observing an extreme event far from the average case |
| Law of large numbers | The principle that, as sample size grows, the proportion in a random sample approaches the population proportion |
| Sign test | A nonparametric test that focuses on how often the direction of a difference repeats, rather than the size of the difference |
| Audit trigger | A signal strong enough to require raw-data disclosure and independent verification, without itself proving misconduct |

## Appendix B. Early Voting and the Law of Large Numbers

Public discussions often invoke the "law of large numbers" in early-vote debates, but that phrase alone cannot prove misconduct. The law of large numbers says that as sample size grows, the proportion in a random sample tends to approach the population proportion. To apply that principle to early voting, early voters and election-day voters would have to be randomly split from the same population. In real elections, this premise is incomplete because voters choose whether to vote early.

Nevertheless, the law-of-large-numbers discussion is not meaningless. If sample sizes are large and nearly every constituency shows an early-vote advantage in the same party direction, that pattern is difficult to treat as sampling error alone. This appendix checks that point using the simplest sign test.

For each constituency, the calculation asks whether the Democratic candidate's early-vote two-party share is higher than the same candidate's election-day two-party share. The null hypothesis is:

> If the early/election-day difference is not tilted toward one party direction, the probability that a constituency shows a Democratic early-vote advantage is roughly \(1/2\).

Under this null hypothesis, the probability that at least \(x\) out of \(n\) constituencies show a Democratic early-vote advantage is the one-sided tail probability:

\[
P(X \ge x) = \sum_{k=x}^{n} \binom{n}{k}\left(\frac{1}{2}\right)^n
\]

The same idea can be described in terms of the random variable:

\[
\Delta = p_E - p_D
\]

where \(\Delta\) is the difference between the early-vote share and election-day share. If simple sampling error is the main cause, the distribution of \(\Delta\) should fluctuate around zero. If most constituencies have \(\Delta>0\), and the center of the distribution moves toward roughly +10 percentage points, the pattern indicates systematic directionality. Whether that directionality is caused by voter self-selection, party mobilization, administrative processes, or another mechanism requires separate data. But the claim that it is not a statistical issue is difficult to sustain.

Direct parsing of official National Assembly data gives:

| Election | Constituencies | Democratic early advantage | Democratic early disadvantage | One-sided sign-test p-value | Intuitive frequency |
| --- | ---: | ---: | ---: | ---: | ---: |
| 2016 National Assembly | 229 | 211 | 18 | \(2.99 \times 10^{-43}\) | about 1 in \(3.35 \times 10^{42}\) |
| 2020 National Assembly | 236 | 236 | 0 | \(9.06 \times 10^{-72}\) | about 1 in \(1.10 \times 10^{71}\) |
| 2024 National Assembly | 245 | 245 | 0 | \(1.77 \times 10^{-74}\) | about 1 in \(5.65 \times 10^{73}\) |

The meaning of this calculation is limited but clear. If early/election-day differences were merely moving up and down like sampling error, the probability of seeing Democratic early-vote advantages in all 236 analyzable constituencies in 2020 and all 245 analyzable constituencies in 2024 would be extremely small under this simple model. Therefore "it only looked that way because the sample was large" is not a sufficient explanation under the symmetric sign-test null.

This result must not be read as direct proof of misconduct. The sign test does not remove alternative explanations such as voter self-selection, party-specific early-vote mobilization, age, occupation, regional mobility, or COVID-period voting effects. If those factors were strongly operating, the symmetric \(1/2\) null hypothesis would be weakened.

The appendix conclusion is therefore narrow. The same-direction early-vote pattern in the 2020 and 2024 National Assembly elections is statistically extremely unlikely under a simple sampling-error model. But it is an auxiliary anomaly indicator that supports the identical-vote-pair analysis; legal or administrative conclusions require constituency-level voter composition, campaign-mobilization evidence, separated in-district/out-of-district early-vote data, original counting statements, and first-pass sorter records.

## References

- National Election Commission, election-statistics system, counting-unit result pages.
- Public Data Portal, National Election Commission vote-counting data files for past elections.
- Public Data Portal, 2014 nationwide local election counting data.
- Public Data Portal, 2016 National Assembly election counting data.
- Public Data Portal, 2018 nationwide local election counting data.
- Public Data Portal, 2020 National Assembly election counting data.
- Public Data Portal, 2022 nationwide local election counting data.
- Public Data Portal, 2024 National Assembly election counting data.
- News1/Daum, June 6, 2026, report on identical vote counts in Songdo 1-dong and Songdo 2-dong.
- Hankyoreh, June 8, 2026, report on the Songdo identical-count controversy and election-management explanation.
- TV Chosun, June 8, 2026, report on identical in-district early-vote counts in twelve places nationwide.

## Reproduction Outputs

Key files in the package include:

- `outputs/dataset_counts.csv`
- `outputs/duplicate_summary.csv`
- `outputs/governor_actual_top2_summary.csv`
- `outputs/governor_actual_top2_by_contest.csv`
- `outputs/governor_actual_top2_duplicates.csv`
- `outputs/governor_bootstrap_summary.csv`
- `outputs/governor_bootstrap_histogram.csv`
- `outputs/nec_2026_gwangju_jeonnam_unit_counts.csv`
- `outputs/nec_2026_gwangju_jeonnam_units.csv`
- `outputs/nec_2026_gwangju_jeonnam_unit_summary.json`
- `outputs/nec_2026_reported_duplicate_cases.csv`
- `outputs/nec_2026_reported_duplicate_pairs.csv`
- `outputs/songdo_probability_summary.csv`
- `outputs/songdo_official_rows.csv`
- `outputs/probability_core.csv`
- `outputs/probability_k_sensitivity.csv`
- `outputs/probability_n_sensitivity.csv`
- `outputs/early_day_assembly_summary.csv`
- `outputs/early_day_assembly_twoparty.csv`
- `outputs/checksums_sha256.csv`
