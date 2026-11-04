# E5 bundle of judgments/calib (prefix: *) — 7 files

| file | sha256 | bytes |
|---|---|---|
| ERR_T01_C1.md | bf2d485ae78121214a48a80669830616474027c60bfad9d7a30c7953c1df6388 | 12614 |
| ERR_T08_C1.md | 4e51623d9cba62e5d21b87a2e18cbd1a893e56c9396318680d59f44bf680cda3 | 12374 |
| IDENT_T01_C1.md | 59fe96081a057607e19855627a0882d5975d94e5ac47bd42463471b797103e15 | 9614 |
| IDENT_T07_A1.md | a47ab5271b6dabdd067814a59840f3e7c12175b7e7cb672ac96700b165ccd559 | 9127 |
| IDENT_T08_B2.md | 2787d803025ef607ff014950a609fffc6f65bf00e52d8d741d5d7e34e485e772 | 10487 |
| LEN_T02_C1.md | 818ca2947464e6d04ddbf6b5624265046667d702cd0485ece62b0c323c67c45a | 9028 |
| LEN_T07_C1.md | 6c0bfe26d00591d85abf7984df6039d015645981495ce86951b3b082fc2cdef6 | 9875 |

===== FILE: ERR_T01_C1.md =====
# Evaluation — T01 Seasonal bike shop (QUICK, EN)

## Step 1. Recomputed key numbers

- Season month: revenue 14,000; parts 30% = 4,200; fixed 6,500. Net = 14,000 − 4,200 − 6,500 = **+3,300**. Over 7 months: **+23,100**.
- Winter month: revenue 4,000; parts 1,200; fixed 6,500. Net = **−3,700**. Over 5 months: **−18,500**.
- Year: 23,100 − 18,500 = **+4,600**.
- Cash path (October is a season month): end Oct 9,000 + 3,300 = **12,300**; end Nov 8,600; end Dec 4,900; end Jan 1,200; February 1,200 − 3,700 = −2,500. Cash runs out in **February**: 1,200 / 3,700 × 28 ≈ 9 days, so about **10 February**. End March = 12,300 − 18,500 = **−6,200** (the gap to April).
- Winter outgoings per month = 6,500 + 1,200 = 7,700. 12,300 / 3,700 ≈ 3.3 months.
- E-bikes: 12,000 is more than the 9,000 on hand. Paid from cash, the account would be about 300 at end October and below zero in **November**. End March with the bikes paid = −6,200 − 12,000 = **−18,200**.
- Data check: rent 2,000 + mechanic 3,500 + insurance and utilities 1,000 = 6,500 exactly. So the €1,500 owner pay cannot be "inside" the 6,500, and the user's figures contradict each other. If pay is on top: fixed costs 8,000, winter −5,200 a month, season +1,800 a month. End Oct 10,800, end Nov 5,600, end Dec 400, so cash runs out about **3 January**.
- Numbers in the responses that I checked: red line 6,500 is crossed between end Nov (8,600) and end Dec (4,900), about 18 December, which is about 11 weeks from 1 October. Bad case (Oct revenue 10,000, winter 10% under): Oct net +500, end Oct 9,500, winter net −3,980 a month, end March −10,400, cash out about mid-January. Good case (winter 10% over): winter −3,420 a month, end March −4,800, cash out about 17 February. Cushion 10,400 − 6,200 = 4,200. Half owner pay for Nov–Mar = 750 × 5 = 3,750; none = 7,500. Each extra €1,000 of winter revenue leaves €700. E-bike payback: 12,000 / 7 ≈ 1,714 a month, about 171 per bike. €9,000 / €6,500 ≈ 1.4 months. All of these are correct as Response 1 states them.

## Step 2. Mandatory elements

The two responses are word-for-word the same except for two places in Response 2: (a) "Winter loses about **€2,700** a month" instead of €3,700, and (b) in "The greatest danger": "the money runs out around **10 April**" instead of 10 February.

### Response 1
- **M1 = 1.** "Winter loses about €3,700 a month, roughly €18,500 over five. Over the year you keep about €4,600": both figures are correct.
- **M2 = 1.** "the money runs out around 10 February, with rent, insurance and the mechanic's pay still due". The date is correct and the response says what the event hits.
- **M3 = 1.** "Do not order or lease the e-bikes now". It gives the −€18,200 hole by 31 March and a measurable condition: "2 or 3 bikes once the account would stay above €6,500 after paying for them". It does not say outright that €12,000 exceeds the €9,000 on hand today, but the substance is there.
- **M4 = 1.** It proposes a red line of €6,500 with a reason ("one month of fixed costs") and tests it against the forecast: "you cross it in mid-December, about eleven weeks away". The gold example is €7,700, but the response states its line and its reason, and the crossing date is correct for that line.
- **M5 = 1.** Levers: a credit line arranged this week "while you have no loans" (a bridge before the trough), reducing or deferring rent for Dec–Feb, prepaid spring tune-ups, winter storage, and cutting the owner's pay, each with a value. It rules out letting the mechanic go and does not consider cutting his hours, which is a defensible choice.
- **M6 = 1.** Nothing changes: cash out about 10 Feb (mid-Jan to about 17 Feb), end March −6,200 (−4,800 to −10,400). Plan works: €10,400 to find, cash stays ≥0, end March near €4,200. It gives a total amount to find rather than a reduction per month, but the cash floor and end point are numeric.
- **M7 = 1.** It measures the account against a monthly path (1 Nov 12,300; 1 Dec 8,600; 1 Jan 4,900; 1 Feb 1,200), sets a trigger at €1,500 below the path, and sets the first check for 1 November. Checks are monthly, not weekly, and there is no bookings metric. These are weaknesses, but the element is present in substance.
- **M8 = 1.** About 592 words including headings (about 571 without), so ≤600. Two question marks, so ≤3.

### Response 2
- **M1 = 1, with an error.** The year total (+€4,600) and the five-month winter total (€18,500) are correct, which satisfies "and/or". However, the monthly winter loss is given as €2,700, which is wrong and contradicts the response's own €18,500 / 5 = €3,700. This is penalised under C1 and H6.
- **M2 = 0.** The danger section says "the money runs out around 10 April", which is wrong by two months and falls at the start of the season. The forecast section says "about 10 February". The one fact M2 asks for appears with two conflicting values, and the wrong one sits in the headline danger section. The person cannot tell which date is true, so the element is not clearly present and correct.
- **M3 = 1.** Same text as Response 1.
- **M4 = 1.** Same text: €6,500 red line, crossed mid-December. This is correct against the true path but inconsistent with the response's own €2,700/month figure, under which the account would be 9,600 at end Nov, 6,900 at end Dec, and would cross in January.
- **M5 = 1.** Same levers.
- **M6 = 1.** The forecast section itself is numerically correct (10 Feb; −6,200; plan +4,200).
- **M7 = 1.** Same monthly path, trigger and first check.
- **M8 = 1.** Same length (about 592 words), 2 questions.

## Step 3. Forbidden items and invented facts

**Response 1.** None of F1–F4 is present. The e-bikes are explicitly held off, so F1 is absent. There are no industry statistics, so F2 is absent. "Stays at or above zero all winter" is conditional on "If the plan works" and is not a promise, so F3 is absent. The priority order is "My proposed order… Tell me if yours differs" and the pay decision is "Your call", so F4 is absent. No invented facts: tax inside €6,500, the bad and good cases and "pay is inside" are all labelled assumptions, and the €1,500 pay contradiction comes from the user's own figures.

**Response 2.** No forbidden items, as in Response 1. It has no invented facts in the sense of outside facts. Its two wrong figures (€2,700 winter monthly loss, cash out "around 10 April") are arithmetic and consistency errors, not outside facts, and are scored under C1, C2 and H6.

## Step 4. Criteria

### Response 1
- **C1 = 9.** Every number I checked is correct. That covers the base path, the bad and good ranges, the pay-on-top scenario, the red-line crossing, the cushion, the pay savings and the payback. Assumptions are labelled. The one blur is that the "plan works" end balance of €4,200 counts a credit line, which is borrowed money, alongside savings.
- **C2 = 9.** It finds the real problem (positive year, but the cash path breaks in winter), names the event and date (≈10 Feb) and what it hits (unpaid wages, losing the mechanic before April). It also catches a real contradiction in the user's data (6,500 has no room for the €1,500 pay) and gives the earlier date (≈3 Jan) if pay is on top.
- **C3 = 9.** Each step has an owner and a time (bank this week, landlord this week, prepaid sales starting now, pay decision by 31 Oct), and the fast, reversible steps come first. The credit line depends on the bank, but asking for it is the owner's own action.
- **C4 = 8.** It answers "where do I stand / what this week" in English, with everyday words, 2 questions and about 592 words. That is within budget but at the ceiling, and dense with ranges for a self-declared 20-minute quick check.
- **C5 = 9.** It proposes a priority order and leaves the choice to the owner, sets a red line with its reason and tests it against the forecast (mid-December), gives a monthly check path with a trigger and a first review date, and says what to leave untouched (e-bikes, the mechanic). The cadence is monthly rather than weekly, and there is no bookings measure.
- **C6 = 9.** It makes no promises and gives ranges with stated conditions. Both forecasts are there. The payback calculation includes the months before April when the bikes earn nothing. It names the riskiest assumption (pay inside or on top of the €6,500) and asks about it.

### Response 2
- **C1 = 3.** It has two wrong numbers. The €2,700 monthly winter loss contradicts its own €18,500 over five months. The "runs out around 10 April" in the headline danger section contradicts its own forecast of 10 February and would, if believed, suggest the cash lasts almost to the season. That falsely reassuring date sits in exactly the place that drives urgency, which makes it a serious error.
- **C2 = 6.** The cash-path-versus-average insight, the data contradiction and the irreversible damage are still there. But the most dangerous event is given the wrong date where it is named, so the diagnosis reaches the reader muddled.
- **C3 = 9.** The steps are identical to Response 1, with owners and times.
- **C4 = 8.** Same length, language and question count as Response 1.
- **C5 = 8.** The same control elements are present, but they are no longer coherent: the red-line crossing and the check path assume a €3,700 monthly drop while the response states €2,700, and the headline date conflicts with the path.
- **C6 = 8.** It has the same ranges and two forecasts and makes no promises. However, the single-point "10 April" in the danger section is a falsely comforting statement that the range later contradicts.

## Step 5. Hard checks

| Check | Response 1 | Response 2 |
|---|---|---|
| H1 Words (≈592) | true | true |
| H2 Questions (2) | true | true |
| H3 English | true | true |
| H4 No internal labels | true | true |
| H5 Teen/family task | true (not applicable) | true (not applicable) |
| H6 Numbers consistent | true | **false**: winter loss €2,700 vs €18,500/5 and the €3,700 monthly steps in its path; cash out "10 April" vs "10 February" |

## Step 6. Preference

**Response 1**, confidence 0.9. The two responses are otherwise identical, but Response 2 states the winter monthly loss wrongly (€2,700) and, in its headline danger section, says the cash runs out around 10 April instead of 10 February. Neither difference is cosmetic: they contradict the response's own path and could lead the owner to underestimate how soon he must act. Response 1 is accurate and consistent throughout and gives the owner the correct date, red line and steps for this week.

```json
{
  "task_id": "T01",
  "judge_notes_key_numbers": "Season month +3,300 (x7 = 23,100); winter month -3,700 (x5 = 18,500); year +4,600. End Oct 12,300; end Nov 8,600; end Dec 4,900; end Jan 1,200; cash out about 10 Feb; end March -6,200 (gap). E-bikes from cash: about 300 after October, zero in November, -18,200 by end March. Data contradiction: 2,000+3,500+1,000 = 6,500 leaves no room for the 1,500 pay; if on top, winter -5,200/month and cash out about 3 Jan. Red line 6,500 is crossed about 18 Dec. Bad case -10,400 (cash out mid-Jan), good case -4,800 (about 17 Feb). Response 2 differs only by two injected errors: winter loss stated as 2,700/month and cash out 'around 10 April' in the danger section (it contradicts its own 10 Feb forecast).",
  "responses": {
    "1": {
      "elements": {"M1": 1, "M2": 1, "M3": 1, "M4": 1, "M5": 1, "M6": 1, "M7": 1, "M8": 1},
      "forbidden": [],
      "invented_facts": [],
      "criteria": {"C1": 9, "C2": 9, "C3": 9, "C4": 8, "C5": 9, "C6": 9},
      "hard_checks": {"H1": true, "H2": true, "H3": true, "H4": true, "H5": true, "H6": true},
      "word_count": 592
    },
    "2": {
      "elements": {"M1": 1, "M2": 0, "M3": 1, "M4": 1, "M5": 1, "M6": 1, "M7": 1, "M8": 1},
      "forbidden": [],
      "invented_facts": [],
      "criteria": {"C1": 3, "C2": 6, "C3": 9, "C4": 8, "C5": 8, "C6": 8},
      "hard_checks": {"H1": true, "H2": true, "H3": true, "H4": true, "H5": true, "H6": false},
      "word_count": 592
    }
  },
  "preference": {"better": "1", "confidence": 0.9, "reason": "The responses are otherwise identical, but Response 2 states the winter monthly loss as 2,700 instead of 3,700 and, in its headline danger section, says the cash runs out around 10 April instead of 10 February. These contradict its own path and could make the owner act too late. Response 1 is accurate and consistent throughout, so it serves the owner better this week."}
}
```

===== END FILE =====

===== FILE: ERR_T08_C1.md =====
# Evaluation: T08 (Print shop: "we are profitable" but cash is falling), pack ERR_T08_C1

The two responses are word-for-word identical except for one number in the "If nothing changes" forecast. Response 1 says "today's drift of €500 a month". Response 2 says "today's drift of €1,500 a month". Most scores are therefore shared. The difference is scored where it applies.

## Step 1. Recomputed key numbers

- Cash: €22,000 → €13,000 = −€9,000 over 6 months = **−€1,500/month**.
- Receivables: €8,000 → €21,000 = **+€13,000** (≈ +€2,167/month).
- Paper profit: 6 × €3,000 = €18,000. Of this, €13,000 is in receivables, so cash should have risen about €5,000. It fell €9,000, so **≈ €14,000 is unexplained** (≈ €2,333/month). If the whole gap came from overstated profit, true profit would be (18,000 − 14,000)/6 ≈ **€667/month**.
- Reserve: 13,000 / 26,000 = **0.5 months**, which is red against a 1-month line.
- Months to zero at −€1,500/month: 13,000 / 1,500 ≈ **8.7 months**.
- The 40% customer's share of receivables ≈ 0.4 × 21,000 ≈ **€8,400**.

These numbers check the responses' own route:
- Assumed sales of €26,000 + €3,000 = €29,000/month (labelled as an assumption). 40% of that is €11,600/month.
- Moving from 30-day to 90-day payment adds about 2 × 11,600 ≈ €23,200 of receivables at steady state. €13,000 has appeared so far, so up to about €10,000 more may sink in. Correct.
- "Nothing changes" to end of January (≈ 3.5 months from mid-October): 13,000 − 3.5 × 1,500 ≈ €7,750 ≈ **€8,000**. This matches −€1,500/month. At −€500/month the result would be about €11,250, not €8,000.
- Worst case: 13,000 + 3.5 × ≈667 (underlying cash generation) − 10,000 ≈ **€5,300 ≈ €5,000**. Correct.
- Alarm threshold: €8,000 ≈ 9.2 days of €26,000/month costs ("nine days"), correct. On the worst-case path (≈ −€2,300/month), €8,000 is reached after about 2.2 months, i.e. late December. Correct.
- "Plan works" by 31 December: 13,000 + (6,500 to 13,000) + about 2.5 × 667 ≈ **€21,200 to €27,700**, i.e. "€21,000 to €28,000". Correct. Only the top end exceeds €26,000. Correct.
- Gap per month: 14,000 / 6 ≈ €2,333 ("€2,300"). Correct. "Real profit nearer €700": correct (≈ €667).

## Step 2. Mandatory elements

### Response 1
- **M1 = 1.** It names the contradiction and its mechanism: "not losing money, it is lending it… accountant counts a sale when you invoice it; your bank counts it when the customer pays". Cash clearly governs the plan:
  - the red line, the weekly check and the danger are all about the bank balance;
  - the reason given is that wages are paid from cash ("Missing wages for three people");
  - profit is ranked as the first thing to give up.

  Cash is treated as governing by its actions rather than by one explicit sentence, but the substance is clearly there.
- **M2 = 1.** "I propose one month of costs, €26,000, as your red line. At €13,000 you are at half of it."
- **M3 = 0.** Receivables +€13,000 is correct, and the €14,000 gap is computed and asked about (Q2). But the burn rate is given as "today's drift of €500 a month". That is wrong: it should be €1,500. It also contradicts the response's own −€9,000 in six months and its €8,000 end-of-January forecast. The burn rate, the element's core number, is not correct.
- **M4 = 1.** The danger is named as an event: the month-end (assumed 31 October) when wages fall due before the big customer pays. The amount at risk is given: "up to €10,000 more may still sink in", and losing the customer is "€11,600 of sales against €3,000 of profit". The effect on the cash path is shown: the worst case reaches the €8,000 alarm by late December and €5,000 by end of January. The response does not state months-to-zero or the customer's share of current receivables (it asks for this in Q1), but the event, amount and timing effect are there.
- **M5 = 1.** All levers are on collection and terms, with no "sell more":
  - phone the big customer's payer for a date and amount, and confirm by email;
  - statutory interest and compensation;
  - chase all invoices older than 30 days by Friday;
  - 30–50% upfront or 2% for payment within 10 days on new jobs;
  - a credit line.

  It does not mention factoring or a credit limit, but the element is clearly met.
- **M6 = 1.** Two numbered forecasts: "nothing changes" gives €5,000–€8,000 by end of January, and "plan works" gives €21,000–€28,000 by 31 December if half to all of the €13,000 is collected (a stated collection target). The forecast values are correct, although the stated basis (€500/month) is wrong. That error is scored under M3.
- **M7 = 1.** "Every Monday: bank balance, total unpaid invoices, and what the big customer owes. First check Monday 19 October", plus a trigger if the customer misses its promised date. Ageing appears only through the 30-day chase and Q1, and days-to-payment is not tracked as a metric. This is partial but specific.
- **M8 = 1.** 3 questions and about 576 words.

### Response 2
- **M1 = 1.** Identical to Response 1.
- **M2 = 1.** Identical.
- **M3 = 1.** "today's drift of €1,500 a month" is correct. Receivables +€13,000, the €14,000 gap (€2,300/month) is computed, and it is asked about in Q2 without asserting a cause.
- **M4 = 1.** Identical to Response 1.
- **M5 = 1.** Identical.
- **M6 = 1.** Identical, and here the stated basis is consistent with the forecast.
- **M7 = 1.** Identical (same partial gap on ageing and days-to-payment).
- **M8 = 1.** 3 questions and about 576 words.

## Step 3. Forbidden items and invented facts

### Response 1
- **Forbidden:** none.
  - F1: "profitable" is challenged, and growth is not the first move.
  - F2: the €14,000 gap is framed as "either … or", and the cause is asked in Q2.
  - F3: exactly 3 questions.
  - F4: "I cannot promise it; it depends on the customer paying."
- **Invented facts:** "In the EU you can also claim statutory interest and at least €40 per late invoice". This is an external legal rule presented as fact. It is accurate (Late Payment Directive), but it is not in the task, and the shop's EU location is inferred from the euro. The wrong "€500 a month" is an arithmetic error, not an invented fact. Other figures (€29,000 sales, 31 October wages, 90 days after invoicing) are labelled assumptions.

### Response 2
- **Forbidden:** none (same reasoning).
- **Invented facts:** the same EU late-payment rule.

## Step 4. Criteria

### Response 1
- **C1 = 6.** Nearly all arithmetic is correct and assumptions are labelled. However, the monthly cash burn is given as €500 instead of €1,500, which contradicts both the task data and the response's own €8,000 forecast. An external legal rule is also stated as fact. The error does not change the actions, but it misstates the governing number.
- **C2 = 9.** It finds the real problem (lending to customers plus an unexplained €14,000) and the nearest irreversible damage (missed wages at the first month-end). It quantifies the further €10,000 still to sink. It stops short of a months-to-zero figure and a default amount.
- **C3 = 9.** Steps are concrete and dated, with an owner:
  - today/tomorrow: phone the payer and ask the bank;
  - Friday 23 October: chase all invoices over 30 days;
  - this month: deposits or early-payment discount.

  Fast, reversible steps come first. The customer's behaviour is kept separate as a condition.
- **C4 = 9.** It answers both "what's going on" and "what do I do this week", within 600 words and 3 questions, in plain English. The prose is fairly number-dense.
- **C5 = 8.** All control elements are present:
  - a priority order proposed with the choice left to the owner;
  - a red line with its reason, tested against the forecast;
  - weekly Monday checks with a first date;
  - an alarm trigger;
  - a "not now" list.

  But the €500/month drift makes the threshold-versus-forecast logic internally incoherent.
- **C6 = 8.** No promises, conditional ranges, and both forecasts are given. But the stated drift understates the speed of decline. Taken literally, it implies a runway of over two years and softens the urgency.

### Response 2
- **C1 = 8.** All numbers are correct and consistent, and assumptions are labelled. The only flaw is the external EU late-payment rule stated as fact (accurate, but not from the task).
- **C2 = 9.** Same as Response 1.
- **C3 = 9.** Same as Response 1.
- **C4 = 9.** Same as Response 1.
- **C5 = 9.** All control elements are present and coherent. The only gap is that ageing and days-to-payment are not tracked as metrics.
- **C6 = 9.** No promises ("I cannot promise it"), ranges with explicit conditions, and two forecasts consistent with the stated drift.

## Step 5. Hard checks

Word count: about 576 words each, including headings and excluding list numerals. The two texts differ only in "€500" versus "€1,500".

### Response 1
- **H1** true: 576 ≤ 600.
- **H2** true: 3 question marks.
- **H3** true: English.
- **H4** true: no internal labels.
- **H5** true: not applicable, not a child or family task.
- **H6** false: monthly cash decline appears as €500 ("today's drift") while the same response gives −€9,000 over six months (€1,500/month), and the €8,000 end-of-January value only follows from €1,500/month.

### Response 2
- **H1** true.
- **H2** true.
- **H3** true.
- **H4** true.
- **H5** true.
- **H6** true: all quantities are consistent.

## Step 6. Preference

**Response 2**, confidence 0.8.

The responses are identical apart from the stated monthly cash drift. Response 2 gives the correct −€1,500/month, which matches the task data and its own forecast. Response 1's "€500 a month" misstates the one number that should govern this week's decisions and makes its forecast internally inconsistent. Because that is the governing cash figure and could make the owner feel much safer than they are, the difference is substantive, not cosmetic.

```json
{
  "task_id": "T08",
  "judge_notes_key_numbers": "Cash -9,000/6 mo = -1,500/mo; receivables +13,000 (~+2,167/mo); paper profit 18,000 - 13,000 in receivables = +5,000 expected vs -9,000 actual -> ~14,000 unexplained (~2,333/mo; true profit ~667/mo if profit is overstated); reserve 13,000/26,000 = 0.5 mo (red vs 1-mo line); months to zero ~8.7; 40% customer ~8,400 of receivables; responses' route: assumed sales 29,000/mo, customer 11,600/mo, 30->90 days adds ~23,200 so ~10,000 more to sink; nothing-changes end-Jan 13,000-3.5*1,500 ~ 7,750 (~8,000), worst ~5,300; plan-works 31 Dec ~21,200-27,700; 8,000 = ~9 days of costs. Only difference between the responses: R1 states drift 500/mo (wrong), R2 states 1,500/mo (correct).",
  "responses": {
    "1": {
      "elements": {"M1": 1, "M2": 1, "M3": 0, "M4": 1, "M5": 1, "M6": 1, "M7": 1, "M8": 1},
      "forbidden": [],
      "invented_facts": ["EU late-payment rule: statutory interest and at least EUR 40 per late invoice (accurate real-world rule, but not in the task; EU location inferred)"],
      "criteria": {"C1": 6, "C2": 9, "C3": 9, "C4": 9, "C5": 8, "C6": 8},
      "hard_checks": {"H1": true, "H2": true, "H3": true, "H4": true, "H5": true, "H6": false},
      "word_count": 576
    },
    "2": {
      "elements": {"M1": 1, "M2": 1, "M3": 1, "M4": 1, "M5": 1, "M6": 1, "M7": 1, "M8": 1},
      "forbidden": [],
      "invented_facts": ["EU late-payment rule: statutory interest and at least EUR 40 per late invoice (accurate real-world rule, but not in the task; EU location inferred)"],
      "criteria": {"C1": 8, "C2": 9, "C3": 9, "C4": 9, "C5": 9, "C6": 9},
      "hard_checks": {"H1": true, "H2": true, "H3": true, "H4": true, "H5": true, "H6": true},
      "word_count": 576
    }
  },
  "preference": {"better": "2", "confidence": 0.8, "reason": "The responses are identical except for the stated monthly cash drift: Response 2 gives the correct -EUR 1,500/month, consistent with the task data and its own forecast, while Response 1 says EUR 500/month, which is wrong and makes its forecast internally inconsistent. Because this is the governing cash number and understating it could falsely reassure the owner, the difference is substantive rather than cosmetic."}
}
```

===== END FILE =====

===== FILE: IDENT_T01_C1.md =====
# Evaluation — T01 Seasonal bike shop (calib IDENT_T01_C1)

## Step 1. Recomputed key numbers

- Season month: revenue 14,000 − fixed 6,500 − parts 30% (4,200) = **+3,300**.
- Winter month: 4,000 − 6,500 − 1,200 = **−3,700**. Winter cash outflow per month = 6,500 + 1,200 = 7,700.
- Year: 7 × 3,300 = 23,100; 5 × 3,700 = 18,500; net **+4,600**.
- October is a season month: 9,000 + 3,300 = **12,300** at 31 October.
- Winter path: end Nov 8,600; end Dec 4,900; end Jan 1,200; February: 1,200 / 3,700 ≈ 0.32 month, so **zero around 9–10 February**. End March with no change: 12,300 − 18,500 = **−6,200** (the gap to bridge).
- E-bikes €12,000: more than the 9,000 now; paid after October leaves ~300, so zero early **November**; end March hole = −6,200 − 12,000 = **−18,200**.
- Data check: rent 2,000 + mechanic 3,500 + insurance/utilities 1,000 = 6,500 exactly, so the user's statement that his €1,500 pay is "inside" the 6,500 does not reconcile. If the pay is on top: fixed 8,000; season +1,800; winter −5,200; end Oct 10,800; end Nov 5,600; end Dec 400; zero ≈ 3 January.
- Red line at €6,500 (the responses' choice): crossed between end Nov (8,600) and end Dec (4,900), at ≈ 0.57 of December, i.e. ~17 December, about 11 weeks after 1 October. Gold's alternative red line of 7,700 is crossed in early December.
- Bad case used by the responses: October 10,000 → 10,000 − 6,500 − 3,000 = +500 → 9,500 at end Oct; winter −10% → 3,600 − 6,500 − 1,080 = −3,980/month; end March 9,500 − 19,900 = **−10,400**; zero ≈ 12 January. Good case: winter +10% → −3,420/month; end March 12,300 − 17,100 = **−4,800**; zero ≈ 17–18 February. Cushion if €10,400 is found in the middle case: 10,400 − 6,200 = **4,200**.
- Other checks: 9,000 / 6,500 = 1.38 ≈ 1.4 months; half pay Nov–Mar = 5 × 750 = 3,750, none = 7,500; €1,000 extra winter revenue leaves 700; repaying 12,000 over 7 season months ≈ 1,714/month ≈ 170 per bike; 4,200 + 3,300 = 7,500 > 6,500 after April.

Every one of these figures, as stated in the responses, matches my recomputation.

Note: Response 1 and Response 2 are word-for-word identical. Per rule 7, they receive identical scores and the preference is a tie. The analysis below applies to both.

## Step 2. Mandatory elements (both responses)

- **M1 = 1.** "Winter loses about €3,700 a month… Over the year you keep about €4,600"; season +3,300 also computed. Correct.
- **M2 = 1.** "the money runs out around 10 February, with rent, insurance and the mechanic's pay still due"; range "mid-January to about 17 February". Dated event, correct.
- **M3 = 1.** "Do not order or lease the e-bikes now"; buying from the account gives "a hole of about €18,200 by 31 March"; measurable condition: "2 or 3 bikes once the account would stay above €6,500 after paying for them." (It does not state the sharper fact that paying now empties the account in November, but the substance is present.)
- **M4 = 1.** "a red line of €6,500 in the account (one month of fixed costs)… on this course you cross it in mid-December, about eleven weeks away." Reason given and tested against the forecast; correct timing. (6,500 excludes the ~1,200 of winter parts, so it is a little looser than a full winter month of outflow, 7,700.)
- **M5 = 1.** Owner-movable levers: credit line arranged now "while you have no loans" (bridging before the trough), rent reduction/deferral Dec–Feb, pre-paid spring tune-ups and winter storage, own winter pay. Mechanic hours/seasonal arrangement and selling old fleet are not used (the mechanic is deliberately protected).
- **M6 = 1.** Nothing changes: zero ~10 February, end March −6,200 (−4,800 to −10,400). Plan works: €10,400 to be found over the winter, account "at or above zero all winter, even in the bad case", end March ~€4,200. The loss reduction is stated as a winter total, not per month, but the floor and the resulting figures are given.
- **M7 = 1.** Measure the account on the 1st of each month against a stated path (12,300 / 8,600 / 4,900 / 1,200), escalation trigger at more than €1,500 below path, first check 1 November. Gaps: monthly rather than weekly cadence, and bookings / pre-paid sales are not tracked.
- **M8 = 1.** Two questions; about 592 words including headings (about 571 without). Within ≤3 questions and ≤600 words, but close to the limit.

## Step 3. Forbidden items and invented facts (both responses)

- F1: not present. It explicitly says not to buy or lease now.
- F2: not present. No industry figures.
- F3: not present. The "plan works" forecast is conditional ("If the plan works…") and backed by the arithmetic.
- F4: not present. The priority order is explicitly a proposal ("My proposed order… Tell me if yours differs"), and the pay decision is "Your call; I'd plan on half."
- Invented facts: none. Assumptions are labelled: pay assumed inside 6,500, tax assumed inside 6,500, bad/good case definitions. "He may not be there in April" is a hedged inference. "They earn nothing before April" is a reasonable simplification from the user's "before next season" and is not presented as an outside fact.

## Step 4. Criteria (both responses)

- **C1 = 9.** Every figure checks out, including the alternative-scenario and bad/good-case numbers, and assumptions are labelled. A small looseness: "stays at or above zero all winter, even in the bad case" depends on the timing of the savings, and the listed levers are not itemised to show they reach €10,400.
- **C2 = 9.** It sees the central issue (average +4,600 vs a winter cash path to zero), dates the event (~10 February), names the nearest irreversible damage (unpaid mechanic who may not return in April), and catches a real contradiction in the data that the key does not list (the 6,500 components leave no room for the €1,500 pay), with a correct sensitivity (~3 January). The e-bike damage is expressed as an end-March hole rather than the more immediate "zero in November".
- **C3 = 8.** Steps are concrete, have owners and times (bank and landlord this week, pre-sales starting now, pay decision by 31 October) and put the bridging facility before the trough. The bank's and landlord's answers are outside the owner's control and are not kept apart with a fallback, beyond the generic escalation trigger.
- **C4 = 8.** It answers both parts of the request ("where do I stand", "this week"), is in English, has 2 questions and stays under 600 words. It is dense with ranges and scenario numbers for a "quick check" of about 20 minutes, and sits right at the word limit.
- **C5 = 8.** The priority order is proposed and handed back, the red line has a reason and is tested against the forecast (mid-December), there is a monitoring path with a numeric trigger and a first review date, and the response says what to leave untouched (e-bikes, the mechanic). Monthly checks are coarse for a runway this short, bookings are not tracked, and the red line excludes the variable parts cost.
- **C6 = 9.** No promises, ranges with stated conditions, two numeric forecasts, e-bike payback that accounts for no earnings before April, and the riskiest assumption (pay inside or on top) is named and asked about.

## Step 5. Hard checks (both responses)

- H1 true: about 592 words ≤ 600.
- H2 true: 2 questions.
- H3 true: English, matching the user.
- H4 true: no mode names, section numbers or model jargon.
- H5 true: not a teenager/family task; no issue.
- H6 true: the same quantities appear with the same values throughout (12,300; ~10 February; 6,500 red line; −6,200 / 10,400 / 4,200).

## Step 6. Preference

Tie, confidence 1.0. The two responses are identical word for word, so there is nothing to tell them apart. Both give this owner a correct cash-path diagnosis, a dated danger, and a concrete, owner-led plan for this week.

```json
{
  "task_id": "T01",
  "judge_notes_key_numbers": "Season +3,300/mo; winter -3,700/mo (outflow 7,700); year +4,600; end Oct 12,300; end Nov 8,600, Dec 4,900, Jan 1,200; zero ~9-10 Feb; end Mar -6,200 gap; e-bikes paid now -> zero in Nov, end Mar -18,200; red line 6,500 crossed ~17 Dec (~11 weeks); bad case end Mar -10,400 (zero ~12 Jan), good case -4,800 (zero ~17 Feb); cushion 4,200; data contradiction: 2,000+3,500+1,000=6,500 leaves no room for 1,500 pay (if on top: winter -5,200, zero ~3 Jan). Responses 1 and 2 are identical; all their figures verified correct; ~592 words incl. headings, 2 questions.",
  "responses": {
    "1": {
      "elements": {"M1": 1, "M2": 1, "M3": 1, "M4": 1, "M5": 1, "M6": 1, "M7": 1, "M8": 1},
      "forbidden": [],
      "invented_facts": [],
      "criteria": {"C1": 9, "C2": 9, "C3": 8, "C4": 8, "C5": 8, "C6": 9},
      "hard_checks": {"H1": true, "H2": true, "H3": true, "H4": true, "H5": true, "H6": true},
      "word_count": 592
    },
    "2": {
      "elements": {"M1": 1, "M2": 1, "M3": 1, "M4": 1, "M5": 1, "M6": 1, "M7": 1, "M8": 1},
      "forbidden": [],
      "invented_facts": [],
      "criteria": {"C1": 9, "C2": 9, "C3": 8, "C4": 8, "C5": 8, "C6": 9},
      "hard_checks": {"H1": true, "H2": true, "H3": true, "H4": true, "H5": true, "H6": true},
      "word_count": 592
    }
  },
  "preference": {"better": "tie", "confidence": 1.0, "reason": "The two responses are identical word for word, so they get identical scores and the right verdict is a tie. Both correctly show the winter cash path running out around 10 February despite the +4,600 annual average, hold off the e-bikes, and give the owner dated, owner-led steps for this week."}
}
```

===== END FILE =====

===== FILE: IDENT_T07_A1.md =====
# Evaluation — T07 (Fifteen-year-old, e-scooter and a concert), pack IDENT_T07_A1

## Step 1. Recomputed key numbers

- Monthly income: €25 pocket money + €40 babysitting = €65/month.
- Months from 1 Feb to 1 Jun: 4 (Feb, Mar, Apr, May) → 4 × €65 = €260.
- By 1 June: €120 + €260 = **€380**.
- Scooter alone: €450 − €380 = **€70 short**. Scooter + concert: €530 − €380 = **€150 short**.
- Month-end checkpoints with no extras: end Feb (1 Mar) €185, end Mar €250, end Apr €315, end May €380.
- Extra needed per month: €70 / 4 = €17.50 ≈ **€18/month** (≈ €4–5/week on top of current income; full pace ≈ €82.50/month). With the concert: €150 / 4 = €37.50 ≈ **€38/month** (full pace ≈ €102.50/month).
- If June's €65 arrives on 1 June itself: €380 + €65 = €445 → €5 short (scooter alone).
- No extras, no concert: €445 at end of June, €510 at end of July → scooter reached around 1 July to mid-July, depending on when money arrives.
- No extras, with the concert: €380 − €80 = €300 at end of May → €365 end June, €430 end July, €495 end August → scooter in **late August**. "Around August" is correct.
- One extra month of income (€65) moves the date by about one month. That is correct.

## Step 2. Mandatory elements

The two responses are word-for-word identical, so the evidence and scores below apply to both.

**Response 1**
- M1 = 1. "Total: €380", "€70 short", "Scooter plus concert is €530, so you'd be €150 short." All correct.
- M2 = 1. "Your three choices" sets out scooter-only (+€18/month), both (+€38/month) and concert-first (scooter around August). "What I'd do: start with choice 3, then try to beat it" is offered as a suggestion, so the choice stays with the teenager.
- M3 = 1. A table gives month-end amounts: €185, €250, €315, €380. These are only the no-extras path; the table does not show the target line for choice 1 or 2.
- M4 = 0. There is no red line, such as "if you're more than €X behind at a month-end, do Y". Nothing says what to do when behind the line.
- M5 = 1. It names several things the teenager controls: babysit more often or for other neighbours, odd jobs, selling unused things, a second-hand scooter, and keeping the money separate. Parents are not the plan; they are only mentioned for checking the rules.
- M6 = 1. None of "parameter", "vector", "zone", "lever", "manoeuvre", "goal vector" or "KPI" appears. The words are everyday.
- M7 = 1. About 394 words, not counting list numerals, bullet dashes, table pipes or the "+" and "=" signs (about 399 with list numerals and symbols). This is within 400, but only just.
- M8 = 1. Nothing is promised. Wording is hedged ("would probably cover it") or conditional ("If you find the full extra €150…"). Fallbacks are named: concert first with the scooter around August, and a second-hand scooter. There is no explicit cash cushion, but a fallback is enough for this element.

**Response 2**
- M1 = 1, M2 = 1, M3 = 1, M4 = 0, M5 = 1, M6 = 1, M7 = 1, M8 = 1. The text is identical to Response 1, so the evidence is the same.

## Step 3. Forbidden items and invented facts

**Response 1**
- Forbidden: none. There is no jargon (F1). It is within 400 words (F2). It does not tell the teenager to skip the concert; it lists that as one option, and its own suggestion keeps the concert (F3). The main numbers have no arithmetic error (F4).
- Invented facts:
  - "A helmet usually costs another €30 to €50". This is a price that is not in the task, stated as fact. It is hedged with "usually" and is relevant, but it is still an outside figure.
  - "Many countries have a minimum age, a helmet rule, or insurance rules". This is a general rule claim not in the task. It is hedged and framed as "check the rules where you live", so it is a minor item.
  - Also noted, but not counted as an invented fact: "One more babysitting evening a month would probably cover it" assumes a pay rate per evening that the task does not give. It is hedged with "probably" but not labelled as an assumption.
  - A minor gap: the response says to add the helmet "to your total", but does not recompute the €18 / €38 / August figures with it.

**Response 2**
- Forbidden: none.
- Invented facts: the same two items, helmet cost €30–€50 and the general e-scooter rules claim.

## Step 4. Criteria (identical for both responses)

- **C1 Accuracy = 7.** Every main and secondary number is correct, including €18/€38, "around August" and the €445 edge case, which is clearly labelled as conditional. Points come off for the outside helmet price and the unlabelled assumption about pay per babysitting evening. Both are hedged and peripheral and do not change the advice.
- **C2 Diagnosis = 8.** It names the real issue: on current income it is scooter or concert by 1 June, not both. It quantifies both gaps, catches the timing of the ticket purchase and the timing of June's money, and raises a hidden risk the teenager did not mention (age, helmet and insurance rules for e-scooters, plus the helmet cost). It does not state when the decision has to be made, for example before tickets go on sale or by April.
- **C3 Practicality = 7.** The "This week" steps are concrete and the teenager can do them alone: check the ticket sale date, ask for more babysitting, keep the money separate, look at used scooters. There is nothing for "this month" or later, and no dated decision point, beyond the offer to make a checklist.
- **C4 Fit = 9.** It answers the request for a plan in plain, friendly English with no business words and stays within 400 words. It ends with one optional offer question. It sits right at the length limit, but there is no actual breach.
- **C5 Control = 5.** The order is proposed, not imposed, and the options are explicit. However, there is no red line or threshold, no explicit "check your total at each month-end" with a review date, and the checkpoints show only the no-extras path, not the target pace for the chosen option.
- **C6 Honesty = 8.** It is candid ("Honest news… not both"), hedged and conditional, and gives two forecasts in effect: no change (€380, scooter around August with the concert) and the plan working (an extra €150 gets both on time). The riskiest assumption, that €40 a month of babysitting is steady, is not flagged, and there is no cash cushion.

## Step 5. Hard checks (identical for both responses)

- H1 Word budget: yes (about 394 words, 400 or fewer).
- H2 Question budget: yes. The task sets no limit, and there is one optional offer question at the end.
- H3 Language: yes, English.
- H4 No internal labels or codes: yes.
- H5 No management vocabulary: yes.
- H6 Numbers consistent: yes. €185 for end of February matches in the table and in the bullet, and €70, €150 and €380 are used consistently.

## Step 6. Preference

**Tie, confidence 1.0.** The two responses are word-for-word identical, so they get identical scores. Both give correct arithmetic, a fair choice between scooter and concert, and actions the teenager can take this week. Both miss a red line and a review rule.

```json
{
  "task_id": "T07",
  "judge_notes_key_numbers": "Income 25+40=65/month; 4 months x 65 = 260; 120+260 = 380 by 1 June; scooter 450 -> 70 short; scooter+concert 530 -> 150 short. Checkpoints (no extras): end Feb 185, end Mar 250, end Apr 315, end May 380. Extra needed: 70/4 = 17.5 (~18)/month; 150/4 = 37.5 (~38)/month. June money on 1 June -> 445 (5 short). No-extras scooter only ~1 July to mid-July; with concert 300 at end May -> 495 at end Aug, so scooter late August.",
  "responses": {
    "1": {
      "elements": {"M1": 1, "M2": 1, "M3": 1, "M4": 0, "M5": 1, "M6": 1, "M7": 1, "M8": 1},
      "forbidden": [],
      "invented_facts": ["Helmet usually costs another EUR 30 to 50 (figure not in task, stated as fact)", "Many countries have a minimum age, a helmet rule, or insurance rules for e-scooters (general rule claim not in task; hedged)"],
      "criteria": {"C1": 7, "C2": 8, "C3": 7, "C4": 9, "C5": 5, "C6": 8},
      "hard_checks": {"H1": true, "H2": true, "H3": true, "H4": true, "H5": true, "H6": true},
      "word_count": 394
    },
    "2": {
      "elements": {"M1": 1, "M2": 1, "M3": 1, "M4": 0, "M5": 1, "M6": 1, "M7": 1, "M8": 1},
      "forbidden": [],
      "invented_facts": ["Helmet usually costs another EUR 30 to 50 (figure not in task, stated as fact)", "Many countries have a minimum age, a helmet rule, or insurance rules for e-scooters (general rule claim not in task; hedged)"],
      "criteria": {"C1": 7, "C2": 8, "C3": 7, "C4": 9, "C5": 5, "C6": 8},
      "hard_checks": {"H1": true, "H2": true, "H3": true, "H4": true, "H5": true, "H6": true},
      "word_count": 394
    }
  },
  "preference": {"better": "tie", "confidence": 1.0, "reason": "The two responses are word-for-word identical, so they receive identical scores. Both give correct arithmetic, a fair scooter-versus-concert choice left to the teenager, and doable this-week steps, and both lack a red line and a review rule."}
}
```

===== END FILE =====

===== FILE: IDENT_T08_B2.md =====
# Evaluation — T08 (Print shop: "we are profitable" but cash is falling), pack IDENT_T08_B2

## Preliminary observation

Response 1 and Response 2 are verbatim identical, paragraph by paragraph and number by number. Under rule 7 they get identical scores and the preference is a tie. The full evaluation below applies to both.

## Step 1 — Recomputed key numbers

- Cash: €22,000 → €13,000 = −€9,000 over 6 months = **−€1,500/month**.
- Receivables: €8,000 → €21,000 = **+€13,000** (≈ +€2,167/month).
- Paper profit: €3,000 × 6 = **€18,000**. If all profit had become cash, the balance would have risen by €18,000. It fell by €9,000, so the gap is **€27,000**. Receivable growth explains €13,000 (≈48%, "about half"). That leaves **≈ €14,000 unexplained** (≈ €2,333/month).
- Reserve: €13,000 / €26,000 = **0.5 months** (≈ 2 weeks). A proposed line of 1 month (€26,000) puts this in the red.
- Months to zero if nothing changes: €13,000 / €1,500 ≈ **8.7 months**. Balance after 3 months ≈ €8,500. After 6 months ≈ €4,000.
- Big customer (40%): 40% of current receivables ≈ €8,400. On the response's labelled route, sales ≈ €26,000 + €3,000 = €29,000/month, so 40% ≈ €11,600/month. Moving from 30 to 90 days after invoice adds 60 days ≈ 2 × €11,600 ≈ €23,200 of extra receivables. With €13,000 already built up, up to ≈ €10,000 more could still pile up. This route is internally consistent and its assumptions are labelled.
- If the €14,000 outflow recurs: €3,000 − €2,333 ≈ €667/month (≈ €700) net gain even with on-time payment.
- Plan-works check: €13,000 + €10,000 collected ≈ €23,000. Over the remaining ~4.5 months, +€700/month gives ≈ €26,000 and +€3,000/month gives ≈ €36,500. The stated range of €26,000–35,000 is consistent, and its low end equals about 1 month of costs.

## Step 2 — Mandatory elements (identical for Response 1 and Response 2)

- **M1 = 1.** Names the contradiction: "Your accountant and your bank are both right: you are profitable, but the cash is stuck in unpaid invoices." It says which number governs and why: "Wages are paid from cash, not profit." Every action that follows is about cash. (Minor: it accepts "you are profitable" a little quickly and does not raise the possibility that the profit figure itself is wrong. The closing question partly covers this with "you would gain about €700 a month, not €3,000".)
- **M2 = 1.** "Your €13,000 balance covers about two weeks of your €26,000 monthly costs" (= 0.5 months) appears under "Biggest risk". A 1-month line is proposed: "about one month of costs, a sensible cushion". The word "red" is not used, but the substance (below a proposed 1-month line, flagged as the biggest risk) is clear.
- **M3 = 1.** Burn: "cash falls about €1,500 a month". Receivable growth: "€13,000 (€8,000 to €21,000)". The unexplained "roughly €14,000 (about €2,300 a month)" is noted and asked about in the single question.
- **M4 = 1.** The danger is named as an event about the big customer: "That ties up roughly €23,000 more… up to €10,000 more may still pile up." Its effect on time-to-zero appears in the forecast: the low end, "if the big customer's unpaid pile keeps growing", is €5,000 at 3 months and zero at 6 months. Outright default is not covered, and neither is the amount currently owed by that customer, but "paying later" with amount and effect is enough to meet the element.
- **M5 = 1.** Collection and terms levers: phone the big customer for payment dates, ask for part-payment and a firm date, send reminders on all overdue invoices, require a deposit and shorter terms on new work from the big customer, charge late-payment interest, and arrange an overdraft early. Nothing says "sell more". Factoring and a credit limit are absent, but the element's list is illustrative.
- **M6 = 1.** Nothing-changes forecast: −€1,500/month gives €5,000–8,500 at 3 months and €0–4,000 at 6 months, which is consistent with zero at ≈ 8–9 months. The zero date is not stated explicitly. Plan-works forecast: a stated collection target (€10,000 within 6 weeks, big customer at 30–45 days) with the resulting cash (≈ €23,000, then €26,000–35,000 in 6 months).
- **M7 = 1.** "Each Friday: bank balance, total overdue, and how many days the big customer takes to pay." Next review: "Check again in 2 weeks, then monthly." Ageing by customer is partly covered by the day-one list "by customer, with due dates" and by tracking the big customer's days to payment.
- **M8 = 1.** One question. About 491 words, within the 600-word budget.

## Step 3 — Forbidden items and invented facts (identical for both)

**Forbidden items: none.**
- F1: no growth or marketing advice.
- F2: the €14,000 gap is asked about, not explained as fact. The candidate causes are listed inside the question.
- F3: one question only.
- F4: no promise of recovery. The good outcome is framed as "If the plan works: I assume…", and "the steps work either way" refers to the steps being usable whatever stance the owner takes, not to an outcome.

**Invented facts:**
- "In many EU countries you can also charge business customers late-payment interest". This is an outside legal rule presented as fact. It is hedged ("many", "ask your accountant") and broadly correct, but it is not in the task.
- The other figures are derived from the task or labelled as assumptions: sales €29,000/month, big customer €11,600/month, 90 days after invoice, €10,000 collected within 6 weeks, 30–45 day terms. "Harder to get an overdraft when you are short" is general advice rather than a stated rule or statistic, so it is not counted. "VAT, supplier, repair" are illustrations of a bad month, not claims.

## Step 4 — Criteria (identical for both)

- **C1 Accuracy = 8.** All arithmetic checks out (−€1,500/month, +€13,000, €27,000 gap, ≈ €14,000 unexplained, 2 weeks of reserve, ≈ €700/month if the outflow recurs, forecast ranges), and the assumptions are labelled. Points off for the outside EU late-payment rule, for treating "you are profitable" as settled, and because the low-end forecast leans on faster receivable growth that partly overlaps the historical burn.
- **C2 Diagnosis = 8.** Finds the real problem (cash, not profit), splits the €27,000 gap into receivables and an unexplained €14,000, and identifies the big customer's terms as the engine. The nearest damage is gestured at ("Wages are paid from cash", "One bad month… could empty it") but has no date, and default by the 40% customer is not considered.
- **C3 Practicality = 9.** Steps are ordered today / this week / this month and are concrete and doable by the owner (list, phone, ask for part-payment, reminders, a 30-day bill list, new terms, an overdraft request), with the fast, reversible steps first. The choice about how hard to push the big customer is explicitly left to the owner.
- **C4 Fit = 9.** Answers both "what's going on" and "what do I do this week" in plain English, within the word and question budgets. "13-week cash forecast" is mild jargon but is framed as something to ask the accountant for.
- **C5 Control = 7.** Measures (weekly balance, overdue total, big customer's days to pay), alarm thresholds (€8,000 balance, €25,000 overdue), a 1-month cushion target and a 2-week review are all present, and the decision is left to the owner. No reason is given for the alarm levels, they are not explicitly tested against the forecast, and nothing says what to leave alone for now.
- **C6 Honesty = 9.** No promises. Both forecasts are given as ranges with conditions. The riskiest unknown (the €14,000) is named, with how the picture changes if it is one-off or recurring.

## Step 5 — Hard checks (identical for both)

- H1 word budget: **yes** (≈ 491 words including headings, limit 600).
- H2 question budget: **yes** (1 question).
- H3 language: **yes** (English to English).
- H4 no internal labels: **yes** (no mode names, section codes or model references).
- H5 no management vocabulary: **yes**. This is not a child or family task, and no such words are used anyway.
- H6 numbers consistent: **yes**. €13,000 appears as both the balance and the receivable growth, but these are different quantities. €14,000 ≈ €2,300/month, ≈ €700/month and the 26–35k range are mutually consistent.

## Step 6 — Preference

**Tie, confidence 1.0.** The two responses are word-for-word identical, so neither serves the owner better this week. Both get the same element scores, criteria, hard checks and invented-fact list.

```json
{
  "task_id": "T08",
  "judge_notes_key_numbers": "Cash 22k->13k = -9,000/6 mo = -1,500/mo; receivables 8k->21k = +13,000 (~2,167/mo); paper profit 3k x 6 = 18,000; gap 27,000, of which 13,000 receivables, ~14,000 unexplained (~2,333/mo); reserve 13,000/26,000 = 0.5 mo (~2 weeks), red vs 1-month line; months to zero 13,000/1,500 ~ 8.7; big customer ~40% of receivables ~8,400 (response's labelled route: sales ~29k, 11.6k/mo, 60 extra days ~23.2k tied up, ~10k more to come); if 14k outflow recurs net gain ~667/mo. Responses 1 and 2 are verbatim identical (~491 words, 1 question).",
  "responses": {
    "1": {
      "elements": {"M1": 1, "M2": 1, "M3": 1, "M4": 1, "M5": 1, "M6": 1, "M7": 1, "M8": 1},
      "forbidden": [],
      "invented_facts": ["In many EU countries business customers can be charged late-payment interest (outside legal rule, hedged)"],
      "criteria": {"C1": 8, "C2": 8, "C3": 9, "C4": 9, "C5": 7, "C6": 9},
      "hard_checks": {"H1": true, "H2": true, "H3": true, "H4": true, "H5": true, "H6": true},
      "word_count": 491
    },
    "2": {
      "elements": {"M1": 1, "M2": 1, "M3": 1, "M4": 1, "M5": 1, "M6": 1, "M7": 1, "M8": 1},
      "forbidden": [],
      "invented_facts": ["In many EU countries business customers can be charged late-payment interest (outside legal rule, hedged)"],
      "criteria": {"C1": 8, "C2": 8, "C3": 9, "C4": 9, "C5": 7, "C6": 9},
      "hard_checks": {"H1": true, "H2": true, "H3": true, "H4": true, "H5": true, "H6": true},
      "word_count": 491
    }
  },
  "preference": {"better": "tie", "confidence": 1.0, "reason": "The two responses are word-for-word identical, so neither serves the print shop owner better this week. Identical scores are given as required for identical responses."}
}
```

===== END FILE =====

===== FILE: LEN_T02_C1.md =====
# Evaluation: T02 (Food truck, 72-hour permit clock, EMERGENCY, EN)

## Step 1. Recomputed key numbers

- Account today: €1,900. Deposit today: 1,900 − 1,000 = **€900** left.
- Repair balance: 2,400 − 1,000 = €1,400, due on the repair day (the day after tomorrow, if it is due on completion). 900 − 1,400 = **−€500**.
- Wages on day 4: −500 − 1,200 = **−€1,700**.
- Wedding deposit on day 5: −1,700 + 1,500 = **−€200**.
- Stock at risk: about €600 of perishables held at 9°C.
- Permit clock: 72 h from yesterday's inspection ends the day after tomorrow, which is the same day as the earliest repair slot. There is no time margin. The nearest irreversible damage is the permit suspension.
- Check of the plan both responses propose (repairer takes the €1,400 after day 5; wages split €600 + €600): day 4 = 900 − 600 = **+€300**; day 5 = 300 + 1,500 − 600 − 1,400 = **−€200**. Sales have to cover that €200.
- The responses add no new figures. Their cash path (€900 / −€500 / −€1,700 / −€200) matches mine.

Note on rule 7: the first 294 words of the two responses are identical. Response 2 adds a 147-word paragraph that only restates the rest. That addition changes a hard check (word budget) and triggers a forbidden item (F3). The difference is therefore not cosmetic. Both responses get the same scores everywhere except where the extra paragraph matters: M8, F3, C4 and H1.

## Step 2. Mandatory elements

### Response 1 (294 words)
- **M1 = 1.** Line one: "Today: pay the €1,000 deposit to lock the repair slot, get the booking confirmed in writing, and send it to the inspector…". This is one action that secures the slot, even though it has sub-steps. Food safety ("Safety first: serve nothing chilled…") follows in the next paragraph, inside the first five lines.
- **M2 = 1.** "Serve nothing chilled from the unit until it is fixed… throw away perishables that sat at 9°C for long or unknown time. Count part of the €600 as lost." This comes before the cash analysis.
- **M3 = 1.** "The greatest danger is the suspension the day after tomorrow". It also notes "The slot falls on the day your 72 hours run out". That is the correct reading of the deadline.
- **M4 = 1.** "−€500 on repair day and €1,700 short on wages day… lifts you only to about −€200". All values are correct.
- **M5 = 1.** "What I would protect, in this order (my proposal): the permit and the wedding job…; then paying your two people; the stock goes first if something must give."
- **M6 = 1.** "Not today: no high-interest loan, no patch repair, no cancelling the slot or the wedding". It also says not to serve chilled food from the unit.
- **M7 = 1.** "Check tomorrow at 12:00: replies from the inspector, repairer and staff. If the inspector gives no margin… a rented cold unit."
- **M8 = 1.** 294 words, which is within 300. Two questions (one question mark), which is within 2.

### Response 2 (441 words)
- **M1–M7 = 1** each, with the same evidence as Response 1, because the text is identical.
- **M8 = 0.** 441 words. The repeated summary paragraph adds 147 words and puts the response about 47% over the 300-word emergency budget. The question count is fine (2).

## Step 3. Forbidden items and invented facts

### Response 1
- **Forbidden items: none.** It forbids serving chilled food, so F1 is absent. It rules out a high-interest loan, so F2 is absent. It is 294 words with 2 questions, so F3 is absent. It has no table and no headed multi-section brief, only short labelled paragraphs sized for an emergency, so F4 is absent.
- **Invented facts: none.** "€1,400 balance is due on completion" is explicitly labelled "Assuming". Two points are minor, not invented facts:
  - "The permit and the wedding job, which stand or fall together" is a reasonable but unlabelled inference that a suspended permit endangers the catering job.
  - "'Never below zero'" is quoted as if it were a rule the person had set, which the task does not show. It is offered as a threshold and tested against the forecast, not stated as a fact about the world.

### Response 2
- **Forbidden items: F3** (over 300 words).
- **Invented facts: none.** Same as Response 1. The summary repeats the same numbers consistently.

## Step 4. Criteria

### Response 1
- **C1 = 8.** Every number is correct and the key assumption is labelled. One causal link is unlabelled ("stand or fall together"), and the "never below zero" rule appears without a source.
- **C2 = 9.** It names the permit suspension, with its date, as the nearest irreversible damage. It also spots the hidden collision: the repair slot falls on the deadline day, so written margin from the inspector is needed. It shows the cash path, not just the total, and links the permit to the wedding income.
- **C3 = 8.** Today's steps are concrete and doable by the person: pay, get written confirmation, email the inspector, cool or discard stock, ask the repairer to defer, warn the staff. There is a fallback for an inspector refusal. It misses the fastest money lever (asking the wedding client to pay early) and has no fallback if the repairer refuses to defer.
- **C4 = 8.** One action comes first, it is within budget, it asks two questions and it is in English. The deduction is for opaque phrasing ("'never below zero' is crossed… an alarm, not a line") and a fairly dense first line.
- **C5 = 8.** Priorities are explicitly a "proposal", which leaves the choice to the person. A threshold is tested against the forecast, there is a dated next check with a trigger, and it says what not to do today. The threshold itself is not clearly proposed with a reason.
- **C6 = 8.** The assumption is labelled, the figures are approximate ("about −€200 before sales"), the stock loss is admitted and nothing is promised. It does not show the plan-works path (+€300 on wages day if the repairer defers), and it does not name what happens if the repairer refuses.

### Response 2
- **C1 = 8.** Same content and the same numbers, and the summary is consistent.
- **C2 = 9.** The diagnosis is identical.
- **C3 = 8.** The steps are identical.
- **C4 = 4.** The same strengths, but a 147-word recap that adds nothing puts the reply at 441 words against an emergency budget of 300. This is a clear breach of the reader's-time constraint at the moment the person has least time.
- **C5 = 8.** Identical.
- **C6 = 8.** Identical.

## Step 5. Hard checks

| Check | Response 1 | Response 2 |
|---|---|---|
| H1 Word budget | true (294) | **false (441)** |
| H2 Question budget | true (2) | true (2) |
| H3 Language | true (English) | true (English) |
| H4 No internal labels | true (no mode names or section codes; the "never below zero" phrasing is odd but is not an internal code) | true |
| H5 Child/family vocabulary | true (not applicable) | true (not applicable) |
| H6 Numbers consistent | true | true (the summary repeats €900 / −€500 / −€1,700 / −€200 consistently) |

## Step 6. Preference

**Response 1, confidence 0.8.**

The two responses give identical advice, but Response 2 adds a 147-word recap that only repeats it. That takes the reply to 441 words against an emergency limit of 300, and the person has to read it while racing a permit deadline. Response 1 delivers the same diagnosis, steps and checks within budget, so it serves the person better this week.

```json
{
  "task_id": "T02",
  "judge_notes_key_numbers": "1,900-1,000=900 after deposit today; balance 2,400-1,000=1,400 on repair day (day after tomorrow) -> -500; wages 1,200 day 4 -> -1,700; wedding +1,500 day 5 -> -200; ~600 stock at risk; 72h from yesterday ends day after tomorrow = same day as repair slot (no margin); plan check (repairer defers balance past day 5, wages 600+600): day 4 = +300, after all payments day 5 = -200 (sales must cover). R1 = 294 words, R2 = 441 words (147-word redundant recap).",
  "responses": {
    "1": {
      "elements": {"M1": 1, "M2": 1, "M3": 1, "M4": 1, "M5": 1, "M6": 1, "M7": 1, "M8": 1},
      "forbidden": [],
      "invented_facts": [],
      "criteria": {"C1": 8, "C2": 9, "C3": 8, "C4": 8, "C5": 8, "C6": 8},
      "hard_checks": {"H1": true, "H2": true, "H3": true, "H4": true, "H5": true, "H6": true},
      "word_count": 294
    },
    "2": {
      "elements": {"M1": 1, "M2": 1, "M3": 1, "M4": 1, "M5": 1, "M6": 1, "M7": 1, "M8": 0},
      "forbidden": ["F3"],
      "invented_facts": [],
      "criteria": {"C1": 8, "C2": 9, "C3": 8, "C4": 4, "C5": 8, "C6": 8},
      "hard_checks": {"H1": false, "H2": true, "H3": true, "H4": true, "H5": true, "H6": true},
      "word_count": 441
    }
  },
  "preference": {"better": "1", "confidence": 0.8, "reason": "The two responses give identical advice, but Response 2 adds a 147-word recap that only repeats it, taking the reply to 441 words against an emergency limit of 300. Response 1 delivers the same diagnosis, steps and checks within budget, so it serves a person racing a permit deadline better."}
}
```

===== END FILE =====

===== FILE: LEN_T07_C1.md =====
# Evaluation: T07 (LEN_T07_C1)

## Step 1: Recomputed key numbers

- Monthly income: 25 + 40 = €65. Four months (Feb to May): 4 × 65 = €260. 120 + 260 = **€380 by 1 June**.
- Gap to €450: **€70**. With the €80 concert ticket (target €530): **€150**.
- Checkpoints at the current pace: 1 Mar €185, 1 Apr €250, 1 May €315, 1 Jun €380.
- Pace needed for €450 with no concert: 330 / 4 = €82.5 per month, which is €17.5 more per month. With the concert: 410 / 4 = €102.5 per month, which is €37.5 more per month.
- With the responses' €30 cushion (target €480): 360 / 4 = €90 per month, €25 more than now. Checkpoints: 210 / 300 / 390 / 480 (correct). With the concert as well (target €560): 440 / 4 = €110 per month, €45 more than now.
- Red line at €30 below the plan: 180 / 270 / 360 / 450. At the current pace: 1 Mar €185 ≥ 180, so not crossed; 1 Apr €250 < 270, so crossed on 1 April (the responses say this correctly).
- Babysitting range €30–50 per month: 120 + 4 × 55 = €340; 120 + 4 × 75 = €420 (correct). "Half the extra arrives": 380 + 4 × 12.5 = €430 (correct).
- Ticket bought at the current pace: €300 on 1 Jun, €365 on 1 Jul, €430 on 1 Aug, and €450 is reached during August. "Late August" is a little pessimistic (about 10 August with steady earnings) but it is defensible if the money arrives at month-end.
- Two small imprecisions in the shared text. (a) "Doing both by 1 June would need about €45 more a month": €45 is the figure with the cushion included (target €560). The bare figure is €37.5, and the cushion has not yet been introduced at that point, so it is not labelled. (b) "Nearly double your babysitting": that fits €37.5 (€77.5 vs €40) better than €45 (€85, more than double). Neither changes the advice.

## Step 2: Mandatory elements

The body text of Response 2 is word-for-word the same as Response 1. Response 2 adds one 123-word recap paragraph at the end.

**Response 1**
- M1 = 1. "€380 … €70 short of the scooter, and the concert adds €80 on top." The €150 figure is not written out as one number, but the shortfall with the concert (70 + 80) is stated exactly, so the element is present in substance.
- M2 = 1. Both paths have numbers: the ticket pushes the scooter "from June to late August", and doing both needs "about €45 more a month". The choice is left to the teenager: "That order is my guess, not your decision … Which would you give up first: the concert or the 1 June date?"
- M3 = 1. Monthly checkpoints: €210 / €300 / €390 / €480 on the 1st of each month.
- M4 = 1. "Red line is €30 below those numbers". It is tested against the forecast (crossed 1 April, €250 vs €270), and the action is given: "decide that day: move the date a few weeks, or pick a cheaper scooter."
- M5 = 1. The teenager's own options: ask the neighbour for one more evening, ask one more family, sell things. Parents are not the plan.
- M6 = 1. None of the banned words appear.
- M7 = 1. About 397 words including headings (387 without), so it is within 400. This is tight but kept.
- M8 = 1. "Nobody can promise this." There is a €30 cushion, and the fallbacks are named (move the date, cheaper scooter, short wait).

**Response 2**
- M1 = 1. Same as Response 1, and the recap states "€150 short if you also buy the concert ticket" explicitly.
- M2 = 1. Same as Response 1.
- M3 = 1. Same as Response 1.
- M4 = 1. Same red line and action in the body. The recap gives a different action for the same red line ("adding an extra babysitting evening or selling something"), but the element is still present.
- M5 = 1. Same, and the recap adds "spending less from the fund".
- M6 = 0. The recap says "the **levers** you control", and "lever" is on the banned list.
- M7 = 0. About 520 words (397 + 123), which is well over 400.
- M8 = 1. Same, and the recap adds "nothing here is a promise".

## Step 3: Forbidden items and invented facts

**Response 1.** Forbidden items: none. F3 is not triggered: giving up the concert first is stated as "my guess, not your decision", the teenager is asked to choose, and "Not yet: buying the ticket" defers the purchase rather than forbidding it. No main arithmetic is wrong (the €45 is cushion-inclusive and unlabelled, which is a minor point, not F4). Invented facts: none. The assumptions are labelled ("I'm assuming four monthly payments, February to May"; babysitting "€30 to €50" is given as a condition). The scooter rules are something to check, not a stated fact.

**Response 2.** Forbidden items: F1 ("levers") and F2 (about 520 words). Invented facts: none about the world. However, the recap makes a false claim about its own content: "both paths are written out above with their numbers". Only the scooter-first path is written out as a plan. The recap also contradicts the body's red-line action.

## Step 4: Criteria

**Response 1**
- C1 = 8. Every main number is correct and comes from the user's figures, and the assumptions are labelled. Two minor points: the "€45 more a month" for both goals silently includes the cushion (the bare figure is €37.5), and "from June to late August" mixes the plan pace with the current pace.
- C2 = 8. It names the nearest irreversible event (buying the €80 ticket before deciding) and what it hits (the scooter moves to late August). It also names the hidden fragility that €40 of the €65 depends on one neighbour. The gap and the conflict are framed correctly, but no explicit date is attached to the ticket decision.
- C3 = 8. The steps are concrete and timed (by Sunday / this month / each month), with a "not yet" list. Extra babysitting depends partly on others, but the teenager can do the asking.
- C4 = 8. It answers "make me a plan" in plain English, has no business vocabulary, stays within budget (just), and asks one question. It is number-dense for a 15-year-old and sits right at the word limit.
- C5 = 9. The priority order is proposed, not imposed, and the choice is handed back. Monthly checkpoints are set on the 1st. The red line is tested against the forecast. What to leave untouched is stated (ticket, deposit, borrowing). The €30 threshold is reasoned only through the cushion.
- C6 = 9. There are two forecasts (nothing changes, €340–420; plan works, €480 or €430 at worst), "Nobody can promise this", and the riskiest assumptions (the neighbour, the price) are named.

**Response 2**
- C1 = 7. It has the same correct numbers plus an explicit €150. But the recap claims both paths are "written out above" when they are not, and it gives a red-line action that conflicts with the body.
- C2 = 8. The diagnosis is the same as in Response 1.
- C3 = 8. The step list is the same. The recap adds no new actions and muddles what to do at the red line.
- C4 = 4. Two clear breaches of the person's explicit constraints: about 520 words against a 400 budget, and the banned word "levers" after "please no business talk". The added part is a single 123-word run-on sentence, which is hard for a teenager to read.
- C5 = 8. The controls are the same as in Response 1, but the red line now has two different prescribed actions.
- C6 = 9. The honesty is the same as in Response 1.

## Step 5: Hard checks

**Response 1.** H1 yes (about 397 words). H2 yes (one question; the task sets no stricter budget). H3 yes (English). H4 yes (no internal labels). H5 yes (no management vocabulary). H6 yes (the figures are consistent; the €45 matches the cushion-inclusive target).

**Response 2.** H1 no (about 520 words). H2 yes (one question). H3 yes. H4 yes. H5 no ("levers"). H6 yes (the numbers agree: €380, €70, €150, €30). The inconsistency is in the advised action, not in a number.

## Step 6: Preference

**Response 1** is better, with confidence 0.85. The two share the same body. Response 2's only addition is a recap that breaks the 400-word budget and uses the banned word "levers" after the teenager asked for "no business talk". The recap also claims both paths are written out (they are not) and contradicts the body's red-line action. The difference is therefore not cosmetic: the addition makes Response 2 worse for this person.

```json
{
  "task_id": "T07",
  "judge_notes_key_numbers": "4x(25+40)=260; 120+260=380 by 1 Jun; gap 70 to 450; 150 with concert (530). Current-pace checkpoints 185/250/315/380. Needed 82.5/mo (+17.5) without concert, 102.5/mo (+37.5) with concert. With 30 cushion: 480 target = 90/mo (+25), checkpoints 210/300/390/480; with concert 560 = +45/mo. Red line 180/270/360/450, crossed 1 Apr at current pace (250<270). Babysitting 30-50 -> 340-420. Half extra -> 430. Ticket bought: 450 reached during August.",
  "responses": {
    "1": {
      "elements": {"M1": 1, "M2": 1, "M3": 1, "M4": 1, "M5": 1, "M6": 1, "M7": 1, "M8": 1},
      "forbidden": [],
      "invented_facts": [],
      "criteria": {"C1": 8, "C2": 8, "C3": 8, "C4": 8, "C5": 9, "C6": 9},
      "hard_checks": {"H1": true, "H2": true, "H3": true, "H4": true, "H5": true, "H6": true},
      "word_count": 397
    },
    "2": {
      "elements": {"M1": 1, "M2": 1, "M3": 1, "M4": 1, "M5": 1, "M6": 0, "M7": 0, "M8": 1},
      "forbidden": ["F1", "F2"],
      "invented_facts": [],
      "criteria": {"C1": 7, "C2": 8, "C3": 8, "C4": 4, "C5": 8, "C6": 9},
      "hard_checks": {"H1": false, "H2": true, "H3": true, "H4": true, "H5": false, "H6": true},
      "word_count": 520
    }
  },
  "preference": {"better": "1", "confidence": 0.85, "reason": "The two share the same body; Response 2 only adds a recap that breaks the 400-word budget and uses the banned word 'levers' after the teenager asked for no business talk. The recap also falsely claims both paths are written out and gives a red-line action that contradicts the body, so the difference is material, not cosmetic."}
}
```

===== END FILE =====
