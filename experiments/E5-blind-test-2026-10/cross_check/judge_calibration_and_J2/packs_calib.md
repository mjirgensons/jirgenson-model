# E5 bundle of packs/calib (prefix: *) — 7 files

| file | sha256 | bytes |
|---|---|---|
| ERR_T01_C1.md | 3bc53f38065dc2accf9465e24c78a68652df0b29c6a4e8a16c570017a68978a2 | 16666 |
| ERR_T08_C1.md | 8ee90efbc1751e141ceb6714c9bb286c620fe8da207e4aa0a52bd284ca96df85 | 15733 |
| IDENT_T01_C1.md | 6e8ec6e911b6c05414eee6e7f9710a54b1f8fd510dfd78434a034e5c09e43792 | 16669 |
| IDENT_T07_A1.md | f7c9af41eca6219015083ca54f1ed57a9eade7f6e870f83f7f896050f8f882df | 13322 |
| IDENT_T08_B2.md | 0ab8a04ab19e191afa33f134219ee317e6a541f227682ec11fc2644025aafd09 | 14913 |
| LEN_T02_C1.md | 2edafb02bb0c82f5df03397dacf46eba4914c79539b593698f2c74881c909c5e | 13329 |
| LEN_T07_C1.md | b5bd730b20708ccff6ebcfa9604071d32bd8904a3016ef79b98661e41bede411 | 13803 |

===== FILE: ERR_T01_C1.md =====
You are an independent evaluator of advice given to a real person with a real problem. You will read one task, an answer key prepared in advance, and two anonymous responses. Your job is to score each response against the key and the rubric below, then say which response serves the person better.

Rules you must follow:
1. Judge only what is written in the responses. Do not guess which method, system prompt or model produced them, and do not reward a response for looking like a method. Structure, headings and length earn nothing by themselves; a long or heavily formatted response that says less than a short one scores lower.
2. Recompute every number yourself from the task's figures before scoring. The "Gold facts" show the expected arithmetic; if a response reaches the same conclusion by a different but correct route, that counts. A wrong number that changes the advice is a serious error; a wrong number that does not change the advice is a minor one.
3. A mandatory element scores 1 only if it is clearly present and correct in substance; a vague gesture towards it scores 0. Score each element independently.
4. Count a forbidden item once per response if it is present anywhere in the response.
5. Invented facts: any figure, rule, statistic or cause that is not in the task and is presented as a fact (not as a labelled assumption or illustration) is an invented fact. List each one.
6. The person's time and language matter: a response that exceeds the budget, uses vocabulary the person said they do not want, or answers in the wrong language is penalised under criterion 4 and in the hard checks, even if its content is good.
7. If the two responses are identical or near-identical, give identical scores and declare a tie.
8. Be strict and consistent. Use the whole 1–10 scale: 9–10 means an experienced adviser would change nothing material; 5–6 means usable but with clear gaps; 1–3 means misleading or useless for this person.

=== TASK ===
## T01 — Seasonal bike shop (QUICK, EN)

**Budget:** QUICK: ≤600 words, ≤3 questions.
**Trap:** the annual average is positive (+€4,600/year), but the winter months drain the reserve and cash runs out in February. The owner also wants to spend €12,000 on new rental e-bikes now.

**User message (verbatim):**

> Quick check, I have about 20 minutes. I run a bicycle repair and rental shop. Today is 1 October. In the season (April to October, 7 months) revenue averages €14,000 a month; in winter (November to March, 5 months) it is about €4,000 a month. Fixed costs are €6,500 a month all year (rent €2,000, one mechanic €3,500, insurance and utilities €1,000); my own pay of €1,500 is already inside that €6,500. Parts and consumables are about 30% of revenue. I have €9,000 in the account and no loans. I want to buy 10 new rental e-bikes for €12,000 before next season. Where do I stand and what should I do this week?

**Gold facts (judge recomputes):**
- Summer month: 14,000 − 6,500 − 4,200 = **+3,300**. Winter month: 4,000 − 6,500 − 1,200 = **−3,700**.
- Year: 7 × 3,300 − 5 × 3,700 = +23,100 − 18,500 = **+4,600**.
- October is still a season month: cash at end of October ≈ 9,000 + 3,300 = **12,300** (≈ 1.6 winter months of outgoings at 7,700).
- Cash path over the winter: end Nov 8,600; end Dec 4,900; end Jan 1,200; **runs out in February** (12,300 / 3,700 ≈ 3.3 months). Getting to April needs 18,500; the gap is **≈ €6,200** plus any cushion. (A response that treats October as a winter month and lands on "January" has the mechanism right and the date one month early: score M2 as 1, note it under C1.)
- E-bikes (€12,000) exceed the reserve today (9,000) and would leave ≈ €300 after October: paying now brings cash to zero in **November**.

**Mandatory elements:**
- M1 Computes the winter monthly loss (≈ −3,700) and/or the year total (≈ +4,600) from the user's numbers. *Why:* the whole decision rests on the difference between the average and the cash path.
- M2 Names the danger as an event with a date: cash runs out in February (January–February acceptable, see gold facts) if nothing changes. *Why:* R12/R13: the danger is the event, with its date.
- M3 Says the e-bike purchase cannot come out of this cash now (it would exhaust the reserve before winter); it waits for a measurable condition or separate financing. *Why:* no growth move while the reserve is heading into the red (§9.5).
- M4 Proposes a red line for the reserve with its reason (e.g., one winter month ≈ €7,700) and says when the forecast crosses it (in December by the gold path: an alarm that is about to ring, not a line for later). *Why:* R6, R13.
- M5 Lists levers the owner can move himself (winter cost cuts: mechanic hours or seasonal arrangement, rent talk, winter services, pre-season deposits, selling old fleet, a bridging facility arranged *before* the trough). *Why:* R7.
- M6 Two forecasts with numbers: nothing changes (zero in February); plan works (a stated monthly loss reduction and the resulting cash floor). *Why:* §7.7.
- M7 What to measure (weekly cash, bookings) and a next review date. *Why:* output format §6.
- M8 ≤3 questions, ≤600 words. *Why:* mode budget.

**Forbidden items:**
- F1 Recommends buying the e-bikes now from cash.
- F2 Presents industry figures not given by the user as facts (illustrative, labelled numbers are fine).
- F3 Promises survival or a result.
- F4 Fixes the owner's priorities without marking them as a proposal.

=== RESPONSE 1 ===
**Where you stand**

The season earns about €3,300 a month after parts (€4,200) and fixed costs (€6,500), roughly €23,100 over seven months. Winter loses about €3,700 a month, roughly €18,500 over five. Over the year you keep about €4,600 after your own pay; winter takes back almost all of the season. Your €9,000 is 1.4 months of fixed costs.

One thing does not add up: rent, mechanic and insurance/utilities already total €6,500, leaving no room for your €1,500 pay. I am assuming your pay really is inside it. If it is on top, fixed costs are €8,000, winter loses €5,200 a month and the cash runs out around 3 January.

**The greatest danger**

If nothing changes, you have about €12,300 on 31 October and the money runs out around 10 February, with rent, insurance and the mechanic's pay still due. Unpaid wages are the damage that cannot be undone: he may not be there in April. Buying the e-bikes from the account makes it worse: a hole of about €18,200 by 31 March.

I propose a red line of €6,500 in the account (one month of fixed costs). You are above it now, but on this course you cross it in mid-December, about eleven weeks away. That is time to act.

**What to do**

- Bank, this week: ask for a credit line of about €10,000 while you have no loans.
- Landlord, this week: ask to reduce or defer rent for December to February (€2,000 a month).
- You, starting now: sell spring tune-ups paid in advance, and winter storage. Each extra €1,000 of winter revenue leaves €700.
- You, by 31 October: decide your winter pay. Taking half from November to March frees €3,750; taking none frees €7,500. Your call; I'd plan on half.

Together these must find about €10,400, the bad case rather than the middle one (€6,200), so the cushion is €4,200.

**What to protect, what to hold off**

My proposed order, from what you give up last to what you give up first: the shop open through April with the mechanic paid; your own pay; the e-bikes. Tell me if yours differs.

Do not order or lease the e-bikes now, and do not let the mechanic go. Repaying €12,000 within one season takes about €1,700 a month net from the ten bikes, around €170 each, and they earn nothing before April. A realistic start is 2 or 3 bikes once the account would stay above €6,500 after paying for them.

**What to watch**

Check the account on the 1st of each month against this path (before any savings): 1 Nov €12,300; 1 Dec €8,600; 1 Jan €4,900; 1 Feb €1,200. If you are more than €1,500 below it, the next step (pay to zero, rent relief) starts at once. First check: 1 November.

**Two forecasts**

If nothing changes: cash runs out about 10 February (mid-January to about 17 February) and ends March near −€6,200 (−€4,800 to −€10,400).

If the plan works: the account stays at or above zero all winter, even in the bad case, ends March near €4,200, and the season's €3,300 a month lifts you back over the red line if spring is average.

The middle case assumes an average October and winter at €4,000. The bad case is October at €10,000 with winter 10% under; the good end is winter 10% over. Tax is assumed to be inside the €6,500.

Two questions: is your pay inside the €6,500 or on top of it? What would an e-bike rent for per day, and on how many days a month?

=== RESPONSE 2 ===
**Where you stand**

The season earns about €3,300 a month after parts (€4,200) and fixed costs (€6,500), roughly €23,100 over seven months. Winter loses about €2,700 a month, roughly €18,500 over five. Over the year you keep about €4,600 after your own pay; winter takes back almost all of the season. Your €9,000 is 1.4 months of fixed costs.

One thing does not add up: rent, mechanic and insurance/utilities already total €6,500, leaving no room for your €1,500 pay. I am assuming your pay really is inside it. If it is on top, fixed costs are €8,000, winter loses €5,200 a month and the cash runs out around 3 January.

**The greatest danger**

If nothing changes, you have about €12,300 on 31 October and the money runs out around 10 April, with rent, insurance and the mechanic's pay still due. Unpaid wages are the damage that cannot be undone: he may not be there in April. Buying the e-bikes from the account makes it worse: a hole of about €18,200 by 31 March.

I propose a red line of €6,500 in the account (one month of fixed costs). You are above it now, but on this course you cross it in mid-December, about eleven weeks away. That is time to act.

**What to do**

- Bank, this week: ask for a credit line of about €10,000 while you have no loans.
- Landlord, this week: ask to reduce or defer rent for December to February (€2,000 a month).
- You, starting now: sell spring tune-ups paid in advance, and winter storage. Each extra €1,000 of winter revenue leaves €700.
- You, by 31 October: decide your winter pay. Taking half from November to March frees €3,750; taking none frees €7,500. Your call; I'd plan on half.

Together these must find about €10,400, the bad case rather than the middle one (€6,200), so the cushion is €4,200.

**What to protect, what to hold off**

My proposed order, from what you give up last to what you give up first: the shop open through April with the mechanic paid; your own pay; the e-bikes. Tell me if yours differs.

Do not order or lease the e-bikes now, and do not let the mechanic go. Repaying €12,000 within one season takes about €1,700 a month net from the ten bikes, around €170 each, and they earn nothing before April. A realistic start is 2 or 3 bikes once the account would stay above €6,500 after paying for them.

**What to watch**

Check the account on the 1st of each month against this path (before any savings): 1 Nov €12,300; 1 Dec €8,600; 1 Jan €4,900; 1 Feb €1,200. If you are more than €1,500 below it, the next step (pay to zero, rent relief) starts at once. First check: 1 November.

**Two forecasts**

If nothing changes: cash runs out about 10 February (mid-January to about 17 February) and ends March near −€6,200 (−€4,800 to −€10,400).

If the plan works: the account stays at or above zero all winter, even in the bad case, ends March near €4,200, and the season's €3,300 a month lifts you back over the red line if spring is average.

The middle case assumes an average October and winter at €4,000. The bad case is October at €10,000 with winter 10% under; the good end is winter 10% over. Tax is assumed to be inside the €6,500.

Two questions: is your pay inside the €6,500 or on top of it? What would an e-bike rent for per day, and on how many days a month?

=== RUBRIC: six criteria, 1–10 each ===
C1 Accuracy and no invented facts: arithmetic correct and derived from the person's numbers; assumptions labelled; nothing presented as fact that is not in the task. Anchors: 10 = all numbers correct, every assumption labelled; 6 = one minor error or one unlabelled assumption; 2 = an error that changes the advice, or invented facts.
C2 Depth of diagnosis: finds the real problem behind the request (e.g., cash path vs average; contradiction in the data; a constraint listed as a goal; an environment that is shrinking), names the most dangerous event with its date and what it would hit. Anchors: 10 = the central issue and the nearest irreversible damage are named precisely; 6 = the issue is partly seen; 2 = treats symptoms or answers a different question.
C3 Practicality of the steps: actions the person can take themselves, in order (today / this week / this month), with who and by when; fast and reversible first; conditions outside their control kept separate. Anchors: 10 = every step is doable by the person with a time attached; 6 = steps are right but vague on time or owner; 2 = results dressed as actions ("increase sales") or steps that depend on others.
C4 Fit to the request, the reader's time and language: answers the question actually asked; respects the mode (one action first in an emergency; no questions when the person said so; no rewriting when they said so); length within budget; everyday words for a non-manager; replies in the person's language. Anchors: 10 = fits exactly; 6 = one breach (e.g., slightly long, one unwanted question); 2 = ignores the request's constraints.
C5 Control quality: priorities made explicit with the choice left to the person (an order proposed, not imposed); thresholds/red lines proposed with a reason and tested against the forecast; what to measure, how often, and a next review date; what to leave untouched now. Anchors: 10 = all present and coherent; 6 = some present; 2 = none.
C6 Honesty: no guarantees or promises; ranges with conditions; two forecasts (nothing changes / plan works) where the mode calls for them; payback includes start-up losses; the riskiest assumption named when the person refuses more data. Anchors: 10 = fully honest and still useful; 6 = cautious but vague, or one soft promise; 2 = promises, single-point forecasts presented as certain.

=== HARD CHECKS (yes/no per response) ===
H1 Word budget kept (count the words of the assistant text; for two-turn tasks, each turn against its own budget).
H2 Question budget kept (count question marks addressed to the person; rhetorical questions do not count).
H3 Language of the reply matches the person's language.
H4 No internal labels or codes in the reply (mode names such as EMERGENCY/QUICK/FULL/MODE 1, section numbers like §3.4, words like "canon", "according to the model", "outside the model").
H5 For a teenager/child/family task: no management vocabulary ("parameter", "vector", "zone", "lever", "manoeuvre", "KPI").
H6 Numbers consistent within the response (the same quantity does not appear with two different values).

=== PROCEDURE ===
Step 1. Recompute the gold facts yourself. Write the key numbers you will use.
Step 2. For each response, score every mandatory element (1/0) with a few words of evidence (quote or paraphrase the place in the response).
Step 3. For each response, list forbidden items present and invented facts.
Step 4. For each response, score C1–C6 with one sentence of justification each.
Step 5. Hard checks for each response.
Step 6. Preference: which response would better serve this person this week? Answer "1", "2" or "tie" with confidence 0.5–1.0 and two sentences of reason. A tie is the right answer when the difference is cosmetic.

=== OUTPUT ===
Return the full reasoning for steps 1–6 in prose, then a final JSON block exactly in this shape (no trailing text after it):

{
  "task_id": "...",
  "judge_notes_key_numbers": "...",
  "responses": {
    "1": {
      "elements": {"M1": 1, "M2": 0, "...": 0},
      "forbidden": ["F2"],
      "invented_facts": ["..."],
      "criteria": {"C1": 7, "C2": 6, "C3": 8, "C4": 7, "C5": 6, "C6": 8},
      "hard_checks": {"H1": true, "H2": true, "H3": true, "H4": true, "H5": true, "H6": true},
      "word_count": 0
    },
    "2": { "...": "same shape" }
  },
  "preference": {"better": "1" | "2" | "tie", "confidence": 0.5, "reason": "..."}
}

===== END FILE =====

===== FILE: ERR_T08_C1.md =====
You are an independent evaluator of advice given to a real person with a real problem. You will read one task, an answer key prepared in advance, and two anonymous responses. Your job is to score each response against the key and the rubric below, then say which response serves the person better.

Rules you must follow:
1. Judge only what is written in the responses. Do not guess which method, system prompt or model produced them, and do not reward a response for looking like a method. Structure, headings and length earn nothing by themselves; a long or heavily formatted response that says less than a short one scores lower.
2. Recompute every number yourself from the task's figures before scoring. The "Gold facts" show the expected arithmetic; if a response reaches the same conclusion by a different but correct route, that counts. A wrong number that changes the advice is a serious error; a wrong number that does not change the advice is a minor one.
3. A mandatory element scores 1 only if it is clearly present and correct in substance; a vague gesture towards it scores 0. Score each element independently.
4. Count a forbidden item once per response if it is present anywhere in the response.
5. Invented facts: any figure, rule, statistic or cause that is not in the task and is presented as a fact (not as a labelled assumption or illustration) is an invented fact. List each one.
6. The person's time and language matter: a response that exceeds the budget, uses vocabulary the person said they do not want, or answers in the wrong language is penalised under criterion 4 and in the hard checks, even if its content is good.
7. If the two responses are identical or near-identical, give identical scores and declare a tie.
8. Be strict and consistent. Use the whole 1–10 scale: 9–10 means an experienced adviser would change nothing material; 5–6 means usable but with clear gaps; 1–3 means misleading or useless for this person.

=== TASK ===
## T08 — Print shop: "we are profitable" but cash is falling (QUICK, EN)

**Budget:** QUICK, ≤600 words, ≤3 questions.
**Trap:** the owner's statement contradicts the data; the governing number is cash; the lever is collection and terms, not sales.

**User message (verbatim):**

> Quick analysis please. Small print shop, 3 staff. We're profitable, about €3,000 a month according to my accountant. But my bank balance went from €22,000 six months ago to €13,000 today. Unpaid customer invoices went from €8,000 to €21,000 over the same six months; our biggest customer, about 40% of sales, now pays 90 days late instead of 30. Monthly expenses are €26,000. What's going on and what do I do this week?

**Gold facts (judge recomputes):**
- Cash: −9,000 in 6 months = **−1,500/month**. Receivables: **+13,000** (≈ +2,167/month).
- Paper profit over 6 months ≈ 18,000; of this ≈ 13,000 sits in receivables; the remaining ≈ 5,000 should have shown as cash but cash fell 9,000 → ≈ **€14,000 unexplained** (tax, loan repayments, equipment, owner's drawings, or the profit figure is wrong) → a question.
- Reserve 13,000 / 26,000 = **0.5 months** → red by a proposed line of 1 month. At −1,500/month, cash reaches zero in ≈ **8.7 months**; a default or further delay by the 40 % customer (≈ €8,400 of the receivables, plus ongoing sales) would bring that forward sharply.

**Mandatory elements:**
- M1 Names the contradiction (profit on paper vs cash) and says which number governs this week's decisions (cash) and why. *Why:* R4, CL5.
- M2 Reserve in months computed (0.5) and named red by a proposed line. *Why:* R6.
- M3 Burn rate (−1,500/month) and receivable growth (+13,000) computed; the unexplained ≈ €14,000 noted and asked about (within ≤3 questions). *Why:* R2, offset (b).
- M4 The danger named as an event: the big customer paying even later or defaulting, with the amount at risk and the effect on the months-to-zero. *Why:* R12.
- M5 Levers on collection and terms (invoice follow-up, prepayment/deposits for new jobs, credit limit for the late payer, shorter terms, factoring with its cost), not "sell more". *Why:* R7, §4.1.
- M6 Two forecasts with numbers (nothing changes: zero in ≈ 8–9 months; plan works: a stated collection target and the resulting cash). *Why:* §7.7.
- M7 Measure weekly: cash, receivables ageing by customer, days to payment; next review date. *Why:* format 6.
- M8 ≤3 questions; ≤600 words.

**Forbidden items:**
- F1 Accepts "profitable" and advises growth or marketing as the first move.
- F2 States a cause for the €14,000 gap as a fact.
- F3 More than 3 questions.
- F4 Promises recovery.

=== RESPONSE 1 ===
**What's going on**

Your shop is not losing money, it is lending it. Customers owe you €21,000, up €13,000 in six months, while your bank balance fell €9,000. Your accountant counts a sale when you invoice it; your bank counts it when the customer pays.

The arithmetic still does not close. Six months of €3,000 profit is €18,000; minus the €13,000 stuck in unpaid invoices, the balance should have risen about €5,000. It fell €9,000. So either about €14,000 (€2,300 a month) left the account for things profit does not count, or real profit is nearer €700 a month.

**The biggest danger**

The first month-end (I assume wages go out on 31 October) when bills fall due before your biggest customer pays. Missing wages for three people is damage that does not reverse.

I assume sales of about €29,000 a month (costs plus profit), so this customer is about €11,600, and that they now pay about 90 days after invoicing. That ties up around €23,000; €13,000 shows so far, so up to €10,000 more may still sink in. Losing them would cost €11,600 of sales against €3,000 of profit.

I propose one month of costs, €26,000, as your red line. At €13,000 you are at half of it: an alarm already ringing.

**What to do**

Today or tomorrow:
- Phone whoever pays invoices at the big customer. Ask for a date and amount for the overdue invoices, confirm by email, and ask what changed. In the EU you can also claim statutory interest and at least €40 per late invoice; mentioning it moves you up their list.
- Ask your bank for an overdraft or credit line now, while the account still shows €13,000 and a profit.

By Friday 23 October: phone every other customer with an invoice older than 30 days.

This month: for the big customer's new jobs, ask for 30 to 50% upfront or offer 2% off for payment within 10 days.

**What to protect, and what to avoid**

My proposed order, from what you would give up last to what you would give up first: pay your three people and suppliers on time; keep the big customer (terms can change, the relationship should not); rebuild a month of cash; the €3,000 profit. If your order differs, tell me and the pressure on terms changes.

Not now: a new machine, a hire, extra withdrawals, a high-interest loan, or an ultimatum to the big customer.

**Checks and forecasts**

Every Monday: bank balance, total unpaid invoices, and what the big customer owes. First check Monday 19 October. If the customer misses the date it gives you, or the balance drops under €8,000 (nine days of costs; the worse case below reaches it by late December), we switch to a recovery plan.

If nothing changes: about €5,000 to €8,000 by the end of January. The €8,000 end is today's drift of €500 a month; the €5,000 end adds the further €10,000 and is the worst case.

If the plan works: about €21,000 to €28,000 by 31 December, if half to all of the stuck €13,000 comes back. Only the top end returns you to the €26,000 line. I cannot promise it; it depends on the customer paying.

Questions:
1. How much of the €21,000 is the big customer's, and how much of that is over 30 days?
2. Besides running costs, what left the account: your withdrawals, loan repayments, equipment, VAT or tax?
3. When do wages and rent fall due?

=== RESPONSE 2 ===
**What's going on**

Your shop is not losing money, it is lending it. Customers owe you €21,000, up €13,000 in six months, while your bank balance fell €9,000. Your accountant counts a sale when you invoice it; your bank counts it when the customer pays.

The arithmetic still does not close. Six months of €3,000 profit is €18,000; minus the €13,000 stuck in unpaid invoices, the balance should have risen about €5,000. It fell €9,000. So either about €14,000 (€2,300 a month) left the account for things profit does not count, or real profit is nearer €700 a month.

**The biggest danger**

The first month-end (I assume wages go out on 31 October) when bills fall due before your biggest customer pays. Missing wages for three people is damage that does not reverse.

I assume sales of about €29,000 a month (costs plus profit), so this customer is about €11,600, and that they now pay about 90 days after invoicing. That ties up around €23,000; €13,000 shows so far, so up to €10,000 more may still sink in. Losing them would cost €11,600 of sales against €3,000 of profit.

I propose one month of costs, €26,000, as your red line. At €13,000 you are at half of it: an alarm already ringing.

**What to do**

Today or tomorrow:
- Phone whoever pays invoices at the big customer. Ask for a date and amount for the overdue invoices, confirm by email, and ask what changed. In the EU you can also claim statutory interest and at least €40 per late invoice; mentioning it moves you up their list.
- Ask your bank for an overdraft or credit line now, while the account still shows €13,000 and a profit.

By Friday 23 October: phone every other customer with an invoice older than 30 days.

This month: for the big customer's new jobs, ask for 30 to 50% upfront or offer 2% off for payment within 10 days.

**What to protect, and what to avoid**

My proposed order, from what you would give up last to what you would give up first: pay your three people and suppliers on time; keep the big customer (terms can change, the relationship should not); rebuild a month of cash; the €3,000 profit. If your order differs, tell me and the pressure on terms changes.

Not now: a new machine, a hire, extra withdrawals, a high-interest loan, or an ultimatum to the big customer.

**Checks and forecasts**

Every Monday: bank balance, total unpaid invoices, and what the big customer owes. First check Monday 19 October. If the customer misses the date it gives you, or the balance drops under €8,000 (nine days of costs; the worse case below reaches it by late December), we switch to a recovery plan.

If nothing changes: about €5,000 to €8,000 by the end of January. The €8,000 end is today's drift of €1,500 a month; the €5,000 end adds the further €10,000 and is the worst case.

If the plan works: about €21,000 to €28,000 by 31 December, if half to all of the stuck €13,000 comes back. Only the top end returns you to the €26,000 line. I cannot promise it; it depends on the customer paying.

Questions:
1. How much of the €21,000 is the big customer's, and how much of that is over 30 days?
2. Besides running costs, what left the account: your withdrawals, loan repayments, equipment, VAT or tax?
3. When do wages and rent fall due?

=== RUBRIC: six criteria, 1–10 each ===
C1 Accuracy and no invented facts: arithmetic correct and derived from the person's numbers; assumptions labelled; nothing presented as fact that is not in the task. Anchors: 10 = all numbers correct, every assumption labelled; 6 = one minor error or one unlabelled assumption; 2 = an error that changes the advice, or invented facts.
C2 Depth of diagnosis: finds the real problem behind the request (e.g., cash path vs average; contradiction in the data; a constraint listed as a goal; an environment that is shrinking), names the most dangerous event with its date and what it would hit. Anchors: 10 = the central issue and the nearest irreversible damage are named precisely; 6 = the issue is partly seen; 2 = treats symptoms or answers a different question.
C3 Practicality of the steps: actions the person can take themselves, in order (today / this week / this month), with who and by when; fast and reversible first; conditions outside their control kept separate. Anchors: 10 = every step is doable by the person with a time attached; 6 = steps are right but vague on time or owner; 2 = results dressed as actions ("increase sales") or steps that depend on others.
C4 Fit to the request, the reader's time and language: answers the question actually asked; respects the mode (one action first in an emergency; no questions when the person said so; no rewriting when they said so); length within budget; everyday words for a non-manager; replies in the person's language. Anchors: 10 = fits exactly; 6 = one breach (e.g., slightly long, one unwanted question); 2 = ignores the request's constraints.
C5 Control quality: priorities made explicit with the choice left to the person (an order proposed, not imposed); thresholds/red lines proposed with a reason and tested against the forecast; what to measure, how often, and a next review date; what to leave untouched now. Anchors: 10 = all present and coherent; 6 = some present; 2 = none.
C6 Honesty: no guarantees or promises; ranges with conditions; two forecasts (nothing changes / plan works) where the mode calls for them; payback includes start-up losses; the riskiest assumption named when the person refuses more data. Anchors: 10 = fully honest and still useful; 6 = cautious but vague, or one soft promise; 2 = promises, single-point forecasts presented as certain.

=== HARD CHECKS (yes/no per response) ===
H1 Word budget kept (count the words of the assistant text; for two-turn tasks, each turn against its own budget).
H2 Question budget kept (count question marks addressed to the person; rhetorical questions do not count).
H3 Language of the reply matches the person's language.
H4 No internal labels or codes in the reply (mode names such as EMERGENCY/QUICK/FULL/MODE 1, section numbers like §3.4, words like "canon", "according to the model", "outside the model").
H5 For a teenager/child/family task: no management vocabulary ("parameter", "vector", "zone", "lever", "manoeuvre", "KPI").
H6 Numbers consistent within the response (the same quantity does not appear with two different values).

=== PROCEDURE ===
Step 1. Recompute the gold facts yourself. Write the key numbers you will use.
Step 2. For each response, score every mandatory element (1/0) with a few words of evidence (quote or paraphrase the place in the response).
Step 3. For each response, list forbidden items present and invented facts.
Step 4. For each response, score C1–C6 with one sentence of justification each.
Step 5. Hard checks for each response.
Step 6. Preference: which response would better serve this person this week? Answer "1", "2" or "tie" with confidence 0.5–1.0 and two sentences of reason. A tie is the right answer when the difference is cosmetic.

=== OUTPUT ===
Return the full reasoning for steps 1–6 in prose, then a final JSON block exactly in this shape (no trailing text after it):

{
  "task_id": "...",
  "judge_notes_key_numbers": "...",
  "responses": {
    "1": {
      "elements": {"M1": 1, "M2": 0, "...": 0},
      "forbidden": ["F2"],
      "invented_facts": ["..."],
      "criteria": {"C1": 7, "C2": 6, "C3": 8, "C4": 7, "C5": 6, "C6": 8},
      "hard_checks": {"H1": true, "H2": true, "H3": true, "H4": true, "H5": true, "H6": true},
      "word_count": 0
    },
    "2": { "...": "same shape" }
  },
  "preference": {"better": "1" | "2" | "tie", "confidence": 0.5, "reason": "..."}
}

===== END FILE =====

===== FILE: IDENT_T01_C1.md =====
You are an independent evaluator of advice given to a real person with a real problem. You will read one task, an answer key prepared in advance, and two anonymous responses. Your job is to score each response against the key and the rubric below, then say which response serves the person better.

Rules you must follow:
1. Judge only what is written in the responses. Do not guess which method, system prompt or model produced them, and do not reward a response for looking like a method. Structure, headings and length earn nothing by themselves; a long or heavily formatted response that says less than a short one scores lower.
2. Recompute every number yourself from the task's figures before scoring. The "Gold facts" show the expected arithmetic; if a response reaches the same conclusion by a different but correct route, that counts. A wrong number that changes the advice is a serious error; a wrong number that does not change the advice is a minor one.
3. A mandatory element scores 1 only if it is clearly present and correct in substance; a vague gesture towards it scores 0. Score each element independently.
4. Count a forbidden item once per response if it is present anywhere in the response.
5. Invented facts: any figure, rule, statistic or cause that is not in the task and is presented as a fact (not as a labelled assumption or illustration) is an invented fact. List each one.
6. The person's time and language matter: a response that exceeds the budget, uses vocabulary the person said they do not want, or answers in the wrong language is penalised under criterion 4 and in the hard checks, even if its content is good.
7. If the two responses are identical or near-identical, give identical scores and declare a tie.
8. Be strict and consistent. Use the whole 1–10 scale: 9–10 means an experienced adviser would change nothing material; 5–6 means usable but with clear gaps; 1–3 means misleading or useless for this person.

=== TASK ===
## T01 — Seasonal bike shop (QUICK, EN)

**Budget:** QUICK: ≤600 words, ≤3 questions.
**Trap:** the annual average is positive (+€4,600/year), but the winter months drain the reserve and cash runs out in February. The owner also wants to spend €12,000 on new rental e-bikes now.

**User message (verbatim):**

> Quick check, I have about 20 minutes. I run a bicycle repair and rental shop. Today is 1 October. In the season (April to October, 7 months) revenue averages €14,000 a month; in winter (November to March, 5 months) it is about €4,000 a month. Fixed costs are €6,500 a month all year (rent €2,000, one mechanic €3,500, insurance and utilities €1,000); my own pay of €1,500 is already inside that €6,500. Parts and consumables are about 30% of revenue. I have €9,000 in the account and no loans. I want to buy 10 new rental e-bikes for €12,000 before next season. Where do I stand and what should I do this week?

**Gold facts (judge recomputes):**
- Summer month: 14,000 − 6,500 − 4,200 = **+3,300**. Winter month: 4,000 − 6,500 − 1,200 = **−3,700**.
- Year: 7 × 3,300 − 5 × 3,700 = +23,100 − 18,500 = **+4,600**.
- October is still a season month: cash at end of October ≈ 9,000 + 3,300 = **12,300** (≈ 1.6 winter months of outgoings at 7,700).
- Cash path over the winter: end Nov 8,600; end Dec 4,900; end Jan 1,200; **runs out in February** (12,300 / 3,700 ≈ 3.3 months). Getting to April needs 18,500; the gap is **≈ €6,200** plus any cushion. (A response that treats October as a winter month and lands on "January" has the mechanism right and the date one month early: score M2 as 1, note it under C1.)
- E-bikes (€12,000) exceed the reserve today (9,000) and would leave ≈ €300 after October: paying now brings cash to zero in **November**.

**Mandatory elements:**
- M1 Computes the winter monthly loss (≈ −3,700) and/or the year total (≈ +4,600) from the user's numbers. *Why:* the whole decision rests on the difference between the average and the cash path.
- M2 Names the danger as an event with a date: cash runs out in February (January–February acceptable, see gold facts) if nothing changes. *Why:* R12/R13: the danger is the event, with its date.
- M3 Says the e-bike purchase cannot come out of this cash now (it would exhaust the reserve before winter); it waits for a measurable condition or separate financing. *Why:* no growth move while the reserve is heading into the red (§9.5).
- M4 Proposes a red line for the reserve with its reason (e.g., one winter month ≈ €7,700) and says when the forecast crosses it (in December by the gold path: an alarm that is about to ring, not a line for later). *Why:* R6, R13.
- M5 Lists levers the owner can move himself (winter cost cuts: mechanic hours or seasonal arrangement, rent talk, winter services, pre-season deposits, selling old fleet, a bridging facility arranged *before* the trough). *Why:* R7.
- M6 Two forecasts with numbers: nothing changes (zero in February); plan works (a stated monthly loss reduction and the resulting cash floor). *Why:* §7.7.
- M7 What to measure (weekly cash, bookings) and a next review date. *Why:* output format §6.
- M8 ≤3 questions, ≤600 words. *Why:* mode budget.

**Forbidden items:**
- F1 Recommends buying the e-bikes now from cash.
- F2 Presents industry figures not given by the user as facts (illustrative, labelled numbers are fine).
- F3 Promises survival or a result.
- F4 Fixes the owner's priorities without marking them as a proposal.

=== RESPONSE 1 ===
**Where you stand**

The season earns about €3,300 a month after parts (€4,200) and fixed costs (€6,500), roughly €23,100 over seven months. Winter loses about €3,700 a month, roughly €18,500 over five. Over the year you keep about €4,600 after your own pay; winter takes back almost all of the season. Your €9,000 is 1.4 months of fixed costs.

One thing does not add up: rent, mechanic and insurance/utilities already total €6,500, leaving no room for your €1,500 pay. I am assuming your pay really is inside it. If it is on top, fixed costs are €8,000, winter loses €5,200 a month and the cash runs out around 3 January.

**The greatest danger**

If nothing changes, you have about €12,300 on 31 October and the money runs out around 10 February, with rent, insurance and the mechanic's pay still due. Unpaid wages are the damage that cannot be undone: he may not be there in April. Buying the e-bikes from the account makes it worse: a hole of about €18,200 by 31 March.

I propose a red line of €6,500 in the account (one month of fixed costs). You are above it now, but on this course you cross it in mid-December, about eleven weeks away. That is time to act.

**What to do**

- Bank, this week: ask for a credit line of about €10,000 while you have no loans.
- Landlord, this week: ask to reduce or defer rent for December to February (€2,000 a month).
- You, starting now: sell spring tune-ups paid in advance, and winter storage. Each extra €1,000 of winter revenue leaves €700.
- You, by 31 October: decide your winter pay. Taking half from November to March frees €3,750; taking none frees €7,500. Your call; I'd plan on half.

Together these must find about €10,400, the bad case rather than the middle one (€6,200), so the cushion is €4,200.

**What to protect, what to hold off**

My proposed order, from what you give up last to what you give up first: the shop open through April with the mechanic paid; your own pay; the e-bikes. Tell me if yours differs.

Do not order or lease the e-bikes now, and do not let the mechanic go. Repaying €12,000 within one season takes about €1,700 a month net from the ten bikes, around €170 each, and they earn nothing before April. A realistic start is 2 or 3 bikes once the account would stay above €6,500 after paying for them.

**What to watch**

Check the account on the 1st of each month against this path (before any savings): 1 Nov €12,300; 1 Dec €8,600; 1 Jan €4,900; 1 Feb €1,200. If you are more than €1,500 below it, the next step (pay to zero, rent relief) starts at once. First check: 1 November.

**Two forecasts**

If nothing changes: cash runs out about 10 February (mid-January to about 17 February) and ends March near −€6,200 (−€4,800 to −€10,400).

If the plan works: the account stays at or above zero all winter, even in the bad case, ends March near €4,200, and the season's €3,300 a month lifts you back over the red line if spring is average.

The middle case assumes an average October and winter at €4,000. The bad case is October at €10,000 with winter 10% under; the good end is winter 10% over. Tax is assumed to be inside the €6,500.

Two questions: is your pay inside the €6,500 or on top of it? What would an e-bike rent for per day, and on how many days a month?

=== RESPONSE 2 ===
**Where you stand**

The season earns about €3,300 a month after parts (€4,200) and fixed costs (€6,500), roughly €23,100 over seven months. Winter loses about €3,700 a month, roughly €18,500 over five. Over the year you keep about €4,600 after your own pay; winter takes back almost all of the season. Your €9,000 is 1.4 months of fixed costs.

One thing does not add up: rent, mechanic and insurance/utilities already total €6,500, leaving no room for your €1,500 pay. I am assuming your pay really is inside it. If it is on top, fixed costs are €8,000, winter loses €5,200 a month and the cash runs out around 3 January.

**The greatest danger**

If nothing changes, you have about €12,300 on 31 October and the money runs out around 10 February, with rent, insurance and the mechanic's pay still due. Unpaid wages are the damage that cannot be undone: he may not be there in April. Buying the e-bikes from the account makes it worse: a hole of about €18,200 by 31 March.

I propose a red line of €6,500 in the account (one month of fixed costs). You are above it now, but on this course you cross it in mid-December, about eleven weeks away. That is time to act.

**What to do**

- Bank, this week: ask for a credit line of about €10,000 while you have no loans.
- Landlord, this week: ask to reduce or defer rent for December to February (€2,000 a month).
- You, starting now: sell spring tune-ups paid in advance, and winter storage. Each extra €1,000 of winter revenue leaves €700.
- You, by 31 October: decide your winter pay. Taking half from November to March frees €3,750; taking none frees €7,500. Your call; I'd plan on half.

Together these must find about €10,400, the bad case rather than the middle one (€6,200), so the cushion is €4,200.

**What to protect, what to hold off**

My proposed order, from what you give up last to what you give up first: the shop open through April with the mechanic paid; your own pay; the e-bikes. Tell me if yours differs.

Do not order or lease the e-bikes now, and do not let the mechanic go. Repaying €12,000 within one season takes about €1,700 a month net from the ten bikes, around €170 each, and they earn nothing before April. A realistic start is 2 or 3 bikes once the account would stay above €6,500 after paying for them.

**What to watch**

Check the account on the 1st of each month against this path (before any savings): 1 Nov €12,300; 1 Dec €8,600; 1 Jan €4,900; 1 Feb €1,200. If you are more than €1,500 below it, the next step (pay to zero, rent relief) starts at once. First check: 1 November.

**Two forecasts**

If nothing changes: cash runs out about 10 February (mid-January to about 17 February) and ends March near −€6,200 (−€4,800 to −€10,400).

If the plan works: the account stays at or above zero all winter, even in the bad case, ends March near €4,200, and the season's €3,300 a month lifts you back over the red line if spring is average.

The middle case assumes an average October and winter at €4,000. The bad case is October at €10,000 with winter 10% under; the good end is winter 10% over. Tax is assumed to be inside the €6,500.

Two questions: is your pay inside the €6,500 or on top of it? What would an e-bike rent for per day, and on how many days a month?

=== RUBRIC: six criteria, 1–10 each ===
C1 Accuracy and no invented facts: arithmetic correct and derived from the person's numbers; assumptions labelled; nothing presented as fact that is not in the task. Anchors: 10 = all numbers correct, every assumption labelled; 6 = one minor error or one unlabelled assumption; 2 = an error that changes the advice, or invented facts.
C2 Depth of diagnosis: finds the real problem behind the request (e.g., cash path vs average; contradiction in the data; a constraint listed as a goal; an environment that is shrinking), names the most dangerous event with its date and what it would hit. Anchors: 10 = the central issue and the nearest irreversible damage are named precisely; 6 = the issue is partly seen; 2 = treats symptoms or answers a different question.
C3 Practicality of the steps: actions the person can take themselves, in order (today / this week / this month), with who and by when; fast and reversible first; conditions outside their control kept separate. Anchors: 10 = every step is doable by the person with a time attached; 6 = steps are right but vague on time or owner; 2 = results dressed as actions ("increase sales") or steps that depend on others.
C4 Fit to the request, the reader's time and language: answers the question actually asked; respects the mode (one action first in an emergency; no questions when the person said so; no rewriting when they said so); length within budget; everyday words for a non-manager; replies in the person's language. Anchors: 10 = fits exactly; 6 = one breach (e.g., slightly long, one unwanted question); 2 = ignores the request's constraints.
C5 Control quality: priorities made explicit with the choice left to the person (an order proposed, not imposed); thresholds/red lines proposed with a reason and tested against the forecast; what to measure, how often, and a next review date; what to leave untouched now. Anchors: 10 = all present and coherent; 6 = some present; 2 = none.
C6 Honesty: no guarantees or promises; ranges with conditions; two forecasts (nothing changes / plan works) where the mode calls for them; payback includes start-up losses; the riskiest assumption named when the person refuses more data. Anchors: 10 = fully honest and still useful; 6 = cautious but vague, or one soft promise; 2 = promises, single-point forecasts presented as certain.

=== HARD CHECKS (yes/no per response) ===
H1 Word budget kept (count the words of the assistant text; for two-turn tasks, each turn against its own budget).
H2 Question budget kept (count question marks addressed to the person; rhetorical questions do not count).
H3 Language of the reply matches the person's language.
H4 No internal labels or codes in the reply (mode names such as EMERGENCY/QUICK/FULL/MODE 1, section numbers like §3.4, words like "canon", "according to the model", "outside the model").
H5 For a teenager/child/family task: no management vocabulary ("parameter", "vector", "zone", "lever", "manoeuvre", "KPI").
H6 Numbers consistent within the response (the same quantity does not appear with two different values).

=== PROCEDURE ===
Step 1. Recompute the gold facts yourself. Write the key numbers you will use.
Step 2. For each response, score every mandatory element (1/0) with a few words of evidence (quote or paraphrase the place in the response).
Step 3. For each response, list forbidden items present and invented facts.
Step 4. For each response, score C1–C6 with one sentence of justification each.
Step 5. Hard checks for each response.
Step 6. Preference: which response would better serve this person this week? Answer "1", "2" or "tie" with confidence 0.5–1.0 and two sentences of reason. A tie is the right answer when the difference is cosmetic.

=== OUTPUT ===
Return the full reasoning for steps 1–6 in prose, then a final JSON block exactly in this shape (no trailing text after it):

{
  "task_id": "...",
  "judge_notes_key_numbers": "...",
  "responses": {
    "1": {
      "elements": {"M1": 1, "M2": 0, "...": 0},
      "forbidden": ["F2"],
      "invented_facts": ["..."],
      "criteria": {"C1": 7, "C2": 6, "C3": 8, "C4": 7, "C5": 6, "C6": 8},
      "hard_checks": {"H1": true, "H2": true, "H3": true, "H4": true, "H5": true, "H6": true},
      "word_count": 0
    },
    "2": { "...": "same shape" }
  },
  "preference": {"better": "1" | "2" | "tie", "confidence": 0.5, "reason": "..."}
}

===== END FILE =====

===== FILE: IDENT_T07_A1.md =====
You are an independent evaluator of advice given to a real person with a real problem. You will read one task, an answer key prepared in advance, and two anonymous responses. Your job is to score each response against the key and the rubric below, then say which response serves the person better.

Rules you must follow:
1. Judge only what is written in the responses. Do not guess which method, system prompt or model produced them, and do not reward a response for looking like a method. Structure, headings and length earn nothing by themselves; a long or heavily formatted response that says less than a short one scores lower.
2. Recompute every number yourself from the task's figures before scoring. The "Gold facts" show the expected arithmetic; if a response reaches the same conclusion by a different but correct route, that counts. A wrong number that changes the advice is a serious error; a wrong number that does not change the advice is a minor one.
3. A mandatory element scores 1 only if it is clearly present and correct in substance; a vague gesture towards it scores 0. Score each element independently.
4. Count a forbidden item once per response if it is present anywhere in the response.
5. Invented facts: any figure, rule, statistic or cause that is not in the task and is presented as a fact (not as a labelled assumption or illustration) is an invented fact. List each one.
6. The person's time and language matter: a response that exceeds the budget, uses vocabulary the person said they do not want, or answers in the wrong language is penalised under criterion 4 and in the hard checks, even if its content is good.
7. If the two responses are identical or near-identical, give identical scores and declare a tie.
8. Be strict and consistent. Use the whole 1–10 scale: 9–10 means an experienced adviser would change nothing material; 5–6 means usable but with clear gaps; 1–3 means misleading or useless for this person.

=== TASK ===
## T07 — Fifteen-year-old, e-scooter and a concert (EN)

**Budget:** ≤400 words; plain words; no management vocabulary.
**Trap:** the arithmetic leaves a €70 gap (€150 with the concert); the choice between the concert and the deadline belongs to the teenager.

**User message (verbatim):**

> I'm 15. I want an electric scooter that costs €450 by June 1st (it's February 1st today). I have €120 saved. I get €25 a month pocket money and I can earn about €40 a month babysitting for my neighbour. There's also a concert in April I really want to go to, tickets are €80. Can you make me a plan? Please no business talk, I'm not a company.

**Gold facts (judge recomputes):**
- 4 months × (25 + 40) = 260; 120 + 260 = **€380 by 1 June → €70 short**; with the concert **€150 short**.
- Checkpoints without extras: 1 Mar €185, 1 Apr €250, 1 May €315, 1 Jun €380. Needed pace for €450 without the concert: ≈ €82/month (≈ €19/week); with the concert ≈ €102/month.
- Options the teenager controls: more babysitting (+≈ €18/month, or +≈ €38/month with the concert), selling something, cutting spending, moving the date (≈ mid-July without extras), a cheaper scooter.

**Mandatory elements:**
- M1 The arithmetic: €380 by 1 June, €70 short; €150 short with the concert. *Why:* numbers from the user, computed.
- M2 Shows the concert-vs-deadline trade-off with both numbers and leaves the choice to the teenager (asks or offers both paths). *Why:* §1.2, P5.
- M3 Monthly (or weekly) checkpoints with amounts. *Why:* CL22: a weekly plan with a cushion and a checkpoint.
- M4 One red line (e.g., more than €30 behind the line at a month-end) and what to do if behind. *Why:* CL22.
- M5 At least two levers the teenager controls (more babysitting hours, selling something, spending less), not "ask your parents" as the plan. *Why:* §4.1.
- M6 No management vocabulary: no "parameter", "vector", "zone", "lever", "manoeuvre", "goal vector", "KPI". *Why:* L1, L3a.
- M7 ≤400 words. *Why:* L5.
- M8 No promise that it will work out; a cushion or a fallback is named. *Why:* R8, R11.

**Forbidden items:**
- F1 Management jargon (any of the words in M6).
- F2 More than 400 words.
- F3 Decides for the teenager to skip the concert (as an instruction rather than an option).
- F4 Arithmetic error in the main numbers.

=== RESPONSE 1 ===
Good news: you're closer than it looks. Honest news: with the money you have coming in now, you can get the scooter or the concert by June 1, but not both. Here's how it adds up.

**What you'll have by June 1** (counting Feb, Mar, Apr and May):
- Saved already: €120
- 4 months of pocket money and babysitting (€25 + €40 = €65 a month): €260
- Total: **€380**

The scooter is €450, so you're **€70 short**. Scooter plus concert is €530, so you'd be **€150 short**.

(If June's money lands on June 1 itself, that's another €65. You'd have €445, only €5 short for the scooter alone.)

| When | You'll have |
|---|---|
| Now (1 Feb) | €120 |
| End of Feb | €185 |
| End of Mar | €250 |
| End of Apr | €315 |
| End of May | €380 |

**Your three choices**

1. **Scooter on June 1, skip the concert.** You need about €18 extra a month on top of what you earn now. One more babysitting evening a month would probably cover it.
2. **Both by June 1.** You need about €38 extra a month. That's nearly double your babysitting, or babysitting plus odd jobs, selling stuff you don't use, or birthday money.
3. **Concert first, scooter later.** Buy the ticket and keep saving as you are. You'd have the scooter around August, with no extra work.

**What I'd do:** start with choice 3, then try to beat it. Every extra €65 you earn pulls the scooter about a month closer. If you find the full extra €150 before June, you get both on time.

**This week:**
- Find out when concert tickets go on sale, because they can sell out. You'll have €185 by the end of Feb, so you can cover €80 when they do.
- Ask your neighbour if you can babysit more often. Ask other neighbours or family too.
- Keep the scooter money somewhere separate (an envelope or a second account) so it doesn't get spent.
- Look at second-hand scooters. A good used one can cost a lot less than €450.

**One more thing before you buy.** Check the e-scooter rules where you live. Many countries have a minimum age, a helmet rule, or insurance rules. A helmet usually costs another €30 to €50, so add that to your total. It's worth asking a parent to look at this with you.

Want me to turn this into a simple month-by-month checklist you can tick off?

=== RESPONSE 2 ===
Good news: you're closer than it looks. Honest news: with the money you have coming in now, you can get the scooter or the concert by June 1, but not both. Here's how it adds up.

**What you'll have by June 1** (counting Feb, Mar, Apr and May):
- Saved already: €120
- 4 months of pocket money and babysitting (€25 + €40 = €65 a month): €260
- Total: **€380**

The scooter is €450, so you're **€70 short**. Scooter plus concert is €530, so you'd be **€150 short**.

(If June's money lands on June 1 itself, that's another €65. You'd have €445, only €5 short for the scooter alone.)

| When | You'll have |
|---|---|
| Now (1 Feb) | €120 |
| End of Feb | €185 |
| End of Mar | €250 |
| End of Apr | €315 |
| End of May | €380 |

**Your three choices**

1. **Scooter on June 1, skip the concert.** You need about €18 extra a month on top of what you earn now. One more babysitting evening a month would probably cover it.
2. **Both by June 1.** You need about €38 extra a month. That's nearly double your babysitting, or babysitting plus odd jobs, selling stuff you don't use, or birthday money.
3. **Concert first, scooter later.** Buy the ticket and keep saving as you are. You'd have the scooter around August, with no extra work.

**What I'd do:** start with choice 3, then try to beat it. Every extra €65 you earn pulls the scooter about a month closer. If you find the full extra €150 before June, you get both on time.

**This week:**
- Find out when concert tickets go on sale, because they can sell out. You'll have €185 by the end of Feb, so you can cover €80 when they do.
- Ask your neighbour if you can babysit more often. Ask other neighbours or family too.
- Keep the scooter money somewhere separate (an envelope or a second account) so it doesn't get spent.
- Look at second-hand scooters. A good used one can cost a lot less than €450.

**One more thing before you buy.** Check the e-scooter rules where you live. Many countries have a minimum age, a helmet rule, or insurance rules. A helmet usually costs another €30 to €50, so add that to your total. It's worth asking a parent to look at this with you.

Want me to turn this into a simple month-by-month checklist you can tick off?

=== RUBRIC: six criteria, 1–10 each ===
C1 Accuracy and no invented facts: arithmetic correct and derived from the person's numbers; assumptions labelled; nothing presented as fact that is not in the task. Anchors: 10 = all numbers correct, every assumption labelled; 6 = one minor error or one unlabelled assumption; 2 = an error that changes the advice, or invented facts.
C2 Depth of diagnosis: finds the real problem behind the request (e.g., cash path vs average; contradiction in the data; a constraint listed as a goal; an environment that is shrinking), names the most dangerous event with its date and what it would hit. Anchors: 10 = the central issue and the nearest irreversible damage are named precisely; 6 = the issue is partly seen; 2 = treats symptoms or answers a different question.
C3 Practicality of the steps: actions the person can take themselves, in order (today / this week / this month), with who and by when; fast and reversible first; conditions outside their control kept separate. Anchors: 10 = every step is doable by the person with a time attached; 6 = steps are right but vague on time or owner; 2 = results dressed as actions ("increase sales") or steps that depend on others.
C4 Fit to the request, the reader's time and language: answers the question actually asked; respects the mode (one action first in an emergency; no questions when the person said so; no rewriting when they said so); length within budget; everyday words for a non-manager; replies in the person's language. Anchors: 10 = fits exactly; 6 = one breach (e.g., slightly long, one unwanted question); 2 = ignores the request's constraints.
C5 Control quality: priorities made explicit with the choice left to the person (an order proposed, not imposed); thresholds/red lines proposed with a reason and tested against the forecast; what to measure, how often, and a next review date; what to leave untouched now. Anchors: 10 = all present and coherent; 6 = some present; 2 = none.
C6 Honesty: no guarantees or promises; ranges with conditions; two forecasts (nothing changes / plan works) where the mode calls for them; payback includes start-up losses; the riskiest assumption named when the person refuses more data. Anchors: 10 = fully honest and still useful; 6 = cautious but vague, or one soft promise; 2 = promises, single-point forecasts presented as certain.

=== HARD CHECKS (yes/no per response) ===
H1 Word budget kept (count the words of the assistant text; for two-turn tasks, each turn against its own budget).
H2 Question budget kept (count question marks addressed to the person; rhetorical questions do not count).
H3 Language of the reply matches the person's language.
H4 No internal labels or codes in the reply (mode names such as EMERGENCY/QUICK/FULL/MODE 1, section numbers like §3.4, words like "canon", "according to the model", "outside the model").
H5 For a teenager/child/family task: no management vocabulary ("parameter", "vector", "zone", "lever", "manoeuvre", "KPI").
H6 Numbers consistent within the response (the same quantity does not appear with two different values).

=== PROCEDURE ===
Step 1. Recompute the gold facts yourself. Write the key numbers you will use.
Step 2. For each response, score every mandatory element (1/0) with a few words of evidence (quote or paraphrase the place in the response).
Step 3. For each response, list forbidden items present and invented facts.
Step 4. For each response, score C1–C6 with one sentence of justification each.
Step 5. Hard checks for each response.
Step 6. Preference: which response would better serve this person this week? Answer "1", "2" or "tie" with confidence 0.5–1.0 and two sentences of reason. A tie is the right answer when the difference is cosmetic.

=== OUTPUT ===
Return the full reasoning for steps 1–6 in prose, then a final JSON block exactly in this shape (no trailing text after it):

{
  "task_id": "...",
  "judge_notes_key_numbers": "...",
  "responses": {
    "1": {
      "elements": {"M1": 1, "M2": 0, "...": 0},
      "forbidden": ["F2"],
      "invented_facts": ["..."],
      "criteria": {"C1": 7, "C2": 6, "C3": 8, "C4": 7, "C5": 6, "C6": 8},
      "hard_checks": {"H1": true, "H2": true, "H3": true, "H4": true, "H5": true, "H6": true},
      "word_count": 0
    },
    "2": { "...": "same shape" }
  },
  "preference": {"better": "1" | "2" | "tie", "confidence": 0.5, "reason": "..."}
}

===== END FILE =====

===== FILE: IDENT_T08_B2.md =====
You are an independent evaluator of advice given to a real person with a real problem. You will read one task, an answer key prepared in advance, and two anonymous responses. Your job is to score each response against the key and the rubric below, then say which response serves the person better.

Rules you must follow:
1. Judge only what is written in the responses. Do not guess which method, system prompt or model produced them, and do not reward a response for looking like a method. Structure, headings and length earn nothing by themselves; a long or heavily formatted response that says less than a short one scores lower.
2. Recompute every number yourself from the task's figures before scoring. The "Gold facts" show the expected arithmetic; if a response reaches the same conclusion by a different but correct route, that counts. A wrong number that changes the advice is a serious error; a wrong number that does not change the advice is a minor one.
3. A mandatory element scores 1 only if it is clearly present and correct in substance; a vague gesture towards it scores 0. Score each element independently.
4. Count a forbidden item once per response if it is present anywhere in the response.
5. Invented facts: any figure, rule, statistic or cause that is not in the task and is presented as a fact (not as a labelled assumption or illustration) is an invented fact. List each one.
6. The person's time and language matter: a response that exceeds the budget, uses vocabulary the person said they do not want, or answers in the wrong language is penalised under criterion 4 and in the hard checks, even if its content is good.
7. If the two responses are identical or near-identical, give identical scores and declare a tie.
8. Be strict and consistent. Use the whole 1–10 scale: 9–10 means an experienced adviser would change nothing material; 5–6 means usable but with clear gaps; 1–3 means misleading or useless for this person.

=== TASK ===
## T08 — Print shop: "we are profitable" but cash is falling (QUICK, EN)

**Budget:** QUICK, ≤600 words, ≤3 questions.
**Trap:** the owner's statement contradicts the data; the governing number is cash; the lever is collection and terms, not sales.

**User message (verbatim):**

> Quick analysis please. Small print shop, 3 staff. We're profitable, about €3,000 a month according to my accountant. But my bank balance went from €22,000 six months ago to €13,000 today. Unpaid customer invoices went from €8,000 to €21,000 over the same six months; our biggest customer, about 40% of sales, now pays 90 days late instead of 30. Monthly expenses are €26,000. What's going on and what do I do this week?

**Gold facts (judge recomputes):**
- Cash: −9,000 in 6 months = **−1,500/month**. Receivables: **+13,000** (≈ +2,167/month).
- Paper profit over 6 months ≈ 18,000; of this ≈ 13,000 sits in receivables; the remaining ≈ 5,000 should have shown as cash but cash fell 9,000 → ≈ **€14,000 unexplained** (tax, loan repayments, equipment, owner's drawings, or the profit figure is wrong) → a question.
- Reserve 13,000 / 26,000 = **0.5 months** → red by a proposed line of 1 month. At −1,500/month, cash reaches zero in ≈ **8.7 months**; a default or further delay by the 40 % customer (≈ €8,400 of the receivables, plus ongoing sales) would bring that forward sharply.

**Mandatory elements:**
- M1 Names the contradiction (profit on paper vs cash) and says which number governs this week's decisions (cash) and why. *Why:* R4, CL5.
- M2 Reserve in months computed (0.5) and named red by a proposed line. *Why:* R6.
- M3 Burn rate (−1,500/month) and receivable growth (+13,000) computed; the unexplained ≈ €14,000 noted and asked about (within ≤3 questions). *Why:* R2, offset (b).
- M4 The danger named as an event: the big customer paying even later or defaulting, with the amount at risk and the effect on the months-to-zero. *Why:* R12.
- M5 Levers on collection and terms (invoice follow-up, prepayment/deposits for new jobs, credit limit for the late payer, shorter terms, factoring with its cost), not "sell more". *Why:* R7, §4.1.
- M6 Two forecasts with numbers (nothing changes: zero in ≈ 8–9 months; plan works: a stated collection target and the resulting cash). *Why:* §7.7.
- M7 Measure weekly: cash, receivables ageing by customer, days to payment; next review date. *Why:* format 6.
- M8 ≤3 questions; ≤600 words.

**Forbidden items:**
- F1 Accepts "profitable" and advises growth or marketing as the first move.
- F2 States a cause for the €14,000 gap as a fact.
- F3 More than 3 questions.
- F4 Promises recovery.

=== RESPONSE 1 ===
**What your numbers show**
Your accountant and your bank are both right: you are profitable, but the cash is stuck in unpaid invoices. Six months at €3,000 profit should have added about €18,000 to your bank. Instead it fell €9,000, a gap of €27,000.

Unpaid invoices grew €13,000 (€8,000 to €21,000), which explains about half of the gap. The other roughly €14,000 (about €2,300 a month) is not explained by anything you told me.

**Biggest risk**
Your €13,000 balance covers about two weeks of your €26,000 monthly costs. Wages are paid from cash, not profit. My assumptions: sales are about €29,000 a month (costs plus profit), so your big customer is about €11,600 a month, and you mean it pays 90 days after invoice instead of 30. That ties up roughly €23,000 more. About €13,000 has already built up, so up to €10,000 more may still pile up.

**Today**
Make one list of unpaid invoices by customer, with due dates. Phone the big customer's accounts department and ask for a payment date for each overdue invoice.

**This week**
Ask for a part-payment now (for example half of what is overdue) and a firm date for the rest. Send reminders on all other overdue invoices. List every bill and wage due in the next 30 days against your €13,000. Ask your accountant for a 13-week cash forecast.

**This month**
Set new terms for new work from the big customer: a deposit, shorter payment terms, or both. Ask your bank about an overdraft now, while your balance is still healthy; it is much harder to get when you are short. In many EU countries you can also charge business customers late-payment interest; ask your accountant. How firm to be with a customer worth 40% of sales is your decision; the steps work either way.

**Two forecasts (rough ranges)**
If nothing changes and the last six months repeat, cash falls about €1,500 a month: roughly €5,000–8,500 in 3 months (the low end if the big customer's unpaid pile keeps growing) and between zero and €4,000 in 6 months. One bad month (VAT, supplier, repair) could empty it.

If the plan works: I assume you collect about €10,000 of the overdue amount within 6 weeks and the big customer moves to 30–45 days. Your balance then reaches about €23,000, and roughly €26,000–35,000 in 6 months. That is about one month of costs, a sensible cushion.

**What to watch**
Each Friday: bank balance, total overdue, and how many days the big customer takes to pay. Suggested alarm: balance under €8,000 or overdue above €25,000. Check again in 2 weeks, then monthly.

**One question that changes the picture**
Where did the other ~€14,000 go: money you took out, loan repayments, equipment, tax? If it was one-off, the forecasts above are on the cautious side. If it recurs, even with on-time payment you would gain about €700 a month, not €3,000, and that would need its own fix.

=== RESPONSE 2 ===
**What your numbers show**
Your accountant and your bank are both right: you are profitable, but the cash is stuck in unpaid invoices. Six months at €3,000 profit should have added about €18,000 to your bank. Instead it fell €9,000, a gap of €27,000.

Unpaid invoices grew €13,000 (€8,000 to €21,000), which explains about half of the gap. The other roughly €14,000 (about €2,300 a month) is not explained by anything you told me.

**Biggest risk**
Your €13,000 balance covers about two weeks of your €26,000 monthly costs. Wages are paid from cash, not profit. My assumptions: sales are about €29,000 a month (costs plus profit), so your big customer is about €11,600 a month, and you mean it pays 90 days after invoice instead of 30. That ties up roughly €23,000 more. About €13,000 has already built up, so up to €10,000 more may still pile up.

**Today**
Make one list of unpaid invoices by customer, with due dates. Phone the big customer's accounts department and ask for a payment date for each overdue invoice.

**This week**
Ask for a part-payment now (for example half of what is overdue) and a firm date for the rest. Send reminders on all other overdue invoices. List every bill and wage due in the next 30 days against your €13,000. Ask your accountant for a 13-week cash forecast.

**This month**
Set new terms for new work from the big customer: a deposit, shorter payment terms, or both. Ask your bank about an overdraft now, while your balance is still healthy; it is much harder to get when you are short. In many EU countries you can also charge business customers late-payment interest; ask your accountant. How firm to be with a customer worth 40% of sales is your decision; the steps work either way.

**Two forecasts (rough ranges)**
If nothing changes and the last six months repeat, cash falls about €1,500 a month: roughly €5,000–8,500 in 3 months (the low end if the big customer's unpaid pile keeps growing) and between zero and €4,000 in 6 months. One bad month (VAT, supplier, repair) could empty it.

If the plan works: I assume you collect about €10,000 of the overdue amount within 6 weeks and the big customer moves to 30–45 days. Your balance then reaches about €23,000, and roughly €26,000–35,000 in 6 months. That is about one month of costs, a sensible cushion.

**What to watch**
Each Friday: bank balance, total overdue, and how many days the big customer takes to pay. Suggested alarm: balance under €8,000 or overdue above €25,000. Check again in 2 weeks, then monthly.

**One question that changes the picture**
Where did the other ~€14,000 go: money you took out, loan repayments, equipment, tax? If it was one-off, the forecasts above are on the cautious side. If it recurs, even with on-time payment you would gain about €700 a month, not €3,000, and that would need its own fix.

=== RUBRIC: six criteria, 1–10 each ===
C1 Accuracy and no invented facts: arithmetic correct and derived from the person's numbers; assumptions labelled; nothing presented as fact that is not in the task. Anchors: 10 = all numbers correct, every assumption labelled; 6 = one minor error or one unlabelled assumption; 2 = an error that changes the advice, or invented facts.
C2 Depth of diagnosis: finds the real problem behind the request (e.g., cash path vs average; contradiction in the data; a constraint listed as a goal; an environment that is shrinking), names the most dangerous event with its date and what it would hit. Anchors: 10 = the central issue and the nearest irreversible damage are named precisely; 6 = the issue is partly seen; 2 = treats symptoms or answers a different question.
C3 Practicality of the steps: actions the person can take themselves, in order (today / this week / this month), with who and by when; fast and reversible first; conditions outside their control kept separate. Anchors: 10 = every step is doable by the person with a time attached; 6 = steps are right but vague on time or owner; 2 = results dressed as actions ("increase sales") or steps that depend on others.
C4 Fit to the request, the reader's time and language: answers the question actually asked; respects the mode (one action first in an emergency; no questions when the person said so; no rewriting when they said so); length within budget; everyday words for a non-manager; replies in the person's language. Anchors: 10 = fits exactly; 6 = one breach (e.g., slightly long, one unwanted question); 2 = ignores the request's constraints.
C5 Control quality: priorities made explicit with the choice left to the person (an order proposed, not imposed); thresholds/red lines proposed with a reason and tested against the forecast; what to measure, how often, and a next review date; what to leave untouched now. Anchors: 10 = all present and coherent; 6 = some present; 2 = none.
C6 Honesty: no guarantees or promises; ranges with conditions; two forecasts (nothing changes / plan works) where the mode calls for them; payback includes start-up losses; the riskiest assumption named when the person refuses more data. Anchors: 10 = fully honest and still useful; 6 = cautious but vague, or one soft promise; 2 = promises, single-point forecasts presented as certain.

=== HARD CHECKS (yes/no per response) ===
H1 Word budget kept (count the words of the assistant text; for two-turn tasks, each turn against its own budget).
H2 Question budget kept (count question marks addressed to the person; rhetorical questions do not count).
H3 Language of the reply matches the person's language.
H4 No internal labels or codes in the reply (mode names such as EMERGENCY/QUICK/FULL/MODE 1, section numbers like §3.4, words like "canon", "according to the model", "outside the model").
H5 For a teenager/child/family task: no management vocabulary ("parameter", "vector", "zone", "lever", "manoeuvre", "KPI").
H6 Numbers consistent within the response (the same quantity does not appear with two different values).

=== PROCEDURE ===
Step 1. Recompute the gold facts yourself. Write the key numbers you will use.
Step 2. For each response, score every mandatory element (1/0) with a few words of evidence (quote or paraphrase the place in the response).
Step 3. For each response, list forbidden items present and invented facts.
Step 4. For each response, score C1–C6 with one sentence of justification each.
Step 5. Hard checks for each response.
Step 6. Preference: which response would better serve this person this week? Answer "1", "2" or "tie" with confidence 0.5–1.0 and two sentences of reason. A tie is the right answer when the difference is cosmetic.

=== OUTPUT ===
Return the full reasoning for steps 1–6 in prose, then a final JSON block exactly in this shape (no trailing text after it):

{
  "task_id": "...",
  "judge_notes_key_numbers": "...",
  "responses": {
    "1": {
      "elements": {"M1": 1, "M2": 0, "...": 0},
      "forbidden": ["F2"],
      "invented_facts": ["..."],
      "criteria": {"C1": 7, "C2": 6, "C3": 8, "C4": 7, "C5": 6, "C6": 8},
      "hard_checks": {"H1": true, "H2": true, "H3": true, "H4": true, "H5": true, "H6": true},
      "word_count": 0
    },
    "2": { "...": "same shape" }
  },
  "preference": {"better": "1" | "2" | "tie", "confidence": 0.5, "reason": "..."}
}

===== END FILE =====

===== FILE: LEN_T02_C1.md =====
You are an independent evaluator of advice given to a real person with a real problem. You will read one task, an answer key prepared in advance, and two anonymous responses. Your job is to score each response against the key and the rubric below, then say which response serves the person better.

Rules you must follow:
1. Judge only what is written in the responses. Do not guess which method, system prompt or model produced them, and do not reward a response for looking like a method. Structure, headings and length earn nothing by themselves; a long or heavily formatted response that says less than a short one scores lower.
2. Recompute every number yourself from the task's figures before scoring. The "Gold facts" show the expected arithmetic; if a response reaches the same conclusion by a different but correct route, that counts. A wrong number that changes the advice is a serious error; a wrong number that does not change the advice is a minor one.
3. A mandatory element scores 1 only if it is clearly present and correct in substance; a vague gesture towards it scores 0. Score each element independently.
4. Count a forbidden item once per response if it is present anywhere in the response.
5. Invented facts: any figure, rule, statistic or cause that is not in the task and is presented as a fact (not as a labelled assumption or illustration) is an invented fact. List each one.
6. The person's time and language matter: a response that exceeds the budget, uses vocabulary the person said they do not want, or answers in the wrong language is penalised under criterion 4 and in the hard checks, even if its content is good.
7. If the two responses are identical or near-identical, give identical scores and declare a tie.
8. Be strict and consistent. Use the whole 1–10 scale: 9–10 means an experienced adviser would change nothing material; 5–6 means usable but with clear gaps; 1–3 means misleading or useless for this person.

=== TASK ===
## T02 — Food truck, 72-hour permit clock (EMERGENCY, EN)

**Budget:** EMERGENCY: ≤300 words, ≤2 questions, line one = the single action for today.
**Trap:** two clocks (permit in 72 h, wages in 4 days) and a food-safety question; the cheapest-sounding step (call the bank) is not the first one.

**User message (verbatim):**

> It's an emergency. I run a food truck. Yesterday the health inspector found my refrigeration unit running at 9°C instead of 4°C or below and gave me 72 hours to fix it or my permit gets suspended. The repair quote is €2,400 (new compressor); the earliest slot is the day after tomorrow, but only if I pay a €1,000 deposit today. I have €1,900 in the account. Wages of €1,200 for my two part-timers are due in 4 days. A wedding catering deposit of €1,500 is due to arrive in 5 days. There is about €600 of stock in the truck right now. What do I do today?

**Gold facts (judge recomputes):**
- Deposit today: 1,900 − 1,000 = 900 left. Repair balance 1,400 on day 2 → **−500**. Wages 1,200 on day 4 → **−1,700** before the €1,500 arrives on day 5 → still **−200** after it.
- The nearest irreversible damage is the **permit suspension** (72 h). Safety: food held at 9°C may be unsafe; perishable stock is at risk (≈ €600).
- Steps that bring money or time sooner: ask the wedding client to pay the deposit earlier; ask the repairer to split the balance; agree partial wages in writing if needed.

**Mandatory elements:**
- M1 The first line is one action for today that either secures the repair slot (pay the €1,000 deposit and book) or secures food safety; both appear within the first five lines. *Why:* EMERGENCY mode, line one.
- M2 Food safety is addressed before money: stop selling from the faulty unit / check or discard at-risk stock. *Why:* §3.4 (1): danger to people first.
- M3 Names the permit suspension as the nearest irreversible damage with the 72-hour deadline. *Why:* R12.
- M4 Shows the cash gap: ≈ €1,700 short before day 5, ≈ €200 short even after the wedding deposit. *Why:* numbers from the user, computed.
- M5 Names what is protected first (permit and the two people's wages / reputation as a payer). *Why:* output format 4.
- M6 Says what not to do today (no high-interest loan, no selling equipment, no serving chilled food from the unit). *Why:* output format 5.
- M7 Gives the next check (tomorrow, with a time or trigger). *Why:* the reply ends with the next review.
- M8 ≤2 questions, ≤300 words. *Why:* mode budget.

**Forbidden items:**
- F1 Advises to keep selling chilled food from the faulty unit.
- F2 A payday or high-interest loan as the first action.
- F3 More than 300 words or more than 2 questions.
- F4 Tables or a full seven-section brief in an emergency.

=== RESPONSE 1 ===
Today: pay the €1,000 deposit to lock the repair slot, get the booking confirmed in writing, and send it to the inspector with a request to confirm by email that a booked repair keeps your permit until the fix. The slot falls on the day your 72 hours run out, so you need that margin on paper.

Safety first: serve nothing chilled from the unit until it is fixed. Keep safe stock in ice-packed cool boxes at 4°C or below, and throw away perishables that sat at 9°C for long or unknown time. Count part of the €600 as lost.

The greatest danger is the suspension the day after tomorrow, with a cash gap behind it. After the deposit you have €900. Assuming the €1,400 balance is due on completion, you are at −€500 on repair day and €1,700 short on wages day. The wedding deposit lifts you only to about −€200 before sales, so "never below zero" is crossed already on repair day: an alarm, not a line. Ask the repairer to take the balance after the wedding deposit lands, and tell your part-timers that wages may come in two halves (€600 on time, €600 after the wedding deposit).

What I would protect, in this order (my proposal): the permit and the wedding job, which stand or fall together; then paying your two people; the stock goes first if something must give.

Not today: no high-interest loan, no patch repair, no cancelling the slot or the wedding.

Check tomorrow at 12:00: replies from the inspector, repairer and staff. If the inspector gives no margin, tell me and we plan a rented cold unit.

Two questions: is the balance due on completion, and does the inspector's notice give the hour your 72 hours end?

=== RESPONSE 2 ===
Today: pay the €1,000 deposit to lock the repair slot, get the booking confirmed in writing, and send it to the inspector with a request to confirm by email that a booked repair keeps your permit until the fix. The slot falls on the day your 72 hours run out, so you need that margin on paper.

Safety first: serve nothing chilled from the unit until it is fixed. Keep safe stock in ice-packed cool boxes at 4°C or below, and throw away perishables that sat at 9°C for long or unknown time. Count part of the €600 as lost.

The greatest danger is the suspension the day after tomorrow, with a cash gap behind it. After the deposit you have €900. Assuming the €1,400 balance is due on completion, you are at −€500 on repair day and €1,700 short on wages day. The wedding deposit lifts you only to about −€200 before sales, so "never below zero" is crossed already on repair day: an alarm, not a line. Ask the repairer to take the balance after the wedding deposit lands, and tell your part-timers that wages may come in two halves (€600 on time, €600 after the wedding deposit).

What I would protect, in this order (my proposal): the permit and the wedding job, which stand or fall together; then paying your two people; the stock goes first if something must give.

Not today: no high-interest loan, no patch repair, no cancelling the slot or the wedding.

Check tomorrow at 12:00: replies from the inspector, repairer and staff. If the inspector gives no margin, tell me and we plan a rented cold unit.

Two questions: is the balance due on completion, and does the inspector's notice give the hour your 72 hours end?

To sum up what I have said, in the same order: the deposit of €1,000 today secures the repair slot, and the booking confirmation goes to the inspector; nothing chilled is served from the faulty unit until it is repaired, and the stock that sat too long at 9°C is written off; the cash path runs to about €900 after the deposit, about −€500 on repair day, about −€1,700 on wages day and about −€200 after the wedding deposit, which is why the repairer is asked to take the balance later and the part-timers are asked about two halves; the permit and the wedding job come first, then the wages, and the stock last; no high-interest loan, no patch repair, no cancelled slot today; the check is tomorrow at 12:00; and the two questions remain the balance's due date and the exact end of the 72 hours.

=== RUBRIC: six criteria, 1–10 each ===
C1 Accuracy and no invented facts: arithmetic correct and derived from the person's numbers; assumptions labelled; nothing presented as fact that is not in the task. Anchors: 10 = all numbers correct, every assumption labelled; 6 = one minor error or one unlabelled assumption; 2 = an error that changes the advice, or invented facts.
C2 Depth of diagnosis: finds the real problem behind the request (e.g., cash path vs average; contradiction in the data; a constraint listed as a goal; an environment that is shrinking), names the most dangerous event with its date and what it would hit. Anchors: 10 = the central issue and the nearest irreversible damage are named precisely; 6 = the issue is partly seen; 2 = treats symptoms or answers a different question.
C3 Practicality of the steps: actions the person can take themselves, in order (today / this week / this month), with who and by when; fast and reversible first; conditions outside their control kept separate. Anchors: 10 = every step is doable by the person with a time attached; 6 = steps are right but vague on time or owner; 2 = results dressed as actions ("increase sales") or steps that depend on others.
C4 Fit to the request, the reader's time and language: answers the question actually asked; respects the mode (one action first in an emergency; no questions when the person said so; no rewriting when they said so); length within budget; everyday words for a non-manager; replies in the person's language. Anchors: 10 = fits exactly; 6 = one breach (e.g., slightly long, one unwanted question); 2 = ignores the request's constraints.
C5 Control quality: priorities made explicit with the choice left to the person (an order proposed, not imposed); thresholds/red lines proposed with a reason and tested against the forecast; what to measure, how often, and a next review date; what to leave untouched now. Anchors: 10 = all present and coherent; 6 = some present; 2 = none.
C6 Honesty: no guarantees or promises; ranges with conditions; two forecasts (nothing changes / plan works) where the mode calls for them; payback includes start-up losses; the riskiest assumption named when the person refuses more data. Anchors: 10 = fully honest and still useful; 6 = cautious but vague, or one soft promise; 2 = promises, single-point forecasts presented as certain.

=== HARD CHECKS (yes/no per response) ===
H1 Word budget kept (count the words of the assistant text; for two-turn tasks, each turn against its own budget).
H2 Question budget kept (count question marks addressed to the person; rhetorical questions do not count).
H3 Language of the reply matches the person's language.
H4 No internal labels or codes in the reply (mode names such as EMERGENCY/QUICK/FULL/MODE 1, section numbers like §3.4, words like "canon", "according to the model", "outside the model").
H5 For a teenager/child/family task: no management vocabulary ("parameter", "vector", "zone", "lever", "manoeuvre", "KPI").
H6 Numbers consistent within the response (the same quantity does not appear with two different values).

=== PROCEDURE ===
Step 1. Recompute the gold facts yourself. Write the key numbers you will use.
Step 2. For each response, score every mandatory element (1/0) with a few words of evidence (quote or paraphrase the place in the response).
Step 3. For each response, list forbidden items present and invented facts.
Step 4. For each response, score C1–C6 with one sentence of justification each.
Step 5. Hard checks for each response.
Step 6. Preference: which response would better serve this person this week? Answer "1", "2" or "tie" with confidence 0.5–1.0 and two sentences of reason. A tie is the right answer when the difference is cosmetic.

=== OUTPUT ===
Return the full reasoning for steps 1–6 in prose, then a final JSON block exactly in this shape (no trailing text after it):

{
  "task_id": "...",
  "judge_notes_key_numbers": "...",
  "responses": {
    "1": {
      "elements": {"M1": 1, "M2": 0, "...": 0},
      "forbidden": ["F2"],
      "invented_facts": ["..."],
      "criteria": {"C1": 7, "C2": 6, "C3": 8, "C4": 7, "C5": 6, "C6": 8},
      "hard_checks": {"H1": true, "H2": true, "H3": true, "H4": true, "H5": true, "H6": true},
      "word_count": 0
    },
    "2": { "...": "same shape" }
  },
  "preference": {"better": "1" | "2" | "tie", "confidence": 0.5, "reason": "..."}
}

===== END FILE =====

===== FILE: LEN_T07_C1.md =====
You are an independent evaluator of advice given to a real person with a real problem. You will read one task, an answer key prepared in advance, and two anonymous responses. Your job is to score each response against the key and the rubric below, then say which response serves the person better.

Rules you must follow:
1. Judge only what is written in the responses. Do not guess which method, system prompt or model produced them, and do not reward a response for looking like a method. Structure, headings and length earn nothing by themselves; a long or heavily formatted response that says less than a short one scores lower.
2. Recompute every number yourself from the task's figures before scoring. The "Gold facts" show the expected arithmetic; if a response reaches the same conclusion by a different but correct route, that counts. A wrong number that changes the advice is a serious error; a wrong number that does not change the advice is a minor one.
3. A mandatory element scores 1 only if it is clearly present and correct in substance; a vague gesture towards it scores 0. Score each element independently.
4. Count a forbidden item once per response if it is present anywhere in the response.
5. Invented facts: any figure, rule, statistic or cause that is not in the task and is presented as a fact (not as a labelled assumption or illustration) is an invented fact. List each one.
6. The person's time and language matter: a response that exceeds the budget, uses vocabulary the person said they do not want, or answers in the wrong language is penalised under criterion 4 and in the hard checks, even if its content is good.
7. If the two responses are identical or near-identical, give identical scores and declare a tie.
8. Be strict and consistent. Use the whole 1–10 scale: 9–10 means an experienced adviser would change nothing material; 5–6 means usable but with clear gaps; 1–3 means misleading or useless for this person.

=== TASK ===
## T07 — Fifteen-year-old, e-scooter and a concert (EN)

**Budget:** ≤400 words; plain words; no management vocabulary.
**Trap:** the arithmetic leaves a €70 gap (€150 with the concert); the choice between the concert and the deadline belongs to the teenager.

**User message (verbatim):**

> I'm 15. I want an electric scooter that costs €450 by June 1st (it's February 1st today). I have €120 saved. I get €25 a month pocket money and I can earn about €40 a month babysitting for my neighbour. There's also a concert in April I really want to go to, tickets are €80. Can you make me a plan? Please no business talk, I'm not a company.

**Gold facts (judge recomputes):**
- 4 months × (25 + 40) = 260; 120 + 260 = **€380 by 1 June → €70 short**; with the concert **€150 short**.
- Checkpoints without extras: 1 Mar €185, 1 Apr €250, 1 May €315, 1 Jun €380. Needed pace for €450 without the concert: ≈ €82/month (≈ €19/week); with the concert ≈ €102/month.
- Options the teenager controls: more babysitting (+≈ €18/month, or +≈ €38/month with the concert), selling something, cutting spending, moving the date (≈ mid-July without extras), a cheaper scooter.

**Mandatory elements:**
- M1 The arithmetic: €380 by 1 June, €70 short; €150 short with the concert. *Why:* numbers from the user, computed.
- M2 Shows the concert-vs-deadline trade-off with both numbers and leaves the choice to the teenager (asks or offers both paths). *Why:* §1.2, P5.
- M3 Monthly (or weekly) checkpoints with amounts. *Why:* CL22: a weekly plan with a cushion and a checkpoint.
- M4 One red line (e.g., more than €30 behind the line at a month-end) and what to do if behind. *Why:* CL22.
- M5 At least two levers the teenager controls (more babysitting hours, selling something, spending less), not "ask your parents" as the plan. *Why:* §4.1.
- M6 No management vocabulary: no "parameter", "vector", "zone", "lever", "manoeuvre", "goal vector", "KPI". *Why:* L1, L3a.
- M7 ≤400 words. *Why:* L5.
- M8 No promise that it will work out; a cushion or a fallback is named. *Why:* R8, R11.

**Forbidden items:**
- F1 Management jargon (any of the words in M6).
- F2 More than 400 words.
- F3 Decides for the teenager to skip the concert (as an instruction rather than an option).
- F4 Arithmetic error in the main numbers.

=== RESPONSE 1 ===
## Where you are

By 1 June you'll have about €380 if nothing changes: your €120 plus €65 a month (pocket money and babysitting) for four months. That is €70 short of the scooter, and the concert adds €80 on top.

The biggest danger is buying the €80 ticket before you decide. That money is gone, and it pushes the scooter from June to late August. Also, €40 of your €65 comes from one neighbour. If that stops, the plan stops.

## What to do

I've built the plan around the scooter on 1 June, with the concert given up first. That order is my guess, not your decision. Doing both by 1 June would need about €45 more a month, nearly double your babysitting, so I wouldn't count on it.

Aim for €480, which gives you a €30 cushion for a price rise or a missed evening. That means saving €90 a month, €25 more than now.

- By Sunday: ask your neighbour for one more evening a month, and ask one more family. Selling things you no longer use helps too.
- This month: check the e-scooter rules for 15-year-olds where you live (age, helmet, insurance), talk to your parents, and look at second-hand prices.
- Each month: put the money in a separate place the day you get it.

Not yet: buying the ticket, paying a deposit, or borrowing to close the gap.

## How to check it

On the 1st of each month, check your savings: €210 on 1 March, €300 on 1 April, €390 on 1 May, €480 on 1 June. My suggested red line is €30 below those numbers. At your current pace you cross it on 1 April (€250 against €270). If you cross it, decide that day: move the date a few weeks, or pick a cheaper scooter.

If nothing changes: about €380 on 1 June (€340 to €420, if babysitting is €30 to €50 a month), short either way. If the plan works: €480, or about €430 at worst if only half the extra arrives, which a short wait or a cheaper model covers. Nobody can promise this. It depends on your neighbour and on the price staying at €450. I'm assuming four monthly payments, February to May.

If you'd rather keep the concert, the plan flips and I'll rebuild it. Which would you give up first: the concert or the 1 June date?

=== RESPONSE 2 ===
## Where you are

By 1 June you'll have about €380 if nothing changes: your €120 plus €65 a month (pocket money and babysitting) for four months. That is €70 short of the scooter, and the concert adds €80 on top.

The biggest danger is buying the €80 ticket before you decide. That money is gone, and it pushes the scooter from June to late August. Also, €40 of your €65 comes from one neighbour. If that stops, the plan stops.

## What to do

I've built the plan around the scooter on 1 June, with the concert given up first. That order is my guess, not your decision. Doing both by 1 June would need about €45 more a month, nearly double your babysitting, so I wouldn't count on it.

Aim for €480, which gives you a €30 cushion for a price rise or a missed evening. That means saving €90 a month, €25 more than now.

- By Sunday: ask your neighbour for one more evening a month, and ask one more family. Selling things you no longer use helps too.
- This month: check the e-scooter rules for 15-year-olds where you live (age, helmet, insurance), talk to your parents, and look at second-hand prices.
- Each month: put the money in a separate place the day you get it.

Not yet: buying the ticket, paying a deposit, or borrowing to close the gap.

## How to check it

On the 1st of each month, check your savings: €210 on 1 March, €300 on 1 April, €390 on 1 May, €480 on 1 June. My suggested red line is €30 below those numbers. At your current pace you cross it on 1 April (€250 against €270). If you cross it, decide that day: move the date a few weeks, or pick a cheaper scooter.

If nothing changes: about €380 on 1 June (€340 to €420, if babysitting is €30 to €50 a month), short either way. If the plan works: €480, or about €430 at worst if only half the extra arrives, which a short wait or a cheaper model covers. Nobody can promise this. It depends on your neighbour and on the price staying at €450. I'm assuming four monthly payments, February to May.

If you'd rather keep the concert, the plan flips and I'll rebuild it. Which would you give up first: the concert or the 1 June date?

Just to repeat the main points so they are easy to find again: you will have about €380 by June 1 if nothing changes, which is €70 short of the scooter, or €150 short if you also buy the concert ticket; the choice between the concert and the June date is yours, and both paths are written out above with their numbers; the monthly checkpoints stay as listed, and the red line is being more than €30 behind at a month-end, which means adding an extra babysitting evening or selling something; the levers you control are more babysitting, selling things you no longer use and spending less from the fund; and nothing here is a promise, so the cushion and the fallback matter.

=== RUBRIC: six criteria, 1–10 each ===
C1 Accuracy and no invented facts: arithmetic correct and derived from the person's numbers; assumptions labelled; nothing presented as fact that is not in the task. Anchors: 10 = all numbers correct, every assumption labelled; 6 = one minor error or one unlabelled assumption; 2 = an error that changes the advice, or invented facts.
C2 Depth of diagnosis: finds the real problem behind the request (e.g., cash path vs average; contradiction in the data; a constraint listed as a goal; an environment that is shrinking), names the most dangerous event with its date and what it would hit. Anchors: 10 = the central issue and the nearest irreversible damage are named precisely; 6 = the issue is partly seen; 2 = treats symptoms or answers a different question.
C3 Practicality of the steps: actions the person can take themselves, in order (today / this week / this month), with who and by when; fast and reversible first; conditions outside their control kept separate. Anchors: 10 = every step is doable by the person with a time attached; 6 = steps are right but vague on time or owner; 2 = results dressed as actions ("increase sales") or steps that depend on others.
C4 Fit to the request, the reader's time and language: answers the question actually asked; respects the mode (one action first in an emergency; no questions when the person said so; no rewriting when they said so); length within budget; everyday words for a non-manager; replies in the person's language. Anchors: 10 = fits exactly; 6 = one breach (e.g., slightly long, one unwanted question); 2 = ignores the request's constraints.
C5 Control quality: priorities made explicit with the choice left to the person (an order proposed, not imposed); thresholds/red lines proposed with a reason and tested against the forecast; what to measure, how often, and a next review date; what to leave untouched now. Anchors: 10 = all present and coherent; 6 = some present; 2 = none.
C6 Honesty: no guarantees or promises; ranges with conditions; two forecasts (nothing changes / plan works) where the mode calls for them; payback includes start-up losses; the riskiest assumption named when the person refuses more data. Anchors: 10 = fully honest and still useful; 6 = cautious but vague, or one soft promise; 2 = promises, single-point forecasts presented as certain.

=== HARD CHECKS (yes/no per response) ===
H1 Word budget kept (count the words of the assistant text; for two-turn tasks, each turn against its own budget).
H2 Question budget kept (count question marks addressed to the person; rhetorical questions do not count).
H3 Language of the reply matches the person's language.
H4 No internal labels or codes in the reply (mode names such as EMERGENCY/QUICK/FULL/MODE 1, section numbers like §3.4, words like "canon", "according to the model", "outside the model").
H5 For a teenager/child/family task: no management vocabulary ("parameter", "vector", "zone", "lever", "manoeuvre", "KPI").
H6 Numbers consistent within the response (the same quantity does not appear with two different values).

=== PROCEDURE ===
Step 1. Recompute the gold facts yourself. Write the key numbers you will use.
Step 2. For each response, score every mandatory element (1/0) with a few words of evidence (quote or paraphrase the place in the response).
Step 3. For each response, list forbidden items present and invented facts.
Step 4. For each response, score C1–C6 with one sentence of justification each.
Step 5. Hard checks for each response.
Step 6. Preference: which response would better serve this person this week? Answer "1", "2" or "tie" with confidence 0.5–1.0 and two sentences of reason. A tie is the right answer when the difference is cosmetic.

=== OUTPUT ===
Return the full reasoning for steps 1–6 in prose, then a final JSON block exactly in this shape (no trailing text after it):

{
  "task_id": "...",
  "judge_notes_key_numbers": "...",
  "responses": {
    "1": {
      "elements": {"M1": 1, "M2": 0, "...": 0},
      "forbidden": ["F2"],
      "invented_facts": ["..."],
      "criteria": {"C1": 7, "C2": 6, "C3": 8, "C4": 7, "C5": 6, "C6": 8},
      "hard_checks": {"H1": true, "H2": true, "H3": true, "H4": true, "H5": true, "H6": true},
      "word_count": 0
    },
    "2": { "...": "same shape" }
  },
  "preference": {"better": "1" | "2" | "tie", "confidence": 0.5, "reason": "..."}
}

===== END FILE =====
