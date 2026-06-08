# Election Duplicate Vote-Pair Statistical Review / 관내사전투표 동일 득표쌍 통계 검토

This repository contains the Korean and English papers, official-data reproduction scripts, intermediate outputs, cached source files, and compiled Korean and English PDFs.

이 저장소는 관내사전투표 동일 득표쌍 분석의 한글/영문 원고, 공식자료 재현 스크립트, 중간 산출물, 원자료 캐시, IEIE 형식 한글 PDF를 포함한다.

- 저자: 김준호
- 소속: 없음
- 이메일: junhokim0331@gmail.com

## Read the Papers

| Language | Markdown | PDF / LaTeX |
|---|---|---|
| Korean | [`paper_statistical_implausibility_ko.md`](paper_statistical_implausibility_ko.md) | [`latex/ieie/main.pdf`](latex/ieie/main.pdf), [`latex/ieie/main.tex`](latex/ieie/main.tex) |
| English | [`paper_statistical_implausibility_en.md`](paper_statistical_implausibility_en.md) | [`latex/en/main_en.pdf`](latex/en/main_en.pdf), [`latex/en/main_en.tex`](latex/en/main_en.tex) |

## Scope

The papers argue that the repeated identical in-district early-vote pairs are not adequately explained by ordinary chance under the reported statistical tests. They do not, by themselves, identify a perpetrator or establish a legal finding of election fraud. The requested remedy is raw-data disclosure and independent audit.

한글 원고의 결론은 특정 개인이나 기관의 범죄를 통계만으로 법적으로 단정하는 것이 아니라, 우연가설만으로 해소되지 않는 통계적 이상치이므로 원자료 공개와 독립 감사가 필요하다는 것이다.

## Source Policy

The repository intentionally excludes informal video-platform materials and video-derived claims as evidentiary sources. The core analysis uses official election files, NEC election-statistics HTML pages, reproducible parsing scripts, and explicitly named media reports only to define the initially reported 2026 event rows before official-page rechecking.

이 저장소는 비공식 영상 플랫폼 자료와 영상 기반 비공식 주장을 증거 출처로 쓰지 않는다. 핵심 분석은 공식 선거자료, 선관위 선거통계시스템 HTML, 재현 가능한 파싱 스크립트, 그리고 2026년 사건행 정의를 위한 명시적 보도자료에 한정한다.

## 주요 문서

- `paper_statistical_implausibility_ko.md`: 학술 원고 본문
- `paper_statistical_implausibility_en.md`: English paper
- `cover_letter_ko.md`: 학회 제출용 커버레터
- `cover_letter_en.md`: English submission cover letter
- `submission_memo_ko.md`: 제출 메모, 주장 범위, 한계, 재현 절차, 예상 반론 요약
- `submission_memo_en.md`: English submission memo
- `reviewer_response_ko.md`: 심사자 반론 대응 메모
- `reviewer_response_en.md`: English reviewer objection response memo
- `evidence_matrix_ko.md`: 핵심 주장과 재현 파일의 대응표
- `evidence_matrix_en.md`: English claim-to-evidence matrix
- `DATA_DICTIONARY_ko.md`: 핵심 출력 CSV·JSON 데이터 사전
- `DATA_DICTIONARY_en.md`: English output data dictionary
- `REVIEWER_QUICKSTART_ko.md`: 심사자용 5~10분 핵심 재현 Quickstart
- `REVIEWER_QUICKSTART_en.md`: English reviewer reproduction quickstart
- `REPRODUCIBILITY_CHECKLIST_ko.md`: 독립 검증자용 재현성 점검표
- `REPRODUCIBILITY_CHECKLIST_en.md`: English reproducibility checklist
- `STATISTICAL_CALCULATION_NOTE_ko.md`: 핵심 확률값의 공식·입력값·출력 파일 연결 노트
- `STATISTICAL_CALCULATION_NOTE_en.md`: English statistical calculation note
- `data_availability_2026_ko.md`: 2026년 공식 개표자료 가용성 점검 메모
- `data_availability_2026_en.md`: English 2026 data availability memo
- `AUDIT_PROTOCOL_ko.md`: 독립 원자료 감사 프로토콜
- `AUDIT_PROTOCOL_en.md`: English independent raw-data audit protocol
- `ALTERNATIVE_EXPLANATIONS_MATRIX_ko.md`: 대안 설명별 검증 매트릭스
- `ALTERNATIVE_EXPLANATIONS_MATRIX_en.md`: English alternative-explanations evaluation matrix
- `LOOK_ELSEWHERE_ROBUSTNESS_ko.md`: 사후탐색·다중비교 반론 강건성 노트
- `LOOK_ELSEWHERE_ROBUSTNESS_en.md`: English look-elsewhere robustness note
- `FINAL_SUBMISSION_CHECKLIST_ko.md`: 최종 제출 전 점검표
- `FINAL_SUBMISSION_CHECKLIST_en.md`: English final pre-submission checklist
- `latex/ieie/main.tex`: IEIE 템플릿 기반 LaTeX 원고
- `latex/ieie/main.pdf`: 컴파일된 PDF 원고
- `latex/en/main_en.tex`: English LaTeX source
- `latex/en/main_en.pdf`: compiled English PDF

## 원자료

공개된 과거 선거자료는 `data/`에 정리했다.

- `local2014.xlsx`
- `assembly2016.xlsx`
- `pres2017.xlsx`
- `local2018.xlsx`
- `assembly2020.xlsx`
- `pres2022.xlsx`
- `local2022.xlsx`
- `assembly2024.xlsx`
- `pres2025.xlsx`
- `nec_2026_official_html/`: 중앙선거관리위원회 선거통계시스템 개표단위별 개표결과 공식 HTML 캐시

2026년 지방선거의 공공데이터포털 공식 통합 XLSX 개표 원자료는 이 패키지에 포함되어 있지 않다. 본 원고 작성 시점에는 과거 기준선 자료와 같은 방식의 공식 통합 파일을 확보하지 못했기 때문이다. 다만 2026년 12개 사건행의 득표값은 중앙선거관리위원회 선거통계시스템의 개표단위별 개표결과 공식 HTML에서 직접 추출해 대조했다. 원본 HTML 캐시는 `data/nec_2026_official_html/`에, 파싱 결과는 `outputs/nec_2026_reported_duplicate_cases.csv`와 `outputs/nec_2026_reported_duplicate_pairs.csv`에 정리했다. 자세한 점검 내용은 `data_availability_2026_ko.md`에 정리했다.

## 재현 방법

패키지 루트에서 의존성을 설치한 뒤 전체 재현 스크립트를 실행한다.

```bash
python3 -m pip install -r requirements.txt
python3 scripts/run_all.py
```

심사자가 핵심 수치만 빠르게 검산하려면 다음 문서를 먼저 보면 된다.

- `REVIEWER_QUICKSTART_ko.md`
- `REVIEWER_QUICKSTART_en.md`

개별 스크립트를 직접 실행할 수도 있다.

```bash
python3 scripts/analyze_duplicates.py
python3 scripts/count_nec_2026_gwangju_jeonnam_units.py
python3 scripts/analyze_governor_actual_top2.py
python3 scripts/bootstrap_governor_duplicates.py
python3 scripts/fetch_nec_2026_duplicate_cases.py
python3 scripts/analyze_songdo_probability.py
python3 scripts/probability_sensitivity.py
python3 scripts/analyze_early_day_assembly.py
python3 scripts/verify_core_claims.py
python3 scripts/statistical_robustness_audit.py
python3 scripts/video_source_exclusion_audit.py
python3 scripts/source_provenance_audit.py
python3 scripts/claim_boundary_audit.py
python3 scripts/objection_coverage_audit.py
python3 scripts/pre_submission_audit.py
python3 scripts/submission_integrity_report.py
python3 scripts/generate_checksums.py
python3 scripts/create_submission_zip.py
python3 scripts/local_ci_validation_report.py
```

2026년 선관위 공식 HTML 캐시를 새로 내려받아 재검증하려면 다음처럼 실행한다.

```bash
python3 scripts/fetch_nec_2026_duplicate_cases.py --fetch
```

LaTeX 제출본은 다음 명령으로 다시 생성하고 컴파일할 수 있다.

```bash
python3 latex/convert_to_ieie.py
cd latex/ieie
xelatex -interaction=nonstopmode -halt-on-error main.tex
xelatex -interaction=nonstopmode -halt-on-error main.tex
cd ../en
xelatex -interaction=nonstopmode -halt-on-error main_en.tex
xelatex -interaction=nonstopmode -halt-on-error main_en.tex
cd ../..
```

업로드용 zip은 다음 명령으로 생성한다.

```bash
python3 scripts/create_submission_zip.py
```

이 명령은 제출 ZIP과 함께 ZIP 자체를 식별하기 위한 sidecar 파일도 생성한다.

- `dist/election_duplicate_ieie_submission.zip.sha256`
- `dist/election_duplicate_ieie_submission_manifest.json`

## 주요 출력

- `outputs/duplicate_summary.csv`
- `outputs/duplicate_groups.csv`
- `outputs/governor_actual_top2_summary.csv`
- `outputs/governor_actual_top2_by_contest.csv`
- `outputs/governor_actual_top2_duplicates.csv`
- `outputs/governor_bootstrap_summary.csv`
- `outputs/governor_bootstrap_histogram.csv`
- `outputs/nec_2026_gwangju_jeonnam_unit_counts.csv`
- `outputs/nec_2026_gwangju_jeonnam_units.csv`
- `outputs/nec_2026_gwangju_jeonnam_unit_summary.json`
- `outputs/nec_2026_reported_duplicate_cases.csv`
- `outputs/nec_2026_reported_duplicate_pairs.csv`
- `outputs/nec_2026_fetch_manifest.json`
- `outputs/songdo_probability_summary.csv`
- `outputs/songdo_official_rows.csv`
- `outputs/probability_core.csv`
- `outputs/probability_exact_collision.csv`
- `outputs/probability_k_sensitivity.csv`
- `outputs/probability_n_sensitivity.csv`
- `outputs/early_day_assembly_summary.csv`
- `outputs/early_day_assembly_twoparty.csv`
- `outputs/core_claims_verification.csv`
- `outputs/core_claims_verification.json`
- `outputs/statistical_robustness_audit.csv`
- `outputs/statistical_robustness_audit.json`
- `outputs/video_source_exclusion_audit.csv`
- `outputs/video_source_exclusion_audit.json`
- `outputs/source_provenance_audit.csv`
- `outputs/source_provenance_audit.json`
- `outputs/claim_boundary_audit.csv`
- `outputs/claim_boundary_audit.json`
- `outputs/objection_coverage_audit.csv`
- `outputs/objection_coverage_audit.json`
- `outputs/pre_submission_audit.csv`
- `outputs/pre_submission_audit.json`
- `outputs/submission_integrity_report.md`
- `outputs/submission_integrity_report.json`
- `outputs/local_ci_validation_report.md`
- `outputs/local_ci_validation_report.json`
- `outputs/checksums_sha256.csv`
- `dist/election_duplicate_ieie_submission.zip.sha256`
- `dist/election_duplicate_ieie_submission_manifest.json`

`outputs/local_ci_validation_report.*`는 최종 ZIP을 검증하는 외부 리포트이므로 제출 ZIP 내부에는 포함하지 않는다. ZIP 내부에 넣으면 리포트가 기록한 ZIP 해시가 다시 바뀌는 순환 문제가 생긴다.

## 현재 검증된 핵심 숫자

- 과거 파싱 행: `81,701`
- 과거 시·도지사 선거구: `51`
- 시·도지사 실제 1·2위 비교쌍: `1,514,172`
- 시·도지사 실제 1·2위 동일 득표쌍: `15`
- 과거 한 선거구 안 최대 반복: `3쌍`
- 선관위 공식 HTML 기준 광주전남 관내사전 개표단위: `393`
- 추정 \(K\): `100,944.8`
- `N=393` 기준 `P(C >= 5)`: `0.0011484064`, 약 `0.115%`
- `N=393`, `K=100945` 기준 정확 pair-collision `P(C >= 5)`: `0.0012190884`, 약 `0.122%`
- `N=393` 기준 `P(C >= 6)`: `0.0001432242`, 약 `0.0143%`
- 연수구 관내사전 15개 단위 중 한 쌍 이상 동일 득표쌍 확률: 약 `0.104%`
- 특정 송도1동-송도2동 두 단위가 같은 득표쌍을 가질 조건부 확률: 약 `0.000991%`
- 시·도지사 실제 득표쌍 비복원 재표본추출: `200,000`회
- 비복원 재표본추출 `C >= 5`: `0`회, 관측해상도 기준 `<0.0005%`, 3의 법칙 95% 상한 약 `0.0015%`
- 선관위 선거통계시스템 공식 HTML에서 재확인한 2026년 사건행: `12`
- 선관위 선거통계시스템 공식 HTML에서 재확인한 2026년 동일 득표쌍: `6`
- 핵심 주장 검증: `45`개 항목 `pass`
- 제출 전 자동 감사: `11`개 항목 `pass`

## 출처 정책

원고는 과거 공식 선거자료, 공공데이터포털 설명, 2026년 사건 정의를 위한 공개 기사에 의존한다. 인용하지 않은 임시 매체 산출물은 원고와 재현 패키지에서 제외했다.

## 주장 범위

이 원고는 특정 개인이나 기관의 개표 조작이 법적으로 입증되었다고 주장하지 않는다. 원고의 주장은 더 좁고 재현 가능하다. 과거 시·도지사 관내사전투표 기준선과 본문에서 정의한 사건 기준을 적용하면, 선관위 선거통계시스템 공식 화면에서 재확인되는 2026년 광주전남 5쌍 동일 득표 반복은 개표상황표 원본과 1차 분류기 결과의 독립 감사가 필요한 통계적 이상치라는 것이다.

## 제출 패키지 구성

- `paper_statistical_implausibility_ko.md`
- `paper_statistical_implausibility_en.md`
- `cover_letter_ko.md`
- `cover_letter_en.md`
- `submission_memo_ko.md`
- `submission_memo_en.md`
- `reviewer_response_ko.md`
- `reviewer_response_en.md`
- `evidence_matrix_ko.md`
- `evidence_matrix_en.md`
- `DATA_DICTIONARY_ko.md`
- `DATA_DICTIONARY_en.md`
- `REVIEWER_QUICKSTART_ko.md`
- `REVIEWER_QUICKSTART_en.md`
- `REPRODUCIBILITY_CHECKLIST_ko.md`
- `REPRODUCIBILITY_CHECKLIST_en.md`
- `STATISTICAL_CALCULATION_NOTE_ko.md`
- `STATISTICAL_CALCULATION_NOTE_en.md`
- `data_availability_2026_ko.md`
- `data_availability_2026_en.md`
- `AUDIT_PROTOCOL_ko.md`
- `AUDIT_PROTOCOL_en.md`
- `ALTERNATIVE_EXPLANATIONS_MATRIX_ko.md`
- `ALTERNATIVE_EXPLANATIONS_MATRIX_en.md`
- `LOOK_ELSEWHERE_ROBUSTNESS_ko.md`
- `LOOK_ELSEWHERE_ROBUSTNESS_en.md`
- `FINAL_SUBMISSION_CHECKLIST_ko.md`
- `FINAL_SUBMISSION_CHECKLIST_en.md`
- `README.md`
- `requirements.txt`
- `latex/`
- `scripts/`
- `outputs/`
- `data/`
- `dist/election_duplicate_ieie_submission.zip`
- `dist/election_duplicate_ieie_submission.zip.sha256`
- `dist/election_duplicate_ieie_submission_manifest.json`
