# Reproducibility Checklist

## Purpose

This checklist helps reviewers and independent readers reproduce the core calculations in the submission package. The paper's conclusion is not a final legal attribution of cause. It is a reproducible statistical claim: public official-page values and official historical data identify a statistical anomaly that requires raw-data audit.

## Runtime Environment

- Python 3.10 or later
- Python packages listed in `requirements.txt`
- XeLaTeX if the PDFs need to be rebuilt

## Full Reproduction Command

Run the following commands from the package root:

```bash
python3 -m pip install -r requirements.txt
python3 scripts/run_all.py
```

On success, the final output should state the following:

```text
All reproduction scripts completed, package validation passed, and expected outputs exist.
```

## Core Outputs and Expected Values

| Check item | Expected value | File to inspect |
| --- | ---: | --- |
| Historical parsed rows | 81,701 | `outputs/dataset_counts.csv` |
| Governor constituency contests | 51 | `outputs/governor_actual_top2_summary.csv` |
| Governor actual top-two comparison pairs | 1,514,172 | `outputs/governor_actual_top2_summary.csv` |
| Historical identical vote pairs | 15 | `outputs/governor_actual_top2_summary.csv` |
| Historical maximum repeated pairs within one contest | 3 pairs | `outputs/governor_actual_top2_summary.csv` |
| Gwangju-Jeonnam in-district early-vote counting units | 393 | `outputs/nec_2026_gwangju_jeonnam_unit_summary.json` |
| 2026 official-page event rows | 12 | `outputs/nec_2026_reported_duplicate_cases.csv` |
| 2026 official-page identical vote pairs | 6 pairs | `outputs/nec_2026_reported_duplicate_pairs.csv` |
| \(P(C \geq 5)\) at \(N=393\) | 0.0011484064248148407 | `outputs/probability_core.csv` |
| \(P(C \geq 6)\) at \(N=393\) | 0.00014322422035484283 | `outputs/probability_core.csv` |
| Probability of at least one identical pair inside Yeonsu | 0.0010396316588441312 | `outputs/songdo_probability_summary.csv` |
| Conditional probability of the specific Songdo 1/Songdo 2 identical pair | 0.000009906404292246851 | `outputs/songdo_probability_summary.csv` |
| Nonparametric resampling repetitions | 200,000 | `outputs/governor_bootstrap_summary.csv` |
| Nonparametric resampling hits for \(C \geq 5\) | 0 | `outputs/governor_bootstrap_summary.csv` |
| Rule-of-three 95% upper bound for \(C \geq 5\) | 0.000015 | `outputs/governor_bootstrap_summary.csv` |
| 2020 National Assembly constituencies with Democratic early-vote advantage | 236/236 | `outputs/early_day_assembly_summary.csv` |
| 2024 National Assembly constituencies with Democratic early-vote advantage | 245/245 | `outputs/early_day_assembly_summary.csv` |

## Integrity Checks

`outputs/checksums_sha256.csv` contains SHA-256 hashes for major source files, scripts, output CSVs, and PDFs. After receiving the submission ZIP, check that:

1. `latex/ieie/main.pdf` is present.
2. `latex/en/main_en.pdf` is present.
3. `outputs/checksums_sha256.csv` is present.
4. `outputs/governor_bootstrap_summary.csv` is present.
5. `outputs/nec_2026_gwangju_jeonnam_unit_summary.json` is present.
6. `outputs/nec_2026_reported_duplicate_cases.csv` is present.
7. `paper_statistical_implausibility_ko.md` and `paper_statistical_implausibility_en.md` are present.
8. `reviewer_response_en.md` and `evidence_matrix_en.md` are present.
9. LaTeX byproducts such as `.aux`, `.log`, `.out`, and `.synctex.gz` are absent from the ZIP.

These conditions are automatically checked by:

```bash
python3 scripts/validate_package.py
```

## Interpretation Standard

If the values above are reproduced, the paper's core conclusion is supported within this scope:

> Taken together, the NEC official page values and the historical official-data baseline indicate that the 2026 Gwangju-Jeonnam five-pair repetition is a statistical anomaly difficult to reconcile with the ordinary-randomness hypothesis, and independent verification of original counting statements and first-pass sorter records is required.

The conclusion should be weakened or revised if any of the following is confirmed:

1. The official 2026 integrated file or original counting statements show event-row values different from the current official-page values.
2. The Gwangju-Jeonnam five-pair set is not a repeated pattern within the same top-two candidate combination, same in-district early-vote category, and same contest environment.
3. Comparable official governor in-district early-vote data under the same institutional regime show many contests with five or more repeated pairs.
4. For all five Gwangju-Jeonnam pairs, first-pass sorter outputs, reviewed-ballot allocations, and input logs independently reconcile the identical final pairs as ordinary documented counting outcomes.

