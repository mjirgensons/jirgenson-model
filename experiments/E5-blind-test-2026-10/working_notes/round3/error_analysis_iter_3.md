# E5 — error analysis, iteration 3, condition C (canon v1.0 + prompt v1.3-c)

Data source: 120 evaluations (J1 = Opus 5.5); 30 C-v1.3-c responses, each judged 4× (vs A and vs C-v1.1-c, in both orders). One-to-one comparison with the same v1.1-c responses (iter. 1), re-judged in this iteration. Raw tables: `error_analysis_iter_3_raw.md` (v1.3-c, 12 evaluations per task) and `error_analysis_iter_3_raw_base_v1.1-c.md` (base v1.1-c, 6 evaluations per task, the same calls).

**Overall:** C(v1.3-c) 88.9 vs C(v1.1-c) 84.5 → **Δ = +4.38** [+1.97; +7.47], **10/10 tasks**, Wilcoxon p = 0.002. Only in the 60 calls where both versions were judged together: Δ +3.45 [+0.90; +6.53], 8/10. Pairwise preference **15 : 10 : 5** (v1.3-c wins : loses : ties). Violations **0.35 → 0.00**; invented facts **1.20 → 0.11**; elements 94 % → 97 %; C1 7.3 → 8.5; C4 7.8 → 8.6; C6 8.2 → 8.7; C2 8.15 → 8.08.

## 1. Each v1.3 hypothesis: prediction vs result

Element counts: from the 6 evaluations in which both versions are in the same call (v1.1-c → v1.3-c).

| ID | Prediction (changes_v1.3, before the data) | Result | Verdict |
|---|---|---|---|
| CH6 (FULL round: five questions = five "?"; the whole round under budget) | T04 form is retained | T04 F2 6→0, H2 6→0, M4 6→0, M8 4→0, H1 4→0; words 355–440 (v1.1-c 488–554); T04 **67.2 → 83.1 (+15.9)** | **succeeded** (as in iter. 2) |
| CH7b (external knowledge only as a check or a labelled assumption **+ plausible risks remain as hypotheses**) | invented facts ≤0.3; T04 M2/M7, T10 M6, T02 M2 back at v1.1-c level | invented facts **0.11** (≤0.3 ✓); T04 M2 0 (v1.2-c: 6) ✓; T10 M6 2→2 (v1.2-c: 6) ✓; T02 M2 0 ✓; **but T04 M7 2→6** (see §2, row 1) | **succeeded on 4 of 5 targets**; M7 did not recover |
| CH10 (PLAN CHECK closing cannot be shortened) | T03 gain is retained | T03 M8 6→0; T03 +4.8 | **succeeded** |
| CH11 (internal budgets ≈10 % below the person's limit) | H1/F2/F3/M8 violations T02, T05, T07, T08 → ≤1/6 | **0 violations in all 120 evaluations** (v1.1-c 0.35/response); 33/33 hard checks; T07 F2/H1 2→0; elements did not decrease (97 %) | **succeeded**; side effect — see §2.4 |
| pack as a whole | +1.5…+3; invented facts ≤0.3; violations ≤0.25 | **+4.38**; 0.11; 0.00 | **exceeded the prediction**; §5.4 met |

## 2. Where v1.3-c still loses points

| # | Task → element | How often (v1.3-c, 12 eval.) | Cause | Class |
|---|---|---|---|---|
| 1 | **T04 M7** — whether AI replacement affects **the whole market** (environment check) | **12/12** (v1.1-c 2/6) | The responses apply the AI hypothesis only to the main client. The CH7b example in the prompt is literally "a market shift that may reach their main client" — the model followed the example and narrowed the hypothesis to the client | (c) wording — the example narrows the rule |
| 2 | **T09 M5** (+ M7) — the end of the lease as a decision point **with an orderly exit as an option** | M5 5/12, M7 2/12 (v1.1-c M5 1/6) | The decision point with a date is there (R14 works), the time is estimated, but exit is not offered as an option, and the cost of a mistaken exit is shown as high rather than compared with mistakenly staying; M7: no "when to stop" condition | (a) rule incomplete (R14 requires the cost of both mistakes, but not exit as an option) |
| 3 | **T02 M4** — the cash-flow **low point** (≈ −1,700 before day 5) | 4/12 (one response, r2; v1.1-c 0/6) | The response shows the balance on day 2 and on day 5, but not the deepest point, which determines the size of the bridge needed | (b) missing rule (cash-flow low point) |
| 4 | T08 M3/M4 (r3) | 2/12 each | the €14,000 gap turned into an action rather than a question; the risk amount and the effect on months to zero are not in numbers | (e) one response; not systemic |
| 5 | T03 M1 (r2) | 2/12 | one response starts rewriting the goals list | (e) one response |
| 6 | T10 M6 (r3) | 2/12 (v1.1-c 2/6) | no change vs the base | — |

### 2.4 CH11 side effect: shorter ≠ always better in the pairwise comparison
In the total score v1.3-c is better in all 10 tasks, but in pairwise preference only 15 : 10. v1.1-c wins 2/3 of the pairs on T06, T08 and T10. The reason on T10 is the wording of the first action (a written demand with its own deadline and a second channel). On T06 and T08 the judge's rationales (verbatim in the evaluations): v1.1-c "models the downside the owner most needs", "carries the forecast to zero", "models ramp-up losses more realistically" — i.e., a deeper worst-case calculation. The v1.3-c responses are 10–15 % shorter (T06 342–353 vs 388–397; T08 508–521 vs 586–590 words). C2 diagnosis in the same calls 8.15 → 7.88 (−0.27; the §5.4 limit of −1.0 is not close). **Hypothesis:** the lower internal budgets (CH11) removed the violations but in some tasks also cut off the worst-case forecast. Not fixed in this iteration (length reserve 117 words; the violation gain is larger), but to be monitored: C2 and pairwise preference on T06/T08.

### 2.5 Judge effect (methodological note)
The same v1.3-c response receives on average 89.8 when judged vs A, and 88.0 when judged vs v1.1-c (contrast effect; the T08 M3/M4, T09 M7, T03 M1, T10 M6 deficiencies are flagged only in comparison with a strong opponent, T09 M5 in both). The same was true in iter. 1–2, so the method (all evaluations) is consistent; the robustness check with shared calls only (+3.45) also meets §5.4. Base v1.1-c responses: iter. 1 86.2 → iter. 2 84.7 → iter. 3 84.5 (judge repeatability within the noise band).

## 3. Conclusion
1. **v1.3-c meets §5.4** on all four points; the prediction was exceeded (+4.38 vs +1.5…+3). All four changes worked on their target; the only unrecovered element is T04 M7, and its cause is the wording of the CH7b example itself.
2. The remaining losses are small and narrow: T04 M7 (systemic, 1 task), T09 M5/M7 (exit as an option), T02 M4 (cash-flow low point). Together they give ≈ +0.5…+1.2 points — **less than the noise band ±1.51**. So the next pack, even if it works, most likely **cannot meet §5.4(1)** with this set (10 tasks × 3 replicates): the development set is approaching the ceiling for this judge and rubric (elements 97 %, violations 0).
3. Pack v1.4-c (draft, `changes_v1.4.md`) fixes the three narrow causes with +41 words (reserve afterwards 76). It is prepared **but not generated** (Martin's instruction 2026-10-18: "do not continue further for now"). The decision on continuation — for Martin (see `comparison.md` §6).
