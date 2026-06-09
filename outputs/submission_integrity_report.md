# Submission Integrity Report

- Status: `pass`
- Scope: submission package integrity summary excluding final zip self-hash
- Core-claims verification: `pass`, 47 checks
- Statistical robustness audit: `pass`, 11 checks
- Video/source exclusion audit: `pass`, 25 files
- Source provenance audit: `pass`, 24 URLs
- Claim-boundary audit: `pass`, 22 checks
- Objection coverage audit: `pass`, 30 checks
- Pre-submission audit: `pass`, 17 checks
- Public-discussion claim audit: `pass`, 2 official rows
- Submission index audit: `pass`, 132 checks

## PDF Artifacts

- Korean PDF: `latex/ieie/main.pdf`, 16 pages, sha256 `a5d35998090fda8f69d5f9d7279d85989f75dfbcbd7f025a1247a12b55075b43`
- English PDF: `latex/en/main_en.pdf`, 21 pages, sha256 `021d16f0375e0c28aeb8b6ddef5a46bb1b9a1e56040577ec4b1d25c664d1c73e`
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
- `designated_five_pair_conditional_probability`: `9.540700009422666e-26`
- `bootstrap_trials`: `200000`
- `bootstrap_at_least_5_exceedances`: `0`
- `nec_2026_event_rows`: `12`
- `nec_2026_duplicate_pairs`: `6`

## Notes

This report intentionally excludes the final submission ZIP hash because the report itself is included in the ZIP. The ZIP hash is recorded in `dist/election_duplicate_ieie_submission.zip.sha256` and `dist/election_duplicate_ieie_submission_manifest.json`.
