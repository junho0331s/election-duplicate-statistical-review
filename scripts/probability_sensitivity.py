#!/usr/bin/env python3
from __future__ import annotations

import csv
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs"
OUT.mkdir(parents=True, exist_ok=True)


def poisson_tail_at_least(lam: float, threshold: int) -> float:
    return 1 - sum(math.exp(-lam) * lam**k / math.factorial(k) for k in range(threshold))


def exact_pair_collision_tail(n: int, k_space: int, threshold: int) -> float:
    """Exact occupancy tail for pair-collision count >= threshold.

    The state keeps only paths whose current pair-collision count is below the
    threshold. This is enough because all paths at or above the threshold are
    absorbed into the tail probability.
    """
    states: dict[tuple[tuple[int, ...], int], float] = {((0,) * threshold, 0): 1.0}
    for _ in range(n):
        next_states: dict[tuple[tuple[int, ...], int], float] = {}
        for (counts, collision_count), probability in states.items():
            occupied = sum(counts)
            empty_probability = (k_space - occupied) / k_space
            if empty_probability:
                next_counts = list(counts)
                next_counts[0] += 1
                key = (tuple(next_counts), collision_count)
                next_states[key] = next_states.get(key, 0.0) + probability * empty_probability

            for size in range(1, threshold + 1):
                boxes = counts[size - 1]
                if not boxes:
                    continue
                next_collision_count = collision_count + size
                if next_collision_count >= threshold:
                    continue
                next_counts = list(counts)
                next_counts[size - 1] -= 1
                if size < threshold:
                    next_counts[size] += 1
                key = (tuple(next_counts), next_collision_count)
                next_states[key] = next_states.get(key, 0.0) + probability * boxes / k_space
        states = next_states
    return 1 - sum(states.values())


def reciprocal(p: float) -> float:
    return float("inf") if p == 0 else 1 / p


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def probability_row(n: int, k_space: float, threshold: int) -> dict[str, Any]:
    lam = n * (n - 1) / (2 * k_space)
    p = poisson_tail_at_least(lam, threshold)
    return {
        "n": n,
        "k_space": k_space,
        "threshold": threshold,
        "lambda": lam,
        "probability": p,
        "probability_percent": p * 100,
        "reciprocal": reciprocal(p),
    }


def designated_pair_row(case: str, k_space: float, designated_pairs: int) -> dict[str, Any]:
    p = (1 / k_space) ** designated_pairs
    return {
        "case": case,
        "k_space": k_space,
        "designated_pairs": designated_pairs,
        "probability": p,
        "probability_percent": p * 100,
        "reciprocal": reciprocal(p),
    }


def main() -> None:
    base_n = 393
    base_k = 100_944.8

    core = [
        probability_row(base_n, base_k, 3),
        probability_row(base_n, base_k, 4),
        probability_row(base_n, base_k, 5),
        probability_row(base_n, base_k, 6),
    ]

    k_sensitivity = []
    for k_space in [50_000, 100_000, 100_944.8, 200_000, 337_354, 500_000]:
        k_sensitivity.append(probability_row(base_n, k_space, 5))
        k_sensitivity.append(probability_row(base_n, k_space, 6))

    n_sensitivity = []
    for n in [350, 390, 393, 400, 430, 450]:
        n_sensitivity.append(probability_row(n, base_k, 5))

    designated_pairs = [
        designated_pair_row("gwangju_jeonnam_5_pre_designated_pairs", base_k, 5),
        designated_pair_row("nationwide_6_pre_designated_pairs", base_k, 6),
    ]

    write_csv(OUT / "probability_core.csv", core)

    exact_collision = []
    rounded_k = round(base_k)
    for row in core:
        exact_p = exact_pair_collision_tail(base_n, rounded_k, int(row["threshold"]))
        exact_collision.append({
            "n": base_n,
            "k_space": rounded_k,
            "threshold": row["threshold"],
            "poisson_probability": row["probability"],
            "exact_probability": exact_p,
            "exact_probability_percent": exact_p * 100,
            "poisson_minus_exact": row["probability"] - exact_p,
            "exact_reciprocal": reciprocal(exact_p),
        })
    write_csv(OUT / "probability_exact_collision.csv", exact_collision)

    write_csv(OUT / "probability_designated_pairs.csv", designated_pairs)
    write_csv(OUT / "probability_k_sensitivity.csv", k_sensitivity)
    write_csv(OUT / "probability_n_sensitivity.csv", n_sensitivity)

    print({
        "base_n": base_n,
        "base_k": base_k,
        "p_at_least_5": core[2]["probability"],
        "p_at_least_6": core[3]["probability"],
        "outputs": [
            "outputs/probability_core.csv",
            "outputs/probability_exact_collision.csv",
            "outputs/probability_designated_pairs.csv",
            "outputs/probability_k_sensitivity.csv",
            "outputs/probability_n_sensitivity.csv",
        ],
    })


if __name__ == "__main__":
    main()
