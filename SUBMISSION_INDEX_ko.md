# 제출 인덱스

이 문서는 심사자와 독립 검증자가 제출 패키지의 핵심 파일을 빠르게 찾기 위한 최상위 안내서이다. 결론의 범위는 통계적 이상치와 원자료 감사 필요성이다. 특정 행위자나 법적 책임을 이 문서만으로 단정하지 않는다.

## 1. 제출 패키지

- 제출 ZIP: `dist/election_duplicate_ieie_submission.zip`
- ZIP 해시 사이드카: `dist/election_duplicate_ieie_submission.zip.sha256`
- ZIP 매니페스트: `dist/election_duplicate_ieie_submission_manifest.json`

ZIP 해시는 ZIP 생성 이후 외부 사이드카 파일에 기록한다. ZIP 내부 문서에는 최종 ZIP 해시를 직접 쓰지 않는다.

## 2. 원고

- 국문 PDF: `latex/ieie/main.pdf`
- 영문 PDF: `latex/en/main_en.pdf`
- 국문 LaTeX: `latex/ieie/main.tex`
- 영문 LaTeX: `latex/en/main_en.tex`
- 국문 Markdown 원고: `paper_statistical_implausibility_ko.md`
- 영문 Markdown 원고: `paper_statistical_implausibility_en.md`

## 3. 심사용 안내 문서

- 핵심 주장-증거 대응표: `evidence_matrix_ko.md`, `evidence_matrix_en.md`
- 데이터 사전: `DATA_DICTIONARY_ko.md`, `DATA_DICTIONARY_en.md`
- 빠른 재현 안내: `REVIEWER_QUICKSTART_ko.md`, `REVIEWER_QUICKSTART_en.md`
- 재현성 점검표: `REPRODUCIBILITY_CHECKLIST_ko.md`, `REPRODUCIBILITY_CHECKLIST_en.md`
- 확률 계산 노트: `STATISTICAL_CALCULATION_NOTE_ko.md`, `STATISTICAL_CALCULATION_NOTE_en.md`
- 2026년 자료 가용성 메모: `data_availability_2026_ko.md`, `data_availability_2026_en.md`
- 원자료 감사 프로토콜: `AUDIT_PROTOCOL_ko.md`, `AUDIT_PROTOCOL_en.md`
- 대안 설명 매트릭스: `ALTERNATIVE_EXPLANATIONS_MATRIX_ko.md`, `ALTERNATIVE_EXPLANATIONS_MATRIX_en.md`
- 사후탐색 강건성 노트: `LOOK_ELSEWHERE_ROBUSTNESS_ko.md`, `LOOK_ELSEWHERE_ROBUSTNESS_en.md`
- 최종 제출 점검표: `FINAL_SUBMISSION_CHECKLIST_ko.md`, `FINAL_SUBMISSION_CHECKLIST_en.md`
- 공개 논의 보조 주장 검산: `PUBLIC_DISCUSSION_CLAIMS_ko.md`, `PUBLIC_DISCUSSION_CLAIMS_en.md`

## 4. 핵심 검증 산출물

- 핵심 주장 검증: `outputs/core_claims_verification.json` (`pass`, 45 checks)
- 통계 강건성 감사: `outputs/statistical_robustness_audit.json` (`pass`, 10 checks)
- 비공식 영상 출처 배제 감사: `outputs/video_source_exclusion_audit.json` (`pass`, 23 files)
- 출처 추적 감사: `outputs/source_provenance_audit.json` (`pass`, 24 URLs)
- 주장 범위 감사: `outputs/claim_boundary_audit.json` (`pass`, 18 checks)
- 예상 반론 포괄성 감사: `outputs/objection_coverage_audit.json` (`pass`, 22 checks)
- 제출 전 자동 감사: `outputs/pre_submission_audit.json` (`pass`, 15 checks)
- 공개 논의 보조 주장 감사: `outputs/public_discussion_claims_audit.json`
- 제출 무결성 보고서: `outputs/submission_integrity_report.json`
- 제출 인덱스 감사: `outputs/submission_index_audit.json`

## 5. ZIP 생성 후 외부 검증 산출물

- ZIP 독립 재현 감사: `outputs/zip_reproduction_audit.json`
- 로컬 CI 검증 보고서: `outputs/local_ci_validation_report.json`

이 두 산출물은 최종 ZIP을 만든 뒤 생성된다. 따라서 ZIP 내부 체크섬의 자기참조 순환을 피하기 위해 제출 ZIP 안에는 넣지 않고 외부 보고서로 보관한다.

## 6. 빠른 재현 명령

```bash
python3 -m pip install -r requirements.txt
python3 scripts/run_all.py
```

전체 재현이 성공하면 `outputs/`, `latex/`, `dist/`의 산출물이 다시 생성되고 `scripts/validate_package.py`가 제출 패키지 구조를 검증한다.

공개 논의 보조 주장은 `scripts/verify_public_discussion_claims.py`가 공식 2022년 대선 파일에서 별도로 검산한다.
