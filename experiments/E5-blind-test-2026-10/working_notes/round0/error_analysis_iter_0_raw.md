# Error analysis — iteration 0, condition C-v1.0

| task | n judgments | mean total | missed elements (share) | forbidden | hard-check fails | C1 | C2 | C3 | C4 | C5 | C6 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| T01 | 12 | 91.2 | — | — | — | 8.1 | 8.9 | 8.3 | 8.2 | 8.9 | 8.8 |
| T02 | 12 | 84.7 | M4 6/12, M2 2/12 | — | H4 1/12 | 7.8 | 7.9 | 7.5 | 8.5 | 8.2 | 8.2 |
| T03 | 12 | 85.2 | M3 4/12, M1 2/12 | F1 2/12 | — | 8.1 | 8.2 | 7.6 | 8.2 | 7.3 | 8.0 |
| T04 | 12 | 68.9 | M8 12/12, M7 6/12, M4 6/12, M5 3/12 | F2 6/12, F1 2/12 | H1 12/12, H2 8/12 | 7.6 | 8.1 | 7.9 | 5.1 | 7.9 | 8.2 |
| T05 | 12 | 92.3 | — | — | — | 8.6 | 8.6 | 9.0 | 8.2 | 9.0 | 8.9 |
| T06 | 12 | 84.0 | M7 8/12, M2 2/12, M4 1/12 | — | — | 7.8 | 8.2 | 7.3 | 8.0 | 8.8 | 8.4 |
| T07 | 12 | 90.2 | M1 1/12 | — | — | 8.3 | 8.2 | 8.0 | 8.2 | 8.9 | 9.0 |
| T08 | 12 | 88.8 | M3 1/12 | — | H6 2/12 | 6.9 | 8.4 | 8.7 | 7.8 | 8.9 | 8.8 |
| T09 | 12 | 87.3 | M5 7/12, M7 1/12 | — | — | 8.0 | 8.2 | 8.4 | 8.4 | 9.1 | 8.5 |
| T10 | 12 | 86.4 | M6 4/12 | — | — | 7.2 | 7.3 | 7.7 | 8.9 | 8.7 | 8.2 |

## Invented facts flagged by the judge (verbatim)

**T01**
- [T01_C-v1.0-r3_vs_A-r3/12 r3] Generic claim that a good mechanic is hard to win back, stated as fact (minor, does not change the advice)
- [T01_C-v1.0-r4_vs_B-r1/12 r4] Banks say yes more easily while the account still shows EUR 9,000 (general rule stated as fact, unlabelled)
- [T01_C-v1.0-r4_vs_B-r1/21 r4] Banks say yes more easily while the account still shows EUR 9,000 (general claim stated as fact, borderline)
- [T01_C-v1.0-r5_vs_B-r2/12 r5] Credit line 'costs nothing until used' (ignores arrangement/commitment fees; stated as fact)
- [T01_C-v1.0-r5_vs_B-r2/12 r5] Banks agree more readily while the account looks healthy (general causal claim)
- [T01_C-v1.0-r5_vs_B-r2/12 r5] First seasons often only just break even (generalisation stated as fact)
- [T01_C-v1.0-r5_vs_B-r2/21 r5] Credit line 'costs nothing until used' (fees often apply; stated as fact)
- [T01_C-v1.0-r5_vs_B-r2/21 r5] 'Banks agree more readily while your account looks healthy' (general lending claim stated as fact)
- [T01_C-v1.0-r5_vs_B-r2/21 r5] 'First seasons often only just break even' (unsupported generalisation stated as fact)
- [T01_C-v1.0-r6_vs_B-r3/12 r6] 'a new rental line usually needs a season to find its demand' (general claim stated as fact, not from the task; minor)
- [T01_C-v1.0-r6_vs_B-r3/21 r6] 'a new rental line usually needs a season to find its demand' - general rule of thumb not in the task, stated as fact (minor)

**T02**
- [T02_C-v1.0-r1_vs_A-r1/12 r1] Quoted rule 'never below zero' presented as an existing threshold the person never set
- [T02_C-v1.0-r1_vs_A-r1/21 r1] Quoted threshold 'never below zero' presented as an established rule though absent from the task
- [T02_C-v1.0-r3_vs_A-r3/12 r3] Two-hour discard rule ('food that may have been warm over two hours') stated as a rule, not in the task
- [T02_C-v1.0-r3_vs_A-r3/21 r3] 'warm over two hours' discard threshold given as a rule, not in the task
- [T02_C-v1.0-r5_vs_B-r2/21 r5] Permit suspension 'also endangers the wedding job' stated as fact (unlabelled inference that the catering job depends on the permit)
- [T02_C-v1.0-r6_vs_B-r3/21 r6] 'A suspension stops the wedding job' stated as certain although the wedding date is not given (unlabelled assumption)

**T03**
- [T03_C-v1.0-r1_vs_A-r1/12 r1] Members who got used to €120 rarely accept €150 again (unsourced behavioural claim stated as a regularity)
- [T03_C-v1.0-r1_vs_A-r1/12 r1] Tax offices are usually more willing to agree instalments before they start enforcing (unsourced general claim)
- [T03_C-v1.0-r1_vs_A-r1/21 r1] Members who got used to €120 rarely accept €150 again (unsupported behavioural generalisation stated as fact)
- [T03_C-v1.0-r1_vs_A-r1/21 r1] Tax offices are usually more willing to agree instalments before they start enforcing (general claim not in task)
- [T03_C-v1.0-r2_vs_A-r2/12 r2] 'three to five goals are usually enough for a year' (unsourced rule of thumb)
- [T03_C-v1.0-r2_vs_A-r2/12 r2] 'Complaints and reviews share one cause, service quality' (asserted cause)
- [T03_C-v1.0-r2_vs_A-r2/12 r2] 'a new room usually loses money at first' (unsourced general claim)
- [T03_C-v1.0-r2_vs_A-r2/21 r2] Complaints and reviews share one cause, service quality (causal claim stated as fact, not in task)
- [T03_C-v1.0-r3_vs_A-r3/21 r3] 'Three to five goals are usually enough for a year' - unsourced rule of thumb stated as general fact (minor)
- [T03_C-v1.0-r4_vs_B-r1/21 r4] 'three to five goals are usually enough for a year' stated as a rule without source
- [T03_C-v1.0-r4_vs_B-r1/21 r4] 'the app, hires and room will cost you more hours before they save any' stated as fact
- [T03_C-v1.0-r5_vs_B-r2/12 r5] '11 weeks remain' in the calendar year and '~€6,000 of profit' by then: the current date is not in the task and the plan is for next year (conditional framing; does not change the advice)
- [T03_C-v1.0-r5_vs_B-r2/21 r5] '11 weeks remain' in the year (current date not given in the task; conditional and correct for mid-October)
- [T03_C-v1.0-r5_vs_B-r2/21 r5] 'three to five [goals] are usually enough for a year' (unlabelled norm)
- [T03_C-v1.0-r6_vs_B-r3/21 r6] 'a cut is the hardest move to undo, because raising prices later loses members' - general causal claim stated as fact (minor)

**T04**
- [T04_C-v1.0-r1_vs_A-r1/12 r1] AI substitution asserted as a market-wide shift in plain translation that 'you cannot change' (stated as fact, not a labelled hypothesis)
- [T04_C-v1.0-r1_vs_A-r1/12 r1] Reviewing machine output and specialist, legal or certified texts asserted as 'firmer ground' (stated as fact)
- [T04_C-v1.0-r1_vs_A-r1/21 r1] Stated as fact, unlabelled: the client's AI move reflects a shift in 'plain translation as a whole' that 'you cannot change'
- [T04_C-v1.0-r1_vs_A-r1/21 r1] Stated as fact, unlabelled: 'firmer ground' is reviewing machine output and specialist, legal or certified texts
- [T04_C-v1.0-r2_vs_A-r2/12 r2] AI translation tools 'handle badly' specialist/certified texts and machine-output checking (stated as fact, not in task)
- [T04_C-v1.0-r2_vs_A-r2/21 r2] AI translation tools handle specialist/certified texts and checking of machine output badly (stated as fact)
- [T04_C-v1.0-r3_vs_A-r3/12 r3] Firms that adopt a tool often keep a reviewer.
- [T04_C-v1.0-r3_vs_A-r3/12 r3] Machine translation is a strong pull against plain translation work (stated as fact).
- [T04_C-v1.0-r3_vs_A-r3/21 r3] Firms that adopt a tool often keep a reviewer (unsourced general claim stated as fact)
- [T04_C-v1.0-r3_vs_A-r3/21 r3] Machine translation is a strong pull against plain translation work (unsourced market claim stated as fact)
- [T04_C-v1.0-r4_vs_B-r1/12 r4] 'clients often still want it' — claim that clients still pay for human review of machine output, stated as fact without basis in the task
- [T04_C-v1.0-r4_vs_B-r1/21 r4] 'clients often still want it' — claim that clients still pay for human review of machine output, presented as fact, not in the task
- [T04_C-v1.0-r5_vs_B-r2/12 r5] 'post-editing is a paid service of its own' stated as general industry fact (minor)
- [T04_C-v1.0-r5_vs_B-r2/21 r5] Post-editing is a paid service of its own (unlabelled industry claim)
- [T04_C-v1.0-r5_vs_B-r2/21 r5] You heard it early (no stop date known)

**T05**
- [T05_C-v1.0-r1_vs_A-r1/21 r1] Rent as an ongoing cost during illness (rent not given in the task; minor)
- [T05_C-v1.0-r2_vs_A-r2/12 r2] A 10% monthly revenue swing described as 'normal' (unlabelled assumption, borderline)
- [T05_C-v1.0-r2_vs_A-r2/21 r2] A normal 10% swing in revenue (10% monthly swing presented as normal without labelling it an assumption)

**T06**
- [T06_C-v1.0-r2_vs_A-r2/12 r2] Employer-tax add-on 'about EUR 650-800 a month' (rate not in task, conditional but not labelled as an assumption)
- [T06_C-v1.0-r2_vs_A-r2/21 r2] Employer taxes on the two technicians add about EUR 650-800 a month (external rate range stated as fact)
- [T06_C-v1.0-r6_vs_B-r3/12 r6] Break-even upper bound of about 6,800 relies on an unstated employer-contribution rate (minor, stated conditionally)

**T07**
- [T07_C-v1.0-r3_vs_A-r3/12 r3] A helmet isn't in the €450 (unlabelled side claim, minor)
- [T07_C-v1.0-r3_vs_A-r3/21 r3] A helmet isn't in the €450 (unlabelled product claim)

**T08**
- [T08_C-v1.0-r1_vs_A-r1/12 r1] EU rule stated unhedged: statutory interest and at least EUR 40 per late invoice (accurate, but not in the task, and EU location not given)
- [T08_C-v1.0-r1_vs_A-r1/12 r1] 'mentioning it moves you up their list' presented as a certain effect
- [T08_C-v1.0-r1_vs_A-r1/21 r1] EU statutory late-payment interest and at least EUR 40 per late invoice (not in task; true in substance, presented as fact)
- [T08_C-v1.0-r1_vs_A-r1/21 r1] Claim that mentioning statutory interest moves you up the customer's payment list (unsupported)
- [T08_C-v1.0-r2_vs_A-r2/12 r2] EU/euro-area late-payment interest and fixed fee of at least EUR 40 per invoice (external rule, hedged 'check national rules')
- [T08_C-v1.0-r2_vs_A-r2/21 r2] Euro-area late-payment interest and fixed fee of at least €40 per invoice (not in task; accurate and hedged)
- [T08_C-v1.0-r3_vs_A-r3/12 r3] EU rules normally give late-payment interest and at least EUR40 per invoice (external rule, not in task; hedged with 'normally')
- [T08_C-v1.0-r3_vs_A-r3/12 r3] All EUR13,000 of receivable growth attributed to the big customer ('EUR13,000 has built so far') without labelling as an assumption
- [T08_C-v1.0-r3_vs_A-r3/21 r3] EU rules normally give late-payment interest and at least EUR 40 per invoice (outside rule with specific figure, hedged)
- [T08_C-v1.0-r4_vs_B-r1/12 r4] Late-payment interest 'which most EU countries allow with a minimum €40 per invoice' - legal rule not in the task, presented as fact (jurisdiction unknown; conflates statutory interest with the fixed €40 compensation)
- [T08_C-v1.0-r4_vs_B-r1/21 r4] Late-payment interest 'which most EU countries allow with a minimum €40 per invoice' (external legal rule/figure not in the task, presented as fact)
- [T08_C-v1.0-r5_vs_B-r2/12 r5] In the EU, late business payments carry statutory interest plus EUR 40 per invoice (external legal rule with specific figure, stated as fact; not in task)
- [T08_C-v1.0-r5_vs_B-r2/21 r5] 'In the EU, late business payments carry statutory interest plus €40 per invoice' - specific legal rule and figure not in the task, country not stated, presented as fact
- [T08_C-v1.0-r5_vs_B-r2/21 r5] 'The other €14,000 left the bank without touching profit' - asserts the class of cause as fact (excludes a wrong profit figure), unlabelled
- [T08_C-v1.0-r6_vs_B-r3/12 r6] EU business invoices carry statutory late-payment interest and at least €40 per invoice (external legal rule stated flatly; assumes an EU location; accurate in substance)
- [T08_C-v1.0-r6_vs_B-r3/12 r6] In many countries VAT falls due on invoicing, before payment (external rule, hedged and framed as a question for the accountant; accurate)
- [T08_C-v1.0-r6_vs_B-r3/21 r6] EU business invoices carry statutory late-payment interest and at least EUR 40 per invoice (external rule with a figure, stated categorically, EU location assumed)
- [T08_C-v1.0-r6_vs_B-r3/21 r6] VAT in many countries falls due on invoicing, before payment (external rule, hedged)

**T09**
- [T09_C-v1.0-r1_vs_A-r1/12 r1] States that in 2024 'the factory was still working' (task says it closed in 2023)
- [T09_C-v1.0-r1_vs_A-r1/12 r1] Compares pay to the minimum wage ('considerably below the minimum wage'), an external rule not in the task (no figure given)
- [T09_C-v1.0-r1_vs_A-r1/21 r1] The factory was still working in 2024 (contradicts task: closed in 2023)
- [T09_C-v1.0-r1_vs_A-r1/21 r1] EUR 2.10/h is well below the minimum wage (external benchmark, unlabelled, no figure)
- [T09_C-v1.0-r3_vs_A-r3/21 r3] 'the biggest employer': the task says the largest factory closed, not that it was the largest employer (minor reinterpretation)

**T10**
- [T10_C-v1.0-r1_vs_A-r1/12 r1] EU rule stated as fact without knowing the country: late B2B payment entitles interest and a minimum €40 compensation
- [T10_C-v1.0-r1_vs_A-r1/21 r1] In the EU, B2B late payment entitles to interest and a minimum 40 EUR compensation (external legal rule; accurate but stated as fact while the person's country is unknown)
- [T10_C-v1.0-r2_vs_A-r2/12 r2] EU B2B late-payment rule stated as fact: interest plus fixed compensation of at least 40 EUR per invoice in most EU countries (hedged with 'check your country')
- [T10_C-v1.0-r2_vs_A-r2/21 r2] In most EU countries B2B late payment gives interest plus fixed compensation of at least €40 per invoice (external rule, hedged)
- [T10_C-v1.0-r2_vs_A-r2/21 r2] Unlabelled assumption that paying one invoice (≥€650) makes the credit line unnecessary
- [T10_C-v1.0-r3_vs_A-r3/21 r3] EU late-payment directive: interest and at least 40 EUR per invoice (accurate external rule, conditioned on 'if EU and client is a company')
- [T10_C-v1.0-r4_vs_B-r1/12 r4] EU late-payment rule: interest plus compensation 'usually €40 per invoice' stated as fact; jurisdiction not in task
- [T10_C-v1.0-r4_vs_B-r1/12 r4] 'he doesn't read emails' — task only says the client does not reply
- [T10_C-v1.0-r4_vs_B-r1/12 r4] Specific calendar dates (rent on 21 October, red line ~21 November, Monday 19 October) not given in task; rent would be 22.10 if today is 16.10 (minor, does not change advice)
- [T10_C-v1.0-r4_vs_B-r1/21 r4] In the EU late payment gives the right to interest and compensation, usually 40 EUR per invoice (external legal rule; client's jurisdiction not given)
- [T10_C-v1.0-r4_vs_B-r1/21 r4] The client does not read emails ('he doesn't read emails'); task says only that he does not reply
- [T10_C-v1.0-r5_vs_B-r2/12 r5] EU legal rule stated as fact (conditional): late-payment penalty and at least 40 EUR compensation per invoice
- [T10_C-v1.0-r5_vs_B-r2/21 r5] EU late-payment rule: by law a penalty and at least 40 EUR compensation per invoice (external legal rule, conditional on being in the EU, not in task)
- [T10_C-v1.0-r6_vs_B-r3/12 r6] EU late-payment rule (right to charge penalty interest and compensation) stated as fact, conditioned only on 'if you are in the EU', not in task
- [T10_C-v1.0-r6_vs_B-r3/12 r6] Specific calendar dates ('tomorrow… 16 October', 'by 19 October', 'by Friday') assume today's date, which the task does not give; unlabelled
- [T10_C-v1.0-r6_vs_B-r3/21 r6] Calendar dates '16 October' (tomorrow) and '19 October' presented as fact; the task gives no current date
- [T10_C-v1.0-r6_vs_B-r3/21 r6] EU rule: right to charge late-payment interest and compensation (conditional 'if you are in the EU'; not in task, accurate in substance)

## Lowest-scoring judgments per task (file, slot, total)

- T01: T01_C-v1.0-r5_vs_B-r2_21.md slot 2 = 88.0; T01_C-v1.0-r4_vs_B-r1_21.md slot 2 = 90.0; T01_C-v1.0-r6_vs_B-r3_12.md slot 1 = 90.0
- T02: T02_C-v1.0-r3_vs_A-r3_12.md slot 1 = 78.0; T02_C-v1.0-r4_vs_B-r1_21.md slot 2 = 79.0; T02_C-v1.0-r2_vs_A-r2_12.md slot 1 = 80.0
- T03: T03_C-v1.0-r3_vs_A-r3_12.md slot 1 = 80.0; T03_C-v1.0-r3_vs_A-r3_21.md slot 2 = 82.0; T03_C-v1.0-r2_vs_A-r2_12.md slot 1 = 84.0
- T04: T04_C-v1.0-r4_vs_B-r1_12.md slot 1 = 63.0; T04_C-v1.0-r4_vs_B-r1_21.md slot 2 = 63.0; T04_C-v1.0-r1_vs_A-r1_12.md slot 1 = 66.0
- T05: T05_C-v1.0-r2_vs_A-r2_21.md slot 2 = 91.0; T05_C-v1.0-r4_vs_B-r1_21.md slot 2 = 91.0; T05_C-v1.0-r1_vs_A-r1_21.md slot 2 = 92.0
- T06: T06_C-v1.0-r4_vs_B-r1_21.md slot 2 = 76.0; T06_C-v1.0-r4_vs_B-r1_12.md slot 1 = 80.0; T06_C-v1.0-r3_vs_A-r3_12.md slot 1 = 81.0
- T07: T07_C-v1.0-r1_vs_A-r1_21.md slot 2 = 82.0; T07_C-v1.0-r4_vs_B-r1_21.md slot 2 = 89.0; T07_C-v1.0-r5_vs_B-r2_12.md slot 1 = 89.0
- T08: T08_C-v1.0-r3_vs_A-r3_21.md slot 2 = 83.0; T08_C-v1.0-r4_vs_B-r1_21.md slot 2 = 85.0; T08_C-v1.0-r3_vs_A-r3_12.md slot 1 = 87.0
- T09: T09_C-v1.0-r5_vs_B-r2_12.md slot 1 = 80.0; T09_C-v1.0-r1_vs_A-r1_21.md slot 2 = 82.0; T09_C-v1.0-r4_vs_B-r1_12.md slot 1 = 84.0
- T10: T10_C-v1.0-r2_vs_A-r2_12.md slot 1 = 79.0; T10_C-v1.0-r2_vs_A-r2_21.md slot 2 = 79.0; T10_C-v1.0-r5_vs_B-r2_12.md slot 1 = 82.0
