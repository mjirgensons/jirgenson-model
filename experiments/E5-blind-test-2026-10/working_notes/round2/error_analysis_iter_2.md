# E5 — error analysis, iteration 2, condition C (canon v1.0 + prompt v1.2-c)

Data source: 120 judgments (J1 = Opus 5.5); 30 C-v1.2-c responses, each judged 4× (vs A and vs C-v1.1-c, in both orders). One-to-one comparison with the same v1.1-c responses (iter. 1), re-judged in this iteration. Raw table: `error_analysis_iter_2_raw.md`.

**In total:** C(v1.2-c) 82.5 vs C(v1.1-c) 84.7 in the same pairs → **Δ = −2.18** [−5.88; +0.77], 4/6 tasks, pairwise preference **4 : 18 : 8** (v1.2-c wins : loses : ties). Invented facts **1.32 → 0.02**; elements 93 % → 89 %; violations 0.33 → 0.53; C1 7.4 → 8.3; C2 8.2 → 7.6.

## 1. Each v1.2 hypothesis: forecast vs result

| ID | Forecast | Result (v1.1-c → v1.2-c, out of 6 judgments) | Verdict |
|---|---|---|---|
| CH6 (FULL round: 450 in total; 5 = five "?") | T04 F2/H2 ≤2/12, M8 ≤2/12, M4 ≤3/12, T04 ≥80 | F2 6→0, H2 6→0, M4 6→0, M8 4→0, words 505–570 → 337–363; **but** M2 0→6, M7 1→6; T04 69.3 → 72.8 | **form succeeded, content lost** (M2/M7 — see CH7) |
| CH7 (external knowledge only as a check or a labelled assumption; generalisations out) | invented facts ≤0.5; C1 +0.2 | invented facts **1.32 → 0.02**, C1 **+0.9**; **but** too broad: it also dropped risk hypotheses — T04 M2/M7 (the AI factor may hit the main client), T10 M6 2→6 (client insolvency as the greatest risk), T02 M2 0→2 (food safety) | **succeeded on target, the side effect costs more** |
| CH8 ("the budget is a ceiling; finish 10–15 % below") | T07 F2 → 0; T03 ≤620; T04 ≤450 | words **did not decrease** (T01 614–647, T05 564–630, T06 up to 682, T07 411–422, T08 596–693); new H1 violations T02 0→4, T05 0→4, T07 2→6, T08 0→4, T06 0→2; T02 F3 0→4 | **failed** — the sentence does not change behaviour |
| CH9 (R14 only for dates set by others) | T07 words −15…−25; T09 M5 kept | T07 389–418 → 411–422 (not shorter); T09 M5 2→4 | **failed / neutral** |
| CH10 (the PLAN CHECK ending is not to be shortened) | T03 M8 7/12 → ≤2/12 | T03 M8 **6→0**; T03 +2.6 | **succeeded** |
| pack as a whole | +2…+3 | **−2.18** | rejected |

## 2. Where v1.2-c loses points

| # | Task | Δ | Cause | Class |
|---|---|---|---|---|
| 1 | **T02** (EMERGENCY, 300 words) | **−15.3** | 2/3 of the responses 310–317 words (F3, H1); r2 omits food safety before money (M2) and makes an error in the cash flow (M4: postponing the remaining repair payment "protects" wages) | (d) budget + (c) CH7 dropped the safety rule |
| 2 | **T07** (teenager, 400) | −6.8 | all 3 responses 411–422 (F2, M7, H1) | (d) budget; CH8/CH9 did not help |
| 3 | T05 (QUICK 600 + 900) | −3.8 | 1st round 625/630 (M9, H1) | (d) budget |
| 4 | T06 (600) | −3.0 | r2 682 words | (d) |
| 5 | T01 | −2.4 | 642/647 words; noticed the contradiction in fixed costs less often | (d) |
| 6 | **T04, T10** — risk hypotheses | +3.5 / −0.4 (but M2, M7, M6 → missing 6/6) | the model understood CH7 "generalisations about the market, clients … out" as "do not mention these risks at all" | **(c)** wording |

**Gains that remain:** near-complete disappearance of invented facts (CH7 core), T04 form (CH6), T03 ending (CH10), T09 +3.3, T08 M4/M7 improved.

## 3. Conclusion for iteration 3
1. **The CH7 core works** (check or labelled assumption) — keep it, but **risk hypotheses about the person's situation must be explicitly allowed** (CH7b): "a risk that the person's facts make plausible is not dropped because it is general — name it as a hypothesis with a check to perform".
2. **A sentence about length does not change length** (CH8). The model aims at the number written in the prompt: where CH6 gave the number 450, T04 came out at 337–363. Therefore CH11 changes **the numbers themselves** in L5 (≈10 % below the person's limit), rather than adding a sentence.
3. CH9 without a proven gain — revert to the v1.1-c R14.
4. The base remains **v1.1-c** (v1.2-c not accepted); v1.3-c = v1.1-c + CH6 + CH7b + CH10 + CH11.

Methodological note: the same v1.1-c responses gave 86.2 in iter. 1 and 84.7 in iter. 2; invented facts 1.01 → 1.32 (judge repeatability; SD 2.4/response from test–retest). Therefore the comparison is always one-to-one within the same iteration.
