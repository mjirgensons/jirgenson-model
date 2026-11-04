# Document for evaluation (iteration 1) — paste into Gemini SECOND, in the same conversation, immediately after the judge prompt.

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
