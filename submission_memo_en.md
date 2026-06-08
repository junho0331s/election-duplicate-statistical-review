# Submission Memo: Repeated Identical In-District Early-Vote Pair Analysis

## Manuscript Information

- Title: Repeated Identical In-District Early-Vote Pairs That Overwhelm the Random-Chance Hypothesis: Statistical Anomalies in the 2026 Korean Local Election and the Need for Raw-Data Audit
- Author: Junho Kim
- Affiliation: None
- Email: junhokim0331@gmail.com
- Manuscript file: `paper_statistical_implausibility_en.md`
- LaTeX source: `latex/en/main_en.tex`
- Compiled PDF: `latex/en/main_en.pdf`
- Reproduction guide: `README.md`
- Reviewer-response memo: `reviewer_response_en.md`
- Evidence matrix: `evidence_matrix_en.md`
- Analysis type: Public-data statistical review and raw-data audit trigger

## One-Sentence Summary

The Gwangju-Jeonnam five-pair repetition in the 2026 in-district early-vote results, rechecked from official National Election Commission election-statistics page values, is rare relative to historical governor-election benchmarks and cannot be statistically closed as ordinary chance without independent verification of original counting records and first-pass sorter outputs.

## Core Contributions

1. The package parses 81,701 official counting-unit rows from public election files covering 2014 through 2025.
2. The paper recalculates 51 governor in-district early-vote contests from 2014, 2018, and 2022 using actual first- and second-place candidates.
3. In that historical governor benchmark, the maximum repeated identical top-two pair count within one contest is three, and no contest reaches five.
4. With \(K=100,944.8\) inferred from historical data and \(N=393\) official-page Gwangju-Jeonnam in-district early-vote units, the probability of five or more repeated pairs is approximately 0.115%.
5. In 200,000 nonparametric resampling trials drawing 393 units without replacement from historical governor actual vote pairs, five or more repeated pairs occur zero times; the rule-of-three 95% upper bound is approximately 0.0015%.
6. The Incheon Songdo case is analyzed separately as an auxiliary audit signal. The probability that the specific Songdo 1-dong and Songdo 2-dong pair shares the same top-two vote pair is approximately 0.000991% under the same \(K\) benchmark.
7. The 2016, 2020, and 2024 National Assembly early-vote/election-day comparison is included only as an auxiliary directional-pattern check, not as direct proof of misconduct.

## Claim Boundary

The manuscript does not assert that a specific person, institution, or technical process has been legally proven to have committed election misconduct. The defensible claim is:

> Given the current official-page values and the stated event definition, the 2026 Gwangju-Jeonnam five-pair repetition is a statistical anomaly that is difficult to reconcile with the ordinary-randomness hypothesis and requires official raw-data disclosure and independent audit.

This boundary is not a weakening of the paper. It is the strongest claim that can be defended from the current public package without overclaiming causal or legal conclusions.

## Main Limitations

1. The 2026 event values are extracted from official NEC election-statistics HTML pages, not from a historical-style integrated public-data XLSX file.
2. When the 2026 integrated XLSX file or original counting statements become available, the twelve event rows and six duplicate pairs should be recalculated.
3. The Poisson approximation is a simplified rare-collision model; the package therefore also includes \(K\)-sensitivity, \(N\)-sensitivity, and nonparametric resampling checks.
4. The early-vote/election-day analysis cannot remove all lawful explanations such as voter self-selection, party mobilization, demographic composition, and pandemic-era voting behavior.

## Reproduction Command

```bash
python3 -m pip install -r requirements.txt
python3 scripts/run_all.py
```

## Key Reproducible Numbers

| Item | Value |
| --- | ---: |
| Historical parsed rows | 81,701 |
| Governor contests | 51 |
| Actual top-two governor comparison pairs | 1,514,172 |
| Historical governor identical vote pairs | 15 |
| Historical maximum within one contest | 3 pairs |
| Estimated \(K\) | 100,944.8 |
| \(N=393\), probability of five or more pairs | 0.115% |
| \(N=393\), probability of six or more pairs | 0.0143% |
| Yeonsu in-district early-vote probability of at least one duplicate pair | 0.104% |
| Conditional probability for the specific Songdo 1/Songdo 2 pair | 0.000991% |

## Anticipated Reviewer Questions

### 1. "If three pairs occurred historically, why is five special?"

Three pairs is the observed maximum across 51 historical governor contests. Five exceeds that historical upper value. Under the same \(N=393, K=100,945\) benchmark, \(P(C \geq 3)\) is approximately 4.23%, while \(P(C \geq 5)\) is approximately 0.115%, about 37 times smaller.

### 2. "Is the nationwide twelve-case set vulnerable to post-search bias?"

Yes. The paper therefore does not use the nationwide twelve cases as the main probability event. The main test is the Gwangju-Jeonnam internal five-pair cluster, defined within the same top-two candidate combination, vote type, and contest environment.

### 3. "Do unit size and regional preference invalidate the calculation?"

They can affect any simple probability model. For that reason, the paper estimates \(K\) from actual historical Korean governor data and reports sensitivity and resampling checks. A stronger benign explanation should provide a covariate-adjusted model that generates five-pair clusters at non-negligible frequency under the same event definition.

### 4. "Does the absence of the 2026 integrated XLSX file invalidate the paper?"

No, but it bounds the conclusion. The official-page values are sufficient to define a reproducible statistical audit trigger. Final administrative or legal conclusions require the integrated file, original counting statements, first-pass sorter outputs, reviewed-ballot allocation records, and input logs.

### 5. "Can rare events happen naturally?"

Yes. The paper does not treat rarity as impossibility. It treats the pattern as a reason to move from public aggregate data to raw-record audit.

### 6. "Is the Songdo case merged into the Gwangju-Jeonnam probability calculation?"

No. Songdo belongs to a different contest and is reported as a separate auxiliary case. Its role is to motivate a narrower raw-record question about first-pass values, reviewed-ballot allocation, and final equality in the two named Songdo units.

## Required Raw Records for Stronger Conclusions

1. 2026 integrated public-data counting-unit file.
2. Original counting statements for the twelve event rows.
3. Ballot-sorter first-pass outputs for the affected units.
4. Reviewed-ballot candidate allocation records.
5. Manual count, correction, data-entry, and publication logs.
6. Chain-of-custody records for the affected ballot boxes or counting batches.

## Package Contents

- `paper_statistical_implausibility_en.md`
- `cover_letter_en.md`
- `submission_memo_en.md`
- `reviewer_response_en.md`
- `evidence_matrix_en.md`
- `REPRODUCIBILITY_CHECKLIST_en.md`
- `STATISTICAL_CALCULATION_NOTE_en.md`
- `data_availability_2026_en.md`
- `latex/en/main_en.tex`
- `latex/en/main_en.pdf`
- `README.md`
- `requirements.txt`
- `latex/`
- `scripts/`
- `outputs/`
- `data/`
- `dist/election_duplicate_ieie_submission.zip`
