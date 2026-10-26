# E5 summary  [iteration 0, dev set, J1=Opus 5.5]

Rows: 240; iterations: [np.int64(0)]; versions: {0: 'v1.0'}

**Noise band (test–retest, v1.0 two blocks):** SE = 0.75, band = ±1.51 points (block difference mean +0.00, n = 10 tasks)

| iteration | comparison | n tasks | mean diff | 95 % CI | Cohen d | tasks +/− | Wilcoxon p | sign p |
|---|---|---|---|---|---|---|---|---|
| 0 | C:v1.0 − A | 10 | +30.56 | [+26.68, +34.36] | 4.68 | 10/0 | 0.002 | 0.002 |
| 0 | C:v1.0 − B | 10 | +18.24 | [+13.10, +23.39] | 2.09 | 10/0 | 0.002 | 0.002 |

| version/condition | set | iteration | total | criteria (60) | elements % | violations | invented facts | C1 | C2 | C3 | C4 | C5 | C6 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A | dev | 0 | 55.3 | 36.0 | 54 | 1.07 | 1.72 | 7.0 | 6.6 | 5.9 | 6.4 | 3.9 | 6.1 |
| B | dev | 0 | 67.7 | 43.3 | 66 | 0.97 | 0.70 | 7.8 | 7.0 | 7.7 | 6.7 | 6.0 | 8.1 |
| C:v1.0 | dev | 0 | 85.9 | 49.1 | 93 | 0.28 | 0.79 | 7.8 | 8.2 | 8.0 | 8.0 | 8.6 | 8.5 |

| iteration | set | cond | vs | wins | ties | n | win rate | Wilson 95 % CI |
|---|---|---|---|---|---|---|---|---|
| 0 | dev | A | C:v1.0 | 0 | 0 | 30 | 0.00 | [-0.00, 0.11] |
| 0 | dev | C:v1.0 | A | 30 | 0 | 30 | 1.00 | [0.89, 1.00] |
| 0 | dev | B | C:v1.0 | 1 | 0 | 30 | 0.03 | [0.01, 0.17] |
| 0 | dev | C:v1.0 | B | 29 | 0 | 30 | 0.97 | [0.83, 0.99] |
