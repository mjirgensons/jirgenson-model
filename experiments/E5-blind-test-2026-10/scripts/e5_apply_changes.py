#!/usr/bin/env python3
"""
E5 — apply a change pack to a prompt as exact, logged text replacements.

Usage: python3 e5_apply_changes.py --base prompts/02b_v1.1-c.md --changes index/changes_v1.2.json --out prompts/02b_v1.2-c.md

The JSON file is a list of {"id": "CH6", "section": "...", "old": "...", "new": "..."}. Every "old" must occur exactly once
in the base text (otherwise the script stops and nothing is written), so the diff between versions is fully determined by
the change pack and can be re-applied by anyone. Prints SHA-256 and word counts of base and result.
"""
import argparse, hashlib, json, sys


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", required=True); ap.add_argument("--changes", required=True); ap.add_argument("--out", required=True)
    a = ap.parse_args()
    base = open(a.base, encoding="utf-8").read()
    changes = json.load(open(a.changes, encoding="utf-8"))
    text = base
    for ch in changes:
        n = text.count(ch["old"])
        if n != 1:
            sys.exit(f"{ch['id']}: 'old' text occurs {n} times (must be exactly 1) — nothing written")
        text = text.replace(ch["old"], ch["new"])
        print(f"{ch['id']} applied ({ch['section']}): {len(ch['old'].split())} -> {len(ch['new'].split())} words")
    open(a.out, "w", encoding="utf-8").write(text)
    for name, t in (("base", base), ("result", text)):
        print(f"{name}: sha256 {hashlib.sha256(t.encode('utf-8')).hexdigest()}  words {len(t.split())}")
    print(f"delta words: {len(text.split()) - len(base.split()):+d} ({(len(text.split()) / len(base.split()) - 1) * 100:+.1f} %)")


if __name__ == "__main__":
    main()
