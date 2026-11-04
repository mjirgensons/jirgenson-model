# Error analysis — iteration 3, condition C-v1.1-c

| task | n judgments | mean total | missed elements (share) | forbidden | hard-check fails | C1 | C2 | C3 | C4 | C5 | C6 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| T01 | 6 | 89.8 | — | — | — | 7.5 | 8.7 | 8.3 | 8.2 | 8.5 | 8.7 |
| T02 | 6 | 88.2 | — | — | — | 7.8 | 8.5 | 8.3 | 7.8 | 7.7 | 8.0 |
| T03 | 6 | 83.3 | M8 6/6 | — | — | 7.7 | 8.2 | 8.0 | 8.3 | 7.0 | 8.2 |
| T04 | 6 | 67.2 | M4 6/6, M8 4/6, M7 2/6 | F2 6/6 | H2 6/6, H1 4/6 | 7.2 | 8.0 | 7.7 | 5.2 | 6.8 | 7.7 |
| T05 | 6 | 89.8 | — | — | — | 7.0 | 7.8 | 8.2 | 9.0 | 9.0 | 8.8 |
| T06 | 6 | 89.0 | M4 1/6 | — | — | 8.3 | 8.5 | 7.5 | 8.5 | 8.5 | 8.5 |
| T07 | 6 | 82.0 | M7 2/6 | F2 2/6 | H1 2/6 | 6.5 | 8.0 | 7.5 | 7.5 | 7.7 | 7.8 |
| T08 | 6 | 86.8 | M7 2/6 | — | — | 7.3 | 8.5 | 8.0 | 8.0 | 8.0 | 8.7 |
| T09 | 6 | 85.5 | M5 1/6, M6 1/6 | — | H6 1/6 | 6.7 | 8.2 | 8.2 | 8.0 | 8.5 | 8.0 |
| T10 | 6 | 83.3 | M6 2/6, M1 2/6 | — | — | 7.0 | 7.2 | 8.2 | 7.8 | 8.7 | 7.8 |

## Invented facts flagged by the judge (verbatim)

**T01**
- [T01_C-v1.3-c-r1_vs_C-v1.1-c-r1/12 r1] 'in many countries' a tax or VAT instalment falls in winter (general claim not in task, presented as fact; minor, framed as a check)
- [T01_C-v1.3-c-r1_vs_C-v1.1-c-r1/21 r1] 'in many countries' a tax or VAT instalment falls in winter: general claim not in the task, unlabelled (minor, framed as a check)
- [T01_C-v1.3-c-r2_vs_C-v1.1-c-r2/12 r2] October is usually weaker
- [T01_C-v1.3-c-r2_vs_C-v1.1-c-r2/12 r2] in most EU countries cutting hours needs the employee's agreement
- [T01_C-v1.3-c-r2_vs_C-v1.1-c-r2/12 r2] many dealers allow payment in spring
- [T01_C-v1.3-c-r2_vs_C-v1.1-c-r2/12 r2] the first season is usually weaker
- [T01_C-v1.3-c-r2_vs_C-v1.1-c-r2/21 r2] October is usually weaker (unlabelled general claim)
- [T01_C-v1.3-c-r2_vs_C-v1.1-c-r2/21 r2] in most EU countries reduced hours need the employee's agreement (legal generalisation, hedged with 'check yours')
- [T01_C-v1.3-c-r2_vs_C-v1.1-c-r2/21 r2] many dealers allow payment in spring (unlabelled claim)
- [T01_C-v1.3-c-r2_vs_C-v1.1-c-r2/21 r2] the first season is usually weaker (unlabelled general claim)

**T02**
- [T02_C-v1.3-c-r2_vs_C-v1.1-c-r2/12 r2] A few hours' grace is 'often allowed for a booked repair' (unsupported claim about inspector practice, only softly hedged)
- [T02_C-v1.3-c-r2_vs_C-v1.1-c-r2/21 r2] Grace for a booked repair is 'often allowed' (inspector practice not in task, weakly hedged)
- [T02_C-v1.3-c-r2_vs_C-v1.1-c-r2/21 r2] Food-safety threshold 'usually past 2 to 4 hours' (external rule, hedged with 'check local rules'; minor)
- [T02_C-v1.3-c-r3_vs_C-v1.1-c-r3/12 r3] Food above about 8°C for more than a few hours usually has to be thrown away (hedged food-safety rule not in the task)
- [T02_C-v1.3-c-r3_vs_C-v1.1-c-r3/21 r3] Food above about 8C for more than a few hours usually has to be thrown away (external food-safety rule not in the task; hedged with 'check your local rule')

**T03**
- [T03_C-v1.3-c-r1_vs_C-v1.1-c-r1/12 r1] in most countries the tax office agrees an instalment plan more readily before it starts enforcement (hedged general rule, not in task)
- [T03_C-v1.3-c-r2_vs_C-v1.1-c-r2/12 r2] in most countries tax offices will consider an instalment plan if you ask first (general rule presented as fact)
- [T03_C-v1.3-c-r2_vs_C-v1.1-c-r2/21 r2] 'in most countries tax offices will consider [an instalment plan] if you ask first' stated as a general rule
- [T03_C-v1.3-c-r2_vs_C-v1.1-c-r2/21 r2] 'with a new studio taking some of yours' stated as fact although no member loss is given
- [T03_C-v1.3-c-r3_vs_C-v1.1-c-r3/21 r3] 'Many tax offices agree to instalments if asked before enforcement starts' (hedged general claim not in task, minor)

**T04**
- [T04_C-v1.3-c-r1_vs_C-v1.1-c-r1/12 r1] Companies often keep human checking for legal or customer-facing texts because raw machine output still has errors that matter there (general industry claim/cause not in the task)
- [T04_C-v1.3-c-r1_vs_C-v1.1-c-r1/21 r1] Companies often keep human checking for legal or customer-facing texts because raw machine output still has errors that matter there (general industry claim presented as fact)
- [T04_C-v1.3-c-r2_vs_C-v1.1-c-r2/12 r2] Routine, repetitive text is often where companies try AI tools first (general industry claim presented as fact)
- [T04_C-v1.3-c-r2_vs_C-v1.1-c-r2/12 r2] Companies often still want a human check for legal or customer-facing text, usually at a lower rate per word (market/pricing claim presented as fact)
- [T04_C-v1.3-c-r2_vs_C-v1.1-c-r2/21 r2] Routine, repetitive text is often where companies try AI tools first (general industry claim stated as fact)
- [T04_C-v1.3-c-r2_vs_C-v1.1-c-r2/21 r2] Companies often still want a human check for legal or customer-facing text, usually at a lower rate per word (general industry claim stated as fact)

**T05**
- [T05_C-v1.3-c-r1_vs_C-v1.1-c-r1/12 r1] In most EU countries a cancellation fee is allowed if the client agrees when booking (legal rule not in the task, stated as fact, hedged with 'check yours')
- [T05_C-v1.3-c-r1_vs_C-v1.1-c-r1/21 r1] In most EU countries a cancellation fee is allowed if the client agrees when booking (legal rule not in task, stated as fact in both turns, softened by 'check yours')
- [T05_C-v1.3-c-r2_vs_C-v1.1-c-r2/12 r2] In most EU countries a cancellation fee is allowed if announced in advance (legal rule not in task, stated as fact)
- [T05_C-v1.3-c-r2_vs_C-v1.1-c-r2/21 r2] In most EU countries a cancellation fee is allowed if announced in advance (legal claim presented as fact, softened by 'check yours')
- [T05_C-v1.3-c-r3_vs_C-v1.1-c-r3/12 r3] In most EU countries no-show charges/deposits are allowed if agreed at booking (legal rule stated as fact, hedged 'check yours')
- [T05_C-v1.3-c-r3_vs_C-v1.1-c-r3/12 r3] Many self-employed have little sick pay (general claim, hedged 'check yours')
- [T05_C-v1.3-c-r3_vs_C-v1.1-c-r3/21 r3] 'In most EU countries this is allowed if agreed at booking' (legal generalisation assuming EU location; hedged with 'check yours')
- [T05_C-v1.3-c-r3_vs_C-v1.1-c-r3/21 r3] 'many self-employed have little sick pay' (general claim; hedged with 'check yours')

**T06**
- [T06_C-v1.3-c-r2_vs_C-v1.1-c-r2/21 r2] 'A new salon usually takes months to fill its diary' stated as general fact (qualitative, minor)
- [T06_C-v1.3-c-r3_vs_C-v1.1-c-r3/12 r3] Hire the second technician when the first is booked about 80% for four weeks, presented as a 'usual rule of thumb'

**T07**
- [T07_C-v1.3-c-r1_vs_C-v1.1-c-r1/12 r1] Helmet and lock are 'usually extra' (stated as fact)
- [T07_C-v1.3-c-r1_vs_C-v1.1-c-r1/12 r1] As a minor you 'will often need a parent to buy or insure it' (rule stated as fact)
- [T07_C-v1.3-c-r1_vs_C-v1.1-c-r1/21 r1] Helmet and lock are 'usually extra' (stated as fact, not in task)
- [T07_C-v1.3-c-r1_vs_C-v1.1-c-r1/21 r1] As a minor you will often need a parent to buy or insure the scooter; minimum age/helmet/insurance rules differ by country (stated as fact, not framed as a check)
- [T07_C-v1.3-c-r2_vs_C-v1.1-c-r2/12 r2] In many EU countries the minimum e-scooter age is 14 to 16 and some places require insurance
- [T07_C-v1.3-c-r2_vs_C-v1.1-c-r2/12 r2] A helmet usually costs another €30 to €50
- [T07_C-v1.3-c-r2_vs_C-v1.1-c-r2/21 r2] In many EU countries the minimum e-scooter riding age is 14 to 16
- [T07_C-v1.3-c-r2_vs_C-v1.1-c-r2/21 r2] Some places require insurance for e-scooters
- [T07_C-v1.3-c-r2_vs_C-v1.1-c-r2/21 r2] A helmet usually costs another €30 to €50
- [T07_C-v1.3-c-r3_vs_C-v1.1-c-r3/12 r3] In most EU countries e-scooters have age, speed and sometimes insurance or helmet rules (stated as fact, not in task)
- [T07_C-v1.3-c-r3_vs_C-v1.1-c-r3/21 r3] 'in most EU countries e-scooters have age, speed and sometimes insurance or helmet rules' stated as fact (hedged, not in task)

**T08**
- [T08_C-v1.3-c-r1_vs_C-v1.1-c-r1/12 r1] 'In most EU countries late payment can carry interest' - external legal rule stated as fact (hedged, minor, not material)
- [T08_C-v1.3-c-r1_vs_C-v1.1-c-r1/21 r1] 'In most EU countries late payment can carry interest' - general legal rule not in the task, presented as fact (hedged with 'check yours')
- [T08_C-v1.3-c-r2_vs_C-v1.1-c-r2/12 r2] 'in many countries VAT is due on the invoice date even if unpaid' (general rule stated as fact, hedged, plausibly true, offered as something to check)
- [T08_C-v1.3-c-r2_vs_C-v1.1-c-r2/12 r2] 'banks usually lend before the balance is low' (general claim stated as fact)
- [T08_C-v1.3-c-r2_vs_C-v1.1-c-r2/21 r2] Hedged general rule: in many countries VAT is due on the invoice date even if unpaid (accurate, offered as a check, minor)
- [T08_C-v1.3-c-r2_vs_C-v1.1-c-r2/21 r2] General claim: banks usually lend before the balance is low (minor heuristic)
- [T08_C-v1.3-c-r3_vs_C-v1.1-c-r3/12 r3] Late-payment fixed fee 'at least €40 under EU rules' — external legal rule not in the task, stated as fact (accurate, hedged with 'check yours')
- [T08_C-v1.3-c-r3_vs_C-v1.1-c-r3/21 r3] Late-payment rule presented as fact: 'In most EU countries you may charge late-payment interest plus a fixed fee per invoice (at least €40 under EU rules)' - external legal rule and EU location not in the task (accurate in substance, hedged with 'check yours')

**T09**
- [T09_C-v1.3-c-r1_vs_C-v1.1-c-r1/12 r1] 'many leases require 1–3 months' notice' (notice-period rule not in task)
- [T09_C-v1.3-c-r1_vs_C-v1.1-c-r1/12 r1] 'Where there are fewer residents, it is usually not easier for the landlord to find another tenant' (market claim presented as fact)
- [T09_C-v1.3-c-r1_vs_C-v1.1-c-r1/21 r1] 'many leases require 1–3 months' notice' — general contract notice rule not in the task, stated as fact
- [T09_C-v1.3-c-r1_vs_C-v1.1-c-r1/21 r1] 'Where there are fewer residents, it is usually not easier for the landlord to find another tenant' — general landlord-market claim stated as fact
- [T09_C-v1.3-c-r2_vs_C-v1.1-c-r2/12 r2] Unlabelled generalisation: 'In a shrinking town landlords usually give way, because empty premises bring no income' (softened by 'not guaranteed')
- [T09_C-v1.3-c-r2_vs_C-v1.1-c-r2/21 r2] Landlords in shrinking towns usually concede because empty premises earn nothing (unlabelled generalisation, softened by 'not guaranteed')
- [T09_C-v1.3-c-r2_vs_C-v1.1-c-r2/21 r2] Parcel pick-up points are commonly paid a fee ('in many places a fee is paid for it'), unlabelled
- [T09_C-v1.3-c-r3_vs_C-v1.1-c-r3/12 r3] Hedged general claim: parcel/bill-payment points 'usually bring people in and pay a small fee per item'
- [T09_C-v1.3-c-r3_vs_C-v1.1-c-r3/12 r3] Hedged general claim: 'in a small town an empty unit is often worse for the landlord than a lower rent'
- [T09_C-v1.3-c-r3_vs_C-v1.1-c-r3/21 r3] Parcel/bill-payment points 'usually brings people in and pays a small fee per item' (hedged general claim, minor)
- [T09_C-v1.3-c-r3_vs_C-v1.1-c-r3/21 r3] 'in a small town an empty space is often worse for the landlord than lower rent' (hedged general claim, minor)

**T10**
- [T10_C-v1.3-c-r1_vs_C-v1.1-c-r1/12 r1] In most EU countries businesses can claim statutory late-payment interest and fixed compensation, often EUR 40 per invoice (external legal rule not in the task; accurate in substance and hedged, but presented as fact)
- [T10_C-v1.3-c-r1_vs_C-v1.1-c-r1/21 r1] EU late-payment rule: statutory interest and fixed compensation of 'often 40 EUR per invoice' between businesses in most EU countries (not in task; jurisdiction not given)
- [T10_C-v1.3-c-r2_vs_C-v1.1-c-r2/12 r2] In most EU countries late B2B payments carry statutory interest and fixed compensation (legal rule not in the task, stated as fact; accurate and hedged with 'check locally')
- [T10_C-v1.3-c-r2_vs_C-v1.1-c-r2/21 r2] EU-wide statutory late-payment interest and fixed compensation between companies stated as fact (accurate in substance, hedged with 'check locally', but not in the task)
- [T10_C-v1.3-c-r3_vs_C-v1.1-c-r3/12 r3] EU statutory late-payment interest between companies ('between companies, in most EU countries a late-payment penalty is also due by law') presented as fact, hedged with 'check your country'; not in the task
- [T10_C-v1.3-c-r3_vs_C-v1.1-c-r3/21 r3] Between companies in most EU countries a late-payment penalty is due by law (external legal rule stated as fact, hedged with 'check your country')

## Lowest-scoring judgments per task (file, slot, total)

- T01: T01_C-v1.3-c-r2_vs_C-v1.1-c-r2_12.md slot 2 = 86.0; T01_C-v1.3-c-r2_vs_C-v1.1-c-r2_21.md slot 1 = 87.0; T01_C-v1.3-c-r1_vs_C-v1.1-c-r1_12.md slot 2 = 89.0
- T02: T02_C-v1.3-c-r3_vs_C-v1.1-c-r3_21.md slot 1 = 86.0; T02_C-v1.3-c-r2_vs_C-v1.1-c-r2_12.md slot 2 = 87.0; T02_C-v1.3-c-r2_vs_C-v1.1-c-r2_21.md slot 1 = 87.0
- T03: T03_C-v1.3-c-r3_vs_C-v1.1-c-r3_21.md slot 1 = 81.0; T03_C-v1.3-c-r1_vs_C-v1.1-c-r1_21.md slot 1 = 82.0; T03_C-v1.3-c-r2_vs_C-v1.1-c-r2_21.md slot 1 = 83.0
- T04: T04_C-v1.3-c-r1_vs_C-v1.1-c-r1_21.md slot 1 = 59.0; T04_C-v1.3-c-r1_vs_C-v1.1-c-r1_12.md slot 2 = 62.0; T04_C-v1.3-c-r2_vs_C-v1.1-c-r2_12.md slot 2 = 62.0
- T05: T05_C-v1.3-c-r1_vs_C-v1.1-c-r1_12.md slot 2 = 89.0; T05_C-v1.3-c-r2_vs_C-v1.1-c-r2_12.md slot 2 = 89.0; T05_C-v1.3-c-r1_vs_C-v1.1-c-r1_21.md slot 1 = 90.0
- T06: T06_C-v1.3-c-r3_vs_C-v1.1-c-r3_12.md slot 2 = 85.0; T06_C-v1.3-c-r1_vs_C-v1.1-c-r1_21.md slot 1 = 88.0; T06_C-v1.3-c-r2_vs_C-v1.1-c-r2_21.md slot 1 = 88.0
- T07: T07_C-v1.3-c-r2_vs_C-v1.1-c-r2_12.md slot 2 = 71.0; T07_C-v1.3-c-r2_vs_C-v1.1-c-r2_21.md slot 1 = 72.0; T07_C-v1.3-c-r3_vs_C-v1.1-c-r3_12.md slot 2 = 83.0
- T08: T08_C-v1.3-c-r3_vs_C-v1.1-c-r3_12.md slot 2 = 79.0; T08_C-v1.3-c-r3_vs_C-v1.1-c-r3_21.md slot 1 = 82.0; T08_C-v1.3-c-r2_vs_C-v1.1-c-r2_12.md slot 2 = 88.0
- T09: T09_C-v1.3-c-r1_vs_C-v1.1-c-r1_12.md slot 2 = 74.0; T09_C-v1.3-c-r1_vs_C-v1.1-c-r1_21.md slot 1 = 85.0; T09_C-v1.3-c-r3_vs_C-v1.1-c-r3_12.md slot 2 = 86.0
- T10: T10_C-v1.3-c-r1_vs_C-v1.1-c-r1_21.md slot 1 = 78.0; T10_C-v1.3-c-r1_vs_C-v1.1-c-r1_12.md slot 2 = 80.0; T10_C-v1.3-c-r3_vs_C-v1.1-c-r3_21.md slot 1 = 81.0
