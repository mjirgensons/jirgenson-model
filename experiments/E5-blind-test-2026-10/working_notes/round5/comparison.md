# E5 — Iteration comparison: 3 → 5 (prompt v1.5-c vs base v1.3-c)

*Standard document after each iteration. Numbers from `iter_5/analysis/summary.md`, `figure_data/*.csv`, `iter5_d54_check.txt` and `iter5_context_check.txt`; every number is traceable to a specific judge judgment. Base: v1.3-c (iter. 3 responses, re-judged in this iteration in the same judge calls).*

## 1. Short answer

**Formally yes; in substance — "neutral, not worse", with clear accuracy gains.** The pre-registered acceptance rule (29 §5.4 / D5.4) is **met on all four points** on the primary measure: v1.5-c **+1.71** points [+0.23; +3.36] vs v1.3-c, better in 6 tasks / worse in 3 / equal in 1. But the robustness check on shared calls only (the same 60 judge sessions, both versions together) gives **+0.86** [−0.66; +2.43] — within the noise band (±1.51), and in the pairwise comparison the judge chooses v1.5-c **14 times, v1.3-c — 13** (3 split; sign test p = 1.0). The difference between the two measures is a **systematic measurement bias** (§5): a C response judged next to A receives a score higher by +1.1…+2.7, and the primary measure carries this only for the version under test.

What has been securely achieved (does not depend on context): **invented facts 0.11 → 0.008** (1 flag in 120 judgments; v1.3-c in the same calls 0.22), **violations 0.02 → 0.00**, elements 95 → 97 %, **T09 M5 and T02 M4 are no longer missing in any judgment** (were 10/18 and 6/18), **T04 M7 18/18 → 6/12**. Vs A: **+32.5** [+26.6; +38.5], in 10/10 tasks, 30/30 pairs (v1.3-c iter. 3: +33.0).

What got worse: **T09 M3** (the shrinking town as the strongest force) missing 11/12 — a new, systematic loss, a side effect of R1 strictness (D5.5 risk 1); **T05 0/3 pairs** (the danger formulated as "one weak month", which the person's own numbers refute); C6 honesty −0.05 (in shared calls −0.32), C4 −0.22 — within limits.

## 2. What we wanted (fixed before data, D5.3–D5.5)

Martin's goal (28.10.): maximum on all points, **especially invented facts → almost zero**, changing the prompt systemically. Forecast: Δ +1.5…+3.0; invented facts 0.00–0.03; pairs ≈ 18 : 7 : 5; T04 M7 ≤ 4/12, T09 M5 ≤ 3/12, T02 M4 0/12. Rule D5.4: (1) Δ > 1.51 and CI lower bound > −1; (2) no criterion drops > 1.0; (3) violations do not increase (one-to-one); (4) length ≤ +15 % vs v1.0.

## 3. What we changed (v1.5-c = v1.3-c + 41 replacements, `changes_v1.5.md`)

Three systemic axes, each with a rule + thinking step + self-check line: **A evidence discipline** (R1: only fact / shown arithmetic / labelled assumption; R2: no inferred dates; the prompt's internal "usually" sources fixed; final re-read sentence by sentence); **B forecast depth** (R13 to the red line and to zero with months; R8 funding includes start-up losses; R12 danger with amount and months, obligations ranked); **C usefulness of actions and choice** (R7 day and person, decision made, written demand today; R14 exit as an option; **R15** direct instruction overrides format; market-scale check in step 8). Length 4,570 words (+2.6 % vs v1.3-c; **+14.9 % vs v1.0**, limit 4,572) — duplicated text shortened (CL bank, L1/L3a, R10 removed), examples kept.

## 4. What we gained (iteration 5: 30 new responses, 120 judgments)

| Metric | A (no prompt) | v1.3-c (the same responses, iter. 5) | **v1.5-c** | Better? |
|---|---|---|---|---|
| Overall score (all judgments) | 56.2 | 87.1 | **88.8** | yes, +1.71 [+0.23; +3.36] |
| Overall score (shared calls only) | — | 87.1 | 87.9 | +0.86 [−0.66; +2.43] — in noise |
| Pair preference vs v1.3-c | — | 13 wins | **14 wins** (3 split) | tie |
| Pair preference vs A | — | — | 30/30 | yes |
| **Violations / response** | 1.05 | 0.02 | **0.00** | yes |
| **Invented facts / response** | 1.70 | 0.22 | **0.008** | **yes** |
| Mandatory elements | 55 % | 95 % | **97 %** | yes |
| C1 accuracy | 6.8 | 8.2 | **8.7** | yes (+0.46) |
| C2 diagnosis | 6.8 | 7.9 | 8.0 | +0.12 |
| C3 practicality | 5.9 | 7.7 | **8.3** | yes (+0.54) |
| C4 fit | 6.4 | 8.6 | 8.4 | −0.22 |
| C5 control | 4.2 | 8.1 | 8.3 | +0.15 |
| C6 honesty | 6.4 | 8.5 | 8.5 | −0.05 |
| Hard checks (33 turns) | — | 33/33 | 33/33 | = |
| Words / response (judge count) | 501 | 461 | 454 | shorter |

**By task** (A / v1.3-c / v1.5-c; Δ primary; Δ shared calls): T01 67.7 / 91.0 / 91.0 (0.0; −0.5) · T02 46.8 / 87.8 / 89.2 (+1.4; +2.0) · T03 59.5 / 87.5 / 86.9 (−0.6; −2.5) · **T04 34.3 / 80.8 / 85.2 (+4.4; +4.0)** · T05 58.8 / 91.5 / 90.0 (−1.5; −2.4) · T06 55.7 / 90.2 / 90.6 (+0.4; +0.2) · T07 67.7 / 90.2 / 89.8 (−0.4; −1.3) · **T08 54.0 / 84.2 / 90.3 (+6.1; +4.5)** · T09 67.2 / 83.2 / 84.8 (+1.6; +0.7) · **T10 50.8 / 84.2 / 89.7 (+5.5; +4.0)**.

Pairs by task (v1.5-c wins : v1.3-c wins : split): T01 1:2:0, T02 2:1:0, T03 1:2:0, T04 2:1:0, **T05 0:3:0**, T06 2:1:0, T07 1:2:0, T08 1:0:2, T09 2:1:0, T10 2:0:1.

**D5.4:** (1) Δ +1.71 > 1.51 and CI lower bound +0.23 > −1 ✓; (2) largest drop C4 −0.22 ≤ 1.0 ✓; (3) violations 0.000 vs 0.017 (one-to-one) ✓; (4) +14.9 % ≤ +15 % ✓ → **formally an "improvement"**. Additional targets: invented facts ✓ (0.008 ≤ 0.03); pairs ✗ (14 < 17); T09 M5 ✓ (0/12); T02 M4 ✓ (0/12); T04 M7 ✗ (6/12 > 4/12, but 18/18 → 6/12).

Progression of versions in the optimisation line (each in its own iteration, all judgments): v1.0 85.9 → v1.1-c 86.2 → v1.2-c 82.5 (rejected) → v1.3-c 88.9 → **v1.5-c 88.8**. Judge repeatability: the same v1.3-c responses iter. 3 → 88.9 (mixed calls), iter. 5 → 87.1 (only vs v1.5-c) — the drop is explained by context, not drift (§5); A iter. 0–5 55.3–56.5.

## 5. Measurement finding: the primary measure is biased in favour of the version under test

`iter5_context_check.txt`: in all iterations a C response judged next to A receives a higher overall score than the same response next to another C version (iter. 1 +2.70; 2 +1.11; 3 +1.87; 5 +1.71). The version under test is judged 60× vs A and 60× vs the base, the re-judged base — only 60× vs the version under test; therefore the "all judgments" Δ carries ≈ half of the context effect on one side only. Three views on v1.5-c − v1.3-c: **+1.71** (primary, biased ≈ +0.9) / **+0.86** (shared calls, unbiased, power of 60 calls) / **−0.12** (symmetric across iterations, contains judge drift). In iteration 3 the bias did not change the verdict (+4.38 / +3.45); in iteration 5 it decides criterion (1). This is a protocol flaw, not an error of this iteration — the same measure was applied in iterations 1–4.

## 6. What we do next — **decisions for Martin** (nothing is started without them)

1. **Base.** Under the pre-registered rule v1.5-c qualifies as the new base; under the unbiased measure it is "neutral, not worse". My recommendation: **accept v1.5-c as the base** — Martin's main goal (invented facts → ≈ 0) is achieved, violations 0, no criterion drops, two of the three target elements are resolved, and v1.5-c does not lose in any task by more than the noise; with the honest caveat that the gain in the overall score is not proven. Alternative: keep v1.3-c and test v1.6 against it.
2. **Protocol fix for iteration 6** (to be pre-registered before data): primary Δ = the shared-calls measure; to regain power — 6 replicates (120 shared calls, band ≈ ±1.1) or hold-out H01–H10 as a second set. "All judgments" remains as an additional metric and for comparability with iter. 0–5.
3. **v1.6 draft** (`changes_v1.6.md`, CH49–CH56; not generated): R1 sentence on comparison between the person's own numbers (T09 M3 11/12); R7 unknown number = question (T08 M1); R12 danger = shock the reserve cannot absorb + riskiest assumption (T05 0/3); R13 monthly checkpoints (T07, T10); R8 payback at full cost (T06 r1); L4 example without a number (the only invented fact); T04 M7 in the self-check. Net length ≈ 0 (shortenings in the CL bank).
4. Open from iter. 3: hold-out H01–H10 (not measured); J2 (Gemini) for iteration 5 — material `cross_check/judge_calibration_and_J2/j2_gemini/iter_5/`.

**What this iteration teaches about prompt optimisation:** (1) accuracy can be pressed down to zero with one clear rule about the allowed sentence types — but the same rule, read too literally, also cuts off conclusions that follow from the user's own numbers (T09 M3) — the rule must name what **is** shown arithmetic, not only what is not; (2) at the ceiling (elements 97 %, violations 0) the overall-score measure with a 10 × 3 design and biased context no longer distinguishes the versions; element-level targets (T09 M5, T02 M4, T04 M7) are a more precise instrument; (3) the prompt's internal examples are a source of invented facts — the only remaining flag is the L4 example sentence.

## 7. Where the data are

`[local archive]\iter_5\` — `analysis/` (summary, fig1–fig4, fig6, fig7, figure_data, panel_iter_5.png, snapshots, iter5_d54_check.txt, iter5_context_check.txt), `judgments/` (120), `responses/` (30 + bundle), `packs/` (gen 30, judge 120), `hardchecks/`, `prompt/` (02b_v1.5-c.md, changes_v1.5.md/.json/.diff), `error_analysis/` (error_analysis_iter_5.md + raw for v1.5-c and for base v1.3-c, v15_losses.txt, the in-depth v1.3-c analysis before the iteration, changes_v1.6.md draft), `decisions.md`, `comparison.md`. J2 (Gemini) material: `cross_check/judge_calibration_and_J2/j2_gemini/iter_5/`.
