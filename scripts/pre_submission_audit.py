#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs"


@dataclass
class AuditCheck:
    check: str
    expected: str
    actual: str
    status: str


def read_text(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8", errors="ignore")


def check(condition: bool, name: str, expected: str, actual: str) -> AuditCheck:
    return AuditCheck(
        check=name,
        expected=expected,
        actual=actual,
        status="pass" if condition else "fail",
    )


def text_files() -> list[Path]:
    suffixes = {".md", ".py", ".txt", ".csv", ".json", ".tex", ".cls"}
    skipped_parts = {".git", "data", "dist"}
    return [
        path
        for path in ROOT.rglob("*")
        if (
            path.is_file()
            and path.suffix.lower() in suffixes
            and not any(part in skipped_parts for part in path.relative_to(ROOT).parts)
        )
    ]


def forbidden_patterns_absent() -> AuditCheck:
    patterns = [
        "유" + "튜브",
        "You" + "Tube",
        "you" + "tube",
        "자" + "막",
        "반박" + "불가",
        "아무도 " + "반박",
        "부정선거 " + "확정",
        "조작 " + "확정",
        "범죄 " + "확정",
        "fraud " + "proven",
        "ir" + "refutable",
        "cannot be " + "refuted",
        "election fraud " + "occurred",
        "ghp" + "_",
        "github_pat" + "_",
        "gho" + "_",
    ]
    hits: list[str] = []
    for path in text_files():
        text = path.read_text(encoding="utf-8", errors="ignore")
        for pattern in patterns:
            if pattern in text:
                hits.append(f"{path.relative_to(ROOT)}:{pattern}")
    return check(not hits, "forbidden patterns absent", "0 hits", f"{len(hits)} hits")


def privacy_and_credential_scan() -> AuditCheck:
    allowed_emails = {"junhokim0331@gmail.com"}
    email_pattern = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
    token_patterns = [
        re.compile(r"gh[pousr]_[A-Za-z0-9_]{20,}"),
        re.compile(r"github" + r"_pat_[A-Za-z0-9_]{20,}"),
    ]
    phone_pattern = re.compile(r"\b01[016789]-?\d{3,4}-?\d{4}\b")
    korean_rrn_pattern = re.compile(r"\b\d{6}-[1-4]\d{6}\b")

    hits: list[str] = []
    for path in text_files():
        text = path.read_text(encoding="utf-8", errors="ignore")
        rel = path.relative_to(ROOT)
        for email in email_pattern.findall(text):
            if email not in allowed_emails:
                hits.append(f"{rel}:email:{email}")
        for pattern in token_patterns:
            if pattern.search(text):
                hits.append(f"{rel}:credential-token-pattern")
        if phone_pattern.search(text):
            hits.append(f"{rel}:phone-number-pattern")
        if korean_rrn_pattern.search(text):
            hits.append(f"{rel}:korean-rrn-pattern")

    return check(
        not hits,
        "privacy and credential scan",
        "only allowed author email; 0 credential, phone, or resident-number patterns",
        f"{len(hits)} hits",
    )


def checklist_items_complete() -> AuditCheck:
    checklist_paths = [
        "FINAL_SUBMISSION_CHECKLIST_ko.md",
        "FINAL_SUBMISSION_CHECKLIST_en.md",
    ]
    incomplete = []
    for path in checklist_paths:
        count = read_text(path).count("[ ]")
        if count:
            incomplete.append(f"{path}:{count}")
    return check(not incomplete, "final checklist items complete", "0 unchecked boxes", ", ".join(incomplete) or "0 unchecked boxes")


def core_claims_pass() -> AuditCheck:
    data = json.loads((OUT / "core_claims_verification.json").read_text(encoding="utf-8"))
    status = data.get("status")
    check_count = int(data.get("check_count", 0))
    return check(
        status == "pass" and check_count == 47,
        "core claims verification",
        "status pass, 47 checks",
        f"status {status}, {check_count} checks",
    )


def source_provenance_pass() -> AuditCheck:
    path = OUT / "source_provenance_audit.json"
    if not path.exists():
        return check(False, "source provenance audit", "status pass", "missing source_provenance_audit.json")
    data = json.loads(path.read_text(encoding="utf-8"))
    status = data.get("status")
    url_count = int(data.get("url_count", 0))
    failures = data.get("failures", [])
    return check(
        status == "pass" and url_count > 0 and not failures,
        "source provenance audit",
        "status pass with approved source domains only",
        f"status {status}, {url_count} URLs, {len(failures)} failures",
    )


def video_source_exclusion_pass() -> AuditCheck:
    path = OUT / "video_source_exclusion_audit.json"
    if not path.exists():
        return check(False, "video source exclusion audit", "status pass with 25 checked files", "missing video_source_exclusion_audit.json")
    data = json.loads(path.read_text(encoding="utf-8"))
    status = data.get("status")
    check_count = int(data.get("check_count", 0))
    failures = data.get("failures", [])
    return check(
        status == "pass" and check_count == 25 and not failures,
        "video source exclusion audit",
        "status pass with 25 checked files and 0 failures",
        f"status {status}, {check_count} files, {len(failures)} failures",
    )


def statistical_robustness_pass() -> AuditCheck:
    path = OUT / "statistical_robustness_audit.json"
    if not path.exists():
        return check(False, "statistical robustness audit", "status pass with 11 checks", "missing statistical_robustness_audit.json")
    data = json.loads(path.read_text(encoding="utf-8"))
    status = data.get("status")
    check_count = int(data.get("check_count", 0))
    return check(
        status == "pass" and check_count == 11,
        "statistical robustness audit",
        "status pass with 11 checks",
        f"status {status}, {check_count} checks",
    )


def claim_boundary_pass() -> AuditCheck:
    path = OUT / "claim_boundary_audit.json"
    if not path.exists():
        return check(False, "claim-boundary audit", "status pass with 22 checks", "missing claim_boundary_audit.json")
    data = json.loads(path.read_text(encoding="utf-8"))
    status = data.get("status")
    check_count = int(data.get("check_count", 0))
    return check(
        status == "pass" and check_count == 22,
        "claim-boundary audit",
        "status pass with 22 checks",
        f"status {status}, {check_count} checks",
    )


def objection_coverage_pass() -> AuditCheck:
    path = OUT / "objection_coverage_audit.json"
    if not path.exists():
        return check(False, "objection coverage audit", "status pass with 30 checks", "missing objection_coverage_audit.json")
    data = json.loads(path.read_text(encoding="utf-8"))
    status = data.get("status")
    check_count = int(data.get("check_count", 0))
    return check(
        status == "pass" and check_count == 30,
        "objection coverage audit",
        "status pass with 30 checks",
        f"status {status}, {check_count} checks",
    )


def english_pdf_has_no_korean() -> AuditCheck:
    try:
        import fitz  # type: ignore[import-not-found]
    except ImportError:
        return check(False, "English PDF Korean text scan", "PyMuPDF available, 0 Korean fragments", "PyMuPDF unavailable")

    pdf = fitz.open(ROOT / "latex" / "en" / "main_en.pdf")
    text = "\n".join(page.get_text() for page in pdf)
    korean_count = len(re.findall(r"[가-힣]", text))
    has_exact = "Exact Pair-Collision" in text and "0.0012190884" in text
    return check(
        korean_count == 0 and has_exact,
        "English PDF translation coverage",
        "0 Korean characters and exact-collision section present",
        f"{korean_count} Korean characters, exact section {'present' if has_exact else 'missing'}",
    )


def english_sources_have_no_korean() -> AuditCheck:
    english_sources = sorted(ROOT.glob("*_en.md")) + [ROOT / "latex" / "en" / "main_en.tex"]
    hits: list[str] = []
    for path in english_sources:
        text = path.read_text(encoding="utf-8", errors="ignore")
        korean = re.findall(r"[가-힣]+", text)
        if korean:
            hits.append(f"{path.relative_to(ROOT)}:{', '.join(korean[:5])}")
    return check(
        not hits,
        "English source translation scan",
        "0 Korean fragments in *_en.md and latex/en/main_en.tex",
        f"{len(hits)} files with Korean fragments",
    )


def english_pdf_references_english_evidence_matrix() -> AuditCheck:
    try:
        import fitz  # type: ignore[import-not-found]
    except ImportError:
        return check(False, "English PDF evidence-matrix reference", "PyMuPDF available and English matrix referenced", "PyMuPDF unavailable")

    pdf = fitz.open(ROOT / "latex" / "en" / "main_en.pdf")
    text = "\n".join(page.get_text() for page in pdf)
    en_present = "evidence_matrix_en.md" in text or "evidence matrix en.md" in text
    ko_present = "evidence_matrix_ko.md" in text or "evidence matrix ko.md" in text
    ok = en_present and not ko_present
    actual = (
        f"en reference {'present' if en_present else 'missing'}, "
        f"ko reference {'present' if ko_present else 'absent'}"
    )
    return check(
        ok,
        "English PDF evidence-matrix reference",
        "evidence_matrix_en.md present and evidence_matrix_ko.md absent",
        actual,
    )


def submission_sources_present() -> AuditCheck:
    required = {
        "paper_statistical_implausibility_ko.md",
        "paper_statistical_implausibility_en.md",
        "latex/ieie/main.pdf",
        "latex/en/main_en.pdf",
        "PUBLIC_DISCUSSION_CLAIMS_ko.md",
        "PUBLIC_DISCUSSION_CLAIMS_en.md",
        "outputs/public_discussion_claims_audit.json",
        "outputs/core_claims_verification.json",
        "FINAL_SUBMISSION_CHECKLIST_ko.md",
        "FINAL_SUBMISSION_CHECKLIST_en.md",
    }
    missing = sorted(rel for rel in required if not (ROOT / rel).exists())
    docs = {
        "DATA_DICTIONARY_ko.md": read_text("DATA_DICTIONARY_ko.md"),
        "DATA_DICTIONARY_en.md": read_text("DATA_DICTIONARY_en.md"),
        "FINAL_SUBMISSION_CHECKLIST_ko.md": read_text("FINAL_SUBMISSION_CHECKLIST_ko.md"),
        "FINAL_SUBMISSION_CHECKLIST_en.md": read_text("FINAL_SUBMISSION_CHECKLIST_en.md"),
    }
    stale_markers = [
        f"{path}: stale 23-file video audit count"
        for path, text in docs.items()
        if "23개 파일" in text or "23 checked files" in text or "23 manuscript-facing files" in text
    ]
    public_discussion_refs = [
        path
        for path, text in docs.items()
        if "public_discussion_claims_audit" in text or "공개 논의 보조 주장" in text
    ]
    failures = missing + stale_markers
    if len(public_discussion_refs) != len(docs):
        failures.append("public-discussion audit not referenced by all checklist/data-dictionary docs")
    return check(
        not failures,
        "submission source files present",
        "required source files present and documentation audit counts current",
        f"{len(failures)} failures",
    )


def data_availability_boundary_present() -> AuditCheck:
    required_by_file = {
        "data_availability_2026_ko.md": [
            "제3회부터 제8회까지",
            "제9회 전국동시지방선거 개표결과 통합 XLSX 파일은 확인되지 않았다",
            "공식 화면값은 통합 XLSX 파일 또는 개표상황표 원본과 동일한 층위의 원자료는 아니다",
            "피해야 할 표현",
        ],
        "data_availability_2026_en.md": [
            "3rd through 8th elections",
            "no integrated XLSX file for the 9th nationwide local-election vote-count result was identified",
            "official page values are not the same evidentiary layer as an integrated XLSX file or original counting statements",
            "Wording to avoid",
        ],
    }
    missing: list[str] = []
    for rel, needles in required_by_file.items():
        text = read_text(rel)
        for needle in needles:
            if needle not in text:
                missing.append(f"{rel}:{needle}")
    return check(
        not missing,
        "2026 data availability boundary",
        "Korean/English data-availability notes preserve official-file limitation and supported wording",
        f"{len(missing)} missing markers",
    )


def media_source_role_boundary_present() -> AuditCheck:
    required_by_file = {
        "README.md": [
            "media reports only to define the initially reported 2026 event rows before official-page rechecking",
            "2026년 사건행 정의를 위한 명시적 보도자료",
            "공식 선거자료",
            "선관위 선거통계시스템 HTML",
        ],
        "paper_statistical_implausibility_ko.md": [
            "분석의 출발점은 공개 보도",
            "HTML에서 직접 추출해 대조",
            "더 이상 보도 화면에만 의존하지 않는다",
            "전국 12곳은 보조적 맥락이지",
        ],
        "paper_statistical_implausibility_en.md": [
            "The starting point is the public report",
            "extracting them directly from the National Election Commission election-statistics system",
            "no longer depend only on a media screenshot",
            "The nationwide twelve cases are contextual",
        ],
    }
    missing: list[str] = []
    for rel, needles in required_by_file.items():
        text = read_text(rel)
        for needle in needles:
            if needle not in text:
                missing.append(f"{rel}:{needle}")

    try:
        import fitz  # type: ignore[import-not-found]
    except ImportError:
        missing.append("PDF media-source role boundary:PyMuPDF unavailable")
    else:
        pdf_sources = {
            "latex/ieie/main.pdf": "".join(
                page.get_text() for page in fitz.open(ROOT / "latex" / "ieie" / "main.pdf")
            ),
            "latex/en/main_en.pdf": "\n".join(
                page.get_text() for page in fitz.open(ROOT / "latex" / "en" / "main_en.pdf")
            ),
        }
        compact_pdf_sources = {
            rel: "".join(text.split()) for rel, text in pdf_sources.items()
        }
        pdf_required = {
            "latex/ieie/main.pdf": [
                "공식화면HTML",
                "12개사건행",
                "보도화면에만의존하지않는다",
                "전국12곳은보조적맥락",
                "확률산정대상이아니다",
            ],
            "latex/en/main_en.pdf": [
                "The twelve event rows",
                "election-statistics HTML pages",
                "no longer depend only on a media screenshot",
                "The nationwide twelve cases are contextual",
            ],
        }
        for rel, needles in pdf_required.items():
            text = pdf_sources[rel]
            compact = compact_pdf_sources[rel]
            for needle in needles:
                if needle not in text and "".join(needle.split()) not in compact:
                    missing.append(f"{rel}:{needle}")
    return check(
        not missing,
        "media source role boundary",
        "public reports are limited to event-definition/context while official pages and reproducible scripts support the analysis",
        f"{len(missing)} missing markers",
    )


def exact_collision_output_present() -> AuditCheck:
    rows = list(csv.DictReader((OUT / "probability_exact_collision.csv").open(encoding="utf-8")))
    by_threshold = {int(row["threshold"]): row for row in rows}
    row5 = by_threshold.get(5)
    actual = row5["exact_probability"] if row5 else "missing"
    return check(
        actual == "0.0012190883791786122",
        "exact collision probability output",
        "threshold 5 exact probability 0.0012190883791786122",
        f"threshold 5 exact probability {actual}",
    )


def manuscript_core_numbers_present() -> AuditCheck:
    try:
        import fitz  # type: ignore[import-not-found]
    except ImportError:
        return check(False, "manuscript core number consistency", "PyMuPDF available and core numbers present", "PyMuPDF unavailable")

    sources: dict[str, str] = {
        "paper_statistical_implausibility_ko.md": read_text("paper_statistical_implausibility_ko.md"),
        "paper_statistical_implausibility_en.md": read_text("paper_statistical_implausibility_en.md"),
    }
    for pdf_path in ["latex/ieie/main.pdf", "latex/en/main_en.pdf"]:
        pdf = fitz.open(ROOT / pdf_path)
        sources[pdf_path] = "\n".join(page.get_text() for page in pdf)

    required_by_source = {
        "paper_statistical_implausibility_ko.md": [
            "81,701",
            "1,514,172",
            "0.0011484064",
            "0.0012190884",
            "200,000",
            "0회",
            "393",
            "12개",
            "6개",
        ],
        "paper_statistical_implausibility_en.md": [
            "81,701",
            "1,514,172",
            "0.0011484064",
            "0.0012190884",
            "200,000",
            "zero",
            "393",
            "twelve",
            "six",
        ],
        "latex/ieie/main.pdf": [
            "81,701",
            "1,514,172",
            "0.0011484064",
            "0.0012190884",
            "200,000",
            "0회",
            "393",
            "12개",
            "6개",
        ],
        "latex/en/main_en.pdf": [
            "81,701",
            "1,514,172",
            "0.0011484064",
            "0.0012190884",
            "200,000",
            "zero",
            "393",
            "twelve",
            "six",
        ],
    }
    missing: list[str] = []
    for source, needles in required_by_source.items():
        text = sources[source]
        for needle in needles:
            if needle not in text:
                missing.append(f"{source}:{needle}")
    return check(
        not missing,
        "manuscript core number consistency",
        "core numbers present in Korean/English Markdown and PDFs",
        f"{len(missing)} missing markers",
    )


def audit_checks() -> list[AuditCheck]:
    return [
        checklist_items_complete(),
        forbidden_patterns_absent(),
        privacy_and_credential_scan(),
        core_claims_pass(),
        statistical_robustness_pass(),
        video_source_exclusion_pass(),
        source_provenance_pass(),
        claim_boundary_pass(),
        objection_coverage_pass(),
        exact_collision_output_present(),
        manuscript_core_numbers_present(),
        english_pdf_has_no_korean(),
        english_sources_have_no_korean(),
        english_pdf_references_english_evidence_matrix(),
        submission_sources_present(),
        data_availability_boundary_present(),
        media_source_role_boundary_present(),
    ]


def write_outputs(rows: list[AuditCheck]) -> None:
    OUT.mkdir(exist_ok=True)
    data = {
        "status": "pass" if all(row.status == "pass" for row in rows) else "fail",
        "check_count": len(rows),
        "scope": "pre-submission package readiness",
        "checks": [asdict(row) for row in rows],
    }
    (OUT / "pre_submission_audit.json").write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    with (OUT / "pre_submission_audit.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["check", "expected", "actual", "status"])
        writer.writeheader()
        for row in rows:
            writer.writerow(asdict(row))


def main() -> None:
    rows = audit_checks()
    write_outputs(rows)
    status = "passed" if all(row.status == "pass" for row in rows) else "failed"
    print(f"Pre-submission audit {status} with {len(rows)} checks.")
    if status != "passed":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
