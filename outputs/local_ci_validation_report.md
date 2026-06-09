# Local CI Validation Report

- Status: `pass`
- Scope: local equivalent of .github/workflows/validate-submission.yml
- Validation command: `python scripts/validate_package.py`
- Validation return code: `0`
- ZIP file count: `146`
- ZIP SHA256: `e6c630c9c6962189271d4c807b7d5aec217d0df09b009af6a445461f6b2834a8`
- ZIP reproduction audit command: `python scripts/zip_reproduction_audit.py`
- ZIP reproduction audit return code: `0`
- Manifest SHA256 matches ZIP: `True`
- Manifest byte count matches ZIP: `True`
- SHA256 sidecar matches ZIP: `True`

## validate_package.py Output Tail

- `Package validation passed.`

## zip_reproduction_audit.py Output Tail

- `ZIP reproduction audit passed. Wrote outputs/zip_reproduction_audit.json and outputs/zip_reproduction_audit.md.`
