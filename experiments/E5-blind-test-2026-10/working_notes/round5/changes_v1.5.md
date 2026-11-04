# Change pack v1.5-c, 2026-10-28, after an in-depth v1.3-c error investigation (`error_analysis_v1.3-c_deep.md`)

**Base: `02b_v1.3-c.md`** (sha256 693dd23c…, 4,455 words) — the best version (iter. 3: +4.38 vs v1.1-c; §5.4 met). Result: `02b_v1.5-c.md` sha256 **36ab059b**ee95bcc65b8e75e572646e40f2b3b5024f7c569c15cf65d03a269477, **4,570 words** (+2.6 % vs v1.3-c; **+14.9 % vs v1.0**; limit 4,572 — margin 2 words). Machine-readable: `changes_v1.5.json` (41 exact replacements, applied with `e5_apply_changes.py`); text diff `changes_v1.5.diff`. Canon unchanged. Examples kept.

**Why systemic rather than three patches (v1.4-c draft):** in 180 v1.3-c judgments, the remaining errors form three classes, not three tasks. For each class the pack provides one rule, one thinking step and one self-check line. The length limit is respected by taking out duplicated text (not content).

## A. Evidence discipline — target: invented facts 0.11 → ≈ 0

| ID | Source | Location | What it does |
|---|---|---|---|
| CH19 | 20 invented-fact flags: unlabelled assumptions about cost/demand behaviour and "what can be afforded" (8), calendar dates without today's date (4), split of causes (3), a given date made more precise (2) | R1 (new; the old R1 duplicated L1), R2 | **R1:** about the person's situation only three kinds of sentence are allowed — a fact, shown arithmetic, a labelled assumption with sensitivity; everything else is a check to carry out; risk classes named directly (causes, cost/demand behaviour, third-party actions, typical values). **R2:** without today's date — only relative time, no inferred calendar dates; do not make a given date more precise; lowest balance with the day (formerly CH14) |
| CH18 | T03 r1: the judge flagged "three to five goals are enough" — this is the prompt's own L4 example with "usually" | L4 | example tied to the person's hours, without a general law |
| CH28 | source of the same class in the prompt itself: in the EMERGENCY example "a landlord usually allows a week" | example | → "ask the landlord today for a week" |
| CH37 | R8 example "a new outlet is usually at break-even or at a loss" — a typical value without a label | R8 | range "computed from their numbers"; shortened |
| CH30 | self-check | self_check | **final re-read sentence by sentence:** number, date, cause, cost assumption, "can afford" → fact / arithmetic / labelled; no inferred dates; plausible risks remain as hypotheses |
| CH15 | canon_gate para. 3 shortened (repetition "only when it changes the first action or the risk" twice); **includes former CH12** — market-scale risk | canon_gate | "a shift in their whole market and not only at their main client" |
| CH25 | T04 M7 18/18 — the environment check is not asked | step 8 | offsets (c): whether the force affects them specifically or the whole market; whether it exceeds the owner's means |

## B. Forecast depth — 11 lost pairs (T06, T08, T09): "never says when cash runs out", "start-up losses unfunded"

| ID | Source | Location | What it does |
|---|---|---|---|
| CH23 | T08 ×4, T06 ×6 | R13 | the no-change forecast names the month when the reserve crosses the red line and the month when it reaches zero; the worst case with the date when the payer / client / new project may fail; forecasts with numbers, not only directions |
| CH21 | T06 ×6: launch with only the fit-out funded | R8 | funding includes start-up losses: fit-out + ramp-up months |
| CH22 | T08 M4 4/18, T10 M6 3/18, T06 "never sizes the gap"; T08 "pay only wages, rent and materials" | R12 | dangers with the amount at risk and the impact in months; behind the urgent symptom — the biggest danger (the debtor may not pay at all; the drop may be a shrinking market); obligations are ranked, not dropped |
| CH30c | self-check | self_check | the danger/forecast/promise lines merged into one with the new depth |

## C. Usefulness of actions and choice — 11 + 6 + 3 lost pairs

| ID | Source | Location | What it does |
|---|---|---|---|
| CH20 | T01 ×4 ("defers the cash decision"), T10 ×5 ("written demand … waits until 30 Oct"), T02 ×2 ("never works out where its levers leave the cash"), T10 F4 (irreversible step today) | R7 | each action this week has a day and a person; the decision the numbers allow is made in the response; for the debtor — a written demand today with the person's own amount and date, also through a second channel; stoppages only as conditions with a trigger day; levers worked out down to the balance on the critical day |
| CH24 | T09 ×3 ("frames leaving as the risky side"), T07 ×2 ("imposes 'the concert is off'"), T06 | R14 + **R15 (new)** | exit / not opening / waiting among the options, which error is cheaper (formerly CH13); if the request already contains a plan the numbers do not support — the alternative as a real option with a price, the choice stays with the person, with a fallback path; **R15:** a direct instruction about form ("don't rewrite", "no questions") overrides the format (T03 M1 4/18, 3 lost pairs) |
| CH30 | self-check | self_check | actions with a day and a person; decision made; the written demand first; the irreversible one — a condition; the direct instruction followed |
| CH30f | T09 M5 | self_check | in the decision-date line — "and the exit among the options" |

## D. Shortenings (only duplicated text; content does not change)

| ID | What | Words |
|---|---|---|
| CH17/CH17b | L1 and L3a merged (one vocabulary table) | −32 |
| CH16 | P4 shortened (the assumption content moves to R1) | −21 |
| CH29 | CL8 (Titanic → CL7), CL15 (Bellman), CL16 (= step 5), CL20 (= R8), CL21 (= R6), CL23 (= L3/P1) removed; CL renumbered 1–17 | −97 |
| CH31 | R10 (status labelling) removed — covered by R1 and canon_gate; **R11–R15 numbering kept** for continuity | −23 |
| CH26, CH27, CH35 | question bank B/K/L and the long overview shortened | −30 |
| CH32, CH30b, CH30d, CH30e | duplicated self-check lines | −60 |
| CH33, CH34, CH36, CH38, CH39, CH40–CH48 | degradation_rule, role_and_context, iteration_note, L2/L3/L6, R4, step 5, canon_gate 1, PLAN CHECK 2, P1/P2/P5, FULL round, output para. 2 | −95 |

**Not changed:** L5 budgets, both examples (except the CH28 sentence), CH6 FULL round rule, CH7b hypothesis rule, CH10 PLAN CHECK ending, CH11 budgets, mode structure, output format.

## Acceptance rule and forecast (fixed before data; see `decisions_iter_5.md` D5.4)
§5.4 vs v1.3-c (the same iter. 3 responses, re-judged): Δ > 1.51 and CI lower bound > −1; no criterion drops > 1.0; violations do not increase; length +14.9 % ≤ +15 % ✓. Additional targets (not acceptance conditions, but to be reported): invented facts ≤ 0.03 per response; T04 M7 ≤ 6/18 equivalent (≤ 4/12); T09 M5 ≤ 3/12; T02 M4 0/12; pair preference ≥ 17 wins out of 30.
**Forecast:** +1.5 … +3.0 vs v1.3-c (ceiling effect: elements 97 %, violations 0); invented facts 0.11 → 0.00–0.03; pairs ≈ 18 : 7 : 5. **Risks:** (1) R1 strictness may cut off plausible risk hypotheses (iter. 2 CH7 effect) — counterweight: canon_gate and the self-check keep them explicitly; (2) the additional forecast content may exceed the EMERGENCY/QUICK budgets — L5 unchanged, examples kept; monitor H1 T02/T10/T08; (3) R7 "the decision is made" may clash with P5 "decisions belong to the owner" — R14 balances this.
