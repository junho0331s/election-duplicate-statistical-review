# Public-Discussion Claim Check Memo

This memo rechecks auxiliary claims that appear in public collaborative encyclopedia pages or online discussions against official data, then separates them from the paper's primary statistical test. Public collaborative encyclopedia pages are not used as evidentiary sources in the academic manuscript. The purpose here is only to identify checkable claims and verify them against official files.

## 1. Auxiliary Claim Checked

One public-discussion claim states that, in the 2022 Korean presidential election, Daegu Seo-gu Bisan 1-dong polling stations 3 and 4 gave the same vote counts to Lee Jae-myung and Yoon Suk-yeol: 131 and 618 votes, respectively.

## 2. Official-Data Check

Direct checking of `data/pres2022.xlsx` confirms the following two rows.

| Election | City | District | Polling station | Lee Jae-myung | Yoon Suk-yeol | Ballots cast | Registered voters |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| 2022 presidential | Daegu | Seo-gu | Bisan 1-dong polling station 3 | 131 | 618 | 787 | 1268 |
| 2022 presidential | Daegu | Seo-gu | Bisan 1-dong polling station 4 | 131 | 618 | 791 | 1263 |

This check is reproduced by `scripts/verify_public_discussion_claims.py` and `outputs/public_discussion_claims_audit.json`.

## 3. Interpretation in This Study

This is a real identical vote-pair case in official data. However, it is not at the same level as the paper's primary event.

- This case is an election-day polling-station case in a presidential election.
- The paper's primary event is five repeated identical pairs for the same candidate combination in in-district early-vote eup/myeon/dong counting units in a local governor election.
- This case is one identical pair, so it is not pooled into the Gwangju-Jeonnam five-pair probability calculation.
- It can be used as an honest auxiliary note acknowledging that identical pairs have appeared before.

## 4. Relevance to Reviewer Objections

This case matters because it prevents the paper from overstating the claim. Identical vote pairs have appeared before. Therefore the paper does not claim that one identical pair is impossible. The narrower claim is:

> Five repeated identical pairs inside the same contest, same vote type, and same candidate combination are statistically different from a historical one-pair example.

The 2022 Bisan 1-dong case therefore does not invalidate the primary conclusion. Instead, it helps explain why the paper separates one-pair events from five-pair concentration.
