# E5: a blind test and stepwise optimisation of the Jirgenson Model operating prompt

October–November 2026. Author of the Model and of this record: Martin Jirgenson. The experiment was run with Claude (protocol, execution, analysis); every decision on versions, interpretation and publication was taken by the author.

Permanent record: [doi.org/10.5281/zenodo.23964934](https://doi.org/10.5281/zenodo.23964934) (Zenodo). This page describes one experiment: what was tested, how it was scored, what came out in each round, and what it does not show. Every number below can be traced to a file in this record. All rounds of the optimisation are included; where a result is weak, it is said here.

## 1. Question

When a language model is given the canon of the Jirgenson Model plus its operating prompt, are its answers to small-business crisis messages better than the same model's answers without them, judged blind against a fixed answer key? And can the operating prompt be improved in controlled, pre-registered rounds while the canon stays fixed?

## 2. Design

- **Scenarios.** Ten messages written before the first run and frozen (`tasks/dev_tasks_T01-T10.md`, machine-readable `tasks/tasks_T01-T10.json`): a seasonal bike shop, a food truck with a 72-hour permit clock, a yoga studio with 11 "goals", a translation agency, a dog-grooming salon, a nail-salon owner demanding a guaranteed payback, a fifteen-year-old, a print shop that is "profitable" while cash falls, a newsstand in a small town, a freelancer whose client does not pay. Eight scenarios were posed in English; the newsstand scenario (T09) was posed in Latvian and the freelancer scenario (T10) in Russian, to test whether the answer keeps the user's language. In this record both scenarios and all answers to them are given in English translation (§10). Each has an answer key: gold arithmetic, 8 to 10 mandatory elements, 3 to 5 forbidden items, and a word and question budget.
- **Conditions.** A: no system prompt. B: a generic structured-adviser prompt of 158 words. C: canon v1.0 attached plus an operating-prompt version (`prompt/control_conditions_A_B_C.md`).
- **Generator.** Claude Sonnet 5.5, the same in every round. Three independent answers per scenario and condition, each in a fresh conversation. In round 0, C was generated in two independent blocks of three to measure noise.
- **Judge.** Claude Opus 5.5, blind: it sees the scenario, the key and two anonymous answers, never the prompts or condition names (`judge/judge_prompt_v1.md`, frozen). Each pair is judged twice with the order swapped. Each record contains six reasoning steps in prose and a JSON score block.
- **Score (0 to 100).** 40 × share of mandatory elements + six criteria scored 1 to 10 (C1 accuracy, C2 diagnosis, C3 practicality, C4 fit, C5 control, C6 honesty) − 2 per violation. The judge also lists every "invented fact": any figure, date, rule or cause that is not in the scenario and is presented as fact rather than as a labelled assumption.
- **Hard checks.** Word counts, question counts, language and internal-label leaks are checked by script, not by the judge (`scripts/e5_hardchecks.py`).
- **Statistics.** Differences are taken per scenario (n = 10), with 95 % bootstrap intervals (10 000 resamples, seed 0), Wilcoxon signed-rank and sign tests; a pairwise win counts only when the same answer is preferred in both orders (Wilson intervals).
- **Noise band.** Two identical blocks of v1.0 answers in round 0 differed by SE 0.75, so the band is **±1.51 points**.
- **Acceptance rule** (pre-registered, `working_notes/29_E5_protocol.md` §5.4): a new version is accepted if its gain over the base is above 1.51 with the lower 95 % bound above −1, no criterion drops by more than 1.0, violations do not rise, and the prompt is at most 15 % longer than v1.0.
- **Pairing in each round.** The version under test is judged against A (30 pairs) and against the current base version (30 pairs), both orders: 120 judge records per round.

## 3. Rounds and versions

| Round | Version tested | What changed | Score | Test vs base [95 % CI] | Verdict |
|---|---|---|---|---|---|
| 0 | v1.0 | first version, before any tuning | 85.9 | vs A +30.6 [+26.7; +34.4]; vs B +18.2 [+13.1; +23.4] | baseline |
| 1 | v1.1-c | format budgets, discipline of the four response modes | 86.2 | vs v1.0 +2.34 [−0.18; +4.58] | accepted (narrowly) |
| 2 | v1.2-c | strict ban on hypotheses | 82.5 | vs v1.1-c −2.18 [−5.88; +0.77] | rejected: content was cut, violations rose |
| 3 | v1.3-c | hypotheses allowed when labelled, a closing PLAN CHECK step, lower word budgets | 88.9 | vs v1.1-c +4.38 [+1.97; +7.47], 10/10 scenarios | accepted |
| 5 | v1.5-c | 41 replacements on three axes: evidence discipline, forecast depth, usefulness of actions | 88.8 | vs v1.3-c +1.71 [+0.23; +3.36]; same-call +0.86 [−0.66; +2.43] | passes the rule formally; total-score gain not robust (§6) |

Each version is in `prompt/`. The change list that defines v1.5-c is in `working_notes/round5/changes_v1.5.md` (exact replacements in `.json`, text diff in `.diff`). Round number 4 belongs to a separate test that is not part of this record; the error analysis for round 5 also read the v1.3-c judge records of that run.

The prompt published with the book (edition 1.1, Appendix I) corresponds to v1.3-c; it differs from it in three places only: the title line, a spacing in "±10 %", and one clause in section K. v1.5-c is newer than the book edition.

## 4. Results

### 4.1 Round 0: the first version, before any tuning

| | A (no prompt) | B (generic prompt) | C (canon + prompt v1.0) |
|---|---|---|---|
| Score | 55.3 | 67.7 | 85.9 |
| Mandatory elements covered | 54 % | 66 % | 93 % |
| Answers with at least one invented fact | 68 % | 45 % | 55 % |
| Answers with at least one violation | 55 % | 40 % | 14 % |

C beat A by **+30.6 points** (95 % interval +26.7 to +34.4) and B by +18.2 (+13.1 to +23.4), in 10 of 10 scenarios each. C was preferred over A in 30 of 30 pairs and over B in 29 of 30. The generic prompt B closes about 40 % of the gap on its own; the rest is the Model's content. This is the least tuned comparison in the study.

### 4.2 Round 3: v1.3-c (the version behind the book's prompt)

| | A | C (v1.3-c) |
|---|---|---|
| Total score | 55.9 | 88.9 |
| Mandatory elements covered | 54 % | 97 % |
| Answers with at least one invented fact | 75 % | 11 % |
| Invented facts per answer | 1.72 | 0.11 |
| Answers with at least one violation | 52 % | 0 % |

Difference **+33.0 points** (+27.8 to +38.4), 10 of 10 scenarios; C preferred in 30 of 30 pairs. The lowest C evaluation was 75; the highest A evaluation was 72.

### 4.3 Round 5: v1.5-c (final version)

| | A | C (v1.3-c, re-judged) | C (v1.5-c) |
|---|---|---|---|
| Total score | 56.2 | 87.0 | 88.8 |
| Mandatory elements covered | 55 % | 95 % | 97 % |
| Answers with at least one invented fact | 70 % | 20 % | 0.8 % (1 of 120) |
| Invented facts per answer | 1.70 | 0.22 | 0.008 |
| Answers with at least one violation | 53 % | 2 % | 0 % |
| Words per answer | 501 | 461 | 454 |

- Difference to A: **+32.5 points** (+26.6 to +38.5), 10 of 10 scenarios, C preferred in 30 of 30 pairs. The lowest v1.5-c evaluation was 80; the highest A evaluation was 76.
- Against v1.3-c in the same judge calls: 14 wins, 13 losses, 3 ties.
- Against the earlier rounds (across rounds, not in shared calls): +21.1 over B (+15.2 to +27.5) and +2.9 over v1.0 (0.0 to +6.4).
- Hard checks: 33 of 33 turns within word budget, question budget, language and without internal labels.

How the percentages are counted: each of the 30 v1.5-c answers was judged against A and against v1.3-c in both orders, so the v1.5-c column uses 120 evaluations; against A alone (60 evaluations) the share with an invented fact is 1.7 % and with a violation 0 %. A and the re-judged v1.3-c have 60 evaluations each.

Per scenario, A → v1.5-c: bike shop 67.7 → 91.0; food truck 46.8 → 89.2; yoga studio 59.5 → 86.9; translation agency 34.3 → 85.2; dog grooming 58.8 → 90.0; nail salon 55.7 → 90.6; teenager 67.7 → 89.8; print shop 54.0 → 90.3; newsstand 67.2 → 84.8; freelancer 50.8 → 89.7.

What round 5 changed is precision, not the total score: invented facts per answer fell from 0.22 to 0.008, violations from 0.02 to 0, and three targeted elements improved (newsstand "closing is a real option" and food-truck "lowest cash point": now missing in 0 of 12 evaluations; translation agency "does AI affect the whole market": missing 18/18 → 6/12).

### 4.4 Stability of the judge

The same answers were judged again in the following round: v1.0 scored 85.9 in round 0 and 83.9 in round 1, v1.1-c 86.2, 84.7 and 84.5 in rounds 1 to 3, and v1.3-c 88.9 in round 3 and 87.0 in round 5. The no-prompt answers A ranged from 55.3 to 56.5 over the five rounds. Full tables: `data/summary_rounds_0-5.md`.

## 5. What is still not right in v1.5-c

- **Newsstand (T09), element 3** (the shrinking town named as the strongest force, which marketing alone will not reverse) is missing in 11 of 12 evaluations: the new evidence rule turns even a conclusion drawn from the user's own numbers into a question. T09 is the only scenario where v1.5-c scores below v1.0 (84.8 against 87.3).
- **Dog grooming (T05)** loses all 3 direct pairs against v1.3-c: the danger is framed as "one weak month", which the answer's own numbers contradict.
- **Translation agency (T04), element 7** (whether AI affects the whole market) is still missing in 6 of 12 evaluations.
- **The only invented fact** in 120 evaluations is a sentence taken from one of the prompt's own examples.
- A draft change pack for a next version (`working_notes/round5/changes_v1.6.md`) addresses these. It has not been generated or tested.

## 6. A methodological finding: judging context

In every round the judge scored a C answer **+1.1 to +2.7 points higher when it was paired with a weak no-prompt answer** than when the same answer was paired with another C version (`data/round5/iter5_context_check.txt`). The version under test is judged against both A and the base, while the re-judged base is judged only against the version under test, so the pre-registered primary difference carries about half of this effect in favour of the new version (about +0.9 in round 5).

This does not change the verdicts of rounds 1 to 3 (in round 3 the same-call difference is +3.45, still above the band). In round 5 it is the difference between "above the noise band" (+1.71, primary) and "inside the noise band" (+0.86, same-call only). Both figures are reported. A future design should compare versions only within shared judge calls and use six answers per scenario (band about ±1.1).

## 7. What this shows

With these ten scenarios, generator Claude Sonnet 5.5, judge Claude Opus 5.5 and this rubric, the canon plus the operating prompt scores about 31 to 33 points above the same model without a prompt with every accepted version (10 of 10 scenarios, 30 of 30 pairs each time; the rejected v1.2-c: +26.0) and about 18 to 21 points above a good generic adviser prompt. Judge-flagged invented facts fall from about 1.7 per answer without a prompt to 0.008 with v1.5-c, and violations to zero.

## 8. What this does not show

1. **The prompt was tuned on the same ten scenarios it was scored on.** Changes between rounds came from an error analysis of the C answers on these scenarios, and some target the failure of a single scenario. Round 0 (+30.6, untuned) is the cleanest number; rounds 3 and 5 include fitting.
2. **A sealed hold-out set of ten further scenarios (H01 to H10) exists and has not been measured.** It is not published, so that it stays usable. SHA-256 of the sealed file, recorded on 2026-10-16 before any data: `4af01f8e1341001f16437dc86879ae529e39eb215d68c743c186601263c7903b`. If it is ever measured, the hash lets anyone confirm the file was not changed.
3. **One model family judged and generated.** A cross-check by Gemini on four pairs agreed on every mandatory element and never preferred the opposite answer, but Gemini was more lenient and could not tell close versions apart (`cross_check/`). Four pairs is a spot check, not a validation. No human raters were used.
4. **The answer key was written by the Model's author with Claude.** Several mandatory elements reward behaviours the Model prescribes (for example asking for a refusal order, or naming an outside factor). The key is public; judge for yourself whether it measures what a reader would want.
5. **A is not a clean chat.** The runs happened in an agent environment that adds its own system prompt to all conditions, so "no prompt" here is weaker than a bare chat window.
6. **This compares model answers with model answers.** It does not compare the framework with unaided human managers and says nothing about outcomes in real businesses.
7. **Nine round-0 judge texts were lost** in a working-session reset before archiving. Their scores survive in the frozen table, and all nine pairs were judged again (`judgments/round0_rejudge/`). This is logged in `working_notes/30_E5_scientific_report.md` §10.
8. **Interruptions.** API rate limits and a safety classifier stopped some judge calls. The rule, fixed in round 1, was to use a record only if its file was fully written and parses, otherwise to re-run it with a fresh agent and the identical input. Every case is in the run log.

## 9. Reproduce or check

1. Read the scenarios and the key: `tasks/dev_tasks_T01-T10.md`.
2. Run your own model with `prompt/canon_v1.0.md` and an operating prompt from `prompt/` as the system message (canon first, prompt after it), against any scenario. The exact inputs given to the generator are in `inputs/roundN/generation/`. Compare with `responses/`.
3. Score with `judge/judge_prompt_v1.md` and a model of your choice; the exact judge inputs are in `inputs/roundN/judge/`. Expect different absolute numbers; check whether the direction and the size of the gap hold.
4. Re-run the statistics (Python 3 with pandas, numpy, scipy, matplotlib):
   ```
   python3 scripts/e5_analyze.py run --results data/e5_results_rounds_0-5.csv --pairwise data/e5_pairwise_rounds_0-5.csv --out out
   python3 scripts/e5_accept_check.py --iter 5 --test v1.5-c --base v1.3-c --ctrl A --results data/e5_results_rounds_0-5.csv --pairwise data/e5_pairwise_rounds_0-5.csv --length-pct 14.9
   ```
5. Trace any number to its source: a row in `data/roundN/e5_results_iter_N_snapshot.csv` (pair id, order) → `judgments/roundN/<pair id>_<order>.md` → the judge input in `inputs/roundN/judge/` → the answers in `responses/`.

## 10. Use of AI

The experiment was designed, run and analysed with Anthropic's Claude models acting under the author's instructions (orchestration Claude Fable 5.1 and Claude Opus 5.5; generation Claude Sonnet 5.5; judging Claude Opus 5.5). The answers and judge records in this record are model outputs and are published unedited, with one exception: the record is entirely in English. Scenario T09 was posed in Latvian and T10 in Russian, so the inputs and the model's answers for these two scenarios were in those languages, and the judge records quote them. For this record the T09 and T10 scenario texts, the 48 answers to them, the quotations from them in the judge records, and the corresponding generator and judge inputs were translated into English by Claude, sentence by sentence; each translated answer starts with a line saying so. Scores were given on the original-language answers and are unchanged. The SHA-256 values in `responses/INDEX_roundN.csv` and `judgments/roundN/INDEX.csv` refer to the original files; `MANIFEST_sha256.csv` lists the files as published. The working notes (protocol, scientific report, run log, final results, per-round decisions, comparisons, error analyses and change packs) were written in Latvian during the experiment and are published in English translation; every number in each translation was checked by script against the original. Passages of the notes about the separate round-4 test were removed, and in the run log the name of the author's computer was replaced with "[computer name removed]". Paths mentioned inside the notes refer to the original working folders: `iter_N/` corresponds to `roundN/` here.

## 11. Related

Martin Jirgenson, *Steer, Don't Guess. Setting Priorities, Reading the Numbers and Correcting Course in Business and Life. The Jirgenson Model* (2026), ISBN 979-8-1648-3374-9. Canon and published prompt: https://github.com/mjirgensons/jirgenson-model. Site: https://mjirgensons.github.io/.

This is not financial, legal or investment advice.
