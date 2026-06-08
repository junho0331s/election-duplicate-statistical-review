# ZIP Reproduction Audit

- Status: `pass`
- Scope: fresh extraction of the submission ZIP into an isolated temporary directory
- Package: `election_duplicate_ieie_submission.zip`
- Required extracted files checked: `11`
- Missing required extracted files: `0`

## Commands

- `python scripts/verify_core_claims.py` -> return code `0`
- `python scripts/statistical_robustness_audit.py` -> return code `0`
- `python scripts/video_source_exclusion_audit.py` -> return code `0`
- `python scripts/source_provenance_audit.py` -> return code `0`
- `python scripts/claim_boundary_audit.py` -> return code `0`
- `python scripts/objection_coverage_audit.py` -> return code `0`
- `python scripts/pre_submission_audit.py` -> return code `0`
