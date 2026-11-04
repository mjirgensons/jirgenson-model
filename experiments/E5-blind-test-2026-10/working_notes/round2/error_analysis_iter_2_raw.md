# Error analysis — iteration 2, condition C-v1.2-c

| task | n judgments | mean total | missed elements (share) | forbidden | hard-check fails | C1 | C2 | C3 | C4 | C5 | C6 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| T01 | 12 | 88.8 | M8 4/12 | — | H1 4/12 | 8.8 | 8.8 | 8.2 | 7.6 | 8.8 | 8.9 |
| T02 | 12 | 74.8 | M8 8/12, M4 4/12, M2 3/12, M1 1/12 | F3 8/12 | H1 8/12 | 7.4 | 7.7 | 7.1 | 6.9 | 7.5 | 7.6 |
| T03 | 12 | 86.1 | M1 2/12 | — | — | 8.1 | 8.2 | 7.2 | 8.2 | 7.0 | 8.0 |
| T04 | 12 | 72.8 | M2 12/12, M7 12/12, M1 4/12 | — | — | 9.0 | 5.8 | 7.1 | 8.9 | 5.7 | 8.0 |
| T05 | 12 | 85.9 | M9 8/12, M7 1/12 | — | H1 8/12 | 8.6 | 8.0 | 8.6 | 7.5 | 8.9 | 9.0 |
| T06 | 12 | 85.3 | M8 4/12, M4 2/12 | — | H1 4/12 | 7.8 | 7.9 | 8.0 | 7.7 | 8.7 | 8.4 |
| T07 | 12 | 77.1 | M7 12/12 | F2 12/12 | H1 12/12 | 8.6 | 7.4 | 7.2 | 6.0 | 8.1 | 8.8 |
| T08 | 12 | 84.6 | M8 8/12 | — | H1 8/12 | 8.0 | 8.2 | 8.7 | 6.9 | 8.8 | 8.7 |
| T09 | 12 | 87.2 | M5 8/12 | — | — | 8.4 | 8.0 | 7.9 | 8.6 | 8.7 | 8.9 |
| T10 | 12 | 82.4 | M6 12/12 | — | — | 8.7 | 6.3 | 7.3 | 8.5 | 8.2 | 8.4 |

## Invented facts flagged by the judge (verbatim)

**T05**
- [T05_C-v1.2-c-r1_vs_C-v1.1-c-r1/21 r1] 'You, about 15 minutes' - unlabelled time estimate for messaging next week's bookings
- [T05_C-v1.2-c-r3_vs_C-v1.1-c-r3/21 r3] Reminder messages 'cost nothing' (minor unqualified claim)

## Lowest-scoring judgments per task (file, slot, total)

- T01: T01_C-v1.2-c-r3_vs_A-r3_21.md slot 2 = 82.0; T01_C-v1.2-c-r1_vs_A-r1_12.md slot 1 = 85.0; T01_C-v1.2-c-r1_vs_A-r1_21.md slot 2 = 85.0
- T02: T02_C-v1.2-c-r2_vs_C-v1.1-c-r2_21.md slot 2 = 62.0; T02_C-v1.2-c-r2_vs_A-r2_12.md slot 1 = 68.0; T02_C-v1.2-c-r2_vs_C-v1.1-c-r2_12.md slot 1 = 68.0
- T03: T03_C-v1.2-c-r3_vs_A-r3_12.md slot 1 = 82.0; T03_C-v1.2-c-r3_vs_A-r3_21.md slot 2 = 83.0; T03_C-v1.2-c-r1_vs_A-r1_12.md slot 1 = 84.0
- T04: T04_C-v1.2-c-r1_vs_C-v1.1-c-r1_12.md slot 1 = 66.0; T04_C-v1.2-c-r1_vs_C-v1.1-c-r1_21.md slot 2 = 69.0; T04_C-v1.2-c-r1_vs_A-r1_12.md slot 1 = 70.0
- T05: T05_C-v1.2-c-r3_vs_C-v1.1-c-r3_21.md slot 2 = 80.1; T05_C-v1.2-c-r1_vs_C-v1.1-c-r1_21.md slot 2 = 82.6; T05_C-v1.2-c-r3_vs_A-r3_21.md slot 2 = 82.6
- T06: T06_C-v1.2-c-r1_vs_C-v1.1-c-r1_12.md slot 1 = 81.0; T06_C-v1.2-c-r1_vs_C-v1.1-c-r1_21.md slot 2 = 82.0; T06_C-v1.2-c-r2_vs_A-r2_12.md slot 1 = 82.0
- T07: T07_C-v1.2-c-r2_vs_C-v1.1-c-r2_21.md slot 2 = 74.0; T07_C-v1.2-c-r1_vs_C-v1.1-c-r1_12.md slot 1 = 75.0; T07_C-v1.2-c-r1_vs_C-v1.1-c-r1_21.md slot 2 = 75.0
- T08: T08_C-v1.2-c-r1_vs_C-v1.1-c-r1_12.md slot 1 = 79.0; T08_C-v1.2-c-r1_vs_C-v1.1-c-r1_21.md slot 2 = 80.0; T08_C-v1.2-c-r3_vs_C-v1.1-c-r3_21.md slot 2 = 82.0
- T09: T09_C-v1.2-c-r3_vs_A-r3_21.md slot 2 = 85.0; T09_C-v1.2-c-r1_vs_A-r1_21.md slot 2 = 86.0; T09_C-v1.2-c-r1_vs_C-v1.1-c-r1_12.md slot 1 = 86.0
- T10: T10_C-v1.2-c-r1_vs_C-v1.1-c-r1_12.md slot 1 = 79.0; T10_C-v1.2-c-r1_vs_C-v1.1-c-r1_21.md slot 2 = 79.0; T10_C-v1.2-c-r3_vs_C-v1.1-c-r3_21.md slot 2 = 80.0
