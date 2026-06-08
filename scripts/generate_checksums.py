#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs"
OUT.mkdir(parents=True, exist_ok=True)

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
    "latex/convert_to_ieie.py",
    "latex/ieie/IEIE.cls",
    "latex/ieie/main.tex",
    "latex/ieie/main.pdf",
    "latex/en/main_en.tex",
    "latex/en/main_en.pdf",
]

INCLUDE_DIRS = [
    "data",
    "scripts",
    "outputs",
]

EXCLUDE_NAMES = {
    ".DS_Store",
    "__pycache__",
}

EXCLUDE_RELATIVE = {
    "outputs/checksums_sha256.csv",
}


def should_include(path: Path) -> bool:
    if not path.is_file():
        return False
    rel = path.relative_to(ROOT).as_posix()
    if rel in EXCLUDE_RELATIVE:
        return False
    if any(part in EXCLUDE_NAMES for part in path.parts):
        return False
    return True


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def collect_paths() -> list[Path]:
    paths = [ROOT / rel for rel in INCLUDE_FILES]
    for dirname in INCLUDE_DIRS:
        base = ROOT / dirname
        paths.extend(path for path in base.rglob("*") if should_include(path))
    existing = [path for path in paths if path.exists() and should_include(path)]
    return sorted(set(existing), key=lambda path: path.relative_to(ROOT).as_posix())


def main() -> None:
    rows = []
    for path in collect_paths():
        rel = path.relative_to(ROOT).as_posix()
        rows.append({
            "path": rel,
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
        })

    out_path = OUT / "checksums_sha256.csv"
    with out_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["path", "bytes", "sha256"])
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {out_path.relative_to(ROOT)} with {len(rows)} rows.")


if __name__ == "__main__":
    main()
