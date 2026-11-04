# Document for evaluation (iteration 2) — paste into Gemini SECOND, in the same conversation, immediately after the judge prompt.

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
Do not order the e-bikes this autumn. Your own numbers show the account running dry this winter, and the bikes cost more than the account holds.

## Where you are
A season month leaves €3,300 after everything, your pay included (14,000 − 4,200 parts − 6,500 fixed). A winter month loses €3,700 (4,000 − 1,200 − 6,500). Over the year that is +€23,100 and −€18,500, so the shop keeps €4,600 after paying you. The e-bikes cost 2.6 times that.

## The greatest danger
Cash runs out in early February, with rent and the mechanic's wages still due. Buying the bikes from the account would bring that forward to early November.

## What to do
- This week, you: sign nothing and pay no deposit for the bikes. If the seller has an ordering deadline for spring delivery, find out the date.
- By 7 October, you: set your winter pay. I suggest €750 a month, November to March, which saves €3,750. The decision is yours; the number is mine.
- By 15 October, you: check what your contract allows, then ask the mechanic about 20% fewer winter hours by agreement. That saves €700 a month, €3,500 over the winter.
- By 31 October, you: put out a winter servicing offer aimed at €5,000 a month instead of €4,000. Each extra €1,000 leaves €700 after parts, so €3,500 over the winter.
- This month: ask your bank whether a small overdraft is possible for February to May, while the account is healthy. This is a fallback, not part of the plan.

## What we protect first
My proposed order, last to give up first: the shop paying its bills all winter; the mechanic's job; your pay; the e-bikes go first. If your order differs, tell me. If your pay ranks above the mechanic's hours, the cuts move to the hours side and I rebuild the numbers.

## What not to do now
No e-bikes and no other growth spending. To return €12,000 at a 70% margin, the bikes would need about €17,100 of extra rental revenue, roughly €2,450 a month over seven months, before extra insurance or financing. I am assuming the 30% parts share also applies to rentals; I have not checked that. After the winter plan, 10 bikes fit only if the account would still hold €7,400 (two winter months) after paying, and that comes around September. A test of 2 bikes (€2,400) fits from about the end of May.

## What to measure and when to check
Every Monday: the account balance. Each month: winter revenue against €5,000. Next check 1 November, when October's real revenue shows against the €14,000 I assumed. Trigger: if the account is under €10,000 on 1 December, your pay goes to zero.

## Two forecasts
If nothing changes: about €12,300 on 1 November. The proposed red line, €3,700 (one winter month's loss), is crossed in early January. Zero comes in early February, and the account stands near −€6,200 on 1 April, worst case −€7,600. It is back above zero in late May.

If the plan works: about €4,550 on 1 April, above the red line all winter, with all three steps working. With only two working, the account stays positive but dips under the red line in late February and ends near €1,000.

I am assuming October brings €14,000, winter stays at €4,000, and there are no one-off bills (tax, annual insurance) beyond your fixed costs. Any such bill brings the dates forward. A 10% error in winter revenue moves 1 April to between −€7,600 and −€4,800, so the conclusion holds.

Two questions:
1. What do you expect one e-bike to earn in a season?
2. Is the mechanic's contract open to reduced winter hours?

=== RESPONSE 2 ===
I would not order the e-bikes this week. The shop earns a profit over the year, but winter takes about €18,500 out of your account, and without changes the money runs out between mid-January and 10 February.

**Where you stand**

A season month leaves €3,300 after parts (€4,200), fixed costs and your own pay; seven months give €23,100. A winter month loses €3,700; five months lose €18,500. The year ends about €4,600 ahead after your pay, so the €12,000 for the bikes equals 2.6 years of that surplus.

I am assuming October brings the average €14,000: that gives €12,300 on 1 November, or €9,500 if October is weak (€10,000). A 10% error in winter revenue moves March cash by about €1,400; the conclusion holds.

**The danger**

The danger is the winter running dry before spring income, which would hit rent and the mechanic's pay; losing the mechanic before April would cost you the season. With no changes the account ends March at −€6,200 to −€9,000. Paying for the bikes from cash on 1 November would leave about €300, gone within days.

I propose a red line of €3,700 in the account, one winter month of costs. With no changes you cross it between mid-December and 10 January.

**What to do**

This week:
- Ask your bank for a credit line of about €6,000 while the account looks healthy; draw on it only near the red line.
- Ask the supplier for the last order date, the deposit, and leasing or instalments starting in April.
- Decide how much of your own €1,500 stays in the business from November to March; half is €3,750.

By 1 November:
- Sell winter income early: prepaid tune-ups, winter servicing, season-rental bookings with a deposit. Each extra €1,000 of winter revenue keeps €700 after parts, €3,500 over the winter.
- Check whether a tax or VAT instalment falls in winter (in many countries one does); it widens the gap.

**What to protect, what to leave alone**

My proposed order, first to give up to last: the e-bikes this year, then part of your own pay; protected to the end are rent, the mechanic's pay and cash when the season opens. Tell me if yours differs; keeping your full pay, for example, needs a credit line about €3,750 bigger.

Leave alone for now: the e-bike order, a high-interest loan for it, any cut to the mechanic.

**Check and outlook**

Every Monday: account balance and prepaid winter jobs booked. Next review: 1 November. If the balance is then below €9,500, take your own pay to zero for the winter; below €3,700 at any time, draw the credit line and freeze other spending.

If nothing changes: zero between mid-January and 10 February; −€6,200 to −€9,000 at the end of March.

If the plan works (half pay, €1,000 more winter revenue): the monthly loss falls to about €2,250, you cross the red line between mid-January and late February, and March ends at about €1,050 (−€1,750 if October is weak); the credit line covers that.

The bikes earn nothing before April. Repaying €12,000 in one season takes about €1,700 net a month, in two seasons about €860. Paying from cash early leaves you broke; ordering late costs one-seventh of a season's bike income per month.

Two questions: what does one e-bike earn per rental day, and on how many days a season? And how is October running against €14,000?
