# E5 — Iteration comparison: iteration 0 (baseline measurement, prompt v1.0)

*Standard document after each iteration. Iteration 0 has no previous iteration, so the comparison is against both controls: A (no prompt) and B (general advisor prompt). Numbers from `iter_0/analysis/summary.md` and `figure_data/*.csv`; each number can be traced to a specific judge score. Document prepared on 2026-10-17 to align the structure, from the already frozen iteration 0 data (nothing was recalculated).*

## 1. The short answer

**Yes — canon + prompt v1.0 is considerably better than both controls.** C(v1.0) 85.9 vs A 55.3 and B 67.7. Paired difference C − A **+30.56** [+26.68; +34.36], C − B **+18.24** [+13.10; +23.39]; in both cases on 10/10 tasks. In the pairwise comparison, C beats A 30 times out of 30 and B 29 times out of 30.

Iteration 0 also sets the noise band: two independent blocks of the same v1.0 version differ on average by 0.00 pts, SE 0.75 → **band ±1.51 pts**. From now on a change is considered real only if it is outside this band (29 §5.4).

## 2. What we wanted (pre-registered, 29 §5)
1. Measure how much the canon + operating prompt gives vs the model without a prompt (A) and vs a general structured advisor (B).
2. Measure the measurement noise (v1.0 in two blocks), so that later iterations can distinguish a real improvement from chance.
3. Find where C loses points, and build the first change pack from that.

## 3. What we changed and why
Nothing. v1.0 is the user's 2026-10-13 prompt without changes (`prompt/02b_v1.0.md`), canon v1.0 (`02a_canon_v1.0.md`). This is the baseline.

## 4. What we got (120 responses: A 30, B 30, C-v1.0 60; 120 judgments)
| Measure | A (no prompt) | B (general prompt) | **C (canon + v1.0)** |
|---|---|---|---|
| Total score (0–100) | 55.3 | 67.7 | **85.9** |
| Mandatory elements | 54% | 66% | **93%** |
| Violations / response | 1.07 | 0.97 | **0.28** |
| Invented facts / response | 1.72 | **0.70** | 0.79 |
| C1 accuracy | 7.0 | 7.8 | 7.8 |
| C2 diagnosis | 6.6 | 7.0 | 8.2 |
| C3 practicality | 5.9 | 7.7 | 8.0 |
| C4 fit | 6.4 | 6.7 | 8.0 |
| C5 control | 3.9 | 6.0 | **8.6** |
| C6 honesty | 6.1 | 8.1 | 8.5 |
| Pairwise wins of C vs … | 30/30 | 29/30 | — |

The largest difference is in C5 "control" (8.6 vs 6.0 and 3.9) and in the mandatory elements (93% vs 66%): the contribution comes from the model's content, not only from a structured form (B shows this).

## 5. Did we achieve it? Where C loses points
| # | Task → requirement | How often | Class | What to do |
|---|---|---|---|---|
| 1 | **T04 FULL round 1** — length (M8, H1 12/12), number of questions (M4/F2 6/12, H2 8/12), AI factor (M7 6/12) | systemic | missing rule + contradiction | a word budget for the FULL round and ≤5 questions |
| 2 | **Invented facts** 0.79/response (T08 C1 6.9) | widespread | contradiction between rules | external knowledge only with a condition |
| 3 | **T06** M7 (data items that narrow the range) 8/12 | often | contradiction | name the data items as a statement |
| 4 | **T09** M5 (end of the lease as a decision point) 7/12 | often | missing rule | new rule on the decision point |
| 5 | **T03** M3 (tax debt as a constraint, first) 4/12 | sometimes | rule not followed | PLAN CHECK: the obligation first |
| 6 | T02 M4 (cash flow), T10 M6 (client insolvency) | sometimes | budget | postponed to a later iteration |

### 5b. What not to change (works)
| Task | Why keep it |
|---|---|
| T01, T05, T07 (90+) | EMERGENCY / QUICK / the teenager format works; the jargon problem does not appear on Sonnet (T07 H5 0 violations) |
| C5 control 8.6; elements 93% | the core of the model — do not touch |

## 6. What we do in v1.1 (tested in iteration 1; Martin approved v1.1-c as the base on 2026-10-16 19:13 Toronto after the iteration 1 results)
v1.1-c = v1.0 + **CH1** (FULL round: budget, ≤5 questions, the refusal order one of them) + **CH2** (data items as a statement) + **CH3** (external knowledge with a condition) + **CH4** (obligation first in PLAN CHECK) + **CH5** (decision point with a date, R14). 4,333 words (+9.0% vs v1.0). Forecast +3…+5 pts. Details: `iter_0/error_analysis/changes_v1.1.md`, text changes: `changes_v1.1.diff`, `changes_v1.1.json`.

## 7. Where the data is
`[local archive]\iter_0\` — `analysis/` (summary, fig1–fig7, figure_data, panel_iter_0.png, snapshots), `judgments/` (111 judgment texts + bundle; the prose of 9 texts was lost on 16 October, their numbers are preserved in the snapshot — see `judgments/INDEX.csv`), `judgments_rejudge/` (12 re-judgments, test–retest), `judgments_J2_gemini/`, `responses/` (120), `packs/` (gen 120, judge 120), `error_analysis/`, `decisions.md`.
