# Submission Integrity Report

- Status: `pass`
- Scope: submission package integrity summary excluding final zip self-hash
- Core-claims verification: `pass`, 45 checks
- Statistical robustness audit: `pass`, 10 checks
- Video/source exclusion audit: `pass`, 23 files
- Source provenance audit: `pass`, 15 URLs
- Claim-boundary audit: `pass`, 18 checks
- Objection coverage audit: `pass`, 22 checks
- Pre-submission audit: `pass`, 15 checks

## PDF Artifacts

- Korean PDF: `latex/ieie/main.pdf`, 15 pages, sha256 `3d74423670e56158e665ab36f754e00e17274d596fb29268b0028e3387ba3683`
- English PDF: `latex/en/main_en.pdf`, 18 pages, sha256 `4b778bd13f239b3153d3ac7da1a2ef18371f767883f0ffd6348420ff2adac584`
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
