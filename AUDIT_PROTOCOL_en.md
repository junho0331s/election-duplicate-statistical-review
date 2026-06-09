# Independent Raw-Data Audit Protocol

## 1. Purpose

This document is not designed to assert a legal conclusion from statistics alone. Its purpose is to turn the public statistical anomaly into a concrete raw-data audit question. It defines which records would distinguish ordinary chance, display error, data-entry error, reviewed-ballot processing, or another administrative explanation.

The audit questions are:

1. Do the official National Election Commission election-statistics page values match the original counting statements?
2. Are the differences between first-pass ballot-sorter results and final published values fully explained by counting statements and reviewed-ballot records?
3. Do the Gwangju-Jeonnam five-pair cluster and the Songdo pair reproduce from raw records under the same event definition?
4. Can the repeated identical vote pairs be explained by public-page display error, data-entry error, later correction, reviewed-ballot allocation, or another lawful procedure?
5. If unexplained discrepancies remain, can they be located by counting unit, candidate, and processing stage?

## 2. Audit Scope

The minimum audit scope is:

- the five Gwangju-Jeonnam in-district early-vote identical pairs in the governor contest, covering ten counting-unit rows;
- the Songdo 1-dong and Songdo 2-dong in-district early-vote identical pair in Yeonsu-gu, covering two counting-unit rows;
- comparison rows in the same contest environments: 393 Gwangju-Jeonnam in-district early-vote units and 15 Yeonsu-gu in-district early-vote units.

The expanded audit scope should include:

- every eup, myeon, or dong level counting-unit row in the same election, same candidate combination, and same in-district early-vote category;
- separated in-district and out-of-district early-vote results;
- candidate-level comparison tables against election-day voting;
- row-level reconciliation among the official integrated XLSX counting file, the election-statistics HTML pages, and the original counting statements.

## 3. Required Raw Records

An independent audit requires at least the following records.

| Record | Reason needed |
| --- | --- |
| Original counting statements | Check whether final published values match field records |
| First-pass ballot-sorter candidate results | Determine whether final identical pairs existed at first pass or emerged later |
| Reviewed-ballot counts | Explain the gap between first-pass and final values |
| Candidate allocation of reviewed ballots | Verify whether final equality was produced during review, as reported in Songdo |
| Invalid votes, abstentions, and third-candidate votes | Check whether only the top-two pair is identical while surrounding quantities differ |
| Counting-table and review-table logs | Locate the processing stage where candidate totals changed |
| Data-entry, correction, and publication logs | Check for input error, correction, or republishing |
| Sorter identifiers and batch identifiers | Test whether repetitions concentrate by equipment or batch |
| Ballot-box and counting-batch chain-of-custody records | Trace the equipment, timestamp, and review-table path for affected ballots |
| Observer objection records | Check whether concerns were raised during the count |
| File hashes and creation timestamps | Control for later alteration of audit materials |

Private voter-identifying information is not needed. The audit should rely on candidate-level totals, batch-level totals, logs, and counting-statement reconciliation.

## 4. Audit Procedure

### 4.1 Freeze the Event Definition

Before auditing, the following definitions must be fixed.

- Comparison unit: in-district early-vote counting-unit result
- Candidate rule: the actual first- and second-place candidates in the relevant contest
- Identical vote pair: two counting units sharing both the first-candidate count and the second-candidate count
- Gwangju-Jeonnam event: five repeated pairs in the same candidate combination and same vote type
- Songdo event: identical final top-two vote pair in Songdo 1-dong and Songdo 2-dong

These definitions must not be changed during the audit. If the definition changes, the count of events and the probability calculation change; that must be reported as a separate analysis.

### 4.2 Preserve Files and Hashes

For every audit file, record:

1. file name;
2. providing institution;
3. delivery timestamp;
4. file size;
5. SHA-256 hash;
6. whether it is an original file or a derived copy.

All subsequent analysis should be performed on read-only copies whose hashes have been recorded.

### 4.3 Reconcile Official Pages and Integrated Files

Match the following three sources row by row:

1. National Election Commission election-statistics HTML page values;
2. official integrated XLSX or CSV counting file;
3. original counting statements.

The matching keys should be election name, constituency, city/county/district, eup/myeon/dong, vote type, and candidate name. If candidate-name spellings differ, candidate ID or candidate number should be used as an auxiliary key.

### 4.4 Recalculate First-Pass to Final Differences

For each event row, compute:

\[
\Delta_i = F_i - S_i
\]

where \(S_i\) is candidate \(i\)'s first-pass ballot-sorter result and \(F_i\) is the final published value. Across all candidates, \(\sum_i \Delta_i\) must reconcile to the reviewed-ballot count.

If it does not reconcile, one of the following records is needed:

- additional manual count record;
- conversion from invalid to valid vote;
- conversion from valid to invalid vote;
- correction and republication history;
- data-entry correction log.

### 4.5 Verify Reviewed-Ballot Candidate Allocation

If final identical pairs emerged during the review stage, the core audit object is the candidate allocation of reviewed ballots. For each affected unit, produce this table.

| Unit | Candidate | First-pass result | Review-stage change | Final result | Raw-record match |
| --- | ---: | ---: | ---: | ---: | --- |
| Event row A | Candidate 1 |  |  |  |  |
| Event row A | Candidate 2 |  |  |  |  |
| Event row B | Candidate 1 |  |  |  |  |
| Event row B | Candidate 2 |  |  |  |  |

In a case like Songdo, where the first-pass values reportedly differed but the final values matched, the candidate-by-candidate path that produced identical final values must be documented.

### 4.6 Recompute Identical Vote Pairs

After raw-record reconciliation, recompute the event count using the same script rules.

1. Filter to in-district early voting.
2. Exclude aggregate and subtotal rows.
3. Create actual first- and second-place candidate vote pairs.
4. Find identical vote-pair groups within the same contest.
5. Check whether the Gwangju-Jeonnam five pairs and the Songdo pair remain.

If the official integrated file changes the event count, record the row-level cause of the difference.

## 5. Decision Criteria by Explanation

| Explanation | Evidence that weakens the anomaly | Evidence that strengthens the anomaly |
| --- | --- | --- |
| Public-page display error | Identical pairs disappear in original statements and integrated files | Original statements, integrated files, and HTML all show the same identical pairs |
| Simple data-entry error | Correction logs show before/after values and approval | Final identical pairs remain without correction logs |
| Reviewed-ballot processing | First-pass to final differences are fully explained by candidate-level reviewed-ballot allocation | Reviewed-ballot allocation is missing or does not reconcile |
| Low-probability chance | Auxiliary counts, batch logs, and surrounding quantities look independent and ordinary | Multiple pairs repeat the same candidate direction or processing-stage pattern |
| Post-search effect | A nationwide re-search under the same rules finds similar repetitions frequently | The same historical and nationwide re-search still finds five-pair clusters rare |
| Administrative/counting-process anomaly | Procedure logs are complete and all candidate changes reconcile | Repetitions concentrate by equipment, batch, timestamp, review table, or data-entry operator |

## 6. Falsification Criteria

The audit claim is weakened if:

1. the official integrated counting file or original counting statements differ from the current official HTML cache and the identical-pair repetition disappears;
2. the candidate-level path from first-pass ballot-sorter result to final published value is fully explained for every event row by reviewed-ballot records;
3. a broader raw-data reanalysis under the same event definition shows that five-pair clusters commonly occur in comparable elections;
4. a hierarchical model accounting for unit size, early-vote rate, candidate support, urban/rural status, and age structure places the Gwangju-Jeonnam five-pair cluster inside an ordinary predictive range.

The audit claim is strengthened if:

1. original counting statements, integrated files, and official HTML all show the same identical vote pairs;
2. first-pass results differ but identical pairs emerge during review or final data entry;
3. candidate-level reviewed-ballot allocation tables are missing or do not reconcile to the totals;
4. repetitions concentrate by equipment, timestamp, review table, data-entry operator, or batch;
5. independent reanalysis preserves the paper's historical-baseline and resampling conclusions.

## 7. Audit Outputs

The audit should publish at least:

- row-level raw-record reconciliation table;
- candidate-level first-pass to final change table;
- candidate allocation table for reviewed ballots;
- discrepancy list among official HTML, integrated file, and original counting statements;
- recomputed identical-vote-pair CSV;
- analysis scripts and execution logs;
- file-hash list for audit materials;
- ballot-box and counting-batch chain-of-custody reconciliation table;
- decision table by explanation.

## 8. Research Ethics and Disclosure Principle

The audit must not trace individual voter choices. It requires candidate-level totals, counting-unit totals, equipment/batch/timestamp logs, and publication-change history. Any internal document containing voter-identifying information should be redacted before publication.

Auditors should not predetermine the conclusion. If raw records explain the anomaly through ordinary chance or lawful administrative procedure, that conclusion should be accepted. If raw records fail to explain it, the remaining discrepancy should be reported by location, candidate, and processing stage. The purpose of this protocol is not to inflate a statistical anomaly into a political claim, but to separate what the raw records can explain from what remains unexplained.
