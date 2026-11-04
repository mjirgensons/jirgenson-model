# E5 — Iteration comparison: 2 → 3 (prompt v1.3-c vs base v1.1-c)

*Standard document after each iteration. Figures from `iter_3/analysis/summary.md` and `figure_data/*.csv`; every figure is traceable to a specific judge evaluation. The comparison is against the **last accepted** version v1.1-c (iter. 1 responses, re-judged in this iteration), not against v1.2-c, rejected in iter. 2.*

## 1. Short answer

**Yes — v1.3-c is better than v1.1-c.** On average **+4.38** points [+1.97; +7.47], **in all 10 tasks**, Wilcoxon p = 0.002. The acceptance rule (29 §5.4) is **met on all four points** → v1.3-c can become the new base (takes effect upon Martin's approval).

This is the first result in the experiment that is clearly outside the noise band (±1.51) and whose CI does not include zero. It was achieved by **violations disappearing completely (0.35 → 0.00)** and **invented facts almost completely (1.20 → 0.11)**, without losing mandatory elements (94 % → 97 %).

Two caveats: (1) in the pairwise comparison the judge chooses v1.3-c **15 times, v1.1-c — 10** (5 ties) — a clear but not convincing advantage; v1.1-c wins where its longer responses calculate the worst case more deeply (T06, T08); (2) the remaining losses are so small that the next change pack most likely can no longer demonstrate an improvement with this task set (see §6).

The main result is unchanged: with canon and prompt **+33.0 vs no prompt** [+27.8; +38.4], in 10/10 tasks, 30/30 pairs.

## 2. What we wanted (changes_v1.3, fixed before the data)
Keep the iteration 2 gains (disappearance of invented facts, T04 form, T03 closing) and fix two v1.2-c side effects: (1) risk hypotheses, which CH7 threw out together with generalisations; (2) word-budget violations, which the sentence about length did not change. Prediction +1.5…+3 vs v1.1-c; invented facts ≤0.3; violations ≤0.25.

## 3. What we changed and why (v1.3-c = v1.1-c + CH6 + CH7b + CH10 + CH11; CH8, CH9 reverted)
| ID | Why | What we changed |
|---|---|---|
| CH6 | T04 v1.1-c: 488–554 words, 6–8 "?" | FULL round: five questions = five "?"; the whole round under budget |
| CH7b | v1.1-c invented facts 1.01–1.32; v1.2-c CH7 also threw out risk hypotheses | external knowledge only as a check or a labelled assumption **+** plausible risks remain as hypotheses with a check action |
| CH10 | T03 M8 (closing cut off) | the PLAN CHECK closing must not be shortened |
| CH11 | the sentence "finish 10–15 % below" did not change length | the numbers themselves changed in L5: internal ceilings ≈10 % below the person's limit |

4,455 words (+12.0 % vs v1.0). sha256 693dd23c…

## 4. What we gained (iteration 3: 30 new responses, 120 evaluations)
| Measure | A (no prompt) | v1.1-c (the same responses, iter. 3) | **v1.3-c** | Better? |
|---|---|---|---|---|
| Total score | 55.9 | 84.5 | **88.9** | **yes, +4.38** |
| Pairwise preference vs v1.1-c | — | 10 wins | **15 wins** (5 ties) | yes, moderately |
| Violations / response | 0.98 | 0.35 | **0.00** | **yes** |
| Invented facts / response | 1.72 | 1.20 | **0.11** | **yes** |
| Mandatory elements | 54 % | 94 % | **97 %** | yes |
| C1 accuracy | 6.9 | 7.3 | **8.5** | yes |
| C2 diagnosis | 6.8 | 8.2 | 8.1 | ≈ (−0.1) |
| C3 practicality | 6.0 | 8.0 | 8.0 | = |
| C4 fit | 6.4 | 7.8 | **8.6** | yes |
| C5 control | 4.0 | 8.0 | 8.3 | yes |
| C6 honesty | 6.1 | 8.2 | **8.7** | yes |

By task (Δ v1.3-c − v1.1-c): **T04 +15.9**, T07 +8.3, T10 +6.2, T03 +4.8, T01 +1.8, T05 +1.8, T08 +1.8, T09 +1.2, T06 +1.1, T02 +0.8 — **all positive**.
Robustness check (only the 60 calls in which both versions were judged together): Δ +3.45 [+0.90; +6.53], 8/10 — also meets §5.4.
**§5.4:** (1) Δ 4.38 > 1.51 and CI lower bound +1.97 > −1 ✓; (2) no criterion falls by > 1.0 ✓ (C2 −0.08); (3) violations do not increase ✓ (0.35 → 0.00); (4) length +12.0 % ≤ +15 % ✓. Hold-out was not measured in this iteration (optional in the protocol; D0.9).

Version history (each in its own iteration; the judge level fluctuates slightly between iterations, so versions are comparable only within one iteration): v1.0 85.9 → v1.1-c 86.2 → v1.2-c 82.5 (rejected) → **v1.3-c 88.9**.

## 5. Did we achieve it? By change
| ID | Verdict | Why |
|---|---|---|
| CH6 | **succeeded** | T04 number of questions and length: 0 violations (v1.1-c 6/6); T04 +15.9 |
| CH7b | **succeeded on 4 of 5 targets** | invented facts 0.11; T04 M2, T10 M6, T02 M2 recovered; **T04 M7 not** — the example in the prompt ("a market shift that may affect the main client") narrowed the hypothesis to a single client |
| CH10 | **succeeded** | T03 M8 6/6 → 0/6 |
| CH11 | **succeeded** | 0 budget violations in all 120 evaluations; elements did not decrease. Side effect: responses 10–15 % shorter, and in some tasks the judge, in pairs, prefers v1.1-c's deeper worst-case calculation |

### 5b. At element level (6 shared evaluations, v1.1-c → v1.3-c)
| Improved → **we keep** | v1.1-c → v1.3-c |
|---|---|
| T04 F2/H2/M4 (number of questions) | 6 → 0 |
| T04 M8, H1 (length) | 4 → 0 |
| T03 M8 (closing) | 6 → 0 |
| T07 F2/H1 (length), T08 M7, T10 M1 | 2 → 0 |
| T09 M6, H6; T06 M4 | 1 → 0 |
| Invented facts (all tasks, the same calls) | 1.20 → 0.07 |
| Violations (all tasks) | 0.35 → 0.00 |

| Worsened or unchanged → **we fix in v1.4-c (draft)** | v1.1-c → v1.3-c | What we do |
|---|---|---|
| T04 M7 (AI factor across the whole market, not only at the client) | 2 → 6 | CH12: example "a shift in their whole market, not only at their main client" |
| T09 M5, M7 (exit as an option before the lease decision) | 1 → 3, 0 → 2 | CH13: R14 + "orderly exit among the options; which mistake costs less" |
| T02 M4 (cash-flow low point) | 0 → 2 | CH14: R2 + "show the lowest balance and its day" |
| T08 M3/M4, T03 M1 (one response each) | 0 → 2 | not fixed (not systemic) |
| Worst-case depth T06/T08 (pairs), C2 −0.27 in the shared calls | — | not fixed (CH11 gain is larger); monitor |

## 6. What we do next — **decision for Martin** (nothing is started without it)
1. **v1.3-c as the new base** — §5.4 met mechanically; Martin's "yes" is needed (as for v1.1-c on 16.10.).
2. **The v1.4-c pack is prepared but is not being generated** (`iter_3/error_analysis/changes_v1.4.md/.json/.diff`; `02b_v1.4-c.md` sha256 d153e545…, 4,496 words, +13.1 % vs v1.0). It fixes three narrow causes. **Prediction +0.5…+1.2 — below the noise band ±1.51.** With 10 tasks × 3 replicates even a working pack will most likely not meet §5.4(1); two such iterations in a row trigger the protocol's stopping rule (a).
3. Therefore, before iteration 4 it is worth choosing one of:
   - **(A) iteration 4 with v1.4-c**, as planned (measures at element level; in the total score most likely noise);
   - **(B) hold-out set (hold-out H01–H10) now** — the protocol provides for it in iteration 3 as optional (29 §2.4; stopping rule (b) §2.5); it is the only test not yet performed and answers whether the v1.3-c gain is not an adaptation to the 10 tasks;
   - **(C) straight to the final round** with v1.3-c as the final candidate (hold-out + 3 confirmation models + J2).
   My recommendation: **(B)**, because the development set is approaching the ceiling (elements 97 %, violations 0), and the next most informative answer is about transferability, not about yet another small fix.

**What this iteration teaches about prompt optimisation:** (1) "what improved — we keep, what worsened — we revert" works: the three changes kept from v1.2-c and the two fixed ones gave +4.4 after −2.2; (2) a number in the prompt changes behaviour, a sentence about it does not (CH11 vs CH8); (3) an example in a rule is read literally and can narrow the rule itself (CH7b → T04 M7); (4) after violations and invented facts are eliminated, the remaining errors are narrow, and this measurement no longer distinguishes small improvements.

## 7. Where the data are
`[local archive]\iter_3\` — `analysis/` (summary, fig1–fig4, fig6, fig7, figure_data, panel_iter_3.png, snapshots), `judgments/` (120), `responses/` (30), `packs/` (gen 30, judge 120), `hardchecks/`, `error_analysis/` (error analysis, raw tables for v1.3-c and for the base v1.1-c, changes_v1.4.md/.json/.diff), `decisions.md`, `comparison.md`. J2 (Gemini) material: `cross_check/judge_calibration_and_J2/j2_gemini/iter_3/`.
