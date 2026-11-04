# E5 — Iteration comparison: 0 → 1 (prompt v1.0 → v1.1-c)

*Standard document after each iteration: what we wanted, what we changed and why, what we got, whether it is what we wanted, what we do next. All numbers — from `iter_1/analysis/summary.md` and `figure_data/*.csv`; each number is traceable to a specific judge judgment.*

## 1. The short answer

**Partly yes.** Prompt v1.1-c is better than v1.0 by **+2.34 points** on average (85.9 → 86.2 on a 0–100 scale; one-to-one in the same pairs 83.9 → 86.2), and it passes the pre-fixed acceptance rule (29 §5.4). But the gain is **smaller than we forecast** (+3…+5), and in the pairwise comparison the judge picks the v1.1-c response as often as the v1.0 response (12 : 13 : 5). The improvement is real in three tasks (T02, T04, T06) and negative in one (T07). Of the five changes **two worked, two partly, one worked the opposite way** — and precisely because of that we now know what to fix in v1.2.

The main result, which does not change: with a prompt (any version) the model is **≈ +31 points** better than without a prompt (A) and **≈ +18** better than with a generic adviser prompt (B) — in 10/10 tasks, 30/30 pairs.

## 2. What we wanted to achieve with v1.1 (fixed before the data, `changes_v1.1.md`)

The iteration 0 error analysis showed where v1.0 loses points: (1) the first round of FULL mode (T04) — the model writes a full overview in 600–730 words with 5–8 questions, although the task requires ≤500 words and ≤5 questions; (2) external "facts" (EU rules, industry generalisations) without labelling; (3) T06 — when the user forbids questions, the model does not name the data that would narrow the range; (4) T03 — the tax debt is not reported first as an obligation; (5) T09 — the end of the lease is not assessed as a decision point.

Target: Δ(v1.1-c − v1.0) > 1.5 (noise band), CI lower bound > −1, criteria do not fall, violations do not increase. Forecast: +3…+5 points, of which ~2 from T04.

## 3. What we changed and why (5 changes, +9 % words, canon unchanged)

| ID | Why (error in iteration 0) | What we changed in the prompt | What we expected |
|---|---|---|---|
| CH1 | T04: FULL round too long, too many questions, full overview before the answers (in 12/12 judgments) | FULL round: ≤350 words + questions; overview sections wait for the answers; one question always — the refusal order; combine related questions | T04 68.9 → ≥85 |
| CH2 | T06: "zero questions" suppresses naming the data items (8/12) | R8: naming data items is not a question — express it as a statement even when questions are forbidden | T06 M7 8/12 → ≤2/12 |
| CH3 | Invented facts 0.79/response: external rules as certain facts | canon_gate: external knowledge with a condition in the same sentence ("in most EU countries …; check yours"), rules of thumb as "usually/often" | 0.79 → ≤0.45 |
| CH4 | T03: tax debt is not first (4/12) | PLAN CHECK: an obligation recorded as a goal is to be reported first as a constraint | T03 M3 4/12 → ≤1/12 |
| CH5 | T09: lease end is not a decision point (7/12) | New R14: a fixed date = a decision point with the price of both choices | T09 M5 7/12 → ≤3/12 |

## 4. What we got (iteration 1: 30 new v1.1-c responses, 120 judge judgments)

| Metric | Iter. 0: v1.0 | Iter. 1: v1.0 (the same responses, re-judged) | Iter. 1: **v1.1-c** | Better? |
|---|---|---|---|---|
| Overall score (0–100) | 85.9 | 83.9 | **86.2** | yes, +2.34 [−0.18; +4.58] |
| vs A (no prompt) | +30.6 | — | **+30.9** | unchanged, high |
| Tasks where better / worse than v1.0 | — | — | **8 / 2** | yes |
| Pairwise preference vs v1.0 (both orders) | — | — | **12 wins : 13 losses : 5 ties** | **no** — balance |
| Mandatory elements | 93 % | 91 % | **95 %** | yes |
| Violations per response | 0.28 (0.317 block 1) | 0.33 | **0.32** | do not increase |
| Invented facts per response | 0.79 | 0.57 | **1.01** | **no — worsened** |
| Criteria C1…C6 | 7.8 / 8.2 / 8.0 / 8.0 / 8.6 / 8.5 | 7.8 / 7.9 / 8.0 / 7.9 / 8.1 / 8.4 | 7.8 / 8.2 / 7.9 / 8.0 / 8.2 / 8.5 | none falls > 1.0 |
| Prompt length | 3,976 words | — | 4,333 (+9 %) | within the limit (≤ +15 %) |

By task (Δ v1.1-c − v1.0, in the same pairs): T02 **+7.5**, T04 **+6.2**, T06 **+6.2**, T03 +3.9, T08 +2.9, T09 +2.2, T10 +0.9, T05 +0.5, T01 −1.0, T07 **−6.1**.

Judge repeatability (checked by re-judging 9 pairs): preference agrees 9/9, overall score ±2.4 points per response — so +2.34 on the 10-task mean is above the noise, but not by much.

## 5. Did we achieve what we wanted? By change

| ID | Expected | Got | Verdict and why |
|---|---|---|---|
| CH1 | T04 ≥ 85 | T04 64.2 → **70.4**; words 731/585/690 → 522/570/505; questions 5–8 → 6–8 | **Partly.** Words decreased, but are still > 500: the prompt said "350 words *before* the questions", the questions added another 150–220. The number of questions did not change: the model understood "combine related ones" as 5 numbered blocks with sub-questions — the judge counts question marks (6–8). A wording error, not a model error. |
| CH2 | T06 M7 ≤ 2/12 | **0/12**; T06 +6.2 | **Succeeded.** |
| CH3 | invented facts ≤ 0.45 | **1.01** (was 0.57) | **Failed — the opposite.** The permission "in most EU countries …; check yours" was followed literally and *more often*: 1–3 such sentences in every response. The judge rubric does not regard "check yours" as labelling — it is still a claim without a source. Must be reverted. |
| CH4 | T03 M3 ≤ 1/12 | **0/12**; but a new loss M8 7/12 (the ending on the missing reserve squeezed out) | **Succeeded with a side effect.** The new content fitted in at the expense of the ending (646–682 of 700 words). |
| CH5 | T09 M5 ≤ 3/12 | **4/12**; T09 +2.2; T07 r2 418 > 400 words → T07 −6.1 | **Partly, with a side effect.** R14 also fired where the date is the person's own goal (teenager, 1 June), added sentences and exceeded the 400-word budget — exactly the side risk we had written down. |

**In total:** the acceptance rule is met (all four points), v1.1-c becomes the base — but with an open caveat that the gain is on average, not in every pair, and that one hypothesis (CH3) is rejected.

## 5b. At element level: what improved, what worsened (the same pairs, the same judge calls; omissions out of 6 judgments per task)

| Improved → **we keep** | v1.0 → v1.1-c | Source |
|---|---|---|
| T04 M5 refusal order among the questions | 6/6 → **0/6** | CH1 |
| T06 M7 data items that narrow the range | 4/6 → **0/6** | CH2 |
| T03 M3 tax debt as an obligation first | 4/6 → **0/6** | CH4 |
| T02 M4 cash flow in both numbers; T02 M2 | 4/6 → **0/6**; 2/6 → 0/6 | indirect (self_check) |
| T09 M5 lease end as a decision point | 5/6 → **2/6** | CH5 |
| T04 M8 length ≤500 | 6/6 → 4/6 | CH1 (partly) |
| T03, T08 violations | 2 → 0; 2 → 0 | — |

| Worsened → **we revert / fix** | v1.0 → v1.1-c | Cause | What we do in v1.2 |
|---|---|---|---|
| Invented facts per response | 0.57 → **1.01** | CH3 permission "check yours" | **CH3 reverted**, CH7 opposite rule |
| T07 violations (r2 > 400 words) | 0 → **4** | CH5 R14 + CH3 sentences | CH9 narrows R14; CH8 budget = ceiling |
| T03 M8 missing reserve + checks at the end | 0/6 → **5/6** | CH4 content squeezed out the ending | CH10 the ending is not shortened |
| T04 M4 ≤5 questions and nothing after them | 4/6 → **6/6** | CH1 "combine" → blocks with sub-questions | CH6 "5 = five question marks" |
| T04 M7, T07 M7, T10 M1 | 0 → 2/6 each | generalisations as facts (CH3) | CH7 |

## 6. What this teaches and what we do in v1.2 (awaiting Martin's approval)

Three causes account for almost all lost points, and all three are **prompt wording** that the judge rubric reads differently than the model does:

1. **The budget must be defined the way the rubric counts it** — in total, including the questions; "five questions" = five question marks. → CH6.
2. **External knowledge only in two forms** — as a check to perform ("check whether the contract allows…") or as a labelled assumption; never as a "usually/often" statement. CH3 reverted. → CH7.
3. **The budget is a ceiling, not a target** — finish 10–15 % below it; in the short modes (400 words) there is no margin for error. → CH8; R14 narrowed to dates set by others (→ CH9); the PLAN CHECK ending on the missing data must not be shortened (→ CH10).

Prompt v1.2-c: 4,487 words (+12.9 % vs v1.0; limit 15 % — 85 words remain; for iteration 3 the pack must be net-neutral). Forecast: +2…+3 points (86.2 → 88–89), invented facts ≤ 0.5, T04 ≥ 80, T07 back to ≥ 89.

## 7. Where the data are
`[local archive]\iter_1\` — `analysis/summary.md` (tables), `analysis/fig1…fig7.png` + `figure_data/` (the numbers behind the figures), `analysis/panel_iter_1.png` (the whole set in one figure), `judgments/` (120 judgments), `responses/` (30 responses), `error_analysis/` (error analysis, change pack v1.2 with an exact diff), `decisions.md` (13 decisions with rationale). The iteration 0 set is laid out in exactly the same way in `iter_0\`. After each subsequent iteration, this same document: `iter_N\comparison.md`.
