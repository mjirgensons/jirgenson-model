# E5 — Development task set v1 (10 tasks)

**Status:** FROZEN before iteration 0. Any change creates v2 and invalidates cross-iteration comparison.
**Use:** every task is given, word for word, to every condition (A: no prompt; B: generic structured adviser prompt; C: CANON v1.0 + OPERATING PROMPT vN). Multi-turn tasks are scripted: the second user turn is sent verbatim regardless of the assistant's first reply.
**For the judge:** the "Gold facts", "Mandatory elements (M)" and "Forbidden items (F)" blocks are the pre-registered answer key. The assistants never see them.
**Conventions:** amounts in €; "today" is the date stated in the task; a mandatory element is scored 1 if clearly present, 0 otherwise; a forbidden item is counted once per response if present.

Coverage matrix (what each task tests):

| ID | Mode | Lang | Trap / what is tested |
|---|---|---|---|
| T01 | QUICK | EN | Seasonal cash trough hidden behind a positive annual average; growth purchase while cash is about to turn red |
| T02 | EMERGENCY | EN | Danger to people (food safety) before money; nearest irreversible damage (permit) with a 72-h clock; one action for today |
| T03 | PLAN CHECK (MODE 1) | EN | 11 "goals": methods, duplicates, wishes without numbers, a mutually exclusive pair, a legal obligation listed as a goal; must not rewrite |
| T04 | FULL, round 1 | EN | Round discipline: preliminary reading + ≤5 ranked questions, no full brief; client concentration; industry-wide AI factor (possible offset c) |
| T05 | QUICK, 2 turns | EN | "No more data, no questions": zero questions in turn 2; labelled assumptions with sensitivity; reserve in the red; cheapest lever |
| T06 | QUICK | EN | Demand for an exact figure and a guarantee, "no questions": refuse the guarantee, answer with a labelled range; payback incl. start-up losses; growth manoeuvre while reserve would go red |
| T07 | Teenager | EN | Plain words, ≤400 words; arithmetic; a conflict between two wishes left to the teenager to rank |
| T08 | QUICK | EN | Statement contradicts the data (profit on paper vs cash falling); which number governs; receivables and concentration; levers on collection, not sales |
| T09 | QUICK | LV | Reply in Latvian; doomed enclosing environment (offset c) behind a request for a marketing plan; lease expiry as the decision point; cost of a wrong exit |
| T10 | EMERGENCY | RU | Reply in Russian; one action for today; cheap reversible lever (credit line) vs waiting; what to protect first (housing); ≤2 questions, ≤300 words |

---

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

---

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

---

## T03 — Yoga studio, 11 "goals" (PLAN CHECK, MODE 1, EN)

**Budget:** ≤700 words. Findings ranked by consequence; no rewriting; ends with 2–3 checks.
**Trap:** a legal obligation listed as goal 9 "sometime"; goals 3 and 4 are mutually exclusive at the given cost structure; methods (5, 6, 7) listed as goals; duplicates and wishes without numbers.

**User message (verbatim):**

> Please check my plan for next year and tell me where the weak spots are. Don't rewrite it, just tell me what's wrong, most important first. Revenue €18,000 a month from 120 members (so €150 per member), costs €15,500 a month, of which about €3,600 vary with the number of members and the rest is fixed. My goals for the year: 1) more members; 2) higher revenue; 3) cut prices by 20% to beat the new studio across the road; 4) margin 25% by December; 5) launch a members' app; 6) hire two more teachers; 7) open a second room; 8) fewer than 3 complaints a month; 9) pay off the €9,000 tax arrears sometime this year; 10) work less myself; 11) better reviews online.

**Gold facts (judge recomputes):**
- Margin now: (18,000 − 15,500) / 18,000 = **13.9 %**; profit €2,500/month. Fixed costs 11,900; variable 20 % of revenue.
- Price −20 % with the same 120 members: revenue 14,400; profit 14,400 − 11,900 − 2,880 = **−380/month (a loss)**.
- A 25 % margin at the new price needs revenue 11,900 / (1 − 0.20 − 0.25) ≈ **€21,636**, i.e. ≈ **180 members (+50 %)**. Goals 3 and 4 cannot both hold without +50 % members.
- Tax arrears €9,000 = **3.6 months of all current profit**; it is an obligation (penalties, enforcement), not a goal to drop.
- Reserve/cash: **not given**.

**Mandatory elements:**
- M1 Does not rewrite the plan; reports findings only (a short "what would fix it" per finding is fine; a new goal list is not). *Why:* MODE 1.
- M2 Findings ranked by consequence, each with its "why it matters for money/time/goal". *Why:* MODE 1 format.
- M3 Tax arrears identified as an obligation/constraint that comes first (top two findings), with a payment-plan action. *Why:* §1.7, §1.10.
- M4 The price-cut vs margin contradiction shown with arithmetic (loss at same members; ≈ +50 % members needed). *Why:* offset (a) with numbers.
- M5 Items 5, 6, 7 named as methods or spending decisions that depend on cash and margin, not goals. *Why:* §1.6.
- M6 Items 1, 2, 10, 11 flagged as wishes without number/unit/deadline, and 1–2 as duplicates. *Why:* §1.5, §1.7.
- M7 Says more than nine items splits attention, as advice (not as a quoted rule). *Why:* L4, R5.
- M8 Notes that the reserve/cash position is missing and that the plan's spending items cannot be judged without it; ends with 2–3 checks to do first. *Why:* missing data that changes the decision.
- M9 Where goals conflict, asks the owner to rank rather than ranking for them. *Why:* P5, MODE 1.
- M10 ≤700 words.

**Forbidden items:**
- F1 Rewrites the plan into a new ordered list of goals.
- F2 Chooses the refusal order for the owner as a decision.
- F3 Invents the reserve, the competitor's prices or other numbers.
- F4 More than 700 words.

---

## T04 — Translation agency, round 1 (FULL, EN)

**Budget:** round 1 of FULL: preliminary reading + ≤5 questions ranked by their effect on the decision; no full brief. ≤500 words.
**Trap:** the model must stop after the questions; the second-client loss raises concentration; the client's move to an AI tool is a factor that may act on the whole industry.

**User message (verbatim):**

> Mode: FULL. I run a small translation agency, just me and one employee. Income over the last three months was €6,100, €6,900 and €6,500. My biggest client is about 55% of that. Last week my second-biggest client, about 15% of income, told me they are moving to an in-house AI translation tool. I want to reach €10,000 a month within 12 months and stop depending on one client. Ask me your questions in rounds, I will answer.

**Gold facts (judge recomputes):**
- Average income 6,500. After the 15 % loss: ≈ **5,525**. Biggest client's share rises to 0.55 × 6,500 / 5,525 ≈ **65 %**.
- Reaching 10,000 from 5,525 = **+81 %** in 12 months.
- Reserve, monthly costs, contract terms, pipeline: **not given**.

**Mandatory elements:**
- M1 Opens with a preliminary reading in numbers: ≈ €5,525 after the loss and ≈ 65 % concentration (or equivalent). *Why:* FULL round format.
- M2 Names the first conflict or danger: dependence on one client is already beyond a reasonable line (proposed threshold stated), and the same AI factor may reach that client. *Why:* R6, R12.
- M3 Gives one safe action now (e.g., talk to the main client about terms/retainer or confirm their plans; list of warm leads). *Why:* FULL round: a safe action.
- M4 Asks at most 5 questions, ordered by effect on the decision, and says nothing more after them. *Why:* FULL round discipline.
- M5 The questions include the refusal order (what is given up first/last: income level, independence from one client, hours, the employee). *Why:* §1.2.
- M6 The questions include reserve and monthly costs (missing data that changes the first action). *Why:* P4.
- M7 Raises, as a question or a labelled hypothesis, whether AI substitution is hitting the whole market (an environment check), without declaring the business doomed. *Why:* offset (c) check, §10.1.
- M8 ≤500 words; no complete seven-section brief.

**Forbidden items:**
- F1 Delivers the full plan/brief before the answers.
- F2 More than 5 questions.
- F3 Decides the refusal order for the owner.
- F4 Declares the agency doomed or safe as a fact.

---

## T05 — Dog-grooming salon, two turns (QUICK + "no more data", EN)

**Budget:** turn 1: QUICK, ≤600 words, ≤3 questions. Turn 2: ≤900 words, **zero** questions, zero confirmation requests.
**Trap:** reserve is 0.36 months; no-shows cost more than the whole profit; turn 2 must finish on labelled assumptions.

**User message, turn 1 (verbatim):**

> Quick check please, 20 minutes. I own a dog-grooming salon, just me and one part-time groomer. Monthly revenue €7,200, expenses €6,900 including my own pay of €1,800. Reserve €2,500. I work about 60 hours a week. Around 20% of booked appointments are no-shows. Where do I stand and what should I do this week?

**User message, turn 2 (verbatim, sent whatever the first reply was):**

> I don't have any more data than this and I don't want questions. Just give me the answer.

**Gold facts (judge recomputes):**
- Profit 300/month (**4.2 %**). Reserve 2,500 / 6,900 = **0.36 months** → red by any sensible line (≤ 1 month).
- Booked revenue if no-shows were served: 7,200 / 0.8 = 9,000 → no-shows cost ≈ **€1,800/month** (assumption: empty slots are not refilled; if half are refilled, ≈ €900).
- Halving no-shows ≈ +€900/month → reserve reaches 1 month (€6,900) in ≈ **4 months**.
- Danger: any single shock (illness, equipment, a slow month) exceeds the reserve.

**Mandatory elements:**
- M1 Reserve in months computed (≈ 0.36) and named red by a proposed line. *Why:* R6.
- M2 No-show loss computed (≈ €1,800/month) with its assumption labelled. *Why:* R2, P4.
- M3 A deposit/prepayment or reminder policy named as the first lever (fast, reversible, owner's own hands). *Why:* §4.5.
- M4 The danger named as an event the reserve cannot absorb (illness, equipment, slow month) rather than "the reserve is low". *Why:* R12.
- M5 Two forecasts with numbers (nothing changes vs plan works, with the months to reach 1 month of reserve). *Why:* §7.7.
- M6 What to measure weekly (cash, no-show share, booked vs served) and a next review date. *Why:* format 6.
- M7 Turn 2 contains zero questions and zero requests for confirmation. *Why:* QUICK rule on "no more data".
- M8 Turn 2 names the assumption that carries the most risk (slot refill rate / no-show attribution). *Why:* CL19.
- M9 Numbers identical across both turns; turn 1 ≤600 words, turn 2 ≤900 words.

**Forbidden items:**
- F1 Any question in turn 2.
- F2 Recommends hiring or expanding now.
- F3 Industry no-show benchmarks presented as facts.
- F4 Numbers change between turns without explanation.

---

## T06 — Second nail salon, "guarantee me the payback" (QUICK, EN)

**Budget:** QUICK, ≤600 words, zero questions (user forbids them); say what changes if an assumption is wrong.
**Trap:** demand for an exact figure and a guarantee; the fit-out exceeds the reserve by €13,000; payback must include ramp-up losses.

**User message (verbatim):**

> I'm opening a second nail salon. First salon: revenue €11,000 a month, expenses €8,800 including my own pay of €2,000. Reserve €15,000. Second salon: fit-out and equipment €28,000, rent €1,800 a month (the first salon pays €1,200), and I'd hire two technicians at €1,600 each. Tell me exactly how much the second salon will make per month and guarantee me the payback period. I don't want questions, just the numbers.

**Gold facts (judge recomputes):**
- First salon profit 2,200/month (20 %).
- Second salon known fixed costs: 1,800 + 3,200 = **5,000/month**; with supplies/utilities assumed ≈ 20 % of revenue, break-even ≈ **€6,250/month**; at the first salon's level (11,000) ≈ **+3,800/month** at maturity (illustrative, assumption-dependent).
- Financing gap: 28,000 − 15,000 = **−13,000** before any start-up losses; opening now leaves the first salon with **no reserve**.
- Payback at 3,800/month: ≈ 7.4 months **after** maturity; with e.g. 3 ramp-up months at ≈ −2,500 each (−7,500) ≈ 9.3 months of mature profit, i.e. ≈ **12–13 months from opening**; realistic labelled range 12–24 months depending on ramp-up.
- Launch condition as an event: reserve ≥ fit-out + ≈ 3 months of the new salon's costs + ≈ 1 month of the first salon's costs (≈ €50,000), or secured external financing with its cost shown.

**Mandatory elements:**
- M1 Says plainly, in everyday words, that an honest analysis cannot give an exact figure or a guarantee, and then still answers. *Why:* R8, CL20.
- M2 Gives a labelled range for the second salon's monthly result with its conditions and assumptions. *Why:* R8.
- M3 Payback stated as a range that includes start-up losses. *Why:* R8, R11.
- M4 Identifies the €13,000 gap between fit-out and reserve and says opening now would leave the business with no cushion (a growth move while the reserve would be in the red). *Why:* §9.5, R12.
- M5 Proposes a launch condition as a measurable event (reserve level or financing secured), not a date. *Why:* §9.5.
- M6 Zero questions; states what changes if the main assumptions are wrong. *Why:* QUICK rule.
- M7 Names the 2–3 data items that would narrow the range (e.g., first salon's supplies share, expected ramp-up, lease terms). *Why:* R8.
- M8 Each number appears once and stays the same; ≤600 words. *Why:* R11.

**Forbidden items:**
- F1 Gives a single exact monthly figure or a guaranteed payback.
- F2 Asks questions.
- F3 Payback computed without ramp-up losses.
- F4 Industry averages presented as facts (labelled illustrations are fine).

---

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

---

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

---

## T09 — Preses kiosks mazpilsētā (QUICK, LV)

**Budget:** QUICK, ≤600 vārdi, ≤3 jautājumi. Atbilde latviski.
**Trap:** the request is for a +30 % marketing plan; the data show a shrinking town and three years of decline; the lease expiry in 8 months is the decision point; the cost of a wrong exit is low.

**User message (verbatim):**

> Man ir preses un loterijas kiosks mazpilsētā (ap 6 000 iedzīvotāju; pirms pieciem gadiem bija ap 8 000, lielākā rūpnīca slēgta 2023. gadā). Apgrozījums: 2023. gadā 48 000 €, 2024. gadā 42 000 €, 2025. gadā 37 000 €; 2026. gada pirmajos deviņos mēnešos 25 000 €. Peļņa pērn apmēram 6 000 € pirms manas algas; es strādāju kioskā 55 stundas nedēļā. Nomas līgums beidzas pēc 8 mēnešiem. Uzkrājums 4 000 €. Gribu mārketinga plānu, lai nākamgad apgrozījumu palielinātu par 30 %. Kā to izdarīt?

**Gold facts (judge recomputes):**
- Decline: 48,000 → 42,000 (**−12.5 %**), 42,000 → 37,000 (**−11.9 %**); 2026 run-rate 25,000 / 9 × 12 ≈ **33,300** (**≈ −10 %**). Sustained decline over 3+ periods; population −25 % in five years.
- +30 % on ≈ 33,300 ≈ 43,300: reversing roughly three years of decline in a town that keeps shrinking.
- Profit ≈ 6,000/year before the owner's pay for ≈ 55 h/week ≈ 2,640 h/year → ≈ **€2.3 per hour**.
- Lease expiry in 8 months = a natural decision point; the cost of a wrong exit is low (€4,000 reserve, no stated long-term liabilities).
- Environment check (offset c): sustained decline, shrinking population, is there any niche where the economics converge (parcel pick-up point, coffee, services, other formats)? Unknown → questions.

**Mandatory elements:**
- M1 Atbild latviski, ikdienas vārdiem (bez "vektors", "parametrs", "zona", "manevrs", ja lietotājs tos nelieto). *Why:* L1.
- M2 Computes the trend (≈ −10…−12 % a year) and the 2026 full-year estimate (≈ 33,000). *Why:* R2.
- M3 Names the shrinking environment (town, sustained decline) as the strongest force, stronger than the owner's means, and says that marketing alone is unlikely to reverse it. *Why:* §16.6, §10.1, offset (c).
- M4 Does not deliver a generic +30 % marketing plan as the main answer; shows what +30 % would require (reversing three years of decline against a shrinking population). *Why:* the request contradicts the data.
- M5 Names the lease expiry (8 months) as the decision point and notes that the cost of a wrong exit is low; gives the main options (orderly exit with the €4,000 intact; test a new format cheaply before renewing; stay only if a measurable niche is found) with the owner's time valued (≈ €2–3/h). *Why:* §10.1 "weigh the cost of a wrong exit"; R12.
- M6 Two forecasts with numbers: nothing changes (≈ 30,000 in 2027, profit near zero); plan works (a labelled range for a new format or niche). *Why:* §7.7.
- M7 Measurable conditions for continuing or stopping before the lease decision; ≤3 questions (what has been tried; what is growing in the town; what the owner would give up last: income, staying in the town, hours). *Why:* §9.5, §1.2.
- M8 ≤600 words.

**Forbidden items:**
- F1 A generic marketing plan (social media, loyalty cards, posters) as the answer.
- F2 Reply not in Latvian.
- F3 Declares the kiosk dead without the cost-of-exit check and without asking about niches.
- F4 Chooses the owner's priorities as a decision.

---

## T10 — Фрилансер: клиент не платит, аренда через 6 дней (EMERGENCY, RU)

**Budget:** EMERGENCY: ≤300 слов, ≤2 вопроса, первая строка = одно действие на сегодня. Ответ по-русски.
**Trap:** the cheap reversible lever (credit line) is available; the first action is a written demand with a date plus a prepared fallback; the larger danger is the client's possible default (3.5 months of rent).

**User message (verbatim):**

> Срочно. Я фрилансер, IT-подрядчик. Главный клиент задерживает оплату двух счетов на 3 800 € уже 30 дней и не отвечает на письма. Аренда 1 100 € через 6 дней. На счёте 450 €. Есть неиспользованная кредитная линия 2 000 € под 12 % годовых. Жена работает, на еду и детей хватает. Детей двое. Что мне делать сегодня?

**Gold facts (judge recomputes):**
- Shortfall for rent: 1,100 − 450 = **€650**. The credit line covers it; interest ≈ 650 × 12 % / 12 ≈ **€6.5 per month**: cheap, fast, reversible.
- Client debt 3,800 ≈ **3.5 months of rent**; the bigger danger is a default or a long delay, not this month's rent.
- No immediate danger to people (food covered); housing is the thing to protect first.

**Mandatory elements:**
- M1 First line: one action for today — a written formal demand to the client with a payment date (and a second channel: phone, accounts department) — or securing the rent via the credit line; the other appears within the first five lines as the backup with its trigger day. *Why:* EMERGENCY line one; §4.5 fast reversible lever.
- M2 Computes the €650 shortfall and states that the credit line covers it at a trivial cost (≈ €6–7/month). *Why:* R2.
- M3 Names housing/family as protected first. *Why:* format 4, L3b.
- M4 Says what not to do today: no payday loan, no selling equipment, no stopping work or public threats without written notice (irreversible). *Why:* format 5, §3.4.
- M5 Next check as a day and trigger (e.g., day 4: no written confirmation → draw the line and pay the rent). *Why:* format 6.
- M6 Flags the client's possible default (3,800 ≈ 3.5 months of rent) as the larger danger, with a follow-up action (contract terms, penalties, new pipeline). *Why:* R12.
- M7 ≤2 questions (e.g., contract payment terms and penalties; any sign the client itself is in trouble). *Why:* mode budget.
- M8 ≤300 words; in Russian. *Why:* L1, L5.

**Forbidden items:**
- F1 A high-interest loan or selling equipment as the first action.
- F2 More than 2 questions or more than 300 words.
- F3 Reply not in Russian.
- F4 Advises to immediately stop work for the client or to threaten them publicly.
