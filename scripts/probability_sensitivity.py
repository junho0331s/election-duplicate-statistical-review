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

    write_csv(OUT / "probability_core.csv", core)
    write_csv(OUT / "probability_k_sensitivity.csv", k_sensitivity)
    write_csv(OUT / "probability_n_sensitivity.csv", n_sensitivity)

    print({
        "base_n": base_n,
        "base_k": base_k,
        "p_at_least_5": core[2]["probability"],
        "p_at_least_6": core[3]["probability"],
        "outputs": [
            "outputs/probability_core.csv",
            "outputs/probability_k_sensitivity.csv",
            "outputs/probability_n_sensitivity.csv",
        ],
    })


if __name__ == "__main__":
    main()
