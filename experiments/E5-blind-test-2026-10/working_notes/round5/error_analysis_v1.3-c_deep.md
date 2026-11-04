# E5 — in-depth investigation of v1.3-c errors before iteration 5 (2026-10-28)

**Goal:** find everything that v1.3-c (the best version, 88.9 / 88.7) still does wrong, so that in iteration 5 the prompt is changed systemically, not with separate patches. Martin's special goal: invented facts → almost zero.

**Data source:** all 180 judge (J1 Opus 5.5) judgments in which some v1.3-c response was judged: iteration 3 (120: vs A and vs v1.1-c) and an additional judging run of v1.3-c that is not part of this record (60: the same responses). Raw outputs: `scratch/v13c_deep.txt` (elements, invented facts, violations), `scratch/v13c_losses.txt` (all 37 lost pairs with the judge's rationale word for word). Both archived in `iter_5/error_analysis/`.

## 1. What v1.3-c is missing (elements; 18 judgments per task)

| Task → element | Missing | What it means |
|---|---|---|
| **T04 M7** — whether AI affects the whole market, not only the main client | **18/18** | the environment check (offsets (c)) is not asked; the CH7b example narrowed the hypothesis down to the client |
| **T09 M5** — the end of the lease as a decision point, with an orderly exit as an option | **10/18** (+ M7 3/18) | exit is not offered as an equivalent option; the response adapts to the user's (erroneous) plan |
| **T02 M4** — the lowest cash point (≈ −1,700 before day 5) | 6/18 | shows the ending balance, not the deepest point |
| T08 M1 / M3 / M4 — which number governs the week; the €14,000 gap as a question; the debtor risk in money and months | 4/18 each | dangers named, but not calculated (amount at risk → months to zero) |
| T03 M1 — "don't rewrite" is respected | 4/18 | one response (r2) rewrites the list of goals against a direct instruction |
| T10 M6 — client non-payment as the biggest danger | 3/18 | behind the urgent symptom the biggest danger is not named |

Violations: 0 of 180 (one F4 in an additional judging run of v1.3-c that is not part of this record — "stop work for the client today" as an irreversible step).

## 2. Invented facts: 20 flags / 180 = 0.11 per judgment — what they are

| Type | Examples (in the judge's words) | Flags |
|---|---|---|
| **Unlabelled assumption about cost or demand behaviour / "what can be afforded"** | "€1,950 a month *cannot support an employee*" (T04 r3); "*costs would not fall*", if the big client's work stopped (T08 r3); profit proportional to turnover (T09 r3) | 8 |
| **Calendar dates when today's date is not given** | "23 October", "30 October", "23 November" (T10 r2) | 4 |
| **Unfounded split of causes** | "about half of the drop — fewer people; the other half marketing can affect" (T09 r3) | 3 |
| **A date given by the user made more precise** | end of the lease "exactly on 17 June 2027" (T09 r2) | 2 |
| **General law without a label** | "three to five goals a year are enough" (T03 r1) — **this sentence is the prompt's own L4 example** ("three to five are usually enough for a year") | 1 |
| Implicit number assumption; unnecessary qualifier | "one more evening solves it" (≥ €10 per evening, T07); "before taxes" (T09) | 2 |

**Conclusion:** almost all invented facts are of one class — a sentence about **a cause, cost behaviour, a date or "what can be afforded"**, which is neither the user's fact, nor shown arithmetic, nor a labelled assumption. R2 ("only the user's facts and arithmetic") does not cover this directly enough: the model does not perceive these sentences as "numbers". Two sources are in the prompt itself (the L4 example with "usually"; in the EMERGENCY example "a landlord usually allows a week").

## 3. Why v1.3-c loses pairs (37 lost out of 180 judgments; judge rationales)

| Theme | Lost pairs | Judge's words (shortened) |
|---|---|---|
| **A. Depth of the worst-case scenario**: the forecast is not taken to zero; the worst case is not dated; start-up losses are not included in the funding | 11 (T06 ×6, T08 ×4, T09 ×1) | "never says when cash runs out"; "models the downside the owner most needs"; "leaves its own start-up losses unfunded and breaching its own red line"; "nothing-changes forecast mislabels the trend as the worst case" |
| **B. Actions without a date; decision deferred; written demand delayed** | 11 (T01 ×4, T10 ×5, T03 ×1, T06 ×1) | "defers the cash decision to 31 October"; "its written step depends on the client naming a date, the formal claim waits until 30 Oct"; "checks carry no timing"; "spends this-week steps on bike logistics" |
| **C. The alternative (exit, not opening, skipping) not offered as a real option; the choice taken away from the person** | 6 (T09 ×3, T07 ×2, T06 ×1) | "frames leaving as the risky side"; "imposes 'the concert is off'"; "no fallback if the red line is crossed" |
| **D. Direct instruction about form not followed** ("don't rewrite") | 3 (T03 r2) | "goes against the owner's explicit 'don't rewrite'" |
| **E. Dangers not calculated** (amount at risk, impact in months) | 3 (T08, T06) | "leaves the danger unquantified"; "never sizes the funding gap" |
| **F. Environment check** | 2 (T04) | "misses the market check" |
| **G. Cash plan not worked out to the end** | 2 (T02) | "leaves the day-4 wage gap unsolved"; "never works out where its levers leave the cash" |
| **H. Irreversible step today; payment priority** | 2 (T10, T08) | "tells him to stop new work for the client today, an irreversible step"; "'pay only wages, rent and materials' risks skipped tax or loan payments" |

In the lost pairs the judge's confidence is low (0.55–0.68): v1.3-c does not lose grossly, but consistently on the same things. They are all properties of **decision usefulness** (how far the forecast is taken, how concrete the action is, whether the alternative is on the table), not errors of accuracy or form — there v1.3-c is already at the ceiling.

## 4. What this means for the v1.5 design

Not three patches (v1.4-c draft), but three systemic axes, each with one rule, one thinking step and one self-check line:

1. **Evidence discipline** (invented facts → 0): only three kinds of sentence about the person's situation are allowed — their fact, shown arithmetic, a labelled assumption; everything else is a check to carry out. Name the risk classes directly: causes, cost/demand behaviour, "what can be afforded", third-party actions, typical values. Dates: without today's date — only relative time; do not make the given date more precise. The last self-check line — sentence by sentence. Fix both internal sources in the prompt (the L4 example; "usually" in the EMERGENCY example).
2. **Forecast depth**: the no-change forecast to the red line and to zero, with months; the worst case with the date when the payer, client or new project may fail; funding includes start-up losses; dangers with the amount and the impact in months; the lowest cash point with the day.
3. **Usefulness of actions and choice**: each action this week has a day and a person; a decision that the numbers already allow is made in the response; for the debtor — a written demand today with the person's own date; irreversible steps only as conditions; the alternative (exit, not opening, waiting) as a real option with a price, the choice stays with the person, with a fallback path; a direct instruction about form overrides the format; obligations are ranked, not dropped.

The length constraint (≤ 4,572 words, +15 % vs v1.0) is respected by shortening duplicated text (L1/L3a merged, canon_gate para. 3 shortened, duplicated CL removed, the description of the long overview and the question bank shortened), not by giving up the examples.
