# PromptBase listing texts, v1 (2026-10-21)

Paste field by field. Limits checked on the seller form: Name 40 chars, Description 500 chars, template 8,192 tokens, 4 example outputs, Prompt instructions = rich text seen after purchase.

## Item type / model
Prompt · Text · Claude (Sonnet 5.5). Second listing for ChatGPT only after a test with ChatGPT.

## Name (32/40)
```
Jirgenson Model Business Analyst
```

## Description (≤500 chars; count before pasting)
```
Not a template, a management method. Attach the free Canon file, describe your business, freelance work or family budget, and the model works by instruments: where you stand, the most dangerous event with its date, what to do this week, what to protect, two honest forecasts. Blind test, 10 real cases: 88.9/100 with the method vs 55.9 without; judge preferred it 30/30; invented facts 75%→11%. "Gives mechanics, not advice." Not financial or legal advice.
```
(≈ 470 characters)

## Prompt template
File `jirgenson_prompt_v1.1_promptbase_en.txt` (header with one variable + Operating Prompt v1.1 unchanged). ≈ 6,700 tokens by estimate; the form shows the exact count.

## Example outputs (4, real outputs of this template with the Canon attached)
`examples/T01_output.md` bike shop, QUICK, EN · `examples/T02_output.md` food truck, EMERGENCY, EN · `examples/T03_output.md` yoga studio, PLAN CHECK, EN · `examples/T10_output.md` freelancer, EMERGENCY, RU.
Inputs for each: `examples/T0x_input_filled_template.txt`.

## Test prompt (for the review team)
`examples/T01_input_filled_template.txt`. Note in the instructions field for reviewers: "Attach the Canon file (link in the template header) to the chat before running; the prompt does not answer without it."

## Prompt instructions (rich text after purchase; links allowed)
```
HOW TO USE

1. Download the Jirgenson Model Canon v1.0 (free):
   https://raw.githubusercontent.com/mjirgensons/jirgenson-canon/main/jirgenson_canon_v1.0_en.md
   The Canon is the theory; this prompt is the instruction for applying it. The prompt checks that the Canon is present and will not answer without it.
2. Open a new chat. Attach the Canon file. Paste this prompt with your situation written into the first line. For repeated use, put both into a project or system instructions.
3. Describe what is going on and what you want to decide. The model asks for what it needs, at most a few questions at a time. Say "emergency" if you need one action for today; say "no more data" and it stops asking and labels its assumptions. It answers in the language you write in.

WHAT YOU GET
Where you really stand, in your own numbers. The most dangerous event and its date. What to do today / this week / this month. What to protect first and what not to do now. What to measure and when to review. Two forecasts: if nothing changes, if the plan works. It proposes, you decide; it never invents data.

MEASURED, NOT PROMISED (experiment of 18 October 2026)
The same model (Claude Sonnet 5.5) answered 10 realistic cases (a seasonal bike shop, a food truck with a 72-hour permit deadline, a yoga studio with 11 "goals", a freelancer whose client does not pay; English, Latvian, Russian) three times with the Canon + this prompt and three times without. A stronger model (Claude Opus 5.5) judged every pair blind, twice, in both orders, against a pre-registered answer key.
- Score: 88.9 / 100 with the method vs 55.9 without (+33, 95% CI +27.8 to +38.4)
- The judge preferred the method's answer in 30 of 30 pairs
- Answers containing an invented fact: 75% → 11%
- Rule violations (too long, too many questions, wrong language): 52% → 0%
- Worst answer with the method (75) beat the best answer without it (72)
Limits: the judge was a language model, 10 cases, one model family. The prompt was refined on these same cases, so a fresh set may score somewhat lower.

WHAT READERS SAY ABOUT THE METHOD (reviews of the book Steer, Don't Guess)
"Most management books give advice. This one gives mechanics."
"From constant firefighting to steering by instruments."
"The author does not present the model as a miracle cure: forecasts can be wrong, data can be incomplete."

THE BOOK
The full method, with examples and the reasoning behind it: Steer, Don't Guess (250 pages), https://jirgenstorm4.gumroad.com/l/steer-dont-guess

NOT ADVICE
Not financial, legal or investment advice. The model never decides for you.
```

## Price
$9.99 (category median). Review after the first sales.

## Tags
business, finance, planning, decision, analysis, strategy, freelance, budget
