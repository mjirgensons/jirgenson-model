# Error analysis — iteration 1, condition C-v1.1-c

| task | n judgments | mean total | missed elements (share) | forbidden | hard-check fails | C1 | C2 | C3 | C4 | C5 | C6 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| T01 | 12 | 90.3 | — | — | — | 7.8 | 8.7 | 8.2 | 8.1 | 8.6 | 9.0 |
| T02 | 12 | 88.5 | — | — | H6 1/12 | 8.0 | 8.4 | 7.8 | 8.2 | 8.1 | 8.1 |
| T03 | 12 | 86.1 | M8 7/12 | — | — | 8.2 | 8.1 | 8.0 | 8.8 | 7.0 | 8.3 |
| T04 | 12 | 70.4 | M4 9/12, M8 8/12, M7 4/12 | F2 9/12 | H2 12/12, H1 8/12 | 7.8 | 7.7 | 7.4 | 6.2 | 7.0 | 8.0 |
| T05 | 12 | 90.4 | — | — | — | 7.3 | 8.2 | 8.3 | 8.4 | 9.0 | 9.1 |
| T06 | 12 | 87.9 | M4 2/12 | — | — | 8.2 | 8.1 | 7.2 | 8.5 | 8.2 | 8.7 |
| T07 | 12 | 84.2 | M7 4/12 | F2 4/12 | H1 4/12 | 7.2 | 8.2 | 7.8 | 7.3 | 8.0 | 8.8 |
| T08 | 12 | 90.1 | M7 1/12 | — | — | 8.1 | 8.4 | 8.4 | 8.0 | 8.8 | 8.8 |
| T09 | 12 | 87.6 | M5 4/12, M6 1/12 | — | — | 7.2 | 8.3 | 8.5 | 8.3 | 8.8 | 8.4 |
| T10 | 12 | 86.6 | M6 3/12, M1 2/12 | — | — | 8.0 | 7.7 | 7.8 | 8.1 | 8.8 | 8.2 |

## Invented facts flagged by the judge (verbatim)

**T01**
- [T01_C-v1.1-c-r1_vs_A-r1/12 r1] Losing the mechanic before April would cost you the season (unlabelled consequence, minor)
- [T01_C-v1.1-c-r1_vs_A-r1/12 r1] In many countries a tax/VAT instalment falls in winter (general claim, hedged, used as a check, minor)
- [T01_C-v1.1-c-r1_vs_C-v1.0-r1/12 r1] 'in many countries' a tax or VAT instalment falls in winter (unsourced general claim stated as fact; minor, drives no numbers)
- [T01_C-v1.1-c-r1_vs_C-v1.0-r1/21 r1] 'In many countries' a tax or VAT instalment falls in winter: a general rule not in the task, stated as fact (hedged, used only to prompt a check)
- [T01_C-v1.1-c-r2_vs_A-r2/12 r2] October is usually weaker (than the season average)
- [T01_C-v1.1-c-r2_vs_A-r2/12 r2] In most EU countries cutting hours needs the employee's agreement (legal rule stated as fact, softened by 'check yours')
- [T01_C-v1.1-c-r2_vs_A-r2/12 r2] Many dealers allow payment in spring
- [T01_C-v1.1-c-r2_vs_A-r2/12 r2] The first season is usually weaker
- [T01_C-v1.1-c-r2_vs_A-r2/21 r2] October is usually weaker (unlabelled generalisation)
- [T01_C-v1.1-c-r2_vs_A-r2/21 r2] many dealers allow payment in spring (unlabelled generalisation)
- [T01_C-v1.1-c-r2_vs_A-r2/21 r2] the first season is usually weaker (unlabelled generalisation)
- [T01_C-v1.1-c-r2_vs_C-v1.0-r2/12 r2] October is usually weaker (general claim, not labelled as assumption)
- [T01_C-v1.1-c-r2_vs_C-v1.0-r2/12 r2] many dealers allow payment in spring
- [T01_C-v1.1-c-r2_vs_C-v1.0-r2/12 r2] in most EU countries cutting hours needs the employee's agreement (softened by 'check yours')
- [T01_C-v1.1-c-r2_vs_C-v1.0-r2/12 r2] the first season is usually weaker
- [T01_C-v1.1-c-r2_vs_C-v1.0-r2/21 r2] October is usually weaker (unlabelled general claim)
- [T01_C-v1.1-c-r2_vs_C-v1.0-r2/21 r2] many dealers allow payment in spring
- [T01_C-v1.1-c-r2_vs_C-v1.0-r2/21 r2] in most EU countries cutting the mechanic's hours needs his agreement (softened by 'check yours')
- [T01_C-v1.1-c-r2_vs_C-v1.0-r2/21 r2] the first season is usually weaker

**T02**
- [T02_C-v1.1-c-r2_vs_A-r2/12 r2] A few hours' grace is 'often allowed for a booked repair' (general claim about inspector practice, hedged with 'check yours')
- [T02_C-v1.1-c-r2_vs_A-r2/21 r2] A few hours' grace is 'often allowed for a booked repair' (unsupported practice claim, softened by 'check yours')
- [T02_C-v1.1-c-r2_vs_A-r2/21 r2] 'In 4 days ... EUR 900 left' silently assumes the EUR 1,400 balance is deferred, contradicting the base-case EUR 1,700 shortfall (unlabelled assumption)
- [T02_C-v1.1-c-r2_vs_C-v1.0-r2/12 r2] Inspector grace of a few hours 'often allowed for a booked repair' (hedged general claim, not in task)
- [T02_C-v1.1-c-r2_vs_C-v1.0-r2/12 r2] Discard threshold 'usually past 2 to 4 hours' (hedged general food-safety rule, not in task)
- [T02_C-v1.1-c-r2_vs_C-v1.0-r2/21 r2] A few hours' grace is 'often allowed for a booked repair' (hedged only with 'check yours')
- [T02_C-v1.1-c-r2_vs_C-v1.0-r2/21 r2] Discard threshold 'usually past 2 to 4 hours' at 9C (outside rule, hedged with 'check local rules')
- [T02_C-v1.1-c-r3_vs_A-r3/12 r3] Food above about 8°C for more than a few hours usually has to be thrown away (hedged threshold not in task, flagged 'check your local rule')

**T03**
- [T03_C-v1.1-c-r2_vs_A-r2/21 r2] tax offices are often less flexible with someone they have not heard from (hedged general claim)
- [T03_C-v1.1-c-r2_vs_A-r2/21 r2] in most countries tax offices will consider an instalment plan if you ask first (hedged general claim)
- [T03_C-v1.1-c-r2_vs_C-v1.0-r2/21 r2] 'with a new studio taking some of yours' (member losses stated as fact; the response later notes none reported; minor)
- [T03_C-v1.1-c-r3_vs_C-v1.0-r3/12 r3] 'more members will push it [complaints] up' stated as fact (minor, general, does not change advice)

**T04**
- [T04_C-v1.1-c-r1_vs_A-r1/12 r1] Companies often keep human review for legal or customer-facing texts because raw machine output still has errors that matter there (general industry claim stated as fact)
- [T04_C-v1.1-c-r1_vs_A-r1/21 r1] General industry claim that companies often keep human review for legal or customer-facing texts because raw machine output still has errors that matter there (hedged with 'it is not certain'; not from the task)
- [T04_C-v1.1-c-r1_vs_C-v1.0-r1/12 r1] Companies often keep human review for legal or customer-facing texts because raw machine output still has errors that matter there (general industry claim presented as fact)
- [T04_C-v1.1-c-r1_vs_C-v1.0-r1/21 r1] General claim partly hedged: 'Companies often keep that [human checking] for legal or customer-facing texts, because raw machine output still has errors that matter there'
- [T04_C-v1.1-c-r2_vs_A-r2/12 r2] routine, repetitive text is often where companies try AI tools first (unlabelled industry generalisation)
- [T04_C-v1.1-c-r2_vs_A-r2/12 r2] companies often still want a human check for legal or customer-facing text, usually at a lower rate per word (unlabelled industry generalisation)
- [T04_C-v1.1-c-r2_vs_A-r2/21 r2] Routine, repetitive text is often where companies try AI tools first
- [T04_C-v1.1-c-r2_vs_A-r2/21 r2] Companies often still want a human check for legal or customer-facing text, usually at a lower rate per word
- [T04_C-v1.1-c-r2_vs_C-v1.0-r2/12 r2] Routine, repetitive text is often where companies try AI tools first (unlabelled general claim)
- [T04_C-v1.1-c-r2_vs_C-v1.0-r2/12 r2] Companies often still want a human check for legal or customer-facing text, usually at a lower rate per word (unlabelled market claim)
- [T04_C-v1.1-c-r2_vs_C-v1.0-r2/21 r2] 'routine, repetitive text is often where companies try AI tools first' stated as fact
- [T04_C-v1.1-c-r2_vs_C-v1.0-r2/21 r2] 'Companies often still want a human check for legal or customer-facing text, usually at a lower rate per word' stated as fact

**T05**
- [T05_C-v1.1-c-r1_vs_A-r1/12 r1] In most EU countries a cancellation fee is allowed if the client agrees when booking (hedged with 'check yours')
- [T05_C-v1.1-c-r1_vs_A-r1/21 r1] In most EU countries a cancellation fee is allowed if the client agrees when booking (legal rule not in task; hedged with 'check yours')
- [T05_C-v1.1-c-r1_vs_C-v1.0-r1/12 r1] 'In most EU countries a cancellation fee is allowed if the client agrees when booking' — legal rule not in the task, presented as fact (hedged with 'check yours')
- [T05_C-v1.1-c-r1_vs_C-v1.0-r1/21 r1] In most EU countries a cancellation fee is allowed if the client agrees when booking (outside legal rule stated as fact, hedged with 'check yours')
- [T05_C-v1.1-c-r1_vs_C-v1.0-r1/21 r1] 60 hours is already your limit (person's limit asserted as fact)
- [T05_C-v1.1-c-r2_vs_A-r2/12 r2] In most EU countries a late-cancellation fee is allowed if announced in advance (hedged with 'check yours')
- [T05_C-v1.1-c-r2_vs_A-r2/21 r2] In most EU countries a cancellation fee is allowed if announced in advance (legal claim not in task, hedged with 'check yours')
- [T05_C-v1.1-c-r2_vs_A-r2/21 r2] Booking apps can send reminders (minor general claim)
- [T05_C-v1.1-c-r2_vs_C-v1.0-r2/12 r2] 'In most EU countries this [cancellation fee] is allowed if announced in advance' — legal rule not in task (hedged with 'check yours')
- [T05_C-v1.1-c-r2_vs_C-v1.0-r2/21 r2] 'In most EU countries this [late-cancellation fee] is allowed if announced in advance' — legal rule not in the task, presented as fact though hedged with 'check yours'
- [T05_C-v1.1-c-r3_vs_A-r3/12 r3] In most EU countries no-show charges are allowed if agreed at booking (hedged: 'check yours')
- [T05_C-v1.1-c-r3_vs_A-r3/12 r3] Many self-employed have little sick pay (hedged: 'check yours')
- [T05_C-v1.1-c-r3_vs_A-r3/21 r3] In most EU countries no-show charges are allowed if agreed at booking (hedged with 'check yours')
- [T05_C-v1.1-c-r3_vs_A-r3/21 r3] Many self-employed have little sick pay (hedged with 'check yours')
- [T05_C-v1.1-c-r3_vs_C-v1.0-r3/12 r3] In most EU countries a no-show charge/deposit is allowed if agreed at booking (softened only by 'check yours')
- [T05_C-v1.1-c-r3_vs_C-v1.0-r3/12 r3] Many self-employed have little sick pay (softened only by 'check yours')
- [T05_C-v1.1-c-r3_vs_C-v1.0-r3/21 r3] In most EU countries no-show charges/deposits are allowed if agreed at booking (legal rule stated as fact, hedged with 'check yours')
- [T05_C-v1.1-c-r3_vs_C-v1.0-r3/21 r3] Many self-employed have little sick pay (general claim stated as fact, hedged)

**T06**
- [T06_C-v1.1-c-r2_vs_C-v1.0-r2/21 r2] 'A new salon usually takes months to fill its diary' stated as a general rule without label (qualitative, minor)
- [T06_C-v1.1-c-r3_vs_A-r3/12 r3] Hire the second technician when the first is booked about 80% for four weeks, presented as a 'usual rule of thumb' (heuristic not in the task)
- [T06_C-v1.1-c-r3_vs_C-v1.0-r3/12 r3] 80% booked for four weeks presented as the 'usual rule of thumb' (industry norm not in the task)
- [T06_C-v1.1-c-r3_vs_C-v1.0-r3/21 r3] 80% booking threshold presented as the 'usual rule of thumb' (unsourced common-practice claim)

**T07**
- [T07_C-v1.1-c-r1_vs_A-r1/21 r1] As a minor you will often need a parent to buy or insure it (rule claim not in task, hedged)
- [T07_C-v1.1-c-r1_vs_C-v1.0-r1/12 r1] as a minor you will often need a parent to buy or insure it
- [T07_C-v1.1-c-r1_vs_C-v1.0-r1/12 r1] helmet and lock are usually extra
- [T07_C-v1.1-c-r1_vs_C-v1.0-r1/21 r1] Helmet and lock are 'usually extra' (not in task, stated as fact)
- [T07_C-v1.1-c-r1_vs_C-v1.0-r1/21 r1] As a minor you will often need a parent to buy or insure it; rules differ by country (general rule not in task, stated as fact)
- [T07_C-v1.1-c-r2_vs_A-r2/12 r2] In many EU countries the minimum e-scooter age is 14 to 16 and some places require insurance (rule not in task, stated as fact)
- [T07_C-v1.1-c-r2_vs_A-r2/12 r2] A helmet usually costs €30 to €50 (price not in task)
- [T07_C-v1.1-c-r2_vs_A-r2/21 r2] In many EU countries the e-scooter minimum age is 14 to 16 and some places require insurance (external rule presented as fact)
- [T07_C-v1.1-c-r2_vs_A-r2/21 r2] A helmet usually costs EUR 30 to 50 (external price)
- [T07_C-v1.1-c-r2_vs_C-v1.0-r2/12 r2] In many EU countries the minimum e-scooter age is 14 to 16 and some places require insurance (stated as fact)
- [T07_C-v1.1-c-r2_vs_C-v1.0-r2/12 r2] A helmet usually costs another EUR30 to EUR50 (stated as fact)
- [T07_C-v1.1-c-r2_vs_C-v1.0-r2/21 r2] In many EU countries the minimum e-scooter age is 14 to 16 and some places require insurance (stated as fact)
- [T07_C-v1.1-c-r2_vs_C-v1.0-r2/21 r2] A helmet usually costs another €30 to €50 (stated as fact, not labelled as an assumption)
- [T07_C-v1.1-c-r3_vs_A-r3/12 r3] 'in most EU countries e-scooters have age, speed and sometimes insurance or helmet rules' (general rule stated as fact, hedged with 'check yours')
- [T07_C-v1.1-c-r3_vs_A-r3/12 r3] Unlabelled estimate that €30 covers helmet, lock and cushion
- [T07_C-v1.1-c-r3_vs_A-r3/21 r3] '€30 extra for a helmet and a lock', unlabelled cost assumption
- [T07_C-v1.1-c-r3_vs_A-r3/21 r3] 'In most EU countries e-scooters have age, speed and sometimes insurance or helmet rules', outside the task, hedged with 'check yours'
- [T07_C-v1.1-c-r3_vs_C-v1.0-r3/12 r3] €30 extra for a helmet and a lock (plus cushion) - unlabelled cost figure
- [T07_C-v1.1-c-r3_vs_C-v1.0-r3/12 r3] in most EU countries e-scooters have age, speed and sometimes insurance or helmet rules - external rule stated as fact
- [T07_C-v1.1-c-r3_vs_C-v1.0-r3/21 r3] in most EU countries e-scooters have age, speed and sometimes insurance or helmet rules (regulatory claim presented as fact, not in task)

**T08**
- [T08_C-v1.1-c-r1_vs_A-r1/21 r1] In most EU countries late payment can carry interest (legal rule not in task; hedged with 'can' and 'check yours')
- [T08_C-v1.1-c-r2_vs_A-r2/12 r2] 'in many countries VAT is due on the invoice date even if unpaid' (accurate general rule, hedged and offered as a check; minor)
- [T08_C-v1.1-c-r2_vs_A-r2/21 r2] 'In many countries VAT is due on the invoice date even if unpaid' (external rule; accurate and hedged, minor)
- [T08_C-v1.1-c-r2_vs_C-v1.0-r2/12 r2] 'in many countries VAT is due on the invoice date even if unpaid' (general rule, hedged, framed as a check)
- [T08_C-v1.1-c-r2_vs_C-v1.0-r2/12 r2] 'banks usually lend before the balance is low' (generalisation stated as fact)
- [T08_C-v1.1-c-r2_vs_C-v1.0-r2/21 r2] VAT due on invoice date even if unpaid in many countries (external rule, hedged as something to check)
- [T08_C-v1.1-c-r2_vs_C-v1.0-r2/21 r2] Banks usually lend before the balance is low (general claim)
- [T08_C-v1.1-c-r3_vs_A-r3/12 r3] EU late-payment rule: fixed fee of at least EUR 40 per invoice (external rule, hedged 'check yours')
- [T08_C-v1.1-c-r3_vs_A-r3/21 r3] EU late-payment rules give a fixed fee of at least EUR 40 per invoice (external figure, hedged 'check yours')
- [T08_C-v1.1-c-r3_vs_C-v1.0-r3/12 r3] EU late-payment rule: late-payment interest plus fixed fee of at least EUR 40 per invoice (accurate, hedged with 'check yours', but not in the task)
- [T08_C-v1.1-c-r3_vs_C-v1.0-r3/21 r3] EU late-payment rule: fixed fee of at least EUR 40 per invoice (external legal rule, accurate, hedged with 'check yours')

**T09**
- [T09_C-v1.1-c-r1_vs_A-r1/12 r1] 'many leases require 1–3 months' notice' (general lease notice-period claim, hedged with 'check')
- [T09_C-v1.1-c-r1_vs_A-r1/21 r1] Many leases require 1-3 months' notice ('many leases require 1–3 months' notice'), a general claim not in task (hedged, with 'check')
- [T09_C-v1.1-c-r1_vs_A-r1/21 r1] The location would be hard to regain after leaving ('a spot that is hard to get back'), an unsupported assertion
- [T09_C-v1.1-c-r1_vs_C-v1.0-r1/12 r1] 'many leases require 1–3 months' notice' – general claim about lease notice periods, not in the task
- [T09_C-v1.1-c-r1_vs_C-v1.0-r1/12 r1] 'a spot that is hard to get back' – unsupported claim that the kiosk location is hard to regain
- [T09_C-v1.1-c-r1_vs_C-v1.0-r1/12 r1] 'Where there are fewer residents, it is usually not easier for the landlord to find another tenant' – general claim about the landlord's market
- [T09_C-v1.1-c-r1_vs_C-v1.0-r1/21 r1] Leaving loses a location that is hard to regain (unsupported; conflicts with its own claim that landlords in shrinking towns struggle to find tenants)
- [T09_C-v1.1-c-r2_vs_A-r2/12 r2] In a shrinking town landlords usually give way (hedged general rule, 'not guaranteed')
- [T09_C-v1.1-c-r2_vs_A-r2/12 r2] In many places parcel handout points are paid a fee (general claim not in task)
- [T09_C-v1.1-c-r2_vs_A-r2/21 r2] In a shrinking town landlords usually concede because empty premises earn nothing (general claim, softened by 'not guaranteed')
- [T09_C-v1.1-c-r2_vs_C-v1.0-r2/12 r2] 'In a shrinking town landlords usually give way, because empty premises bring no income' - general rule stated as typical (hedged 'not guaranteed', not labelled as an assumption)
- [T09_C-v1.1-c-r2_vs_C-v1.0-r2/21 r2] 'In a shrinking town landlords usually give way' - general claim about landlord behaviour presented as typical (hedged with 'not guaranteed')
- [T09_C-v1.1-c-r3_vs_A-r3/21 r3] Unlabelled assumption that after a forced exit from a multi-year lease the remaining rent would be covered by (i.e. consume) the EUR 4,000 reserve (rent is unknown)
- [T09_C-v1.1-c-r3_vs_C-v1.0-r3/12 r3] Unlabelled generalisation that in a small town an empty unit is often worse for the landlord than a lower rent
- [T09_C-v1.1-c-r3_vs_C-v1.0-r3/21 r3] Unlabelled generalisation: 'in a small town an empty space is often worse for the landlord than lower rent' (hedged with 'often', minor)

**T10**
- [T10_C-v1.1-c-r1_vs_A-r1/12 r1] EU B2B statutory late-payment interest and fixed compensation 'often €40 per invoice' (external rule, accurate, hedged with 'check your country and contract'; the person's country is not given)
- [T10_C-v1.1-c-r1_vs_A-r1/12 r1] Client 'has not answered emails for 30 days' (task says the invoices are 30 days late; duration of silence not stated)
- [T10_C-v1.1-c-r1_vs_A-r1/21 r1] the phone is the only chance to get the money before the rent (overstated claim presented as fact)
- [T10_C-v1.1-c-r1_vs_C-v1.0-r1/12 r1] EU late-payment rule: statutory interest and fixed compensation 'often 40 EUR per invoice' in most EU countries (hedged, with instruction to check country and contract; minor)
- [T10_C-v1.1-c-r2_vs_A-r2/21 r2] 'In most EU countries statutory interest and fixed compensation apply to B2B late payment' (accurate external rule, hedged with 'check for your country', no figures)
- [T10_C-v1.1-c-r2_vs_C-v1.0-r2/12 r2] EU-wide B2B late-payment statutory interest plus fixed compensation, stated as fact (hedged with 'check this for your country'; EU location assumed, not labelled)
- [T10_C-v1.1-c-r3_vs_A-r3/12 r3] Legal rule stated as fact: late-payment interest between companies is due by law in most EU countries (hedged with 'check your country'; not in task, assumes EU jurisdiction)
- [T10_C-v1.1-c-r3_vs_A-r3/21 r3] Between companies in most EU countries late-payment penalty is due by law (legal rule not in task; hedged with 'check your country')
- [T10_C-v1.1-c-r3_vs_C-v1.0-r3/12 r3] Statutory late-payment penalty between companies in most EU countries (external legal rule, accurate, hedged with 'check your country')
- [T10_C-v1.1-c-r3_vs_C-v1.0-r3/21 r3] In most EU countries a statutory late-payment penalty applies between companies (external rule, hedged with 'check your country')

## Lowest-scoring judgments per task (file, slot, total)

- T01: T01_C-v1.1-c-r1_vs_C-v1.0-r1_21.md slot 2 = 87.0; T01_C-v1.1-c-r1_vs_C-v1.0-r1_12.md slot 1 = 88.0; T01_C-v1.1-c-r2_vs_A-r2_12.md slot 1 = 89.0
- T02: T02_C-v1.1-c-r2_vs_A-r2_21.md slot 2 = 83.0; T02_C-v1.1-c-r2_vs_C-v1.0-r2_21.md slot 2 = 85.0; T02_C-v1.1-c-r3_vs_C-v1.0-r3_21.md slot 2 = 86.0
- T03: T03_C-v1.1-c-r1_vs_C-v1.0-r1_12.md slot 1 = 83.0; T03_C-v1.1-c-r3_vs_A-r3_12.md slot 1 = 83.0; T03_C-v1.1-c-r1_vs_C-v1.0-r1_21.md slot 2 = 84.0
- T04: T04_C-v1.1-c-r1_vs_C-v1.0-r1_12.md slot 1 = 59.0; T04_C-v1.1-c-r1_vs_C-v1.0-r1_21.md slot 2 = 61.0; T04_C-v1.1-c-r2_vs_C-v1.0-r2_12.md slot 1 = 64.0
- T05: T05_C-v1.1-c-r2_vs_A-r2_21.md slot 2 = 88.0; T05_C-v1.1-c-r3_vs_C-v1.0-r3_21.md slot 2 = 88.0; T05_C-v1.1-c-r1_vs_A-r1_21.md slot 2 = 90.0
- T06: T06_C-v1.1-c-r2_vs_C-v1.0-r2_12.md slot 1 = 81.0; T06_C-v1.1-c-r1_vs_C-v1.0-r1_12.md slot 1 = 86.0; T06_C-v1.1-c-r2_vs_A-r2_21.md slot 2 = 87.0
- T07: T07_C-v1.1-c-r2_vs_C-v1.0-r2_12.md slot 1 = 73.0; T07_C-v1.1-c-r2_vs_C-v1.0-r2_21.md slot 2 = 73.0; T07_C-v1.1-c-r2_vs_A-r2_12.md slot 1 = 77.0
- T08: T08_C-v1.1-c-r3_vs_C-v1.0-r3_21.md slot 2 = 81.0; T08_C-v1.1-c-r3_vs_C-v1.0-r3_12.md slot 1 = 87.0; T08_C-v1.1-c-r3_vs_A-r3_21.md slot 2 = 88.0
- T09: T09_C-v1.1-c-r1_vs_C-v1.0-r1_21.md slot 2 = 74.0; T09_C-v1.1-c-r1_vs_C-v1.0-r1_12.md slot 1 = 77.0; T09_C-v1.1-c-r1_vs_A-r1_21.md slot 2 = 82.0
- T10: T10_C-v1.1-c-r3_vs_C-v1.0-r3_12.md slot 1 = 79.0; T10_C-v1.1-c-r3_vs_C-v1.0-r3_21.md slot 2 = 82.0; T10_C-v1.1-c-r1_vs_A-r1_12.md slot 1 = 83.0
