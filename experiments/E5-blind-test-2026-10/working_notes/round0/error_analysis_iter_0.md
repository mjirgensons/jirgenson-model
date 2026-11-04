# E5 — error analysis, iteration 0, condition C (canon v1.0 + prompt v1.0)

Data source: 120 judgments (J1 = Opus 5.5), each C response variant judged 2 times (both orders); 60 C responses = 120 judgments; raw table `index/error_analysis_iter_0_raw.md`.
Total score C(v1.0) = 85.9 (A 55.3; B 67.7). Noise band ±1.5 pts. Elements 93%, violations 0.28/response, invented facts 0.79/response.

## 1. Where C loses points (sorted by the amount of points lost)

| # | Task → requirement | How often | Class | Diagnosis (from the judgments and responses) |
|---|---|---|---|---|
| 1 | **T04 FULL round 1**: M8 (≤500 words, no full brief) 12/12; H1 12/12; M4/F2 (≤5 questions) 6/12, H2 8/12; M7 (AI factor as a question/hypothesis) 6/12; M5 (refusal-order question) 3/12; F1 (full plan before the answers) 2/12. C4 = 5.1. Task mean 68.9 | systemic | **(b) + (c)** | The prompt's FULL mode says "preliminary reading + up to 5 questions", but L5 gives no word budget for the FULL round, and the seven sections of output_format pull towards a full brief. Responses: 573–731 words, 5–8 questions, the sections "most dangerous", "what to protect", "what to do", forecast included. The question bank (A–M, 13 categories) encourages >5 questions. |
| 2 | **Invented facts** (C1 mean 7.8; T08 C1 6.9; 47 flags in 120 judgments). Dominant: the EU late-payment rule "interest + €40" as a fact, country unknown (T08, T10); generalizations as facts ("banks agree more readily while the account looks healthy", "three to five goals are usually enough", "the first season usually only breaks even", "clients often still want a check") (T01, T03, T04); T09 r1 factual error (the factory "was still operating in 2024." — in the task: closed in 2023). | widespread | **(c)** | canon_gate point 3 says to give practical knowledge "as ordinary advice … without labeling", but R2/C6 require assumptions to be labeled. Result: external rules and generalizations are presented as certain facts about this person. The judge is strict also towards hedged ("check your country") claims, but penalizes them less. |
| 3 | **T06** M7 (2–3 data items that would narrow the range) 8/12 | often | **(c)** | The user forbids questions; the model takes this also as a ban on naming which data would narrow the range. R8 requires it, QUICK "zero questions" suppresses it. A contradiction between rules. |
| 4 | **T09** M5 (end of the lease as a decision point; low cost of a wrong exit; options with the value of the owner's time) 7/12 | often | **(b)** | The prompt has no rule about a "decision point" with a fixed date (end of a lease, of a contract) and about the cost of a wrong choice in both directions; canon §10.1 mentions it only in the "Titanic" context. The responses name the lease but do not assess the cost of exiting. |
| 5 | **T02** M4 (cash flow: −1,700 € before day 5, −200 € after) 6/12; M2 (food safety before money) 2/12 | often | **(a)/(d)** | 300-word budget; some responses give only one of the two numbers. The rule (R2 arithmetic) exists; the budget squeezes it out. |
| 6 | **T03** M3 (tax debt as a constraint in first place) 4/12; M1/F1 (rewrote the plan) 2/12 | sometimes | **(a)** | The MODE 1 text does not say that an obligation (taxes, law, safety) entered as a goal is to be reported first as a constraint; §1.10 is in the canon, R5 mentions only "methods or constraints". |
| 7 | **T10** M6 (client insolvency as the biggest risk) 4/12; C1 7.2 | sometimes | **(a)** | R12 exists; 300-word budget. Leave for iteration 2. |
| 8 | T08 H6 2/12 (numeric inconsistency), T02 H4 1/12 ("never below zero" as a quoted rule) | rarely | (d)/(a) | not systemic |

Classes: (a) the rule exists, is not followed; (b) there is no rule; (c) rules contradictory; (d) model/budget limit; (e) judge error.

## 2. What not to change
T01, T05, T07 (90+): the EMERGENCY/QUICK/teenager format works; the jargon problem (E1 Haiku) does not appear on Sonnet (T07 H5 0 violations). The B comparison shows that the content (C5 8.6 vs 6.0; elements 93% vs 66%) is the source of the contribution, not only the structure.

## 3. Conclusion for iteration 1
One systemic gap (the FULL round) and one contradiction between rules (external knowledge without labeling) account for most of the lost points. Change pack v1.1-c: `index/changes_v1.1.md`.
