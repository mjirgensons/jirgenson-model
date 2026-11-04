# Iteration 2 — decisions (with rationale); status: judging and analysis completed (120/120); change pack v1.3-c awaiting Martin's approval

| # | Decision | Rationale | Where documented |
|---|---|---|---|
| D2.1 | Martin approves v1.1-c as the base and the pack v1.2-c (16.10. 19:13 Toronto); orchestrator → Claude Opus 5.5 (Fable limit) | 29 §6 steps 8–9; the orchestrator is not a measured component | log 23:13, `E5_RESTORE.md` HANDOVER |
| D2.2 | Prompt v1.2-c (CH0 label, CH6–CH10) sha256 eb465d4a…, 4,487 words; 30 generations Sonnet 5.5, 0 transcriptions | — | `prompt/02b_v1.2-c.md`, log 23:15–23:45 |
| D2.3 | Pairs: C-v1.2-c r vs A r (iter. 0) and vs C-v1.1-c r (iter. 1), r = 1..3, both orders = 120 | the same plan as D1.3 | `packs/judge_index.csv` |
| D2.4 | The generation agent's verbatim text for iter. 0–1 was not archived; in iter. 2 the text of the E5_RESTORE HANDOVER section was used ("exactly two tool calls") — the substance is the same | deviation 30 §10 | log |
| D2.5 | Judging batch 1 (18) was not recorded in the log; 6 files existed only in the working environment at the session break; restored 17.10. 01:50 without data loss | a process gap, not a data gap | log 01:50 |
| D2.6 | Classifier stops: 7 before writing → repeated (D1.5); 2 after writing → used | ≈14 % of calls, as in iter. 1 | log 01:55–02:50 |
| D2.7 | Result frozen: `e5_results_iter_2_snapshot.csv` (240), `e5_pairwise_iter_2_snapshot.csv` (120); summary from the frozen record identical | D0.7 procedure | `analysis/`, `e5_run_config.json` |
| D2.8 | **§5.4 v1.2-c: (1) Δ −2.18 < 1.51 ✗; (2) criteria do not fall > 1.0 ✓ (C2 −0.6), violations 0.33 → 0.53 ✗; (4) +12.9 % ✓ → v1.2-c REJECTED; the base remains v1.1-c** | Pre-registered rule applied mechanically | `analysis/summary.md`, `comparison.md` |
| D2.9 | Error analysis: CH6 form ✓ / content ✗ (because of CH7), CH7 core ✓✓ (invented facts 0.02) with an excessive side effect, CH8 ✗, CH9 ✗, CH10 ✓ | 120 judgments, element table 5b | `error_analysis/error_analysis_iter_2.md` |
| D2.10 | Pack v1.3-c **on the v1.1-c base**: CH6 + CH7b (CH7 + permission for risk hypotheses) + CH10 + CH11 (lower L5 numbers); CH8, CH9 reverted. sha256 693dd23c…, 4,455 words (+12.0 % vs v1.0) | 29 §6 step 8; "what improved — we keep, what worsened — we revert" (Martin 16.10.) | `error_analysis/changes_v1.3.md/.json` |
| D2.11 | Iteration 3 generation **does not start** until Martin's approval | 29 §6 steps 8–9 | log |
| D2.12 | Log timestamps 01:55–04:20 were estimated (0–79 min too late); the correction added as a new entry, the old ones are not overwritten; actual times from file mtime | traceability; time from `date -u` from now on | log 03:11 |
| D2.13 | Archive structure aligned: all iterations (0–4, final) have one and the same 13-folder structure with `_STATUS.md` and INDEX.csv; missing parts filled in (iter. 0–1 gen packs restored and checked, changes_v1.1.json derived and checked, .diff for all packs, iter. 0 comparison) | Martin's instruction 2026-10-17 01:43 Toronto: "save it with the correct structure, so that all iterations have the same structure" | log 05:52, 30 §10, `ARCHIVE_README` |
