#!/usr/bin/env python3
"""
E5 — build generation packs and judge packs.

gen:   python3 e5_packs.py gen --iter 0 --cond C --version v1.0 --runs 1-3 --set dev [--block 1]
       cond A: user message only; B: control prompt + user; C: operating prompt vN + canon attachment + user.
       Writes packs/iter_N/gen/{condkey}_{task}_{run}.md and appends packs/iter_N/gen_index.csv
regen: python3 e5_packs.py regen --iter 0 [--out DIR]
       Rebuilds the gen packs listed in gen_index.csv (index not changed); for iterations whose packs were not archived.

judge: python3 e5_packs.py judge --iter 0 --pair C-v1.0:A --runs 1:1,2:2,3:3 --set dev [--resp-iter-x 0 --resp-iter-y 0]
       Pairs response files responses/iter_X/{condx}_{task}_{rx}.md with responses/iter_Y/{condy}_{task}_{ry}.md,
       writes packs/iter_N/judge/{pairid}_{order}.md for order 12 and 21, appends packs/iter_N/judge_index.csv
"""
import argparse, csv, os, re, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TASKS = os.path.join(ROOT, "tasks", "tasks.json")
CANON = os.path.join(ROOT, "prompts", "02a_canon_v1.0.md")
CONTROL = os.path.join(ROOT, "29d_E5_CONTROL_PROMPTS_v1.md")
JUDGE = os.path.join(ROOT, "29c_E5_JUDGE_PROMPT_v1.md")


def code_block(path, nth=0):
    text = open(path, encoding="utf-8").read()
    blocks = re.findall(r"```\n(.*?)\n```", text, flags=re.DOTALL)
    return blocks[nth].strip()


def parse_runs(s):
    out = []
    for part in s.split(","):
        if "-" in part:
            a, b = part.split("-"); out += list(range(int(a), int(b) + 1))
        else:
            out.append(int(part))
    return out


def cmd_gen(a):
    tasks = json.load(open(TASKS, encoding="utf-8"))
    outdir = os.path.join(ROOT, "packs", f"iter_{a.iter}", "gen"); os.makedirs(outdir, exist_ok=True)
    idx_path = os.path.join(ROOT, "packs", f"iter_{a.iter}", "gen_index.csv")
    new_index = not os.path.exists(idx_path)
    canon = open(CANON, encoding="utf-8").read().strip()
    if a.cond == "C":
        condkey = f"C-{a.version}"
        system = open(os.path.join(ROOT, "prompts", f"02b_{a.version}.md"), encoding="utf-8").read().strip()
    elif a.cond == "B":
        condkey = "B"; system = code_block(CONTROL, 0)
    else:
        condkey = "A"; system = None
    rows = []
    for tid, t in tasks.items():
        if t["set"] != a.set:
            continue
        for run in parse_runs(a.runs):
            parts = []
            if system:
                parts.append("=== SYSTEM (instructions the assistant was given before the conversation) ===\n" + system)
            if a.cond == "C":
                parts.append("=== ATTACHMENT: jirgenson_canon_v1.0_en.txt (file attached by the user) ===\n" + canon)
            parts.append("=== USER ===\n" + t["turns"][0])
            fn = f"{condkey}_{tid}_{run}.md"
            open(os.path.join(outdir, fn), "w", encoding="utf-8").write("\n\n".join(parts) + "\n")
            rows.append({"iteration": a.iter, "condkey": condkey, "condition": a.cond, "prompt_version": a.version if a.cond == "C" else "",
                         "task_id": tid, "task_set": a.set, "run": run, "block": a.block or "", "turns": len(t["turns"]),
                         "turn2": t["turns"][1] if len(t["turns"]) > 1 else "", "pack": fn, "response": f"{condkey}_{tid}_{run}.md"})
    with open(idx_path, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        if new_index:
            w.writeheader()
        w.writerows(rows)
    print(f"{len(rows)} gen packs -> {outdir}")


def cmd_judge(a):
    tasks = json.load(open(TASKS, encoding="utf-8"))
    judge_prompt = code_block(JUDGE, 0)
    condx, condy = a.pair.split(":")
    itx = a.resp_iter_x if a.resp_iter_x is not None else a.iter
    ity = a.resp_iter_y if a.resp_iter_y is not None else a.iter
    outdir = os.path.join(ROOT, "packs", f"iter_{a.iter}", "judge"); os.makedirs(outdir, exist_ok=True)
    idx_path = os.path.join(ROOT, "packs", f"iter_{a.iter}", "judge_index.csv")
    new_index = not os.path.exists(idx_path)
    rows, missing = [], []
    for tid, t in tasks.items():
        if t["set"] != a.set:
            continue
        for pair in a.runs.split(","):
            rx, ry = pair.split(":")
            fx = os.path.join(ROOT, "responses", f"iter_{itx}", f"{condx}_{tid}_{rx}.md")
            fy = os.path.join(ROOT, "responses", f"iter_{ity}", f"{condy}_{tid}_{ry}.md")
            if not (os.path.exists(fx) and os.path.exists(fy)):
                missing += [p for p in (fx, fy) if not os.path.exists(p)]; continue
            rtx = open(fx, encoding="utf-8").read().strip(); rty = open(fy, encoding="utf-8").read().strip()
            pairid = f"{tid}_{condx}-r{rx}_vs_{condy}-r{ry}"
            for order in ("12", "21"):
                r1, r2 = (rtx, rty) if order == "12" else (rty, rtx)
                body = judge_prompt.replace("{{TASK_BLOCK: user message(s) verbatim, budget, gold facts, mandatory elements, forbidden items}}", t["block"])
                body = body.replace("{{RESPONSE_1}}", r1).replace("{{RESPONSE_2}}", r2)
                fn = f"{pairid}_{order}.md"
                open(os.path.join(outdir, fn), "w", encoding="utf-8").write(body + "\n")
                rows.append({"iteration": a.iter, "task_id": tid, "task_set": a.set, "pairid": pairid, "order": order,
                             "cond_1": condx if order == "12" else condy, "cond_2": condy if order == "12" else condx,
                             "run_1": rx if order == "12" else ry, "run_2": ry if order == "12" else rx,
                             "file_1": os.path.basename(fx) if order == "12" else os.path.basename(fy),
                             "file_2": os.path.basename(fy) if order == "12" else os.path.basename(fx),
                             "resp_iter_1": itx if order == "12" else ity, "resp_iter_2": ity if order == "12" else itx,
                             "pack": fn, "judgment": fn})
    if rows:
        with open(idx_path, "a", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            if new_index:
                w.writeheader()
            w.writerows(rows)
    print(f"{len(rows)} judge packs -> {outdir}; missing responses: {len(missing)}")
    for m in missing[:20]:
        print("  missing:", m)


def cmd_regen(a):
    """Rebuild the generation packs listed in packs/iter_N/gen_index.csv byte-for-byte as cmd_gen writes them,
    WITHOUT touching gen_index.csv. Used when the original pack files were not archived (iterations 0-1): every
    input (tasks.json, canon 02a, 02b version, control prompt 29d) is a frozen, hashed file, so the pack is fully
    determined by the index row. Determinism is checked by regenerating an iteration whose packs were archived."""
    tasks = json.load(open(TASKS, encoding="utf-8"))
    canon = open(CANON, encoding="utf-8").read().strip()
    outdir = a.out or os.path.join(ROOT, "packs", f"iter_{a.iter}", "gen"); os.makedirs(outdir, exist_ok=True)
    rows = list(csv.DictReader(open(os.path.join(ROOT, "packs", f"iter_{a.iter}", "gen_index.csv"), encoding="utf-8")))
    for r in rows:
        cond, t = r["condition"], tasks[r["task_id"]]
        system = (open(os.path.join(ROOT, "prompts", f"02b_{r['prompt_version']}.md"), encoding="utf-8").read().strip() if cond == "C"
                  else code_block(CONTROL, 0) if cond == "B" else None)
        parts = []
        if system:
            parts.append("=== SYSTEM (instructions the assistant was given before the conversation) ===\n" + system)
        if cond == "C":
            parts.append("=== ATTACHMENT: jirgenson_canon_v1.0_en.txt (file attached by the user) ===\n" + canon)
        parts.append("=== USER ===\n" + t["turns"][0])
        open(os.path.join(outdir, r["pack"]), "w", encoding="utf-8").write("\n\n".join(parts) + "\n")
    print(f"{len(rows)} gen packs regenerated from gen_index -> {outdir}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    g = sub.add_parser("gen"); g.add_argument("--iter", type=int, required=True); g.add_argument("--cond", choices=["A", "B", "C"], required=True)
    g.add_argument("--version", default="v1.0"); g.add_argument("--runs", default="1-3"); g.add_argument("--set", default="dev"); g.add_argument("--block", default="")
    j = sub.add_parser("judge"); j.add_argument("--iter", type=int, required=True); j.add_argument("--pair", required=True)
    j.add_argument("--runs", default="1:1,2:2,3:3"); j.add_argument("--set", default="dev")
    j.add_argument("--resp-iter-x", type=int, default=None); j.add_argument("--resp-iter-y", type=int, default=None)
    r = sub.add_parser("regen"); r.add_argument("--iter", type=int, required=True); r.add_argument("--out", default=None)
    a = ap.parse_args()
    {"gen": cmd_gen, "judge": cmd_judge, "regen": cmd_regen}[a.cmd](a)


if __name__ == "__main__":
    main()
