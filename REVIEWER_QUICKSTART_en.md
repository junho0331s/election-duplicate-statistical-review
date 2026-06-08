# Reviewer Reproduction Quickstart

This document gives reviewers and independent validators a 5- to 10-minute path for checking whether the manuscript's core reproducible claims match the files and scripts in this package. The purpose is not to determine a legal cause. The purpose is to verify that the public-data calculations in the paper are actually reproducible.

## 0. Verification Scope

This Quickstart checks the following items.

- `12` event rows rechecked from official NEC election-statistics HTML
- `6` identical vote pairs formed by those event rows
- `5` identical vote pairs in the internal Gwangju-Jeonnam event
- `N=393` Gwangju-Jeonnam in-district early-vote counting units from official NEC HTML
- Historical maximum of `3` repeated pairs inside one constituency contest across `51` governor contests
- `P(C >= 5) = 0.0011484064`, approximately `0.115%`, under `N=393` and `K=100,944.8`
- Exact pair-collision `P(C >= 5) = 0.0012190884`, approximately `0.122%`, under `N=393` and `K=100945`
- `0` occurrences of `C >= 5` in `200,000` nonparametric resampling trials from historical actual vote pairs
- Sign-test inputs showing that in the 2020 and 2024 National Assembly elections every analyzable constituency had a higher Democratic two-party share in early voting than on election day
- Auxiliary probability values for the Incheon Songdo case

This Quickstart does not verify the following items.

- Full agreement between original counting statements and official screen values
- Candidate-by-candidate changes between first-pass sorter results and final published values
- Candidate allocation of reviewed ballots
- Data-entry and correction logs
- Legal responsibility of any specific actor

The package conclusion is therefore limited to a statistical anomaly in public data and the need for raw-record audit.

## 1. Minimal Check

Run the following commands at the package root.

```bash
python3 -m pip install -r requirements.txt
python3 scripts/verify_core_claims.py
python3 scripts/validate_package.py
```

Expected output:

```text
Core claim verification passed with 45 checks.
Package validation passed.
```

`verify_core_claims.py` checks 45 core numerical claims against the output files. `validate_package.py` checks required files, forbidden informal-source strings, core CSV and JSON values, English PDF translation coverage, checksums, ZIP package contents, and the external local ZIP-reproduction audit.

## 2. Full Reproduction

To rebuild the outputs from the analysis scripts, run:

```bash
python3 scripts/run_all.py
```

The expected result is successful completion of all analysis scripts, core-claim verification, checksum generation, ZIP generation, and package validation. After reproduction, check that the following files were refreshed.

- `outputs/core_claims_verification.json`
- `outputs/core_claims_verification.csv`
- `outputs/checksums_sha256.csv`
- `dist/election_duplicate_ieie_submission.zip`

## 3. Core Files

Reviewers should inspect these files first.

| Purpose | File |
|---|---|
| Machine-readable core-claim verification | `outputs/core_claims_verification.json` |
| Spreadsheet-readable core-claim verification | `outputs/core_claims_verification.csv` |
| 2026 event rows | `outputs/nec_2026_reported_duplicate_cases.csv` |
| 2026 identical vote pairs | `outputs/nec_2026_reported_duplicate_pairs.csv` |
| Historical governor baseline summary | `outputs/governor_actual_top2_summary.csv` |
| Historical governor duplicate details | `outputs/governor_actual_top2_duplicates.csv` |
| Core Poisson probabilities | `outputs/probability_core.csv` |
| Exact pair-collision probabilities | `outputs/probability_exact_collision.csv` |
| Nonparametric resampling result | `outputs/governor_bootstrap_summary.csv` |
| Early-vote versus election-day sign test | `outputs/early_day_assembly_summary.csv` |
| Incheon Songdo auxiliary probability | `outputs/songdo_probability_summary.csv` |
| Output data dictionary | `DATA_DICTIONARY_en.md` |
| Claim-to-file mapping | `evidence_matrix_en.md` |

## 4. Numerical Checklist

| Claim | Expected value | Source file |
|---|---:|---|
| Parsed historical rows | `81,701` | `outputs/dataset_counts.csv` |
| Historical governor contests | `51` | `outputs/governor_actual_top2_summary.csv` |
| Actual top-two comparison pairs | `1,514,172` | `outputs/governor_actual_top2_summary.csv` |
| Historical identical vote pairs | `15` | `outputs/governor_actual_top2_summary.csv` |
| Historical maximum inside one contest | `3` | `outputs/governor_actual_top2_summary.csv` |
| Gwangju-Jeonnam in-district early-vote units | `393` | `outputs/nec_2026_gwangju_jeonnam_unit_summary.json` |
| Estimated effective vote-pair space | `100,944.8` | `outputs/governor_actual_top2_summary.csv` |
| `P(C >= 5)` | `0.0011484064` | `outputs/probability_core.csv` |
| Exact pair-collision `P(C >= 5)` | `0.0012190884` | `outputs/probability_exact_collision.csv` |
| Nonparametric resampling `C >= 5` | `0 / 200,000` | `outputs/governor_bootstrap_summary.csv` |
| 2026 event rows | `12` | `outputs/nec_2026_reported_duplicate_cases.csv` |
| 2026 identical vote pairs | `6` | `outputs/nec_2026_reported_duplicate_pairs.csv` |

## 5. Interpretation Rule

If the verification scripts pass, the reviewer can confirm that the manuscript's core statistical values match the public-data outputs in this package. That result is not a cause determination. Cause determination requires original counting statements, first-pass sorter records, reviewed-ballot allocation records, and data-entry logs. The paper's practical request is that those raw records be disclosed so that chance, display error, review or aggregation procedure, and data-entry explanations can be independently distinguished.
