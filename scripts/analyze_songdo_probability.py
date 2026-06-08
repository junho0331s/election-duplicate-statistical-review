#!/usr/bin/env python3
from __future__ import annotations

import csv
import importlib.util
import math
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

YEONSU = {
    "city_code": "2800",
    "city": "인천광역시",
    "town_code": "2804",
    "town": "연수구",
}
K_SPACE = 100_944.8


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    path = fetch_mod.raw_path(YEONSU)
    rows = fetch_mod.parse_table(path.read_text(encoding="utf-8"), YEONSU)
    early = [
        row for row in rows
        if row["vote_class"] == "관내사전투표" and row["unit"] != "합계"
    ]
    songdo = {row["unit"]: row for row in early if row["unit"] in {"송도1동", "송도2동"}}
    if set(songdo) != {"송도1동", "송도2동"}:
        raise SystemExit(f"Missing Songdo rows: {sorted(songdo)}")

    n = len(early)
    pair_count = n * (n - 1) // 2
    lam = pair_count / K_SPACE
    p_any_pair_in_yeonsu = 1 - math.exp(-lam)
    p_designated_pair_match = 1 / K_SPACE

    rows_out = [
        {
            "case": "yeonsu_any_pair",
            "description": "연수구 관내사전 개표단위 15개 중 어딘가 한 쌍 이상 같은 1·2위 득표쌍",
            "n_units": n,
            "comparison_pairs": pair_count,
            "k_space": K_SPACE,
            "lambda": lam,
            "probability": p_any_pair_in_yeonsu,
            "probability_percent": p_any_pair_in_yeonsu * 100,
            "reciprocal": 1 / p_any_pair_in_yeonsu,
        },
        {
            "case": "songdo1_songdo2_designated_pair",
            "description": "특정된 송도1동-송도2동 두 개표단위가 같은 1·2위 득표쌍을 갖는 조건부 확률",
            "n_units": 2,
            "comparison_pairs": 1,
            "k_space": K_SPACE,
            "lambda": "",
            "probability": p_designated_pair_match,
            "probability_percent": p_designated_pair_match * 100,
            "reciprocal": 1 / p_designated_pair_match,
        },
    ]

    detail_rows = []
    for unit in ["송도1동", "송도2동"]:
        row = songdo[unit]
        votes = row["candidate_votes"]
        detail_rows.append({
            "unit": unit,
            "candidate_1": "박찬대",
            "candidate_1_votes": votes["박찬대"],
            "candidate_2": "유정복",
            "candidate_2_votes": votes["유정복"],
            "electors": row["electors"],
            "turnout": row["turnout"],
            "invalid_votes": row["invalid_votes"],
            "abstentions": row["abstentions"],
            "source_file": row["source_file"],
        })

    write_csv(OUT / "songdo_probability_summary.csv", rows_out)
    write_csv(OUT / "songdo_official_rows.csv", detail_rows)
    print({
        "yeonsu_in_district_early_units": n,
        "p_any_pair_in_yeonsu": p_any_pair_in_yeonsu,
        "p_songdo1_songdo2_designated_pair": p_designated_pair_match,
        "outputs": [
            "outputs/songdo_probability_summary.csv",
            "outputs/songdo_official_rows.csv",
        ],
    })


if __name__ == "__main__":
    main()
