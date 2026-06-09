#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs"


@dataclass
class BoundaryCheck:
    check: str
    file: str
    expected: str
    actual: str
    status: str


def pass_fail(condition: bool) -> str:
    return "pass" if condition else "fail"


def text(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8", errors="ignore")


def pdf_text(path: str) -> str:
    import fitz  # type: ignore[import-not-found]

    pdf = fitz.open(ROOT / path)
    return "\n".join(page.get_text() for page in pdf)


def contains_any(body: str, needles: list[str]) -> bool:
    return any(needle in body for needle in needles)


def compact(body: str) -> str:
    return "".join(body.split())


def unnegated_hits(body: str, patterns: list[str]) -> list[str]:
    hits: list[str] = []
    for label, pattern in zip(FORBIDDEN_LABELS, patterns):
        start = 0
        while True:
            index = body.find(pattern, start)
            if index < 0:
                break
            prefix = body[max(0, index - 120):index].lower()
            negated = (
                "not" in prefix
                or "does not assert" in prefix
                or "does not claim" in prefix
                or "아니" in prefix
                or "않" in prefix
            )
            if not negated:
                hits.append(label)
            start = index + len(pattern)
    return hits


def check_required(path: str, body: str, name: str, needles: list[str], expected: str) -> BoundaryCheck:
    hits = [needle for needle in needles if needle in body]
    return BoundaryCheck(
        check=name,
        file=path,
        expected=expected,
        actual=f"{len(hits)}/{len(needles)} markers present",
        status=pass_fail(len(hits) == len(needles)),
    )


def check_required_compact(path: str, body: str, name: str, needles: list[str], expected: str) -> BoundaryCheck:
    body_compact = compact(body).lower()
    hits = [needle for needle in needles if needle.lower() in body_compact]
    return BoundaryCheck(
        check=name,
        file=path,
        expected=expected,
        actual=f"{len(hits)}/{len(needles)} compact markers present",
        status=pass_fail(len(hits) == len(needles)),
    )


def check_any(path: str, body: str, name: str, alternatives: list[str], expected: str) -> BoundaryCheck:
    ok = contains_any(body, alternatives)
    return BoundaryCheck(
        check=name,
        file=path,
        expected=expected,
        actual="present" if ok else "missing",
        status=pass_fail(ok),
    )


def check_forbidden(path: str, body: str, patterns: list[str]) -> BoundaryCheck:
    hits = unnegated_hits(body, patterns)
    return BoundaryCheck(
        check="overclaim phrase absence",
        file=path,
        expected="0 legal-finality or non-falsifiable overclaim markers",
        actual=f"{len(hits)} hits",
        status=pass_fail(not hits),
    )


FORBIDDEN_PATTERNS = [
    "부정선거 " + "확정",
    "조작 " + "확정",
    "범죄 " + "확정",
    "부정행위가 " + "확정",
    "원인이 " + "확정",
    "반박" + "불가",
    "아무도 " + "반박",
    "fraud " + "proven",
    "misconduct has been " + "proven",
    "election fraud " + "occurred",
    "ir" + "refutable",
    "cannot be " + "refuted",
]

FORBIDDEN_LABELS = [
    "ko_election_fraud_final",
    "ko_manipulation_final",
    "ko_crime_final",
    "ko_misconduct_final",
    "ko_cause_final",
    "ko_nonfalsifiable_a",
    "ko_no_one_can_refute",
    "en_fraud_proven",
    "en_misconduct_proven",
    "en_fraud_occurred",
    "en_nonfalsifiable_a",
    "en_cannot_be_refuted",
]


def audit_checks() -> list[BoundaryCheck]:
    sources = {
        "paper_statistical_implausibility_ko.md": text("paper_statistical_implausibility_ko.md"),
        "paper_statistical_implausibility_en.md": text("paper_statistical_implausibility_en.md"),
        "submission_memo_ko.md": text("submission_memo_ko.md"),
        "submission_memo_en.md": text("submission_memo_en.md"),
        "reviewer_response_ko.md": text("reviewer_response_ko.md"),
        "reviewer_response_en.md": text("reviewer_response_en.md"),
        "latex/ieie/main.pdf": pdf_text("latex/ieie/main.pdf"),
        "latex/en/main_en.pdf": pdf_text("latex/en/main_en.pdf"),
    }

    checks: list[BoundaryCheck] = []
    for path, body in sources.items():
        checks.append(check_forbidden(path, body, FORBIDDEN_PATTERNS))

    checks.extend([
        check_required(
            "paper_statistical_implausibility_ko.md",
            sources["paper_statistical_implausibility_ko.md"],
            "Korean manuscript boundary markers",
            ["법적 확정", "직접 증거는 아니다", "원자료 감사", "반증 가능"],
            "legal boundary, direct-proof boundary, raw-data audit, and falsifiability are explicit",
        ),
        check_required(
            "paper_statistical_implausibility_en.md",
            sources["paper_statistical_implausibility_en.md"],
            "English manuscript boundary markers",
            ["not a legal finding", "not direct proof of misconduct", "raw-data audit", "falsified"],
            "legal boundary, direct-proof boundary, raw-data audit, and falsifiability are explicit",
        ),
        check_required(
            "submission_memo_ko.md",
            sources["submission_memo_ko.md"],
            "Korean submission memo boundary markers",
            ["법적 확정", "통계적 결론", "원자료", "독립 감사"],
            "submission memo states the bounded statistical claim and audit remedy",
        ),
        check_required(
            "submission_memo_en.md",
            sources["submission_memo_en.md"],
            "English submission memo boundary markers",
            ["legally proven", "defensible claim", "raw-data", "independent audit"],
            "submission memo states the bounded statistical claim and audit remedy",
        ),
        check_required(
            "reviewer_response_ko.md",
            sources["reviewer_response_ko.md"],
            "Korean reviewer-response boundary markers",
            ["반증 가능 조건", "원자료 감사", "직접 증거"],
            "reviewer response anticipates overclaim and falsifiability objections",
        ),
        check_required(
            "reviewer_response_en.md",
            sources["reviewer_response_en.md"],
            "English reviewer-response boundary markers",
            ["statistical audit trigger", "not a final legal attribution", "direct proof of misconduct"],
            "reviewer response anticipates overclaim and falsifiability objections",
        ),
        check_required(
            "paper_statistical_implausibility_ko.md",
            sources["paper_statistical_implausibility_ko.md"],
            "Korean raw-record requirements",
            ["개표상황표 원본", "1차 분류기 결과", "재확인표", "입력 로그"],
            "raw records needed for causal/legal attribution are listed",
        ),
        check_required(
            "paper_statistical_implausibility_en.md",
            sources["paper_statistical_implausibility_en.md"],
            "English raw-record requirements",
            ["original counting statements", "first-pass sorter results", "reviewed-ballot allocation records", "input logs"],
            "raw records needed for causal/legal attribution are listed",
        ),
        check_required(
            "paper_statistical_implausibility_ko.md",
            sources["paper_statistical_implausibility_ko.md"],
            "Korean post-disclosure decision levels",
            ["약화 또는 철회", "행정적으로 설명된 사건", "원인조사 단계", "독립 감사의 대상"],
            "post-disclosure decision levels state how raw records weaken, explain, strengthen, or keep audit open",
        ),
        check_required(
            "paper_statistical_implausibility_en.md",
            sources["paper_statistical_implausibility_en.md"],
            "English post-disclosure decision levels",
            ["weakened or withdrawn", "administratively explained", "causal-investigation stage", "object of independent audit"],
            "post-disclosure decision levels state how raw records weaken, explain, strengthen, or keep audit open",
        ),
        check_required_compact(
            "latex/ieie/main.pdf",
            sources["latex/ieie/main.pdf"],
            "Korean PDF post-disclosure decision levels",
            ["약화또는철회", "행정적으로설명된사건", "원인조사단계", "독립감사의대상"],
            "Korean PDF renders post-disclosure decision levels",
        ),
        check_required_compact(
            "latex/en/main_en.pdf",
            sources["latex/en/main_en.pdf"],
            "English PDF post-disclosure decision levels",
            ["weakenedorwithdrawn", "eventbecomesadmin-istrativelyexplained", "causal-investigationstage", "objectofindependentaudit"],
            "English PDF renders post-disclosure decision levels",
        ),
        check_any(
            "latex/ieie/main.pdf",
            compact(sources["latex/ieie/main.pdf"]),
            "Korean PDF claim-boundary rendering",
            ["법적확정", "직접증거가아니다", "직접증거는아니다"],
            "Korean PDF renders the claim-boundary text",
        ),
        check_any(
            "latex/en/main_en.pdf",
            sources["latex/en/main_en.pdf"],
            "English PDF claim-boundary rendering",
            ["not a legal finding", "not direct proof of misconduct"],
            "English PDF renders the claim-boundary text",
        ),
    ])
    return checks


def main() -> None:
    OUT.mkdir(exist_ok=True)
    checks = audit_checks()
    data = {
        "status": "pass" if all(row.status == "pass" for row in checks) else "fail",
        "check_count": len(checks),
        "scope": "claim-boundary, falsifiability, and raw-data-audit wording audit",
        "checks": [asdict(row) for row in checks],
    }
    (OUT / "claim_boundary_audit.json").write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    with (OUT / "claim_boundary_audit.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["check", "file", "expected", "actual", "status"])
        writer.writeheader()
        for row in checks:
            writer.writerow(asdict(row))

    if data["status"] != "pass":
        failures = [row for row in checks if row.status != "pass"]
        sample = "; ".join(f"{row.file}:{row.check}:{row.actual}" for row in failures[:10])
        raise SystemExit(f"Claim-boundary audit failed: {sample}")
    print(f"Claim-boundary audit passed with {len(checks)} checks.")


if __name__ == "__main__":
    main()
