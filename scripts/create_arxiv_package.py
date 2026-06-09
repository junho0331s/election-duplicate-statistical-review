#!/usr/bin/env python3
"""Create a clean arXiv-ready English source package.

The main repository keeps the English manuscript under latex/en and refers to
the IEIE class through a parent-relative path. arXiv source uploads should be
self-contained, so this script copies the manuscript and class into dist/arxiv
and rewrites the documentclass line to use the local class file.
"""

from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_TEX = ROOT / "latex" / "en" / "main_en.tex"
SOURCE_PDF = ROOT / "latex" / "en" / "main_en.pdf"
SOURCE_CLASS = ROOT / "latex" / "ieie" / "IEIE.cls"
ARXIV_DIR = ROOT / "dist" / "arxiv"
SOURCE_DIR = ARXIV_DIR / "source"
PACKAGE_ZIP = ARXIV_DIR / "election_duplicate_arxiv_source.zip"
PDF_COPY = ARXIV_DIR / "election_duplicate_arxiv_pdf.pdf"
MANIFEST = ARXIV_DIR / "manifest.json"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def run(command: list[str], cwd: Path) -> None:
    subprocess.run(command, cwd=cwd, check=True)


def main() -> None:
    ARXIV_DIR.mkdir(parents=True, exist_ok=True)
    if SOURCE_DIR.exists():
        shutil.rmtree(SOURCE_DIR)
    SOURCE_DIR.mkdir(parents=True)

    tex = SOURCE_TEX.read_text(encoding="utf-8")
    tex = tex.replace(
        r"\documentclass[preprint]{../ieie/IEIE}",
        r"\documentclass[preprint]{IEIE}",
        1,
    )
    (SOURCE_DIR / "main.tex").write_text(tex, encoding="utf-8")
    shutil.copy2(SOURCE_CLASS, SOURCE_DIR / "IEIE.cls")
    shutil.copy2(SOURCE_PDF, PDF_COPY)

    for _ in range(2):
        run(
            [
                "xelatex",
                "-interaction=nonstopmode",
                "-halt-on-error",
                "main.tex",
            ],
            SOURCE_DIR,
        )

    if PACKAGE_ZIP.exists():
        PACKAGE_ZIP.unlink()
    run(["zip", "-q", "-r", str(PACKAGE_ZIP), "main.tex", "IEIE.cls"], SOURCE_DIR)

    generated_pdf = SOURCE_DIR / "main.pdf"
    manifest = {
        "package": str(PACKAGE_ZIP.relative_to(ROOT)),
        "pdf_copy": str(PDF_COPY.relative_to(ROOT)),
        "generated_pdf": str(generated_pdf.relative_to(ROOT)),
        "source_files": ["main.tex", "IEIE.cls"],
        "checksums": {
            str(PACKAGE_ZIP.relative_to(ROOT)): sha256(PACKAGE_ZIP),
            str(PDF_COPY.relative_to(ROOT)): sha256(PDF_COPY),
            str(generated_pdf.relative_to(ROOT)): sha256(generated_pdf),
        },
        "notes": [
            "Prepared for arXiv-style source upload.",
            "Final arXiv submission requires the author's arXiv account, category selection, metadata confirmation, and explicit final-submit approval.",
        ],
    }
    MANIFEST.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
