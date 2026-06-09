#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
import json
import math
import os
import re
from pathlib import Path
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "requirements.txt",
    "SUBMISSION_INDEX_ko.md",
    "SUBMISSION_INDEX_en.md",
    "PUBLIC_DISCUSSION_CLAIMS_ko.md",
    "PUBLIC_DISCUSSION_CLAIMS_en.md",
    "paper_statistical_implausibility_ko.md",
    "paper_statistical_implausibility_en.md",
    "cover_letter_ko.md",
    "cover_letter_en.md",
    "submission_memo_ko.md",
    "submission_memo_en.md",
    "reviewer_response_ko.md",
    "reviewer_response_en.md",
    "evidence_matrix_ko.md",
    "evidence_matrix_en.md",
    "DATA_DICTIONARY_ko.md",
    "DATA_DICTIONARY_en.md",
    "REVIEWER_QUICKSTART_ko.md",
    "REVIEWER_QUICKSTART_en.md",
    "REPRODUCIBILITY_CHECKLIST_ko.md",
    "REPRODUCIBILITY_CHECKLIST_en.md",
    "STATISTICAL_CALCULATION_NOTE_ko.md",
    "STATISTICAL_CALCULATION_NOTE_en.md",
    "data_availability_2026_ko.md",
    "data_availability_2026_en.md",
    "AUDIT_PROTOCOL_ko.md",
    "AUDIT_PROTOCOL_en.md",
    "ALTERNATIVE_EXPLANATIONS_MATRIX_ko.md",
    "ALTERNATIVE_EXPLANATIONS_MATRIX_en.md",
    "LOOK_ELSEWHERE_ROBUSTNESS_ko.md",
    "LOOK_ELSEWHERE_ROBUSTNESS_en.md",
    "FINAL_SUBMISSION_CHECKLIST_ko.md",
    "FINAL_SUBMISSION_CHECKLIST_en.md",
    "latex/convert_to_ieie.py",
    "latex/ieie/IEIE.cls",
    "latex/ieie/main.tex",
    "latex/ieie/main.pdf",
    "latex/en/main_en.tex",
    "latex/en/main_en.pdf",
    "scripts/analyze_duplicates.py",
    "scripts/count_nec_2026_gwangju_jeonnam_units.py",
    "scripts/analyze_governor_actual_top2.py",
    "scripts/bootstrap_governor_duplicates.py",
    "scripts/fetch_nec_2026_duplicate_cases.py",
    "scripts/analyze_songdo_probability.py",
    "scripts/probability_sensitivity.py",
    "scripts/analyze_early_day_assembly.py",
    "scripts/verify_public_discussion_claims.py",
    "scripts/verify_core_claims.py",
    "scripts/statistical_robustness_audit.py",
    "scripts/video_source_exclusion_audit.py",
    "scripts/source_provenance_audit.py",
    "scripts/claim_boundary_audit.py",
    "scripts/objection_coverage_audit.py",
    "scripts/pre_submission_audit.py",
    "scripts/submission_index_audit.py",
    "scripts/submission_integrity_report.py",
    "scripts/generate_checksums.py",
    "scripts/run_all.py",
    "scripts/validate_package.py",
    "scripts/create_submission_zip.py",
    "scripts/zip_reproduction_audit.py",
    "outputs/duplicate_summary.csv",
    "outputs/dataset_counts.csv",
    "outputs/governor_actual_top2_summary.csv",
    "outputs/governor_bootstrap_summary.csv",
    "outputs/governor_bootstrap_histogram.csv",
    "outputs/nec_2026_gwangju_jeonnam_unit_counts.csv",
    "outputs/nec_2026_gwangju_jeonnam_units.csv",
    "outputs/nec_2026_gwangju_jeonnam_unit_summary.json",
    "outputs/nec_2026_reported_duplicate_cases.csv",
    "outputs/nec_2026_reported_duplicate_pairs.csv",
    "outputs/nec_2026_fetch_manifest.json",
    "outputs/songdo_probability_summary.csv",
    "outputs/songdo_official_rows.csv",
    "outputs/probability_core.csv",
    "outputs/probability_exact_collision.csv",
    "outputs/probability_designated_pairs.csv",
    "outputs/early_day_assembly_summary.csv",
    "outputs/public_discussion_claims_audit.csv",
    "outputs/public_discussion_claims_audit.json",
    "outputs/core_claims_verification.csv",
    "outputs/core_claims_verification.json",
    "outputs/statistical_robustness_audit.csv",
    "outputs/statistical_robustness_audit.json",
    "outputs/video_source_exclusion_audit.csv",
    "outputs/video_source_exclusion_audit.json",
    "outputs/source_provenance_audit.csv",
    "outputs/source_provenance_audit.json",
    "outputs/claim_boundary_audit.csv",
    "outputs/claim_boundary_audit.json",
    "outputs/objection_coverage_audit.csv",
    "outputs/objection_coverage_audit.json",
    "outputs/pre_submission_audit.csv",
    "outputs/pre_submission_audit.json",
    "outputs/submission_index_audit.csv",
    "outputs/submission_index_audit.json",
    "outputs/submission_integrity_report.md",
    "outputs/submission_integrity_report.json",
    "outputs/checksums_sha256.csv",
    "dist/election_duplicate_ieie_submission.zip",
    "dist/election_duplicate_ieie_submission.zip.sha256",
    "dist/election_duplicate_ieie_submission_manifest.json",
]

FORBIDDEN_PATTERNS = [
    "/tmp/" + "election-duplicates",
    "유" + "튜브",
    "You" + "Tube",
    "you" + "tube",
    "자" + "막",
    "HlLEt" + "L4OIOk",
    "AWcoe" + "47sihg",
    "DDCTr" + "WfCBqc",
    "l_kl4" + "hlOfBU",
    "xgI9" + "h3_5ZKw",
    "부정선거 " + "확정",
    "조작 " + "확정",
    "범죄 " + "확정",
    "무조건 " + "부정",
    "반박" + "불가",
    "아무도 " + "반박",
    "부정행위 " + "확정",
    "원인이 " + "확정",
]


def read_text_files() -> list[Path]:
    return [
        path for path in ROOT.rglob("*")
        if (
            path.is_file()
            and path != Path(__file__).resolve()
            and path.suffix.lower() in {".md", ".py", ".txt", ".csv", ".json", ".tex", ".cls"}
        )
    ]


def assert_required_files() -> None:
    required = REQUIRED_FILES
    if os.environ.get("LOCAL_CI_VALIDATION_IN_PROGRESS") == "true":
        required = [
            rel for rel in REQUIRED_FILES
            if rel not in {
                "outputs/local_ci_validation_report.md",
                "outputs/local_ci_validation_report.json",
            }
        ]
    missing = [rel for rel in required if not (ROOT / rel).exists()]
    if missing:
        raise AssertionError(f"Missing required files: {', '.join(missing)}")


def assert_forbidden_patterns() -> None:
    hits: list[str] = []
    for path in read_text_files():
        text = path.read_text(encoding="utf-8", errors="ignore")
        for pattern in FORBIDDEN_PATTERNS:
            if pattern in text:
                hits.append(f"{path.relative_to(ROOT)}: {pattern}")
    if hits:
        raise AssertionError("Forbidden patterns found:\n" + "\n".join(hits))


def assert_duplicate_summary() -> None:
    summary_path = ROOT / "outputs" / "dataset_counts.csv"
    rows = list(csv.DictReader(summary_path.open(encoding="utf-8")))
    total = sum(int(row["rows"]) for row in rows)
    if total != 81_701:
        raise AssertionError(f"Expected 81,701 parsed rows, got {total}")


def assert_governor_summary() -> None:
    path = ROOT / "outputs" / "governor_actual_top2_summary.csv"
    row = next(csv.DictReader(path.open(encoding="utf-8")))
    expected_ints = {
        "governor_contests": 51,
        "comparison_pairs": 1_514_172,
        "collision_pairs": 15,
        "duplicate_groups": 15,
        "max_duplicate_groups_in_contest": 3,
    }
    for key, expected in expected_ints.items():
        actual = int(float(row[key]))
        if actual != expected:
            raise AssertionError(f"{key}: expected {expected}, got {actual}")

    p5 = float(row["p_at_least_5"])
    if not math.isclose(p5, 0.0011484064248148407, rel_tol=0, abs_tol=1e-15):
        raise AssertionError(f"p_at_least_5 mismatch: {p5}")


def assert_probability_core() -> None:
    path = ROOT / "outputs" / "probability_core.csv"
    rows = list(csv.DictReader(path.open(encoding="utf-8")))
    p_by_threshold = {int(row["threshold"]): float(row["probability"]) for row in rows}
    expected = {
        3: 0.04226077201454281,
        4: 0.007734837111887716,
        5: 0.0011484064248148407,
        6: 0.00014322422035484283,
    }
    for threshold, value in expected.items():
        actual = p_by_threshold.get(threshold)
        if actual is None or not math.isclose(actual, value, rel_tol=0, abs_tol=1e-15):
            raise AssertionError(f"probability threshold {threshold}: expected {value}, got {actual}")

    designated_rows = list(csv.DictReader((ROOT / "outputs" / "probability_designated_pairs.csv").open(encoding="utf-8")))
    designated = {row["case"]: row for row in designated_rows}
    row5 = designated.get("gwangju_jeonnam_5_pre_designated_pairs")
    if row5 is None:
        raise AssertionError("Missing designated five-pair probability row")
    if int(row5["designated_pairs"]) != 5:
        raise AssertionError(f"Expected five designated pairs, got {row5['designated_pairs']}")
    if not math.isclose(float(row5["probability"]), 9.540700009422666e-26, rel_tol=0, abs_tol=1e-38):
        raise AssertionError(f"Designated five-pair probability mismatch: {row5['probability']}")


def assert_bootstrap_summary() -> None:
    path = ROOT / "outputs" / "governor_bootstrap_summary.csv"
    rows = list(csv.DictReader(path.open(encoding="utf-8")))
    if len(rows) != 3:
        raise AssertionError(f"Expected 3 bootstrap summary rows, got {len(rows)}")
    by_threshold = {int(row["threshold"]): row for row in rows}
    row5 = by_threshold.get(5)
    if row5 is None:
        raise AssertionError("Missing bootstrap threshold 5 row")
    if int(row5["sample_size"]) != 393 or int(row5["trials"]) != 200_000:
        raise AssertionError(f"Unexpected bootstrap design: {row5}")
    if int(row5["exceedances"]) != 0 or float(row5["probability"]) != 0.0:
        raise AssertionError(f"Expected zero bootstrap exceedances for threshold 5, got {row5}")
    if not math.isclose(float(row5["plus_one_probability"]), 1 / 200_001, rel_tol=0, abs_tol=1e-15):
        raise AssertionError(f"Unexpected plus-one bootstrap estimate: {row5}")
    if not math.isclose(float(row5["rule_of_three_upper_95"]), 3 / 200_000, rel_tol=0, abs_tol=1e-15):
        raise AssertionError(f"Unexpected bootstrap 95% upper bound: {row5}")


def assert_nec_2026_unit_count() -> None:
    summary_path = ROOT / "outputs" / "nec_2026_gwangju_jeonnam_unit_summary.json"
    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    if summary.get("towns") != 27:
        raise AssertionError(f"Expected 27 Gwangju+Jeonnam towns, got {summary.get('towns')}")
    if summary.get("in_district_early_units") != 393:
        raise AssertionError(
            "Expected 393 Gwangju+Jeonnam in-district early-vote units, "
            f"got {summary.get('in_district_early_units')}"
        )

    count_rows = list(csv.DictReader((ROOT / "outputs" / "nec_2026_gwangju_jeonnam_unit_counts.csv").open(encoding="utf-8")))
    by_city: dict[str, int] = {}
    for row in count_rows:
        by_city[row["city"]] = by_city.get(row["city"], 0) + int(row["in_district_early_units"])
    if by_city.get("광주광역시") != 96 or by_city.get("전라남도") != 297:
        raise AssertionError(f"Unexpected regional unit counts: {by_city}")

    unit_rows = list(csv.DictReader((ROOT / "outputs" / "nec_2026_gwangju_jeonnam_units.csv").open(encoding="utf-8")))
    if len(unit_rows) != 393:
        raise AssertionError(f"Expected 393 unit rows, got {len(unit_rows)}")


def assert_nec_2026_cases() -> None:
    path = ROOT / "outputs" / "nec_2026_reported_duplicate_cases.csv"
    rows = list(csv.DictReader(path.open(encoding="utf-8")))
    if len(rows) != 12:
        raise AssertionError(f"Expected 12 NEC 2026 case rows, got {len(rows)}")
    required = {
        ("인천광역시", "연수구", "송도1동", "박찬대", "3030", "유정복", "1440"),
        ("인천광역시", "연수구", "송도2동", "박찬대", "3030", "유정복", "1440"),
        ("광주광역시", "광산구", "송정1동", "민형배", "1401", "이정현", "120"),
        ("전라남도", "고흥군", "금산면", "민형배", "1401", "이정현", "120"),
    }
    actual = {
        (
            row["city"],
            row["town"],
            row["unit"],
            row["candidate_1"],
            row["candidate_1_votes"],
            row["candidate_2"],
            row["candidate_2_votes"],
        )
        for row in rows
    }
    missing = sorted(required - actual)
    if missing:
        raise AssertionError(f"Missing required NEC 2026 cases: {missing}")

    pair_rows = list(csv.DictReader((ROOT / "outputs" / "nec_2026_reported_duplicate_pairs.csv").open(encoding="utf-8")))
    if len(pair_rows) != 6:
        raise AssertionError(f"Expected 6 NEC 2026 duplicate pairs, got {len(pair_rows)}")


def assert_songdo_probability() -> None:
    rows = list(csv.DictReader((ROOT / "outputs" / "songdo_probability_summary.csv").open(encoding="utf-8")))
    by_case = {row["case"]: row for row in rows}
    any_pair = by_case.get("yeonsu_any_pair")
    designated = by_case.get("songdo1_songdo2_designated_pair")
    if any_pair is None or designated is None:
        raise AssertionError(f"Missing Songdo probability rows: {sorted(by_case)}")
    if int(any_pair["n_units"]) != 15 or int(any_pair["comparison_pairs"]) != 105:
        raise AssertionError(f"Unexpected Yeonsu design: {any_pair}")
    if not math.isclose(float(any_pair["probability"]), 0.0010396316588441312, rel_tol=0, abs_tol=1e-15):
        raise AssertionError(f"Unexpected Yeonsu any-pair probability: {any_pair}")
    if not math.isclose(float(designated["probability"]), 9.906404292246851e-06, rel_tol=0, abs_tol=1e-18):
        raise AssertionError(f"Unexpected Songdo designated-pair probability: {designated}")

    detail = list(csv.DictReader((ROOT / "outputs" / "songdo_official_rows.csv").open(encoding="utf-8")))
    if len(detail) != 2:
        raise AssertionError(f"Expected 2 Songdo detail rows, got {len(detail)}")
    signatures = {
        (
            row["unit"],
            row["candidate_1_votes"],
            row["candidate_2_votes"],
            row["electors"],
            row["turnout"],
        )
        for row in detail
    }
    expected = {
        ("송도1동", "3030", "1440", "4548", "4546"),
        ("송도2동", "3030", "1440", "4540", "4539"),
    }
    if signatures != expected:
        raise AssertionError(f"Unexpected Songdo official rows: {signatures}")


def assert_manifest_json() -> None:
    path = ROOT / "outputs" / "manifest.json"
    if path.exists():
        json.loads(path.read_text(encoding="utf-8"))


def assert_core_claims_verification() -> None:
    path = ROOT / "outputs" / "core_claims_verification.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("status") != "pass":
        raise AssertionError(f"Core claim verification status is not pass: {data.get('status')}")
    if int(data.get("check_count", 0)) < 40:
        raise AssertionError(f"Core claim verification has too few checks: {data.get('check_count')}")
    checks = data.get("checks")
    if not isinstance(checks, list) or len(checks) != data.get("check_count"):
        raise AssertionError("Core claim verification checks list does not match check_count")
    required_claims = {
        "historical parsed rows",
        "historical governor contests",
        "historical maximum duplicate groups in one contest",
        "Poisson probability threshold 5",
        "exact collision probability threshold 5",
        "pre-designated five-pair conditional probability",
        "bootstrap threshold 5 exceedances",
        "NEC 2026 Gwangju-Jeonnam in-district early units summary",
        "NEC 2026 event rows",
        "NEC 2026 duplicate pairs",
        "NEC 2026 Gwangju-Jeonnam Min-Lee duplicate pairs",
        "Songdo designated-pair probability percent",
        "2020 Democratic early higher count",
        "2024 Democratic early higher count",
    }
    actual_claims = {row.get("claim") for row in checks}
    missing = sorted(required_claims - actual_claims)
    if missing:
        raise AssertionError(f"Core claim verification missing claims: {', '.join(missing)}")

    csv_path = ROOT / "outputs" / "core_claims_verification.csv"
    csv_rows = list(csv.DictReader(csv_path.open(encoding="utf-8")))
    if len(csv_rows) != data.get("check_count"):
        raise AssertionError(
            "Core claim verification CSV row count does not match check_count: "
            f"{len(csv_rows)} != {data.get('check_count')}"
        )
    if any(row.get("status") != "pass" for row in csv_rows):
        raise AssertionError("Core claim verification CSV contains non-pass status")
    csv_claims = {row.get("claim") for row in csv_rows}
    missing_csv_claims = sorted(actual_claims - csv_claims)
    if missing_csv_claims:
        raise AssertionError(f"Core claim verification CSV missing claims: {', '.join(missing_csv_claims)}")


def assert_pre_submission_audit() -> None:
    path = ROOT / "outputs" / "pre_submission_audit.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("status") != "pass":
        raise AssertionError(f"Pre-submission audit status is not pass: {data.get('status')}")
    if int(data.get("check_count", 0)) < 6:
        raise AssertionError(f"Pre-submission audit has too few checks: {data.get('check_count')}")
    required = {
        "final checklist items complete",
        "forbidden patterns absent",
        "privacy and credential scan",
        "core claims verification",
        "statistical robustness audit",
        "video source exclusion audit",
        "source provenance audit",
        "claim-boundary audit",
        "objection coverage audit",
        "exact collision probability output",
        "manuscript core number consistency",
        "English PDF translation coverage",
        "English source translation scan",
        "English PDF evidence-matrix reference",
        "submission source files present",
        "2026 data availability boundary",
        "media source role boundary",
    }
    checks = data.get("checks")
    if not isinstance(checks, list):
        raise AssertionError("Pre-submission audit checks are missing")
    actual = {row.get("check") for row in checks}
    missing = sorted(required - actual)
    if missing:
        raise AssertionError(f"Pre-submission audit missing checks: {', '.join(missing)}")
    if any(row.get("status") != "pass" for row in checks):
        raise AssertionError("Pre-submission audit contains non-pass status")

    csv_rows = list(csv.DictReader((ROOT / "outputs" / "pre_submission_audit.csv").open(encoding="utf-8")))
    if len(csv_rows) != data.get("check_count"):
        raise AssertionError("Pre-submission audit CSV row count does not match check_count")
    if any(row.get("status") != "pass" for row in csv_rows):
        raise AssertionError("Pre-submission audit CSV contains non-pass status")


def assert_source_provenance_audit() -> None:
    path = ROOT / "outputs" / "source_provenance_audit.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("status") != "pass":
        raise AssertionError(f"Source provenance audit status is not pass: {data.get('status')}")
    if int(data.get("url_count", 0)) <= 0:
        raise AssertionError("Source provenance audit did not find source URLs")
    if data.get("failures"):
        raise AssertionError(f"Source provenance audit contains failures: {data.get('failures')}")

    rows = list(csv.DictReader((ROOT / "outputs" / "source_provenance_audit.csv").open(encoding="utf-8")))
    if len(rows) != data.get("url_count"):
        raise AssertionError("Source provenance audit CSV row count does not match url_count")
    if any(row.get("status") != "pass" for row in rows):
        raise AssertionError("Source provenance audit CSV contains non-pass status")


def assert_video_source_exclusion_audit() -> None:
    path = ROOT / "outputs" / "video_source_exclusion_audit.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("status") != "pass":
        raise AssertionError(f"Video source exclusion audit status is not pass: {data.get('status')}")
    if int(data.get("check_count", 0)) != 25:
        raise AssertionError(f"Video source exclusion audit check count mismatch: {data.get('check_count')}")
    if data.get("failures"):
        raise AssertionError(f"Video source exclusion audit contains failures: {data.get('failures')}")

    rows = list(csv.DictReader((ROOT / "outputs" / "video_source_exclusion_audit.csv").open(encoding="utf-8")))
    if len(rows) != data.get("check_count"):
        raise AssertionError("Video source exclusion audit CSV row count does not match check_count")
    if any(row.get("status") != "pass" for row in rows):
        raise AssertionError("Video source exclusion audit CSV contains non-pass status")


def assert_statistical_robustness_audit() -> None:
    path = ROOT / "outputs" / "statistical_robustness_audit.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("status") != "pass":
        raise AssertionError(f"Statistical robustness audit status is not pass: {data.get('status')}")
    if int(data.get("check_count", 0)) != 11:
        raise AssertionError(f"Statistical robustness audit check count mismatch: {data.get('check_count')}")
    checks = data.get("checks")
    if not isinstance(checks, list) or len(checks) != data.get("check_count"):
        raise AssertionError("Statistical robustness audit checks list does not match check_count")
    required = {
        "historical empirical upper bound",
        "Poisson baseline probability",
        "exact collision probability",
        "Poisson and exact agreement",
        "pre-designated five-pair conditional probability",
        "nonparametric resampling threshold 5",
        "rule-of-three upper bound",
        "effective-pair-space sensitivity",
        "K sensitivity monotonicity",
        "counting-unit N sensitivity",
        "N sensitivity upper range",
    }
    actual = {row.get("check") for row in checks}
    missing = sorted(required - actual)
    if missing:
        raise AssertionError(f"Statistical robustness audit missing checks: {', '.join(missing)}")
    if any(row.get("status") != "pass" for row in checks):
        raise AssertionError("Statistical robustness audit contains non-pass status")

    rows = list(csv.DictReader((ROOT / "outputs" / "statistical_robustness_audit.csv").open(encoding="utf-8")))
    if len(rows) != data.get("check_count"):
        raise AssertionError("Statistical robustness audit CSV row count does not match check_count")
    if any(row.get("status") != "pass" for row in rows):
        raise AssertionError("Statistical robustness audit CSV contains non-pass status")


def assert_public_discussion_claims_audit() -> None:
    path = ROOT / "outputs" / "public_discussion_claims_audit.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("status") != "pass":
        raise AssertionError(f"Public-discussion claim audit status is not pass: {data.get('status')}")
    if data.get("row_count") != 2:
        raise AssertionError("Public-discussion claim audit does not record two official rows")
    pair = data.get("confirmed_pair", {})
    if pair.get("lee_jae_myung") != 131 or pair.get("yoon_suk_yeol") != 618:
        raise AssertionError("Public-discussion claim audit records unexpected candidate values")

    rows = list(csv.DictReader((ROOT / "outputs" / "public_discussion_claims_audit.csv").open(encoding="utf-8")))
    if len(rows) != 2:
        raise AssertionError("Public-discussion claim audit CSV row count mismatch")
    stations = {row.get("polling_station") for row in rows}
    if stations != {"비산1동제3투", "비산1동제4투"}:
        raise AssertionError(f"Public-discussion claim audit has unexpected polling stations: {stations}")


def assert_claim_boundary_audit() -> None:
    path = ROOT / "outputs" / "claim_boundary_audit.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("status") != "pass":
        raise AssertionError(f"Claim-boundary audit status is not pass: {data.get('status')}")
    if int(data.get("check_count", 0)) < 22:
        raise AssertionError(f"Claim-boundary audit has too few checks: {data.get('check_count')}")
    checks = data.get("checks")
    if not isinstance(checks, list) or len(checks) != data.get("check_count"):
        raise AssertionError("Claim-boundary audit checks list does not match check_count")
    required = {
        "overclaim phrase absence",
        "Korean manuscript boundary markers",
        "English manuscript boundary markers",
        "Korean raw-record requirements",
        "English raw-record requirements",
        "Korean post-disclosure decision levels",
        "English post-disclosure decision levels",
        "Korean PDF post-disclosure decision levels",
        "English PDF post-disclosure decision levels",
        "Korean PDF claim-boundary rendering",
        "English PDF claim-boundary rendering",
    }
    actual = {row.get("check") for row in checks}
    missing = sorted(required - actual)
    if missing:
        raise AssertionError(f"Claim-boundary audit missing checks: {', '.join(missing)}")
    if any(row.get("status") != "pass" for row in checks):
        raise AssertionError("Claim-boundary audit contains non-pass status")

    rows = list(csv.DictReader((ROOT / "outputs" / "claim_boundary_audit.csv").open(encoding="utf-8")))
    if len(rows) != data.get("check_count"):
        raise AssertionError("Claim-boundary audit CSV row count does not match check_count")
    if any(row.get("status") != "pass" for row in rows):
        raise AssertionError("Claim-boundary audit CSV contains non-pass status")


def assert_objection_coverage_audit() -> None:
    path = ROOT / "outputs" / "objection_coverage_audit.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("status") != "pass":
        raise AssertionError(f"Objection coverage audit status is not pass: {data.get('status')}")
    if int(data.get("check_count", 0)) < 26:
        raise AssertionError(f"Objection coverage audit has too few checks: {data.get('check_count')}")
    checks = data.get("checks")
    if not isinstance(checks, list) or len(checks) != data.get("check_count"):
        raise AssertionError("Objection coverage audit checks list does not match check_count")
    required = {
        "many units can produce one duplicate",
        "2014 inclusion weakens but does not remove result",
        "three historical pairs versus five observed pairs",
        "post-search and multiple-comparison objection",
        "unit heterogeneity and model dependence",
        "self-selection objection for early voting",
        "rare events can occur objection",
        "official integrated file limitation",
        "benign alternatives matrix",
        "reviewer response memo coverage",
        "post-disclosure reviewer decision tree",
        "chain-of-custody raw-record requirement",
        "Korean PDF objection controls render",
        "English PDF objection controls render",
    }
    actual = {row.get("objection") for row in checks}
    missing = sorted(required - actual)
    if missing:
        raise AssertionError(f"Objection coverage audit missing objections: {', '.join(missing)}")
    if any(row.get("status") != "pass" for row in checks):
        raise AssertionError("Objection coverage audit contains non-pass status")

    rows = list(csv.DictReader((ROOT / "outputs" / "objection_coverage_audit.csv").open(encoding="utf-8")))
    if len(rows) != data.get("check_count"):
        raise AssertionError("Objection coverage audit CSV row count does not match check_count")
    if any(row.get("status") != "pass" for row in rows):
        raise AssertionError("Objection coverage audit CSV contains non-pass status")


def assert_submission_integrity_report() -> None:
    path = ROOT / "outputs" / "submission_integrity_report.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("status") != "pass":
        raise AssertionError(f"Submission integrity report status is not pass: {data.get('status')}")
    if data.get("core_claims_check_count") != 47:
        raise AssertionError("Submission integrity report does not record 47 core checks")
    if data.get("source_provenance_status") != "pass":
        raise AssertionError("Submission integrity report does not record passing source provenance audit")
    if int(data.get("source_provenance_url_count", 0)) <= 0:
        raise AssertionError("Submission integrity report does not record source URLs")
    if data.get("statistical_robustness_audit_status") != "pass":
        raise AssertionError("Submission integrity report does not record passing statistical robustness audit")
    if data.get("statistical_robustness_audit_check_count") != 11:
        raise AssertionError("Submission integrity report does not record 11 statistical robustness checks")
    if data.get("video_source_exclusion_status") != "pass":
        raise AssertionError("Submission integrity report does not record passing video source exclusion audit")
    if data.get("video_source_exclusion_check_count") != 25:
        raise AssertionError("Submission integrity report does not record 25 video source exclusion file checks")
    if data.get("public_discussion_claims_audit_status") != "pass":
        raise AssertionError("Submission integrity report does not record passing public-discussion claim audit")
    if data.get("public_discussion_claims_audit_row_count") != 2:
        raise AssertionError("Submission integrity report does not record two public-discussion claim rows")
    if data.get("claim_boundary_audit_status") != "pass":
        raise AssertionError("Submission integrity report does not record passing claim-boundary audit")
    if data.get("claim_boundary_audit_check_count") != 22:
        raise AssertionError("Submission integrity report does not record 22 claim-boundary checks")
    if data.get("objection_coverage_audit_status") != "pass":
        raise AssertionError("Submission integrity report does not record passing objection coverage audit")
    if data.get("objection_coverage_audit_check_count") != 28:
        raise AssertionError("Submission integrity report does not record 28 objection coverage checks")
    if data.get("pre_submission_audit_check_count") != 17:
        raise AssertionError("Submission integrity report does not record 17 audit checks")
    if data.get("submission_index_audit_check_count") != 132:
        raise AssertionError("Submission integrity report does not record 132 submission-index checks")

    english_pdf = data.get("english_pdf", {})
    if english_pdf.get("korean_character_count") != 0:
        raise AssertionError("Submission integrity report found Korean characters in English PDF")
    if not english_pdf.get("references_english_evidence_matrix"):
        raise AssertionError("Submission integrity report missing English evidence-matrix reference")
    if english_pdf.get("references_korean_evidence_matrix"):
        raise AssertionError("Submission integrity report found Korean evidence-matrix reference")

    key_claims = data.get("key_claims", {})
    required_claims = {
        "historical_rows": 81701,
        "historical_governor_contests": 51,
        "gwangju_jeonnam_units_n": 393,
        "nec_2026_event_rows": 12,
        "nec_2026_duplicate_pairs": 6,
    }
    for key, expected in required_claims.items():
        if key_claims.get(key) != expected:
            raise AssertionError(f"Submission integrity report mismatch for {key}: {key_claims.get(key)}")

    md_text = (ROOT / "outputs" / "submission_integrity_report.md").read_text(encoding="utf-8")
    for phrase in ["Submission Integrity Report", "Core-claims verification", "English PDF"]:
        if phrase not in md_text:
            raise AssertionError(f"Submission integrity markdown missing phrase: {phrase}")


def assert_local_ci_validation_report() -> None:
    if os.environ.get("LOCAL_CI_VALIDATION_IN_PROGRESS") == "true":
        return

    path = ROOT / "outputs" / "local_ci_validation_report.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("status") != "pass":
        raise AssertionError(f"Local CI validation report status is not pass: {data.get('status')}")
    validate = data.get("validate_package", {})
    if not validate.get("passed") or validate.get("returncode") != 0:
        raise AssertionError("Local CI validation report did not pass validate_package.py")
    zip_reproduction = data.get("zip_reproduction_audit", {})
    if not zip_reproduction.get("passed") or zip_reproduction.get("returncode") != 0:
        raise AssertionError("Local CI validation report did not pass zip_reproduction_audit.py")
    sidecar = data.get("zip_sidecar", {})
    for key in ["manifest_sha256_matches", "manifest_bytes_matches", "sha256_sidecar_matches", "passed"]:
        if not sidecar.get(key):
            raise AssertionError(f"Local CI validation report sidecar check failed: {key}")

    md_text = (ROOT / "outputs" / "local_ci_validation_report.md").read_text(encoding="utf-8")
    for phrase in ["Local CI Validation Report", "ZIP SHA256", "validate_package.py Output Tail", "zip_reproduction_audit.py Output Tail"]:
        if phrase not in md_text:
            raise AssertionError(f"Local CI markdown missing phrase: {phrase}")


def assert_checksums() -> None:
    path = ROOT / "outputs" / "checksums_sha256.csv"
    rows = list(csv.DictReader(path.open(encoding="utf-8")))
    by_path = {row["path"]: row for row in rows}
    required = [
        "paper_statistical_implausibility_ko.md",
        "paper_statistical_implausibility_en.md",
        "SUBMISSION_INDEX_ko.md",
        "SUBMISSION_INDEX_en.md",
        "PUBLIC_DISCUSSION_CLAIMS_ko.md",
        "PUBLIC_DISCUSSION_CLAIMS_en.md",
        "cover_letter_ko.md",
        "cover_letter_en.md",
        "submission_memo_ko.md",
        "submission_memo_en.md",
        "reviewer_response_ko.md",
        "reviewer_response_en.md",
        "evidence_matrix_ko.md",
        "evidence_matrix_en.md",
        "DATA_DICTIONARY_ko.md",
        "DATA_DICTIONARY_en.md",
        "REVIEWER_QUICKSTART_ko.md",
        "REVIEWER_QUICKSTART_en.md",
        "REPRODUCIBILITY_CHECKLIST_ko.md",
        "REPRODUCIBILITY_CHECKLIST_en.md",
        "STATISTICAL_CALCULATION_NOTE_ko.md",
        "STATISTICAL_CALCULATION_NOTE_en.md",
        "data_availability_2026_ko.md",
        "data_availability_2026_en.md",
        "AUDIT_PROTOCOL_ko.md",
        "AUDIT_PROTOCOL_en.md",
        "ALTERNATIVE_EXPLANATIONS_MATRIX_ko.md",
        "ALTERNATIVE_EXPLANATIONS_MATRIX_en.md",
        "LOOK_ELSEWHERE_ROBUSTNESS_ko.md",
        "LOOK_ELSEWHERE_ROBUSTNESS_en.md",
        "FINAL_SUBMISSION_CHECKLIST_ko.md",
        "FINAL_SUBMISSION_CHECKLIST_en.md",
        "latex/ieie/main.pdf",
        "latex/en/main_en.pdf",
        "scripts/bootstrap_governor_duplicates.py",
        "scripts/verify_public_discussion_claims.py",
        "scripts/verify_core_claims.py",
        "scripts/statistical_robustness_audit.py",
        "scripts/video_source_exclusion_audit.py",
        "scripts/zip_reproduction_audit.py",
        "outputs/governor_bootstrap_summary.csv",
        "outputs/nec_2026_reported_duplicate_cases.csv",
        "outputs/core_claims_verification.csv",
        "outputs/core_claims_verification.json",
        "outputs/statistical_robustness_audit.csv",
        "outputs/statistical_robustness_audit.json",
        "outputs/public_discussion_claims_audit.csv",
        "outputs/public_discussion_claims_audit.json",
        "outputs/video_source_exclusion_audit.csv",
        "outputs/video_source_exclusion_audit.json",
        "outputs/source_provenance_audit.csv",
        "outputs/source_provenance_audit.json",
        "outputs/claim_boundary_audit.csv",
        "outputs/claim_boundary_audit.json",
        "outputs/objection_coverage_audit.csv",
        "outputs/objection_coverage_audit.json",
        "outputs/pre_submission_audit.csv",
        "outputs/pre_submission_audit.json",
        "outputs/submission_integrity_report.md",
        "outputs/submission_integrity_report.json",
        "outputs/probability_core.csv",
        "outputs/probability_exact_collision.csv",
        "outputs/probability_designated_pairs.csv",
    ]
    missing = [rel for rel in required if rel not in by_path]
    if missing:
        raise AssertionError(f"Checksums missing required files: {', '.join(missing)}")
    for rel, row in by_path.items():
        digest = row["sha256"]
        if len(digest) != 64 or any(ch not in "0123456789abcdef" for ch in digest):
            raise AssertionError(f"Invalid sha256 for {rel}: {digest}")


def assert_artifact_freshness() -> None:
    """Guard against submitting a stale PDF, checksum file, or zip bundle."""
    if os.environ.get("GITHUB_ACTIONS") == "true":
        return

    ko_md = ROOT / "paper_statistical_implausibility_ko.md"
    ko_converter = ROOT / "latex" / "convert_to_ieie.py"
    ko_tex = ROOT / "latex" / "ieie" / "main.tex"
    ko_pdf = ROOT / "latex" / "ieie" / "main.pdf"
    en_tex = ROOT / "latex" / "en" / "main_en.tex"
    en_pdf = ROOT / "latex" / "en" / "main_en.pdf"
    checksums = ROOT / "outputs" / "checksums_sha256.csv"
    zip_path = ROOT / "dist" / "election_duplicate_ieie_submission.zip"

    if ko_tex.stat().st_mtime < max(ko_md.stat().st_mtime, ko_converter.stat().st_mtime):
        raise AssertionError("main.tex is older than the Markdown source or converter script")
    if ko_pdf.stat().st_mtime < ko_tex.stat().st_mtime:
        raise AssertionError("main.pdf is older than main.tex")
    if en_pdf.stat().st_mtime < en_tex.stat().st_mtime:
        raise AssertionError("main_en.pdf is older than main_en.tex")

    package_sources = [ROOT / rel for rel in REQUIRED_FILES if not rel.startswith("dist/")]
    newest_source = max(path.stat().st_mtime for path in package_sources)
    if checksums.stat().st_mtime < newest_source:
        raise AssertionError("checksums_sha256.csv is older than a required package source")
    if zip_path.stat().st_mtime < checksums.stat().st_mtime:
        raise AssertionError("submission zip is older than checksums_sha256.csv")


def assert_english_pdf_translation_coverage() -> None:
    """Guard against stale or partially translated English PDF submissions."""
    try:
        import fitz  # type: ignore[import-not-found]
    except ImportError as exc:
        raise AssertionError("PyMuPDF is required to validate English PDF text coverage") from exc

    pdf_path = ROOT / "latex" / "en" / "main_en.pdf"
    pdf = fitz.open(pdf_path)
    text = "\n".join(page.get_text() for page in pdf)

    if pdf.page_count < 18:
        raise AssertionError(f"English PDF appears too short for the full translated manuscript: {pdf.page_count} pages")

    korean = re.findall(r"[가-힣]+", text)
    if korean:
        sample = ", ".join(korean[:10])
        raise AssertionError(f"English PDF contains Korean text fragments: {sample}")

    required_phrases = [
        "+3.90%p",
        "211",
        "0.000991%",
        "Appendix B",
        "Rule of three",
        "Law of large numbers",
        "Reproduction Outputs",
        "candidate allocation",
        "reviewed ballots",
        "core verification material",
    ]
    missing = [phrase for phrase in required_phrases if phrase not in text]
    if "evidence_matrix_en.md" not in text and "evidence matrix en.md" not in text:
        missing.append("evidence_matrix_en.md")
    if missing:
        raise AssertionError(f"English PDF missing expected translated content: {', '.join(missing)}")

    stale_phrases = [
        "2016 National Assembly 229 118 111",
        "about 0.35",
        "evidence_matrix_ko.md",
        "evidence matrix ko.md",
    ]
    stale = [phrase for phrase in stale_phrases if phrase in text]
    if stale:
        raise AssertionError(f"English PDF contains stale pre-translation values: {', '.join(stale)}")


def assert_english_sources_have_no_korean() -> None:
    """Ensure English-facing manuscript files are fully translated."""
    english_sources = sorted(ROOT.glob("*_en.md")) + [ROOT / "latex" / "en" / "main_en.tex"]
    offenders: list[str] = []
    for path in english_sources:
        text = path.read_text(encoding="utf-8")
        fragments = re.findall(r"[가-힣]+", text)
        if fragments:
            rel = path.relative_to(ROOT)
            sample = ", ".join(fragments[:5])
            offenders.append(f"{rel}: {sample}")
    if offenders:
        raise AssertionError("English source files contain untranslated Korean text: " + "; ".join(offenders))


def assert_zip_package() -> None:
    zip_path = ROOT / "dist" / "election_duplicate_ieie_submission.zip"
    manifest_path = ROOT / "dist" / "election_duplicate_ieie_submission_manifest.json"
    sha_path = ROOT / "dist" / "election_duplicate_ieie_submission.zip.sha256"
    required = {
        "README.md",
        "paper_statistical_implausibility_ko.md",
        "paper_statistical_implausibility_en.md",
        "PUBLIC_DISCUSSION_CLAIMS_ko.md",
        "PUBLIC_DISCUSSION_CLAIMS_en.md",
        "cover_letter_ko.md",
        "cover_letter_en.md",
        "submission_memo_ko.md",
        "submission_memo_en.md",
        "reviewer_response_ko.md",
        "reviewer_response_en.md",
        "latex/ieie/main.tex",
        "latex/ieie/main.pdf",
        "latex/en/main_en.tex",
        "latex/en/main_en.pdf",
        "outputs/checksums_sha256.csv",
        "outputs/governor_bootstrap_summary.csv",
        "outputs/nec_2026_gwangju_jeonnam_unit_summary.json",
        "outputs/nec_2026_gwangju_jeonnam_units.csv",
        "outputs/nec_2026_reported_duplicate_cases.csv",
        "outputs/core_claims_verification.csv",
        "outputs/core_claims_verification.json",
        "outputs/statistical_robustness_audit.csv",
        "outputs/statistical_robustness_audit.json",
        "outputs/public_discussion_claims_audit.csv",
        "outputs/public_discussion_claims_audit.json",
        "outputs/video_source_exclusion_audit.csv",
        "outputs/video_source_exclusion_audit.json",
        "outputs/pre_submission_audit.csv",
        "outputs/pre_submission_audit.json",
        "outputs/submission_index_audit.csv",
        "outputs/submission_index_audit.json",
        "outputs/claim_boundary_audit.csv",
        "outputs/claim_boundary_audit.json",
        "outputs/objection_coverage_audit.csv",
        "outputs/objection_coverage_audit.json",
        "outputs/probability_exact_collision.csv",
        "evidence_matrix_ko.md",
        "evidence_matrix_en.md",
        "DATA_DICTIONARY_ko.md",
        "DATA_DICTIONARY_en.md",
        "REVIEWER_QUICKSTART_ko.md",
        "REVIEWER_QUICKSTART_en.md",
        "REPRODUCIBILITY_CHECKLIST_ko.md",
        "REPRODUCIBILITY_CHECKLIST_en.md",
        "STATISTICAL_CALCULATION_NOTE_ko.md",
        "STATISTICAL_CALCULATION_NOTE_en.md",
        "data_availability_2026_ko.md",
        "data_availability_2026_en.md",
        "AUDIT_PROTOCOL_ko.md",
        "AUDIT_PROTOCOL_en.md",
        "ALTERNATIVE_EXPLANATIONS_MATRIX_ko.md",
        "ALTERNATIVE_EXPLANATIONS_MATRIX_en.md",
        "LOOK_ELSEWHERE_ROBUSTNESS_ko.md",
        "LOOK_ELSEWHERE_ROBUSTNESS_en.md",
        "FINAL_SUBMISSION_CHECKLIST_ko.md",
        "FINAL_SUBMISSION_CHECKLIST_en.md",
        "scripts/pre_submission_audit.py",
        "scripts/verify_public_discussion_claims.py",
        "scripts/submission_index_audit.py",
        "scripts/video_source_exclusion_audit.py",
        "scripts/zip_reproduction_audit.py",
        "scripts/claim_boundary_audit.py",
        "scripts/objection_coverage_audit.py",
    }
    with ZipFile(zip_path) as zf:
        names = set(zf.namelist())
    missing = sorted(required - names)
    if missing:
        raise AssertionError(f"Zip missing required entries: {', '.join(missing)}")
    external_reports = {
        "outputs/local_ci_validation_report.md",
        "outputs/local_ci_validation_report.json",
        "outputs/zip_reproduction_audit.md",
        "outputs/zip_reproduction_audit.json",
    }
    embedded_external_reports = sorted(external_reports & names)
    if embedded_external_reports:
        raise AssertionError(
            "Zip contains external post-zip reports: "
            + ", ".join(embedded_external_reports)
        )
    forbidden_suffixes = (".aux", ".log", ".out", ".synctex.gz")
    bad = sorted(name for name in names if name.endswith(forbidden_suffixes))
    if bad:
        raise AssertionError(f"Zip contains LaTeX build byproducts: {', '.join(bad)}")

    checksum_rows = list(csv.DictReader((ROOT / "outputs" / "checksums_sha256.csv").open(encoding="utf-8")))
    missing_checksum_entries = sorted(row["path"] for row in checksum_rows if row["path"] not in names)
    if missing_checksum_entries:
        raise AssertionError(
            "Zip missing entries listed in checksums_sha256.csv: "
            + ", ".join(missing_checksum_entries[:20])
        )
    with ZipFile(zip_path) as zf:
        mismatches = []
        for row in checksum_rows:
            rel = row["path"]
            payload = zf.read(rel)
            digest = hashlib.sha256(payload).hexdigest()
            size = len(payload)
            if digest != row["sha256"] or size != int(row["bytes"]):
                mismatches.append(rel)
    if mismatches:
        raise AssertionError(
            "Zip entries do not match checksums_sha256.csv: "
            + ", ".join(mismatches[:20])
        )

    text_suffixes = {".md", ".py", ".txt", ".csv", ".json", ".tex", ".cls"}
    allowed_emails = {"junhokim0331@gmail.com"}
    email_pattern = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
    token_patterns = [
        re.compile(r"gh[pousr]_[A-Za-z0-9_]{20,}"),
        re.compile(r"github" + r"_pat_[A-Za-z0-9_]{20,}"),
    ]
    phone_pattern = re.compile(r"\b01[016789]-?\d{3,4}-?\d{4}\b")
    korean_rrn_pattern = re.compile(r"\b\d{6}-[1-4]\d{6}\b")
    zip_text_hits: list[str] = []
    with ZipFile(zip_path) as zf:
        for name in sorted(names):
            if Path(name).suffix.lower() not in text_suffixes:
                continue
            text = zf.read(name).decode("utf-8", errors="ignore")
            for pattern in FORBIDDEN_PATTERNS:
                if pattern in text:
                    zip_text_hits.append(f"{name}: forbidden pattern")
            for email in email_pattern.findall(text):
                if email not in allowed_emails:
                    zip_text_hits.append(f"{name}: unexpected email {email}")
            for pattern in token_patterns:
                if pattern.search(text):
                    zip_text_hits.append(f"{name}: credential token pattern")
            if phone_pattern.search(text):
                zip_text_hits.append(f"{name}: phone number pattern")
            if korean_rrn_pattern.search(text):
                zip_text_hits.append(f"{name}: Korean resident-number pattern")
    if zip_text_hits:
        raise AssertionError(
            "Zip text entries contain forbidden/privacy patterns: "
            + "; ".join(zip_text_hits[:20])
        )

    package_digest = hashlib.sha256(zip_path.read_bytes()).hexdigest()
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("package") != zip_path.name:
        raise AssertionError(f"Zip manifest package mismatch: {manifest.get('package')}")
    if manifest.get("sha256") != package_digest:
        raise AssertionError("Zip manifest sha256 does not match the actual zip")
    if int(manifest.get("bytes", -1)) != zip_path.stat().st_size:
        raise AssertionError("Zip manifest byte count does not match the actual zip")
    if int(manifest.get("file_count", -1)) != len(names):
        raise AssertionError("Zip manifest file count does not match the actual zip")
    expected_sha_line = f"{package_digest}  {zip_path.name}"
    actual_sha_line = sha_path.read_text(encoding="utf-8").strip()
    if actual_sha_line != expected_sha_line:
        raise AssertionError("Zip .sha256 sidecar does not match the actual zip")


def main() -> None:
    assert_required_files()
    assert_forbidden_patterns()
    assert_duplicate_summary()
    assert_governor_summary()
    assert_probability_core()
    assert_bootstrap_summary()
    assert_nec_2026_unit_count()
    assert_nec_2026_cases()
    assert_songdo_probability()
    assert_manifest_json()
    assert_core_claims_verification()
    assert_statistical_robustness_audit()
    assert_public_discussion_claims_audit()
    assert_video_source_exclusion_audit()
    assert_source_provenance_audit()
    assert_claim_boundary_audit()
    assert_objection_coverage_audit()
    assert_pre_submission_audit()
    assert_submission_integrity_report()
    assert_local_ci_validation_report()
    assert_checksums()
    assert_artifact_freshness()
    assert_english_pdf_translation_coverage()
    assert_english_sources_have_no_korean()
    assert_zip_package()
    print("Package validation passed.")


if __name__ == "__main__":
    main()
