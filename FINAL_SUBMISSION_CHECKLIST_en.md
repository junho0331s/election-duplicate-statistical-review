# Final Pre-Submission Checklist

This checklist is for the final pass before academic submission. It verifies that the manuscript and reproduction package state the same conclusion, numbers, limitations, and audit request.

Verification status: as of 2026-06-09 KST, `python3 scripts/run_all.py` and `python3 scripts/validate_package.py` pass. The core-claim verification file `outputs/core_claims_verification.json` reports `pass` with 45 checks. The statistical robustness audit file `outputs/statistical_robustness_audit.json` reports `pass` with 10 checks. The video-source exclusion audit file `outputs/video_source_exclusion_audit.json` reports `pass` across 25 checked files. The public-discussion auxiliary-claim audit file `outputs/public_discussion_claims_audit.json` reports `pass` with two official-data rows checked. The claim-boundary audit file `outputs/claim_boundary_audit.json` reports `pass` with 18 checks. The objection coverage audit file `outputs/objection_coverage_audit.json` reports `pass` with 24 checks. The pre-submission audit file `outputs/pre_submission_audit.json` reports `pass` with 17 checks.

## 1. Claim Boundary

- [x] The manuscript does not state that a specific person, institution, or party has been legally proven to have committed a crime.
- [x] The conclusion remains: public data show a statistical anomaly requiring raw-data disclosure and independent audit.
- [x] The paper distinguishes "very low probability under the chance hypothesis" from "direct proof of misconduct."
- [x] The Gwangju-Jeonnam five-pair cluster is the primary test; the nationwide six-pair set and the Songdo case are kept separate or auxiliary.
- [x] The early-vote versus election-day analysis is framed as an auxiliary anomaly indicator and does not claim to remove voter self-selection, party mobilization, or other lawful explanations.

## 2. Source and Evidence Policy

- [x] The manuscript and support documents do not use informal video-platform materials, subtitles, or video-derived claims as evidence.
- [x] The 2026 event rows are described as values rechecked against cached official NEC election-statistics HTML and parsed outputs.
- [x] The historical baseline is reproducible from public official election files and public-data files.
- [x] Media reports are used only to define the initially reported event and public context; the core numerical checks are tied to official page values and reproducible scripts.

## 3. Core Numerical Consistency

Before submission, verify that the following values match across the README, Korean paper, English paper, PDFs, calculation notes, and output CSVs.

| Item | Baseline value |
| --- | ---: |
| Parsed historical rows | 81,701 |
| Historical governor contests | 51 |
| Actual top-two comparison pairs | 1,514,172 |
| Actual top-two identical vote pairs | 15 |
| Historical maximum repeated pairs within one contest | 3 pairs |
| Gwangju-Jeonnam in-district early-vote units | 393 |
| Empirical \(K\) | 100,944.8 |
| \(P(C \ge 5)\), \(N=393\) | 0.0011484064, about 0.115% |
| Exact pair-collision \(P(C \ge 5)\), \(N=393\), \(K=100,945\) | 0.0012190884, about 0.122% |
| \(P(C \ge 6)\), \(N=393\) | 0.0001432242, about 0.0143% |
| Nonparametric resampling trials | 200,000 |
| Nonparametric resampling \(C \ge 5\) | 0 hits |
| Yeonsu 15-unit probability of at least one pair | about 0.104% |
| Specific Songdo 1-dong/Songdo 2-dong pair probability | about 0.000991% |
| 2026 official HTML event rows rechecked | 12 |
| 2026 official HTML duplicate pairs rechecked | 6 |

## 4. Korean and English Manuscripts and PDFs

- [x] Korean PDF `latex/ieie/main.pdf` is newer than `latex/ieie/main.tex`.
- [x] English PDF `latex/en/main_en.pdf` is newer than `latex/en/main_en.tex`.
- [x] The English PDF is a full translation and includes the conclusion, data and code availability, research ethics, appendices, references, and reproduction outputs.
- [x] The English PDF contains no Korean body-text fragments.
- [x] The English early-vote/election-day table does not contain stale `2016 118/111` or `about 0.35` values.
- [x] The English manuscript uses the current checked values: 2016 211/18, mean +3.90 percentage points, and all-constituency directionality in 2020 and 2024.

## 5. Raw-Data Limitation and Audit Request

- [x] The manuscript does not hide the limitation that the 2026 official integrated XLSX file or original counting statements have not yet been obtained.
- [x] This limitation is used to bound the conclusion as a statistical anomaly requiring raw-data audit, not as a legal finding.
- [x] `AUDIT_PROTOCOL_ko.md` and `AUDIT_PROTOCOL_en.md` are included in the submission package.
- [x] The audit protocol requests original counting statements, first-pass ballot-sorter results, candidate allocation of reviewed ballots, data-entry/correction logs, and file hashes.
- [x] The audit protocol includes falsification criteria. If raw records explain the anomaly through ordinary chance or lawful procedure, that conclusion must be accepted.

## 6. Reproduction and Package Validation

Run the following commands before submission.

```bash
python3 -m pip install -r requirements.txt
python3 scripts/run_all.py
python3 latex/convert_to_ieie.py
cd latex/ieie
xelatex -interaction=nonstopmode -halt-on-error main.tex
xelatex -interaction=nonstopmode -halt-on-error main.tex
cd ../..
cd latex/en
xelatex -interaction=nonstopmode -halt-on-error main_en.tex
xelatex -interaction=nonstopmode -halt-on-error main_en.tex
cd ../..
python3 scripts/generate_checksums.py
python3 scripts/create_submission_zip.py
python3 scripts/validate_package.py
```

If there is not enough time to rerun the full reproduction pipeline, at minimum the following command must pass.

```bash
python3 scripts/validate_package.py
```

## 7. Submission ZIP Contents

- [x] `dist/election_duplicate_ieie_submission.zip` is newer than the checksum file.
- [x] `dist/election_duplicate_ieie_submission.zip.sha256` and `dist/election_duplicate_ieie_submission_manifest.json` record the submission ZIP's own hash and file count.
- [x] The ZIP includes Korean and English papers, Korean and English PDFs, cover letters, submission memos, reviewer-response memos, evidence matrices, calculation notes, data-availability memos, audit protocols, reproduction scripts, outputs, and data.
- [x] The ZIP does not include LaTeX temporary files such as `.aux`, `.log`, `.out`, or `.synctex.gz`.
- [x] The ZIP may exceed GitHub's recommended file-size warning threshold; if needed, upload it separately for the academic submission system.

## 8. Final Sentence Check

Before submission, keep the abstract and conclusion aligned with the following claim:

> This study does not establish a legal finding of specific misconduct. It shows that public official data and reproducible calculations reveal a statistical anomaly that cannot be closed by the chance hypothesis alone, and that resolving it requires independent audit of original counting statements, first-pass sorter results, reviewed-ballot candidate allocation, and data-entry/correction logs.

Remove stronger language that legally concludes "crime," "manipulation," or "confirmed misconduct" from the academic submission version.
