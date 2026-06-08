#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
PACKAGE_NAME = "election_duplicate_ieie_submission.zip"
MANIFEST_NAME = "election_duplicate_ieie_submission_manifest.json"
ZIP_TIMESTAMP = (2026, 6, 9, 0, 0, 0)

INCLUDE_FILES = [
    "README.md",
    "requirements.txt",
    "paper_statistical_implausibility_ko.md",
    "paper_statistical_implausibility_en.md",
    "cover_letter_ko.md",
    "cover_letter_en.md",
    "submission_memo_ko.md",
    "submission_memo_en.md",
    "reviewer_response_ko.md",
    "reviewer_response_en.md",
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
    "latex/convert_to_ieie.py",
    "latex/ieie/IEIE.cls",
    "latex/ieie/main.tex",
    "latex/ieie/main.pdf",
    "latex/en/main_en.tex",
    "latex/en/main_en.pdf",
    "scripts/analyze_duplicates.py",
    "scripts/count_nec_2026_gwangju_jeonnam_units.py",
    "scripts/analyze_governor_actual_top2.py",
    "scripts/bootstrap_governor_duplicates.py",
    "scripts/fetch_nec_2026_duplicate_cases.py",
    "scripts/analyze_songdo_probability.py",
    "scripts/probability_sensitivity.py",
    "scripts/analyze_early_day_assembly.py",
    "scripts/verify_core_claims.py",
    "scripts/statistical_robustness_audit.py",
    "scripts/source_provenance_audit.py",
    "scripts/claim_boundary_audit.py",
    "scripts/objection_coverage_audit.py",
    "scripts/pre_submission_audit.py",
    "scripts/submission_integrity_report.py",
    "scripts/local_ci_validation_report.py",
    "scripts/generate_checksums.py",
    "scripts/run_all.py",
    "scripts/validate_package.py",
    "scripts/create_submission_zip.py",
]

INCLUDE_DIRS = [
    "data",
    "outputs",
]

EXCLUDE_SUFFIXES = {
    ".aux",
    ".log",
    ".out",
    ".synctex.gz",
}

EXCLUDE_NAMES = {
    ".DS_Store",
    "__pycache__",
}

EXCLUDE_RELATIVE = {
    "outputs/local_ci_validation_report.md",
    "outputs/local_ci_validation_report.json",
}


def should_include(path: Path) -> bool:
    rel = path.relative_to(ROOT).as_posix()
    if rel in EXCLUDE_RELATIVE:
        return False
    if any(part in EXCLUDE_NAMES for part in path.parts):
        return False
    if path.suffix in EXCLUDE_SUFFIXES:
        return False
    return path.is_file()


def package_paths() -> list[Path]:
    paths = [ROOT / rel for rel in INCLUDE_FILES]
    for dirname in INCLUDE_DIRS:
        base = ROOT / dirname
        paths.extend(path for path in base.rglob("*") if should_include(path))
    unique = sorted(set(paths), key=lambda path: str(path.relative_to(ROOT)))
    missing = [str(path.relative_to(ROOT)) for path in unique if not path.exists()]
    if missing:
        raise SystemExit(f"Missing files for zip: {', '.join(missing)}")
    return unique


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    DIST.mkdir(exist_ok=True)
    zip_path = DIST / PACKAGE_NAME
    manifest_path = DIST / MANIFEST_NAME
    sha_path = DIST / f"{PACKAGE_NAME}.sha256"
    if zip_path.exists():
        zip_path.unlink()
    if manifest_path.exists():
        manifest_path.unlink()
    if sha_path.exists():
        sha_path.unlink()

    paths = package_paths()
    with ZipFile(zip_path, "w", compression=ZIP_DEFLATED) as zf:
        for path in paths:
            rel = path.relative_to(ROOT).as_posix()
            info = ZipInfo(rel, date_time=ZIP_TIMESTAMP)
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            zf.writestr(info, path.read_bytes())

    with ZipFile(zip_path) as zf:
        names = set(zf.namelist())
    expected = {str(path.relative_to(ROOT)) for path in paths}
    missing = sorted(expected - names)
    if missing:
        raise SystemExit(f"Zip missing expected entries: {', '.join(missing)}")

    digest = sha256(zip_path)
    manifest = {
        "package": PACKAGE_NAME,
        "bytes": zip_path.stat().st_size,
        "sha256": digest,
        "file_count": len(names),
        "zip_entry_timestamp": "-".join(str(part) for part in ZIP_TIMESTAMP),
        "scope": "submission zip sidecar manifest; not embedded in the zip",
    }
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    sha_path.write_text(f"{digest}  {PACKAGE_NAME}\n", encoding="utf-8")

    print(f"Created {zip_path.relative_to(ROOT)} with {len(names)} files.")


if __name__ == "__main__":
    main()
