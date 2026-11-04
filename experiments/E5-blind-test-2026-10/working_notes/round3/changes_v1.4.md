# Change pack v1.4-c (candidate), 2026-10-18, after the iteration 3 error analysis

**Base: `02b_v1.3-c.md`** (sha256 693dd23c…, 4,455 words) — v1.3-c met §5.4 in iteration 3 (Δ +4.38 vs v1.1-c); it takes effect as the base upon Martin's approval. Result: `02b_v1.4-c.md` sha256 **d153e545**c764f9284c4d17e3bf10d6b497562d119e538b344b51b1b092466d00, 4,496 words (+0.9 % vs v1.3-c; **+13.1 % vs v1.0**; limit 4,572, reserve afterwards 76 words). Machine-readable diff: `changes_v1.4.json`, applied with `e5_apply_changes.py`; text diff `changes_v1.4.diff`. Canon unchanged.

**Status: draft — NOT approved and NOT being generated.** Martin's instruction 2026-10-18 10:32 Toronto: "finish this iteration … do not continue further for now". The pack was prepared only because it is the standard output of an iteration (29 §6 step 8).

| ID | Source (error analysis iter. 3) | Prompt location | What it does | Expected effect | Side risk |
|---|---|---|---|---|---|
| CH0 | — | heading | label v1.4-c | — | — |
| CH12 | T04 M7 12/12: AI hypothesis only about the main client; the CH7b example "a market shift that may reach their main client" narrowed it | `<canon_gate>` para. 3 (example) | example → "a shift in their whole market, not only at their main client" (+3 words) | T04 M7 ≤3/12; T04 +2…+4 | may add a general market claim without a label → invented facts must be monitored (≤0.3) |
| CH13 | T09 M5 5/12, M7 2/12: exit is not offered as an option; the cost of a mistaken exit is shown only as a threat | `<rules>` R14 | "Include an orderly exit among the options and say which of the two mistakes costs less." (+16) | T09 M5/M7 ≤1/12; T09 +1…+2 | may encourage offering an exit also where it is not needed (T06 expansion) → monitor T06 M5 |
| CH14 | T02 M4 4/12: shows the balance on day 2 and day 5, not the deepest point (−1,700) that determines the size of the bridge | `<rules>` R2 | "When money comes in and goes out on different days, show the lowest balance and its day, not only the end balance." (+22) | T02 M4 0/12; T01 (winter low point) unchanged or better | +1 sentence in the EMERGENCY response (270-word ceiling) → monitor T02/T10 H1 |

**Not changed:** CH6, the CH7b core, CH10, CH11 (all proven in iter. 3). The CH11 side effect (shorter responses; v1.1-c wins the pairs on T06/T08 with a deeper worst-case calculation; C2 −0.27 in the shared calls) **is not fixed** — only monitored.

**Acceptance rule (29 §5.4):** v1.4-c vs v1.3-c (the same v1.3-c responses, re-judged): Δ > 1.51 and CI lower bound > −1; no criterion falls by > 1.0; violations do not increase; length ≤ +15 % vs v1.0.
**Prediction:** **+0.5…+1.2** vs v1.3-c — **below the noise band ±1.51**. So even if all three changes work on their elements, §5.4(1) with 10 tasks × 3 replicates will most likely not be met. This is a decision point for Martin before any generation for iteration 4 (options: `comparison.md` §6).
