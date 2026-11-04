# E5 — error analysis after iteration 5 (v1.5-c vs v1.3-c; 2026-10-29)

**Data source:** 120 J1 (Opus 5.5) judgments in iteration 5 — 60 vs v1.3-c (the same iter. 3 responses, re-judged in the same call) and 60 vs A. Raw tables: `error_analysis_iter_5_raw.md` (v1.5-c, 12 judgments per task), `error_analysis_iter_5_raw_base_v1.3-c.md` (the base in the same calls, 6 per task); outcomes of all 30 vs-C pairs and judge rationales word for word: `v15_losses.txt` (`scratch/losses5.py`). Pre-registered targets: `decisions_iter_5.md` D5.4–D5.5; change pack: `changes_v1.5.md`. Numbers: `analysis/iter5_d54_check.txt`, `iter5_context_check.txt`.

## 1. What was achieved (against the targets fixed before data)

| Target (D5.4/D5.5) | Forecast | Result | Verdict |
|---|---|---|---|
| Invented facts per response | 0.11 → 0.00–0.03 | **0.008 (1 of 120 judgments)**; v1.3-c in the same calls 0.22 (13 flags in 60 judgments); A 1.70 | **achieved** |
| Violations | ≤ 0.05 | 0.000 (v1.3-c 0.017 — one F4 T10 r2) | achieved |
| T09 M5 (exit as an option) | ≤ 3/12 missing | **0/12** (v1.3-c 6/6 missing in the same calls; 10/18 iter. 3 + additional run) | achieved |
| T02 M4 (lowest cash point with the day) | 0/12 missing | **0/12** (v1.3-c 2/6; 6/18) | achieved |
| T04 M7 (AI affects the whole market) | ≤ 4/12 missing | **6/12** (v1.3-c 6/6 in the same calls; 18/18 iter. 3 + additional run) | partly — better by half, target not achieved |
| Δ vs v1.3-c | +1.5 … +3.0 | primary measure **+1.71** [+0.23; +3.36]; shared calls **+0.86** [−0.66; +2.43] | formally achieved, **not robust** (see §5) |
| Pair preference | ≥ 17 wins out of 30 (≈18 : 7 : 5) | **14 : 13 : 3** | not achieved |

Both accuracy targets and two of the three target elements are achieved, the third — halfway. The overall score rose little, because in parallel **new losses** appeared, which to a large extent erase the gain. This is the main finding of the iteration (§2–§3).

## 2. What v1.5-c is missing (elements; 12 judgments per task)

| Task → element | Missing v1.5-c | v1.3-c (18 judgm. iter. 3 + additional run) | What it means |
|---|---|---|---|
| **T09 M3** — the shrinking town named as the strongest force, which marketing alone will not overcome | **11/12** (new) | 0/18 | the v1.5 response mentions the shrinking of the town and turns it into a **question** ("is it your kiosk that is falling, or the whole town?"), rather than a conclusion. The judge: "leaves the town question open … a gesture, not a statement". This is an **R1 side effect**, which D5.5 had forecast as risk (1): the rule "everything else is a check to carry out" makes the model format even **a comparative conclusion that follows from the user's own numbers** (the town −25 % in five years is his fact) as an open question. |
| **T04 M7** — AI affects the whole market | 6/12 | 18/18 | CH25 (step 8, offsets (c)) worked in half of the cases: r1 in both judgments vs C and in one vs A; r2, r3 — no. The check is in the thinking step, but not in the self-check and not in the question bank |
| T03 M6 / M8 — threshold vs the competitor; link between the missing money and spending | 4/12; 2/12 | 0/18 | diagnosis shallower; the only place where the shortenings of the question bank (CH26/27/35) and L1/L3a may have taken away content |
| T04 M2 — dependency threshold checked against the goal | 4/12 | 0/18 | r1 offers a 30 % line, which it does not check against the €10,000 goal; v1.3-c checked 40 % |
| T08 M3 / M1 — the €14,000 gap as a **question**; which number governs | 2/12; 1/12 | 4/18 each | r2 turns the €14,000 gap into a task ("find out"), not a question to the owner — the same "check, not statement" tendency; r1, r3 good (r3 wins in both orders) |
| T10 M1 — written demand today | 2/12 (r2) | 1/18 | r2's first line breaks the EMERGENCY format; r1, r3 fulfil M1 (CH20 works: T10 r2, r3 win) |
| T05 M8 | 1/12 | — | in noise |

## 3. Why v1.5-c loses pairs (13 lost + 3 split out of 30; judge rationales word for word `v15_losses.txt`)

| Theme | Pairs | Judge's words (shortened) |
|---|---|---|
| **A. Wording of the danger T05 (3/3 lost):** "one weak month" as the main danger, which the person's own numbers refute; the shock that the reserve cannot absorb is not named (the owner's illness: €2,550 monthly costs vs the reserve); in turn 2 the riskiest assumption is not named; the effect assumed immediate, without ramp-up | T05 ×3 | "headline danger is undercut by its own numbers"; "never ranks its assumptions"; "assumes the effect starts immediately" |
| **B. Losses in numerical depth** — v1.3-c went further in some specific calculation: payback without materials (T06 r1: "flattering exactly the numbers the person wanted guaranteed"); data contradiction (the owner's salary not included in €6,500 — T01 r2); threshold not checked against the goal (T04 r2); "€1,700 a month cost of delay" as a fact (T01 r1 — the judge does not flag it as an invented fact, but names it in the rationale); the red-line shortfall does not add up (T07 r3) | T01 ×2, T04, T06, T07 | "presents an unsupported 1,700-a-month cost of delay as fact"; "misses the data contradiction and the bridging backstop" |
| **C. Conclusion turned into a question / check** (R1 too strict): the town as the strongest force (T09 r1); €14,000 as a task, not a question (T08 r2 split) | T09, T08 | "leaves the town-vs-kiosk question open"; "turns the 14,000 into a task rather than a question" |
| **D. Checkpoint ladder thinner**: one checkpoint after two months vs a full monthly ladder plan with an early check (T07 ×2); T10 r1 — day-5 credit-line trigger vs the v1.3-c day-3 trigger | T07 ×2, T10 | "relies on a single two-month checkpoint"; "its day-5 draw leaves housing exposed" |
| **E. Safety / third-party step skipped**: food at 9 °C — v1.3-c says throw it away, v1.5 moves it; postponing the repairman €1,400 (T02 r2) | T02 | "both gaps directly threaten the permit or customers' safety" |
| F. Diagnosis shallower (T03 r1/r3 — M8/M6) | T03 ×2 | "misses the cash-to-spending link and gives a shallower diagnosis" |

In the lost pairs the judge's confidence is still low (0.55–0.70); almost every rationale starts with "both are accurate, within budget, complete". The difference between v1.5-c and v1.3-c is **in the depth of one specific calculation or wording**, not in accuracy or form.

## 4. Where v1.5-c wins (14 pairs) — axis C worked, axis A worked

T01 r3, T02 r1/r3, T03 r2, T04 r1/r3, T06 r2/r3, T07 r2, T08 r3, T09 r2/r3, T10 r2/r3. Judge's words: "turns this week into dated, owner-specific steps with each lever priced" (T01 — CH20); "sizes its rescue plan precisely … says plainly that €200 is still missing" (T02); "attaches an owner and deadline to every check … stays strictly within 'don't rewrite'" (T03 — R15); "raises the market-wide AI hypothesis" (T04 r1 — CH25); "labels every assumption with the correct direction" vs v1.3-c "1,950 cannot carry an employee" (T04 r3 — R1); "sizes the full cash need including opening losses (21,800 to find externally)" (T06 — CH21); "quantifies the big-customer default as cutting the runway to about 1.5 months, asks directly about the €14,000" (T08 — CH22/CH23); "names an orderly exit as a real option … a long renewal is costlier than a wrong exit" (T09 — CH24); "opens with a written demand with a deadline today plus a second channel … makes the client's default the main danger" (T10 — CH20/CH22). Vs A: 30/30 pairs, 60/60 judgments in favour of v1.5-c (confidence 0.65–0.90).

**Invented-fact classes of v1.3-c in the same calls (13):** calendar dates without today's date (5: T09 ×3, T10 ×2), unlabelled assumption about cost behaviour / "what can be afforded" (4: T04 ×2, T08 ×2), third parties / general law (2: T07), other (2). v1.5-c: **none** of these classes; the only flag (T03 r2 vs A, "minor") is **the sentence of the prompt's own L4 example** after the CH18 fix ("With your hours, three to five can get real work this year") — the fix was insufficient, the number must be removed entirely.

## 5. Measurement finding: the primary Δ measure is biased in favour of the version under test

`iter5_context_check.txt`: a C response judged next to A receives an overall score higher by **+1.1…+2.7** than the same response next to another C version (iter. 1 +2.70; 2 +1.11; 3 +1.87; 5 +1.71). In each iteration the version under test is judged 60 times vs A and 60 vs the base, but the re-judged base — only 60 times vs the version under test. Therefore the primary measure (all judgments) carries ≈ half of the context effect (+0.9 v1.5-c). Three views on v1.5-c − v1.3-c: **+1.71** (primary) / **+0.86** (shared calls) / **−0.12** (symmetric: v1.5-c iter. 5 vs v1.3-c iter. 3, both 120 mixed; contains judge drift). In iteration 3 the bias did not change the verdict (+4.38 / +3.45 — both above the band); in iteration 5 it decides whether criterion (1) is met. Recommendation for the protocol (decision for Martin, 30 §10): from iteration 6 the primary Δ = the shared-calls measure, but with 6 replicates (120 shared calls), to regain power; "all judgments" remains as an additional metric.

## 6. Conclusion for the design (v1.6 draft `changes_v1.6.md` — not generated)

1. **Axis A (R1/R2) reached the target — invented facts 1/120 — and in one place overshot it**: the model formats as a "check" even a comparative conclusion that follows from the user's own numbers (T09 M3) and the necessary question to the owner (T08 M1). The fix is one sentence in R1 (a comparison between the person's own numbers is shown arithmetic and is said as a statement with both numbers) and one in R7 (an unknown number that changes the decision is a question, not a task).
2. **Axis B (forecast depth) worked where there was a specific rule** (T06 start-up losses, T08 months to zero, T10 biggest danger), **but T05 reveals a hole**: "danger" is not defined as *a shock that the reserve cannot absorb* (monthly costs vs the reserve), and "the riskiest assumption" is not named.
3. **Checkpoints** (T07 ×2, T10 r1): for a path longer than two months — a checkpoint every month, the first ≤ 4 weeks; a trigger that protects a fixed payment fires with margin before the payment day.
4. **Payback at full cost** (T06 r1) and **data contradiction** (T01 r2): R8.
5. **L4 example without a number** (T03 r2 invented fact); **T04 M7** — environment check also in the self-check, not only in step 8.
6. **Shortenings**: T03 M6/M8 is the only place where the shortenings of the question bank / L1 may have taken away content; elsewhere the shortenings left no trace (elements 96.7 % vs 95.0 %).

The measurement-sensitivity note from iter. 3 remains valid and is strengthened by §5: with the 10 × 3 design and a biased primary measure, Δ below ±1.5 cannot be distinguished; the v1.5-c gains are provable **at the level of elements and accuracy** (invented facts ≈ 0, violations 0, T09 M5 and T02 M4 0/12, T04 M7 18/18 → 6/12), not in the overall score.
