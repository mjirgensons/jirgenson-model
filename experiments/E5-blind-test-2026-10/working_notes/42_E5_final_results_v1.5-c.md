# E5 — final results: operating-prompt optimisation (v1.0 → v1.5-c)

**Document for another session: self-contained; contains everything needed to cite and use the results without access to this conversation.** Prepared 2026-10-30 UTC (29.10. evening, Toronto) after the close of iteration 5. Figures from the frozen records `[local archive]\iter_N\analysis\e5_results_iter_N_snapshot.csv`; every figure is traceable to a specific judge evaluation. Authors: Martin Jirgenson (commissioned the experiment; decisions), Claude (protocol, execution, analysis).

---

## 1. What was done (in one paragraph)

Experiment E5 tested whether the operating prompt (02b) of the Jirgenson model can be made measurably better through controlled iterations, and how large the contribution of canon + prompt is compared with the model without a prompt. The canon (02a) was fixed at v1.0 throughout. 10 frozen development tasks (T01–T10: small business owners, a teenager, a freelancer; EN/LV/RU; EMERGENCY, QUICK, FULL and PLAN CHECK modes), each × 3 independent replicates. Generator **Claude Sonnet 5.5**, blind judge J1 **Claude Opus 5.5** with a pre-prepared answer key, each pair judged in both orders. Total score 0–100 = 40 × share of mandatory elements + six criteria (C1 accuracy, C2 diagnosis, C3 practicality, C4 fit, C5 control, C6 honesty; each 1–10) − 2 × violations. Noise band measured in iteration 0: **±1.51 p.** Acceptance rule fixed before the data (29 §5.4): Δ vs base > 1.51 with CI lower bound > −1; no criterion falls by > 1.0; violations do not increase; prompt ≤ +15 % longer than v1.0. Optimisation line: **iter. 0 (v1.0) → 1 (v1.1-c, accepted) → 2 (v1.2-c, rejected) → 3 (v1.3-c, accepted) → 5 (v1.5-c)**. In total in the optimisation line: 240 generated responses, 600 judge evaluations.

## 2. Final version

| | |
|---|---|
| Operating prompt | **`02b_v1.5-c.md`** — 4,570 words (+14.9 % vs v1.0; protocol limit +15 %), sha256 `36ab059bee95bcc65b8e75e572646e40f2b3b5024f7c569c15cf65d03a269477` |
| Canon | **`02a_canon_v1.0.md`** — unchanged throughout the experiment, 3,680 words, sha256 `829a3b9b113d1897b35589d80733ab902af852bd2855532f14a5df62db4155b6` |
| Use | canon first in the SYSTEM part, prompt after it (exactly as in the experiment) |
| What changed vs v1.0 | iter. 1: format budgets and mode discipline; iter. 3: permission for hypotheses with a label, PLAN CHECK closing, lower word budgets; iter. 5: 41 systematic replacements on three axes — **evidence discipline** (R1: about the person's situation only a fact, shown arithmetic or a labelled assumption is allowed; R2: no inferred dates), **forecast depth** (to the red line and to zero with months; funding includes start-up losses; the danger with amount and months), **usefulness of actions and choices** (a day and a person for every action; written demand today; exit as an option; an explicit instruction about form overrides the format). Full list: `iter_5/prompt/changes_v1.5.md`, exact replacements `.json`, text diff `.diff` |

## 3. Main result — the final version vs the controls and vs the start

Mean total score across 10 tasks (each task = 3 replicates × evaluations in both orders):

| Condition | Total score (0–100) | Paired difference v1.5-c − X [95 % CI] | Tasks in which v1.5-c is better | Pairwise preference (both orders agree) |
|---|---|---|---|---|
| **A — no prompt** (the same responses, iter. 5) | 56.2 | **+32.5** [+26.6; +38.5] | 10/10, Wilcoxon p = 0.002 | **30/30** |
| **B — generic structured adviser prompt** (iter. 0) | 67.7 | **+21.1** [+15.2; +27.5] | 10/10, p = 0.002 | — (B measured only in iter. 0) |
| **C — canon + prompt v1.0** (starting point, iter. 0) | 85.9 | **+2.9** [+0.0; +6.4] | 6/4, p = 0.19 | — |
| C — canon + prompt v1.3-c (previous accepted, iter. 3) | 88.9 | −0.1 [−0.9; +0.7] | 5/5 | 14 : 13 : 3 (in the direct comparison, iter. 5) |
| **C — canon + prompt v1.5-c** (final) | **88.8** | — | — | — |

In the same figures: with the canon and the final prompt, the judge rates Sonnet 5.5 responses **58 % higher** than without a prompt (88.8 vs 56.2) and **31 % higher** than with a good generic adviser prompt (vs 67.7). Against the starting point v1.0 itself, the total score is 2.9 points higher — an improvement above the noise band, but with the CI lower bound at zero (a comparison between iterations, not within one judge call).

## 4. Where the contribution is — by measure

| Measure | A (no prompt) | B (generic prompt) | v1.0 (start) | **v1.5-c (final)** |
|---|---|---|---|---|
| Total score | 56.2 | 67.7 | 85.9 | **88.8** |
| Mandatory elements (answer key) | 55 % | 66 % | 93 % | **97 %** |
| **Violations per response** (forbidden actions + hard checks) | 1.05 | 0.97 | 0.28 | **0.00** |
| **Invented facts per response** | 1.70 | 0.70 | 0.79 | **0.008** (1 flag in 120 evaluations) |
| Responses with ≥ 1 invented fact | 70 % | 45 % | 55 % | **0.8 %** |
| C1 accuracy | 6.8 | 7.8 | 7.9 | **8.7** |
| C2 diagnosis | 6.8 | 7.0 | 8.2 | 8.0 |
| C3 practicality | 5.9 | 7.7 | 8.0 | **8.3** |
| C4 fit | 6.4 | 6.7 | 8.0 | **8.4** |
| C5 control (management quality) | 4.2 | 6.0 | 8.6 | 8.3 |
| C6 honesty | 6.4 | 8.1 | 8.5 | 8.5 |
| Words per response (judge count) | 501 | 515 | 533 | **454** |
| Hard checks (word budget, number of questions, language, internal markers) | — | — | — | 33/33 turns clean |

Three things the final prompt does compared with the model without a prompt: (1) **invented facts practically disappear** — from 1.70 per response to 0.008 (A: 7 of 10 responses contain at least one unsupported number, date or cause; v1.5-c: 1 of 120); (2) **there are no violations** — not a single forbidden action, not a single exceeded budget in 120 evaluations; (3) **management quality** (C5: the red line, the review date, what belongs to the owner) is doubled — 4.2 → 8.3. Compared with the generic adviser prompt B, the difference is exactly where the model's content is, not the form: C5 6.0 → 8.3, mandatory elements 66 % → 97 %, invented facts 0.70 → 0.008.

## 5. By task (mean total score)

| Task (29a) | Mode, language | A | B | v1.0 | v1.3-c | **v1.5-c** | v1.5-c − A |
|---|---|---|---|---|---|---|---|
| T01 seasonal bike shop, e-bikes | QUICK, EN | 67.7 | 72.8 | 91.2 | 91.7 | **91.0** | +23 |
| T02 food truck, 72 h permit clock | EMERGENCY, EN | 46.8 | 52.3 | 84.7 | 88.9 | **89.2** | +42 |
| T03 yoga studio, 11 "goals", "don't rewrite" | PLAN CHECK, EN | 59.5 | 63.7 | 85.2 | 88.2 | **86.9** | +27 |
| T04 translation agency, main client and AI | FULL round 1, EN | 34.3 | 50.0 | 68.9 | 83.1 | **85.2** | +51 |
| T05 dog-grooming salon, two-step conversation | QUICK + "no more data", EN | 58.8 | 72.7 | 92.3 | 91.7 | **90.0** | +31 |
| T06 second nail salon, "guarantee the payback" | QUICK, EN | 55.7 | 82.0 | 84.0 | 90.1 | **90.6** | +35 |
| T07 fifteen-year-old, e-scooter and a concert | ≤400 words, EN | 67.7 | 77.2 | 90.2 | 90.3 | **89.8** | +22 |
| T08 print shop, "we are profitable", cash falling | QUICK, EN | 54.0 | 76.2 | 88.8 | 88.7 | **90.3** | +36 |
| T09 newspaper kiosk in a small town, end of lease | QUICK, LV | 67.2 | 73.2 | 87.3 | 86.8 | **84.8** | +18 |
| T10 freelancer, client not paying, rent in 6 days | EMERGENCY, RU | 50.8 | 56.5 | 86.4 | 89.5 | **89.7** | +39 |

The largest gain vs A — T04 (+51: without the prompt the model does not notice the dependence on one client and the AI risk to the whole market) and T02 (+42: in an emergency, without the prompt there is neither the cash low point nor the food-safety step). The only task where the final version is lower than the start is T09 (87.3 → 84.8): the new evidence rule makes the model phrase the conclusion "the shrinking town is the strongest force" as a question (see §7).

## 6. Version history (each version in its own iteration; mean total score)

v1.0 **85.9** → v1.1-c **86.2** (accepted: format budgets) → v1.2-c **82.5** (rejected: an over-strict ban on hypotheses cut content) → v1.3-c **88.9** (accepted: +4.4 vs v1.1-c, in 10/10 tasks) → v1.5-c **88.8** (§5.4 formally met vs v1.3-c: Δ +1.71 [+0.23; +3.36]; in the direct comparison within the same judge calls +0.86 — within the noise band; pairs 14 : 13 : 3). The total score from v1.3-c to v1.5-c has **not** demonstrably risen; what **has** risen is what was the target of iteration 5: invented facts 0.11 → 0.008, violations 0.02 → 0.00, three target elements (T09 exit as an option, T02 cash low point — missing in 0/12; T04 market-scale risk — missing 18/18 → 6/12). Judge repeatability: the same v1.3-c responses in iterations 3 and 5: 88.9 / 87.1; A in five iterations 55.3–56.5.

## 7. What is still not right in the final version (so that another session is not surprised)

- **T09 M3** (the shrinking town named as the strongest force, which marketing alone will not overcome) is missing in 11 of 12 evaluations — the evidence rule R1 ("everything else is a check") turns even a conclusion drawn from the user's own numbers into a question. The fix is one sentence (v1.6 draft CH49).
- **T05** loses all 3 pairs in the direct comparison with v1.3-c: the danger is formulated as "one weak month", which its own numbers refute; the shock that the reserve cannot absorb is not named (CH51).
- **T04 M7** (whether AI affects the whole market) is missing in 6/12 — half as often as with v1.3-c, but not zero (CH55).
- The **only invented fact** in 120 evaluations is a sentence from the prompt's own L4 example ("With your hours, three to five can get real work this year") — the number must be removed from the example (CH54).
- The draft `changes_v1.6.md` (CH49–CH56) is written, **not generated and not tested**.

## 8. What this proves and what it does not (29 §0 wording)

**Proves:** with these 10 tasks, generator Sonnet 5.5, judge Opus 5.5 and this rubric, canon + prompt v1.5-c gives a score **32.5 points** [26.6; 38.5] higher than the same model without a prompt (in 10/10 tasks, 30/30 pairs), **21.1** [15.2; 27.5] higher than a good generic adviser prompt, and **2.9** [0.0; 6.4] higher than the starting version of the prompt, v1.0; the frequency of invented facts is reduced from 1.70 (A) and 0.79 (v1.0) to 0.008 per response, violations — to zero.

**Does not prove:** that the prompt "prevents hallucinations" in general (one judge measured, one model family, 10 tasks); that it works with any model or task (the hold-out set H01–H10 and the confirmation models were **not measured**); that the LLM judge's evaluation agrees with human evaluation (second judge J2 Gemini — 4 pairs, element agreement 100 %, no opposite preferences; iter. 5 material pending).

**Methodological finding (iter. 5):** the judge scores a C response judged alongside a weak A response +1.1…+2.7 higher than the same response alongside another C version (in all iterations). The protocol's primary Δ measure is therefore shifted ≈ +0.9 in favour of the version under test; it does not change earlier verdicts (both measures on the same side of the band), in iteration 5 it decides criterion (1). Recommendation for the next iteration: primary Δ = the shared-calls measure only, 6 replicates (band ≈ ±1.1).

## 9. Open decisions (for Martin)

1. **Base going forward:** v1.5-c (recommendation — accuracy targets achieved, nowhere worse by more than noise) or v1.3-c.
2. **Protocol correction for iteration 6** (§8 finding): the shared-calls measure as primary; 6 replicates or hold-out H01–H10.
3. Whether to generate and test v1.6 (CH49–CH56).
4. Hold-out and confirmation models (29 §2.2, §5.5) — not performed; without them H4 and H5 remain untested.

## 10. Where the data are

Location in this record: protocol, report and notes in `working_notes/`; generator and judge inputs in `inputs/roundN/`; responses in `responses/`; judge records in `judgments/roundN/`; score snapshots, hard checks, figures (fig1–fig7 + panel) in `data/`; error analyses, decisions and comparisons in `working_notes/roundN/`. Iteration 5 summary: `working_notes/round5/comparison.md`; decisions `working_notes/round5/decisions.md` (D5.1–D5.13); error analysis `working_notes/round5/error_analysis_iter_5.md`; scientific report `working_notes/30_E5_scientific_report.md` (§8, §10). Path from a figure to its source: `data/roundN/e5_results_iter_N_snapshot.csv` (pairid, order) → `judgments/roundN/{pairid}_{order}.md` → `inputs/roundN/judge/…` → `responses/…` → `inputs/roundN/generation/…`.
