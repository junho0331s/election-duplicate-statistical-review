# Submission Integrity Report

- Status: `pass`
- Scope: submission package integrity summary excluding final zip self-hash
- Core-claims verification: `pass`, 47 checks
- Statistical robustness audit: `pass`, 11 checks
- Video/source exclusion audit: `pass`, 25 files
- Source provenance audit: `pass`, 24 URLs
- Claim-boundary audit: `pass`, 22 checks
- Objection coverage audit: `pass`, 28 checks
- Pre-submission audit: `pass`, 17 checks
- Public-discussion claim audit: `pass`, 2 official rows
- Submission index audit: `pass`, 132 checks

## PDF Artifacts

- Korean PDF: `latex/ieie/main.pdf`, 16 pages, sha256 `38154dcf4b09be33ba938c6e8c046977c51de214e0f9c62e78952d88e8b52d87`
- English PDF: `latex/en/main_en.pdf`, 21 pages, sha256 `17441843f824d60d1ce6a573f7c6e139fb76f238b318534e41acf0fcd48a94f7`
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
