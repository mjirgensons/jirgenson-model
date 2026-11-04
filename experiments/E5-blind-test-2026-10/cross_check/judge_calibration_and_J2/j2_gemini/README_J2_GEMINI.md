# J2 = Gemini: second-judge agreement check (iteration 0 pairs)

**Why.** Our judge J1 (Claude Opus 5.5) is a model of the same family as the generator (Sonnet 5.5). To rule out an "own kind" bias, the same pairs must be judged by a judge from another family — Gemini — with **exactly the same judge prompt and the same packs**, changing nothing. After that I compare Gemini's and Opus's verdicts pair by pair (preference, elements, criteria) and write down the agreement in the report (30 §10, §8).

**Sample (fixed before judging, `J2_selection.csv`).** 10 pairs — one from each task T01–T10: odd tasks — canon+prompt v1.0 vs A (no prompt); even tasks — canon+prompt v1.0 vs B (generic adviser prompt). The replicate number is determined by the formula ((n−1)÷2 mod 3)+1, so as not to pick "convenient" pairs. Each pair in two orders (12 and 21) = 20 packs.

## Files
| File | What it is |
|---|---|
| `J2_GEMINI_A_order_12_10_packs.md` | **Mandatory part.** 10 packs (order 12), each complete: judge prompt + task + key + 2 anonymous responses + output format. ~2,300–3,100 words each. |
| `J2_GEMINI_B_order_21_10_packs.md` | **Recommended part.** The same 10 pairs in reversed order (response 1 ↔ 2). Needed to check position bias and to apply the "both orders agree" rule to Gemini as well. |
| `packs/*.md` | The same 20 packs, one per file (if it is more convenient to paste from a separate file). |
| `29c_E5_JUDGE_PROMPT_v1.md` | The judge prompt as it is in protocol 29c (the same text as at the start of each pack). Pasting it separately is **not needed** — it is already in the pack. |
| `J2_selection.csv` | The sample list with a SHA-256 for each pack (reproducibility). |
| `summary_iter_0_J1_results_DO_NOT_SHOW_GEMINI.md` | Our J1 results — **for you only**. Gemini must not see them, otherwise it is not a blind judgment. |

## Procedure (for each pack)
1. **New Gemini conversation** (no memory, no previous packs, no files about the Jirgenson model). If Gemini has "personalization"/memory — turn it off.
2. Paste **the whole block** between `========== PACK k/10 ==========` and `========== END OF PACK ==========` (the lines themselves may be left out). Add nothing, explain nothing, do not lead.
3. Gemini's response must contain 6 steps in prose and a ```json block at the end. If there is no JSON block or it is incomplete — reply once "Please output the JSON block exactly in the required format." and take that.
4. **Save the WHOLE Gemini response** (not only the JSON) in a file with the pack's name, e.g. `T01_C-v1.0-r1_vs_A-r1_12.md`, in the folder `[local archive]\iter_0\judgments_J2_gemini\` (or send it to me here). Write down the Gemini model version (e.g. "Gemini 2.5 Pro", date) — once is enough.
5. If Gemini refuses or cuts off the response — write it down, repeat once in a new conversation; keep the original.

Minimum: part A (10 packs). Full set: A + B (20). Time: ~3–5 min per pack.

## What I will do afterwards
I will parse Gemini's JSON the same way as J1 (`e5_collect.py`) and compare pair by pair: preference agreement (expected ≥ 8/10), element match, criteria difference, total score correlation; I will write it down in 30 §8 and §10. If Gemini systematically disagrees with Opus — that is a finding, not an error, and it goes into the report.
