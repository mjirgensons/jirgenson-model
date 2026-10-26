#!/usr/bin/env python3
"""
Parse 29a (dev) and 29b (holdout) task files into tasks.json:
  {task_id: {"set": "dev"|"holdout", "turns": [user msg 1, user msg 2?], "block": full task block for the judge}}
Usage: python3 e5_build_tasks.py --dev 29a_E5_TASKS_DEV_v1.md --holdout 29b_E5_TASKS_HOLDOUT_v1.md --out tasks/tasks.json
"""
import argparse, json, re


def parse(path, task_set):
    text = open(path, encoding="utf-8").read()
    out = {}
    sections = re.split(r"^(?=## [TH]\d{2} )", text, flags=re.MULTILINE)
    for sec in sections:
        m = re.match(r"^## ([TH]\d{2}) ", sec)
        if not m:
            continue
        tid = m.group(1)
        block = sec.split("\n---\n")[0].rstrip()
        turns = []
        for mm in re.finditer(r"\*\*User message[^\n]*\(verbatim[^\n]*\):\*\*\s*\n((?:>.*\n?)+)", sec):
            quoted = mm.group(1)
            msg = "\n".join(line[2:] if line.startswith("> ") else line[1:] for line in quoted.strip().splitlines())
            turns.append(msg.strip())
        if not turns:
            raise SystemExit(f"no user message found for {tid}")
        out[tid] = {"set": task_set, "turns": turns, "block": block}
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dev", required=True); ap.add_argument("--holdout", required=True); ap.add_argument("--out", required=True)
    a = ap.parse_args()
    tasks = {}
    tasks.update(parse(a.dev, "dev")); tasks.update(parse(a.holdout, "holdout"))
    json.dump(tasks, open(a.out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    for k, v in tasks.items():
        print(k, v["set"], len(v["turns"]), "turn(s)", len(v["block"].split()), "block words", "|", v["turns"][0][:60].replace("\n", " "))


if __name__ == "__main__":
    main()
