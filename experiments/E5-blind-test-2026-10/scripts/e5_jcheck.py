#!/usr/bin/env python3
"""E5 — quick status of a judging round: which planned judgments exist and parse (JSON block with both responses).
Usage: python3 e5_jcheck.py --iter 3 [--next 6]   (--next lists the next N planned packs without a judgment, comparison vs C first)"""
import argparse, csv, json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ap = argparse.ArgumentParser(); ap.add_argument("--iter", type=int, required=True); ap.add_argument("--next", type=int, default=0)
a = ap.parse_args()
rows = list(csv.DictReader(open(os.path.join(ROOT, "packs", f"iter_{a.iter}", "judge_index.csv"), encoding="utf-8")))
ok, bad, missing = [], [], []
for r in rows:
    p = os.path.join(ROOT, "judgments", f"iter_{a.iter}", r["judgment"])
    if not os.path.exists(p):
        missing.append(r); continue
    t = open(p, encoding="utf-8").read()
    try:
        j = json.loads(re.findall(r"```json\s*(\{.*\})\s*```", t, re.S)[-1])
        assert set(j["responses"]) >= {"1", "2"} and "preference" in j
        ok.append(r["judgment"])
    except Exception as e:
        bad.append((r["judgment"], str(e)[:60]))
print(f"iter {a.iter}: {len(ok)} parse ok, {len(bad)} unparseable, {len(missing)} missing of {len(rows)}")
for b in bad:
    print("  UNPARSEABLE", *b)
if a.next:
    missing.sort(key=lambda r: (not r["cond_2"].startswith("C-") and not r["cond_1"].startswith("C-v1.1"), r["task_id"], r["pairid"], r["order"]))
    vs_c = [r for r in missing if "_vs_C-" in r["pairid"]]; vs_other = [r for r in missing if "_vs_C-" not in r["pairid"]]
    for r in (vs_c + vs_other)[:a.next]:
        print("NEXT", r["judgment"])
