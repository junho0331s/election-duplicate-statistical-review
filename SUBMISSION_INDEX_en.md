# Submission Index

This document is the top-level guide for reviewers and independent validators. The scope of the conclusion is statistical anomaly and the need for raw-record audit. This document does not, by itself, determine a specific actor or legal liability.

## 1. Submission Package

- Submission ZIP: `dist/election_duplicate_ieie_submission.zip`
- ZIP hash sidecar: `dist/election_duplicate_ieie_submission.zip.sha256`
- ZIP manifest: `dist/election_duplicate_ieie_submission_manifest.json`

The ZIP hash is recorded in an external sidecar after ZIP creation. The final ZIP hash is not written inside documents included in the ZIP.

## 2. Manuscripts

- Korean PDF: `latex/ieie/main.pdf`
- English PDF: `latex/en/main_en.pdf`
- Korean LaTeX: `latex/ieie/main.tex`
- English LaTeX: `latex/en/main_en.tex`
- Korean Markdown manuscript: `paper_statistical_implausibility_ko.md`
- English Markdown manuscript: `paper_statistical_implausibility_en.md`

## 3. Reviewer-Facing Guides

- Claim-to-evidence matrix: `evidence_matrix_ko.md`, `evidence_matrix_en.md`
- Data dictionary: `DATA_DICTIONARY_ko.md`, `DATA_DICTIONARY_en.md`
- Quick reproduction guide: `REVIEWER_QUICKSTART_ko.md`, `REVIEWER_QUICKSTART_en.md`
- Reproducibility checklist: `REPRODUCIBILITY_CHECKLIST_ko.md`, `REPRODUCIBILITY_CHECKLIST_en.md`
- Statistical calculation note: `STATISTICAL_CALCULATION_NOTE_ko.md`, `STATISTICAL_CALCULATION_NOTE_en.md`
- 2026 data availability memo: `data_availability_2026_ko.md`, `data_availability_2026_en.md`
- Raw-data audit protocol: `AUDIT_PROTOCOL_ko.md`, `AUDIT_PROTOCOL_en.md`
- Alternative-explanations matrix: `ALTERNATIVE_EXPLANATIONS_MATRIX_ko.md`, `ALTERNATIVE_EXPLANATIONS_MATRIX_en.md`
- Look-elsewhere robustness note: `LOOK_ELSEWHERE_ROBUSTNESS_ko.md`, `LOOK_ELSEWHERE_ROBUSTNESS_en.md`
- Final submission checklist: `FINAL_SUBMISSION_CHECKLIST_ko.md`, `FINAL_SUBMISSION_CHECKLIST_en.md`

## 4. Core Verification Outputs

- Core-claims verification: `outputs/core_claims_verification.json` (`pass`, 45 checks)
- Statistical robustness audit: `outputs/statistical_robustness_audit.json` (`pass`, 10 checks)
- Informal video-source exclusion audit: `outputs/video_source_exclusion_audit.json` (`pass`, 23 files)
- Source provenance audit: `outputs/source_provenance_audit.json` (`pass`, 24 URLs)
- Claim-boundary audit: `outputs/claim_boundary_audit.json` (`pass`, 18 checks)
- Objection coverage audit: `outputs/objection_coverage_audit.json` (`pass`, 22 checks)
- Pre-submission audit: `outputs/pre_submission_audit.json` (`pass`, 15 checks)
- Submission integrity report: `outputs/submission_integrity_report.json`
- Submission index audit: `outputs/submission_index_audit.json`

## 5. Post-ZIP External Validation Outputs

- Independent ZIP reproduction audit: `outputs/zip_reproduction_audit.json`
- Local CI validation report: `outputs/local_ci_validation_report.json`

These two outputs are generated after the final ZIP is created. They are kept outside the submission ZIP to avoid checksum self-reference cycles.

## 6. Quick Reproduction Command

```bash
python3 -m pip install -r requirements.txt
python3 scripts/run_all.py
```

If the full reproduction succeeds, the artifacts under `outputs/`, `latex/`, and `dist/` are regenerated and `scripts/validate_package.py` verifies the submission package structure.
