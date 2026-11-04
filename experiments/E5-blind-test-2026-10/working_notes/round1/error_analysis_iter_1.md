# E5 — error analysis, iteration 1, condition C (canon v1.0 + prompt v1.1-c)

Data source: 120 judgments (J1 = Opus 5.5); each of the 30 C-v1.1-c responses judged 4 times (vs A and vs C-v1.0, in both orders) → 120 C-v1.1-c judgments; raw table `index/error_analysis_iter_1_raw.md`. One-to-one comparison base: the same v1.0 responses (block 1, runs 1–3), judged in this same iteration in the same pairs.

Overall score C(v1.1-c) = 86.2; C(v1.0) in the same pairs = 83.9; Δ = **+2.34** [−0.18; +4.58], 8/2 tasks, Wilcoxon p = 0.082; pairwise preference 12 : 13 : 5 (wins : losses : ties). Elements 95 % (v1.0: 91 %), violations 0.32/response (v1.0: 0.33), **invented facts 1.01/response (v1.0: 0.57)** — the only metric that worsened.

## 1. Each v1.1 hypothesis: forecast vs result

| ID | Target | Forecast (changes_v1.1) | Result | Verdict |
|---|---|---|---|---|
| CH1 | T04 FULL round: M8/H1 12/12, M4/F2/H2, M7 | M8, H1 → ~0/12; M4/F2/H2 → ≤2/12; T04 68.9 → ≥85 | Words 731/585/690 → 522/570/505 (M8 8/12, H1 8/12); questions 5/6/8 → 6/8/7 (**F2 9/12, H2 12/12**, M4 9/12); M7 4/12; T04 64.2 → 70.4 (+6.2) | **partly**: direction right, target far off |
| CH2 | T06 M7 (data items without a question) | 8/12 → ≤2/12 | M7 **0/12**; T06 81.7 → 87.9 (+6.2) | **succeeded** |
| CH3 | invented facts 0.79 → ≤0.45; C1 +0.3…+0.6 | | invented facts **0.57 → 1.01** (in the same pairs); C1 7.8 → 7.8 | **failed, opposite effect** |
| CH4 | T03 M3 (obligation first) | 4/12 → ≤1/12 | M3 **0/12**; but a new M8 **7/12**; T03 82.2 → 86.1 (+3.9) | **succeeded with a side effect** |
| CH5 | T09 M5 (decision point with a date) | 7/12 → ≤3/12 | M5 **4/12**; T09 85.3 → 87.6 (+2.2); the side risk "word budget" materialised in T07 | **partly** |
| pack as a whole | +3…+5 pts | | **+2.34** | below forecast |

## 2. Where v1.1-c loses points (by amount of points lost)

| # | Task → requirement | How often | Class | Diagnosis (from judgments, responses and prompt text) |
|---|---|---|---|---|
| 1 | **T04 FULL round**: F2/H2 (>5 questions) 9/12 and 12/12; M8/H1 (>500 words) 8/12; M4 9/12; M7 4/12. T04 = 70.4 (lowest) | systemic | **(c)** | Two prompt wording errors. (i) L5/FULL: "up to 350 words *before* the questions" — the questions add 150–220 words, in total 505–570 > the rubric's 500. (ii) FULL: "combine related questions so that five are not exceeded" — the model gives 5 numbered blocks with 2–3 sub-questions (6–8 question marks); the judge counts question marks. M7: the AI factor presented as a fact ("routine text is often where companies try AI first"), not as a hypothesis/question — linked to CH3. |
| 2 | **Invented facts** 1.01/response (121 marks in 120 judgments). Dominant: EU rules ("in most EU countries … check yours": late-payment interest and 40 €, cancellation fee, e-scooter age 14–16, reduction of working hours), industry generalisations ("companies often keep human review", "a new salon usually takes months", "80 % booked for four weeks is the usual rule of thumb"), external prices (helmet 30–50 €). In all tasks, most in T05, T07, T04, T01. | widespread | **(c)** | CH3 gave a permission: "external knowledge … state the condition in the same sentence ('in most EU countries …; check yours')". The model followed it literally and *more often* — each response now contains 1–3 such sentences. The judge rubric (29c) marks every claim that is not from the task and is not labelled as an assumption; for the rubric, "check yours" is not a label. Result: the count doubled, C1 did not change (the judge penalises little), but T07 r2 and T04 M7 suffered directly. |
| 3 | **T07 r2**: F2/M7/H1 (418 > 400 words) 4/12 → T07 90.3 → 84.2 (**−6.1**) | one run, but a systemic cause | **(d)+(a)** | v1.0 T07: 374–397 words; v1.1-c: 389/393/418. The added content (R14 "decision point with the price of both choices" — T07 has a fixed date, 1 June; CH3 "check yours" sentences) pushes the response over the limit. The budget in the prompt works as a target, not as a ceiling with a margin. |
| 4 | **T03 M8** (missing reserve/cash item and 2–3 checks at the end) 7/12 — not present in iteration 0 | often | **(d)/(a)** | Words 646–682 (budget 700). CH4 added "obligation first" content; the ending on the missing data was squeezed out. In PLAN CHECK mode there is no sentence about the missing-data ending. |
| 5 | **T09** M5 4/12, M6 1/12; r1 "the place is hard to get back" (unfounded) | sometimes | **(a)** | R14 is present, but "the price of both choices" is not calculated in the person's units; generalisations about landlord behaviour (CH3 effect). |
| 6 | **T10** M6 3/12, M1 2/12 (client insolvency as the greatest risk; starting numbers) | sometimes | **(a)/(d)** | From iteration 0 (left as is); 300-word budget. |
| 7 | T02 H6 1/12; T06 M4 2/12; T08 M7 1/12 | rarely | — | not systemic; T02 improved 81.0 → 88.5 without a direct change (possibly self_check "numbers consistent"). |

Classes: (a) the rule exists but is not followed; (b) there is no rule; (c) rules contradictory/unclear (here: prompt wording vs the rubric definition); (d) model/budget limit; (e) judge error.

## 3. What not to change
CH2 (R8 data items as a statement) and CH4 (obligation first) work — they stay. T01, T05, T08 (90+) stable. The QUICK/EMERGENCY form works. The B/A gap remains (+30.9 vs A).

## 4. Conclusion for iteration 2
Three causes account for almost all lost points, and all three are **prompt wording** errors, not a model limit: (1) the FULL round budget is defined incompatibly with the rubric (350 "before the questions" vs 500 in total; "combined" questions vs the count of question marks); (2) the CH3 permission for external knowledge with "check yours" — must be reverted and replaced with a labelled assumption or a check to perform; (3) the word budget as a target, not a ceiling — in the short modes (400) there is not enough margin. Change pack v1.2-c: `index/changes_v1.2.md`.

Methodological note: v1.1-c passes 29 §5.4 (Δ > noise; CI lower bound −0.18 > −1; criteria do not fall; violations 0.32 vs 0.33), but the pairwise preference is 12 : 13 — the improvement is in the average overall score (T02, T04, T06), not "in every pair". The forecast +3…+5 did not materialise (+2.34). Both facts are to be recorded in 30 §8.1 without softening.
