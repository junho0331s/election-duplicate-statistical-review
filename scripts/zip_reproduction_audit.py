#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from dataclasses import asdict, dataclass
from pathlib import Path
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs"
ZIP_PATH = ROOT / "dist" / "election_duplicate_ieie_submission.zip"

COMMANDS = [
    ["scripts/verify_core_claims.py"],
    ["scripts/statistical_robustness_audit.py"],
    ["scripts/video_source_exclusion_audit.py"],
    ["scripts/source_provenance_audit.py"],
    ["scripts/claim_boundary_audit.py"],
    ["scripts/objection_coverage_audit.py"],
    ["scripts/pre_submission_audit.py"],
]

REQUIRED_EXTRACTED_FILES = [
    "README.md",
    "paper_statistical_implausibility_ko.md",
    "paper_statistical_implausibility_en.md",
    "latex/ieie/main.pdf",
    "latex/en/main_en.pdf",
    "scripts/verify_core_claims.py",
    "scripts/zip_reproduction_audit.py",
    "outputs/core_claims_verification.json",
    "outputs/statistical_robustness_audit.json",
    "outputs/video_source_exclusion_audit.json",
    "outputs/pre_submission_audit.json",
]


@dataclass
class CommandResult:
    command: str
    returncode: int
    passed: bool
    output_tail: list[str]


def run_command(extracted_root: Path, script: str) -> CommandResult:
    result = subprocess.run(
        [sys.executable, script],
        cwd=extracted_root,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    output = result.stdout.replace(str(extracted_root), "<extracted-package>")
    return CommandResult(
        command=f"python {script}",
        returncode=result.returncode,
        passed=result.returncode == 0,
        output_tail=output.strip().splitlines()[-12:],
    )


def main() -> None:
    OUT.mkdir(exist_ok=True)
    json_path = OUT / "zip_reproduction_audit.json"
    md_path = OUT / "zip_reproduction_audit.md"

    with tempfile.TemporaryDirectory(prefix="election-zip-audit-") as tmp:
        extract_root = Path(tmp) / "package"
        extract_root.mkdir()
        with ZipFile(ZIP_PATH) as zf:
            zf.extractall(extract_root)

        missing = [rel for rel in REQUIRED_EXTRACTED_FILES if not (extract_root / rel).exists()]
        command_results = [run_command(extract_root, script) for script in [cmd[0] for cmd in COMMANDS]]

    report = {
        "status": "pass" if not missing and all(result.passed for result in command_results) else "fail",
        "scope": "fresh extraction of the submission ZIP into an isolated temporary directory",
        "package": ZIP_PATH.name,
        "required_extracted_files": {
            "checked": len(REQUIRED_EXTRACTED_FILES),
            "missing": missing,
        },
        "commands": [asdict(result) for result in command_results],
    }
    json_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    md_lines = [
        "# ZIP Reproduction Audit",
        "",
        f"- Status: `{report['status']}`",
        f"- Scope: {report['scope']}",
        f"- Package: `{report['package']}`",
        f"- Required extracted files checked: `{report['required_extracted_files']['checked']}`",
        f"- Missing required extracted files: `{len(missing)}`",
        "",
        "## Commands",
        "",
    ]
    for result in command_results:
        md_lines.append(f"- `{result.command}` -> return code `{result.returncode}`")
    md_lines.append("")
    md_path.write_text("\n".join(md_lines), encoding="utf-8")

    if report["status"] != "pass":
        raise SystemExit("ZIP reproduction audit failed")
    print(f"ZIP reproduction audit passed. Wrote {json_path.relative_to(ROOT)} and {md_path.relative_to(ROOT)}.")


if __name__ == "__main__":
    main()
