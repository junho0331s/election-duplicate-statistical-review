#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs"


def read_csv(path: str) -> list[dict[str, str]]:
    with (ROOT / path).open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def read_json(path: str) -> Any:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def require_equal(name: str, actual: Any, expected: Any) -> dict[str, Any]:
    if actual != expected:
        raise AssertionError(f"{name}: expected {expected!r}, got {actual!r}")
    return {"claim": name, "expected": expected, "actual": actual, "status": "pass"}


def require_close(name: str, actual: float, expected: float, abs_tol: float) -> dict[str, Any]:
    if not math.isclose(actual, expected, rel_tol=0, abs_tol=abs_tol):
        raise AssertionError(f"{name}: expected {expected!r}, got {actual!r}")
    return {"claim": name, "expected": expected, "actual": actual, "abs_tol": abs_tol, "status": "pass"}


def write_checks_csv(checks: list[dict[str, Any]], path: Path) -> None:
    fieldnames = ["claim", "expected", "actual", "abs_tol", "status"]
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        for check in checks:
            row: dict[str, Any] = {}
            for key in fieldnames:
                value = check.get(key, "")
                if isinstance(value, (list, dict, tuple)):
                    value = json.dumps(value, ensure_ascii=False, sort_keys=True)
                row[key] = value
            writer.writerow(row)


def main() -> None:
    checks: list[dict[str, Any]] = []

    dataset_rows = read_csv("outputs/dataset_counts.csv")
    checks.append(require_equal(
        "historical parsed rows",
        sum(int(row["rows"]) for row in dataset_rows),
        81_701,
    ))

    governor_summary = read_csv("outputs/governor_actual_top2_summary.csv")[0]
    checks.extend([
        require_equal("historical governor contests", int(governor_summary["governor_contests"]), 51),
        require_equal("historical governor comparison pairs", int(governor_summary["comparison_pairs"]), 1_514_172),
        require_equal("historical governor collision pairs", int(governor_summary["collision_pairs"]), 15),
        require_equal("historical governor duplicate groups", int(governor_summary["duplicate_groups"]), 15),
        require_equal("historical maximum duplicate groups in one contest", int(governor_summary["max_duplicate_groups_in_contest"]), 3),
        require_close("estimated effective pair space khat", float(governor_summary["khat"]), 100_944.8, 1e-9),
        require_equal("probability N from official HTML units", int(governor_summary["n_for_probability"]), 393),
        require_close("governor baseline p_at_least_5", float(governor_summary["p_at_least_5"]), 0.0011484064248148407, 1e-15),
    ])

    probability_rows = {int(row["threshold"]): row for row in read_csv("outputs/probability_core.csv")}
    checks.extend([
        require_close("Poisson probability threshold 3", float(probability_rows[3]["probability"]), 0.04226077201454281, 1e-15),
        require_close("Poisson probability threshold 4", float(probability_rows[4]["probability"]), 0.007734837111887716, 1e-15),
        require_close("Poisson probability threshold 5", float(probability_rows[5]["probability"]), 0.0011484064248148407, 1e-15),
        require_close("Poisson probability percent threshold 5", float(probability_rows[5]["probability_percent"]), 0.11484064248148407, 1e-12),
        require_close("Poisson probability threshold 6", float(probability_rows[6]["probability"]), 0.00014322422035484283, 1e-15),
    ])

    bootstrap_rows = {int(row["threshold"]): row for row in read_csv("outputs/governor_bootstrap_summary.csv")}
    bootstrap_5 = bootstrap_rows[5]
    checks.extend([
        require_equal("bootstrap sample size", int(bootstrap_5["sample_size"]), 393),
        require_equal("bootstrap trials", int(bootstrap_5["trials"]), 200_000),
        require_equal("bootstrap threshold 5 exceedances", int(bootstrap_5["exceedances"]), 0),
        require_close("bootstrap threshold 5 probability", float(bootstrap_5["probability"]), 0.0, 0.0),
        require_close("bootstrap rule-of-three upper 95", float(bootstrap_5["rule_of_three_upper_95"]), 0.000015, 1e-18),
    ])

    unit_summary = read_json("outputs/nec_2026_gwangju_jeonnam_unit_summary.json")
    unit_rows = read_csv("outputs/nec_2026_gwangju_jeonnam_units.csv")
    checks.extend([
        require_equal("NEC 2026 Gwangju-Jeonnam towns", int(unit_summary["towns"]), 27),
        require_equal("NEC 2026 Gwangju-Jeonnam in-district early units summary", int(unit_summary["in_district_early_units"]), 393),
        require_equal("NEC 2026 Gwangju-Jeonnam in-district early unit rows", len(unit_rows), 393),
    ])

    case_rows = read_csv("outputs/nec_2026_reported_duplicate_cases.csv")
    pair_rows = read_csv("outputs/nec_2026_reported_duplicate_pairs.csv")
    gwangju_jeonnam_pairs = [row for row in pair_rows if row["candidate_1"] == "민형배" and row["candidate_2"] == "이정현"]
    checks.extend([
        require_equal("NEC 2026 event rows", len(case_rows), 12),
        require_equal("NEC 2026 duplicate pairs", len(pair_rows), 6),
        require_equal("NEC 2026 Gwangju-Jeonnam Min-Lee duplicate pairs", len(gwangju_jeonnam_pairs), 5),
    ])

    expected_pairs = {
        ("1401", "120"),
        ("506", "42"),
        ("444", "46"),
        ("606", "57"),
        ("356", "42"),
    }
    actual_pairs = {(row["candidate_1_votes"], row["candidate_2_votes"]) for row in gwangju_jeonnam_pairs}
    checks.append(require_equal("NEC 2026 Gwangju-Jeonnam duplicate pair values", sorted(actual_pairs), sorted(expected_pairs)))

    songdo_rows = {row["case"]: row for row in read_csv("outputs/songdo_probability_summary.csv")}
    checks.extend([
        require_equal("Songdo Yeonsu unit count", int(songdo_rows["yeonsu_any_pair"]["n_units"]), 15),
        require_close("Songdo Yeonsu any-pair probability percent", float(songdo_rows["yeonsu_any_pair"]["probability_percent"]), 0.10396316588441312, 1e-14),
        require_close("Songdo designated-pair probability percent", float(songdo_rows["songdo1_songdo2_designated_pair"]["probability_percent"]), 0.0009906404292246852, 1e-18),
    ])

    early_rows = {row["election"]: row for row in read_csv("outputs/early_day_assembly_summary.csv")}
    checks.extend([
        require_equal("2016 assembly districts", int(early_rows["2016-assembly"]["districts"]), 229),
        require_equal("2016 Democratic early higher count", int(early_rows["2016-assembly"]["dem_early_higher_count"]), 211),
        require_equal("2016 Democratic early lower count", int(early_rows["2016-assembly"]["dem_early_lower_count"]), 18),
        require_equal("2020 assembly districts", int(early_rows["2020-assembly"]["districts"]), 236),
        require_equal("2020 Democratic early higher count", int(early_rows["2020-assembly"]["dem_early_higher_count"]), 236),
        require_equal("2020 Democratic early lower count", int(early_rows["2020-assembly"]["dem_early_lower_count"]), 0),
        require_equal("2024 assembly districts", int(early_rows["2024-assembly"]["districts"]), 245),
        require_equal("2024 Democratic early higher count", int(early_rows["2024-assembly"]["dem_early_higher_count"]), 245),
        require_equal("2024 Democratic early lower count", int(early_rows["2024-assembly"]["dem_early_lower_count"]), 0),
        require_close("2016 mean early-day difference pp", float(early_rows["2016-assembly"]["mean_early_minus_day_pp"]), 3.902347771407794, 1e-12),
        require_close("2020 mean early-day difference pp", float(early_rows["2020-assembly"]["mean_early_minus_day_pp"]), 10.881931488172144, 1e-12),
        require_close("2024 mean early-day difference pp", float(early_rows["2024-assembly"]["mean_early_minus_day_pp"]), 10.351186302658121, 1e-12),
    ])

    result = {
        "status": "pass",
        "check_count": len(checks),
        "scope": "core reproducible statistical claims only; causal attribution requires raw administrative records",
        "checks": checks,
    }
    out_path = OUT / "core_claims_verification.json"
    out_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    csv_path = OUT / "core_claims_verification.csv"
    write_checks_csv(checks, csv_path)
    print(f"Core claim verification passed with {len(checks)} checks.")
    print(f"Wrote {out_path.relative_to(ROOT)}")
    print(f"Wrote {csv_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
