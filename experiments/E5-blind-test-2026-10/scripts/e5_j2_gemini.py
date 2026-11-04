#!/usr/bin/env python3
"""
E5 — build the J2 (Gemini, manual) material for one iteration from the J1 judge packs, unchanged.

Usage: python3 e5_j2_gemini.py --iter 2 [--pair T01_C-v1.2-c-r1_vs_C-v1.1-c-r1 --order 12]

Writes j2_gemini/iter_N/:
  JUDGE_PROMPT_Gemini.md                 pasted FIRST: the judge pack without the task part (pack[:TASK] + pack[RUBRIC:])
  DOCUMENT_iterN_<task>_pairs_1_order_<order>.md   pasted SECOND: task, key and the two anonymous responses (pack[TASK:RUBRIC])
  J2_selection_iter_N.csv                the selection for this iteration: every task (run by the fixed formula), candidate vs previous
                                         version, both orders, with the pack SHA-256 (same rule as iterations 0-1)
The split is the same one used for iterations 0 and 1 (checked: concatenating the two parts gives the pack back exactly).
Default pair: T01, run 1, candidate vs previous version, order 12 (the first row of the selection).
"""
import argparse, csv, hashlib, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--iter", type=int, required=True); ap.add_argument("--pair", default=None); ap.add_argument("--order", default="12"); ap.add_argument("--out", default=None)
    a = ap.parse_args()
    rows = list(csv.DictReader(open(os.path.join(ROOT, "packs", f"iter_{a.iter}", "judge_index.csv"), encoding="utf-8")))
    # selection: candidate vs the previous C version (not vs A), both orders
    # run per task by the fixed formula used since iteration 0 (README_J2_GEMINI): run = ((n - 1) // 2 mod 3) + 1 for task Tn
    sel = [r for r in rows if r["cond_1"].startswith("C-") and r["cond_2"].startswith("C-")
           and r["run_1"] == str(((int(r["task_id"][1:]) - 1) // 2) % 3 + 1)]
    out = a.out or os.path.join(ROOT, "j2_gemini", f"iter_{a.iter}"); os.makedirs(out, exist_ok=True)
    if a.out is None and os.path.exists(os.path.join(out, "JUDGE_PROMPT_Gemini.md")):
        raise SystemExit(f"{out} already exists — material already given to Martin is never overwritten; use --out for a check")
    with open(os.path.join(out, f"J2_selection_iter_{a.iter}.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(["pairid", "order", "pack", "cond_1", "cond_2", "task_id", "sha256", "words"])
        for r in sel:
            p = os.path.join(ROOT, "packs", f"iter_{a.iter}", "judge", r["pack"]); t = open(p, encoding="utf-8").read()
            w.writerow([r["pairid"], r["order"], r["pack"], r["cond_1"], r["cond_2"], r["task_id"], hashlib.sha256(open(p, "rb").read()).hexdigest(), len(t.split())])
    pairid = a.pair or sel[0]["pairid"]
    r = next(x for x in rows if x["pairid"] == pairid and x["order"] == a.order)
    pack = open(os.path.join(ROOT, "packs", f"iter_{a.iter}", "judge", r["pack"]), encoding="utf-8").read()
    t, rb = pack.index("=== TASK ==="), pack.index("=== RUBRIC")
    judge, doc = pack[:t] + pack[rb:], pack[t:rb]
    assert judge[:t] + doc + judge[t:] == pack
    open(os.path.join(out, "JUDGE_PROMPT_Gemini.md"), "w", encoding="utf-8").write(
        "# Judge prompt (29c v1) — paste into Gemini FIRST (or as the system instruction). Identical to the iteration 0 prompt.\n\n" + judge)
    fn = f"DOCUMENT_iter{a.iter}_{r['task_id']}_pairs_1_order_{a.order}.md"
    open(os.path.join(out, fn), "w", encoding="utf-8").write(
        f"# Document to judge (iteration {a.iter}) — paste into Gemini SECOND, in the same conversation, right after the judge prompt.\n\n" + doc.rstrip() + "\n")
    print(f"{len(sel)} selected packs; pair {pairid} order {a.order} -> {out}/{fn} + JUDGE_PROMPT_Gemini.md")


if __name__ == "__main__":
    main()
