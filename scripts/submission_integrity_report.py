#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def pdf_text(path: Path) -> tuple[int, str]:
    import fitz  # type: ignore[import-not-found]

    pdf = fitz.open(path)
    return pdf.page_count, "\n".join(page.get_text() for page in pdf)


def main() -> None:
    OUT.mkdir(exist_ok=True)

    core = json.loads((OUT / "core_claims_verification.json").read_text(encoding="utf-8"))
    audit = json.loads((OUT / "pre_submission_audit.json").read_text(encoding="utf-8"))
    ko_pdf = ROOT / "latex" / "ieie" / "main.pdf"
    en_pdf = ROOT / "latex" / "en" / "main_en.pdf"
    en_pages, en_text = pdf_text(en_pdf)
    ko_pages, _ = pdf_text(ko_pdf)

    summary = {
        "status": "pass" if core.get("status") == "pass" and audit.get("status") == "pass" else "fail",
        "scope": "submission package integrity summary excluding final zip self-hash",
        "core_claims_status": core.get("status"),
        "core_claims_check_count": core.get("check_count"),
        "pre_submission_audit_status": audit.get("status"),
        "pre_submission_audit_check_count": audit.get("check_count"),
        "korean_pdf": {
            "path": "latex/ieie/main.pdf",
            "pages": ko_pages,
            "sha256": sha256(ko_pdf),
        },
        "english_pdf": {
            "path": "latex/en/main_en.pdf",
            "pages": en_pages,
            "sha256": sha256(en_pdf),
            "korean_character_count": len(re.findall(r"[가-힣]", en_text)),
            "references_english_evidence_matrix": "evidence_matrix_en.md" in en_text,
            "references_korean_evidence_matrix": "evidence_matrix_ko.md" in en_text,
        },
        "key_claims": {
            "historical_rows": 81701,
            "historical_governor_contests": 51,
            "gwangju_jeonnam_units_n": 393,
            "effective_pair_space_k": 100944.8,
            "poisson_p_at_least_5": 0.0011484064248148407,
            "exact_collision_p_at_least_5": 0.0012190883791786122,
            "bootstrap_trials": 200000,
            "bootstrap_at_least_5_exceedances": 0,
            "nec_2026_event_rows": 12,
            "nec_2026_duplicate_pairs": 6,
        },
    }

    if summary["english_pdf"]["korean_character_count"] != 0:
        summary["status"] = "fail"
    if not summary["english_pdf"]["references_english_evidence_matrix"]:
        summary["status"] = "fail"
    if summary["english_pdf"]["references_korean_evidence_matrix"]:
        summary["status"] = "fail"

    json_path = OUT / "submission_integrity_report.json"
    md_path = OUT / "submission_integrity_report.md"
    json_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    md_lines = [
        "# Submission Integrity Report",
        "",
        f"- Status: `{summary['status']}`",
        f"- Scope: {summary['scope']}",
        f"- Core-claims verification: `{summary['core_claims_status']}`, {summary['core_claims_check_count']} checks",
        f"- Pre-submission audit: `{summary['pre_submission_audit_status']}`, {summary['pre_submission_audit_check_count']} checks",
        "",
        "## PDF Artifacts",
        "",
        f"- Korean PDF: `{summary['korean_pdf']['path']}`, {summary['korean_pdf']['pages']} pages, sha256 `{summary['korean_pdf']['sha256']}`",
        f"- English PDF: `{summary['english_pdf']['path']}`, {summary['english_pdf']['pages']} pages, sha256 `{summary['english_pdf']['sha256']}`",
        f"- English PDF Korean-character count: `{summary['english_pdf']['korean_character_count']}`",
        f"- English PDF references `evidence_matrix_en.md`: `{summary['english_pdf']['references_english_evidence_matrix']}`",
        f"- English PDF references `evidence_matrix_ko.md`: `{summary['english_pdf']['references_korean_evidence_matrix']}`",
        "",
        "## Key Reproducible Numbers",
        "",
    ]
    for key, value in summary["key_claims"].items():
        md_lines.append(f"- `{key}`: `{value}`")
    md_lines.extend([
        "",
        "## Notes",
        "",
        "This report intentionally excludes the final submission ZIP hash because the report itself is included in the ZIP. The ZIP hash is recorded in `dist/election_duplicate_ieie_submission.zip.sha256` and `dist/election_duplicate_ieie_submission_manifest.json`.",
        "",
    ])
    md_path.write_text("\n".join(md_lines), encoding="utf-8")
    print(f"Wrote {json_path.relative_to(ROOT)} and {md_path.relative_to(ROOT)}.")


if __name__ == "__main__":
    main()
