# E5 — Iteration comparison: 1 → 2 (prompt v1.1-c → v1.2-c)

*Standard document after each iteration. Numbers from `iter_2/analysis/summary.md` and `figure_data/*.csv`; each number is traceable to a specific judge judgment.*

## 1. The short answer

**No — v1.2-c is worse than v1.1-c.** On average **−2.18** points [−5.88; +0.77]; in the pairwise comparison the judge picks v1.1-c **18 times, v1.2-c — 4 times** (8 ties). The acceptance rule (29 §5.4) **is not met** → v1.2-c rejected, **the base remains v1.1-c**.

But the iteration is not lost: one change did exactly what was needed, with a large effect — **invented facts 1.32 → 0.02 per response** (C1 accuracy 7.4 → 8.3), and two others worked (T04 form, T03 ending). The loss comes from two identified side effects, which v1.3-c fixes.

The main result does not change: with the canon and the prompt (any version) **+26…+31 vs no prompt, in 10/10 tasks** (v1.2-c vs A: 29/30 pairs).

## 2. What we wanted (changes_v1.2, fixed before the data)
Fix three v1.1-c causes: (1) the FULL round budget and the number of questions (T04), (2) CH3 "check yours" doubled the invented facts, (3) the word budget as a target, not a ceiling (T07, T03). Forecast +2…+3.

## 3. What we changed and why
| ID | Why | What we changed |
|---|---|---|
| CH6 | T04: 505–570 words, 6–8 "?" | FULL: 450 in total with the questions; 5 questions = 5 "?" |
| CH7 | invented facts 1.01 | external knowledge only as a check or a labelled assumption; generalisations about the market/clients out |
| CH8 | T07 418 > 400 | "the budget is a ceiling, finish 10–15 % below" |
| CH9 | R14 added text also for the person's own target dates | R14 only for dates set by others |
| CH10 | T03 M8 7/12 | the PLAN CHECK ending must not be shortened |

## 4. What we got (iteration 2: 30 new responses, 120 judgments)
| Metric | v1.1-c (the same responses, iter. 2) | **v1.2-c** | Better? |
|---|---|---|---|
| Overall score | 84.7 | **82.5** | **no, −2.18** |
| Pairwise preference | 18 wins | 4 wins (8 ties) | **no** |
| Invented facts / response | 1.32 | **0.02** | **yes, very much** |
| C1 accuracy | 7.4 | **8.3** | yes |
| C2 diagnosis | 8.2 | 7.6 | no |
| Elements | 93 % | 89 % | no |
| Violations / response | 0.33 | 0.53 | no (word budget) |
| vs A | +29.3 | +26.0 | both ≫ |

By task (Δ v1.2-c − v1.1-c): T04 **+3.5**, T09 +3.3, T03 +2.6, T08 +0.4, T10 −0.4, T01 −2.4, T06 −3.0, T05 −3.8, T07 −6.8, **T02 −15.3**.

## 5. Did we achieve it? By change
| ID | Verdict | Why |
|---|---|---|
| CH6 | **the form succeeded** (T04 F2/H2/M4/M8 → 0) | but M2/M7 disappeared — that is a CH7 side effect |
| CH7 | **target achieved too well** | invented facts → 0.02, but the model also dropped the risk hypotheses (T04 AI factor, T10 client insolvency, T02 food safety) |
| CH8 | **failed** | a sentence about length does not change length; new budget violations in T02, T05, T07, T08 |
| CH9 | **failed** | T07 is not shorter; T09 M5 slightly worse |
| CH10 | **succeeded** | T03 M8 6/6 → 0/6 |

### 5b. At element level
| Improved → **we keep** | v1.1-c → v1.2-c |
|---|---|
| T04 F2/H2/M4 (number of questions) | 6 → 0 |
| T04 M8 (length) | 4 → 0 |
| T03 M8 (ending) | 6 → 0 |
| T08 M4, M7; T09 M6; T10 M1 | 2 → 0 |
| Invented facts (all tasks) | 1.32 → 0.02 |

| Worsened → **we fix / revert** | v1.1-c → v1.2-c | What we do in v1.3-c |
|---|---|---|
| T04 M2, M7 (AI factor as a hypothesis) | 0→6, 1→6 | CH7b: risk hypotheses explicitly allowed |
| T10 M6 (client insolvency) | 2→6 | CH7b |
| T02 M2, M4 (safety, cash flow) | 0→2 | CH7b + CH11 |
| T02 F3/M8, T05 M9, T07 F2/M7, T08 M8, T06 H1 (word budget) | 0–2 → 2–6 | CH8 reverted; CH11 — lower internal numbers in L5 |
| T09 M5 | 2→4 | CH9 reverted |

## 6. What we do in v1.3 (awaiting Martin's approval)
v1.3-c = **v1.1-c + CH6 + CH7b + CH10 + CH11** (CH8, CH9 reverted). 4,455 words (+12.0 % vs v1.0). Forecast +1.5…+3 vs v1.1-c, invented facts ≤0.3. Details: `iter_2/error_analysis/changes_v1.3.md`.

**What this iteration teaches about prompt optimisation:** (1) a prohibition without an exception also throws out what is needed — every "don't do X" needs a "but do Y"; (2) a sentence about length does not change length, a number does; (3) measuring one change against one metric is cheaper than five at once — from iteration 3 onwards each change is tracked in its own element (table 5b).

## 7. Where the data are
`[local archive]\iter_2\` — `analysis/` (summary, fig1–fig7, figure_data, panel_iter_2.png, snapshots), `judgments/` (120), `responses/` (30), `error_analysis/` (error analysis, changes_v1.3.md/.json), `decisions.md`, `comparison.md`.
