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
    "README.md",
    "PUBLIC_DISCUSSION_CLAIMS_ko.md",
    "PUBLIC_DISCUSSION_CLAIMS_en.md",
    "data_availability_2026_ko.md",
    "data_availability_2026_en.md",
    "evidence_matrix_ko.md",
    "evidence_matrix_en.md",
]

ALLOWED_DOMAIN_SUFFIXES = {
    "data.go.kr",
    "nec.go.kr",
    "news.tvchosun.com",
    "v.daum.net",
    "hani.co.kr",
    "jeonnam.go.kr",
}

VIDEO_DOMAIN_MARKERS = [
    "you" + "tube.com",
    "youtu" + ".be",
]


@dataclass
class SourceRow:
    file: str
    url: str
    domain: str
    source_class: str
    status: str


def classify(domain: str) -> str:
    if domain.endswith("data.go.kr") or domain.endswith("nec.go.kr"):
        return "official election/public-data source"
    if domain.endswith("jeonnam.go.kr"):
        return "official administrative geography source"
    if domain.endswith(("news.tvchosun.com", "v.daum.net", "hani.co.kr")):
        return "public report used for event definition or explanation"
    return "unclassified"


def allowed(domain: str) -> bool:
    return any(domain == suffix or domain.endswith("." + suffix) for suffix in ALLOWED_DOMAIN_SUFFIXES)


def extract_urls(text: str) -> list[str]:
    return [url.rstrip(").,]") for url in re.findall(r"https?://[^\s)>\]]+", text)]


def main() -> None:
    OUT.mkdir(exist_ok=True)
    rows: list[SourceRow] = []
    failures: list[str] = []

    for rel in SOURCE_FILES:
        path = ROOT / rel
        text = path.read_text(encoding="utf-8", errors="ignore")
        lowered = text.lower()
        for marker in VIDEO_DOMAIN_MARKERS:
            if marker in lowered:
                failures.append(f"{rel}: informal video platform marker")

        for url in extract_urls(text):
            domain = urlparse(url).netloc.lower()
            if domain.startswith("www."):
                domain = domain[4:]
            status = "pass" if allowed(domain) else "fail"
            if status == "fail":
                failures.append(f"{rel}: unapproved domain {domain}")
            rows.append(SourceRow(rel, url, domain, classify(domain), status))

    if not rows:
        failures.append("no source URLs found")

    csv_path = OUT / "source_provenance_audit.csv"
    json_path = OUT / "source_provenance_audit.json"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["file", "url", "domain", "source_class", "status"], lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow(asdict(row))

    summary = {
        "status": "pass" if not failures and all(row.status == "pass" for row in rows) else "fail",
        "scope": "source provenance audit for manuscript-facing references and source-policy documents",
        "checked_files": SOURCE_FILES,
        "url_count": len(rows),
        "allowed_domain_suffixes": sorted(ALLOWED_DOMAIN_SUFFIXES),
        "source_classes": sorted({row.source_class for row in rows}),
        "failures": failures,
    }
    json_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    if summary["status"] != "pass":
        raise SystemExit("Source provenance audit failed: " + "; ".join(failures))
    print(f"Source provenance audit passed with {len(rows)} URLs.")


if __name__ == "__main__":
    main()
