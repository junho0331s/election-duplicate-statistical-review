#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs"
ZIP_PATH = ROOT / "dist" / "election_duplicate_ieie_submission.zip"
MANIFEST_PATH = ROOT / "dist" / "election_duplicate_ieie_submission_manifest.json"
SHA_PATH = ROOT / "dist" / "election_duplicate_ieie_submission.zip.sha256"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    OUT.mkdir(exist_ok=True)
    json_path = OUT / "local_ci_validation_report.json"
    md_path = OUT / "local_ci_validation_report.md"
    json_path.unlink(missing_ok=True)
    md_path.unlink(missing_ok=True)

    validate = subprocess.run(
        [sys.executable, "scripts/validate_package.py"],
        cwd=ROOT,
        env={**os.environ, "LOCAL_CI_VALIDATION_IN_PROGRESS": "true"},
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )

    digest = sha256(ZIP_PATH)
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    expected_sha_line = f"{digest}  {ZIP_PATH.name}"
    actual_sha_line = SHA_PATH.read_text(encoding="utf-8").strip()
    sidecar_pass = (
        manifest.get("sha256") == digest
        and manifest.get("bytes") == ZIP_PATH.stat().st_size
        and actual_sha_line == expected_sha_line
    )

    report = {
        "status": "pass" if validate.returncode == 0 and sidecar_pass else "fail",
        "scope": "local equivalent of .github/workflows/validate-submission.yml",
        "validate_package": {
            "command": "python scripts/validate_package.py",
            "returncode": validate.returncode,
            "passed": validate.returncode == 0,
            "output_tail": validate.stdout.strip().splitlines()[-20:],
        },
        "zip_sidecar": {
            "package": ZIP_PATH.name,
            "bytes": ZIP_PATH.stat().st_size,
            "sha256": digest,
            "manifest_sha256_matches": manifest.get("sha256") == digest,
            "manifest_bytes_matches": manifest.get("bytes") == ZIP_PATH.stat().st_size,
            "sha256_sidecar_matches": actual_sha_line == expected_sha_line,
            "file_count": manifest.get("file_count"),
            "passed": sidecar_pass,
        },
    }

    json_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    md_lines = [
        "# Local CI Validation Report",
        "",
        f"- Status: `{report['status']}`",
        f"- Scope: {report['scope']}",
        f"- Validation command: `{report['validate_package']['command']}`",
        f"- Validation return code: `{report['validate_package']['returncode']}`",
        f"- ZIP file count: `{report['zip_sidecar']['file_count']}`",
        f"- ZIP SHA256: `{report['zip_sidecar']['sha256']}`",
        f"- Manifest SHA256 matches ZIP: `{report['zip_sidecar']['manifest_sha256_matches']}`",
        f"- Manifest byte count matches ZIP: `{report['zip_sidecar']['manifest_bytes_matches']}`",
        f"- SHA256 sidecar matches ZIP: `{report['zip_sidecar']['sha256_sidecar_matches']}`",
        "",
        "## validate_package.py Output Tail",
        "",
    ]
    md_lines.extend(f"- `{line}`" for line in report["validate_package"]["output_tail"])
    md_lines.append("")
    md_path.write_text("\n".join(md_lines), encoding="utf-8")

    if report["status"] != "pass":
        raise SystemExit("Local CI validation failed")
    print(f"Local CI validation passed. Wrote {json_path.relative_to(ROOT)} and {md_path.relative_to(ROOT)}.")


if __name__ == "__main__":
    main()
