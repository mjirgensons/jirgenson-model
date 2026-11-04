#!/usr/bin/env python3
"""
E5 — automatic hard checks on assistant responses (objective, no judgement).

Usage
  python3 e5_hardchecks.py --responses responses/iter_1 --out hardchecks_iter_1.csv [--tasks dev|holdout]

Response files: one per (condition, task, run); file name  {cond}_{task}_{run}.md
  e.g.  A_T01_1.md   B_T03_2.md   C-v1.1-c_T05_3.md
  Two-turn tasks (T05, H05): put both assistant turns in the same file separated by a line
  containing only  ===TURN2===  ; each turn is checked against its own budget.

Checks (true = passed):
  H1 word budget per turn      H2 question budget      H3 language of reply
  H4 no internal labels/codes  H5 no management jargon on teen/child/family tasks
Outputs counts so a human or the judge can reconcile disagreements.
"""
import argparse, csv, os, re, sys

# task_id: (word budgets per turn, question budget per turn, language code, jargon_check)
BUDGETS = {
    "T01": ([600], [3], "en", False), "T02": ([300], [2], "en", False), "T03": ([700], [3], "en", False),
    "T04": ([500], [5], "en", False), "T05": ([600, 900], [3, 0], "en", False), "T06": ([600], [0], "en", False),
    "T07": ([400], [3], "en", True), "T08": ([600], [3], "en", False), "T09": ([600], [3], "lv", False),
    "T10": ([300], [2], "ru", False),
}
INTERNAL = [r"§\s*\d", r"\bEMERGENCY\b", r"\bQUICK\b", r"\bFULL\b", r"\bMODE\s*[12]\b", r"\bcanon\b", r"\bCANON\b",
            r"according to the model", r"outside the model", r"\bJMC-1\b", r"\bself.check\b", r"\bP[1-6]\b(?=\s|:)", r"\b[RL]\d{1,2}\b(?=[:\s])"]
JARGON = [r"\bparameters?\b", r"\bvectors?\b", r"\bzones?\b", r"\blevers?\b", r"\bman(o|oe)uvres?\b", r"\bKPIs?\b", r"\brefusal order\b",
          r"\bgoal vector\b", r"\berror vector\b"]
LV_CHARS = "\u0101\u010d\u0113\u0123\u012b\u0137\u013c\u0146\u0161\u016b\u017e"  # Latvian lower-case letters with diacritics
RU_RE = re.compile(r"[\u0400-\u04ff]")  # Cyrillic block U+0400..U+04FF


def word_count(t):
    return len(re.findall(r"\b[\w'’-]+\b", t, flags=re.UNICODE))


def question_count(t):
    # questions addressed to the person: sentences ending in '?' ; rhetorical ones cannot be told apart automatically
    return len(re.findall(r"\?", t))


def language_guess(t):
    letters = [c for c in t if c.isalpha()]
    if not letters:
        return "unknown"
    cyr = sum(1 for c in letters if RU_RE.match(c)) / len(letters)
    lv = sum(1 for c in letters if c.lower() in LV_CHARS) / len(letters)
    if cyr > 0.5:
        return "ru"
    if lv > 0.01:
        return "lv"
    return "en"


def check_turn(text, wb, qb, lang, jargon):
    wc, qc, lg = word_count(text), question_count(text), language_guess(text)
    internal = [p for p in INTERNAL if re.search(p, text)]
    jarg = [p for p in JARGON if re.search(p, text, flags=re.IGNORECASE)] if jargon else []
    return {"words": wc, "questions": qc, "lang": lg,
            "H1": wc <= wb * 1.10,            # 10 % tolerance for counting differences
            "H2": qc <= qb,
            "H3": lg == lang,
            "H4": len(internal) == 0, "internal_hits": ";".join(internal),
            "H5": len(jarg) == 0, "jargon_hits": ";".join(jarg)}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--responses", required=True); ap.add_argument("--out", required=True)
    a = ap.parse_args()
    rows = []
    for fn in sorted(os.listdir(a.responses)):
        if not fn.endswith(".md"):
            continue
        m = re.match(r"^(?P<cond>[^_]+)_(?P<task>[TH]\d{2})_(?P<run>\d+)\.md$", fn)
        if not m:
            print(f"skip (name pattern): {fn}", file=sys.stderr); continue
        cond, task, run = m.group("cond"), m.group("task"), int(m.group("run"))
        if task not in BUDGETS:
            print(f"skip (unknown task): {fn}", file=sys.stderr); continue
        text = open(os.path.join(a.responses, fn), encoding="utf-8").read()
        turns = [t.strip() for t in re.split(r"^\s*===TURN2===\s*$", text, flags=re.MULTILINE)]
        wbs, qbs, lang, jargon = BUDGETS[task]
        for i, turn in enumerate(turns):
            if i >= len(wbs):
                break
            r = check_turn(turn, wbs[i], qbs[i], lang, jargon)
            rows.append({"file": fn, "condition": cond, "task_id": task, "run": run, "turn": i + 1, **r,
                         "all_pass": all(r[k] for k in ("H1", "H2", "H3", "H4", "H5")),
                         "hard_fail_count": sum(not r[k] for k in ("H1", "H2", "H3", "H4", "H5"))})
    if not rows:
        print("no responses found", file=sys.stderr); sys.exit(1)
    with open(a.out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    print(f"{len(rows)} turns checked -> {a.out}")


if __name__ == "__main__":
    main()
