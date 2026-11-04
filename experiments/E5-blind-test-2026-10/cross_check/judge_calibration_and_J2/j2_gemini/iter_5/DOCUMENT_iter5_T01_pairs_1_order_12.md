# Document for evaluation (iteration 5) — paste into Gemini SECOND, in the same conversation, immediately after the judge prompt.

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
## Where you stand

A season month leaves €14,000 − €4,200 (parts) − €6,500 (fixed costs) = +€3,300; seven months give +€23,100. A winter month is €4,000 − €1,200 − €6,500 = −€3,700; five months take back €18,500. The year nets about +€4,600 after your own pay.

I am assuming October brings the usual €14,000, so the account is about €12,300 at the end of October. Each €1,000 less revenue in a month costs €700 of cash.

## The greatest danger: the winter, before any bikes

If nothing changes, the account falls to €8,600 (November), €4,900 (December), €1,200 (January), runs out in February and bottoms out at −€6,200 at the end of March. With revenue 10% off, that is −€3,800 to −€8,600 (the worst end); the conclusion holds. I propose a red line of one month's fixed costs, €6,500; the forecast crosses it in December.

The e-bikes make it worse: €12,000 is €3,000 more than you have today. Paid from the account, you are negative from November and at −€18,200 by March.

## What to do

Decision: no payment for the e-bikes now. Decision point: the start of the season, April. Buying too early: the account is negative from November. Buying too late costs the bikes' first weeks: to repay €12,000 in one season they must add about €1,700 a month, so a month's delay costs about that. Waiting costs less. The orderly exit is a smaller first batch: 4 bikes are €4,800.

This week, all by you:
- Today: ask your bank what a €9,000 credit line (covers the worst end) would cost and require.
- In 3 days: decide your winter pay. €750 instead of €1,500 saves €3,750.
- In 3 days: with the mechanic, check what your contract and local rules allow for fewer winter hours. Each 10% of the mechanic's hours is €350 a month.
- In 7 days: offer past customers a service paid in advance; open paid e-bike pre-bookings; ask the supplier about instalments, a smaller batch and delivery time. Each extra €1,000 of winter revenue adds €700.

## Protect, and leave alone

My proposed order, last to give up first: rent and the mechanic paid on time; your own pay; the e-bikes. Tell me if yours differs; if the bikes outrank your pay, the money must come from outside the account. Not now: any deposit or order for the bikes, a loan for the full €12,000 before paid pre-bookings show demand, skipping rent, insurance, utilities or taxes.

## Check and forecasts

Every Monday: the balance, winter revenue against €5,000 a month, paid pre-bookings. Next check: in one month, when October closes; if the balance is under €11,300, October was over 10% weak and the cuts must go deeper.

Nothing changes: −€6,200 at the end of March. Plan works (pay €750, mechanic's hours −20%, +€1,000 revenue a month; targets to test, not promises): −€1,550 a month, March ends near +€4,550 (worst end +€2,200); the red line is crossed in February, zero never.

Questions:
1. What would one e-bike earn per month in season?
2. Any big winter payments outside the monthly figures (taxes, annual insurance)?

=== RESPONSE 2 ===
On my numbers, winter empties your account around 10 February; the bikes cannot be paid from cash.

A season month leaves you about €3,300 (14,000 − 4,200 parts − 6,500 fixed, your pay included). A winter month loses about €3,700 (4,000 − 1,200 − 6,500). Over a year: +€23,100 and −€18,500, so only €4,600 is left after your own pay, and the bikes cost 2.6 years of it.

I am assuming October brings the season average (if only €10,000, dates come three weeks earlier) and winter holds. My proposed red line is one month of fixed costs, €6,500: below it, rent and your mechanic's pay are no longer safe. You are €2,500 above it today.

**The biggest danger**

On these numbers the account holds €12,300 on 1 November, crosses the red line around 18 December and is empty around 10 February. Then pay and rent are missed; losing your only mechanic is hard to undo. By 1 April the gap is about €6,200 (up to €9,000 if October is weak).

Paying €12,000 for the bikes from the account today leaves −€3,000. Bought in March, the gap on 1 April is about €18,200, so they need outside money, and their payback starts from that gap.

**What to do**

- This week, you: ask your bank now for an overdraft limit of about €6,000 as a safety net, and check its cost.
- This week, you: sell winter work now: tune-up and storage packages, and April rental pre-bookings with a deposit. Each extra €1,000 of winter takings adds €700, but revenue alone cannot close the gap: it needs +€1,800 a month.
- This week, you: ask the supplier for a lease or instalment price, the delivery time, and whether you can start with 4 to 5 bikes.
- By 1 November, you: decide your winter pay (my forecast assumes €1,000 less a month, €5,000 over winter) and ask the landlord about lower winter rent.

Decide on the bikes by 1 March (assuming a month's delivery; check). Too early or all at once: the account goes negative. Too late: you lose April's rental weeks (size unknown without your rental income).

**Protect first, avoid now**

I propose you give up the bikes first, your own pay second, and the open shop with the mechanic and rent paid last. If yours differs, tell me.

Do not sign a 10-bike loan before spring, or cut the mechanic's hours without talking to him first; he may leave.

**Checks and two forecasts**

Every Monday: account balance and week's takings. On 1 November expect about €12,300; under €11,000, or November takings under €3,500, start the pay cut at once; at €6,500, spend only on rent, parts and the mechanic's pay.

If nothing changes: the dates above, then −€6,200 on 1 April. If the plan works (pay down €1,000 a month, winter takings up €1,000 a month): red line touched about 28 January, €2,300 on 1 April (−€1,200 with no extra takings, +€5,800 with €2,000 extra). Next review: 1 November.

One question: what rental income per e-bike do you expect over a season, in euros?
