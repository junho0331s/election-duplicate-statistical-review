# 심사자 재현 Quickstart

이 문서는 심사자나 독립 검증자가 5~10분 안에 논문의 핵심 재현 명제가 파일과 스크립트로 맞는지 확인하기 위한 최소 절차이다. 목적은 법적 원인 확정이 아니라, 공개자료와 재현 스크립트가 본문 수치를 실제로 산출하는지 검산하는 것이다.

## 0. 검증 범위

이 Quickstart로 확인되는 항목은 다음과 같다.

- 선관위 선거통계시스템 공식 HTML에서 재확인한 2026년 사건행 `12`개
- 위 사건행에서 형성되는 동일 득표쌍 `6`개
- 광주전남 내부 사건의 동일 득표쌍 `5`개
- 선관위 공식 HTML 기준 광주전남 관내사전 개표단위 `N=393`
- 과거 시·도지사 선거 `51`개 선거구 기준 한 선거구 안 최대 반복 `3`쌍
- `N=393`, `K=100,944.8` 기준 `P(C >= 5) = 0.0011484064`, 약 `0.115%`
- `N=393`, `K=100945` 기준 정확 pair-collision `P(C >= 5) = 0.0012190884`, 약 `0.122%`
- 과거 실제 득표쌍 비복원 재표본추출 `200,000`회에서 `C >= 5` 관측 `0`회
- 2020년과 2024년 총선의 분석 가능 전 지역구에서 민주당 후보의 사전투표 양자득표율이 당일투표보다 높았다는 부호검정 입력값
- 인천 송도 보조 사례의 조건부 확률과 연수구 단위 확률

이 Quickstart만으로 확인되지 않는 항목도 분리한다.

- 개표상황표 원본과 공식 화면값의 완전 일치 여부
- 1차 분류기 결과와 최종 공표값 사이의 후보별 변화
- 재확인표의 후보별 배분 내역
- 전산 입력·수정 로그
- 특정 원인이나 행위자의 법적 책임

따라서 본 패키지의 검증 결론은 “공개자료 기준 통계적 이상치와 원자료 감사 필요성”에 한정된다.

## 1. 최소 검증

패키지 루트에서 다음 명령을 실행한다.

```bash
python3 -m pip install -r requirements.txt
python3 scripts/verify_core_claims.py
python3 scripts/validate_package.py
```

기대 출력은 다음과 같다.

```text
Core claim verification passed with 45 checks.
Package validation passed.
```

`verify_core_claims.py`는 핵심 숫자 45개를 산출물과 대조한다. `validate_package.py`는 필수 파일, 금지 출처 문자열, 핵심 CSV·JSON 값, 영문 PDF 번역 커버리지, 체크섬, ZIP 포함 여부, 외부 로컬 ZIP 재현 감사를 함께 점검한다.

## 2. 전체 재현

산출물을 처음부터 다시 만들려면 다음 명령을 실행한다.

```bash
python3 scripts/run_all.py
```

기대 결과는 전체 분석 스크립트, 핵심 주장 검증, 체크섬 생성, ZIP 생성, 패키지 검증이 모두 완료되는 것이다. 재현 뒤에는 다음 파일들이 갱신되었는지 확인한다.

- `outputs/core_claims_verification.json`
- `outputs/core_claims_verification.csv`
- `outputs/checksums_sha256.csv`
- `dist/election_duplicate_ieie_submission.zip`

## 3. 핵심 파일

심사자가 우선 열어볼 파일은 다음 순서가 적절하다.

| 목적 | 파일 |
|---|---|
| 핵심 주장 자동 검증 결과 | `outputs/core_claims_verification.json` |
| 핵심 주장 자동 검증 결과의 표 형식 | `outputs/core_claims_verification.csv` |
| 2026년 사건행 | `outputs/nec_2026_reported_duplicate_cases.csv` |
| 2026년 동일 득표쌍 | `outputs/nec_2026_reported_duplicate_pairs.csv` |
| 과거 시·도지사 기준선 요약 | `outputs/governor_actual_top2_summary.csv` |
| 과거 시·도지사 중복 상세 | `outputs/governor_actual_top2_duplicates.csv` |
| 포아송 핵심 확률 | `outputs/probability_core.csv` |
| 정확 pair-collision 확률 | `outputs/probability_exact_collision.csv` |
| 비복원 재표본추출 결과 | `outputs/governor_bootstrap_summary.csv` |
| 사전투표·당일투표 부호검정 | `outputs/early_day_assembly_summary.csv` |
| 인천 송도 보조 확률 | `outputs/songdo_probability_summary.csv` |
| 산출물 데이터 사전 | `DATA_DICTIONARY_ko.md` |
| 주장과 파일 대응표 | `evidence_matrix_ko.md` |

## 4. 숫자 체크

| 주장 | 기대값 | 확인 파일 |
|---|---:|---|
| 과거 파싱 행 | `81,701` | `outputs/dataset_counts.csv` |
| 과거 시·도지사 선거구 | `51` | `outputs/governor_actual_top2_summary.csv` |
| 시·도지사 실제 1·2위 비교쌍 | `1,514,172` | `outputs/governor_actual_top2_summary.csv` |
| 과거 동일 득표쌍 | `15` | `outputs/governor_actual_top2_summary.csv` |
| 과거 한 선거구 안 최대 반복 | `3` | `outputs/governor_actual_top2_summary.csv` |
| 광주전남 관내사전 개표단위 | `393` | `outputs/nec_2026_gwangju_jeonnam_unit_summary.json` |
| 추정 가능한 득표쌍 범위 | `100,944.8` | `outputs/governor_actual_top2_summary.csv` |
| `P(C >= 5)` | `0.0011484064` | `outputs/probability_core.csv` |
| 정확 pair-collision `P(C >= 5)` | `0.0012190884` | `outputs/probability_exact_collision.csv` |
| 비복원 재표본추출 `C >= 5` | `0 / 200,000` | `outputs/governor_bootstrap_summary.csv` |
| 2026년 사건행 | `12` | `outputs/nec_2026_reported_duplicate_cases.csv` |
| 2026년 동일 득표쌍 | `6` | `outputs/nec_2026_reported_duplicate_pairs.csv` |

## 5. 해석 기준

검증 스크립트가 통과하면 “본문의 핵심 통계 수치가 패키지 안의 공개자료 기반 산출물과 일치한다”는 점은 확인된다. 다만 그 결과는 원인 확정이 아니다. 원인 판단에는 개표상황표 원본, 1차 분류기 결과, 재확인표 배분, 입력 로그가 필요하다. 본 논문이 요구하는 것은 그 원자료를 공개해 우연, 표시 오류, 검표·합산 과정, 입력 문제 중 어느 설명이 남는지 독립적으로 검증하자는 것이다.
