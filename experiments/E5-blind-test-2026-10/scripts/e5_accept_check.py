#!/usr/bin/env python3
"""E5 — pre-registered acceptance check (protocol 29 §5.4 / decisions D5.4) for one iteration.

Reads the collected tables (registry/e5_results.csv, registry/e5_pairwise.csv — or the frozen snapshots) and prints every number
the comparison document quotes, so the verdict can be re-derived from the archive with one command:

  python3 scripts/e5_accept_check.py --iter 5 --test v1.5-c --base v1.3-c --ctrl A \
      --delta-min 1.51 --ci-low-min -1 --crit-drop-max 1.0 \
      --out figures/iter_5/iter5_d54_check.txt

Numbers follow e5_analyze.py exactly: total = 40*elements_hit/n_elements + C1..C6 - 2*violations (clipped at 0); per-task means over
runs and orders; paired (by task) bootstrap CI (10 000 resamples, seed 0); Wilcoxon; sign test on pairwise preference (a pair is a win
only when the same side is preferred in BOTH orders). The "same-call" robustness check uses only the judgments in which test and base
were scored together (the 60 vs-base calls), so judge drift between calls cannot enter the difference.
"""
import argparse
import csv
import sys
from collections import defaultdict

import numpy as np
import pandas as pd

try:
    import scipy.stats as sps
except Exception:  # pragma: no cover
    sps = None

CRIT = ["C1", "C2", "C3", "C4", "C5", "C6"]


def add_scores(df):
    df = df.copy()
    df["elements_pct"] = df["elements_hit"] / df["n_elements"]
    df["total"] = (df["elements_pct"] * 40 + df[CRIT].sum(axis=1) - 2 * df["violations"]).clip(lower=0)
    df["cond_key"] = np.where(df["condition"] == "C", "C:" + df["prompt_version"].astype(str), df["condition"])
    return df


def paired(a, b, n_boot=10000, seed=0):
    idx = a.index.intersection(b.index)
    d = (a.loc[idx] - b.loc[idx]).values
    rng = np.random.default_rng(seed)
    boots = np.array([rng.choice(d, size=len(d), replace=True).mean() for _ in range(n_boot)])
    out = {"n": len(d), "mean": d.mean(), "lo": np.percentile(boots, 2.5), "hi": np.percentile(boots, 97.5),
           "pos": int((d > 0).sum()), "neg": int((d < 0).sum()), "per_task": {t: round(float(v), 2) for t, v in zip(idx, d)}}
    if sps is not None and len(d) >= 6 and np.any(d != 0):
        out["wilcoxon_p"] = float(sps.wilcoxon(d, zero_method="wilcox").pvalue)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--iter", type=int, required=True)
    ap.add_argument("--test", required=True, help="prompt version under test, e.g. v1.5-c")
    ap.add_argument("--base", required=True, help="base prompt version re-judged in this iteration, e.g. v1.3-c")
    ap.add_argument("--ctrl", default="A")
    ap.add_argument("--results", default="registry/e5_results.csv")
    ap.add_argument("--pairwise", default="registry/e5_pairwise.csv")
    ap.add_argument("--delta-min", type=float, default=1.51, help="noise band: Δ must exceed this (criterion 1)")
    ap.add_argument("--ci-low-min", type=float, default=-1.0, help="CI lower bound must exceed this (criterion 1)")
    ap.add_argument("--crit-drop-max", type=float, default=1.0, help="no criterion may drop by more than this (criterion 2)")
    ap.add_argument("--viol-rise-max", type=float, default=0.0, help="violations per response may not rise by more than this (criterion 3)")
    ap.add_argument("--length-pct", type=float, default=None, help="prompt length vs v1.0 in %% (criterion 4; reported, not computed here)")
    ap.add_argument("--length-max", type=float, default=15.0)
    ap.add_argument("--out", default=None)
    a = ap.parse_args()

    lines = []

    def P(*x):
        s = " ".join(str(v) for v in x)
        lines.append(s)
        print(s)

    df = add_scores(pd.read_csv(a.results))
    it = df[df.iteration == a.iter]
    kt, kb, kc = f"C:{a.test}", f"C:{a.base}", a.ctrl
    P(f"E5 acceptance check — iteration {a.iter}: {kt} (test) vs {kb} (base) and vs {kc}; rows in iteration: {len(it)}")
    P(f"judgments per condition: " + ", ".join(f"{k}={int(v)}" for k, v in it.cond_key.value_counts().items()))

    # ---- 1. all judgments: per-task means, paired by task
    tm = it.groupby(["cond_key", "task_id"]).mean(numeric_only=True)
    tot = {k: tm.loc[k]["total"] for k in (kt, kb, kc) if k in tm.index.get_level_values(0)}
    P("\n== ALL judgments (per-task means over runs and orders) ==")
    for k, v in tot.items():
        P(f"  {k}: mean total {v.mean():.2f}")
    r = paired(tot[kt], tot[kb])
    P(f"  Δ test−base (task means): {r['mean']:+.2f} [{r['lo']:+.2f}; {r['hi']:+.2f}]  tasks +/−: {r['pos']}/{r['neg']}  Wilcoxon p = {r.get('wilcoxon_p', float('nan')):.3f}")
    P("  per task: " + str(r["per_task"]))
    if kc in tot:
        rc = paired(tot[kt], tot[kc])
        P(f"  Δ test−{kc}: {rc['mean']:+.2f} [{rc['lo']:+.2f}; {rc['hi']:+.2f}]  tasks +/−: {rc['pos']}/{rc['neg']}")
        P("  per task: " + str(rc["per_task"]))

    # ---- 2. criteria, violations, invented facts, elements
    P("\n== Criteria / violations / invented facts / elements (all judgments) test / base / diff ==")
    crit_diff = {}
    for c in CRIT + ["violations", "invented_facts", "elements_pct", "word_count"]:
        vt, vb = tm.loc[kt][c].mean(), tm.loc[kb][c].mean()
        crit_diff[c] = vt - vb
        P(f"  {c:14s} {vt:7.3f} {vb:7.3f} {vt - vb:+.3f}")
    P(f"  invented facts per response (test): {it[it.cond_key == kt].invented_facts.mean():.3f} over {len(it[it.cond_key == kt])} judgments; "
      f"judgments with ≥1 invented fact: {int((it[it.cond_key == kt].invented_facts > 0).sum())}")
    P(f"  invented facts per response (base): {it[it.cond_key == kb].invented_facts.mean():.3f}; (ctrl): {it[it.cond_key == kc].invented_facts.mean():.3f}")

    # ---- 3. same-call robustness: only the calls where test and base were judged together
    same = it[it.pairid.str.contains(f"_vs_C-{a.base}-", regex=False)]
    P(f"\n== SAME-CALL robustness ({len(same)} rows = {same.pairid.nunique()} pairs × 2 orders; test and base scored in the same judge call) ==")
    tms = same.groupby(["cond_key", "task_id"]).mean(numeric_only=True)
    rs = paired(tms.loc[kt]["total"], tms.loc[kb]["total"])
    P(f"  test {tms.loc[kt]['total'].mean():.2f} base {tms.loc[kb]['total'].mean():.2f}  Δ {rs['mean']:+.2f} [{rs['lo']:+.2f}; {rs['hi']:+.2f}]  tasks +/−: {rs['pos']}/{rs['neg']}")
    P("  per task: " + str(rs["per_task"]))
    for c in CRIT + ["violations", "invented_facts"]:
        P(f"  {c:14s} same-call diff {tms.loc[kt][c].mean() - tms.loc[kb][c].mean():+.3f}")
    # one-to-one violations: same calls, per response
    vt_same, vb_same = same[same.cond_key == kt].violations.mean(), same[same.cond_key == kb].violations.mean()
    P(f"  violations per response, same calls: test {vt_same:.3f} base {vb_same:.3f} (rise {vt_same - vb_same:+.3f})")

    # ---- 4. pairwise preference (both orders must agree)
    pw = pd.read_csv(a.pairwise)
    pw = pw[pw.iteration == a.iter]

    def tally(key_other):
        sub = pw[((pw.cond_1 == kt) & (pw.cond_2 == key_other)) | ((pw.cond_1 == key_other) & (pw.cond_2 == kt))]
        res = defaultdict(list)
        for _, row in sub.iterrows():
            pref = str(row.preferred)
            who = (row.cond_1 if pref == "1" else row.cond_2 if pref == "2" else "tie")
            res[row.run].append(who)
        wins = sum(1 for v in res.values() if len(v) == 2 and all(x == kt for x in v))
        losses = sum(1 for v in res.values() if len(v) == 2 and all(x == key_other for x in v))
        split = len(res) - wins - losses
        detail = {k: v for k, v in res.items() if not (len(v) == 2 and (all(x == kt for x in v)))}
        return len(res), wins, losses, split, detail

    P("\n== Pairwise preference (a win needs the same side in BOTH orders) ==")
    n_pairs, w, l, s, det = tally(kb)
    p_sign = float(sps.binomtest(w, w + l, 0.5).pvalue) if sps is not None and (w + l) > 0 else float("nan")
    P(f"  vs {kb}: pairs {n_pairs}: test wins {w}, base wins {l}, split/tie {s}; sign test (wins vs losses) p = {p_sign:.4f}")
    P("  non-wins: " + str(det))
    if kc in tot:
        n_pairs_c, wc, lc, sc, detc = tally(kc)
        P(f"  vs {kc}: pairs {n_pairs_c}: test wins {wc}, {kc} wins {lc}, split/tie {sc}")
        P("  non-wins: " + str(detc))

    # ---- 5. verdict
    P("\n== Pre-registered rule (§5.4 / D5.4) ==")
    c1 = (r["mean"] > a.delta_min) and (r["lo"] > a.ci_low_min)
    worst = min(crit_diff[c] for c in CRIT)
    worst_c = min(CRIT, key=lambda c: crit_diff[c])
    c2 = worst >= -a.crit_drop_max
    c3 = (vt_same - vb_same) <= a.viol_rise_max + 1e-9
    P(f"  (1) Δ {r['mean']:+.2f} > {a.delta_min} and CI low {r['lo']:+.2f} > {a.ci_low_min}: {'✓' if c1 else '✗'}")
    P(f"  (2) no criterion drops > {a.crit_drop_max}: worst {worst_c} {worst:+.2f}: {'✓' if c2 else '✗'}")
    P(f"  (3) violations not rising (same calls, one-to-one): {vt_same - vb_same:+.3f}: {'✓' if c3 else '✗'}")
    if a.length_pct is not None:
        c4 = a.length_pct <= a.length_max
        P(f"  (4) prompt length {a.length_pct:+.1f} % vs v1.0 ≤ +{a.length_max:.0f} %: {'✓' if c4 else '✗'}")
    else:
        c4 = True
        P("  (4) prompt length: not supplied (--length-pct); see changes file")
    if c1 and c2 and c3 and c4:
        P("  VERDICT: IMPROVEMENT — all four criteria met; new version becomes the base.")
    elif (not c1) and c2 and c3 and c4 and r["mean"] >= 0:
        P("  VERDICT: NEUTRAL, NOT WORSE — (1) not met, (2)–(4) met and Δ ≥ 0; report, base unchanged.")
    else:
        P("  VERDICT: NOT ACCEPTED — base unchanged.")

    if a.out:
        with open(a.out, "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")
        print(f"\nwritten {a.out}")


if __name__ == "__main__":
    sys.exit(main())
