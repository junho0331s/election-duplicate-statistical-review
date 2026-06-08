# 재현성 점검 체크리스트

## 목적

이 문서는 심사자 또는 독립 검증자가 제출 패키지의 핵심 계산을 빠르게 재현하기 위한 점검표이다. 원고의 결론은 특정 원인의 법적 확정이 아니라, 공개자료와 재현 가능한 계산으로 확인되는 통계적 이상치 및 원자료 감사 필요성이다.

## 실행 환경

- Python 3.10 이상
- `requirements.txt`의 Python 패키지
- PDF 재생성이 필요한 경우 XeLaTeX

## 전체 재현 명령

패키지 루트에서 다음 명령을 실행한다.

```bash
python3 -m pip install -r requirements.txt
python3 scripts/run_all.py
```

성공 시 마지막 줄에는 다음 취지의 문장이 출력되어야 한다.

```text
All reproduction scripts completed, package validation passed, and expected outputs exist.
```

## 핵심 산출물과 기대값

| 점검 항목 | 기대값 | 확인 파일 |
| --- | ---: | --- |
| 과거 파싱 행 수 | 81,701 | `outputs/dataset_counts.csv` |
| 시·도지사 선거구 수 | 51 | `outputs/governor_actual_top2_summary.csv` |
| 시·도지사 실제 1·2위 비교쌍 | 1,514,172 | `outputs/governor_actual_top2_summary.csv` |
| 과거 동일 득표쌍 | 15 | `outputs/governor_actual_top2_summary.csv` |
| 과거 한 선거구 안 최대 반복 | 3쌍 | `outputs/governor_actual_top2_summary.csv` |
| 광주전남 관내사전 개표단위 수 | 393 | `outputs/nec_2026_gwangju_jeonnam_unit_summary.json` |
| 2026년 공식 화면 사건행 | 12 | `outputs/nec_2026_reported_duplicate_cases.csv` |
| 2026년 공식 화면 동일 득표쌍 | 6쌍 | `outputs/nec_2026_reported_duplicate_pairs.csv` |
| \(N=393\) 기준 \(P(C \ge 5)\) | 0.0011484064248148407 | `outputs/probability_core.csv` |
| \(N=393\) 기준 \(P(C \ge 6)\) | 0.00014322422035484283 | `outputs/probability_core.csv` |
| 연수구 내부 한 쌍 이상 동일 득표쌍 확률 | 0.0010396316588441312 | `outputs/songdo_probability_summary.csv` |
| 특정 송도1동-송도2동 동일 득표쌍 조건부 확률 | 0.000009906404292246851 | `outputs/songdo_probability_summary.csv` |
| 비복원 재표본추출 반복 수 | 200,000 | `outputs/governor_bootstrap_summary.csv` |
| 비복원 재표본추출 \(C \ge 5\) | 0회 | `outputs/governor_bootstrap_summary.csv` |
| \(C \ge 5\)의 95% 상한 | 0.000015 | `outputs/governor_bootstrap_summary.csv` |
| 2020년 총선 민주당 사전 우위 지역구 | 236/236 | `outputs/early_day_assembly_summary.csv` |
| 2024년 총선 민주당 사전 우위 지역구 | 245/245 | `outputs/early_day_assembly_summary.csv` |

## 무결성 점검

`outputs/checksums_sha256.csv`는 주요 원자료, 스크립트, 출력 CSV, PDF의 SHA-256 해시를 포함한다. 제출 ZIP을 받은 뒤에는 다음을 확인한다.

1. `latex/ieie/main.pdf`가 ZIP 안에 있다.
2. `outputs/checksums_sha256.csv`가 ZIP 안에 있다.
3. `outputs/governor_bootstrap_summary.csv`가 ZIP 안에 있다.
4. `outputs/nec_2026_gwangju_jeonnam_unit_summary.json`가 ZIP 안에 있다.
5. `outputs/nec_2026_reported_duplicate_cases.csv`가 ZIP 안에 있다.
6. `.aux`, `.log`, `.out`, `.synctex.gz` 같은 LaTeX 부산물이 ZIP 안에 없다.

이 조건들은 `scripts/validate_package.py`가 자동으로 검사한다.

## 결론 해석 기준

위 값들이 재현되면 원고의 핵심 결론은 다음 범위에서 지지된다.

> 중앙선거관리위원회 선거통계시스템 공식 화면값과 과거 공식자료 기준선을 함께 볼 때, 2026년 광주전남 5쌍 동일 득표 반복은 우연가설과 양립하기 어려운 통계적 이상치이며, 개표상황표 원본과 1차 분류기 결과의 독립 검증이 필요하다.

반대로 다음 중 하나가 확인되면 원고의 결론은 약화되거나 수정되어야 한다.

1. 2026년 공식 통합 파일 또는 개표상황표 원본에서 12개 사건행의 득표값이 현재 공식 화면값과 다르다.
2. 광주전남 5쌍이 같은 후보 조합, 같은 관내사전투표 유형, 같은 광역 선거구 내부 반복이 아니다.
3. 동일 제도권 시·도지사 관내사전투표 자료에서 한 선거구 안 5쌍 이상 반복이 다수 확인된다.
4. 2026년 5쌍 모두에 대해 1차 분류기 결과, 재확인표 배분, 입력 로그가 독립적으로 일관되며 동일성이 자연적 개표 과정에서 발생했음이 문서로 확인된다.
