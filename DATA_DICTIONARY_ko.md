# 산출물 데이터 사전

이 문서는 `outputs/` 아래 핵심 CSV·JSON 산출물의 의미를 설명한다. 목적은 심사자나 독립 검증자가 파일 이름과 열 이름만 보고 분석 단위를 오해하지 않도록 하는 것이다. 모든 산출물은 공개 선거자료, 선관위 선거통계시스템 공식 HTML 캐시, 또는 그 자료를 처리한 재현 스크립트에서 생성된다.

## 공통 용어

| 용어 | 의미 |
| --- | --- |
| 개표단위 | 분석에서 한 행으로 취급하는 읍·면·동 또는 이에 준하는 공식 개표 결과 단위 |
| 관내사전투표 | 유권자가 자신의 등록 선거구 안에서 사전투표한 표 |
| 관외사전투표 | 유권자가 자신의 등록 선거구 밖에서 사전투표한 표 |
| 실제 1·2위 후보 | 파일에 적힌 후보 순서가 아니라 같은 선거구·투표유형 묶음에서 총득표 기준으로 산정한 1위와 2위 후보 |
| 득표쌍 | 실제 1위 후보 득표수와 실제 2위 후보 득표수를 순서쌍으로 묶은 값 |
| 동일 득표쌍 | 서로 다른 두 개표단위가 같은 1위 후보 득표수와 같은 2위 후보 득표수를 동시에 갖는 경우 |
| collision_pairs | 동일 득표쌍을 이루는 개표단위 쌍의 수. 같은 값이 3개 단위에서 반복되면 비교쌍은 3개가 된다. |
| duplicate_groups | 같은 득표쌍 값이 반복된 그룹 수. 같은 값이 3개 단위에서 반복되어도 그룹은 1개다. |

## 핵심 산출물

| 파일 | 행 단위 | 원고에서의 역할 | 주요 열 |
| --- | --- | --- | --- |
| `outputs/dataset_counts.csv` | 원자료 파일 또는 선거 단위 | 2014~2025 과거 기준선에 포함된 자료 규모 확인 | `dataset`, `rows` |
| `outputs/duplicate_summary.csv` | 선거·선거종류·투표유형 묶음 | 전체 중복 탐색의 넓은 요약 | `election`, `category`, `vote_class`, `units`, `top2_duplicate_groups`, `top2_duplicate_units` |
| `outputs/duplicate_groups.csv` | 반복된 득표 서명 그룹 | 중복 그룹이 어떤 선거·투표유형에서 생겼는지 확인 | `signature_type`, `election`, `category`, `contest`, `vote_class`, `signature`, `duplicate_units` |
| `outputs/duplicate_examples.csv` | 중복 그룹 안의 개별 개표단위 | 중복 그룹에 속한 구체 단위와 후보명 확인 | `signature_type`, `unit`, `candidate_names` |
| `outputs/governor_actual_top2_summary.csv` | 시·도지사 과거 기준선 전체 요약 1행 | 광주전남 5쌍 검정의 핵심 과거 기준선 | `governor_contests`, `comparison_pairs`, `collision_pairs`, `duplicate_groups`, `max_duplicate_groups_in_contest`, `khat`, `n_for_probability`, `p_at_least_5` |
| `outputs/governor_actual_top2_by_contest.csv` | 과거 시·도지사 선거구 1개 | 과거 51개 선거구 중 각 선거구의 동일쌍 수 확인 | `election`, `contest`, `units`, `comparison_pairs`, `duplicate_groups`, `collision_pairs`, `candidate_1`, `candidate_2` |
| `outputs/governor_actual_top2_duplicates.csv` | 과거 시·도지사 동일 득표쌍 1개 | 과거 실제 동일쌍 목록과 최대값 검증 | `election`, `contest`, `candidate_1`, `candidate_2`, `signature`, `duplicate_units`, `collision_pairs` |
| `outputs/governor_bootstrap_summary.csv` | 비복원 재표본추출 조건 1개 | 과거 실제 득표쌍 풀에서 5쌍 이상이 얼마나 나오는지 확인 | `sample_size`, `trials`, `threshold`, `exceedances`, `probability`, `rule_of_three_upper_95` |
| `outputs/governor_bootstrap_histogram.csv` | 재표본추출에서 관찰된 중복 그룹 수 | 재표본추출 분포의 형태 확인 | `duplicate_groups`, `trials`, `share` |
| `outputs/probability_core.csv` | 확률 계산 시나리오 1개 | 본문 핵심 포아송 근사 확률 표 | `n`, `k_space`, `threshold`, `lambda`, `probability`, `probability_percent`, `reciprocal` |
| `outputs/probability_exact_collision.csv` | 정확 pair-collision 계산 시나리오 1개 | 포아송 근사와 같은 질문을 정확 생일문제식 동적계획법으로 재계산 | `n`, `k_space`, `threshold`, `poisson_probability`, `exact_probability`, `exact_probability_percent`, `poisson_minus_exact`, `exact_reciprocal` |
| `outputs/probability_k_sensitivity.csv` | 가능한 득표쌍 범위 `K` 가정 1개 | `K` 변화에 대한 민감도 분석 | `k_space`, `threshold`, `probability_percent`, `reciprocal` |
| `outputs/probability_n_sensitivity.csv` | 개표단위 수 `N` 가정 1개 | `N` 변화에 대한 민감도 분석 | `n`, `threshold`, `probability_percent`, `reciprocal` |
| `outputs/nec_2026_gwangju_jeonnam_units.csv` | 2026년 광주·전남 시·도지사 관내사전 개표단위 1개 | `N=393`의 공식 HTML 기반 산출 근거 | `city`, `town`, `unit`, `vote_class`, `electors`, `turnout`, `source_file` |
| `outputs/nec_2026_gwangju_jeonnam_unit_counts.csv` | 시군구 또는 읍면동 묶음 | 광주·전남 관내사전 개표단위 수 집계 | `city`, `town`, `in_district_early_units`, `source_url` |
| `outputs/nec_2026_gwangju_jeonnam_unit_summary.json` | JSON 요약 | 2026년 광주·전남 개표단위 수 요약과 출력 파일 연결 | `regions`, `towns`, `in_district_early_units`, `output_counts`, `output_units` |
| `outputs/nec_2026_reported_duplicate_cases.csv` | 2026년 동일 득표 사건행 1개 | 12개 사건행이 공식 HTML에서 재현되는지 확인 | `pair_id`, `city`, `town`, `unit`, `candidate_1_votes`, `candidate_2_votes`, `electors`, `turnout`, `source_url` |
| `outputs/nec_2026_reported_duplicate_pairs.csv` | 2026년 동일 득표쌍 1개 | 12개 사건행이 6개 동일쌍을 이루는지 확인 | `pair_id`, `candidate_1`, `candidate_1_votes`, `candidate_2`, `candidate_2_votes`, `units` |
| `outputs/nec_2026_fetch_manifest.json` | JSON 메타데이터 | 2026년 공식 HTML 추출 조건과 사건 수 확인 | `source`, `election_id`, `election_code`, `case_rows`, `duplicate_pairs`, `towns` |
| `outputs/songdo_official_rows.csv` | 송도 개표단위 1개 | 송도1동·송도2동 최종 공개값 대조 | `unit`, `candidate_1_votes`, `candidate_2_votes`, `electors`, `turnout`, `invalid_votes`, `abstentions` |
| `outputs/songdo_probability_summary.csv` | 송도 확률 계산 조건 1개 | 송도 사례의 보조 감사 신호 계산 | `case`, `n_units`, `comparison_pairs`, `k_space`, `probability_percent`, `reciprocal` |
| `outputs/early_day_assembly_summary.csv` | 총선 1개 | 사전-당일 득표율 차이의 보조 이상성 요약 | `election`, `districts`, `mean_early_minus_day_pp`, `dem_early_higher_count`, `sign_test_p_one_sided`, `max_abs_z` |
| `outputs/early_day_assembly_twoparty.csv` | 총선 지역구 1개 | 각 지역구의 민주당 대 보수정당 양자득표율 차이 | `election`, `sido`, `district`, `early_dem_share`, `day_dem_share`, `early_minus_day_pp`, `z` |
| `outputs/public_discussion_claims_audit.csv` | 공개 논의 보조 주장 검산 행 1개 | 공개 협업형 백과나 온라인 논의에서 나온 확인 가능한 보조 주장을 공식자료로만 재검산 | `election`, `city`, `district`, `polling_station`, `lee_jae_myung`, `yoon_suk_yeol`, `ballots_cast`, `registered_voters` |
| `outputs/public_discussion_claims_audit.json` | JSON 공개 논의 보조 주장 검산 요약 | 2022년 비산1동 제3·제4투표소 동일 득표쌍 주장이 공식 대통령선거 파일에서 확인되는지 기계가독 검증 | `status`, `row_count`, `confirmed_pair`, `classification`, `failures` |
| `outputs/core_claims_verification.csv` | 핵심 검증 명제 1개 | `verify_core_claims.py`가 대조한 45개 핵심 수치를 스프레드시트에서 확인 | `claim`, `expected`, `actual`, `abs_tol`, `status` |
| `outputs/core_claims_verification.json` | JSON 검증 요약 | 같은 45개 핵심 수치의 기계가독 검증 결과 | `status`, `check_count`, `scope`, `checks` |
| `outputs/statistical_robustness_audit.csv` | 통계 강건성 감사 행 1개 | 포아송 근사, 정확계산, 민감도 분석, 재표본추출, 과거 최대값이 같은 결론을 지지하는지 확인 | `check`, `expected`, `actual`, `status` |
| `outputs/statistical_robustness_audit.json` | JSON 통계 강건성 감사 요약 | 같은 10개 강건성 감사 항목의 기계가독 검증 결과 | `status`, `check_count`, `scope`, `checks` |
| `outputs/video_source_exclusion_audit.csv` | 비공식 영상 출처 배제 감사 행 1개 | 원고·제출 문서가 비공식 동영상 플랫폼 기반 자료에 의존하지 않는지 스프레드시트에서 확인 | `file`, `video_url_count`, `informal_marker_count`, `status` |
| `outputs/video_source_exclusion_audit.json` | JSON 비공식 영상 출처 배제 감사 요약 | 원고·제출 문서 25개 파일에서 비공식 동영상 플랫폼 URL과 그 기반 의존 문구가 없는지 기계가독 검증 | `status`, `check_count`, `checked_files`, `failures` |
| `outputs/source_provenance_audit.csv` | 출처 URL 1개 | 원고 및 출처 정책 문서의 URL과 출처 분류를 스프레드시트에서 확인 | `file`, `url`, `domain`, `source_class`, `status` |
| `outputs/source_provenance_audit.json` | JSON 출처 감사 요약 | 원고 및 출처 정책 문서가 승인된 공식자료 또는 명시적 공개 보도 도메인을 쓰는지 검증 | `status`, `url_count`, `allowed_domain_suffixes`, `source_classes`, `failures` |
| `outputs/claim_boundary_audit.csv` | 주장 범위 감사 행 1개 | 원고가 통계적 이상치와 원자료 감사 요구를 말하면서 근거 없는 법적 확정으로 넘어가지 않는지 스프레드시트에서 확인 | `check`, `file`, `expected`, `actual`, `status` |
| `outputs/claim_boundary_audit.json` | JSON 주장 범위 감사 요약 | 과장 주장 부재, 반증 가능성 문구, 원자료 요구 항목이 원고·메모·PDF에 있는지 기계가독 검증 | `status`, `check_count`, `scope`, `checks` |
| `outputs/objection_coverage_audit.csv` | 반론 커버리지 감사 행 1개 | 예상 심사 반론이 원고와 부속 메모에서 다뤄졌는지 스프레드시트에서 확인 | `objection`, `file`, `expected`, `actual`, `status` |
| `outputs/objection_coverage_audit.json` | JSON 반론 커버리지 감사 요약 | 한 쌍 반론, 2014 포함, 3쌍 대 5쌍, 사후탐색, 이질성, 자기선택, 드문 사건, 공식파일 한계, 대안 설명 반론의 커버리지 검증 | `status`, `check_count`, `scope`, `checks` |
| `outputs/pre_submission_audit.csv` | 제출 전 감사 행 1개 | 최종 체크리스트, 금지 표현, 개인정보 스캔, 영문 PDF/소스 번역, 증거표 참조, 핵심 검증 상태를 스프레드시트에서 확인 | `check`, `expected`, `actual`, `status` |
| `outputs/pre_submission_audit.json` | JSON 감사 요약 | 제출 전 감사 16개 항목의 기계가독 검증 결과 | `status`, `check_count`, `scope`, `checks` |
| `outputs/submission_integrity_report.md` | 무결성 리포트 1개 | PDF, 핵심 검증, 통계 강건성, 비공식 영상 출처 배제, 주장 범위 감사, 반론 커버리지, 제출 전 감사, 핵심 재현 수치를 한 파일에서 확인 | Markdown sections |
| `outputs/submission_integrity_report.json` | JSON 무결성 리포트 | 최종 ZIP self-hash를 제외한 제출 패키지 무결성 요약 | `status`, `core_claims_check_count`, `statistical_robustness_audit_check_count`, `video_source_exclusion_check_count`, `public_discussion_claims_audit_row_count`, `claim_boundary_audit_check_count`, `objection_coverage_audit_check_count`, `pre_submission_audit_check_count`, `korean_pdf`, `english_pdf`, `key_claims` |
| `outputs/zip_reproduction_audit.md` | 제출 ZIP 외부 재현 감사 리포트 1개 | 제출 ZIP을 임시 디렉터리에 풀어 핵심 감사 스크립트가 실행되는지 사람이 읽을 수 있게 요약. ZIP self-hash 순환을 피하려고 ZIP에는 넣지 않음 | Markdown sections |
| `outputs/zip_reproduction_audit.json` | 제출 ZIP 외부 JSON 재현 감사 리포트 | 제출 ZIP 독립 압축해제, 필수 파일 존재, 핵심 감사 스크립트 실행 결과의 기계가독 검증. ZIP self-hash 순환을 피하려고 ZIP에는 넣지 않음 | `status`, `required_extracted_files`, `commands` |
| `outputs/local_ci_validation_report.md` | 제출 ZIP 외부 로컬 CI 리포트 1개 | GitHub Actions 검증 워크플로와 같은 검증을 로컬에서 사람이 읽을 수 있게 요약. ZIP self-hash 순환을 피하려고 ZIP에는 넣지 않음 | Markdown sections |
| `outputs/local_ci_validation_report.json` | 제출 ZIP 외부 JSON 로컬 CI 리포트 | `validate_package.py`와 최종 ZIP sidecar 일치 여부의 기계가독 검증. ZIP self-hash 순환을 피하려고 ZIP에는 넣지 않음 | `status`, `validate_package`, `zip_sidecar` |
| `outputs/checksums_sha256.csv` | 패키지 파일 1개 | 제출 패키지 파일 무결성 확인 | `path`, `bytes`, `sha256` |
| `dist/election_duplicate_ieie_submission.zip.sha256` | 제출 ZIP 1개 | 제출 ZIP 자체의 SHA256 sidecar | `sha256  filename` |
| `dist/election_duplicate_ieie_submission_manifest.json` | JSON 제출 ZIP 요약 | 제출 ZIP 자체의 크기, SHA256, 내부 파일 수 확인 | `package`, `bytes`, `sha256`, `file_count` |

## 열 해석상 주의점

1. `units`는 항상 유권자 수가 아니라 분석에 포함된 개표단위 수를 뜻한다.
2. `comparison_pairs`는 개표단위끼리 만들 수 있는 비교쌍 수이며, 대체로 `N(N-1)/2` 형태이다.
3. `duplicate_groups`와 `collision_pairs`는 다르다. 전자는 반복된 값의 그룹 수이고, 후자는 실제 개표단위 쌍의 수이다.
4. `khat`은 자연상수가 아니라 과거 시·도지사 자료에서 역산한 경험적 가능한 득표쌍 범위이다.
5. `probability_percent`는 `probability`에 100을 곱한 값이다.
6. `sign_test_p_one_sided`는 사전투표 우위 방향이 한쪽으로 반복될 때의 단순 부호검정 값이며, 유권자 자기선택 같은 대안 설명을 제거하지 않는다.

## 재현 주장과 파일 대응

| 재현 주장 | 확인 파일 |
| --- | --- |
| 2026년 사건행 12개가 공식 HTML에서 재현된다. | `outputs/nec_2026_reported_duplicate_cases.csv`, `outputs/nec_2026_fetch_manifest.json` |
| 12개 사건행이 6개 동일 득표쌍을 이룬다. | `outputs/nec_2026_reported_duplicate_pairs.csv` |
| 광주·전남 관내사전 개표단위 수는 393개다. | `outputs/nec_2026_gwangju_jeonnam_units.csv`, `outputs/nec_2026_gwangju_jeonnam_unit_summary.json` |
| 과거 시·도지사 51개 선거구에서 한 선거구 안 최대 동일 득표쌍 수는 3쌍이다. | `outputs/governor_actual_top2_summary.csv`, `outputs/governor_actual_top2_by_contest.csv`, `outputs/governor_actual_top2_duplicates.csv` |
| 광주전남 5쌍 이상 반복의 포아송 근사 확률은 약 0.115%다. | `outputs/probability_core.csv`, `outputs/governor_actual_top2_summary.csv` |
| 같은 기준의 정확 pair-collision 확률은 약 0.122%다. | `outputs/probability_exact_collision.csv` |
| 과거 실제 득표쌍 풀의 비복원 재표본추출에서 5쌍 이상은 200,000회 중 0회다. | `outputs/governor_bootstrap_summary.csv`, `outputs/governor_bootstrap_histogram.csv` |
| 통계 결론은 포아송 근사, 정확계산, 민감도 분석, 비복원 재표본추출 점검에서 강건하다. | `outputs/statistical_robustness_audit.csv`, `outputs/statistical_robustness_audit.json` |
| 원고와 제출 문서는 비공식 동영상 플랫폼 기반 자료를 증거 출처로 사용하지 않는다. | `outputs/video_source_exclusion_audit.csv`, `outputs/video_source_exclusion_audit.json` |
| 송도 사례는 광주전남 핵심 검정과 분리된 보조 감사 신호다. | `outputs/songdo_official_rows.csv`, `outputs/songdo_probability_summary.csv` |
| 2020·2024 총선에서 분석 가능한 전 지역구가 같은 사전투표 방향성을 보인다. | `outputs/early_day_assembly_summary.csv`, `outputs/early_day_assembly_twoparty.csv` |
| 공개 논의에서 제기된 2022년 비산1동 한 쌍 사례는 공식자료로 확인되지만 광주전남 5쌍 검정에는 합산하지 않는다. | `outputs/public_discussion_claims_audit.csv`, `outputs/public_discussion_claims_audit.json` |
| 본문 핵심 수치 45개가 현재 산출물과 일치한다. | `outputs/core_claims_verification.csv`, `outputs/core_claims_verification.json` |
| 원고 출처 URL은 승인된 공식자료 또는 명시적 공개 보도 도메인을 사용한다. | `outputs/source_provenance_audit.csv`, `outputs/source_provenance_audit.json` |
| 원고의 법적·인과적 주장 범위와 원자료 감사 프레이밍이 통과한다. | `outputs/claim_boundary_audit.csv`, `outputs/claim_boundary_audit.json` |
| 예상 심사 반론이 원고와 부속 메모에서 커버된다. | `outputs/objection_coverage_audit.csv`, `outputs/objection_coverage_audit.json` |
| 최종 제출 전 감사 항목이 통과한다. | `outputs/pre_submission_audit.csv`, `outputs/pre_submission_audit.json` |
| 최종 PDF와 제출 무결성 요약이 서로 일관된다. | `outputs/submission_integrity_report.md`, `outputs/submission_integrity_report.json` |
| 제출 ZIP을 새 임시 디렉터리에 풀어 핵심 감사 스크립트를 다시 실행할 수 있다. | `outputs/zip_reproduction_audit.md`, `outputs/zip_reproduction_audit.json` |
| GitHub Actions 검증 워크플로와 같은 로컬 검증이 통과한다. | `outputs/local_ci_validation_report.md`, `outputs/local_ci_validation_report.json` |
| 제출 ZIP 자체의 SHA256과 내부 파일 수가 검증된다. | `dist/election_duplicate_ieie_submission.zip.sha256`, `dist/election_duplicate_ieie_submission_manifest.json` |

## 심사자에게 중요한 경계

이 데이터 사전은 산출물의 의미를 명확히 하기 위한 문서이지, 원인 확정 문서가 아니다. 위 파일들은 통계적 이상치와 감사 필요성을 재현하는 데 충분하지만, 특정 행위의 법적 확정에는 개표상황표 원본, 1차 분류기 결과, 재확인표 후보별 배분, 입력·수정 로그가 추가로 필요하다.
