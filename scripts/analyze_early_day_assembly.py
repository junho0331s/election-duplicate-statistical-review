#!/usr/bin/env python3
from __future__ import annotations

import csv
import math
from collections import defaultdict
from pathlib import Path
from typing import Any

import openpyxl


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "outputs"
OUT.mkdir(parents=True, exist_ok=True)


DATASETS = [
    ("2016-assembly", DATA / "assembly2016.xlsx", "새누리당"),
    ("2020-assembly", DATA / "assembly2020.xlsx", "미래통합당"),
    ("2024-assembly", DATA / "assembly2024.xlsx", "국민의힘"),
]


def clean(value: Any) -> str:
    if value is None:
        return ""
    return str(value).replace("_x000D_", "").strip()


def num(value: Any) -> int:
    if value in (None, ""):
        return 0
    try:
        return int(str(value).replace(",", "").strip())
    except ValueError:
        return 0


def is_absentee_or_total(emd: str, unit: str) -> bool:
    joined = f"{emd} {unit}"
    return any(token in joined for token in ["합계", "소계", "거소", "선상", "국외", "재외"])


def vote_bucket(emd: str, unit: str) -> str | None:
    joined = f"{emd} {unit}"
    if "관내사전투표" in joined or "관외사전투표" in joined:
        return "early"
    if is_absentee_or_total(emd, unit):
        return None
    if unit:
        return "day"
    return None


def parse_candidate_headers(rows: list[tuple[Any, ...]], start: int) -> list[tuple[int, str, str]]:
    parties = [clean(x) for x in rows[start][6:]]
    names = [clean(x) for x in rows[start + 1][6:]]
    out = []
    for j, (party, name) in enumerate(zip(parties, names), start=6):
        if party or name:
            out.append((j, party, name))
    return out


def analyze_assembly(election: str, path: Path, conservative_party: str) -> list[dict[str, Any]]:
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    ws = wb["지역구"]
    rows = list(ws.iter_rows(values_only=True))
    out: list[dict[str, Any]] = []
    i = 1
    while i < len(rows):
        row = rows[i]
        # Candidate header block: party row followed by name row.
        if clean(row[2] if len(row) > 2 else "") == "" and num(row[6] if len(row) > 6 else None) == 0:
            ccols = parse_candidate_headers(rows, i)
            party_to_col = {party: (idx, name) for idx, party, name in ccols}
            if "더불어민주당" not in party_to_col or conservative_party not in party_to_col:
                i += 2
                continue
            dem_idx, dem_name = party_to_col["더불어민주당"]
            con_idx, con_name = party_to_col[conservative_party]
            totals = defaultdict(lambda: {"dem": 0, "con": 0})
            current_sido = ""
            current_district = ""
            i += 2
            while i < len(rows):
                r = rows[i]
                if clean(r[0]) and clean(r[2]) == "" and clean(r[3]) == "" and num(r[6] if len(r) > 6 else None) == 0:
                    break
                if clean(r[0]):
                    current_sido = clean(r[0])
                if clean(r[1]):
                    current_district = clean(r[1])
                emd, unit = clean(r[2]), clean(r[3])
                bucket = vote_bucket(emd, unit)
                if bucket:
                    totals[bucket]["dem"] += num(r[dem_idx])
                    totals[bucket]["con"] += num(r[con_idx])
                i += 1
            e_dem, e_con = totals["early"]["dem"], totals["early"]["con"]
            d_dem, d_con = totals["day"]["dem"], totals["day"]["con"]
            n_e, n_d = e_dem + e_con, d_dem + d_con
            if n_e > 0 and n_d > 0:
                p_e = e_dem / n_e
                p_d = d_dem / n_d
                pooled = (e_dem + d_dem) / (n_e + n_d)
                se = math.sqrt(pooled * (1 - pooled) * (1 / n_e + 1 / n_d))
                z = (p_e - p_d) / se if se else 0.0
                out.append({
                    "election": election,
                    "sido": current_sido,
                    "district": current_district,
                    "dem_name": dem_name,
                    "con_party": conservative_party,
                    "con_name": con_name,
                    "early_dem": e_dem,
                    "early_con": e_con,
                    "day_dem": d_dem,
                    "day_con": d_con,
                    "early_two_party_votes": n_e,
                    "day_two_party_votes": n_d,
                    "early_dem_share": p_e,
                    "day_dem_share": p_d,
                    "early_minus_day_pp": (p_e - p_d) * 100,
                    "z": z,
                })
            continue
        i += 1
    return out


def sign_test_tail(successes: int, trials: int) -> float:
    """One-sided sign-test tail under P(positive)=0.5."""
    if successes < 0 or successes > trials:
        raise ValueError("successes must be between 0 and trials")
    numerator = sum(math.comb(trials, k) for k in range(successes, trials + 1))
    return numerator / (2 ** trials)


def main() -> None:
    rows: list[dict[str, Any]] = []
    for election, path, conservative_party in DATASETS:
        rows.extend(analyze_assembly(election, path, conservative_party))

    with (OUT / "early_day_assembly_twoparty.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    summary_rows = []
    for election in sorted({r["election"] for r in rows}):
        subset = [r for r in rows if r["election"] == election]
        diffs = sorted(r["early_minus_day_pp"] for r in subset)
        zs = [r["z"] for r in subset]
        summary_rows.append({
            "election": election,
            "districts": len(subset),
            "mean_early_minus_day_pp": sum(diffs) / len(diffs),
            "median_early_minus_day_pp": diffs[len(diffs) // 2],
            "dem_early_higher_count": sum(1 for d in diffs if d > 0),
            "dem_early_lower_count": sum(1 for d in diffs if d < 0),
            "sign_test_p_one_sided": sign_test_tail(sum(1 for d in diffs if d > 0), len(subset)),
            "sign_test_reciprocal": 1 / sign_test_tail(sum(1 for d in diffs if d > 0), len(subset)),
            "abs_z_gt_5": sum(1 for z in zs if abs(z) > 5),
            "abs_z_gt_10": sum(1 for z in zs if abs(z) > 10),
            "max_abs_z": max(abs(z) for z in zs),
        })

    with (OUT / "early_day_assembly_summary.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(summary_rows[0].keys()))
        writer.writeheader()
        writer.writerows(summary_rows)

    print(summary_rows)


if __name__ == "__main__":
    main()
