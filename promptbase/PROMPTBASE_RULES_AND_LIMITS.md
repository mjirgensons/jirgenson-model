# PromptBase: rules and limits that matter for us (condensed, checked 2026-10-21)

Source: promptbase.com/prompt-guidelines, /knowledge-base/payouts, /knowledge-base/prompt-purchases, the seller form (/sell, logged in). Only what affects our listings.

## Seller form (text prompt, Claude)
| Field | Limit / options |
|---|---|
| Item type | Prompt or Agent Skill (SKILL.md) |
| Generation type | Text |
| Model | Claude (versions: Sonnet 5.5, Opus 5.5, Haiku 5.5, Fable 5.1), also ChatGPT, Gemini, DeepSeek, Grok as separate listings |
| Name | **40 characters** |
| Description | **500 characters** (shown on the store page) |
| Price | Free or $2.99 … **$19.99** (steps of $1) for a prompt; "Auto Pricer" available |
| Prompt template | **8,192 tokens**; variables in `[square brackets]` are mandatory |
| Max tokens / temperature | sliders (we set 16384 / 0) |
| Example outputs | **4** pasted outputs; must be real outputs of the template; varied inputs |
| Prompt instructions | rich text (headings, lists, images, YouTube), seen by the buyer after purchase; **no stated length limit**; links allowed here |
| Test prompt | one filled-in version of the template; the review team runs it and compares with the examples |
| Step 3 | Enable payouts (Stripe or Zoneless) |

## What gets declined (relevant ones)
- No `[variables]` or a prompt that produces one fixed output.
- "Too specific" (more than 3 ideas) or "too simple / guessable".
- Test generations do not match the examples (prompt unstable or examples edited).
- Examples too similar to each other.
- Non-English prompt; spelling errors; "AI generated" mass-produced prompts (human-written ones can be disputed).
- Unsafe: chatbots giving medical advice; keep the "not financial/legal advice" line.
- Plagiarism; a prompt that already exists on PromptBase (AI similarity check on the prompt file).
- Thumbnail with prices, ratings or lots of text.

## What the buyer gets (platform promise)
Template; 4+ examples; the creator's guide (our Prompt instructions); commercial licence; chat support with the creator; 100% money-back if the prompt does not work as advertised; free future updates.

## Money
20% marketplace fee; 0% via the seller's own link. Balance: 72 h pending. Stripe payout: account ≥30 days old and ≥$30 (weekly or monthly); early payout $3.99. Zoneless (USDC): daily, no minimum. Price changes have a cooldown; two listings per day for new sellers (third-party report, not confirmed on site).

## Our consequences
- Canon (~5,900 tokens) + prompt v1.1 (~6,900) = ~12,800 tokens > 8,192, so the template cannot hold both.
- The template must open with the `[variables]` block and must work in the reviewer's test on its own.
- The full two-file product, the book and the experiment write-up go into **Prompt instructions** (links allowed) and into the 500-character description.
