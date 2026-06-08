# Robustness Note on Post-Search and Multiple-Comparison Objections

## 1. Purpose

This note addresses the strongest statistical objection to the identical-vote-pair analysis: the post-search or look-elsewhere problem. The key point is that not all low probabilities should be interpreted with the same force. The defensible structure of the study is layered:

1. Gwangju-Jeonnam internal five-pair cluster: primary test
2. Incheon Songdo identical pair: separate auxiliary case
3. Nationwide twelve event rows and six duplicate pairs: background event definition and audit scope
4. Early-vote versus election-day vote-share difference: separate auxiliary anomaly indicator

This distinction does not weaken the paper. It separates claims that are vulnerable to post-search objections from claims that remain stronger under a narrower event definition.

## 2. What Is the Look-Elsewhere Problem?

The look-elsewhere problem arises when many datasets, offices, candidates, vote types, and regions are searched, and the most striking result is then treated as if it had been specified in advance. If the event is defined as "some identical vote pair somewhere in the country," the number of discovery opportunities is very large. In that setting, a single-comparison probability can exaggerate rarity.

For this reason, the paper does not use the entire nationwide twelve-row set as the main probability event. The nationwide set is used as context and audit scope.

## 3. Why the Gwangju-Jeonnam Five-Pair Cluster Is the Primary Test

The Gwangju-Jeonnam five-pair event is narrowed by the following conditions:

- same election: the 2026 local-election governor race;
- same vote type: in-district early voting;
- same candidate combination: Min Hyung-bae and Lee Jung-hyun;
- same regional contest environment: Gwangju-Jeonnam governor election;
- same comparison unit: eup, myeon, or dong level in-district early-vote counting units;
- same event definition: two units share both the first-candidate count and second-candidate count.

Therefore the Gwangju-Jeonnam five-pair cluster is not "one pair found somewhere after scanning everything." It is five repeated collisions within the same defined structure. The use of \(N=393\) and \(K=100,944.8\) is designed to calculate rarity within that structure: the number of comparable counting units in Gwangju-Jeonnam and the empirical collision rate inferred from historical governor contests.

## 4. Claims That Need Different Levels of Adjustment

| Claim | Need for post-search adjustment | Treatment in this study |
| --- | --- | --- |
| Identical votes appeared in twelve places nationwide | High | Background event and audit scope |
| Simple probability of six nationwide pairs | High | Reference value, not main conclusion |
| Conditional probability for the specific Songdo 1-dong/Songdo 2-dong pair | Medium | Auxiliary calculation if the pair is treated as specified |
| Probability of at least one pair among fifteen Yeonsu units | Medium | Auxiliary Songdo audit signal |
| Gwangju-Jeonnam internal five-pair cluster | Relatively lower | Primary test |
| Historical maximum of three pairs within one governor contest | Low | Empirical baseline |
| Zero five-pair hits in 200,000 nonparametric resamples | Low | Model-reducing auxiliary check |

"Relatively lower" does not mean no adjustment is ever relevant. It means the event definition is narrowed to the same candidate pair, same vote type, and same contest environment, so the discovery space is much smaller than a nationwide all-office search.

## 5. Interpreting a Simple Bonferroni-Style Bound

A simple way to think about multiple comparisons is the Bonferroni upper bound. If a single event has tail probability \(p\), and there are \(M\) independent search opportunities, then:

\[
P(\text{at least one hit}) \le M p
\]

The baseline Gwangju-Jeonnam five-pair probability is approximately \(p=0.001148\). If this value is multiplied by every possible nationwide search opportunity, the adjusted probability can quickly become large. That is why the paper does not make a strong nationwide probability claim from this number alone.

However, the appropriate \(M\) for the Gwangju-Jeonnam internal event is not "all possibilities nationwide." It is the number of comparable candidate-pair, vote-type, and contest environments under the same event definition. This is why the paper uses the 51 historical governor contests as the empirical benchmark. Within that benchmark, the maximum repeated-pair count in one contest is three, and five or more pairs are not observed.

The conservative interpretation is:

- the simple nationwide twelve-case probability should not be asserted without post-search adjustment;
- the Gwangju-Jeonnam five-pair cluster remains above the historical maximum under the same structural definition;
- the historical baseline and nonparametric resampling reduce the force of the post-search objection.

## 6. Why "One Pair Somewhere" and "Five Pairs in One Structure" Are Different

One identical pair somewhere in national data is not strong evidence, because there are many discovery opportunities. The paper's primary test is not one pair. It is five pairs.

Let \(C\) be the number of identical vote-pair collisions. The primary test is not:

\[
P(C \ge 1)
\]

It is:

\[
P(C \ge 5)
\]

Under \(N=393\) and \(K=100,944.8\), \(P(C \ge 1)\) is about 53.37%, which is common. By contrast, \(P(C \ge 5)\) is about 0.115%. Therefore the objection that identical pairs can occur is correct but incomplete. It does not explain five repeated pairs in the same defined contest structure.

## 7. Safe Interpretation of the Songdo Case

The conditional probability of approximately 0.000991% for Songdo 1-dong and Songdo 2-dong is valid only if those two units are treated as the specified pair of interest. If the case is treated as discovered after a nationwide search, that number cannot be used as a nationwide conclusion without adjustment.

The safe interpretation is:

- Songdo is not added to the Gwangju-Jeonnam five-pair probability calculation.
- Songdo is treated as a separate low-probability auxiliary observation.
- The key issue is not only the final identical pair, but how first-pass results and reviewed-ballot allocation produced the final equality.
- Songdo strengthens the request for candidate-level reviewed-ballot allocation records.

## 8. Final Response to the Reviewer Objection

Expected objection:

> If the cases were found after searching nationwide, the low probability is meaningless.

Response:

1. The paper does not use the nationwide twelve-row set as the main probability conclusion.
2. The primary test is the internal Gwangju-Jeonnam five-pair cluster.
3. That event is defined within the same candidate combination, same vote type, and same contest environment.
4. In 51 historical governor contests, the maximum repeated-pair count within one contest is three.
5. In 200,000 nonparametric resamples from actual historical top-two pairs, five or more pairs occur zero times.
6. Therefore the post-search objection weakens the nationwide headline, but it does not eliminate the conclusion that the Gwangju-Jeonnam five-pair cluster is a statistical anomaly requiring raw-data audit.

## 9. Conclusion

The robust conclusion is not: "a low-probability event appeared somewhere nationwide, therefore misconduct is proven." The robust conclusion is:

> The nationwide reported cases are vulnerable to post-search objections, but the Gwangju-Jeonnam internal five-pair cluster is an upper-tail event within the same candidate combination, same in-district early-vote type, and same governor-contest environment. The historical official-data baseline and nonparametric resampling do not treat this event as ordinary background noise. It therefore remains a statistical anomaly requiring raw-data disclosure and independent audit.

This conclusion is a statistical basis for audit, not a legal finding.
