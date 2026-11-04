# 29. Experiment E5: iterative optimization of the operating prompt (protocol v1)

**Date:** 2026-10-15 (Toronto). **Author:** Claude (Fable 5.1) at Martin's request; decisions — Martin's.
**Status:** protocol prepared; iteration 0 **not started**. Before starting, the §11 checklist must be completed and the §12 questions answered.
**Related files (reproducibility package):**

| File | Content | Status |
|---|---|---|
| `29_E5_protocol.md` | this document | v1 |
| `29a_E5_TASKS_DEV_v1.md` | 10 development tasks (T01–T10): texts, answer key | **frozen**, hash §8 |
| `29b_E5_TASKS_HOLDOUT_v1.md` | 10 hold-out tasks (H01–H10), sealed | **frozen**, hash §8 |
| `29c_E5_JUDGE_PROMPT_v1.md` | judge prompt, rubric, formula, calibration | v1 |
| `29d_E5_CONTROL_PROMPTS_v1.md` | conditions A / B / C, control prompt B | v1 |
| `02a_CANON_v1.0_EN.md`, `02b_OPERATING_PROMPT_v1.0_EN.md` | canon (fixed) and prompt v1.0 (starting point) | existing |
| `registry/e5_results_template.csv`, `registry/e5_pairwise_template.csv` | results table format | v1 |
| `scripts/e5_analyze.py` | statistics and charts from the results CSV; demo with synthetic data | v1 |
| `scripts/e5_hardchecks.py` | automatic checks (word count, questions, language, forbidden words) | v1 |

---

## 0. Summary on one page

**Question.** Can the operating prompt (02b) be made measurably better through controlled iterations, and how large is its contribution compared with (A) the model without a prompt and (B) a good general consultant prompt?

**How.** 10 frozen tasks × 3 conditions × 3 replicates × a blind LLM judge with a pre-prepared answer key. After each iteration: error analysis → 1–5 targeted changes are introduced into the prompt, with a hypothesis recorded for each change → new version vN+1 → the same test. Five cycles. At the end: a hold-out set (10 other tasks, sealed) that is not used in any decision, and a check on other models.

**Decision rule (fixed in advance).** Version vN is accepted if on the development set its mean total score exceeds vN−1 by more than the noise band (§5.2), none of the six criteria worsens by more than 1 point, and (when measured) the hold-out set is not worse than vN−1 by more than the noise band. Otherwise the changes are reverted or split (ablation).

**What the experiment proves and what it does not.** It proves: with these tasks, this model, this judge and this rubric, version vN gives a score X points (95% CI …) higher than v1.0 / than A / than B. It does not prove: that the prompt "eliminates hallucinations", that it works with any model or any task, that the LLM judge's score matches a human's judgment (see §9). Wording in sales texts: only after D11 (07).

**Main differences from E1 (Appendix J).** Full task texts, the judge prompt and the answer keys are saved and frozen; 3 replicates, not 1; the judge is blind, with position swapping; a second control condition B; a hold-out set against overfitting; statistics with confidence intervals; every prompt change with a hypothesis and a recorded result.

---

## 1. Goal and hypotheses

**Goal.** Step by step, with a repeatable procedure, improve the operating prompt (02b) without changing the canon (02a), and show the improvement in each iteration with numbers and charts.

**Pre-registered hypotheses.**
- **H1 (the book's claim).** C(v1.0) > A: with the canon and the prompt the score is higher than without them. Expected based on E1 (+7…+11 points on the 60-point scale).
- **H2 (content vs structure).** C(v1.0) > B: the contribution does not come only from good structure. *Never tested.* This is the scientifically most important comparison.
- **H3 (iterations).** C(vN) ≥ C(vN−1) in each accepted iteration; C(v1.5) − C(v1.0) > 0 with a 95% CI that does not include zero.
- **H4 (transfer to other tasks).** The improvement C(v1.5) − C(v1.0) on the hold-out set is at least half of the improvement on the development set. If not — the prompt is overfitted to 10 tasks.
- **H5 (transfer to other models).** The sign of the improvement holds on at least 2 of the 3 other models (Opus 5.5, Haiku 5.5, Fable 5.1 / or an external model).

**Null hypothesis in each comparison:** mean paired difference = 0. The noise band is measured in iteration 0 (§5.2), not assumed.

**What is optimized.** Only the text of `02b`. The canon `02a` is fixed at v1.0: if the error analysis shows that the problem is in the canon, it is recorded as a "canon candidate" for the next experiment (E6), but it is not changed in this experiment.

---

## 2. Design

### 2.1 Variables

| Role | Variable | Values |
|---|---|---|
| Independent | condition | **A** no prompt; **B** general structured consultant prompt (29d); **C** canon v1.0 + prompt vN |
| Independent | prompt version | v1.0 (iter. 0), v1.1-c … v1.5-c (candidates), accepted ones become v1.1 … |
| Dependent | total score 0–100 (29c formula) = elements 40 + criteria 60 − 2 × violations | |
| Dependent (secondary) | element %, criteria sum (comparable with the E1 60-point scale), the 6 criteria separately, number of violations, number of invented facts, pairwise win share, hard checks | |
| Controlled | generating model and version, temperature/default, delivery mode (API/chat), date, task texts, judge prompt and model | fixed within an iteration, recorded |
| Blocking | task (T01–T10) | paired comparison by task |

### 2.2 Models

- **Development (generating) model:** **Claude Sonnet 5.5** — the middle tier, where prompt quality is more visible than on the strongest model (ceiling effect), and which matches what most readers will use. *Alternative:* Haiku 5.5, if the goal is robustness on the weaker model (E1 showed that it is exactly there that the combination limps).
- **Judge J1:** **Claude Opus 5.5** (the strongest available; continuity with E1). **Judge J2:** a model from another family (GPT or Gemini), if Martin has access; if not — Fable 5.1. J2 judges in iteration 0 (calibration and agreement) and in the last iteration; J1 judges in all.
- **Confirmation models (last iteration):** Opus 5.5, Haiku 5.5, Fable 5.1 and, if possible, one external model — only C(v1.0) vs C(v1.5) and A.
- The judge and the generator **must not** be one and the same model (self-preference bias). If J1 = Opus, then the Opus confirmation round is judged by J2.

### 2.3 Replicates and volume

Each (task × condition) is generated **k = 3** times in independent new conversations (temperature — the interface default; not 0, because the reader gets the default; recorded). Two configurations:

| | Standard (recommended) | Minimal |
|---|---|---|
| Iteration 0 | A, B, C(v1.0) × 10 tasks × k=3 = 90 generations + C(v1.0) second independent block (noise) 30 = **120**; hold-out set A, B, C × 10 × 3 = **90** | A, C × 10 × 2 = 40; hold-out A, C × 10 × 2 = 40 |
| Iterations 1–5 (each) | A (repeated, concurrent control), C(vN−1), C(vN) × 10 × 3 = **90** | C(vN) × 10 × 2 = 20 (A and C(vN−1) from the previous round) |
| Last iteration, additionally | hold-out set C(v1.5), B × 10 × 3 = 60; 3 confirmation models × C(v1.0), C(v1.5), A × 10 × 2 = 180 | hold-out C(v1.5) × 10 × 2 = 20 |
| Judge calls | ≈ 2 × generations (each pair in two orders) + pairwise comparisons | ≈ 2 × |

The minimal configuration is fit for a fast internal loop; **a publishable conclusion only from the standard configuration**.

### 2.4 Task sets

- **Development set (29a):** T01–T10, frozen. All decisions about prompt changes are made on it.
- **Hold-out set (29b):** H01–H10, frozen and sealed (hash §8). Used only for measurement: in iteration 0, optionally in iteration 3 (the results are saved in a file that the prompt editor does not open), and in the last iteration. **No prompt change may be justified by a hold-out set result.**
- Coverage: the 10 tasks include all modes (EMERGENCY ×2, QUICK ×4 incl. the two-step "no more data", FULL round 1, PLAN CHECK, teenager), three languages (EN ×8, LV, RU), and each task has its own "trap" (table at the start of 29a). No situation coincides with the book's characters or with the E1 situations.
- Each task has, prepared in advance: *gold facts* (arithmetic that the judge recalculates), 8–10 mandatory elements with a "why" rationale, 3–5 forbidden elements, a word and question budget.

### 2.5 Iteration cycle

```
iter 0  ──►  iter 1  ──►  iter 2  ──►  iter 3  ──►  iter 4  ──►  iter 5
v1.0         v1.1-c       v1.2-c       v1.3-c       v1.4-c       v1.5-c
A, B, C      A, C(prev),  …            … (+holdout  …            A, B, C(prev), C(new)
+noise       C(new)                     unopened)                 + holdout + 3 models
```

In each iteration: generate → hard checks (script) → judge (blind, 2 orders) → analysis (script) → error analysis → change pack with hypotheses → new version → log. Details in §6.

**Stopping rules.** (a) Two iterations in a row without an acceptable change → stop, perform an ablation and review the rubric or the tasks, rather than keep "pushing". (b) If the hold-out set in iteration 3 shows a drop > noise band vs v1.0 → overfitting: return to the last version for which this was not the case.

---

## 3. Task set principles (how they were made and how they may be changed)

1. **One trap per task**, corresponding to a specific prompt rule (R8 guarantees, R12 the most dangerous thing as an event with a date, §9.5 growth in the red zone, CL19 "no more data", L1 language, MODE 1 do not rewrite, offset (b) contradiction in the data, offset (c) dying environment). That way the judge's results show *which* rule is not working.
2. **The answer key is grounded in the reader's benefit, not in the prompt's words.** Each mandatory element has a "why" (what it gives the person), so that the element list does not merely reward "looks like the method". Several elements deliberately work *against* a long, structured response (word budget, no jargon, no questions).
3. **Arithmetic verified** with a script before freezing (all gold facts recalculated on 2026-10-15).
4. **Freezing:** after the hash is recorded (§8), the task texts are not changed. If the judge finds an error in the key, it is recorded in the log, the corrected version is marked v2, and comparisons between v1 and v2 results are not made.
5. **The hold-out set is structurally parallel** (each H mirrors some T), so that H4 measures transfer to *other situations*, not to *other skills*.

---

## 4. Scoring

### 4.1 Rubric (29c)
- **Mandatory elements (40 pts)**: task-specific, binary, with an evidence quote.
- **Six criteria (60 pts)**: C1 accuracy and no invented facts; C2 depth of diagnosis; C3 practicality of the steps; C4 fit to the request, time, language; C5 control quality (priorities, thresholds, measurement, next check); C6 honesty (no guarantees, ranges, two forecasts). The same six as in E1 — so the 60-point sum is comparable with the Appendix J table (with the caveat that the judge prompt is now different).
- **Violations**: forbidden elements + failed hard checks; −2 pts each.
- **Pairwise preference**: which one better serves the person this week; a win only if it agrees in both orders.

### 4.2 Blinding and positions
The judge does not see the system prompts, the condition or the model names. Each pair is judged twice with the order swapped; the results are averaged. **Acknowledged limitation:** C responses can be recognized by their structure, so blinding is partial; mitigation — judge rule 1 (structure earns nothing), control condition B (also structured) and length calibration (29c).

### 4.3 Hard checks (script `e5_hardchecks.py`)
Word count vs budget; number of questions; language (share of Latin/Cyrillic/Latvian diacritics); internal markers ("§", "EMERGENCY", "QUICK", "canon", "according to the model"); jargon in the teenager/family tasks; numeric inconsistency (judge). The script gives an objective value, the judge a second one; discrepancies are recorded.

### 4.4 Judge independence and agreement
- Judge ≠ generator. Preferably from another family (J2).
- Calibration before iteration 0 (29c): identity test, planted-error test, length test, two-judge agreement on 10 pairs (mean absolute difference in the criteria sum; Cohen's kappa for preference; threshold κ ≥ 0.4, otherwise the rubric anchors are refined and the version is changed).
- The judge recalculates the arithmetic itself (as in E1).

---

## 5. Statistics and decision rules

### 5.1 Basic unit
Paired difference **by task**: for each task the mean over k replicates and 2 orders, then the difference between conditions (C − A, C − B, vN − vN−1). n = 10 pairs (tasks); additionally — by replicate (n = 30) as a sensitivity analysis.

### 5.2 Noise band (iteration 0)
C(v1.0) is generated in two independent blocks (3 + 3 replicates, on different days or in different sessions). The difference between the blocks by task gives the **test–retest noise**: its standard error SE₀. **Noise band = 2 × SE₀** (for the mean total score). The minimum detectable effect (MDE) is recorded in the log before iteration 1. As a rough guide (from the E1 spread): if SE₀ ≈ 1.5 pts, the band ≈ 3 pts on the 100-point scale.

### 5.3 Calculations (script `e5_analyze.py`)
- Mean, SD, **bootstrap 95% CI** (10,000 resamples by task) for each paired difference.
- **Wilcoxon signed-rank test** by task (n = 10; low power, so the CI is the main measure) and the sign test.
- **Effect size**: Cohen's d for the paired difference.
- **Win share** in the pairwise preference with a Wilson 95% CI.
- Criteria separately (6 lines), element % and violations — to see *where* the version improves and whether anything gets worse.
- Multiple-comparison correction: there is one main test per iteration (vN vs vN−1 on the total score); the rest are descriptive.

### 5.4 Acceptance rule for version vN (fixed in advance)
1. Δ(vN − vN−1) in the total score on the development set > noise band **and** the lower bound of the bootstrap 95% CI > −1 pt;
2. no criterion C1–C6 drops on average by more than 1.0 pt; the number of violations does not increase;
3. if the hold-out set was measured in that iteration: Δ on the hold-out set > −noise band;
4. the prompt length (tokens) has not grown by more than 15% vs v1.0 without a proven benefit (a long prompt is a risk in itself, 02b degradation_rule).
If 1. holds but 2. does not — the change pack is split and repeated (ablation). If nothing holds — the version is rejected, and the hypotheses are recorded as rejected.

### 5.5 Final conclusion (iteration 5)
Report: C(v1.5) − C(v1.0), C(v1.5) − A, C(v1.5) − B on the development and hold-out sets, with CIs; win shares; by criterion; on the 3 confirmation models. Wording: "with these tasks, models, judge and rubric". No "proven in general".

---

## 6. Iteration procedure (steps for one iteration)

| # | Step | Who does it | Output / file |
|---|---|---|---|
| 1 | Freeze version vN-c: text, SHA-256, token count | editor (Claude) | `e5/prompts/02b_v1.N-c.md`, log |
| 2 | Generate responses: for each (task, condition, replicate) a new conversation; in two-step tasks the 2nd message is sent word for word | executor (§7) | `e5/responses/iter_N/{cond}_{task}_{run}.md` + `responses_index.csv` (model, date, delivery mode) |
| 3 | Hard checks | script | `hardchecks_iter_N.csv` |
| 4 | Prepare judge packs: pairs (C(vN) vs A; C(vN) vs C(vN−1)), random order, both orders; labeled "Response 1/2"; key from 29a | script/executor | `judge_packs_iter_N/` with the random seed |
| 5 | The judge scores; the JSON is parsed | J1 (and J2 in iter. 0 and 5) | `judgments_iter_N.csv` (long format) |
| 6 | Analysis: tables, CIs, charts | script | `e5/figures/iter_N/…png`, `summary_iter_N.md` |
| 7 | **Error analysis** on the development set only: each failed element/violation in the C(vN) responses is classified: (a) the rule is in the prompt but is not followed; (b) there is no rule; (c) the rules are contradictory/unclear; (d) model capability limit; (e) judge error. Table: task × element × class | editor | `error_analysis_iter_N.md` |
| 8 | **Change pack vN+1-c**: 1–5 changes; for each: ID, target error class and elements/tasks, prompt section, exact diff, expected effect (which criteria/tasks), side risk. No more than one change in one prompt section per hypothesis | editor; Martin approves | `changes_v1.N+1.md` |
| 9 | Decision on vN per §5.4; entry in 01 (version), 02 (prompt library), 03 (E5 row), 07 (decision) | Martin | project documents |

**Error analysis discipline.** The rationale for changes may rely only on the C(vN) responses on the development set. The task texts, the key and the judge prompt are *not changed* in order to "improve" the result. If the error class is (d) — a model limit — it is recorded, rather than "pushed" with even longer rules.

**Time and volume estimate for one standard iteration:** 90 generations + ≈ 200 judge calls. With subagents in this environment: 2–4 hours of machine time in batches; manually in chat interfaces: ≈ 2–3 working days; with an API script: < 1 hour.

---

## 7. Execution options

| Option | How | Pros | Cons | When to use |
|---|---|---|---|---|
| **(a) In this chat with subagents** | Claude launches a separate agent (sonnet/opus/haiku/fable) for each (task, condition, replicate), each with a clean context; the judge — another agent with 29c | fast; everything stays in the project; full recording | A is not "clean" (the agent has the environment's system prompt → label `A-harness`); one model family; the judge in the same family | iteration loop 1–4 (fast learning) |
| **(b) Manually in chat interfaces** (claude.ai, ChatGPT, Gemini) | Martin following the run-sheet: new conversation, attachment, prompt, task; copies the responses into files | clean A; judge from another family; matches how the reader uses it | slow; human errors in copying; temperature unknown | calibration (J2) and final confirmation |
| **(c) API script** | Python with the Anthropic/OpenAI/Gemini API, fixed parameters, automatic recording | the cleanest, most reproducible, cheapest in time | needs API keys and a little development; the API may not be reachable from this environment | final confirmation and the publishable version |

**Recommendation:** iterations 0–4 via (a) with full recording; iteration 5 (final) via (c) or (b) with a clean A and a judge from another family. Conclusions about H1/H2 are published only from (b)/(c) data.

**Run-sheet for one generation (all options):**
1. New conversation, without memory and project knowledge (C: only the canon).
2. C: attach `02a` → send `02b vN` → send the task's 1st message. B: system prompt from 29d → task message. A: task message only.
3. In two-step tasks: after the response, send the 2nd message word for word.
4. Save the response(s) in the file `{cond}_{task}_{run}.md`; in the index: model, version, date/time, delivery mode, temperature (if known).
5. No edits to the responses. If the interface truncates a response — record it and repeat (new conversation), keep the original.

---

## 8. Reproducibility package and hashes

SHA-256 of the frozen files (computed 2026-10-15; verify with `sha256sum`):

| File | SHA-256 |
|---|---|
| `29a_E5_TASKS_DEV_v1.md` | `{{HASH_29A}}` |
| `29b_E5_TASKS_HOLDOUT_v1.md` | `{{HASH_29B}}` |
| `29c_E5_JUDGE_PROMPT_v1.md` | `{{HASH_29C}}` |
| `29d_E5_CONTROL_PROMPTS_v1.md` | `{{HASH_29D}}` |
| `02a_CANON_v1.0_EN.md` (the user's 2026-10-13 file) | `{{HASH_02A}}` |
| `02b_OPERATING_PROMPT_v1.0_EN.md` (the user's 2026-10-13 file) | `{{HASH_02B}}` |

For each iteration, record: model IDs and version strings, date, delivery mode, temperature, the random seed for the pair order, the judge prompt version, all response files, all judge outputs (full text, not only the JSON), the script version. Someone else who has this package can repeat the experiment; **the numbers are expected to differ within the noise band, but the sign and size of the effect are not.**

---

## 9. Threats to validity and mitigation

| Threat | Why it is a threat | Mitigation in this protocol | Remains |
|---|---|---|---|
| LLM judge ≠ human | the judge may reward form, length, "persuasiveness" | rubric with anchors; rule 1; length calibration; recalculation of arithmetic; two judges; B control | yes: there is no human judgment. Recommendation: 2–3 real entrepreneurs judge 10 pairs at the end of iteration 5 |
| Self-preference (judge in the same family) | Claude may prefer Claude's style | J2 from another family; kappa check | partly, if J2 is not available |
| Partial blinding | C responses are recognizable by structure | position swapping; B with a similar structure; the judge is forbidden to mention the method | yes |
| Key written "according to the prompt" | the elements may reward following the prompt, not benefit | each element has a "why" for the reader; several elements against length/jargon; the six general criteria reported separately | partly; that is why the criteria sum and the B comparison are also reported |
| Overfitting to 10 tasks | 5 iterations on the same tasks | sealed hold-out set; H4; stopping rule (b) | yes, if the hold-out set is also written by a single author |
| The author writes both the tasks and the prompt | knowledge of the tasks influences the prompt changes | tasks frozen beforehand; hold-out set results unopened until the end; changes justified by error classes, not by the task | partly |
| Randomness (stochastic output) | one generation = noise | k = 3; noise band measured; CI | yes, with small n |
| Model version change during the iterations | the result changes without a prompt change | A repeated in each iteration (concurrent control); version strings recorded | partly |
| A is not "clean" in option (a) | the environment's system prompt | label `A-harness`; final confirmation with `A-clean` | yes, in iterations 1–4 |
| A long prompt degrades the model | each iteration adds rules | token limit §5.4(4); changes can also *shorten* | — |
| Multiple-comparison inflation | many criteria, many tests | one main test per iteration; the rest descriptive | — |

---

## 10. Charts (what each one shows; file names from the script)

1. `fig1_total_by_iteration.png` — **the main one**: mean total score (0–100) by iteration for three lines: A, B (only where measured), C(vN); 95% CI; a horizontal noise band around v1.0. Answers: does each iteration improve.
2. `fig2_criteria_by_version.png` — the six criteria (1–10) by version, grouped bars. Answers: *where* the improvement is (and whether something drops).
3. `fig3_task_heatmap.png` — heatmap: task × version, value = C − A difference. Answers: which tasks (traps) remain unsolved.
4. `fig4_winrate.png` — pairwise win share of C vs A and C vs vN−1 with Wilson CIs. Answers: how often C is better, independently of the scale.
5. `fig5_dev_vs_holdout.png` — development vs hold-out set for each measured version. Answers: overfitting (H4).
6. `fig6_distribution.png` — box plots (all replicates) by version. Answers: whether the worst case also improves, not only the mean.
7. `fig7_elements_violations.png` — element % and the mean number of violations by version. Answers: whether the prompt is *followed*.
8. (in the last iteration) `fig8_models.png` — C(v1.0) vs C(v1.5) vs A on each confirmation model (H5).

The script `scripts/e5_analyze.py demo` generates all the charts from **synthetic** data (clearly labeled), so that the format can be approved before there is real data. Real data: `e5_analyze.py run --results … --pairwise …`.

---

## 11. Checklist before iteration 0

- [ ] Martin approves: development model (Sonnet 5.5), judge J1 (Opus 5.5), J2 (another), execution option (§7), configuration (standard/minimal).
- [ ] 29a/29b read and approved (or corrections made **before** the hash is recorded); after that the hash is recorded in §8 and the files no longer change.
- [ ] `02b v1.0` text copied to `e5/prompts/02b_v1.0.md`, hash and token count recorded.
- [ ] Judge calibration (29c): identity, planted-error, length tests; J1–J2 agreement on 10 pairs (κ ≥ 0.4).
- [ ] The scripts run on the demo data; the CSV templates are understandable.
- [ ] Hold-out set results folder created with the rule "do not open until iteration 5".
- [ ] Entry in 03 (E5 row "STARTED", date) and 07 (decisions on the models and the option).

---

## 12. Open decisions for Martin

1. **Execution:** iterations 0–4 in this chat with subagents (fast, `A-harness`), the final round via API/chat (`A-clean`)? Or everything manually?
2. **External judge J2:** is there access to GPT or Gemini (chat is enough for the calibration and the final round)? If not — J2 = Fable 5.1, with the caveat in §9.
3. **Development model:** Sonnet 5.5 (recommended) or Haiku 5.5 (weaker-model robustness)?
4. **Configuration:** standard (k = 3, A repeated in each iteration) or minimal?
5. **Human check at the end:** are there 2–3 entrepreneurs who would judge 10 pairs (by the same rubric)? That would be the first non-LLM data point.

---

## 13. Log (filled in as the iterations proceed)

| Date | Iteration | Version | Model / judge | Dev: C − A (CI) | Dev: vN − vN−1 (CI) | Holdout | Decision | Notes |
|---|---|---|---|---|---|---|---|---|
| 2026-10-15 | — | v1.0 | — | — | — | — | protocol prepared | awaiting §12 |
