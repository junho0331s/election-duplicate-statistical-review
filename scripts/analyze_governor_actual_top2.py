#!/usr/bin/env python3
from __future__ import annotations

import csv
import importlib.util
import math
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs"
OUT.mkdir(parents=True, exist_ok=True)

spec = importlib.util.spec_from_file_location("analyze_duplicates", ROOT / "scripts" / "analyze_duplicates.py")
mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(mod)


def poisson_tail_at_least(lam: float, threshold: int) -> float:
    return 1 - sum(math.exp(-lam) * lam**k / math.factorial(k) for k in range(threshold))


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
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

    duplicate_rows: list[dict[str, Any]] = []
    summary_by_contest: list[dict[str, Any]] = []
    comparison_pairs = 0
    collision_pairs = 0

    for key, rows in sorted(by_contest.items()):
        election, category, contest, vote_class = key
        if len(rows) < 2:
            continue

        totals: Counter[int] = Counter()
        labels = rows[0]["candidate_labels"]
        for rec in rows:
            for idx, vote in enumerate(rec["votes"]):
                totals[idx] += vote
        top2 = [idx for idx, _ in totals.most_common(2)]
        top2_names = [mod.candidate_name(labels[idx]) for idx in top2]

        buckets: dict[tuple[int, int], list[dict[str, Any]]] = defaultdict(list)
        for rec in rows:
            sig = tuple(rec["votes"][idx] if idx < len(rec["votes"]) else 0 for idx in top2)
            buckets[sig].append(rec)

        contest_comparisons = len(rows) * (len(rows) - 1) // 2
        contest_collisions = 0
        duplicate_group_count = 0
        for sig, sig_rows in sorted(buckets.items()):
            if len(sig_rows) < 2:
                continue
            pairs = len(sig_rows) * (len(sig_rows) - 1) // 2
            contest_collisions += pairs
            duplicate_group_count += 1
            duplicate_rows.append({
                "election": election,
                "contest": contest,
                "vote_class": vote_class,
                "candidate_1": top2_names[0],
                "candidate_2": top2_names[1],
                "signature": f"{sig[0]},{sig[1]}",
                "duplicate_units": len(sig_rows),
                "collision_pairs": pairs,
                "units": "|".join(rec["unit"] for rec in sig_rows),
            })

        comparison_pairs += contest_comparisons
        collision_pairs += contest_collisions
        summary_by_contest.append({
            "election": election,
            "contest": contest,
            "units": len(rows),
            "comparison_pairs": contest_comparisons,
            "duplicate_groups": duplicate_group_count,
            "collision_pairs": contest_collisions,
            "candidate_1": top2_names[0],
            "candidate_2": top2_names[1],
        })

    khat = comparison_pairs / collision_pairs if collision_pairs else float("inf")
    # Official VCCP08 HTML count for Gwangju+Jeonnam in-district early-vote
    # counting units: 96 in Gwangju + 297 in Jeonnam.
    n = 393
    lam = n * (n - 1) / (2 * khat)
    summary = [{
        "governor_contests": len(by_contest),
        "comparison_pairs": comparison_pairs,
        "collision_pairs": collision_pairs,
        "duplicate_groups": len(duplicate_rows),
        "contests_with_duplicates": sum(1 for row in summary_by_contest if row["duplicate_groups"] > 0),
        "max_duplicate_groups_in_contest": max((row["duplicate_groups"] for row in summary_by_contest), default=0),
        "khat": round(khat, 3),
        "n_for_probability": n,
        "lambda": round(lam, 6),
        "p_at_least_5": poisson_tail_at_least(lam, 5),
        "p_at_least_6": poisson_tail_at_least(lam, 6),
    }]

    write_csv(OUT / "governor_actual_top2_summary.csv", summary)
    write_csv(OUT / "governor_actual_top2_by_contest.csv", summary_by_contest)
    write_csv(OUT / "governor_actual_top2_duplicates.csv", duplicate_rows)
    print(summary[0])


if __name__ == "__main__":
    main()
