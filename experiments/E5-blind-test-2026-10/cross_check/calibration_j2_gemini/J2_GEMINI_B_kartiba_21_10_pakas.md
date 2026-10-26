# J2 Gemini — B daļa (ieteicamā): tie paši 10 pāri, kārtība 21 (pozīcijas nobīdes pārbaude)

Katrs bloks starp līnijām `========== PAKA k/10: <nosaukums> ==========` un `========== PAKAS BEIGAS ==========` ir VIENA pilna tiesneša paka. Procedūra: jauna Gemini saruna → ielīmē visu bloku (bez līnijām) → saglabā VISU Gemini atbildi failā ar pakas nosaukumu (piem. `T01_C-v1.0-r1_vs_A-r1_12.md`).


========== PAKA 1/10: T01_C-v1.0-r1_vs_A-r1_21.md ==========

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


========== PAKAS BEIGAS ==========


========== PAKA 2/10: T02_C-v1.0-r4_vs_B-r1_21.md ==========

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
**What your numbers show**
Day 0 is today. You have €1,900. Coming out: €2,400 repair + €1,200 wages = €3,600. Coming in: €1,500 wedding deposit on day 5. So even with the full deposit you are about €200 short before any sales, and the timing is worse than the total: the money goes out on days 0–4 and the wedding money lands on day 5.

**Biggest risk**
Your permit. 72 hours from yesterday ends about the same day as the repair slot, so there is no slack. If the repair slips by hours, you are suspended. Second risk: after the €1,000 deposit you have €900, and if the €1,400 balance is due on completion you are at –€500 on day 2.

**Today**
1. Call the inspector first (15 minutes). Ask: does a paid booking with repair on the last day meet the deadline? When is the re-inspection? Can you keep trading with a borrowed or rented cold unit, or ice-packed boxes and a probe thermometer? What should you do with the stock? Get the answers in writing.
2. Pay the €1,000 deposit today, unless the inspector call or one or two quick calls to other repairers give you an earlier or cheaper fix. It is the only confirmed route to the deadline you have. Keep the receipt.
3. Move the €600 of stock into a working fridge today (a friend's, a restaurant's, a rental). Do not sell anything you are unsure about.
4. Ask, today: the wedding client, whether the deposit can come 3 days early; the repairer, whether the €1,400 can be split or paid after day 5. Asking costs nothing.

**This week**
- Day 2: repair done. Log the temperature twice a day and send the readings to the inspector.
- Day 3: check your balance. If wages on day 4 won't be covered, tell your part-timers that day and ask whether day 5 works. Check what your contract and local rules allow.
- Day 5: wedding deposit lands.

**This month**
Build a cushion of roughly one payroll plus a small repair (about €2,000). Check whether your insurance covers breakdown or spoiled stock. What gets paid first is your call.

**Two forecasts**
If nothing changes (no deposit, no repair): the permit is suspended from about day 2. Cash goes €1,900 → €700 after wages → about €2,200 on day 5 on paper. But no sales, the €600 stock is likely lost, and the wedding job and its deposit are at risk. The €2,400 repair still comes later. Each lost trading day costs you your normal takings, which I don't know.

If the plan works: day 0 €900; day 2 –€500 (balance paid); day 4 –€1,700 (wages); day 5 –€200 (wedding deposit in). Every €100 net you sell on days 3–5 improves this by €100, so about €200 closes it. If the wedding client pays early, day 2 is +€1,000 and day 4 is –€200. Assumptions: the balance is due on completion, the wedding deposit is the full €1,500 and arrives on time, and fuel and restocking are not included, so the real figures are lower. A short bridge (overdraft or a loan from someone you trust) of €500–€1,700 for a few days is the fallback.

**Watch**
Tomorrow morning: the inspector's written answer and the repairer's confirmed slot. Day 2 evening: fridge at 4°C or below. Day 4 morning: balance against €1,200. Day 5: wedding money received.

Two questions that could change this: what does a normal trading day net you, and is the €1,400 due on completion?

=== RESPONSE 2 ===
Today: pay the €1,000 deposit and get the slot (day and hour) confirmed in writing. It is the only way to meet the 72 hours. Until then nothing that must stay cold goes to customers; move the €600 of stock to borrowed cold storage or ice boxes at 4°C or below, and bin anything warm for hours.

The greatest danger is the repair day, in two days. Your 72 hours end about then, with no spare time, and the €1,400 balance probably falls due when you will have about €900 after the deposit. Wages of €1,200 follow in 4 days, the wedding money in 5. You pay €3,600 and receive €3,400, so you stay about €200 short even after the wedding deposit, before wedding ingredients. Cash for the next four days of payments is my proposed red line; you are already below it.

Close the gap today:
- Call the inspector: repair booked, ask for re-inspection after it, reply by email.
- Ask the repairer to take the €1,400 after the wedding money arrives.
- Ask the wedding client to pay the deposit early, even in part.
- If still short, agree with your two part-timers: €900 in 4 days, €300 in 5.

Protected to the last: the permit (without it nothing earns), then your part-timers, then the wedding job. This order is my proposal; tell me if yours differs.

Not today: no high-interest loan, no new stock, no cancelling the wedding.

If nothing changes, the permit is suspended in two days. If the plan works, the fridge is fixed then and you are about €200 short until sales.

Check tomorrow at 12:00.

Questions: Is the balance due on repair day? What hour was the inspection, and what hour is the slot?

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


========== PAKAS BEIGAS ==========


========== PAKA 3/10: T03_C-v1.0-r2_vs_A-r2_21.md ==========

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

=== RESPONSE 1 ===
The biggest problem is that your goals don't add up as a set. The price cut (3) works directly against more revenue (2) and a 25% margin (4), and the three expansion goals (5, 6, 7) add costs with no stated way to pay for them. Here's the list, most important first.

I worked from your numbers. You make €2,500 a month now (a 13.9% margin), fixed costs are about €11,900, and each member brings in about €120 after their own €30 of variable cost.

**1. The 20% price cut probably turns you from profit into loss.**
At €120 a member, 120 members bring in €14,400, which is less than your €15,500 costs. That moves you from +€2,500 to about −€1,100 a month (margin −7.6%). You'd need 150 members just to match today's revenue and 160 to make today's profit. For a 25% margin at the lower price you'd need about 199 members, 66% more than now, before any new costs. Without the cut, about 145 would do it. Put differently, the cut costs you €3,600 a month, which is what you'd lose if 30 of your 120 members left. It only pays if the new studio would otherwise take more than a quarter of your members, and the plan gives no evidence of that. It also goes to every current member, including the ones who weren't leaving.

**2. The app, two teachers and a second room add fixed costs with no figures attached.**
Each one is a monthly cost on a business with €2,500 a month of slack, and you want the margin to rise at the same time. At the lower price, every extra €1,000 a month of fixed cost needs about 17 more members to still reach 25%. The plan doesn't say what these cost, when they start, or where the members to pay for them come from. If the costs arrive before the members, your margin falls during the year instead of rising.

**3. Nothing ties the new room and the teachers to demand.**
You don't say whether the current room is full. If it isn't, a second room is premature. If it is, growth is blocked until the room exists, and that changes the order of everything. Hiring two teachers before the members exist means paying for idle capacity.

**4. The tax arrears are your only hard obligation and your vaguest goal.**
"Sometime this year" gives no date, and in a plan for next year it's unclear which year you mean. €9,000 is 3.6 months of your entire current profit, or €750 a month over a year. With the price cut there would be no profit to pay it from. Arrears usually keep adding interest or penalties, so this belongs above the app and the second room, not ninth on the list.

**5. "Work less myself" conflicts with almost everything else.**
More members, a new app, a new room and two new hires all take your time first, especially in the early months. The plan doesn't say what you stop doing or who takes it over.

**6. Several goals can't be checked in December.**
"More members", "higher revenue" and "better reviews" have no number and no starting point. "Fewer than 3 complaints a month" is a raw count, so it gets harder as members and teachers grow, and you don't say what it is today. "Margin 25% by December" could mean the December month or the year's average, which are very different targets.

**7. One thing I can't tell from your numbers is whether your own pay is inside the €15,500.**
If it isn't, your real margin is lower than 13.9% and every figure above is optimistic.

The unknowns that would change this picture most are how full the room is today, what the app, teachers and room would cost, and how many members you'd lose to the new studio if you didn't cut prices.

=== RESPONSE 2 ===
The weak spot that matters most is the 20% price cut. At your numbers it turns a €2,500 monthly profit (14% of revenue) into a €1,100 monthly loss, and it works against three of your other goals.

## The weak spots, most important first

**1. The price cut cancels the margin, revenue and tax goals.** Each member brings you about €120 after their own costs (€150 minus about €30). At a price of €120, each brings €90. Assuming the cut applies to everyone and the fixed costs (about €11,900 a month) stay the same:

- Break-even needs 133 members, 13 more.
- Today's €2,500 profit needs 160 members, 40 more.
- Revenue returns to €18,000 only at 150 members.
- A 25% margin in December needs 199 members, 79 more. Without the cut it needs 145, or €2,000 a month less in costs at today's 120.

A 10% error in my split of your costs moves break-even by less than one member, so this holds. If the cut were for new members only, the damage is smaller. A price is also much harder to raise than to lower.

**2. The expansions raise fixed costs before the members arrive.** Two teachers, a second room and an app each add a monthly cost you haven't given me. Every extra €1,000 a month needs 9 more members at today's price, or 12 at the cut price, just to stand still. The costs start on day one; the members come slowly, and a new room usually loses money at first. Your whole cushion is €2,500 a month, so one mid-size cost can use it up.

**3. The tax arrears have no date.** €9,000 "sometime this year" is a wish, and it is a legal obligation, not a goal you can drop when money gets tight. Spread over 12 months it is €750 a month, 30% of today's profit; with the price cut there is no profit to pay it from. Interest and penalties usually keep growing, and in most places the tax office can eventually take money straight from your account. Asking for a written instalment plan now is much easier than after they act.

**4. Too many goals, and some are methods.** Eleven split your attention; three to five are usually enough for a year. The price cut, the app, the hiring and the second room are ways to get something, not results. "More members" and "higher revenue" overlap (revenue is members times price), and the price cut pushes them in opposite directions. The results left are about five: members, the 25% margin, the arrears, complaints, your own hours.

**5. Most goals have no number or date.** Only the 25% margin and "fewer than 3 complaints" have a number, and I don't know today's complaint count. "More members", "higher revenue", "work less" and "better reviews" stay wishes until each has a number, a unit and a date: for example, members from 120 to what, by when?

## Smaller points

- Work less conflicts with your plan: hiring and training two teachers, opening a room and launching an app all cost your hours first.
- Complaints and reviews share one cause, service quality, and both are at risk when you add teachers and a room fast.

## What I need from you

Some of your goals can't all be met: the price cut against the margin, the revenue and the arrears; and working less against the expansions. If circumstances forced you to drop goals one by one, which would go first and which last? Tell me, and I will read the numbers in your order.

Three checks to do first:

- This week: ask the tax office for an instalment plan, and tell me how much cash you hold today, since that sets your room for everything else.
- This month: count how many members left for the new studio in the last three months and ask them why, before you touch the price.
- Before committing: get the real monthly cost of each teacher, the room and the app, and how many members your current room can hold.

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


========== PAKAS BEIGAS ==========


========== PAKA 4/10: T04_C-v1.0-r5_vs_B-r2_21.md ==========

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

=== RESPONSE 1 ===
## What your numbers show

I assumed your figures are what clients paid you, before costs and tax.

- Your average is **€6,500 a month**. The three months ranged from €6,100 to €6,900, so a swing of about ±€400 is normal for you.
- Your biggest client is about **€3,575 a month** (55%). The second is about **€975** (15%). Everyone else adds up to about **€1,950** (30%).
- Without the second client you are at about **€5,525 a month**. The biggest client then becomes about **65%** of your income, so this loss makes the dependence worse.
- To reach €10,000 you need about **€4,475 a month of new work** on top of that. If your biggest client stays the same size, €10,000 puts them at 36% of income. Your two goals are really one goal.

## Biggest risk

The biggest risk is the client at 55%, not the one leaving. If they went too, you would have about €1,950 a month, which probably doesn't cover you and your employee. Your second client's reason (an in-house AI tool) could apply to the biggest one as well. I don't know that it does, but it is worth finding out calmly and soon.

## What to do

**Today**
- Ask the leaving client for the exact date their work stops, in writing. Also ask whether they will want a human to check and correct the AI's output.
- Write down your monthly costs, including your employee. That is your break-even number.

**This week**
- List every client from the last 12 months with € per client and the date of their last job. Former clients are the cheapest to win back.
- Have a normal check-in with your biggest client. Ask about their plans for the next 12 months, and whether a fixed monthly volume agreement would suit them.
- Message about 10 former or possible clients, and agencies that subcontract.

**This month**
- Pick one or two kinds of work where clients still pay for a human, and that you really do. Examples are legal or certified, medical, marketing, or rare language pairs. Offer those, plus checking and editing of AI output.
- Aim for about 20 conversations and 2–3 new regular clients. I assumed each is worth €500–1,000 a month.
- Decide what happens to your employee's workload if volume drops.

The order is your call. If you would rather protect the biggest client first, or chase new work first, that is a valid choice.

## Two forecasts

Assumptions: the leaving client's work ends in 1–2 months, and the market stays as it is. "Nothing changes" means no new clients. Its low end assumes you lose another 10% of small clients to AI.

| | Month 2 | Month 6 | Month 12 |
|---|---|---|---|
| **Nothing changes** | €6,000–6,500 | €5,300–5,700 | €4,900–5,600 |
| **Plan works** | €6,000–6,500 | €6,500–7,500 | €8,500–10,500 |

In the "plan works" case, €10,000 is the top of the range, not the middle. If the biggest client holds at €3,575, their share at month 12 would be about 34–42%. If they left, you would be at about €1,950 or less.

## What to watch, and when to check again

- **Monthly:** income per client, the biggest client's share (aim for under 40% by month 12), and their volume. A drop of more than 20% from their usual is a warning.
- **Weekly:** how many new-client conversations you had.
- **Check again** at the end of this month, when the stop date and your costs are clear. Check again at month 3. If you are below €6,000 with no new regular client, rethink the plan, including costs.

## Round 1 questions

Short answers are fine. Questions 1 and 3 could change the plan most.

1. What are your monthly costs, including your employee, and what do you need to take home?
2. What exactly did the second client say? Do you know their stop date, and did they mention checking AI output?
3. How long has the biggest client been with you? Is there a contract or notice period, and have they hinted at AI?
4. For the other 30%, how many clients is that, and what is a typical monthly size?

Round 2 will cover your language pairs and specialisms, your free hours, and your rates.

=== RESPONSE 2 ===
I'm sorry about the second client. You heard it early, and you have a year to respond.

**What your numbers already show**

Your three-month average is €6,500, and it has been steady (€6,100 to €6,900). Of that, your biggest client is about €3,600 a month, the second about €1,000, and all other clients together about €1,950.

Once the second client is gone and nothing replaces it, you are at about €5,500 a month (€5,200 to €5,800 with your usual swings), and the biggest client becomes about 65% of your income. Getting from there to €10,000 means +€4,500, roughly 80% more: income would have to grow by about €375 every month for twelve months. I cannot promise that figure. After your answers I will give you a range and say what it depends on.

I am assuming your monthly figures are invoiced amounts before costs, and that the 55% and 15% are shares of the three-month average. If either share is off by 10%, nothing here changes in substance.

**What is most dangerous**

The biggest client leaving or cutting volume, possibly for the same reason the second one did. You would then be left with about €1,950 a month, against costs I cannot see yet, including your employee. I have no date for this and no cash figure to absorb it, so I treat your cash cushion as unknown, not as safe. Both come up in the questions.

I propose two red lines (mine, change them if you like): no client above half of your income, and cash for less than one month of costs. You are already past the first one, at 55%. That makes it your starting position, not a warning. Until it is fixed, spending on growth (hires, subscriptions, ads) waits, and the first job is a second solid client.

**What I think you give up last**

My proposal, from your words: the agency keeps paying its bills and its people; then spreading your income over several clients; and the first thing to stretch is €10,000 and the 12-month deadline. If your order is different, tell me, because then the plan would chase volume rather than spread, and the single-client risk would stay. For month 12 I would aim at no client above about a third of income. At €10,000, your biggest client at today's size would still be 36%, so independence is the harder goal.

**One safe step this week**

It costs nothing and can be undone. Write to the departing client and ask for the exact last working date, whether they would still pay a human to check and polish the AI output (post-editing is a paid service of its own), and whether they know someone who still needs translators. Then find the notice period in your contract with the biggest client, if you have one. Do not sign anything long or hire anyone until the answers are in.

**My questions, round one**

Rough numbers are fine.

1. How much is in your account today?
2. What leaves each month: your employee's pay (the full cost to you), your own pay, rent, tools?
3. When does the second client's work stop, and does the contract have a notice period or minimum volume?
4. What do you translate for the biggest client, for how long, under what contract, and have they said anything about AI tools?
5. How many other clients make up the rest, and do they order every month or once?

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


========== PAKAS BEIGAS ==========


========== PAKA 5/10: T05_C-v1.0-r3_vs_A-r3_21.md ==========

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

=== RESPONSE 1 ===
**Short version:** you're covering costs but with almost no cushion, and you're paid very little for 60-hour weeks. No-shows are the biggest fixable leak.

**Where you stand**
- **Profit:** €300 a month left after paying yourself €1,800. That's about 4% of revenue.
- **Reserve:** €2,500 covers about 11 days of total costs, or roughly 2 weeks if you skip your own pay. A slow month, a broken dryer or a sick week would use most of it.
- **Your pay:** about 260 hours a month works out to roughly €7 an hour. That's well below what you'd earn employed elsewhere.
- **No-shows:** if 20% of booked slots go empty, that's up to about €1,800 a month of lost revenue (€7,200 ÷ 0.8 = €9,000 booked). Halving no-shows to 10% would add about €900 a month, three times your current profit. That's an upper estimate. It assumes the freed slots would be filled by clients who show up, and supplies cost a little more.

**This week, in order**
1. **Set a no-show rule today.** Take a card on file or a small deposit (€10–15, or 30–50% of the price) and charge a fee for cancellations under 24 hours. Put it in the booking confirmation so clients agree to it in advance. Most booking tools can do this.
2. **Turn on automatic reminders** at 48 and 24 hours, with a one-tap confirm or cancel link. When someone cancels, message a short waitlist of 5–10 regulars to fill the slot.
3. **Check your last 3 months of no-shows by name.** A few repeat clients often cause most of them. Require full prepayment from those clients, or stop booking them.
4. **Pick a price rise for next month.** Even 5% is about €360 a month, which is more than your whole current profit. Announce it with 2–3 weeks' notice.

**Two checks that could make this picture worse**
- Is the €7,200 before or after VAT? And is the €1,800 before or after tax and social contributions?
- Of your 60 hours, how many are actual grooming, and how many are admin, phone calls and waiting for people who don't show?

**Targets:** get no-shows under 10% within 6–8 weeks. Put the first extra €500 a month into the reserve until it reaches about one month of costs (€6,900). Leave your groomer's hours alone for now, and revisit them once you see what the no-show fix does.

===TURN2===
Fair enough. I'll take your numbers as given, with the €7,200 net of VAT and your €1,800 as real take-home.

**Where you stand:** you're barely profitable and one bad month from trouble. You make €300 a month on top of your pay, your reserve covers about 11 days of costs, and you earn roughly €7 an hour.

**What to do:** fix no-shows first, then raise prices.

1. **This week:** require a card on file or a €10-15 deposit for every booking, with a fee for cancellations under 24 hours. Turn on automatic reminders at 48 and 24 hours. Tell clients the rule in the booking confirmation.
2. **Also this week:** announce a 5% price rise starting next month, with 2-3 weeks' notice.
3. **In 8 weeks:** if no-shows are still above 10%, require full prepayment for everyone.

**What it's worth:** halving no-shows adds about €900 a month, and the price rise adds about €400. That takes your profit from €300 to roughly €1,500 a month. If only half of it works, you still reach about €1,000, over three times today's figure.

Put the first extra €500 a month into your reserve until it reaches €6,900, which is one month of costs. Don't change your groomer's hours until you've seen the results.

=== RESPONSE 2 ===
**Where you stand**

The salon makes €300 a month (€7,200 minus €6,900, about 4%) after paying you €1,800. The reserve of €2,500 covers about 11 days of expenses. Over roughly 260 hours a month (60 a week, at 4.3 weeks per month), your pay is about €7 an hour.

No-shows are the biggest hole. I am assuming the €7,200 comes from appointments that took place and the missed slots stay empty. Then the booked work was worth about €9,000, and 20% no-shows cost about €1,800 a month. If you refill some slots, the loss is smaller. The picture holds if any number here is off by 10%.

**The greatest danger**

One weak month. A 10% revenue drop (€720: a quiet January, flu, a sick week of yours) turns €300 profit into a loss of about €420, paid from a thin reserve. I propose a red line at one month of expenses, €6,900. You are below it, and at €300 a month you would need about 15 months to cross back. It will not fix itself, so recovery comes first.

**What to do**

- By Friday 16 October, you or your groomer: message everyone booked in the next seven days and ask them to confirm. Switch on automatic reminders 48 and 24 hours before each visit. Offer unconfirmed slots to a short waiting list.
- By Sunday 18 October: a written rule, stated at booking. New clients and anyone who has missed before leave a deposit (say €10–15, an illustration), deducted from the bill and kept if they cancel with under 24 hours' notice.
- By 16 November: count the last two months' no-shows by client and review prices. As an illustration, a 5% rise is worth about €360 a month if nobody leaves.

**What we protect first**

My proposed order, last to give up first: the salon paying its bills on time, with the reserve back at €6,900 (now €2,500, below the red line); your €1,800 pay (met); your groomer's hours (met); your own time (60 hours a week now). If your order differs, tell me. If your time comes before your pay, I would lean on prices and fewer hours rather than on filling every slot.

**What not to do now**

No hiring, equipment, loans or discounts to win clients while the reserve is below the line. Do not cut your pay or your groomer's hours before the no-show fix has had a month.

**What to check**

Every Monday: last week's no-show share and the account balance, starting Monday 19 October. Full review Monday 16 November. Change the plan if no-shows are still above 15% then, or the reserve falls below €2,000.

**Two forecasts**

If nothing changes: profit stays near €300 a month, the reserve reaches about €4,300 by April 2027, still below the red line, and one weak month erases more than two months of profit.

If the plan works: no-shows fall from 20% to 10–14% over about two months (I plan on the 14% end as a cushion), adding €540–900 a month, so profit of €840–1,200. The reserve returns to €6,900 in about 5 to 7 months, between March and May 2027. The worst end is a smaller gain, later, if deposits drive clients away.

Questions:
1. When a client no-shows, does the slot stay empty, or do you refill some?
2. Do you already send reminders or take deposits?
3. When did you last raise prices?

===TURN2===
**Where you stand**

The salon earns €300 a month after paying you €1,800. The reserve of €2,500 covers about 11 days of expenses, and your pay is about €7 an hour for 60-hour weeks. No-shows are the biggest hole: about €1,800 of work a month, assuming the €7,200 comes from appointments that took place and missed slots stay empty. That is the riskiest assumption: if you refill half those slots, the loss is about €900 and every gain below roughly halves.

The danger is one weak month. A 10% revenue drop (€720) turns €300 profit into a loss of about €420. My proposed red line is one month of expenses, €6,900. You are below it, and at today's profit you would need about 15 months to cross back.

**What to do**

- By Friday 16 October: you or your groomer message this week's clients to confirm, switch on reminders 48 and 24 hours before each visit, and give unconfirmed slots to a waiting list.
- By Sunday 18 October: a written rule at booking. New clients and past no-shows leave a deposit (say €10–15, an illustration), deducted from the bill and kept if they cancel under 24 hours before.
- By 16 November: count the last two months' no-shows by client and review prices. A 5% rise would add about €360 a month, if nobody leaves.

**Protect, avoid, watch**

Protect, last to give up first (my proposal): the salon paying its bills with the reserve back at €6,900; your €1,800 pay; your groomer's hours; your own time. Not now: hiring, equipment, loans, discounts, or cuts to your pay or groomer's hours before the fix has had a month.

Every Monday from 19 October: last week's no-show share and the bank balance. Change the plan if no-shows are still above 15% at the next review, or the reserve falls below €2,000.

If nothing changes: profit near €300, reserve about €4,300 by April 2027, still below the red line. If the plan works: no-shows fall from 20% to 10–14% in about two months (planning on 14% as a cushion), adding €540–900 a month, profit €840–1,200, reserve back at €6,900 in about 5 to 7 months, between March and May 2027. The worst end is a smaller gain, later, if deposits drive clients away.

Next review: Monday 16 November.

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


========== PAKAS BEIGAS ==========


========== PAKA 6/10: T06_C-v1.0-r6_vs_B-r3_21.md ==========

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

=== RESPONSE 1 ===
**What your numbers show**

I can't give you an exact profit or a guaranteed payback, because both depend on what the second salon sells, and nobody knows that yet. Here is the range, with my assumptions.

- Salon 1 today: €11,000 − €8,800 = €2,200 left over after your own €2,000 pay.
- Salon 2 known costs: rent €1,800 + two technicians €3,200 = €5,000 a month. I added about €800 for supplies, utilities, insurance, card fees and marketing, so about €5,800. I assumed €1,600 is the full cost per technician (if employer taxes come on top, add €600–1,000) and no extra pay for you.
- Break-even: salon 2 must sell about €5,800 a month, roughly €2,900 per technician, before it earns anything.
- Upfront: €28,000 against a €15,000 reserve. You are €13,000 short.

**Biggest risk**

Cash, not profit. The fit-out uses your whole reserve and still leaves a gap, and new salons usually lose money in the first months. I assumed sales start near €2,500 and rise evenly over six months. If sales stall, the losses land on salon 1's €2,200 surplus.

**Two forecasts**

- Nothing changes (one salon): about €2,200 a month left over, roughly €26,000 in 12 months. Your reserve stays at €15,000, or grows towards €41,000 if you save it all.
- Plan works: salon 2 reaches €10,000 a month, a bit below salon 1. Profit is about €4,200 a month and payback about 12 months from opening (range 10–16).
- Weaker case: it reaches €7,500 a month. Profit is about €1,700 a month and payback about 2 years. At €800 more costs a month, payback stretches to about 4 years.
- Below about €6,000 a month, it effectively never pays back.

These ignore loan costs. A €13,000 loan over five years at an assumed 8% costs about €265 a month, which lengthens every payback above.

**What to do**

- Today: take salon 1's sales per technician and compare with the €2,900 break-even.
- This week: confirm what the €1,600 covers, ask the landlord for rent-free months during fit-out and ramp-up, and get a written price for covering the €13,000 gap.
- This month: before you sign, write down a cash floor you will not go below (for example one month of salon 1 expenses, €8,800) and a date to stop or adjust. Both are your call.

**What to watch**

Check monthly, with a hard review at month 3 and month 6.
- Sales: about €4,500–5,500 by month 3, and €5,800 or more by month 5.
- Sales per technician: €2,900 or more.
- Cash balance against your floor.
- Salon 1 holding its €2,200 surplus while you are busy with the new one.

=== RESPONSE 2 ===
No honest analysis can give an exact monthly profit or a guaranteed payback: the second salon's revenue does not exist yet. What your numbers do show: it costs €5,000 a month before supplies (rent €1,800, two technicians €3,200), so it needs about €5,900 of revenue a month, a little over half your first salon's, just to stop losing money.

## What it could make

I am assuming: supplies and other costs are 15% of revenue; €1,600 is each technician's full cost to you; the salon takes six months to fill, averaging half its final revenue. Figures are before tax and loan repayments.

| Illustrative final revenue | Profit a month once full | Loss, first 6 months | Payback from opening |
|---|---|---|---|
| €6,000 (weak) | €100 | €14,700 | none in practice |
| €9,000 (middle) | €2,650 | €7,050 | about 19 months |
| €11,000 (like salon 1) | €4,350 | €1,950 | about 13 months |

Paybacks include the start-up losses. If wages exclude employer contributions or running costs reach 20%, break-even rises to about €6,300–6,800.

## The biggest risk

The fit-out: €28,000 against a €15,000 reserve. I propose a red line at one month of your first salon's costs, €8,800, so at most €6,200 of the fit-out can come from the reserve; the other €21,800 must come from elsewhere. Running losses are not the threat: your first salon leaves €2,200 a month after your own pay, nearly covering even the weak row's early losses. The danger is the day you sign the lease and order the work before that money is secured.

## What to do

- Ask the landlord for a rent-free fit-out period and a break clause after 12 months.
- Hire one technician first, the second when the first is booked out: €1,600 a month less fixed cost at the start.
- On the 1st of each month, compare revenue with €5,900; if it is still below at month 6, stop putting money in.

Protect in this order: your first salon and your income, then the reserve above €8,800; the second salon is what you give up first.

If nothing changes and revenue stays near the weak row, you never repay the €28,000; if the plan works and revenue reaches the middle row, expect about €2,650 a month from month 7.

Next check: 2 November, when funding should be settled.

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


========== PAKAS BEIGAS ==========


========== PAKA 7/10: T07_C-v1.0-r1_vs_A-r1_21.md ==========

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


========== PAKAS BEIGAS ==========


========== PAKA 8/10: T08_C-v1.0-r4_vs_B-r1_21.md ==========

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

Your profit is real, but you haven't been paid for part of it. In six months you earned about €18,000 profit, yet your bank balance fell €9,000. That is a €27,000 gap.

Unpaid invoices explain €13,000 of it (€8,000 to €21,000). Your accountant counts a sale when you invoice it; the bank only when it's paid.

The other €14,000 (about €2,300 a month) is not explained by anything you told me. It doesn't show up in profit. Typical causes: money you took out for yourself, loan repayments, VAT or tax payments, equipment, extra stock.

**Biggest risk**

Your €13,000 covers about half a month of costs (€26,000). The big customer is about €11,600 a month, if sales are roughly €29,000 (costs plus profit). Paying 60 days later can lock up as much as €23,000. Unpaid invoices have grown €13,000 so far, so they may still rise. If they slip further or leave, wages become hard to cover.

**What to do**

**Today:** List every unpaid invoice by customer, with due dates. Contact the big customer and ask for a payment date, in writing, for each overdue invoice. Ask why they slowed down; a cash problem on their side and a new approval process need different responses.

**This week:** Ask your accountant for everything that left the bank in six months that wasn't a cost. That is the €14,000 question. Decide how hard to push the big customer: firmer gets cash sooner, but they are 40% of your sales, and that trade-off is yours to weigh.

**This month:** Set terms for new work from them, for example a deposit on big jobs, or a limit on unpaid invoices before you pause new jobs. Ask your bank about an overdraft while you are profitable. Choose the cash cushion you want to reach; one month of costs is €26,000.

**Two forecasts**

Assumptions: profit stays near €3,000; the other outflows continue at about €2,300 a month; "90 days late" means they pay about 90 days after invoicing (if it's 90 days past due, it's worse).

**Nothing changes:** if the last six months repeat (about −€1,500 a month), cash is about €8,500 in 3 months, about €4,000 in 6, and near zero around month 9. Faster if the big customer slips more.

**Plan works:** you collect €5,000–€10,000 of the overdue invoices over 4–6 weeks and new work is paid in 30–45 days. Cash would be about €19,000–€25,000 in 3 months. No guarantee; it depends on the customer.

**What to watch**

Every Monday: bank balance, total unpaid, and the big customer's unpaid amount. If cash falls under €8,000, or their unpaid amount passes €15,000, act that week. Check again in 4 weeks.

One question that would change the picture: what was the €14,000? If it was one-off (equipment, a tax bill), the "nothing changes" case is milder; if it repeats, it matters as much as the customer.

=== RESPONSE 2 ===
You spotted this while there is still money to act with.

**Where you are**

Your accountant and your bank are both right: profit counts an invoice when you send it, the bank when it is paid. Six months of €3,000 profit is about €18,000, yet the bank fell €9,000, a gap of €27,000. Unpaid invoices grew €13,000, which explains about half. The other €14,000 (about €2,300 a month) left the account without being a cost: loan repayments, your own withdrawals, equipment or tax are the usual suspects. If none fits, the profit figure itself needs checking.

Your €13,000 is half a month of expenses. I propose the red line at one month (€26,000), comfortable from two. You are already below it: this is an alarm already ringing.

**The greatest danger**

The big customer. I assume your €26,000 covers all costs, so sales are about €29,000 a month and this customer about €11,600. If it paid nothing for a month, you would be about €8,600 short (the others bring roughly €17,400 against €26,000 out), and the €13,000 would be gone around the end of November. A customer stretching from 30 to 90 days may be in trouble.

**What to do**

Tomorrow, Friday 16 October:
- Phone the customer's accounts contact; get an amount and a date for the overdue invoices, confirmed by email. Aim for at least €13,000 within 30 days (that only brings you back to the red line) and cite late-payment interest, which most EU countries allow with a minimum €40 per invoice.

This week:
- Ask your accountant where the €14,000 went.
- Ask the bank for an overdraft limit now, while you are profitable.
- Until old invoices are paid, take new work from the big customer only with 50% upfront.

**What we protect first**

My proposed order, starting with what you would give up last: your three people's wages and paying rent and suppliers on time; the one-month reserve; the big customer on fair terms; the €3,000 profit. If your order differs, tell me; if this customer matters more than cash to you, I would swap the upfront rule for a firm payment plan.

**What not to do**

No new equipment, hiring, stock or discounts, and no extra withdrawals until the balance passes €26,000.

**What to measure**

Every Monday: balance in months of expenses, total unpaid invoices, and the big customer's share. First check Monday 19 October, full review Monday 16 November. No confirmed payment plan by Friday 30 October: move the customer to full prepayment. Balance below €10,000 (my proposed alarm; the worst case reaches it around December): pay only wages, rent and paper, and draw the overdraft.

**Two forecasts**

If nothing changes: the balance either stays near €13,000 (if the €21,000 unpaid is the new normal) or falls to about €3,000 by January (if the delay is still working through: a 60-day stretch ties up about €23,000 on this customer, €13,000 already stuck). Both stay under the red line, and one missed payment can finish it.

If the plan works: collecting €13,000 puts you near €26,000 by mid-November and €27,000 to €29,000 by mid-December (€3,000 profit a month, less the €2,300 that went missing if that continues).

I assume most of the €13,000 rise is this customer and the others pay on time. A 10% error in my figures does not change the conclusion.

1. How much of the €21,000 is the big customer's, and how old are the invoices?
2. What does your accountant say the €14,000 was?
3. Is there a written contract with payment terms?

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


========== PAKAS BEIGAS ==========


========== PAKA 9/10: T09_C-v1.0-r2_vs_A-r2_21.md ==========

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

=== RESPONSE 1 ===
Īsi: +30 % ar mārketingu šajā situācijā ir ļoti maz ticams, un pat ja izdotos, tavu galveno problēmu tas neatrisinātu. Paskaidroju, kāpēc, un ko es darītu tā vietā.

**Ko rāda skaitļi**

Ja pēdējais ceturksnis būs līdzīgs iepriekšējo gadu ceturkšņiem, 2026. gadā iznāks ap 33–35 tūkst. €. Apgrozījums krīt par aptuveni 10–12 % gadā jau trešo gadu, un tas ir tādā pašā mērogā kā iedzīvotāju skaita kritums. Tātad, visticamāk, trūkst nevis reklāmas, bet pircēju.

+30 % no 34 tūkst. € ir ap 44 tūkst. €, tas ir augstāk nekā 2024. gadā. Ja tendence turpinās, 2027. gadā būs ap 30–31 tūkst. €, tātad jāatrod 13–14 tūkst. € papildu apgrozījuma pilsētā, kas zaudē iedzīvotājus. Preses un loteriju pieprasījumu reklāma paceļ maz: kioska esamību cilvēki jau zina.

Svarīgāk ir tavs paša darbs. 6 000 € par ap 2 800 stundām gadā ir ap 2 € stundā jeb 500 € mēnesī pirms nodokļiem. Ja papildu 13 tūkst. € nestu 16–25 % peļņas (16 % ir tava pašreizējā marža, 25 % ir optimistisks pieņēmums), tie būtu +2–3 tūkst. € gadā, apmēram +1 € stundā. Pat sasniegts, mērķis tevi atstātu krietni zem minimālās algas. Turklāt noma un citi fiksētie izdevumi nesamazinās līdz ar apgrozījumu, tāpēc 2026. gada peļņa, visticamāk, jau ir zem 6 000 €. Pārbaudi faktisko skaitli.

**Ko likt mērķa vietā**

Ne +30 %, bet: apturēt kritumu un palielināt peļņu uz nostrādāto stundu. Ja 2027. gadā noturi ap 34 tūkst. €, tas jau ir par aptuveni 10 % labāk nekā tendence.

**Plāns līdz nomas beigām**

1. **Nākamās divas nedēļas: mērīšana.** Sadali apgrozījumu un peļņu pa kategorijām (prese, loterija, viss pārējais) un pārdošanu pa stundām un dienām. Visticamāk, atradīsies stundas (vēli vakari, svētdienas), kurās kioskā gandrīz nav pircēju. Ja 55 stundas nedēļā samazini līdz, piemēram, 45, apgrozījums var gandrīz nemainīties, bet atalgojums uz stundu pieaugs.

2. **Novembris–decembris: noturēt esošos pircējus.** Pie tik plānas peļņas atlaides ir bīstamas: 5 % atlaide pie 16 % peļņas apēd trešdaļu peļņas. Lētāk darbojas citi veidi: preses abonēšana ar piegādi mājās vecākiem cilvēkiem, vienošanās ar skolu, bibliotēku un pensionāru biedrību, ieraksti vietējā Facebook grupā. Šiem testiem pietiek ar 300–500 €.

3. **Janvāris–februāris: viens pakalpojums, kas atved cilvēkus atkārtoti.** Piemēram, pakešu izsniegšanas punkts, rēķinu maksājumi, biļešu pārdošana, izdrukas vai karstie dzērieni. Pirms ķeries klāt, noskaidro, cik tev paliek par vienu darījumu un cik darījumu dienā vajag, lai tas atmaksātos.

4. **Noma.** Līgums beidzas pēc 8 mēnešiem, un saimniekam, visticamāk, nav daudz citu nomnieku. Lūdz zemāku nomu, īsāku termiņu (6–12 mēneši), iespēju izstāties agrāk vai nomu, kas daļēji atkarīga no apgrozījuma. Līdz līguma pagarināšanai neiegulda remontos vai iekārtās.

5. **Lēmums līdz martam.** Tagad nosaki skaitļus, pēc kuriem lemsi, piemēram: ja janvārī–februārī mēneša apgrozījums ir vismaz X € un peļņa uz stundu vismaz Y €, tad turpinu; ja nē, plānoju izeju. Y nosaki tu pats: kāds ienākums tev ir pieņemams? Uzkrājums 4 000 € ir drošības spilvens izejai, nevis nauda reklāmai. Arī kioska slēgšana ir lēmums, nevis neveiksme: ap 2 € stundā nopelnošu kiosku nav jāglābj par katru cenu.

Lai plānu pārvērstu konkrētos skaitļos, uzraksti: (1) apgrozījuma sadalījumu pa preču grupām, (2) mēneša nomu un citus fiksētos izdevumus, (3) ko kiosks pārdod vai piedāvā papildus presei un loterijai, (4) vai tu gribi kiosku noturēt ilgtermiņā vai vari to arī slēgt.

=== RESPONSE 2 ===
Ar mārketingu vien +30% nākamgad nav reāls: pilsēta sarūk, un reklāma neatgriezīs aizbraukušos. Svarīgāk ir tas, ko tu no apgrozījuma dabū, un nomas beigas jūnijā. Pirmais solis: izlasi nomas līgumu un pieraksti datumu, līdz kuram jāpaziņo par pagarināšanu. Tava slodze ir smaga, un pilsētas sarukšana nav tava vaina.

**Kur tu esi**

Apgrozījums jau trīs gadus samazinās par aptuveni 12% gadā. 2026. gads iet uz aptuveni 33 000 € (25 000 ÷ 9 × 12; 10% mazāk nekā pērn), ja gada beigas nav stiprākas. Pilsēta zaudējusi ceturto daļu iedzīvotāju. +30% no šī līmeņa ir ap 43 000 € jeb 10 000 € vairāk gadā. Tava peļņa pērn bija 6 000 € par aptuveni 2 860 stundām: ap 2 € stundā jeb 500 € mēnesī. Uzkrājums 4 000 €, noma beidzas ap jūnija vidu.

**Lielākais drauds**

Nomas beigas jūnijā. Ja paraksti ilgu līgumu ar tādu pašu maksu, kamēr apgrozījums krīt par aptuveni 10% gadā, vienīgais spilvens ir uzkrājums. Ja līgums pagarinās automātiski vai prasa brīdinājumu pāris mēnešus iepriekš, termiņš var pienākt jau pavasarī. Otrs drauds ir iztērēt uzkrājumu reklāmai. Tāpēc secība: noma, darba stundas un piedāvājums, tikai tad mārketings.

**Ko darīt**

Līdz 22. oktobrim:
- Izlasi līgumu: brīdinājuma termiņš, automātiska pagarināšana, maksa.
- Sāc pierakstīt čekus pa stundām: cik klientu, cik eiro (divas nedēļas).

Līdz 15. novembrim:
- Pēc pierakstiem aizver stundas, kurās pircēju nav. Bez maksas, atceļams.
- Pajautā diviem operatoriem par komisiju: sūtījumu izsniegšana, rēķinu apmaksa, biļetes. Ņem to, kas atved cilvēkus vismaz reizi nedēļā, un izziņo vietējā Facebook grupā un pie durvīm.
- Mārketingam un jaunajiem pakalpojumiem kopā: ne vairāk par 500 € un 3 stundām nedēļā.

Līdz 15. janvārim:
- Nomas sarunas: līgums uz 1 gadu, zemāka vai no apgrozījuma atkarīga maksa, iespēja izbeigt agrāk.

**Ko pasargāt vispirms**

Šo secību piedāvāju es; ja kiosks tev svarīgāks par ienākumu, pasaki, un nomas sarunās varēsim piekāpties vairāk. Pirmais jāsargā uzkrājums un dzīve bez parādiem (sarkanā līnija 3 000 €; tagad 4 000 €, ar 500 € griestiem paliek 3 500 €). Tad tavs ienākums un veselība: vismaz 6 000 € gadā ar mazāk nekā 55 stundām nedēļā līdz 2027. gada beigām; prognoze to sasniedz tikai ar zemāku nomu. Tad pats kiosks. Apgrozījuma pieaugums atkrīt pirmais.

**Ko tagad nedarīt**

Neparaksti nomu uz ilgāk par gadu pirms sarunām, neņem kredītu, netērē virs 500 € un nepalielini stundas.

**Ko mērīt**

Katru pirmdienu: konta atlikums, čeku skaits un summa nedēļā. Katru mēnesi: apgrozījums pret to pašu mēnesi pērn. Nākamā pārbaude 2. novembrī. Ja trīs mēnešus pēc kārtas apgrozījums ir vairāk nekā 15% zem pērnā vai uzkrājums nokrīt zem 3 000 €, plānu mainām: mazākas telpas vai izbeigšana.

**Divas prognozes**

Ja nekas nemainās: 2027. gadā apgrozījums ap 30 000 € (28 000–32 000), peļņa pirms tavas algas 3 900–4 600 €, jeb 330–380 € mēnesī; sliktākajā galā ap 3 300 €.

Ja plāns darbojas: apgrozījums 33 000–36 000 € (mans vērtējums, nevis aprēķins), peļņa 4 800–5 800 € pirms mārketinga izdevumiem; katrs nomas samazinājums par 100 € mēnesī pieliek 1 200 € gadā. +30% (43 000 €) dotu 7 300–7 900 €, bet tam vajag kaut ko, kas kioskam pievieno jaunus pircējus, nevis tikai reklāmu, un to solīt nevaru.

Pieņemu: +30% rēķināju no 2026. gada (no 2025. gada tas būtu 48 100 €); katrs zaudētais apgrozījuma eiro tev atņem 20–30 centus peļņas, jo tavu uzcenojumu nezinu. Ja nē, peļņas skaitļi mainās, secinājums par nomu paliek.

Jautājumi:
1. Cik maksā noma mēnesī un ko līgums saka par pagarināšanu un brīdinājuma termiņu?
2. Cik no apgrozījuma ir prese, loterija un citas preces?

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


========== PAKAS BEIGAS ==========


========== PAKA 10/10: T10_C-v1.0-r5_vs_B-r2_21.md ==========

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

=== RESPONSE 1 ===
**Что показывают ваши цифры**
На счёте 450 €, через 6 дней аренда 1 100 €. Не хватает 650 €. Клиент должен 3 800 € (это больше трёх аренд) уже 30 дней. Кредитная линия 2 000 € под 12 % обходится примерно в 10 € в месяц с каждой взятой 1 000 €. Еда и дети закрыты зарплатой жены, это ваша страховка.

**Главный риск**
Дело не в самом долге, а в сроках: аренда наступит раньше, чем клиент заплатит. Второй риск: почти весь ваш доход завязан на одного клиента.

**Сегодня**
1. Закройте разрыв кредитной линией. Я бы снял 1 000 € (650 на аренду и около 350 запаса). Это ~10 € в месяц. Сначала проверьте комиссию за снятие и условия возврата. Сколько брать, решаете вы.
2. Позвоните клиенту, а не пишите. Лучше в бухгалтерию или менеджеру проекта, а не только тому, кто молчит. Один вопрос: «Когда будет оплата счетов на 3 800 €?» Запишите названную дату.
3. Сразу после звонка отправьте короткое письмо: номера счетов, сумма, просьба назвать дату в течение 3 рабочих дней. Поставьте в копию бухгалтерию или руководителя.
4. Найдите договор: срок оплаты, пени, право приостановить работу.

**На этой неделе**
- Нет даты к третьему дню: отправьте официальное требование (претензию) с суммой и сроком 5–7 дней. В большинстве стран ЕС за просрочку между компаниями положены законные проценты и компенсация издержек (минимум 40 € за счёт). Проверьте правила вашей страны.
- Если вы ещё работаете для этого клиента: не сдавайте новые этапы без оплаты, если договор это позволяет.
- Спросите других клиентов, можно ли получить аванс или оплату раньше.

**В этом месяце**
- Нет оплаты после срока в требовании: юрист, взыскание долга или упрощённое судопроизводство. Идти ли на это против главного клиента, решаете вы, потому что сотрудничество, скорее всего, закончится.
- В новых договорах: аванс 30–50 %, оплата за 14 дней, ни один клиент не больше половины дохода.

**Два прогноза**
Допущения: свои расходы кроме аренды ~200 € в месяц, другого дохода нет, семью покрывает жена.
- *Ничего не менять:* после аренды на счёте ~350 € при долге по линии 1 000 €. К следующей аренде (через ~5 недель) придётся снять ещё ~1 000 €, и линия будет почти исчерпана. Запас: 5–6 недель. Проценты 10–20 € в месяц.
- *План сработал (клиент платит за 2–3 недели):* на счёте около 4 000 €, после возврата линии и процентов (~10 €) остаётся ~3 000 €. Это примерно 2 месяца аренды и расходов. Если заплатит только половину (1 900 €), следующая аренда всё равно закрыта.

Это оценки, не гарантии. Когда клиент заплатит, я предсказать не могу.

**Что отслеживать**
- Через 3 дня: ответил ли клиент и назвал ли дату.
- День 6: аренда оплачена, сколько осталось на счёте.
- День 10–12: реакция на официальное требование.
- Если взято больше 1 500 € по линии, а денег от клиента нет, ищите срочный временный доход.

**Что изменит совет:** вы ещё работаете для этого клиента и в какой стране заключён договор? Если ответите, уточню шаги.

=== RESPONSE 2 ===
Сегодня: позвоните клиенту по телефону и в тот же день отправьте письменное требование не молчащему контакту, а директору или в бухгалтерию. В письме: два счёта на 3 800 €, просрочка 30 дней, оплата хотя бы одного счёта к конкретной дате через 3–4 дня, иначе новые работы приостанавливаются. Если вы в ЕС, укажите: по закону за просрочку положены пеня и от 40 € компенсации за каждый счёт.

Ситуация неприятная, но управляемая. Главная опасность: через 6 дней аренда 1 100 €, на счёте 450 €, не хватает 650 €. Необратимого пока нет; еда и дети обеспечены зарплатой жены, это защищено. Если к 4-му дню от клиента ничего нет, возьмите с кредитной линии 1 100 € и заплатите аренду; ваши 450 € останутся нетронутыми. Это около 11 € в месяц (12 % годовых). Проверьте сегодня, что линия доступна и как быстро идёт перевод.

Красная линия (моё предложение): счёт плюс остаток линии меньше одной аренды, то есть меньше 1 100 €. После этой аренды останется 1 350 € (450 + 900), выше линии, но близко. Если клиент не заплатит совсем, аренда через месяц опустит запас до 250 €, это красная зона. Я считаю, что других доходов и расходов нет; если они есть, запас длиннее.

Порядок защиты (моё предложение, поправьте): дом и спокойствие семьи, затем возможность работать; отношения с этим клиентом уступаем первыми.

Не сегодня: не расторгайте договор, не подавайте в суд, не берите с линии больше, чем нужно на аренду.

Если требование сработает, деньги реально ждать через 1–3 недели (допущение, не гарантия), и линию вы закроете. Если нет, денег хватит на две аренды.

Проверка: завтра вечером, ответил ли клиент; решение по линии: на 4-й день.

Вопросы: есть ли договор со сроками оплаты и пеней? Есть ли другие поступления в ближайший месяц?

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


========== PAKAS BEIGAS ==========
