# Submission Integrity Report

- Status: `pass`
- Scope: submission package integrity summary excluding final zip self-hash
- Core-claims verification: `pass`, 45 checks
- Statistical robustness audit: `pass`, 10 checks
- Video/source exclusion audit: `pass`, 23 files
- Source provenance audit: `pass`, 24 URLs
- Claim-boundary audit: `pass`, 18 checks
- Objection coverage audit: `pass`, 22 checks
- Pre-submission audit: `pass`, 15 checks
- Submission index audit: `pass`, 102 checks

## PDF Artifacts

- Korean PDF: `latex/ieie/main.pdf`, 16 pages, sha256 `01334699241c28c67ae224f60fcd82f12be6fff1f580140b161e2661fcaa9ddd`
- English PDF: `latex/en/main_en.pdf`, 20 pages, sha256 `63fa036b25a9bc2548fc7fc3a372d5d275a1e0d38bb0a4862e305e4d0b3c533f`
- English PDF Korean-character count: `0`
- English PDF references `evidence_matrix_en.md`: `True`
- English PDF references `evidence_matrix_ko.md`: `False`

## Key Reproducible Numbers

- `historical_rows`: `81701`
- `historical_governor_contests`: `51`
- `gwangju_jeonnam_units_n`: `393`
- `effective_pair_space_k`: `100944.8`
- `poisson_p_at_least_5`: `0.0011484064248148407`
- `exact_collision_p_at_least_5`: `0.0012190883791786122`
- `bootstrap_trials`: `200000`
- `bootstrap_at_least_5_exceedances`: `0`
- `nec_2026_event_rows`: `12`
- `nec_2026_duplicate_pairs`: `6`

## Notes

This report intentionally excludes the final submission ZIP hash because the report itself is included in the ZIP. The ZIP hash is recorded in `dist/election_duplicate_ieie_submission.zip.sha256` and `dist/election_duplicate_ieie_submission_manifest.json`.
