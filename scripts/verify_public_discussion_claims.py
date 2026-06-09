#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs"
DATA = ROOT / "data" / "pres2022.xlsx"


def clean_int(value: object) -> int:
    return int(str(value).replace(",", "").strip())


def main() -> None:
    OUT.mkdir(exist_ok=True)
    df = pd.read_excel(DATA, sheet_name="Data", dtype=str).fillna("")
    target = df[
        (df["시도"] == "대구광역시")
        & (df["구시군"] == "서구")
        & (df["투표구명"].isin(["비산1동제3투", "비산1동제4투"]))
    ].copy()

    rows: list[dict[str, object]] = []
    for _, row in target.iterrows():
        rows.append({
            "election": "2022-presidential",
            "city": row["시도"],
            "district": row["구시군"],
            "polling_station": row["투표구명"],
            "lee_jae_myung": clean_int(row["더불어민주당\n이재명"]),
            "yoon_suk_yeol": clean_int(row["국민의힘\n윤석열"]),
            "ballots_cast": clean_int(row["투표수"]),
            "registered_voters": clean_int(row["선거인수"]),
        })

    stations = {row["polling_station"] for row in rows}
    pair_values = {(row["lee_jae_myung"], row["yoon_suk_yeol"]) for row in rows}
    ballots = {row["ballots_cast"] for row in rows}
    voters = {row["registered_voters"] for row in rows}
    failures = []
    if stations != {"비산1동제3투", "비산1동제4투"}:
        failures.append("target polling stations not found")
    if pair_values != {(131, 618)}:
        failures.append(f"unexpected candidate vote pair values: {sorted(pair_values)}")
    if len(ballots) != 2:
        failures.append("ballots cast should differ between the two rows")
    if len(voters) != 2:
        failures.append("registered-voter counts should differ between the two rows")

    summary = {
        "status": "pass" if not failures else "fail",
        "scope": "official-data check of a public-discussion auxiliary identical-pair claim",
        "source_file": "data/pres2022.xlsx",
        "row_count": len(rows),
        "confirmed_pair": {
            "lee_jae_myung": 131,
            "yoon_suk_yeol": 618,
        },
        "classification": "auxiliary one-pair election-day polling-station case, not pooled into the primary in-district early-vote five-pair test",
        "failures": failures,
    }

    csv_path = OUT / "public_discussion_claims_audit.csv"
    json_path = OUT / "public_discussion_claims_audit.json"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "election",
                "city",
                "district",
                "polling_station",
                "lee_jae_myung",
                "yoon_suk_yeol",
                "ballots_cast",
                "registered_voters",
            ],
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)
    json_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    if failures:
        raise SystemExit("Public-discussion claim check failed: " + "; ".join(failures))
    print(f"Public-discussion claim check passed with {len(rows)} official rows.")


if __name__ == "__main__":
    main()
