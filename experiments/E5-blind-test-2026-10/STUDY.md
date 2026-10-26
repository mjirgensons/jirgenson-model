# E5: a blind test of the Jirgenson Model operating prompt

October 2026. Author of the Model: Martin Jirgenson. Experiment run with Claude (protocol, execution, analysis); decisions by the author.

This page describes one experiment: what was tested, how it was scored, what came out, and what it does not show. Every number below can be traced to a file in this folder. Nothing was left out on purpose; where a result is weak, it is said here.

## Question

When a language model is given the canon of the Jirgenson Model plus the operating prompt, are its answers to small-business crisis messages better than the same model's answers without them, judged blind against a fixed answer key?

## Design

- **Scenarios.** Ten messages written before the first run and frozen (`tasks/dev_tasks_T01-T10.md`): a seasonal bike shop, a food truck with a 72-hour permit clock, a yoga studio with 11 "goals", a translation agency, a dog-grooming salon, a nail salon owner demanding a guaranteed payback, a fifteen-year-old, a print shop that is "profitable" while cash falls, a newsstand in a small town (Latvian), a freelancer whose client does not pay (Russian). Each has an answer key: gold arithmetic, 8 to 10 mandatory elements, 3 to 5 forbidden items, and a word and question budget.
- **Conditions.** A: no system prompt. B: a generic structured-adviser prompt of 158 words (`prompt/control_conditions_A_B_C.md`). C: canon v1.0 attached plus the operating prompt.
- **Generator.** Claude Sonnet 5.5. Three independent answers per scenario and condition.
- **Judge.** Claude Opus 5.5, blind: it sees the scenario, the key and two anonymous answers, never the prompts or condition names (`judge/judge_prompt_v1.md`). Each pair is judged twice with the order swapped.
- **Score (0 to 100).** Mandatory elements (40) + six quality criteria (60) − 2 per violation. The judge also lists every "invented fact": any figure, rule or cause that is not in the scenario and is presented as fact rather than as a labelled assumption.
- **Statistics.** Differences are taken per scenario (n = 10), 95% bootstrap intervals, Wilcoxon and sign tests, win rates with Wilson intervals.
- **Hard checks.** Word counts, question counts, language and internal-label leaks are checked by script, not by the judge (`scripts/e5_hardchecks.py`).

The prompt was revised over three rounds on the same ten scenarios (see "What this does not show"). The version that produced the headline numbers is v1.3-c (`prompt/operating_prompt_v1.3-c_as_tested.md`). The published prompt in the repository root (book edition 1.1) differs from v1.3-c in three places only: the title line, a spacing in "±10 %", and one clause in section K (rhythm of the error vector).

## Results

### Round 0: the first version, before any tuning

| | A (no prompt) | B (generic prompt) | C (canon + prompt v1.0) |
|---|---|---|---|
| Score | 55.3 | 67.7 | 85.9 |

C beat A by +30.6 points (95% interval +26.7 to +34.4) and B by +18.2 (+13.1 to +23.4), in 10 of 10 scenarios each. The generic prompt B closes about 40% of the gap on its own; the rest is the Model's content. This is the least tuned comparison in the study.

### Round 3: the tested version v1.3-c

Scores on 0 to 100, mean over ten scenarios. Source: `data/e5_results_iter_3_snapshot.csv`, `data/summary_iter_3.md`.

| | A | C (v1.3-c) |
|---|---|---|
| Total score | 55.9 | 88.9 |
| Mandatory elements covered | 54% | 97% |
| Answers with at least one invented fact | 75% | 11% |
| Invented facts per answer | 1.72 | 0.11 |
| Answers with at least one violation | 52% | 0% |

- Difference: **+33.0 points** (95% interval +27.8 to +38.4), 10 of 10 scenarios.
- Pairwise preference: C chosen over A in 30 of 30 pairs, in both orders.
- The lowest-scoring C evaluation was 75; the highest-scoring A evaluation was 72.
- Per scenario, A to C: bike shop 67.7 to 91.7; food truck 48.2 to 88.9; yoga studio 61.0 to 88.2; translation agency 32.5 to 83.1; dog grooming 57.1 to 91.7; nail salon 57.8 to 90.1; teenager 65.8 to 90.3; print shop 53.8 to 88.7; newsstand 65.5 to 86.8; freelancer 49.7 to 89.5.

How the percentages are counted: each of the 30 C answers and 30 A answers was judged against the other condition in both orders, and C answers were also judged against v1.1-c. The C column uses all 120 C evaluations. Against A alone (60 evaluations) the C figures are 15% with an invented fact, 0% with a violation, 98% of elements. A's figures come from its 60 evaluations. Mandatory elements are the answer key's items that were clearly present; the unguided answers covered 54% of them.

### The path between round 0 and round 3

| Version | Score | Note |
|---|---|---|
| v1.0 | 85.9 | first version |
| v1.1-c | 86.2 | +2.3 over v1.0, inside the noise band, accepted narrowly |
| v1.2-c | 82.5 | worse than v1.1-c (−2.2), not accepted |
| v1.3-c | 88.9 | +4.4 over v1.1-c (95% interval +2.0 to +7.5), better in 10 of 10 scenarios |

The noise band between two identical blocks of v1.0 answers was ±1.5 points.

## What this does not show

1. **The prompt was tuned on the same ten scenarios it was scored on.** Changes between rounds came from an error analysis of the C answers on these scenarios, and some of them target the failure of a single scenario. The scenario texts were seen while the prompt was revised. The honest reading is: round 0 (+30.6, untuned) is the cleaner number; round 3 (+33.0) includes some fitting.
2. **A sealed hold-out set of ten further scenarios (H01 to H10) exists and has not been measured.** It is not published, so that it stays usable. SHA-256 of the sealed file: `4af01f8e1341001f16437dc86879ae529e39eb215d68c743c186601263c7903b`. If the result is ever measured, the hash lets anyone confirm the file was not changed.
3. **One model family judged and generated.** Sonnet 5.5 wrote, Opus 5.5 scored. A cross-check by Gemini on four pairs agreed on every mandatory element and never disagreed on the preferred answer, but Gemini was more lenient and could not tell close versions apart (`cross_check/`). Four pairs is a spot check, not a validation.
4. **The answer key was written by the Model's author with Claude.** Several mandatory elements reward behaviours the Model prescribes (for example asking for a refusal order, or naming an outside factor). The key is public (`tasks/`); judge for yourself whether it measures what a reader would want.
5. **A is not a clean chat.** The runs happened in an agent environment that adds its own system prompt to all conditions, so "no prompt" here is weaker than a bare chat window.
6. **This compares model answers with model answers.** It does not compare the framework with unaided human managers, and it says nothing about outcomes in real businesses.
7. **A later variant did worse.** A version with the worked examples removed (v1.3-pb) scored 80.2 against 88.9 for v1.3-c on the same scenarios. It is not the published version.
8. **Round 0 judgments of B and the earlier rounds are summarised, not fully included.** The folder contains all raw answers for A, B, v1.3-c and v1.1-c, all 120 judge records for round 3, and the score tables for round 0. Raw judge records for rounds 0 to 2 can be added on request.

## Reproduce or check

1. Read the scenarios and the key: `tasks/dev_tasks_T01-T10.md`.
2. Run your own model with the canon in the repository root and `prompt/operating_prompt_v1.3-c_as_tested.md` as the system prompt, against any scenario. Compare with `responses/`.
3. Score with `judge/judge_prompt_v1.md` and a model of your choice. Expect different absolute numbers; check whether the direction and the size of the gap hold.
4. Re-run the statistics: `scripts/e5_analyze.py` on `data/e5_results_iter_3_snapshot.csv`.
5. Trace any number to its source: row in `data/e5_results_iter_3_snapshot.csv` (pair id, order) → `judgments/<pair id>_<order>.md` → answers in `responses/`.

Working notes in Latvian (protocol, run log, decisions) are in `working_notes_lv/`, unedited.
