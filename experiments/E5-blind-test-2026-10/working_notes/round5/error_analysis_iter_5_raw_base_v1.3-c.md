# Error analysis — iteration 5, condition C-v1.3-c

| task | n judgments | mean total | missed elements (share) | forbidden | hard-check fails | C1 | C2 | C3 | C4 | C5 | C6 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| T01 | 6 | 91.0 | — | — | — | 8.5 | 8.8 | 7.5 | 8.5 | 8.8 | 8.8 |
| T02 | 6 | 87.8 | M4 2/6 | — | — | 8.3 | 8.0 | 7.7 | 8.8 | 8.3 | 8.3 |
| T03 | 6 | 87.5 | — | — | — | 8.8 | 8.2 | 7.0 | 8.3 | 6.7 | 8.5 |
| T04 | 6 | 80.8 | M7 6/6 | — | — | 8.0 | 7.2 | 7.3 | 8.7 | 7.0 | 7.7 |
| T05 | 6 | 91.5 | — | — | — | 8.2 | 8.0 | 8.5 | 8.8 | 9.0 | 9.0 |
| T06 | 6 | 90.2 | — | — | — | 9.0 | 7.8 | 7.5 | 8.3 | 8.5 | 9.0 |
| T07 | 6 | 90.2 | — | — | — | 8.5 | 8.2 | 7.8 | 8.5 | 8.2 | 9.0 |
| T08 | 6 | 84.2 | M1 2/6, M3 2/6, M4 2/6 | — | — | 7.5 | 7.8 | 8.0 | 8.8 | 8.7 | 8.3 |
| T09 | 6 | 83.2 | M5 6/6 | — | — | 7.3 | 7.7 | 8.3 | 8.7 | 8.0 | 8.2 |
| T10 | 6 | 84.2 | M1 2/6, M6 2/6 | F4 1/6 | — | 8.2 | 7.3 | 7.5 | 8.5 | 8.0 | 8.3 |

## Invented facts flagged by the judge (verbatim)

**T02**
- [T02_C-v1.5-c-r2_vs_C-v1.3-c-r2/21 r2] EUR 1,400 balance stated as falling due at the repair (timing not in task; unlabelled assumption, minor, matches key's own assumption)

**T04**
- [T04_C-v1.5-c-r3_vs_C-v1.3-c-r3/12 r3] EUR 1,950 a month 'cannot carry an employee' (costs not given, stated as fact)
- [T04_C-v1.5-c-r3_vs_C-v1.3-c-r3/12 r3] 'you found out early, and that gives you time to act' (leaving date unknown)
- [T04_C-v1.5-c-r3_vs_C-v1.3-c-r3/21 r3] States as fact that about EUR 1,950 a month 'cannot carry an employee' - no cost or salary data in the task, unlabelled

**T07**
- [T07_C-v1.5-c-r1_vs_C-v1.3-c-r1/21 r1] 'a bought ticket can't be undone' stated as fact (refund rule not in task; minor)
- [T07_C-v1.5-c-r2_vs_C-v1.3-c-r2/12 r2] 'one more evening fixes it' assumes one babysitting evening earns at least EUR 10 (not in task, unlabelled; minor)

**T08**
- [T08_C-v1.5-c-r3_vs_C-v1.3-c-r3/12 r3] Unlabelled claim that 'your costs would not fall' if work for the biggest customer stopped (materials are variable in a print shop)
- [T08_C-v1.5-c-r3_vs_C-v1.3-c-r3/21 r3] Unlabelled assumption that costs would not fall if work for the biggest customer stopped ('your costs would not fall')

**T09**
- [T09_C-v1.5-c-r2_vs_C-v1.3-c-r2/12 r2] Calendar dates 'around 17 June 2027' (lease end) and '26 October' (start) rest on an unstated current date and are presented as fact (minor; advice unchanged)
- [T09_C-v1.5-c-r2_vs_C-v1.3-c-r2/21 r2] Lease end stated as 'around 17 June 2027' - precise calendar date resting on an unstated assumed current date (minor)
- [T09_C-v1.5-c-r3_vs_C-v1.3-c-r3/12 r3] Exact lease-end date 'around 17 June 2027' (calendar date not in the task; derived from an unstated current date)

**T10**
- [T10_C-v1.5-c-r2_vs_C-v1.3-c-r2/12 r2] Calendar dates '23 October' (rent date), '30 October' and '23 November' stated as fact; the task gives no date, only 'in 6 days'
- [T10_C-v1.5-c-r2_vs_C-v1.3-c-r2/21 r2] Specific calendar dates not in the task presented as fact (rent on 23 October, next rent 23 November, deadline 30 October) without labelling the assumed current date

## Lowest-scoring judgments per task (file, slot, total)

- T01: T01_C-v1.5-c-r3_vs_C-v1.3-c-r3_12.md slot 2 = 89.0; T01_C-v1.5-c-r2_vs_C-v1.3-c-r2_12.md slot 2 = 90.0; T01_C-v1.5-c-r3_vs_C-v1.3-c-r3_21.md slot 1 = 90.0
- T02: T02_C-v1.5-c-r2_vs_C-v1.3-c-r2_21.md slot 1 = 80.0; T02_C-v1.5-c-r2_vs_C-v1.3-c-r2_12.md slot 2 = 84.0; T02_C-v1.5-c-r1_vs_C-v1.3-c-r1_12.md slot 2 = 90.0
- T03: T03_C-v1.5-c-r2_vs_C-v1.3-c-r2_21.md slot 1 = 86.0; T03_C-v1.5-c-r2_vs_C-v1.3-c-r2_12.md slot 2 = 87.0; T03_C-v1.5-c-r3_vs_C-v1.3-c-r3_21.md slot 1 = 87.0
- T04: T04_C-v1.5-c-r3_vs_C-v1.3-c-r3_21.md slot 1 = 75.0; T04_C-v1.5-c-r3_vs_C-v1.3-c-r3_12.md slot 2 = 77.0; T04_C-v1.5-c-r1_vs_C-v1.3-c-r1_12.md slot 2 = 83.0
- T05: T05_C-v1.5-c-r2_vs_C-v1.3-c-r2_21.md slot 1 = 90.0; T05_C-v1.5-c-r1_vs_C-v1.3-c-r1_12.md slot 2 = 91.0; T05_C-v1.5-c-r3_vs_C-v1.3-c-r3_12.md slot 2 = 91.0
- T06: T06_C-v1.5-c-r2_vs_C-v1.3-c-r2_21.md slot 1 = 88.0; T06_C-v1.5-c-r1_vs_C-v1.3-c-r1_12.md slot 2 = 90.0; T06_C-v1.5-c-r2_vs_C-v1.3-c-r2_12.md slot 2 = 90.0
- T07: T07_C-v1.5-c-r2_vs_C-v1.3-c-r2_21.md slot 1 = 87.0; T07_C-v1.5-c-r2_vs_C-v1.3-c-r2_12.md slot 2 = 88.0; T07_C-v1.5-c-r1_vs_C-v1.3-c-r1_12.md slot 2 = 90.0
- T08: T08_C-v1.5-c-r3_vs_C-v1.3-c-r3_12.md slot 2 = 74.0; T08_C-v1.5-c-r3_vs_C-v1.3-c-r3_21.md slot 1 = 74.0; T08_C-v1.5-c-r1_vs_C-v1.3-c-r1_12.md slot 2 = 87.0
- T09: T09_C-v1.5-c-r3_vs_C-v1.3-c-r3_12.md slot 2 = 78.0; T09_C-v1.5-c-r3_vs_C-v1.3-c-r3_21.md slot 1 = 81.0; T09_C-v1.5-c-r2_vs_C-v1.3-c-r2_12.md slot 2 = 84.0
- T10: T10_C-v1.5-c-r3_vs_C-v1.3-c-r3_12.md slot 2 = 76.0; T10_C-v1.5-c-r3_vs_C-v1.3-c-r3_21.md slot 1 = 83.0; T10_C-v1.5-c-r1_vs_C-v1.3-c-r1_12.md slot 2 = 84.0
