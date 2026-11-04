# E5: blind test and optimisation of the Jirgenson Model operating prompt (rounds 0–5)

**Permanent record on Zenodo: [doi.org/10.5281/zenodo.23964934](https://doi.org/10.5281/zenodo.23964934)** (version 1.0: 10.5281/zenodo.23964935). Please cite the DOI.

This folder is the same record as on Zenodo, except `inputs/` (the exact generator and judge inputs, about 20 MB, mostly the canon and prompt repeated in every input), which is only in the Zenodo archive `E5_inputs_v1.0.zip`. `MANIFEST_sha256.csv` lists every file of the full record, including `inputs/`; `README.md` and `STUDY.md` in this folder differ from the archived copies only by the DOI lines.

Results, method and limits are in **[STUDY.md](STUDY.md)**. Start there.

| Folder | Contents |
|---|---|
| `prompt/` | The canon as tested (v1.0, unchanged in all rounds), every operating-prompt version tested on the optimisation line (v1.0, v1.1-c, v1.2-c, v1.3-c, v1.5-c), and the control conditions A, B and C. |
| `tasks/` | The ten development scenarios with the full answer key, the machine-readable task file and its structure file. The ten sealed hold-out scenarios are not published; their hash is in STUDY.md §8. |
| `judge/` | The frozen judge prompt. |
| `inputs/roundN/` | The exact inputs given to the generator (`generation/`) and to the judge (`judge/`) in each round, with their indexes. |
| `responses/` | Every raw answer, one file each: round 0 A, B and C v1.0 (two blocks), and C for v1.1-c, v1.2-c, v1.3-c and v1.5-c. `INDEX_roundN.csv` gives SHA-256 and word counts. |
| `judgments/roundN/` | Every judge record (six reasoning steps in prose and a JSON score block), 120 per round, with `INDEX.csv`; `round0_rejudge/` holds the nine re-judged round-0 pairs. |
| `data/` | Frozen score tables per round (`roundN/`), hard-check results, the combined tables for rounds 0–5, the run configuration, summary statistics and figures with the numbers behind them. |
| `cross_check/` | Judge-calibration packs and the second-judge (Gemini) spot check. |
| `scripts/` | The Python scripts that built the inputs, ran the hard checks, collected the scores and produced the statistics and figures. |
| `working_notes/` | Protocol (29), scientific report (30), final results (42), run log, and per-round decisions, comparisons, error analyses and change packs. Translated into English from the working language of the experiment (STUDY.md §10). |

Rounds: 0 (v1.0), 1 (v1.1-c, accepted), 2 (v1.2-c, rejected), 3 (v1.3-c, accepted), 5 (v1.5-c, final). Round number 4 belongs to a separate test that is not part of this record.

The whole record is in English. Scenarios T09 and T10 were posed in Latvian and Russian; they, the answers to them and the related inputs and quotations are given in English translation (STUDY.md §10).

Licences: see `LICENSE.md`. `MANIFEST_sha256.csv` lists a SHA-256 for every file in this record. How to cite: `CITATION.cff`.

Author: Martin Jirgenson, 2026. This is not financial, legal or investment advice.
