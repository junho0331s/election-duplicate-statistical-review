#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs"


@dataclass
class ObjectionCheck:
    objection: str
    file: str
    expected: str
    actual: str
    status: str


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8", errors="ignore")


def pdf_text(path: str) -> str:
    import fitz  # type: ignore[import-not-found]

    pdf = fitz.open(ROOT / path)
    return "\n".join(page.get_text() for page in pdf)


def ok(condition: bool) -> str:
    return "pass" if condition else "fail"


def check(path: str, objection: str, needles: list[str], expected: str) -> ObjectionCheck:
    body = read(path)
    hits = [needle for needle in needles if needle in body]
    return ObjectionCheck(
        objection=objection,
        file=path,
        expected=expected,
        actual=f"{len(hits)}/{len(needles)} markers present",
        status=ok(len(hits) == len(needles)),
    )


def check_any(path: str, objection: str, alternatives: list[str], expected: str) -> ObjectionCheck:
    body = read(path)
    hit = any(needle in body for needle in alternatives)
    return ObjectionCheck(
        objection=objection,
        file=path,
        expected=expected,
        actual="present" if hit else "missing",
        status=ok(hit),
    )


def check_pdf(path: str, objection: str, needles: list[str], expected: str) -> ObjectionCheck:
    body = pdf_text(path)
    hits = [needle for needle in needles if needle in body]
    return ObjectionCheck(
        objection=objection,
        file=path,
        expected=expected,
        actual=f"{len(hits)}/{len(needles)} markers present",
        status=ok(len(hits) == len(needles)),
    )


def audit_checks() -> list[ObjectionCheck]:
    checks: list[ObjectionCheck] = [
        check(
            "paper_statistical_implausibility_ko.md",
            "many units can produce one duplicate",
            ["개표단위가 많으면", "한 쌍", "5쌍"],
            "Korean paper separates one duplicate from the five-pair cluster",
        ),
        check(
            "paper_statistical_implausibility_en.md",
            "many units can produce one duplicate",
            ["many counting units", "one identical vote pair", "five pairs"],
            "English paper separates one duplicate from the five-pair cluster",
        ),
        check(
            "paper_statistical_implausibility_ko.md",
            "2014 inclusion weakens but does not remove result",
            ["2014년", "보수적", "5쌍 이상은 관찰되지 않았다"],
            "Korean paper states that including 2014 is conservative",
        ),
        check(
            "paper_statistical_implausibility_en.md",
            "2014 inclusion weakens but does not remove result",
            ["2014", "conservative", "five or more pairs"],
            "English paper states that including 2014 is conservative",
        ),
        check(
            "paper_statistical_implausibility_ko.md",
            "three historical pairs versus five observed pairs",
            ["3쌍 이상은 약 4.23%", "5쌍 이상은 약 0.115%", "약 37배"],
            "Korean paper quantifies why three and five are not equivalent",
        ),
        check(
            "paper_statistical_implausibility_en.md",
            "three historical pairs versus five observed pairs",
            ["three or more pairs have probability about 4.23%", "Five or more pairs have probability about 0.115%", "37 times rarer"],
            "English paper quantifies why three and five are not equivalent",
        ),
        check(
            "LOOK_ELSEWHERE_ROBUSTNESS_ko.md",
            "post-search and multiple-comparison objection",
            ["사후탐색", "다중비교", "광주전남 내부 5쌍", "전국 12곳"],
            "Korean robustness note separates primary test from post-search context",
        ),
        check(
            "LOOK_ELSEWHERE_ROBUSTNESS_en.md",
            "post-search and multiple-comparison objection",
            ["look-elsewhere", "multiple comparisons", "Gwangju-Jeonnam internal five-pair", "nationwide"],
            "English robustness note separates primary test from post-search context",
        ),
        check(
            "paper_statistical_implausibility_ko.md",
            "unit heterogeneity and model dependence",
            ["독립적이지도 않고", "경험적", "민감도 분석"],
            "Korean paper acknowledges non-iid units and reports empirical/sensitivity checks",
        ),
        check(
            "paper_statistical_implausibility_en.md",
            "unit heterogeneity and model dependence",
            ["not generated from identical independent draws", "empirical reference value", "Sensitivity to the Effective Pair Space"],
            "English paper acknowledges non-iid units and reports empirical/sensitivity checks",
        ),
        check(
            "paper_statistical_implausibility_ko.md",
            "self-selection objection for early voting",
            ["사전투표자의 자발적 선택", "보조 검정", "직접 증명은 아니다"],
            "Korean paper limits early-vote analysis and acknowledges self-selection",
        ),
        check(
            "paper_statistical_implausibility_en.md",
            "self-selection objection for early voting",
            ["voter self-selection", "auxiliary test", "does not prove misconduct"],
            "English paper limits early-vote analysis and acknowledges self-selection",
        ),
        check(
            "paper_statistical_implausibility_ko.md",
            "rare events can occur objection",
            ["드문 사건", "불가능을 뜻하지 않는다", "원자료 감사"],
            "Korean paper distinguishes rarity from impossibility and points to audit",
        ),
        check(
            "paper_statistical_implausibility_en.md",
            "rare events can occur objection",
            ["Rare events", "does not mean impossibility", "raw-data audit"],
            "English paper distinguishes rarity from impossibility and points to audit",
        ),
        check(
            "paper_statistical_implausibility_ko.md",
            "official integrated file limitation",
            ["공식 통합 파일", "공식 화면 HTML", "개표상황표 원본"],
            "Korean paper states the official-page basis and remaining raw-file limitation",
        ),
        check(
            "paper_statistical_implausibility_en.md",
            "official integrated file limitation",
            ["official integrated file", "official screen HTML", "original counting statements"],
            "English paper states the official-page basis and remaining raw-file limitation",
        ),
        check(
            "ALTERNATIVE_EXPLANATIONS_MATRIX_ko.md",
            "benign alternatives matrix",
            ["낮은 확률의 우연", "전산 입력 또는 정정 오류", "재확인표 후보별 배분", "보도 기반 사건 정의 오류"],
            "Korean alternatives matrix covers chance, input/display, review-ballot, and event-definition alternatives",
        ),
        check(
            "ALTERNATIVE_EXPLANATIONS_MATRIX_en.md",
            "benign alternatives matrix",
            ["Low-probability coincidence", "Data-entry or correction error", "Candidate allocation of reviewed ballots", "Press-defined event error"],
            "English alternatives matrix covers chance, input/display, review-ballot, and event-definition alternatives",
        ),
        check(
            "reviewer_response_ko.md",
            "reviewer response memo coverage",
            ["반론", "응답", "반증 가능 조건", "원자료 감사 판정 기준"],
            "Korean reviewer memo has objection, response, falsifiability, and audit sections",
        ),
        check(
            "reviewer_response_en.md",
            "reviewer response memo coverage",
            ["Main Objections and Responses", "Falsification Conditions", "Raw-Data Audit Criteria"],
            "English reviewer memo has objection, response, falsifiability, and audit sections",
        ),
        check(
            "reviewer_response_ko.md",
            "designated five-pair probability interpretation",
            ["0.115%는 사건을 넓게 잡은 주검정", "사전 지정 대응쌍", "9.54\\times10^{-26}", "probability_designated_pairs.csv"],
            "Korean reviewer memo separates broad Poisson probability from designated five-pair conditional probability",
        ),
        check(
            "reviewer_response_en.md",
            "designated five-pair probability interpretation",
            ["0.115% value is the broad primary test", "pre-designated pairings", "9.54\\times10^{-26}", "probability_designated_pairs.csv"],
            "English reviewer memo separates broad Poisson probability from designated five-pair conditional probability",
        ),
        check(
            "reviewer_response_ko.md",
            "post-disclosure reviewer decision tree",
            ["원자료 공개 후 판정 트리", "약화 또는 철회", "행정적으로 설명된 사건", "원인조사 단계", "독립 감사의 대상"],
            "Korean reviewer memo states the conditional decision path after raw-record disclosure",
        ),
        check(
            "reviewer_response_en.md",
            "post-disclosure reviewer decision tree",
            ["Post-Disclosure Decision Tree", "weakened or withdrawn", "administratively explained event", "causal-investigation stage", "object of independent audit"],
            "English reviewer memo states the conditional decision path after raw-record disclosure",
        ),
        check(
            "paper_statistical_implausibility_ko.md",
            "chain-of-custody raw-record requirement",
            ["투표함·개표배치 인수인계 기록", "장비·시간대·심사 흐름", "배치 흐름"],
            "Korean paper requires custody/batch records as a raw-data audit discriminator",
        ),
        check(
            "paper_statistical_implausibility_en.md",
            "chain-of-custody raw-record requirement",
            ["chain-of-custody records", "equipment, timestamp, review-table, or batch flow", "Batch movement"],
            "English paper requires custody/batch records as a raw-data audit discriminator",
        ),
        check_any(
            "FINAL_SUBMISSION_CHECKLIST_ko.md",
            "final checklist objection controls",
            ["사후탐색", "자기선택", "대안 설명"],
            "Korean final checklist references at least one objection-control category",
        ),
        check_any(
            "FINAL_SUBMISSION_CHECKLIST_en.md",
            "final checklist objection controls",
            ["look-elsewhere", "self-selection", "alternative explanations"],
            "English final checklist references at least one objection-control category",
        ),
        check_pdf(
            "latex/ieie/main.pdf",
            "Korean PDF objection controls render",
            ["사후탐색", "광주전남", "5쌍", "직접증명"],
            "Korean submission PDF renders post-search, primary-cluster, and direct-proof boundaries",
        ),
        check_pdf(
            "latex/en/main_en.pdf",
            "English PDF objection controls render",
            ["multiple", "Gwangju-Jeonnam", "five-pair", "voter self-selection"],
            "English submission PDF renders multiple-comparison, primary-cluster, and self-selection boundaries",
        ),
    ]
    return checks


def main() -> None:
    OUT.mkdir(exist_ok=True)
    checks = audit_checks()
    data = {
        "status": "pass" if all(row.status == "pass" for row in checks) else "fail",
        "check_count": len(checks),
        "scope": "coverage audit for expected statistical and evidentiary objections",
        "checks": [asdict(row) for row in checks],
    }
    (OUT / "objection_coverage_audit.json").write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    with (OUT / "objection_coverage_audit.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["objection", "file", "expected", "actual", "status"])
        writer.writeheader()
        for row in checks:
            writer.writerow(asdict(row))

    if data["status"] != "pass":
        failures = [row for row in checks if row.status != "pass"]
        sample = "; ".join(f"{row.file}:{row.objection}:{row.actual}" for row in failures[:10])
        raise SystemExit(f"Objection coverage audit failed: {sample}")
    print(f"Objection coverage audit passed with {len(checks)} checks.")


if __name__ == "__main__":
    main()
