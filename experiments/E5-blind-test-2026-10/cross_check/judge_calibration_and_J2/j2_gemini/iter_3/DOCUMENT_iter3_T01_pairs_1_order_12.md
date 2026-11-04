# Document for evaluation (iteration 3) — paste into Gemini SECOND, in the same conversation, immediately after the judge prompt.

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
