# E5 — Control conditions v1

Three generating conditions are used. Only C changes between iterations.

## Condition A — no prompt (the book's baseline)

No system prompt and no attachment. The task's user message is sent as the first (and, for two-turn tasks, second) message of a fresh conversation. This is the comparison the book (Appendix J) and experiment E1 made.

Note for in-harness runs (subagents inside this workspace): the "no prompt" condition still carries the harness's own system prompt. Record this as `A-harness` and treat it as a weaker baseline than a clean API/chat run (`A-clean`). Final confirmation uses `A-clean`.

## Condition B — generic structured adviser (control for "any good prompt")

Purpose: separates the effect of the Jirgenson content (canon + rules) from the effect of merely having a sensible structure and a sensible tone. If C beats A but not B, the gain is the structure, not the model. Run at iteration 0, at the final iteration, and on the hold-out set.

System prompt (verbatim, 158 words, FROZEN):

```
You are an experienced adviser to small-business owners, freelancers, families and young people. The person has little time and wants to see their situation clearly and decide what to do.
Reply in the person's language, in plain words, within the time or length they imply. Start with what their own numbers show, then the biggest risk, then what to do today, this week and this month, then what to watch and when to check again. Give two forecasts with numbers: if nothing changes, and if the plan works. Make no guarantees; give ranges and state your assumptions. Do not invent facts; if a number is missing and matters, say what you assumed and ask only what would change the decision. If the person says they want no questions, ask none. If they ask for one action, give one action first. If they ask you to check a plan, do not rewrite it. Leave decisions about priorities to the person.
```

Why this wording: it contains the same *surface* features as the operating prompt (numbers first, danger, actions by horizon, measurement, two forecasts, no guarantees, no invented facts, mode courtesies) without the canon's concepts (refusal order, zones and thresholds, levers vs conditions, environmental factors, offsets, launch conditions, red protocol). Anything C gains over B is attributable to the model's content and rules, not to the structure.

## Condition C — CANON v1.0 + OPERATING PROMPT vN

- CANON: `02a_CANON_v1.0_EN.md` — **fixed for the whole experiment** (the experiment optimises the prompt only; a canon change would start a new experiment, E6).
- OPERATING PROMPT: version vN under test (v1.0 at iteration 0; v1.1-c … v1.5-c candidates after that). The exact text of every version is stored under `claude/e5/prompts/` with its SHA-256 and token count.
- Delivery: canon attached or pasted first, then the operating prompt as the system prompt (API) or as the first message (chat UI), then the task's user message. Record which delivery method was used; do not mix methods within one iteration.

## What is held constant across all conditions

- Task text (verbatim), order of turns, date references.
- Generating model and version string; temperature/sampling settings (default of the interface; recorded).
- Fresh conversation per (task, condition, run): no memory, no project knowledge other than the canon in condition C.
- Same day or consecutive days for all conditions of one iteration (concurrent control).
