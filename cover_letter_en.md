# Submission Cover Letter

Dear Editor,

I submit the manuscript, *Repeated Identical In-District Early-Vote Pairs That Overwhelm the Random-Chance Hypothesis: Statistical Anomalies in the 2026 Korean Local Election and the Need for Raw-Data Audit*.

The purpose of this manuscript is to examine whether the repeated identical vote-pair pattern reported after the 2026 Korean local election, and rechecked against official National Election Commission election-statistics page values, is compatible with the historical empirical baseline from official counting data. The main event is defined as five repeated identical top-two candidate vote pairs in the Gwangju-Jeonnam governor in-district early-vote results. The study also reports auxiliary checks using official National Assembly data from 2016, 2020, and 2024.

The manuscript makes three main contributions.

1. It provides a reproducible package built from 81,701 official counting-unit rows from public election files covering 2014 through 2025.
2. It constructs a historical benchmark using actual first- and second-place candidate vote pairs in 51 governor contests from the 2014, 2018, and 2022 local elections, finding that the historical maximum repeated-pair count within one contest is three.
3. It shows that, using \(N=393\) official-page Gwangju-Jeonnam in-district early-vote units and \(K=100,944.8\) inferred from historical official data, the Poisson-approximation probability of observing five or more repeated pairs is approximately 0.115%.
4. It separately reports that, if the five observed Gwangju-Jeonnam pairings are treated as designated pairings, the conditional probability that all five match is approximately \(9.54\times10^{-26}\).

The paper does not claim that a specific person, institution, or procedure has been legally proven to have committed misconduct. Its claim is narrower and reproducible: under the stated event definition and currently available official-page values, the Gwangju-Jeonnam five-pair repetition is difficult to close as ordinary chance without disclosure and independent verification of original counting statements, first-pass sorter outputs, reviewed-ballot allocation records, and related logs.

The submission package includes the Korean and English manuscripts, compiled PDFs, LaTeX sources, reproduction scripts, public source files, intermediate outputs, checksum records, reviewer-response memoranda, evidence matrices, reproducibility checklists, statistical calculation notes, and data-availability memoranda. The main numerical outputs can be regenerated with:

```bash
python3 scripts/run_all.py
```

The package can be validated with:

```bash
python3 scripts/validate_package.py
```

At the time of submission, the 2026 local-election integrated public-data XLSX file comparable to the historical public-data files was not included in the package. The twelve 2026 event rows are instead rechecked from official National Election Commission election-statistics HTML pages, with cached source files and parsed outputs included. When the integrated public-data file or original counting statements become available, the event definition should be reapplied and the calculations rerun.

I believe the manuscript can contribute to discussions on election-data auditing, duplicate-probability modeling, public-data reproducibility, and statistically disciplined election-integrity review.

Sincerely,

Junho Kim  
No affiliation  
junhokim0331@gmail.com
