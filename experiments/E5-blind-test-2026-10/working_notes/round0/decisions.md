# Iteration 0 — decisions (with rationale)

Source: `working_notes/e5_run_log.md` (timestamps), `working_notes/29_E5_protocol.md` (rules), `error_analysis/`.

| # | Decision | Rationale | Where documented |
|---|---|---|---|
| D0.1 | Generator = Claude Sonnet 5.5; judge J1 = Claude Opus 5.5; k = 3 replicates; C-v1.0 in two independent blocks (runs 1–3, 4–6) to measure the noise band | 29 §2–3, Martin's choice "standard configuration" | 29 §2.3, 30 §6.3–6.5 |
| D0.2 | Pair plan: C block 1 vs A (r vs r), C block 2 vs B; both orders | 29 §4 | 30 §6.7, `packs/judge_index.csv` |
| D0.3 | If an agent returns the response in a message rather than in a file, the orchestrator saves it word for word (11 cases: A ×6, B ×5) | The content is identical; regenerating would change the sample | log, 15 October |
| D0.4 | Wrapper v1 → v2 → v3 (only the text of the file task, not part of the conversation with the model) | So that the agents write a file instead of replying in a message | log, 15 October, `E5_RESTORE.md` |
| D0.5 | Correction of the T01 gold facts before freezing (date the money runs out: February, not January) | Arithmetic error in the task key; 29a hash recalculated | 29 §8 |
| D0.6 | Judge calibration performed after iteration 0 (identity ×3, planted error ×2, length ×2): PASS; judge prompt v1 stays | Time sequence; the result shows no systematic bias | 30 §10, `cross_check/judge_calibration_and_J2/` |
| D0.7 | Iteration 0 result frozen as `analysis/e5_results_iter_0_snapshot.csv` + `e5_pairwise_iter_0_snapshot.csv` (240 + 120 rows = all 120 judgments) | The pre-registered analysis was run on this record at 04:10 | `e5_run_config.json` (`frozen_*`) |
| D0.8 | Change pack v1.1-c: 5 changes (CH1–CH5), prompt +9.0% words (≤ +15%) | Error analysis: FULL round (T04), external knowledge without labeling, T06 M7, T03 M3, T09 M5 | `error_analysis/changes_v1.1.md` |
| D0.9 | Hold-out (H01–H10) is not measured in iteration 0; it is measured together with the final round (A, B, C-v1.0 and C-final on the hold-out on one day) | Budget; a single day reduces time drift | 30 §10 (to be recorded) |
| D0.10 | LOSS: the prose text of 9 judgments (T09 r5 21; T09 r6 12/21; T10 r4–r6 12/21 vs B) is not in the archive; the numbers are in the snapshot. Re-judgment as test–retest (`judgments/iter_0_rejudge/`), without changing the frozen result | The bundle was not re-packed after the last batch; in the second context loss the container disappeared | `e5_STATUS_2026-10-16.md (working file, not included)` §3 |
