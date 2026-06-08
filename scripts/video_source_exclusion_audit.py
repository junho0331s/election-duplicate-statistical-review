#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs"

SOURCE_FILES = [
    "paper_statistical_implausibility_ko.md",
    "paper_statistical_implausibility_en.md",
    "latex/ieie/main.tex",
    "latex/en/main_en.tex",
    "README.md",
    "cover_letter_ko.md",
    "cover_letter_en.md",
    "submission_memo_ko.md",
    "submission_memo_en.md",
    "reviewer_response_ko.md",
    "reviewer_response_en.md",
    "evidence_matrix_ko.md",
    "evidence_matrix_en.md",
    "data_availability_2026_ko.md",
    "data_availability_2026_en.md",
    "AUDIT_PROTOCOL_ko.md",
    "AUDIT_PROTOCOL_en.md",
    "ALTERNATIVE_EXPLANATIONS_MATRIX_ko.md",
    "ALTERNATIVE_EXPLANATIONS_MATRIX_en.md",
    "LOOK_ELSEWHERE_ROBUSTNESS_ko.md",
    "LOOK_ELSEWHERE_ROBUSTNESS_en.md",
    "STATISTICAL_CALCULATION_NOTE_ko.md",
    "STATISTICAL_CALCULATION_NOTE_en.md",
]

VIDEO_DOMAIN_SUFFIXES = [
    "you" + "tube.com",
    "youtu" + ".be",
]

INFORMAL_VIDEO_MARKERS = [
    "유" + "튜브",
    "You" + "Tube",
    "you" + "tube",
    "자" + "막",
]


@dataclass
class AuditRow:
    file: str
    video_url_count: int
    informal_marker_count: int
    status: str


def extract_urls(text: str) -> list[str]:
    return [url.rstrip(").,]") for url in re.findall(r"https?://[^\s)>\]]+", text)]


def is_video_url(url: str) -> bool:
    domain = urlparse(url).netloc.lower()
    if domain.startswith("www."):
        domain = domain[4:]
    return any(domain == suffix or domain.endswith("." + suffix) for suffix in VIDEO_DOMAIN_SUFFIXES)


def marker_count(text: str) -> int:
    return sum(text.count(marker) for marker in INFORMAL_VIDEO_MARKERS)


def main() -> None:
    OUT.mkdir(exist_ok=True)
    rows: list[AuditRow] = []
    failures: list[str] = []

    for rel in SOURCE_FILES:
        path = ROOT / rel
        text = path.read_text(encoding="utf-8", errors="ignore")
        video_urls = [url for url in extract_urls(text) if is_video_url(url)]
        informal_count = marker_count(text)
        status = "pass" if not video_urls and informal_count == 0 else "fail"
        rows.append(
            AuditRow(
                file=rel,
                video_url_count=len(video_urls),
                informal_marker_count=informal_count,
                status=status,
            )
        )
        if video_urls:
            failures.append(f"{rel}: {len(video_urls)} video URLs")
        if informal_count:
            failures.append(f"{rel}: {informal_count} informal video markers")

    csv_path = OUT / "video_source_exclusion_audit.csv"
    json_path = OUT / "video_source_exclusion_audit.json"

    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["file", "video_url_count", "informal_marker_count", "status"],
            lineterminator="\n",
        )
        writer.writeheader()
        for row in rows:
            writer.writerow(asdict(row))

    summary = {
        "status": "pass" if not failures and all(row.status == "pass" for row in rows) else "fail",
        "scope": "manuscript-facing files and reviewer-facing submission documents",
        "checked_files": SOURCE_FILES,
        "check_count": len(rows),
        "video_domain_marker_policy": "configured informal video platform domain markers are excluded from manuscript-facing sources",
        "failures": failures,
    }
    json_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    if summary["status"] != "pass":
        raise SystemExit("Video source exclusion audit failed: " + "; ".join(failures))
    print(f"Video source exclusion audit passed for {len(rows)} files.")


if __name__ == "__main__":
    main()
