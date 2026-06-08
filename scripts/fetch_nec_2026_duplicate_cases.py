#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import html
import json
import re
import urllib.parse
import urllib.request
from html.parser import HTMLParser
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "nec_2026_official_html"
OUT = ROOT / "outputs"
RAW_DIR.mkdir(parents=True, exist_ok=True)
OUT.mkdir(parents=True, exist_ok=True)

BASE_URL = "https://info.nec.go.kr/electioninfo/electionInfo_report.xhtml"
REFERER = "https://info.nec.go.kr/main/showDocument.xhtml?electionId=0020260603&topMenuId=VC&secondMenuId=VCCP08"

TOWNS = [
    {"city_code": "2800", "city": "인천광역시", "town_code": "2804", "town": "연수구"},
    {"city_code": "2900", "city": "광주광역시", "town_code": "2905", "town": "광산구"},
    {"city_code": "4600", "city": "전라남도", "town_code": "4602", "town": "여수시"},
    {"city_code": "4600", "city": "전라남도", "town_code": "4609", "town": "장성군"},
    {"city_code": "4600", "city": "전라남도", "town_code": "4612", "town": "고흥군"},
    {"city_code": "4600", "city": "전라남도", "town_code": "4613", "town": "보성군"},
    {"city_code": "4600", "city": "전라남도", "town_code": "4614", "town": "화순군"},
    {"city_code": "4600", "city": "전라남도", "town_code": "4616", "town": "강진군"},
    {"city_code": "4600", "city": "전라남도", "town_code": "4623", "town": "함평군"},
    {"city_code": "4600", "city": "전라남도", "town_code": "4624", "town": "신안군"},
]

TARGETS = [
    {"pair_id": "incheon_songdo", "city": "인천광역시", "town": "연수구", "unit": "송도1동", "candidate_1": "박찬대", "candidate_2": "유정복", "expected_1": 3030, "expected_2": 1440},
    {"pair_id": "incheon_songdo", "city": "인천광역시", "town": "연수구", "unit": "송도2동", "candidate_1": "박찬대", "candidate_2": "유정복", "expected_1": 3030, "expected_2": 1440},
    {"pair_id": "gwangju_goheung", "city": "광주광역시", "town": "광산구", "unit": "송정1동", "candidate_1": "민형배", "candidate_2": "이정현", "expected_1": 1401, "expected_2": 120},
    {"pair_id": "gwangju_goheung", "city": "전라남도", "town": "고흥군", "unit": "금산면", "candidate_1": "민형배", "candidate_2": "이정현", "expected_1": 1401, "expected_2": 120},
    {"pair_id": "sinan_yeosu", "city": "전라남도", "town": "신안군", "unit": "하의면", "candidate_1": "민형배", "candidate_2": "이정현", "expected_1": 506, "expected_2": 42},
    {"pair_id": "sinan_yeosu", "city": "전라남도", "town": "여수시", "unit": "삼일동", "candidate_1": "민형배", "candidate_2": "이정현", "expected_1": 506, "expected_2": 42},
    {"pair_id": "hampyeong_jangseong", "city": "전라남도", "town": "함평군", "unit": "엄다면", "candidate_1": "민형배", "candidate_2": "이정현", "expected_1": 606, "expected_2": 57},
    {"pair_id": "hampyeong_jangseong", "city": "전라남도", "town": "장성군", "unit": "북하면", "candidate_1": "민형배", "candidate_2": "이정현", "expected_1": 606, "expected_2": 57},
    {"pair_id": "boseong_sinan", "city": "전라남도", "town": "보성군", "unit": "노동면", "candidate_1": "민형배", "candidate_2": "이정현", "expected_1": 356, "expected_2": 42},
    {"pair_id": "boseong_sinan", "city": "전라남도", "town": "신안군", "unit": "팔금면", "candidate_1": "민형배", "candidate_2": "이정현", "expected_1": 356, "expected_2": 42},
    {"pair_id": "hwasun_gangjin", "city": "전라남도", "town": "화순군", "unit": "이양면", "candidate_1": "민형배", "candidate_2": "이정현", "expected_1": 444, "expected_2": 46},
    {"pair_id": "hwasun_gangjin", "city": "전라남도", "town": "강진군", "unit": "병영면", "candidate_1": "민형배", "candidate_2": "이정현", "expected_1": 444, "expected_2": 46},
]


class TableParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.in_table = False
        self.table_depth = 0
        self.in_row = False
        self.in_cell = False
        self.current_cell: list[str] = []
        self.current_row: list[str] = []
        self.rows: list[list[str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = dict(attrs)
        if tag == "table" and attrs_dict.get("id") == "table01":
            self.in_table = True
            self.table_depth = 1
            return
        if self.in_table and tag == "table":
            self.table_depth += 1
        if not self.in_table:
            return
        if tag == "tr":
            self.in_row = True
            self.current_row = []
        elif tag in {"td", "th"} and self.in_row:
            self.in_cell = True
            self.current_cell = []
        elif tag == "br" and self.in_cell:
            self.current_cell.append(" ")

    def handle_endtag(self, tag: str) -> None:
        if not self.in_table:
            return
        if tag in {"td", "th"} and self.in_cell:
            text = normalize_text("".join(self.current_cell))
            self.current_row.append(text)
            self.in_cell = False
        elif tag == "tr" and self.in_row:
            if self.current_row:
                self.rows.append(self.current_row)
            self.in_row = False
        elif tag == "table":
            self.table_depth -= 1
            if self.table_depth <= 0:
                self.in_table = False

    def handle_data(self, data: str) -> None:
        if self.in_cell:
            self.current_cell.append(data)


def normalize_text(value: str) -> str:
    value = html.unescape(value)
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def to_int(value: str) -> int:
    value = value.replace(",", "").strip()
    return int(value) if value else 0


def raw_path(town: dict[str, str]) -> Path:
    return RAW_DIR / f"{town['city_code']}_{town['town_code']}_{town['town']}.html"


def fetch_town(town: dict[str, str]) -> str:
    payload = {
        "electionId": "0020260603",
        "requestURI": "/electioninfo/0020260603/vc/vccp08.jsp",
        "topMenuId": "VC",
        "secondMenuId": "VCCP08",
        "menuId": "VCCP08",
        "statementId": "VCCP08_#00",
        "electionCode": "3",
        "cityCode": town["city_code"],
        "townCode": town["town_code"],
        "sggCityCode": "-1",
        "townCodeFromSgg": "-1",
        "sggTownCode": "-1",
        "checkCityCode": "-1",
    }
    data = urllib.parse.urlencode(payload).encode("utf-8")
    request = urllib.request.Request(
        BASE_URL,
        data=data,
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "Referer": REFERER,
            "User-Agent": "Mozilla/5.0",
        },
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8", errors="replace")


def parse_table(text: str, town: dict[str, str]) -> list[dict[str, Any]]:
    parser = TableParser()
    parser.feed(text)
    if len(parser.rows) < 3:
        raise ValueError(f"No table rows parsed for {town['town']}")

    candidate_headers = parser.rows[1]
    candidate_names = [header.split()[-1] for header in candidate_headers]
    rows: list[dict[str, Any]] = []
    candidate_count = len(candidate_names)
    for row in parser.rows[2:]:
        if len(row) < 4 + candidate_count + 2:
            continue
        candidate_votes = {
            candidate_names[idx]: to_int(row[4 + idx])
            for idx in range(candidate_count)
        }
        rows.append({
            "city": town["city"],
            "town": town["town"],
            "unit": row[0],
            "vote_class": row[1],
            "electors": to_int(row[2]),
            "turnout": to_int(row[3]),
            "candidate_votes": candidate_votes,
            "invalid_votes": to_int(row[4 + candidate_count]),
            "abstentions": to_int(row[5 + candidate_count]),
            "source_file": str(raw_path(town).relative_to(ROOT)),
            "source_url": REFERER,
        })
    return rows


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def collect(fetch: bool) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    all_rows: list[dict[str, Any]] = []
    manifest: list[dict[str, Any]] = []
    for town in TOWNS:
        path = raw_path(town)
        if fetch or not path.exists():
            text = fetch_town(town)
            path.write_text(text, encoding="utf-8")
        else:
            text = path.read_text(encoding="utf-8")
        parsed = parse_table(text, town)
        all_rows.extend(parsed)
        manifest.append({
            "city": town["city"],
            "town": town["town"],
            "town_code": town["town_code"],
            "source_file": str(path.relative_to(ROOT)),
            "rows": len(parsed),
        })
    return all_rows, manifest


def main() -> None:
    argp = argparse.ArgumentParser()
    argp.add_argument("--fetch", action="store_true", help="refresh official NEC HTML cache")
    args = argp.parse_args()

    all_rows, manifest = collect(fetch=args.fetch)
    by_key = {
        (row["city"], row["town"], row["unit"], row["vote_class"]): row
        for row in all_rows
    }

    case_rows: list[dict[str, Any]] = []
    for target in TARGETS:
        key = (target["city"], target["town"], target["unit"], "관내사전투표")
        row = by_key.get(key)
        if not row:
            raise AssertionError(f"Missing target row: {key}")
        votes = row["candidate_votes"]
        actual_1 = votes.get(target["candidate_1"])
        actual_2 = votes.get(target["candidate_2"])
        if actual_1 != target["expected_1"] or actual_2 != target["expected_2"]:
            raise AssertionError(
                f"{key}: expected {target['expected_1']},{target['expected_2']} "
                f"got {actual_1},{actual_2}"
            )
        case_rows.append({
            "pair_id": target["pair_id"],
            "city": target["city"],
            "town": target["town"],
            "unit": target["unit"],
            "vote_class": "관내사전투표",
            "candidate_1": target["candidate_1"],
            "candidate_1_votes": actual_1,
            "candidate_2": target["candidate_2"],
            "candidate_2_votes": actual_2,
            "electors": row["electors"],
            "turnout": row["turnout"],
            "invalid_votes": row["invalid_votes"],
            "abstentions": row["abstentions"],
            "source_file": row["source_file"],
            "source_url": row["source_url"],
        })

    pair_rows: list[dict[str, Any]] = []
    by_pair: dict[str, list[dict[str, Any]]] = {}
    for row in case_rows:
        by_pair.setdefault(row["pair_id"], []).append(row)
    for pair_id, rows in sorted(by_pair.items()):
        if len(rows) != 2:
            raise AssertionError(f"{pair_id}: expected two rows, got {len(rows)}")
        signatures = {
            (
                row["candidate_1"],
                row["candidate_1_votes"],
                row["candidate_2"],
                row["candidate_2_votes"],
            )
            for row in rows
        }
        if len(signatures) != 1:
            raise AssertionError(f"{pair_id}: signature mismatch")
        signature = next(iter(signatures))
        pair_rows.append({
            "pair_id": pair_id,
            "candidate_1": signature[0],
            "candidate_1_votes": signature[1],
            "candidate_2": signature[2],
            "candidate_2_votes": signature[3],
            "units": "|".join(f"{row['city']} {row['town']} {row['unit']}" for row in rows),
        })

    write_csv(OUT / "nec_2026_reported_duplicate_cases.csv", case_rows)
    write_csv(OUT / "nec_2026_reported_duplicate_pairs.csv", pair_rows)
    (OUT / "nec_2026_fetch_manifest.json").write_text(
        json.dumps(
            {
                "source": "NEC election statistics system VCCP08 official result HTML",
                "election_id": "0020260603",
                "election_code": 3,
                "case_rows": len(case_rows),
                "duplicate_pairs": len(pair_rows),
                "towns": manifest,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    print({"case_rows": len(case_rows), "duplicate_pairs": len(pair_rows)})


if __name__ == "__main__":
    main()
