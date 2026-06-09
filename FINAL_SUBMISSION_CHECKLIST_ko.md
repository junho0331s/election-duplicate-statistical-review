# 최종 제출 전 점검표

이 점검표는 학회 제출 직전에 원고와 재현 패키지가 같은 결론, 같은 숫자, 같은 한계를 말하는지 확인하기 위한 것이다.

검증 상태: 2026-06-09 KST 기준 `python3 scripts/run_all.py`와 `python3 scripts/validate_package.py` 통과. 핵심 주장 검증 파일 `outputs/core_claims_verification.json`은 `pass`, 45개 검증 항목을 기록한다. 통계 강건성 감사 파일 `outputs/statistical_robustness_audit.json`은 `pass`, 10개 검증 항목을 기록한다. 비공식 영상 출처 배제 감사 파일 `outputs/video_source_exclusion_audit.json`은 `pass`, 25개 파일 점검을 기록한다. 공개 논의 보조 주장 감사 파일 `outputs/public_discussion_claims_audit.json`은 `pass`, 공식자료 2개 행 검산을 기록한다. 주장 범위 감사 파일 `outputs/claim_boundary_audit.json`은 `pass`, 18개 검증 항목을 기록한다. 반론 커버리지 감사 파일 `outputs/objection_coverage_audit.json`은 `pass`, 26개 검증 항목을 기록한다. 제출 전 감사 파일 `outputs/pre_submission_audit.json`은 `pass`, 17개 검증 항목을 기록한다.

## 1. 주장 범위

- [x] 원고는 특정 개인, 기관, 정당의 범죄가 법적으로 확정되었다고 쓰지 않는다.
- [x] 결론은 "공개자료에서 통계적 이상치가 확인되며, 원자료 공개와 독립 감사가 필요하다"로 유지한다.
- [x] "우연가설 아래 매우 낮은 확률"과 "직접 부정행위 입증"을 구분한다.
- [x] 광주전남 5쌍은 주검정으로, 전국 6쌍과 송도 사례는 별도 또는 보조 관찰로 분리한다.
- [x] 사전투표-당일투표 분석은 보조 이상성 지표이며, 유권자 자기선택과 정당별 동원전략 같은 대안 설명을 제거하지 못한다고 명시한다.

## 2. 출처와 증거 정책

- [x] 원고와 부속문서에 비공식 영상 플랫폼 자료, 영상 전사문, 영상 기반 주장을 증거로 쓰지 않는다.
- [x] 2026년 사건행은 선관위 선거통계시스템 공식 HTML 캐시와 파싱 결과로 재확인한 값임을 밝힌다.
- [x] 과거 기준선은 공개 공식 선거자료와 공공데이터 파일에서 재현 가능해야 한다.
- [x] 언론 보도는 최초 사건 정의와 공개 논란의 맥락에만 사용하고, 핵심 수치 검증은 공식 화면값과 재현 스크립트에 연결한다.

## 3. 핵심 숫자 일치

제출 전 다음 값이 README, 한글 원고, 영문 원고, PDF, 계산 노트, 출력 CSV에서 같은지 확인한다.

| 항목 | 기준값 |
| --- | ---: |
| 과거 파싱 행 | 81,701 |
| 과거 시·도지사 선거구 | 51 |
| 실제 1·2위 비교쌍 | 1,514,172 |
| 실제 1·2위 동일 득표쌍 | 15 |
| 과거 한 선거구 안 최대 반복 | 3쌍 |
| 광주전남 관내사전 개표단위 | 393 |
| 경험적 \(K\) | 100,944.8 |
| \(P(C \ge 5)\), \(N=393\) | 0.0011484064, 약 0.115% |
| 정확 pair-collision \(P(C \ge 5)\), \(N=393\), \(K=100,945\) | 0.0012190884, 약 0.122% |
| \(P(C \ge 6)\), \(N=393\) | 0.0001432242, 약 0.0143% |
| 비복원 재표본추출 반복 수 | 200,000 |
| 비복원 재표본추출 \(C \ge 5\) | 0회 |
| 연수구 15개 단위 중 한 쌍 이상 확률 | 약 0.104% |
| 송도1동-송도2동 특정쌍 조건부 확률 | 약 0.000991% |
| 2026 공식 HTML 재확인 사건행 | 12 |
| 2026 공식 HTML 재확인 동일 득표쌍 | 6 |

## 4. 한글·영문 원고와 PDF

- [x] 한글 PDF `latex/ieie/main.pdf`가 최신 `latex/ieie/main.tex`보다 오래되지 않았다.
- [x] 영문 PDF `latex/en/main_en.pdf`가 최신 `latex/en/main_en.tex`보다 오래되지 않았다.
- [x] 영문 PDF는 전체 번역본이며 결론, 자료·코드 가용성, 연구윤리, 부록, 참고자료, 재현 산출물이 끝까지 들어 있다.
- [x] 영문 PDF 안에 한글 본문 조각이 남아 있지 않다.
- [x] 영문 원고의 사전투표-당일투표 표는 오래된 `2016년 118/111`, `about 0.35` 값을 쓰지 않는다.
- [x] 영문 원고는 최신 검산값인 2016년 211/18, 평균 +3.90%p, 2020·2024 전 지역구 방향 일치를 사용한다.

## 5. 원자료 한계와 감사 요구

- [x] 2026년 공식 통합 XLSX 파일 또는 개표상황표 원본이 아직 확보되지 않았다는 한계를 숨기지 않는다.
- [x] 이 한계가 결론을 "법적 확정"이 아니라 "원자료 감사가 필요한 통계적 이상치"로 제한한다고 명시한다.
- [x] `AUDIT_PROTOCOL_ko.md`와 `AUDIT_PROTOCOL_en.md`가 제출 패키지에 들어 있다.
- [x] 감사 프로토콜은 개표상황표, 1차 투표지분류기 결과, 재확인표 후보별 배분, 입력·수정 로그, 파일 해시를 요구한다.
- [x] 반증 기준을 포함한다. 원자료가 우연 또는 합법 절차로 설명하면 그 결론을 받아들이는 구조여야 한다.

## 6. 재현과 패키지 검증

제출 직전 다음 명령을 실행한다.

```bash
python3 -m pip install -r requirements.txt
python3 scripts/run_all.py
python3 latex/convert_to_ieie.py
cd latex/ieie
xelatex -interaction=nonstopmode -halt-on-error main.tex
xelatex -interaction=nonstopmode -halt-on-error main.tex
cd ../..
cd latex/en
xelatex -interaction=nonstopmode -halt-on-error main_en.tex
xelatex -interaction=nonstopmode -halt-on-error main_en.tex
cd ../..
python3 scripts/generate_checksums.py
python3 scripts/create_submission_zip.py
python3 scripts/validate_package.py
```

시간상 전체 재현을 다시 돌리지 못하는 경우에도 최소한 다음 명령은 반드시 통과해야 한다.

```bash
python3 scripts/validate_package.py
```

## 7. 제출 ZIP 구성

- [x] `dist/election_duplicate_ieie_submission.zip`이 최신 체크섬 파일보다 오래되지 않았다.
- [x] `dist/election_duplicate_ieie_submission.zip.sha256`와 `dist/election_duplicate_ieie_submission_manifest.json`이 제출 ZIP 자체의 해시와 파일 수를 기록한다.
- [x] ZIP 안에 한글/영문 원고, 한글/영문 PDF, 커버레터, 제출 메모, 심사자 반론 대응, 증거 매트릭스, 계산 노트, 자료 가용성 메모, 감사 프로토콜, 재현 스크립트, outputs, data가 들어 있다.
- [x] ZIP 안에 LaTeX 임시 파일 `.aux`, `.log`, `.out`, `.synctex.gz`가 들어 있지 않다.
- [x] ZIP 크기가 GitHub 권고치보다 클 수 있음을 알고, 필요하면 학회 제출용으로만 별도 업로드한다.

## 8. 제출 전 최종 문장 점검

제출 전 초록과 결론에서 다음 취지를 유지한다.

> 본 연구는 특정 부정행위의 법적 확정이 아니라, 공개 공식자료와 재현 가능한 계산에서 우연가설만으로 닫기 어려운 통계적 이상치가 확인되며, 이를 해소하려면 개표상황표 원본, 1차 분류기 결과, 재확인표 후보별 배분, 전산 입력·수정 로그의 독립 감사가 필요하다는 결론을 제시한다.

이 문장보다 강하게 "확정", "범죄", "조작"을 단정하는 표현은 학회 제출본에서 제거한다.
