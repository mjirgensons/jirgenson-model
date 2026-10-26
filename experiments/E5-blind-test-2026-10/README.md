# E5: blind test of the operating prompt (October 2026)

Results, method and limits are in **[STUDY.md](STUDY.md)**. Start there.

| Folder | Contents |
|---|---|
| `prompt/` | The operating prompt exactly as tested (v1.3-c), the canon as tested (v1.0), and the control conditions A, B and C. |
| `tasks/` | The ten development scenarios with the full answer key, and their structure file. The ten sealed hold-out scenarios are not published; their hash is in STUDY.md. |
| `judge/` | The frozen judge prompt. |
| `responses/` | Every raw answer: A (no prompt), B (generic prompt), C v1.3-c (tested), C v1.1-c (comparison). |
| `judgments/` | All 120 judge records for the tested version, with the pairing index. |
| `data/` | Score tables, summaries, hard-check results and figures. |
| `cross_check/` | The second-judge (Gemini) spot check and its materials. |
| `scripts/` | The scripts that built the packs, ran the checks and produced the statistics. |
| `working_notes_lv/` | Protocol, run log and decisions, in Latvian, unedited. |

Licence: CC BY-ND 4.0, same as the repository. `MANIFEST_sha256.csv` lists a SHA-256 for every file in this folder.
