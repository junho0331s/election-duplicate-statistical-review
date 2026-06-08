#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs"


@dataclass
class RobustnessCheck:
    check: str
    expected: str
    actual: str
    status: str


def read_csv(name: str) -> list[dict[str, str]]:
    with (OUT / name).open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def pass_fail(condition: bool) -> str:
    return "pass" if condition else "fail"


def check(condition: bool, name: str, expected: str, actual: str) -> RobustnessCheck:
    return RobustnessCheck(name, expected, actual, pass_fail(condition))


def row_by(rows: list[dict[str, str]], **criteria: str) -> dict[str, str]:
    for row in rows:
        if all(row.get(key) == value for key, value in criteria.items()):
            return row
    raise KeyError(f"Missing row for {criteria}")


def audit_checks() -> list[RobustnessCheck]:
    core = read_csv("probability_core.csv")
    exact = read_csv("probability_exact_collision.csv")
    k_sens = read_csv("probability_k_sensitivity.csv")
    n_sens = read_csv("probability_n_sensitivity.csv")
    bootstrap = read_csv("governor_bootstrap_summary.csv")
    governor = read_csv("governor_actual_top2_summary.csv")[0]

    core5 = row_by(core, threshold="5")
    exact5 = row_by(exact, threshold="5")
    boot5 = row_by(bootstrap, threshold="5")
    k50 = row_by(k_sens, k_space="50000", threshold="5")
    k100 = row_by(k_sens, k_space="100944.8", threshold="5")
    k200 = row_by(k_sens, k_space="200000", threshold="5")
    n350 = row_by(n_sens, n="350", threshold="5")
    n393 = row_by(n_sens, n="393", threshold="5")
    n450 = row_by(n_sens, n="450", threshold="5")

    p_core5 = float(core5["probability"])
    p_exact5 = float(exact5["exact_probability"])
    p_k50 = float(k50["probability"])
    p_k100 = float(k100["probability"])
    p_k200 = float(k200["probability"])
    p_n350 = float(n350["probability"])
    p_n393 = float(n393["probability"])
    p_n450 = float(n450["probability"])
    boot_exceed = int(boot5["exceedances"])
    boot_trials = int(boot5["trials"])
    rule_three = float(boot5["rule_of_three_upper_95"])

    checks = [
        check(
            int(float(governor["governor_contests"])) == 51
            and int(float(governor["max_duplicate_groups_in_contest"])) == 3,
            "historical empirical upper bound",
            "51 governor contests and historical maximum 3 repeated pairs",
            f"{governor['governor_contests']} contests, max {governor['max_duplicate_groups_in_contest']}",
        ),
        check(
            math.isclose(p_core5, 0.0011484064248148407, rel_tol=0, abs_tol=1e-15),
            "Poisson baseline probability",
            "P(C>=5) equals 0.0011484064248148407",
            f"{p_core5}",
        ),
        check(
            math.isclose(p_exact5, 0.0012190883791786122, rel_tol=0, abs_tol=1e-15),
            "exact collision probability",
            "exact P(C>=5) equals 0.0012190883791786122",
            f"{p_exact5}",
        ),
        check(
            abs(p_exact5 - p_core5) < 0.0001,
            "Poisson and exact agreement",
            "absolute difference below 0.0001",
            f"diff {abs(p_exact5 - p_core5)}",
        ),
        check(
            boot_exceed == 0 and boot_trials == 200000,
            "nonparametric resampling threshold 5",
            "0 exceedances in 200,000 trials",
            f"{boot_exceed} exceedances in {boot_trials} trials",
        ),
        check(
            math.isclose(rule_three, 1.5e-05, rel_tol=0, abs_tol=1e-18),
            "rule-of-three upper bound",
            "95% upper bound equals 0.000015",
            f"{rule_three}",
        ),
        check(
            p_k50 < 0.021 and p_k100 < 0.0012 and p_k200 < 0.000052,
            "effective-pair-space sensitivity",
            "K=50,000 remains below 2.1%, baseline below 0.12%, K=200,000 below 0.006%",
            f"K50 {p_k50}, baseline {p_k100}, K200 {p_k200}",
        ),
        check(
            p_k50 > p_k100 > p_k200,
            "K sensitivity monotonicity",
            "probability decreases as K increases",
            f"K50 {p_k50}, baseline {p_k100}, K200 {p_k200}",
        ),
        check(
            p_n350 < p_n393 < p_n450 and p_n450 < 0.0037,
            "counting-unit N sensitivity",
            "probability increases with N but stays below 0.37% through N=450",
            f"N350 {p_n350}, N393 {p_n393}, N450 {p_n450}",
        ),
        check(
            all(float(row["probability"]) < 0.004 for row in n_sens if row["threshold"] == "5"),
            "N sensitivity upper range",
            "all reported N-sensitivity probabilities for threshold 5 below 0.4%",
            f"max {max(float(row['probability']) for row in n_sens if row['threshold'] == '5')}",
        ),
    ]
    return checks


def main() -> None:
    OUT.mkdir(exist_ok=True)
    checks = audit_checks()
    data = {
        "status": "pass" if all(row.status == "pass" for row in checks) else "fail",
        "check_count": len(checks),
        "scope": "statistical robustness audit for probability, exact-collision, sensitivity, and resampling outputs",
        "checks": [asdict(row) for row in checks],
    }
    (OUT / "statistical_robustness_audit.json").write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    with (OUT / "statistical_robustness_audit.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["check", "expected", "actual", "status"])
        writer.writeheader()
        for row in checks:
            writer.writerow(asdict(row))

    if data["status"] != "pass":
        failures = [row for row in checks if row.status != "pass"]
        sample = "; ".join(f"{row.check}:{row.actual}" for row in failures[:10])
        raise SystemExit(f"Statistical robustness audit failed: {sample}")
    print(f"Statistical robustness audit passed with {len(checks)} checks.")


if __name__ == "__main__":
    main()
