#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs"

INDEX_FILES = [
    "SUBMISSION_INDEX_ko.md",
    "SUBMISSION_INDEX_en.md",
]

REQUIRED_REFERENCES = [
    "dist/election_duplicate_ieie_submission.zip",
    "dist/election_duplicate_ieie_submission.zip.sha256",
    "dist/election_duplicate_ieie_submission_manifest.json",
    "latex/ieie/main.pdf",
    "latex/en/main_en.pdf",
    "latex/ieie/main.tex",
    "latex/en/main_en.tex",
    "paper_statistical_implausibility_ko.md",
    "paper_statistical_implausibility_en.md",
    "evidence_matrix_ko.md",
    "evidence_matrix_en.md",
    "DATA_DICTIONARY_ko.md",
    "DATA_DICTIONARY_en.md",
    "REVIEWER_QUICKSTART_ko.md",
    "REVIEWER_QUICKSTART_en.md",
    "REPRODUCIBILITY_CHECKLIST_ko.md",
    "REPRODUCIBILITY_CHECKLIST_en.md",
    "STATISTICAL_CALCULATION_NOTE_ko.md",
    "STATISTICAL_CALCULATION_NOTE_en.md",
    "data_availability_2026_ko.md",
    "data_availability_2026_en.md",
    "AUDIT_PROTOCOL_ko.md",
    "AUDIT_PROTOCOL_en.md",
    "ALTERNATIVE_EXPLANATIONS_MATRIX_ko.md",
    "ALTERNATIVE_EXPLANATIONS_MATRIX_en.md",
    "LOOK_ELSEWHERE_ROBUSTNESS_ko.md",
    "LOOK_ELSEWHERE_ROBUSTNESS_en.md",
    "FINAL_SUBMISSION_CHECKLIST_ko.md",
    "FINAL_SUBMISSION_CHECKLIST_en.md",
    "outputs/core_claims_verification.json",
    "outputs/statistical_robustness_audit.json",
    "outputs/video_source_exclusion_audit.json",
    "outputs/source_provenance_audit.json",
    "outputs/claim_boundary_audit.json",
    "outputs/objection_coverage_audit.json",
    "outputs/pre_submission_audit.json",
    "outputs/submission_integrity_report.json",
    "outputs/submission_index_audit.json",
    "outputs/zip_reproduction_audit.json",
    "outputs/local_ci_validation_report.json",
    "requirements.txt",
    "scripts/run_all.py",
    "scripts/validate_package.py",
]

EXPECTED_OUTPUTS = {
    "outputs/core_claims_verification.json": ("check_count", 45),
    "outputs/statistical_robustness_audit.json": ("check_count", 10),
    "outputs/video_source_exclusion_audit.json": ("check_count", 23),
    "outputs/source_provenance_audit.json": ("url_count", 24),
    "outputs/claim_boundary_audit.json": ("check_count", 18),
    "outputs/objection_coverage_audit.json": ("check_count", 22),
    "outputs/pre_submission_audit.json": ("check_count", 15),
}


def read_json(rel: str) -> dict:
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def main() -> None:
    OUT.mkdir(exist_ok=True)
    rows: list[dict[str, str]] = []

    for rel in INDEX_FILES:
        path = ROOT / rel
        status = "pass" if path.exists() else "fail"
        rows.append({
            "check": f"{rel} exists",
            "status": status,
            "detail": rel,
        })
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for ref in REQUIRED_REFERENCES:
            rows.append({
                "check": f"{rel} references {ref}",
                "status": "pass" if ref in text else "fail",
                "detail": ref,
            })

    for rel, (field, expected) in EXPECTED_OUTPUTS.items():
        data = read_json(rel)
        rows.append({
            "check": f"{rel} status pass",
            "status": "pass" if data.get("status") == "pass" else "fail",
            "detail": str(data.get("status")),
        })
        rows.append({
            "check": f"{rel} {field} {expected}",
            "status": "pass" if data.get(field) == expected else "fail",
            "detail": str(data.get(field)),
        })

    status = "pass" if all(row["status"] == "pass" for row in rows) else "fail"
    summary = {
        "status": status,
        "scope": "submission index references and pre-zip audit-count consistency",
        "check_count": len(rows),
        "failed_checks": [row for row in rows if row["status"] != "pass"],
    }

    json_path = OUT / "submission_index_audit.json"
    csv_path = OUT / "submission_index_audit.csv"
    json_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["check", "status", "detail"], lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    if status != "pass":
        failed = "; ".join(row["check"] for row in summary["failed_checks"][:10])
        raise SystemExit(f"Submission index audit failed: {failed}")

    print(f"Submission index audit passed with {len(rows)} checks.")


if __name__ == "__main__":
    main()
