# Change pack v1.3-c (candidate), 2026-10-17, after the iteration 2 error analysis

**Base: `02b_v1.1-c.md`** (sha256 4af37472…, 4,333 words) — not v1.2-c, because v1.2-c did not pass §5.4 (Δ −2.18; violations 0.33 → 0.53). Result: `02b_v1.3-c.md` sha256 **693dd23c**c9a5857874b9c2873afc6554d198d429647c538e8ce1c4979333c113, 4,455 words (+2.8 % vs v1.1-c; **+12.0 % vs v1.0**; limit 4,572). Machine-readable diff: `changes_v1.3.json`, applied with `e5_apply_changes.py`. Canon unchanged.

**Status: draft — awaiting Martin's approval** before iteration 3 generation.

| ID | Origin | Prompt location | What it does | Expected effect | Side risk |
|---|---|---|---|---|---|
| CH0 | — | title | label v1.3-c | — | — |
| CH6 | v1.2 (proven: T04 F2/H2/M4/M8 → 0/6) | `<modes>` FULL points 1 and 2 | five questions = five "?"; the whole round under the budget (the number is now 420, see CH11) | T04 form is kept | together with CH7b, M2/M7 must be recovered |
| CH7b | v1.2 CH7, **fixed** | `<canon_gate>` point 3; `<self_check>` | external knowledge only as a check or a labelled assumption (CH7 core, invented facts 1.32 → 0.02) **+ a new sentence**: a risk that the person's facts make plausible (a client may not pay; a market shift may hit the main client; a safety rule may apply) is not dropped as "general" — name it as a hypothesis with a check to perform | invented facts ≤0.3; T04 M2/M7, T10 M6, T02 M2 back at the v1.1-c level | some hypotheses may again be presented as fact → monitor invented facts |
| CH10 | v1.2 (proven: T03 M8 6 → 0) | `<modes>` PLAN CHECK | ending on the missing reserve + 2–3 checks, never shortened | T03 gain is kept | none |
| CH11 | **new** (replaces the failed CH8) | `<rules>` L5 (the whole line) | internal budgets **≈10 % below the person's limit** as hard ceilings, counting headings and questions: EMERGENCY 270, QUICK 540 (2nd round 810), FULL round 420 in total, plan check 630, teenager/family 360 | H1/F2/F3/M8 violations in T02, T05, T07, T08 → ≤1/6 in each | too-short responses may omit elements (T01, T05) → monitor element % |

**Reverted (not in v1.3-c):** CH8 (the sentence "finish 10–15 % below" — the word count did not decrease), CH9 (R14 narrowing — no gain; T09 M5 2 → 4).

**Acceptance rule (29 §5.4):** v1.3-c vs v1.1-c (the same v1.1-c responses, re-judged in iter. 3): Δ > 1.51 and CI lower > −1; no criterion falls > 1.0; violations do not increase; length ≤ +15 % vs v1.0.
**Forecast:** +1.5…+3 vs v1.1-c (T02/T07/T05/T08 get back within budget, T03/T04 gains remain); invented facts ≤0.3; violations ≤0.25.
**Length warning:** +12.0 % vs v1.0 → 117 words remain for the iteration 4 pack.
