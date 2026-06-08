# Statistical Calculation Note

## Purpose

This note links the paper's core probability values to their formulas, inputs, scripts, and output files. The paper body provides interpretation; this note provides calculation traceability.

## 1. Poisson Approximation for Identical Vote-Pair Counts

Let \(N\) be the number of comparable in-district early-vote counting units within one contest environment, and let \(K\) be the effective range of possible top-two candidate vote pairs. The expected number of pair collisions is approximated by:

\[
\lambda = \frac{N(N-1)}{2K}.
\]

If the number of repeated identical vote pairs \(C\) can be treated as a rare collision count, then \(C\) can be approximated by a Poisson distribution with mean \(\lambda\):

\[
P(C \geq m) = 1 - e^{-\lambda}\sum_{c=0}^{m-1}\frac{\lambda^c}{c!}.
\]

The package's baseline values are:

| Symbol | Value | Source |
| --- | ---: | --- |
| \(N\) | 393 | Official NEC VCCP08 HTML: 96 Gwangju in-district early-vote units + 297 Jeonnam units |
| \(K\) | 100,944.8 | Effective vote-pair range inferred from 1,514,172 historical actual top-two comparisons and 15 identical vote pairs |
| \(\lambda\) | 0.7630705098231905 | `scripts/probability_sensitivity.py` |

Here \(N\) is not the number of reported event rows. It is the number of potential in-district early-vote counting units that could have produced repeated pairs within the same Gwangju-Jeonnam governor contest environment. The package parses all five Gwangju districts and twenty-two Jeonnam cities/counties from the official NEC VCCP08 HTML and counts non-aggregate in-district early-vote rows. The resulting files are `outputs/nec_2026_gwangju_jeonnam_unit_counts.csv` and `outputs/nec_2026_gwangju_jeonnam_unit_summary.json`.

\(K\) is calculated as:

\[
\hat{K} =
\frac{\text{historical actual top-two comparison pairs}}
     {\text{historical identical vote pairs}}
=
\frac{1,514,172}{15}
\approx 100,944.8.
\]

Substituting these values gives:

| Threshold | Probability | Check file |
| --- | ---: | --- |
| \(P(C \geq 3)\) | 0.04226077201454281 | `outputs/probability_core.csv` |
| \(P(C \geq 4)\) | 0.007734837111887716 | `outputs/probability_core.csv` |
| \(P(C \geq 5)\) | 0.0011484064248148407 | `outputs/probability_core.csv` |
| \(P(C \geq 6)\) | 0.00014322422035484283 | `outputs/probability_core.csv` |

Reproduction command:

```bash
python3 scripts/probability_sensitivity.py
```

## 2. Sensitivity to \(K\) and \(N\)

The Poisson approximation depends on the selected \(K\) and \(N\). The package therefore generates two sensitivity files:

| Sensitivity | Output file | Description |
| --- | --- | --- |
| Varying \(K\) | `outputs/probability_k_sensitivity.csv` | Holds \(N=393\) fixed and varies \(K\) from 50,000 to 500,000 |
| Varying \(N\) | `outputs/probability_n_sensitivity.csv` | Holds \(K=100,944.8\) fixed and varies \(N\) from 350 to 450 |

The purpose of this sensitivity analysis is to avoid overclaiming one exact probability value. Even under a conservative \(K=50,000\), which makes collisions easier, \(P(C \geq 5)\) is about 2.05%; the five-pair Gwangju-Jeonnam event does not become an ordinary background event.

## 3. Nonparametric Resampling From Historical Actual Vote Pairs

Because the Poisson approximation contains model assumptions, the package also performs an empirical resampling test using the historical actual vote-pair pool.

The procedure is implemented in `scripts/bootstrap_governor_duplicates.py`:

1. Construct actual top-two candidate vote pairs from 2014, 2018, and 2022 governor in-district early-vote rows.
2. Draw 393 vote pairs without replacement from the full historical pool of 10,322 vote pairs.
3. Count repeated vote-pair groups within the sample.
4. Repeat the procedure 200,000 times with fixed random seed `20260609`.

Results:

| Threshold | Hits | Empirical proportion | Conservative adjustment |
| --- | ---: | ---: | ---: |
| \(C \geq 3\) | 77/200,000 | 0.000385 | plus-one 0.0003899981 |
| \(C \geq 4\) | 4/200,000 | 0.00002 | plus-one 0.0000249999 |
| \(C \geq 5\) | 0/200,000 | 0 | plus-one 0.00000499998 |

Zero hits for \(C \geq 5\) does not mean the true probability is mathematically zero. The simulation resolution is \(1/200,000=0.000005\), and the rule-of-three 95% upper bound is \(3/200,000=0.000015\).

Check files:

- `outputs/governor_bootstrap_summary.csv`
- `outputs/governor_bootstrap_histogram.csv`

Reproduction command:

```bash
python3 scripts/bootstrap_governor_duplicates.py
```

## 4. Songdo Probability Calculation

The Incheon Songdo case is treated separately from the Gwangju-Jeonnam main test. It uses the Yeonsu official HTML and the same effective \(K=100,944.8\) baseline.

Key outputs:

| Quantity | Value | Check file |
| --- | ---: | --- |
| Yeonsu in-district early-vote units | 15 | `outputs/songdo_probability_summary.csv` |
| Probability of at least one identical pair among Yeonsu units | 0.0010396316588441312 | `outputs/songdo_probability_summary.csv` |
| Conditional probability that the specific Songdo 1/Songdo 2 pair matches | 0.000009906404292246851 | `outputs/songdo_probability_summary.csv` |

Reproduction command:

```bash
python3 scripts/analyze_songdo_probability.py
```

## 5. Interpretation Allowed by These Calculations

The calculations support the following statement:

> Taken together, the historical governor in-district early-vote baseline and the 2026 official page values indicate that the Gwangju-Jeonnam five-pair repetition is a statistical anomaly difficult to explain by ordinary chance.

The calculations do not, by themselves, establish the following statement:

> A specific actor, device, or input procedure intentionally produced the result.

Maintaining this distinction is the paper's central defensive boundary. The calculations support the need for audit, but causal attribution requires original counting statements, first-pass sorter outputs, reviewed-ballot allocation records, and electronic input logs.

