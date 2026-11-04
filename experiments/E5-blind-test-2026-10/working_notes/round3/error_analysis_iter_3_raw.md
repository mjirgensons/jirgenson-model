# Error analysis — iteration 3, condition C-v1.3-c

| task | n judgments | mean total | missed elements (share) | forbidden | hard-check fails | C1 | C2 | C3 | C4 | C5 | C6 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| T01 | 12 | 91.7 | — | — | — | 8.4 | 9.0 | 7.8 | 8.4 | 9.0 | 9.0 |
| T02 | 12 | 88.9 | M4 4/12 | — | — | 8.8 | 7.9 | 7.7 | 8.9 | 8.3 | 8.9 |
| T03 | 12 | 88.2 | M1 2/12 | — | — | 8.8 | 8.2 | 7.8 | 8.2 | 7.3 | 8.5 |
| T04 | 12 | 83.1 | M7 12/12 | — | — | 8.4 | 7.5 | 7.6 | 9.0 | 7.4 | 8.2 |
| T05 | 12 | 91.7 | — | — | — | 8.6 | 8.0 | 8.8 | 8.6 | 8.8 | 8.9 |
| T06 | 12 | 90.1 | — | — | — | 8.5 | 8.2 | 7.8 | 8.2 | 8.4 | 8.9 |
| T07 | 12 | 90.3 | — | — | — | 8.6 | 8.3 | 8.1 | 8.2 | 8.3 | 8.8 |
| T08 | 12 | 88.7 | M3 2/12, M4 2/12 | — | — | 8.0 | 7.9 | 8.4 | 8.5 | 8.9 | 8.6 |
| T09 | 12 | 86.8 | M5 5/12, M7 2/12, M3 1/12 | — | — | 8.1 | 7.9 | 8.2 | 8.7 | 8.6 | 8.6 |
| T10 | 12 | 89.5 | M6 2/12 | — | — | 8.8 | 7.8 | 7.8 | 8.9 | 8.2 | 8.7 |

## Invented facts flagged by the judge (verbatim)

**T03**
- [T03_C-v1.3-c-r1_vs_A-r1/21 r1] Unhedged rule of thumb 'three to five [goals] are enough for a year' (minor, does not change the advice)

**T04**
- [T04_C-v1.3-c-r3_vs_A-r3/21 r3] EUR 1,950 a month 'cannot carry an employee' stated as fact although costs and salary are not given
- [T04_C-v1.3-c-r3_vs_C-v1.1-c-r3/12 r3] '€1,950 a month cannot carry an employee' stated as fact although employee pay and cost base are not given

**T07**
- [T07_C-v1.3-c-r2_vs_A-r2/12 r2] Borderline: 'one more evening fixes it' implies at least EUR 10 per babysitting evening, not given in the task and not labelled

**T08**
- [T08_C-v1.3-c-r3_vs_A-r3/12 r3] Unlabelled assumption that stopping work for the biggest customer would not reduce costs (materials would partly fall)
- [T08_C-v1.3-c-r3_vs_A-r3/21 r3] 'your costs would not fall' if work for the big customer stopped, stated as fact (materials would fall; minor unlabelled assumption)
- [T08_C-v1.3-c-r3_vs_C-v1.1-c-r3/12 r3] 'your costs would not fall' if work for the biggest customer stopped — unlabelled assumption about cost behaviour (materials are partly variable)

**T09**
- [T09_C-v1.3-c-r1_vs_A-r1/21 r1] Profit described as 'before taxes' - task says only 'before my pay' (minor unlabelled gloss)
- [T09_C-v1.3-c-r3_vs_A-r3/21 r3] Profit assumed proportional to turnover at ~16% net margin (2027 profit 4,900; plan 5,100-5,500; test payback ~3,100) - unlabelled, ignores fixed costs such as rent and uses net instead of gross margin
- [T09_C-v1.3-c-r3_vs_C-v1.1-c-r3/12 r3] Soft unsupported causal attribution: 'marketing can affect the other half [of the decline]' (hedged with 'can'; no basis in the task that the non-population half of the decline is marketing-addressable)
- [T09_C-v1.3-c-r3_vs_C-v1.1-c-r3/21 r3] Causal split 'about half of the decline may simply be fewer people; the other half marketing can touch' (unsupported attribution of the non-population half of the decline to marketing-addressable causes)

**T10**
- [T10_C-v1.3-c-r2_vs_A-r2/12 r2] Calendar dates '23 October' / '23 November' assume today's date, which is not in the task (unlabelled assumption, minor)
- [T10_C-v1.3-c-r2_vs_A-r2/21 r2] Specific calendar dates (23 October rent day, 23 November, 30 October) not in the task; they rest on an unstated assumption about today's date

## Lowest-scoring judgments per task (file, slot, total)

- T01: T01_C-v1.3-c-r2_vs_A-r2_12.md slot 1 = 90.0; T01_C-v1.3-c-r2_vs_A-r2_21.md slot 2 = 91.0; T01_C-v1.3-c-r2_vs_C-v1.1-c-r2_12.md slot 1 = 91.0
- T02: T02_C-v1.3-c-r2_vs_A-r2_21.md slot 2 = 82.0; T02_C-v1.3-c-r2_vs_C-v1.1-c-r2_12.md slot 1 = 84.0; T02_C-v1.3-c-r2_vs_A-r2_12.md slot 1 = 86.0
- T03: T03_C-v1.3-c-r2_vs_C-v1.1-c-r2_12.md slot 1 = 83.0; T03_C-v1.3-c-r2_vs_C-v1.1-c-r2_21.md slot 2 = 85.0; T03_C-v1.3-c-r1_vs_A-r1_21.md slot 2 = 86.0
- T04: T04_C-v1.3-c-r3_vs_C-v1.1-c-r3_21.md slot 2 = 80.0; T04_C-v1.3-c-r1_vs_C-v1.1-c-r1_21.md slot 2 = 81.0; T04_C-v1.3-c-r1_vs_C-v1.1-c-r1_12.md slot 1 = 82.0
- T05: T05_C-v1.3-c-r1_vs_C-v1.1-c-r1_12.md slot 1 = 91.0; T05_C-v1.3-c-r1_vs_C-v1.1-c-r1_21.md slot 2 = 91.0; T05_C-v1.3-c-r2_vs_A-r2_12.md slot 1 = 91.0
- T06: T06_C-v1.3-c-r2_vs_A-r2_12.md slot 1 = 87.0; T06_C-v1.3-c-r3_vs_C-v1.1-c-r3_12.md slot 1 = 87.0; T06_C-v1.3-c-r2_vs_C-v1.1-c-r2_12.md slot 1 = 88.0
- T07: T07_C-v1.3-c-r1_vs_A-r1_21.md slot 2 = 89.0; T07_C-v1.3-c-r2_vs_A-r2_21.md slot 2 = 89.0; T07_C-v1.3-c-r3_vs_A-r3_21.md slot 2 = 89.0
- T08: T08_C-v1.3-c-r3_vs_C-v1.1-c-r3_12.md slot 1 = 80.0; T08_C-v1.3-c-r3_vs_C-v1.1-c-r3_21.md slot 2 = 82.0; T08_C-v1.3-c-r2_vs_C-v1.1-c-r2_21.md slot 2 = 85.0
- T09: T09_C-v1.3-c-r3_vs_C-v1.1-c-r3_21.md slot 2 = 75.0; T09_C-v1.3-c-r1_vs_C-v1.1-c-r1_12.md slot 1 = 80.0; T09_C-v1.3-c-r3_vs_C-v1.1-c-r3_12.md slot 1 = 83.0
- T10: T10_C-v1.3-c-r3_vs_C-v1.1-c-r3_21.md slot 2 = 81.0; T10_C-v1.3-c-r3_vs_C-v1.1-c-r3_12.md slot 1 = 82.0; T10_C-v1.3-c-r2_vs_A-r2_12.md slot 1 = 89.0
