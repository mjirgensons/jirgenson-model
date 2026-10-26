#!/usr/bin/env python3
"""
E5 — error analysis for condition C (or any condkey) from the judgments of one iteration.
Usage: python3 e5_error_analysis.py --iter 0 --cond C-v1.0 --out error_analysis_iter_0_raw.md
Tallies, per task: missed mandatory elements (per element id, share of judgments), forbidden items, failed hard checks,
invented facts (text), criteria means; and lists the lowest-scoring judgments for reading.
"""
import argparse, csv, json, os, re, sys
from collections import defaultdict, Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
from e5_collect import extract_json  # noqa

CRIT = ["C1", "C2", "C3", "C4", "C5", "C6"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--iter", type=int, required=True); ap.add_argument("--cond", required=True); ap.add_argument("--out", required=True)
    a = ap.parse_args()
    idx = {(r["pairid"], r["order"]): r for r in csv.DictReader(open(os.path.join(ROOT, "packs", f"iter_{a.iter}", "judge_index.csv"), encoding="utf-8"))}
    jdir = os.path.join(ROOT, "judgments", f"iter_{a.iter}")
    per_task = defaultdict(lambda: {"n": 0, "miss": Counter(), "forb": Counter(), "hard": Counter(), "inv": [], "crit": defaultdict(list), "scores": []})
    for fn in sorted(os.listdir(jdir)):
        m = re.match(r"^(.*)_(12|21)\.md$", fn)
        if not m or (m.group(1), m.group(2)) not in idx:
            continue
        meta = idx[(m.group(1), m.group(2))]
        js = extract_json(open(os.path.join(jdir, fn), encoding="utf-8").read())
        if not js:
            continue
        for slot in ("1", "2"):
            if meta[f"cond_{slot}"] != a.cond:
                continue
            r = js["responses"][slot]; t = per_task[meta["task_id"]]; t["n"] += 1
            for k, v in r["elements"].items():
                if int(v) == 0:
                    t["miss"][k] += 1
            for f in r.get("forbidden", []) or []:
                t["forb"][str(f)] += 1
            for k, v in (r.get("hard_checks", {}) or {}).items():
                if str(v).lower() in ("false", "0", "no"):
                    t["hard"][k] += 1
            for s in r.get("invented_facts", []) or []:
                t["inv"].append(f"[{meta['pairid']}/{meta['order']} r{meta['run_'+slot]}] {s}")
            for c in CRIT:
                t["crit"][c].append(float(r["criteria"][c]))
            el = sum(int(v) for v in r["elements"].values()) / max(1, len(r["elements"])) * 40
            tot = el + sum(float(r["criteria"][c]) for c in CRIT) - 2 * (len(r.get("forbidden", []) or []) + sum(1 for v in (r.get("hard_checks", {}) or {}).values() if str(v).lower() in ("false", "0", "no")))
            t["scores"].append((round(tot, 1), fn, slot))
    lines = [f"# Error analysis — iteration {a.iter}, condition {a.cond}", ""]
    lines += ["| task | n judgments | mean total | missed elements (share) | forbidden | hard-check fails | " + " | ".join(CRIT) + " |", "|---|---|---|---|---|---|" + "---|" * len(CRIT)]
    for tid in sorted(per_task):
        t = per_task[tid]; n = t["n"]
        miss = ", ".join(f"{k} {v}/{n}" for k, v in sorted(t["miss"].items(), key=lambda x: -x[1]))
        forb = ", ".join(f"{k} {v}/{n}" for k, v in t["forb"].most_common())
        hard = ", ".join(f"{k} {v}/{n}" for k, v in t["hard"].most_common())
        mean_tot = sum(s for s, _, _ in t["scores"]) / max(1, n)
        lines.append(f"| {tid} | {n} | {mean_tot:.1f} | {miss or '—'} | {forb or '—'} | {hard or '—'} | " + " | ".join(f"{sum(t['crit'][c])/max(1,len(t['crit'][c])):.1f}" for c in CRIT) + " |")
    lines += ["", "## Invented facts flagged by the judge (verbatim)", ""]
    for tid in sorted(per_task):
        if per_task[tid]["inv"]:
            lines.append(f"**{tid}**"); lines += [f"- {s}" for s in per_task[tid]["inv"]]; lines.append("")
    lines += ["## Lowest-scoring judgments per task (file, slot, total)", ""]
    for tid in sorted(per_task):
        worst = sorted(per_task[tid]["scores"])[:3]
        lines.append(f"- {tid}: " + "; ".join(f"{fn} slot {slot} = {s}" for s, fn, slot in worst))
    open(a.out, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
