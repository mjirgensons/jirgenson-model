# Error analysis — iteration 5, condition C-v1.5-c

| task | n judgments | mean total | missed elements (share) | forbidden | hard-check fails | C1 | C2 | C3 | C4 | C5 | C6 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| T01 | 12 | 91.0 | — | — | — | 8.6 | 8.2 | 8.5 | 8.2 | 8.8 | 8.6 |
| T02 | 12 | 89.2 | — | — | — | 9.0 | 8.2 | 7.5 | 8.4 | 7.9 | 8.2 |
| T03 | 12 | 86.9 | M6 4/12, M8 2/12 | — | — | 8.9 | 7.8 | 8.2 | 8.6 | 7.2 | 8.2 |
| T04 | 12 | 85.2 | M7 6/12, M2 4/12 | — | — | 9.1 | 7.8 | 8.1 | 9.0 | 6.8 | 8.6 |
| T05 | 12 | 90.0 | M8 1/12 | — | — | 8.9 | 7.3 | 8.7 | 8.2 | 8.7 | 8.6 |
| T06 | 12 | 90.6 | — | — | — | 8.4 | 8.5 | 8.4 | 8.3 | 8.5 | 8.4 |
| T07 | 12 | 89.8 | — | — | — | 8.4 | 8.0 | 8.2 | 8.2 | 8.7 | 8.3 |
| T08 | 12 | 90.3 | M3 2/12, M1 1/12 | — | — | 8.3 | 8.2 | 8.7 | 8.6 | 8.8 | 9.0 |
| T09 | 12 | 84.8 | M3 11/12 | — | — | 8.3 | 7.7 | 8.2 | 8.0 | 8.7 | 8.5 |
| T10 | 12 | 89.7 | M1 2/12 | — | — | 8.9 | 8.4 | 8.1 | 8.2 | 8.6 | 8.2 |

## Invented facts flagged by the judge (verbatim)

**T03**
- [T03_C-v1.5-c-r2_vs_A-r2/21 r2] 'With your hours, three to five [goals] can get real work this year' - unlabelled rule of thumb; the owner's hours are not given (minor)

## Lowest-scoring judgments per task (file, slot, total)

- T01: T01_C-v1.5-c-r1_vs_C-v1.3-c-r1_12.md slot 1 = 86.0; T01_C-v1.5-c-r1_vs_C-v1.3-c-r1_21.md slot 2 = 89.0; T01_C-v1.5-c-r1_vs_A-r1_21.md slot 2 = 90.0
- T02: T02_C-v1.5-c-r2_vs_A-r2_21.md slot 2 = 86.0; T02_C-v1.5-c-r2_vs_C-v1.3-c-r2_21.md slot 2 = 86.0; T02_C-v1.5-c-r2_vs_A-r2_12.md slot 1 = 88.0
- T03: T03_C-v1.5-c-r3_vs_C-v1.3-c-r3_21.md slot 2 = 81.0; T03_C-v1.5-c-r1_vs_C-v1.3-c-r1_12.md slot 1 = 82.0; T03_C-v1.5-c-r1_vs_C-v1.3-c-r1_21.md slot 2 = 82.0
- T04: T04_C-v1.5-c-r3_vs_C-v1.3-c-r3_21.md slot 2 = 82.0; T04_C-v1.5-c-r1_vs_C-v1.3-c-r1_12.md slot 1 = 83.0; T04_C-v1.5-c-r1_vs_A-r1_21.md slot 2 = 84.0
- T05: T05_C-v1.5-c-r2_vs_C-v1.3-c-r2_21.md slot 2 = 84.6; T05_C-v1.5-c-r2_vs_C-v1.3-c-r2_12.md slot 1 = 88.0; T05_C-v1.5-c-r3_vs_C-v1.3-c-r3_21.md slot 2 = 88.0
- T06: T06_C-v1.5-c-r1_vs_A-r1_12.md slot 1 = 88.0; T06_C-v1.5-c-r1_vs_A-r1_21.md slot 2 = 88.0; T06_C-v1.5-c-r1_vs_C-v1.3-c-r1_12.md slot 1 = 88.0
- T07: T07_C-v1.5-c-r3_vs_C-v1.3-c-r3_21.md slot 2 = 87.0; T07_C-v1.5-c-r1_vs_C-v1.3-c-r1_12.md slot 1 = 88.0; T07_C-v1.5-c-r1_vs_A-r1_12.md slot 1 = 89.0
- T08: T08_C-v1.5-c-r2_vs_C-v1.3-c-r2_21.md slot 2 = 80.0; T08_C-v1.5-c-r2_vs_C-v1.3-c-r2_12.md slot 1 = 87.0; T08_C-v1.5-c-r3_vs_A-r3_21.md slot 2 = 90.0
- T09: T09_C-v1.5-c-r1_vs_C-v1.3-c-r1_12.md slot 1 = 81.0; T09_C-v1.5-c-r3_vs_C-v1.3-c-r3_12.md slot 1 = 83.0; T09_C-v1.5-c-r3_vs_C-v1.3-c-r3_21.md slot 2 = 83.0
- T10: T10_C-v1.5-c-r2_vs_C-v1.3-c-r2_12.md slot 1 = 81.0; T10_C-v1.5-c-r2_vs_C-v1.3-c-r2_21.md slot 2 = 83.0; T10_C-v1.5-c-r1_vs_C-v1.3-c-r1_12.md slot 1 = 87.0
