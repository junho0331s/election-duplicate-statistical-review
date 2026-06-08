#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import importlib.util
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs"
OUT.mkdir(parents=True, exist_ok=True)

spec = importlib.util.spec_from_file_location(
    "fetch_nec_2026_duplicate_cases",
    ROOT / "scripts" / "fetch_nec_2026_duplicate_cases.py",
)
fetch_mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(fetch_mod)

GWANGJU_JEONNAM_TOWNS = [
    {"city_code": "2900", "city": "광주광역시", "town_code": "2901", "town": "동구"},
    {"city_code": "2900", "city": "광주광역시", "town_code": "2902", "town": "서구"},
    {"city_code": "2900", "city": "광주광역시", "town_code": "2903", "town": "남구"},
    {"city_code": "2900", "city": "광주광역시", "town_code": "2904", "town": "북구"},
    {"city_code": "2900", "city": "광주광역시", "town_code": "2905", "town": "광산구"},
    {"city_code": "4600", "city": "전라남도", "town_code": "4601", "town": "목포시"},
    {"city_code": "4600", "city": "전라남도", "town_code": "4602", "town": "여수시"},
    {"city_code": "4600", "city": "전라남도", "town_code": "4604", "town": "순천시"},
    {"city_code": "4600", "city": "전라남도", "town_code": "4606", "town": "나주시"},
    {"city_code": "4600", "city": "전라남도", "town_code": "4607", "town": "광양시"},
    {"city_code": "4600", "city": "전라남도", "town_code": "4608", "town": "담양군"},
    {"city_code": "4600", "city": "전라남도", "town_code": "4609", "town": "장성군"},
    {"city_code": "4600", "city": "전라남도", "town_code": "4610", "town": "곡성군"},
    {"city_code": "4600", "city": "전라남도", "town_code": "4611", "town": "구례군"},
    {"city_code": "4600", "city": "전라남도", "town_code": "4612", "town": "고흥군"},
    {"city_code": "4600", "city": "전라남도", "town_code": "4613", "town": "보성군"},
    {"city_code": "4600", "city": "전라남도", "town_code": "4614", "town": "화순군"},
    {"city_code": "4600", "city": "전라남도", "town_code": "4615", "town": "장흥군"},
    {"city_code": "4600", "city": "전라남도", "town_code": "4616", "town": "강진군"},
    {"city_code": "4600", "city": "전라남도", "town_code": "4617", "town": "완도군"},
    {"city_code": "4600", "city": "전라남도", "town_code": "4618", "town": "해남군"},
    {"city_code": "4600", "city": "전라남도", "town_code": "4619", "town": "진도군"},
    {"city_code": "4600", "city": "전라남도", "town_code": "4620", "town": "영암군"},
    {"city_code": "4600", "city": "전라남도", "town_code": "4621", "town": "무안군"},
    {"city_code": "4600", "city": "전라남도", "town_code": "4622", "town": "영광군"},
    {"city_code": "4600", "city": "전라남도", "town_code": "4623", "town": "함평군"},
    {"city_code": "4600", "city": "전라남도", "town_code": "4624", "town": "신안군"},
]


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def load_town_rows(town: dict[str, str], fetch: bool) -> list[dict[str, Any]]:
    path = fetch_mod.raw_path(town)
    if fetch or not path.exists():
        text = fetch_mod.fetch_town(town)
        path.write_text(text, encoding="utf-8")
    else:
        text = path.read_text(encoding="utf-8")
    return fetch_mod.parse_table(text, town)


def main() -> None:
    argp = argparse.ArgumentParser()
    argp.add_argument("--fetch", action="store_true", help="refresh official NEC HTML cache")
    args = argp.parse_args()

    rows: list[dict[str, Any]] = []
    unit_rows: list[dict[str, Any]] = []
    for town in GWANGJU_JEONNAM_TOWNS:
        parsed = load_town_rows(town, fetch=args.fetch)
        early = [
            row for row in parsed
            if row["vote_class"] == "관내사전투표" and row["unit"] != "합계"
        ]
        rows.append({
            "city": town["city"],
            "city_code": town["city_code"],
            "town": town["town"],
            "town_code": town["town_code"],
            "in_district_early_units": len(early),
            "source_file": str(fetch_mod.raw_path(town).relative_to(ROOT)),
            "source_url": fetch_mod.REFERER,
        })
        for row in early:
            unit_rows.append({
                "city": town["city"],
                "city_code": town["city_code"],
                "town": town["town"],
                "town_code": town["town_code"],
                "unit": row["unit"],
                "vote_class": row["vote_class"],
                "electors": row["electors"],
                "turnout": row["turnout"],
                "source_file": row["source_file"],
            })

    total = sum(row["in_district_early_units"] for row in rows)
    summary = {
        "source": "NEC election statistics system VCCP08 official result HTML",
        "election_id": "0020260603",
        "election_code": 3,
        "regions": ["광주광역시", "전라남도"],
        "towns": len(rows),
        "in_district_early_units": total,
        "output_counts": "outputs/nec_2026_gwangju_jeonnam_unit_counts.csv",
        "output_units": "outputs/nec_2026_gwangju_jeonnam_units.csv",
    }

    write_csv(OUT / "nec_2026_gwangju_jeonnam_unit_counts.csv", rows)
    write_csv(OUT / "nec_2026_gwangju_jeonnam_units.csv", unit_rows)
    (OUT / "nec_2026_gwangju_jeonnam_unit_summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(summary)


if __name__ == "__main__":
    main()
