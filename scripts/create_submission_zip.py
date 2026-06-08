#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
PACKAGE_NAME = "election_duplicate_ieie_submission.zip"

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
    "REPRODUCIBILITY_CHECKLIST_ko.md",
    "REPRODUCIBILITY_CHECKLIST_en.md",
    "STATISTICAL_CALCULATION_NOTE_ko.md",
    "STATISTICAL_CALCULATION_NOTE_en.md",
    "data_availability_2026_ko.md",
    "data_availability_2026_en.md",
    "AUDIT_PROTOCOL_ko.md",
    "AUDIT_PROTOCOL_en.md",
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


def should_include(path: Path) -> bool:
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


def main() -> None:
    DIST.mkdir(exist_ok=True)
    zip_path = DIST / PACKAGE_NAME
    if zip_path.exists():
        zip_path.unlink()

    paths = package_paths()
    with ZipFile(zip_path, "w", compression=ZIP_DEFLATED) as zf:
        for path in paths:
            zf.write(path, path.relative_to(ROOT))

    with ZipFile(zip_path) as zf:
        names = set(zf.namelist())
    expected = {str(path.relative_to(ROOT)) for path in paths}
    missing = sorted(expected - names)
    if missing:
        raise SystemExit(f"Zip missing expected entries: {', '.join(missing)}")

    print(f"Created {zip_path.relative_to(ROOT)} with {len(names)} files.")


if __name__ == "__main__":
    main()
