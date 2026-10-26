#!/usr/bin/env python3
"""
E5 — parse judge outputs into the results and pairwise CSVs (rebuilt from scratch every time, deterministic).

Usage: python3 e5_collect.py --config registry/e5_run_config.json --results registry/e5_results.csv --pairwise registry/e5_pairwise.csv
Config: a JSON list of entries {"iteration": 0, "judgments_dir": "judgments/iter_0", "judge": "opus-5.5",
                                "generator": "claude-sonnet-5.5", "judge_index": "packs/iter_0/judge_index.csv"}
Each judgment file must end with the JSON block defined in 29c. Files that fail to parse are listed (re-run them).
"""
import argparse, csv, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CRIT = ["C1", "C2", "C3", "C4", "C5", "C6"]


def extract_json(text):
    # prefer fenced ```json blocks (last one), else the last balanced {...}
    fences = re.findall(r"```(?:json)?\s*(\{.*?\})\s*```", text, flags=re.DOTALL)
    cands = fences[::-1] if fences else []
    if not cands:
        end = text.rfind("}")
        depth = 0
        for i in range(end, -1, -1):
            if text[i] == "}":
                depth += 1
            elif text[i] == "{":
                depth -= 1
                if depth == 0:
                    cands = [text[i:end + 1]]; break
    for c in cands:
        try:
            return json.loads(c)
        except Exception:
            c2 = re.sub(r",\s*([}\]])", r"\1", c)  # trailing commas
            try:
                return json.loads(c2)
            except Exception:
                continue
    return None


def condkey_split(ck):
    if ck.startswith("C-"):
        return "C", ck[2:]
    return ck, ""


def load_gen_blocks():
    """block number per (iteration, condkey, task, run) from gen_index files."""
    blocks = {}
    packs = os.path.join(ROOT, "packs")
    if not os.path.isdir(packs):
        return blocks
    for d in os.listdir(packs):
        p = os.path.join(packs, d, "gen_index.csv")
        if os.path.exists(p):
            for r in csv.DictReader(open(p, encoding="utf-8")):
                blocks[(int(r["iteration"]), r["condkey"], r["task_id"], int(r["run"]))] = r.get("block", "")
    return blocks


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default=os.path.join(ROOT, "registry", "e5_run_config.json"))
    ap.add_argument("--results", default=os.path.join(ROOT, "registry", "e5_results.csv"))
    ap.add_argument("--pairwise", default=os.path.join(ROOT, "registry", "e5_pairwise.csv"))
    a = ap.parse_args()
    cfg = json.load(open(a.config, encoding="utf-8"))
    blocks = load_gen_blocks()
    res_rows, pw_rows, failed, n_ok = [], [], [], 0
    for e in cfg:
        it = int(e["iteration"])
        if e.get("frozen_results"):
            # Frozen record: the parsed results of a completed iteration, used as-is (see run log for why).
            fr = list(csv.DictReader(open(os.path.join(ROOT, e["frozen_results"]), encoding="utf-8")))
            fp = list(csv.DictReader(open(os.path.join(ROOT, e["frozen_pairwise"]), encoding="utf-8")))
            res_rows += fr; pw_rows += fp; n_ok += len(fp)
            print(f"iteration {it}: frozen record used ({len(fr)} result rows, {len(fp)} pairwise rows from {e['frozen_results']})")
            continue
        jdir = os.path.join(ROOT, e["judgments_dir"])
        index = {(r["pairid"], r["order"]): r for r in csv.DictReader(open(os.path.join(ROOT, e["judge_index"]), encoding="utf-8"))}
        if not os.path.isdir(jdir):
            continue
        for fn in sorted(os.listdir(jdir)):
            if not fn.endswith(".md"):
                continue
            m = re.match(r"^(.*)_(12|21)\.md$", fn)
            if not m or (m.group(1), m.group(2)) not in index:
                failed.append((fn, "not in index")); continue
            meta = index[(m.group(1), m.group(2))]
            js = extract_json(open(os.path.join(jdir, fn), encoding="utf-8").read())
            if not js or "responses" not in js or "preference" not in js:
                failed.append((fn, "no/invalid JSON")); continue
            try:
                for slot in ("1", "2"):
                    r = js["responses"][slot]
                    ck = meta[f"cond_{slot}"]; cond, ver = condkey_split(ck)
                    crit = {c: int(round(float(r["criteria"][c]))) for c in CRIT}
                    elements = {k: int(v) for k, v in r["elements"].items()}
                    hard = r.get("hard_checks", {})
                    hard_fail = sum(1 for v in hard.values() if str(v).lower() in ("false", "0", "no"))
                    forbidden = r.get("forbidden", []) or []
                    inv = r.get("invented_facts", []) or []
                    resp_iter = int(meta.get(f"resp_iter_{slot}", it))
                    res_rows.append({"iteration": it, "prompt_version": ver, "condition": cond, "task_id": meta["task_id"],
                                     "task_set": meta["task_set"], "run": int(meta[f"run_{slot}"]),
                                     "block": blocks.get((resp_iter, ck, meta["task_id"], int(meta[f"run_{slot}"])), ""),
                                     "generator_model": e["generator"], "judge": e["judge"], "order": meta["order"],
                                     "n_elements": len(elements), "elements_hit": sum(elements.values()), **crit,
                                     "violations": len(forbidden) + hard_fail, "invented_facts": len(inv),
                                     "word_count": int(r.get("word_count", 0) or 0), "pairid": meta["pairid"], "resp_iter": resp_iter,
                                     "forbidden": ";".join(map(str, forbidden)), "hard_failed": ";".join(k for k, v in hard.items() if str(v).lower() in ("false", "0", "no"))})
                pref = js["preference"]
                better = str(pref.get("better", "tie")).strip().lower()
                better = better if better in ("1", "2", "tie") else "tie"
                ck1, ck2 = meta["cond_1"], meta["cond_2"]
                fmt = lambda ck: (f"C:{ck[2:]}" if ck.startswith("C-") else ck)
                pw_rows.append({"iteration": it, "task_id": meta["task_id"], "task_set": meta["task_set"], "run": meta["pairid"],
                                "judge": e["judge"], "order": meta["order"], "cond_1": fmt(ck1), "cond_2": fmt(ck2),
                                "preferred": better, "confidence": float(pref.get("confidence", 0.5) or 0.5)})
                n_ok += 1
            except Exception as ex:
                failed.append((fn, f"schema: {ex}"))
    for path, rows in ((a.results, res_rows), (a.pairwise, pw_rows)):
        if rows:
            with open(path, "w", newline="", encoding="utf-8") as f:
                w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    print(f"parsed {n_ok} judgments -> {len(res_rows)} result rows, {len(pw_rows)} pairwise rows; failed: {len(failed)}")
    for fn, why in failed:
        print("  FAILED:", fn, why)
    if failed:
        sys.exit(2)


if __name__ == "__main__":
    main()
