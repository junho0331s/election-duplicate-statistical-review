#!/usr/bin/env python3
from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = [
    "analyze_duplicates.py",
    "count_nec_2026_gwangju_jeonnam_units.py",
    "analyze_governor_actual_top2.py",
    "bootstrap_governor_duplicates.py",
    "fetch_nec_2026_duplicate_cases.py",
    "analyze_songdo_probability.py",
    "probability_sensitivity.py",
    "analyze_early_day_assembly.py",
    "verify_core_claims.py",
    "statistical_robustness_audit.py",
    "video_source_exclusion_audit.py",
    "source_provenance_audit.py",
    "claim_boundary_audit.py",
    "objection_coverage_audit.py",
    "pre_submission_audit.py",
    "submission_integrity_report.py",
    "generate_checksums.py",
    "create_submission_zip.py",
    "zip_reproduction_audit.py",
    "local_ci_validation_report.py",
    "validate_package.py",
]


def main() -> None:
    for script in SCRIPTS:
        path = ROOT / "scripts" / script
        print(f"\n== {script} ==")
        subprocess.run([sys.executable, str(path)], cwd=ROOT, check=True)

    expected = [
        ROOT / "outputs" / "duplicate_summary.csv",
        ROOT / "outputs" / "duplicate_groups.csv",
        ROOT / "outputs" / "governor_actual_top2_summary.csv",
        ROOT / "outputs" / "governor_actual_top2_by_contest.csv",
        ROOT / "outputs" / "governor_actual_top2_duplicates.csv",
        ROOT / "outputs" / "governor_bootstrap_summary.csv",
        ROOT / "outputs" / "governor_bootstrap_histogram.csv",
        ROOT / "outputs" / "nec_2026_gwangju_jeonnam_unit_counts.csv",
        ROOT / "outputs" / "nec_2026_gwangju_jeonnam_units.csv",
        ROOT / "outputs" / "nec_2026_gwangju_jeonnam_unit_summary.json",
        ROOT / "outputs" / "nec_2026_reported_duplicate_cases.csv",
        ROOT / "outputs" / "nec_2026_reported_duplicate_pairs.csv",
        ROOT / "outputs" / "nec_2026_fetch_manifest.json",
        ROOT / "outputs" / "songdo_probability_summary.csv",
        ROOT / "outputs" / "songdo_official_rows.csv",
        ROOT / "outputs" / "probability_core.csv",
        ROOT / "outputs" / "probability_exact_collision.csv",
        ROOT / "outputs" / "probability_k_sensitivity.csv",
        ROOT / "outputs" / "probability_n_sensitivity.csv",
        ROOT / "outputs" / "early_day_assembly_summary.csv",
        ROOT / "outputs" / "early_day_assembly_twoparty.csv",
        ROOT / "outputs" / "core_claims_verification.csv",
        ROOT / "outputs" / "core_claims_verification.json",
        ROOT / "outputs" / "statistical_robustness_audit.csv",
        ROOT / "outputs" / "statistical_robustness_audit.json",
        ROOT / "outputs" / "video_source_exclusion_audit.csv",
        ROOT / "outputs" / "video_source_exclusion_audit.json",
        ROOT / "outputs" / "source_provenance_audit.csv",
        ROOT / "outputs" / "source_provenance_audit.json",
        ROOT / "outputs" / "claim_boundary_audit.csv",
        ROOT / "outputs" / "claim_boundary_audit.json",
        ROOT / "outputs" / "objection_coverage_audit.csv",
        ROOT / "outputs" / "objection_coverage_audit.json",
        ROOT / "outputs" / "pre_submission_audit.csv",
        ROOT / "outputs" / "pre_submission_audit.json",
        ROOT / "outputs" / "submission_integrity_report.md",
        ROOT / "outputs" / "submission_integrity_report.json",
        ROOT / "outputs" / "local_ci_validation_report.md",
        ROOT / "outputs" / "local_ci_validation_report.json",
        ROOT / "outputs" / "zip_reproduction_audit.md",
        ROOT / "outputs" / "zip_reproduction_audit.json",
        ROOT / "outputs" / "checksums_sha256.csv",
        ROOT / "dist" / "election_duplicate_ieie_submission.zip",
        ROOT / "dist" / "election_duplicate_ieie_submission.zip.sha256",
        ROOT / "dist" / "election_duplicate_ieie_submission_manifest.json",
    ]
    missing = [str(path.relative_to(ROOT)) for path in expected if not path.exists()]
    if missing:
        raise SystemExit(f"Missing expected outputs: {', '.join(missing)}")

    print("\nAll reproduction scripts completed, package validation passed, and expected outputs exist.")


if __name__ == "__main__":
    main()
