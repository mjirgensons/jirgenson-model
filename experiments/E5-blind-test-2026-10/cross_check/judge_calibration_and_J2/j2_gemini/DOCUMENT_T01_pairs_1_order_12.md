# Document for evaluation — paste into Gemini SECOND, in the same conversation, immediately after the judge prompt.

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
**Short version:** your shop makes about €3,300 a month in season and loses about €3,700 a month in winter. Your cash doesn't cover the winter even without the e-bikes, so don't pay the €12,000 out of your account.

**The numbers (your figures, with your pay already inside the fixed costs)**

- Season month: 14,000 − 4,200 parts − 6,500 fixed = **+€3,300**. Over 7 months that is +€23,100.
- Winter month: 4,000 − 1,200 parts − 6,500 fixed = **−€3,700**. Over 5 months that is −€18,500.
- Full year: about **+€4,600** after your own pay. That is thin.

Cash, starting from €9,000 today, with October still to come:

| End of | Cash |
|---|---|
| October | €12,300 |
| November | €8,600 |
| December | €4,900 |
| January | €1,200 |
| February | −€2,500 |
| March | −€6,200 |

Without the bikes you run out of money around 10 February. You bottom out near −€6,200 at the end of March and are back in the black around May. If you buy the bikes from cash, the bottom becomes −€18,200 and you stay overdrawn until roughly September, unless the bikes earn well.

**Do the bikes pay back?** At your shop's 70% margin, they need about €17,100 of extra revenue to cover €12,000, or about €1,700 per bike. Divide that by your daily rental price to get the days each bike must be rented. I don't have your prices or your likely bookings, so that is the number to test. Rentals may carry less parts cost than repairs, but they have more wear, battery and insurance cost, so treat 70% as rough.

**This week**

1. **Check the inputs.** Pull last winter's actual bank statements for November to March and compare them with my assumptions. Also check October bookings, since every €1,000 of missing October revenue takes about €700 off the cash above.
2. **Ask your bank for an overdraft or credit line of about €10,000.** That covers the €6,200 gap plus a cushion. Banks say yes much more easily while your account is healthy and October profit is still coming in.
3. **Ask the e-bike supplier about leasing, instalments, or paying in March with a small deposit.** Payments in season months only would be ideal. Roughly €12,000 over 24 months is about €500 a month before interest, so it only works if the bikes clearly earn more than that.
4. **Look at winter costs.** Options are the mechanic's winter hours, your own pay from December to February, and pre-paid spring-service offers to bring in cash early. Every €1,000 you save per winter month adds €5,000 to your March position.
5. **Look for demand before you order.** Pre-bookings from hotels, groups or regulars tell you more than a guess does. Decide by about February, which still leaves time to order before April.

**What I left out:** VAT and income tax. If your revenue figures include VAT, or tax payments fall in winter, the picture is tighter. April and October are probably weaker than your €14,000 average, so the October figure could be optimistic.
