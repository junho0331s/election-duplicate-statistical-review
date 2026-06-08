#!/usr/bin/env python3
from __future__ import annotations

import csv
import importlib.util
import random
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs"
OUT.mkdir(parents=True, exist_ok=True)

TRIALS = 200_000
SAMPLE_SIZE = 393
SEED = 20_260_609

spec = importlib.util.spec_from_file_location("analyze_duplicates", ROOT / "scripts" / "analyze_duplicates.py")
mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(mod)


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def governor_top2_signatures() -> list[tuple[int, int]]:
    records = []
    for name, path, parser in mod.DATASETS:
        records.extend(parser(path, name))

    governor = [
        rec for rec in records
        if rec["category"] == "시·도지사" and rec["vote_class"] == "관내사전투표"
    ]

    by_contest: dict[tuple[str, str, str, str], list[dict[str, Any]]] = defaultdict(list)
    for rec in governor:
        by_contest[(rec["election"], rec["category"], rec["contest"], rec["vote_class"])].append(rec)

    signatures: list[tuple[int, int]] = []
    for rows in by_contest.values():
        totals: Counter[int] = Counter()
        for rec in rows:
            for idx, vote in enumerate(rec["votes"]):
                totals[idx] += vote
        top2 = [idx for idx, _ in totals.most_common(2)]
        for rec in rows:
            signatures.append(tuple(rec["votes"][idx] if idx < len(rec["votes"]) else 0 for idx in top2))
    return signatures


def main() -> None:
    signatures = governor_top2_signatures()
    if len(signatures) < SAMPLE_SIZE:
        raise SystemExit(f"Not enough historical signatures: {len(signatures)} < {SAMPLE_SIZE}")

    rng = random.Random(SEED)
    histogram: Counter[int] = Counter()
    for _ in range(TRIALS):
        sample = rng.sample(signatures, k=SAMPLE_SIZE)
        counts = Counter(sample)
        duplicate_groups = sum(1 for count in counts.values() if count >= 2)
        histogram[duplicate_groups] += 1

    hist_rows = [
        {
            "duplicate_groups": duplicate_groups,
            "trials": count,
            "share": count / TRIALS,
        }
        for duplicate_groups, count in sorted(histogram.items())
    ]
    write_csv(OUT / "governor_bootstrap_histogram.csv", hist_rows)

    def tail(threshold: int) -> int:
        return sum(count for duplicate_groups, count in histogram.items() if duplicate_groups >= threshold)

    summary = []
    for threshold in [3, 4, 5]:
        exceed = tail(threshold)
        empirical_probability = exceed / TRIALS
        summary.append({
            "sample_size": SAMPLE_SIZE,
            "trials": TRIALS,
            "seed": SEED,
            "historical_signatures": len(signatures),
            "unique_historical_signatures": len(set(signatures)),
            "threshold": threshold,
            "exceedances": exceed,
            "probability": empirical_probability,
            "plus_one_probability": (exceed + 1) / (TRIALS + 1),
            "resolution": 1 / TRIALS,
            "rule_of_three_upper_95": 3 / TRIALS if exceed == 0 else "",
        })
    write_csv(OUT / "governor_bootstrap_summary.csv", summary)
    print(summary)


if __name__ == "__main__":
    main()
