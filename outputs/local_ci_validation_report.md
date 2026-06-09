# Local CI Validation Report

- Status: `pass`
- Scope: local equivalent of .github/workflows/validate-submission.yml
- Validation command: `python scripts/validate_package.py`
- Validation return code: `0`
- ZIP file count: `147`
- ZIP SHA256: `4d7e42789f19d6342793ecb8ee745bd5c7d3d9c09e16a3805c36de0ecc5666ba`
- ZIP reproduction audit command: `python scripts/zip_reproduction_audit.py`
- ZIP reproduction audit return code: `0`
- Manifest SHA256 matches ZIP: `True`
- Manifest byte count matches ZIP: `True`
- SHA256 sidecar matches ZIP: `True`

## validate_package.py Output Tail

- `Package validation passed.`

## zip_reproduction_audit.py Output Tail

- `ZIP reproduction audit passed. Wrote outputs/zip_reproduction_audit.json and outputs/zip_reproduction_audit.md.`
