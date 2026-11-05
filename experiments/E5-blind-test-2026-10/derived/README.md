# Derived files

Added on 5 November 2026, after the Zenodo record v1.0 was published. They are not part of that record and not listed in `MANIFEST_sha256.csv`; they are computed from files that are.

| File | Content |
|---|---|
| `invented_facts_round5.csv` | Every invented fact the judge listed in the final round (round 5), in the judge's own words, for the 60 reviews of the answers without a prompt (A: 102 facts) and the 120 reviews of v1.5-c (1 fact). Columns: scenario, answer, judge record, the judge's wording. |
| `extract_invented_facts.py` | The script that builds the CSV from `judgments/round5/`. Run it from the folder above: `python3 derived/extract_invented_facts.py`. |

The A answers were reviewed in 60 judge records and v1.5-c in 120 (60 of them against A, 60 against v1.3-c); the one v1.5-c item comes from a review against A. Many listed items are small: a rule of thumb, a legal or industry rule, or a generalisation stated as fact without being in the scenario. The judge's definition is in `judge/judge_prompt_v1.md`.
