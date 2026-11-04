#!/usr/bin/env python3
"""
E5 — analysis and charts for the prompt-optimisation experiment.

Usage
  python3 e5_analyze.py demo  --out figures_demo            # synthetic data, clearly labelled
  python3 e5_analyze.py run   --results registry/e5_results.csv \
                              --pairwise registry/e5_pairwise.csv --out figures_iter_N

Input: results CSV, one row per judged response (see registry/e5_results_template.csv):
  iteration, prompt_version, condition, task_id, task_set, run, block, generator_model,
  judge, order, n_elements, elements_hit, C1..C6, violations, invented_facts, word_count
Input: pairwise CSV, one row per judged pair (see registry/e5_pairwise_template.csv):
  iteration, task_id, task_set, run, judge, order, cond_1, cond_2, preferred, confidence
  (cond_x is "A", "B" or "C:v1.2-c"; preferred is "1", "2" or "tie")

Scoring (29c): elements = hit/n * 40; criteria = C1..C6 (max 60);
  total = elements + criteria - 2*violations, floored at 0.
"""
import argparse, os, sys, math, json
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

try:
    from scipy import stats as sps
except Exception:  # scipy optional
    sps = None

# ---- palette (validated default, dataviz reference instance; fixed slot order) ----
PAL = {"A": "#2a78d6",      # slot 1 blue  : no prompt
       "B": "#eb6834",      # slot 2 orange: generic structured adviser
       "C": "#1baf7a",      # slot 3 aqua  : canon + prompt (current version)
       "Cprev": "#6250d6",  # slot 7 violet: previous prompt version
       "band": "#d9d9d6", "text": "#0b0b0b", "muted": "#52514e", "grid": "#e6e6e3"}
SEQ = ["#cde2fb", "#9ec5f4", "#6da7ec", "#3987e5", "#256abf", "#184f95", "#0d366b"]
DIV_NEG, DIV_MID, DIV_POS = "#eb6834", "#d9d9d6", "#2a78d6"

plt.rcParams.update({"font.size": 10, "axes.edgecolor": PAL["muted"], "axes.labelcolor": PAL["text"],
                     "xtick.color": PAL["muted"], "ytick.color": PAL["muted"], "axes.spines.top": False,
                     "axes.spines.right": False, "figure.dpi": 130, "savefig.dpi": 160,
                     "axes.grid": True, "grid.color": PAL["grid"], "grid.linewidth": 0.6})

CRIT = ["C1", "C2", "C3", "C4", "C5", "C6"]
CRIT_NAMES = {"C1": "Accuracy", "C2": "Diagnosis", "C3": "Practicality", "C4": "Fit", "C5": "Control", "C6": "Honesty"}


# ---------------------------------------------------------------- scoring helpers
def add_scores(df):
    df = df.copy()
    df["elements_pct"] = df["elements_hit"] / df["n_elements"]
    df["elements_score"] = df["elements_pct"] * 40
    df["criteria_total"] = df[CRIT].sum(axis=1)
    df["total"] = (df["elements_score"] + df["criteria_total"] - 2 * df["violations"]).clip(lower=0)
    df["cond_key"] = np.where(df["condition"] == "C", "C:" + df["prompt_version"].astype(str), df["condition"])
    return df


def task_means(df, cols=("total", "criteria_total", "elements_pct", "violations", "invented_facts") + tuple(CRIT)):
    """Mean over runs, judges and orders -> one row per (iteration, cond_key, task_set, task_id)."""
    g = df.groupby(["iteration", "cond_key", "task_set", "task_id"])[list(cols)].mean().reset_index()
    return g


def paired_diff(tm, iteration, key_new, key_ref, task_set="dev", col="total", n_boot=10000, seed=0):
    """Paired (by task) difference new - ref with bootstrap CI, Wilcoxon, sign test, Cohen's d."""
    a = tm[(tm.iteration == iteration) & (tm.cond_key == key_new) & (tm.task_set == task_set)].set_index("task_id")[col]
    b = tm[(tm.iteration == iteration) & (tm.cond_key == key_ref) & (tm.task_set == task_set)].set_index("task_id")[col]
    idx = a.index.intersection(b.index)
    if len(idx) == 0:
        return None
    d = (a.loc[idx] - b.loc[idx]).values
    rng = np.random.default_rng(seed)
    boots = np.array([rng.choice(d, size=len(d), replace=True).mean() for _ in range(n_boot)])
    out = {"n_tasks": int(len(d)), "mean_diff": float(d.mean()), "ci_low": float(np.percentile(boots, 2.5)),
           "ci_high": float(np.percentile(boots, 97.5)), "sd": float(d.std(ddof=1)) if len(d) > 1 else float("nan"),
           "cohen_d": float(d.mean() / d.std(ddof=1)) if len(d) > 1 and d.std(ddof=1) > 0 else float("nan"),
           "n_positive": int((d > 0).sum()), "n_negative": int((d < 0).sum())}
    if sps is not None and len(d) >= 6 and np.any(d != 0):
        try:
            out["wilcoxon_p"] = float(sps.wilcoxon(d, zero_method="wilcox").pvalue)
        except Exception:
            out["wilcoxon_p"] = float("nan")
        k, n = int((d > 0).sum()), int((d != 0).sum())
        out["sign_test_p"] = float(sps.binomtest(k, n, 0.5).pvalue) if n > 0 else float("nan")
    return out


def noise_band(df, iteration=0, key="C:v1.0", task_set="dev"):
    """Test-retest noise from two independent blocks of the same condition: 2*SE of the per-task block difference."""
    sub = df[(df.iteration == iteration) & (df.cond_key == key) & (df.task_set == task_set) & df["block"].notna()]
    if sub.empty or sub["block"].nunique() < 2:
        return None
    m = sub.groupby(["task_id", "block"])["total"].mean().unstack("block")
    blocks = list(m.columns)[:2]
    d = (m[blocks[0]] - m[blocks[1]]).dropna()
    if len(d) < 2:
        return None
    se = d.std(ddof=1) / math.sqrt(len(d))
    return {"n_tasks": int(len(d)), "block_diff_mean": float(d.mean()), "se": float(se), "band": float(2 * se)}


def wilson(k, n, z=1.96):
    if n == 0:
        return (float("nan"), float("nan"), float("nan"))
    p = k / n
    den = 1 + z * z / n
    c = (p + z * z / (2 * n)) / den
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return (p, c - h, c + h)


def win_rates(pw):
    """A pair counts as a win for cond X only if X is preferred in both orders (12 and 21); else tie."""
    rows = []
    key = ["iteration", "task_set", "task_id", "run", "judge", "cond_1", "cond_2"]
    pw = pw.copy()
    # normalise so cond_1/cond_2 pair is order-independent: store preferred condition name
    pw["pref_cond"] = np.where(pw.preferred.astype(str) == "1", pw.cond_1,
                               np.where(pw.preferred.astype(str) == "2", pw.cond_2, "tie"))
    pw["pair"] = pw.apply(lambda r: tuple(sorted([r.cond_1, r.cond_2])), axis=1)
    for (it, ts, task, run, judge, pair), g in pw.groupby(["iteration", "task_set", "task_id", "run", "judge", "pair"]):
        prefs = set(g.pref_cond)
        winner = prefs.pop() if len(prefs) == 1 and "tie" not in prefs else "tie"
        rows.append({"iteration": it, "task_set": ts, "task_id": task, "run": run, "judge": judge,
                     "cond_x": pair[0], "cond_y": pair[1], "winner": winner})
    res = pd.DataFrame(rows)
    out = []
    for (it, ts, cx, cy), g in res.groupby(["iteration", "task_set", "cond_x", "cond_y"]):
        n = len(g)
        for c in (cx, cy):
            k = int((g.winner == c).sum())
            p, lo, hi = wilson(k, n)
            out.append({"iteration": it, "task_set": ts, "cond": c, "vs": cy if c == cx else cx,
                        "wins": k, "ties": int((g.winner == "tie").sum()), "n": n, "win_rate": p, "ci_low": lo, "ci_high": hi})
    return pd.DataFrame(out)


# ---------------------------------------------------------------- figures
def _dump(frame, out, name):
    """Write the data behind a figure next to it (figure_data/<name>.csv) so every plotted number is traceable."""
    d = os.path.join(out, "figure_data"); os.makedirs(d, exist_ok=True)
    pd.DataFrame(frame).to_csv(os.path.join(d, name + ".csv"), index=True)


def _ci_by_task(tm, mask, col="total"):
    v = tm[mask][col].values
    if len(v) == 0:
        return (float("nan"),) * 3
    rng = np.random.default_rng(1)
    boots = [rng.choice(v, len(v), replace=True).mean() for _ in range(4000)]
    return (float(v.mean()), float(np.percentile(boots, 2.5)), float(np.percentile(boots, 97.5)))


def fig1_total_by_iteration(tm, versions_by_iter, band, out, tag):
    its = sorted(tm.iteration.unique())
    dump = []
    fig, ax = plt.subplots(figsize=(8, 4.6))
    series = {"A": ("A — no prompt", PAL["A"]), "B": ("B — generic structured adviser", PAL["B"])}
    for cond, (label, color) in series.items():
        xs, ys, lo, hi = [], [], [], []
        for it in its:
            m = (tm.iteration == it) & (tm.cond_key == cond) & (tm.task_set == "dev")
            if m.any():
                mu, l, h = _ci_by_task(tm, m)
                xs.append(it); ys.append(mu); lo.append(l); hi.append(h)
                dump.append({"iteration": it, "cond_key": cond, "mean_total": mu, "ci_low": l, "ci_high": h, "n_tasks": int(m.sum())})
        if xs:
            ax.errorbar(xs, ys, yerr=[np.array(ys) - lo, np.array(hi) - ys], color=color, lw=2, marker="o", ms=7,
                        capsize=3, label=label)
            ax.annotate(f"{ys[-1]:.1f}", (xs[-1], ys[-1]), textcoords="offset points", xytext=(8, -4), color=PAL["text"])
    xs, ys, lo, hi = [], [], [], []
    for it in its:
        v = versions_by_iter.get(it)
        m = (tm.iteration == it) & (tm.cond_key == f"C:{v}") & (tm.task_set == "dev")
        if v and m.any():
            mu, l, h = _ci_by_task(tm, m)
            xs.append(it); ys.append(mu); lo.append(l); hi.append(h)
            dump.append({"iteration": it, "cond_key": f"C:{v}", "mean_total": mu, "ci_low": l, "ci_high": h, "n_tasks": int(m.sum()),
                         "noise_band": band["band"] if band else float("nan")})
    _dump(pd.DataFrame(dump).set_index("iteration"), out, "fig1_total_by_iteration")
    if xs:
        ax.errorbar(xs, ys, yerr=[np.array(ys) - lo, np.array(hi) - ys], color=PAL["C"], lw=2.2, marker="o", ms=7,
                    capsize=3, label="C — canon + operating prompt (version under test)")
        for x, y in zip(xs, ys):
            ax.annotate(f"{y:.1f}", (x, y), textcoords="offset points", xytext=(0, 9), ha="center", color=PAL["text"])
        for x, it in zip(xs, [i for i in its if versions_by_iter.get(i)]):
            ax.annotate(versions_by_iter[it], (x, ax.get_ylim()[0]), textcoords="offset points", xytext=(0, 4),
                        ha="center", color=PAL["muted"], fontsize=8)
        if band and ys:
            ax.axhspan(ys[0] - band["band"], ys[0] + band["band"], color=PAL["band"], alpha=0.5, lw=0,
                       label=f"noise band around v1.0 (±{band['band']:.1f})")
    ax.set_xticks(its); ax.set_xlabel("Iteration"); ax.set_ylabel("Mean total score (0–100), dev set; 95 % CI by task")
    ax.set_title(f"E5 — total score by iteration{tag}", loc="left", color=PAL["text"])
    ax.legend(frameon=False, fontsize=8, loc="upper center", bbox_to_anchor=(0.5, -0.14), ncol=2)
    fig.tight_layout(); fig.savefig(os.path.join(out, "fig1_total_by_iteration.png"), bbox_inches="tight"); plt.close(fig)


AQUA_RAMP = ["#9fe3c8", "#5fcba3", "#1baf7a", "#128a60", "#0a6646"]  # one hue, light -> dark, for ordered prompt versions


BASE_KEY = None  # set in analyze(): the reference (base = last accepted) C version of the latest iteration


def _select_keys(keys):
    """A, B, and at most three C versions (first, base of the latest iteration, last) so the chart stays legible.
    Up to iteration 2 the base was always the middle version; from iteration 3 (v1.2-c rejected) the base is v1.1-c."""
    cs = [k for k in keys if k.startswith("C:")]
    if len(cs) > 3:
        mid = BASE_KEY if BASE_KEY in cs[1:-1] else cs[len(cs) // 2]
        cs = [cs[0], mid, cs[-1]]
    return [k for k in keys if k in ("A", "B")] + cs


def fig2_criteria(tm, keys, out, tag):
    keys = _select_keys([k for k in keys if (tm.cond_key == k).any()])
    fig, ax = plt.subplots(figsize=(8.5, 4.4))
    w = 0.8 / max(len(keys), 1)
    x = np.arange(len(CRIT))
    ci = 0
    dump = {}
    for i, k in enumerate(keys):
        sub = tm[(tm.cond_key == k) & (tm.task_set == "dev")]
        it = sub.iteration.max()
        sub = sub[sub.iteration == it]
        vals = [sub[c].mean() for c in CRIT]
        dump[k] = dict(zip(CRIT, vals)); dump[k]["iteration"] = int(it)
        if k == "A":
            color = PAL["A"]
        elif k == "B":
            color = PAL["B"]
        else:
            color = AQUA_RAMP[[1, 2, 4][ci] if len([q for q in keys if q.startswith("C:")]) == 3 else [2, 4][ci]] if ci < 3 else AQUA_RAMP[4]; ci += 1
        ax.bar(x + i * w - 0.4 + w / 2, vals, width=w * 0.92, color=color, label=k, linewidth=0)
        for xi, v in zip(x, vals):
            ax.text(xi + i * w - 0.4 + w / 2, v + 0.1, f"{v:.1f}", ha="center", fontsize=7, color=PAL["text"])
    _dump(pd.DataFrame(dump).T, out, "fig2_criteria_by_version")
    ax.set_xticks(x); ax.set_xticklabels([f"{c}\n{CRIT_NAMES[c]}" for c in CRIT]); ax.set_ylim(0, 10.8)
    ax.set_ylabel("Mean criterion score (1–10), dev set")
    ax.set_title(f"E5 — six criteria by version{tag}", loc="left"); ax.legend(frameon=False, fontsize=8, ncol=len(keys))
    fig.tight_layout(); fig.savefig(os.path.join(out, "fig2_criteria_by_version.png")); plt.close(fig)


def fig3_heatmap(tm, versions_by_iter, out, tag):
    rows = []
    for it, v in sorted(versions_by_iter.items()):
        c = tm[(tm.iteration == it) & (tm.cond_key == f"C:{v}") & (tm.task_set == "dev")].set_index("task_id")["total"]
        a = tm[(tm.iteration == it) & (tm.cond_key == "A") & (tm.task_set == "dev")].set_index("task_id")["total"]
        if a.empty:  # fall back to the latest A available
            a = tm[(tm.cond_key == "A") & (tm.task_set == "dev")].groupby("task_id")["total"].mean()
        d = (c - a).dropna(); d.name = v; rows.append(d)
    if not rows:
        return
    M = pd.concat(rows, axis=1)
    _dump(M, out, "fig3_task_heatmap")
    fig, ax = plt.subplots(figsize=(max(8.5, 1.2 + 0.9 * M.shape[1]), 1.0 + 0.42 * M.shape[0]))
    lim = max(5, np.nanmax(np.abs(M.values)))
    im = ax.imshow(M.values, cmap=matplotlib.colors.LinearSegmentedColormap.from_list("div", [DIV_NEG, DIV_MID, DIV_POS]),
                   vmin=-lim, vmax=lim, aspect="auto")
    ax.set_xticks(range(M.shape[1])); ax.set_xticklabels(M.columns); ax.set_yticks(range(M.shape[0])); ax.set_yticklabels(M.index)
    ax.grid(False)
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            ax.text(j, i, f"{M.values[i, j]:+.0f}", ha="center", va="center", fontsize=8, color=PAL["text"])
    cb = fig.colorbar(im, ax=ax, fraction=0.04, pad=0.02); cb.set_label("C − A, total score points")
    ax.set_title(f"E5 — gain over no-prompt by task and version{tag}", loc="left")
    fig.tight_layout(); fig.savefig(os.path.join(out, "fig3_task_heatmap.png")); plt.close(fig)


def fig4_winrate(wr, versions_by_iter, out, tag):
    sub = wr[(wr.task_set == "dev")].copy()
    sub = sub[[c == f"C:{versions_by_iter.get(int(i), '')}" for c, i in zip(sub.cond, sub.iteration)]]
    if sub.empty:
        return
    sub["vs_group"] = np.where(sub.vs == "A", "A", np.where(sub.vs == "B", "B", "base version (last accepted)"))
    sub = sub.sort_values(["vs_group", "iteration"])
    _dump(sub.set_index("iteration"), out, "fig4_winrate")
    fig, ax = plt.subplots(figsize=(8, 4.2))
    for i, (vs, g) in enumerate(sub.groupby("vs_group")):
        color = PAL["A"] if vs == "A" else PAL["B"] if vs == "B" else PAL["Cprev"]
        ax.errorbar(g.iteration + i * 0.08, g.win_rate, yerr=[g.win_rate - g.ci_low, g.ci_high - g.win_rate], marker="o", ms=7,
                    lw=2, capsize=3, color=color, label=f"C(vN) vs {vs}")
        for x, y in zip(g.iteration + i * 0.08, g.win_rate):
            ax.annotate(f"{y:.2f}", (x, y), textcoords="offset points", xytext=(0, 8), ha="center", fontsize=7, color=PAL["text"])
    ax.axhline(0.5, color=PAL["muted"], lw=1, ls="--"); ax.set_ylim(0, 1.02)
    ax.set_xlabel("Iteration"); ax.set_ylabel("Win rate of C (both orders agree), Wilson 95 % CI")
    ax.set_title(f"E5 — pairwise win rate{tag}", loc="left"); ax.legend(frameon=False, fontsize=8)
    fig.tight_layout(); fig.savefig(os.path.join(out, "fig4_winrate.png")); plt.close(fig)


def fig5_dev_vs_holdout(tm, out, tag):
    keys = [k for k in tm.cond_key.unique() if (tm[(tm.cond_key == k) & (tm.task_set == "holdout")].shape[0] > 0)]
    if not keys:
        return
    keys = sorted(keys, key=lambda k: (k[0] != "C", k))
    fig, ax = plt.subplots(figsize=(7.5, 4.2))
    x = np.arange(len(keys)); w = 0.38
    dump = []
    for j, (ts, color) in enumerate([("dev", SEQ[4]), ("holdout", SEQ[1])]):
        vals, los, his = [], [], []
        for k in keys:
            sub = tm[(tm.cond_key == k) & (tm.task_set == ts)]
            it = sub.iteration.max(); m = (tm.cond_key == k) & (tm.task_set == ts) & (tm.iteration == it)
            mu, l, h = _ci_by_task(tm, m); vals.append(mu); los.append(l); his.append(h)
            dump.append({"cond_key": k, "task_set": ts, "iteration": int(it), "mean_total": mu, "ci_low": l, "ci_high": h})
        ax.bar(x + (j - 0.5) * w, vals, width=w * 0.94, color=color, label=f"{ts} set", linewidth=0)
        ax.errorbar(x + (j - 0.5) * w, vals, yerr=[np.array(vals) - los, np.array(his) - vals], fmt="none", ecolor=PAL["text"], capsize=3, lw=1)
        for xi, v, h in zip(x, vals, his):
            ax.text(xi + (j - 0.5) * w, h + 1.2, f"{v:.1f}", ha="center", fontsize=8, color=PAL["text"])
    _dump(pd.DataFrame(dump).set_index("cond_key"), out, "fig5_dev_vs_holdout")
    ax.set_xticks(x); ax.set_xticklabels(keys); ax.set_ylim(0, 100); ax.set_ylabel("Mean total score (0–100)")
    ax.set_title(f"E5 — development vs hold-out set (overfitting check){tag}", loc="left"); ax.legend(frameon=False, fontsize=8)
    fig.tight_layout(); fig.savefig(os.path.join(out, "fig5_dev_vs_holdout.png")); plt.close(fig)


def fig6_distribution(df, keys, out, tag):
    keys = _select_keys([k for k in keys if (df.cond_key == k).any()])
    data, labels, colors = [], [], []
    for k in keys:
        sub = df[(df.cond_key == k) & (df.task_set == "dev")]
        it = sub.iteration.max(); sub = sub[sub.iteration == it]
        data.append(sub.total.values); labels.append(k)
        colors.append(PAL["A"] if k == "A" else PAL["B"] if k == "B" else PAL["C"])
    _dump(pd.DataFrame({k: pd.Series(v).describe(percentiles=[.05, .25, .5, .75, .95]) for k, v in zip(labels, data)}).T, out, "fig6_distribution")
    fig, ax = plt.subplots(figsize=(8, 4.2))
    bp = ax.boxplot(data, widths=0.5, patch_artist=True, showfliers=True,
                    medianprops={"color": PAL["text"], "lw": 1.5}, whiskerprops={"color": PAL["muted"]}, capprops={"color": PAL["muted"]})
    ax.set_xticks(range(1, len(labels) + 1)); ax.set_xticklabels(labels)
    for patch, c in zip(bp["boxes"], colors):
        patch.set_facecolor(c); patch.set_alpha(0.55); patch.set_edgecolor(c)
    ax.set_ylabel("Total score per judged response (all runs, orders, judges)"); ax.set_ylim(0, 100)
    ax.set_title(f"E5 — score distribution by version (worst cases matter){tag}", loc="left")
    fig.tight_layout(); fig.savefig(os.path.join(out, "fig6_distribution.png")); plt.close(fig)


def fig7_elements_violations(tm, keys, out, tag):
    keys = _select_keys([k for k in keys if (tm.cond_key == k).any()])
    fig, axes = plt.subplots(1, 2, figsize=(9, 3.8))
    dump = {}
    for ax, col, lab in zip(axes, ["elements_pct", "violations"], ["Mandatory elements present (%)", "Violations per response (forbidden + hard checks)"]):
        vals = []
        for k in keys:
            sub = tm[(tm.cond_key == k) & (tm.task_set == "dev")]; it = sub.iteration.max()
            v = sub[sub.iteration == it][col].mean(); vals.append(v * 100 if col == "elements_pct" else v)
            dump.setdefault(k, {"iteration": int(it)})[col] = vals[-1]
        cols = [PAL["A"] if k == "A" else PAL["B"] if k == "B" else PAL["C"] for k in keys]
        ax.bar(range(len(keys)), vals, color=cols, linewidth=0, width=0.6)
        for i, v in enumerate(vals):
            ax.text(i, v + (1.5 if col == "elements_pct" else 0.05), f"{v:.1f}" if col == "elements_pct" else f"{v:.2f}", ha="center", fontsize=8)
        ax.set_xticks(range(len(keys))); ax.set_xticklabels(keys, fontsize=8); ax.set_title(lab, loc="left", fontsize=9)
        if col == "elements_pct":
            ax.set_ylim(0, 105)
    _dump(pd.DataFrame(dump).T, out, "fig7_elements_violations")
    fig.suptitle(f"E5 — is the prompt being followed?{tag}", x=0.01, ha="left", fontsize=10)
    fig.tight_layout(); fig.savefig(os.path.join(out, "fig7_elements_violations.png")); plt.close(fig)


def fig8_models(df, out, tag):
    if "generator_model" not in df.columns or df.generator_model.nunique() < 2:
        return
    sub = df[df.task_set == "dev"]
    piv = sub.groupby(["generator_model", "cond_key"])["total"].mean().unstack("cond_key")
    piv = piv[[c for c in ["A", "B"] + sorted([c for c in piv.columns if c.startswith("C:")]) if c in piv.columns]]
    _dump(piv, out, "fig8_models")
    fig, ax = plt.subplots(figsize=(8, 4.2))
    x = np.arange(len(piv.index)); w = 0.8 / piv.shape[1]
    for i, c in enumerate(piv.columns):
        color = PAL["A"] if c == "A" else PAL["B"] if c == "B" else SEQ[min(2 + i, 6)]
        ax.bar(x + i * w - 0.4 + w / 2, piv[c].values, width=w * 0.92, color=color, label=c, linewidth=0)
    ax.set_xticks(x); ax.set_xticklabels(piv.index); ax.set_ylim(0, 100); ax.set_ylabel("Mean total score (0–100)")
    ax.set_title(f"E5 — transfer across generating models{tag}", loc="left"); ax.legend(frameon=False, fontsize=8, ncol=3)
    fig.tight_layout(); fig.savefig(os.path.join(out, "fig8_models.png")); plt.close(fig)


# ---------------------------------------------------------------- summary
def analyze(results_csv, pairwise_csv, out, tag=""):
    os.makedirs(out, exist_ok=True)
    df = add_scores(pd.read_csv(results_csv))
    df["iteration"] = df["iteration"].astype(int)
    pw = pd.read_csv(pairwise_csv) if pairwise_csv and os.path.exists(pairwise_csv) else pd.DataFrame()
    if not pw.empty:
        pw["iteration"] = pw["iteration"].astype(int)
    tm = task_means(df)
    # version under test per iteration = the C version whose first appearance is that iteration
    versions_by_iter = {}
    for it in sorted(int(i) for i in df.iteration.unique()):
        cv = df[(df.iteration == it) & (df.condition == "C")]["prompt_version"].dropna().unique()
        if len(cv):
            new = [v for v in cv if df[(df.condition == "C") & (df.prompt_version == v)].iteration.min() == it]
            versions_by_iter[it] = sorted(new)[-1] if new else sorted(cv)[-1]
    band = noise_band(df)
    lines = [f"# E5 summary{tag}", "", f"Rows: {len(df)}; iterations: {sorted(df.iteration.unique())}; versions: {versions_by_iter}", ""]
    if band:
        lines += [f"**Noise band (test–retest, v1.0 two blocks):** SE = {band['se']:.2f}, band = ±{band['band']:.2f} points "
                  f"(block difference mean {band['block_diff_mean']:+.2f}, n = {band['n_tasks']} tasks)", ""]
    lines += ["| iteration | comparison | n tasks | mean diff | 95 % CI | Cohen d | tasks +/− | Wilcoxon p | sign p |", "|---|---|---|---|---|---|---|---|---|"]
    prev = None
    for it in sorted(versions_by_iter):
        v = versions_by_iter[it]; key = f"C:{v}"
        # reference C version(s) = the other C version(s) judged in this same iteration (the base = last accepted version,
        # 29 §5.4). Up to iteration 2 this was always the previous iteration's version; from iteration 3 (v1.2-c rejected)
        # the base is v1.1-c, so the reference is taken from the data, not from the iteration number.
        base_refs = [f"C:{x}" for x in sorted(df[(df.iteration == it) & (df.condition == "C")]["prompt_version"].dropna().unique()) if x != v]
        for ref in ["A", "B"] + (base_refs or ([f"C:{prev}"] if prev else [])):
            if ref is None:
                continue
            r = paired_diff(tm, it, key, ref)
            if r:
                lines.append(f"| {it} | {key} − {ref} | {r['n_tasks']} | {r['mean_diff']:+.2f} | [{r['ci_low']:+.2f}, {r['ci_high']:+.2f}] | "
                             f"{r['cohen_d']:.2f} | {r['n_positive']}/{r['n_negative']} | {r.get('wilcoxon_p', float('nan')):.3f} | {r.get('sign_test_p', float('nan')):.3f} |")
        # hold-out
        for ref in ["A", "B"] + (base_refs or ([f"C:{prev}"] if prev else [])) + ["C:v1.0"]:
            if ref is None or ref == key:
                continue
            r = paired_diff(tm, it, key, ref, task_set="holdout")
            if r:
                lines.append(f"| {it} | HOLDOUT {key} − {ref} | {r['n_tasks']} | {r['mean_diff']:+.2f} | [{r['ci_low']:+.2f}, {r['ci_high']:+.2f}] | "
                             f"{r['cohen_d']:.2f} | {r['n_positive']}/{r['n_negative']} | {r.get('wilcoxon_p', float('nan')):.3f} | {r.get('sign_test_p', float('nan')):.3f} |")
        prev = v
        global BASE_KEY
        BASE_KEY = base_refs[0] if base_refs else None
    # per-version means table
    lines += ["", "| version/condition | set | iteration | total | criteria (60) | elements % | violations | invented facts | " + " | ".join(CRIT) + " |",
              "|---|---|---|---|---|---|---|---|" + "---|" * len(CRIT)]
    for (k, ts, it), g in tm.groupby(["cond_key", "task_set", "iteration"]):
        lines.append(f"| {k} | {ts} | {it} | {g.total.mean():.1f} | {g.criteria_total.mean():.1f} | {100*g.elements_pct.mean():.0f} | "
                     f"{g.violations.mean():.2f} | {g.invented_facts.mean():.2f} | " + " | ".join(f"{g[c].mean():.1f}" for c in CRIT) + " |")
    wr = win_rates(pw) if not pw.empty else pd.DataFrame()
    if not wr.empty:
        lines += ["", "| iteration | set | cond | vs | wins | ties | n | win rate | Wilson 95 % CI |", "|---|---|---|---|---|---|---|---|---|"]
        for _, r in wr.iterrows():
            lines.append(f"| {r.iteration} | {r.task_set} | {r.cond} | {r.vs} | {r.wins} | {r.ties} | {r.n} | {r.win_rate:.2f} | [{r.ci_low:.2f}, {r.ci_high:.2f}] |")
    with open(os.path.join(out, "summary.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    tm.to_csv(os.path.join(out, "task_means.csv"), index=False)
    keys_order = ["A", "B"] + [f"C:{versions_by_iter[i]}" for i in sorted(versions_by_iter)]
    fig1_total_by_iteration(tm, versions_by_iter, band, out, tag)
    fig2_criteria(tm, keys_order, out, tag)
    fig3_heatmap(tm, versions_by_iter, out, tag)
    if not wr.empty:
        fig4_winrate(wr, versions_by_iter, out, tag)
    fig5_dev_vs_holdout(tm, out, tag)
    fig6_distribution(df, keys_order, out, tag)
    fig7_elements_violations(tm, keys_order, out, tag)
    fig8_models(df, out, tag)
    print("\n".join(lines))
    print(f"\nfigures written to {out}")


# ---------------------------------------------------------------- synthetic demo data
def make_demo(out, seed=7):
    """Synthetic data ONLY to show the shape of the outputs. Numbers are invented."""
    rng = np.random.default_rng(seed)
    tasks = [f"T{i:02d}" for i in range(1, 11)]; htasks = [f"H{i:02d}" for i in range(1, 11)]
    task_diff = dict(zip(tasks + htasks, rng.normal(0, 4, 20)))          # task difficulty
    n_el = {t: int(rng.integers(7, 11)) for t in tasks + htasks}
    versions = {0: "v1.0", 1: "v1.1-c", 2: "v1.2-c", 3: "v1.3-c", 4: "v1.4-c", 5: "v1.5-c"}
    gain = {"v1.0": 0, "v1.1-c": 2.5, "v1.2-c": 4.0, "v1.3-c": 3.6, "v1.4-c": 5.5, "v1.5-c": 6.5}  # invented trajectory incl. one dip
    base = {"A": 58, "B": 66, "C": 72}
    rows, prows = [], []

    def resp(cond, ver, task, it, run, block, ts, judge="J1"):
        mu = base[cond] + task_diff[task] + (gain[ver] if cond == "C" else 0)
        total = np.clip(rng.normal(mu, 5), 20, 98)
        el_pct = np.clip((total / 100) * (1.05 if cond == "C" else 0.9) + rng.normal(0, 0.07), 0.2, 1.0)
        el_hit = int(round(el_pct * n_el[task]))
        crit_mean = np.clip(total / 10 + rng.normal(0, 0.3), 2, 10)
        crits = np.clip(rng.normal(crit_mean, 0.8, 6), 1, 10).round()
        viol = max(0, int(rng.poisson(0.9 if cond == "A" else 0.6 if cond == "B" else max(0.1, 0.5 - 0.05 * gain[ver]))))
        inv = max(0, int(rng.poisson(0.7 if cond == "A" else 0.3 if cond == "B" else 0.15)))
        out_rows = []
        for order in ("12", "21"):
            out_rows.append({"iteration": it, "prompt_version": ver if cond == "C" else "", "condition": cond, "task_id": task,
                             "task_set": ts, "run": run, "block": block, "generator_model": "sonnet-5.5", "judge": judge, "order": order,
                             "n_elements": n_el[task], "elements_hit": el_hit, **{f"C{i+1}": int(crits[i]) for i in range(6)},
                             "violations": viol, "invented_facts": inv, "word_count": int(rng.integers(250, 650))})
        return out_rows

    def pair(it, task, ts, run, c1, c2, strength):
        # one latent judgement per pair; each order reports it with 90 % consistency, else a tie
        u = rng.random()
        latent = c1 if u < strength else (c2 if u < strength + (1 - strength) * 0.6 else "tie")
        for order in ("12", "21"):
            a, b = (c1, c2) if order == "12" else (c2, c1)
            seen = latent if rng.random() < 0.9 else "tie"
            pref = "tie" if seen == "tie" else ("1" if seen == a else "2")
            prows.append({"iteration": it, "task_id": task, "task_set": ts, "run": run, "judge": "J1", "order": order,
                          "cond_1": a, "cond_2": b, "preferred": pref, "confidence": round(float(rng.uniform(0.55, 0.95)), 2)})

    for it, ver in versions.items():
        prev = versions.get(it - 1)
        for t in tasks:
            for run in (1, 2, 3):
                rows += resp("A", "", t, it, run, "", "dev")
                rows += resp("C", ver, t, it, run, 1 if it == 0 else "", "dev")
                if it == 0:
                    rows += resp("B", "", t, it, run, "", "dev")
                    rows += resp("C", ver, t, it, run + 3, 2, "dev")          # second block for noise
                if prev and it > 0:
                    rows += resp("C", prev, t, it, run, "", "dev")
                pair(it, t, "dev", run, f"C:{ver}", "A", 0.85)
                if prev:
                    pair(it, t, "dev", run, f"C:{ver}", f"C:{prev}", 0.5 + 0.06 * (gain[ver] - gain[prev]))
                if it == 5:
                    pair(it, t, "dev", run, f"C:{ver}", "B", 0.7)
        if it in (0, 5):
            for t in htasks:
                for run in (1, 2, 3):
                    rows += resp("A", "", t, it, run, "", "holdout"); rows += resp("B", "", t, it, run, "", "holdout")
                    rows += resp("C", ver, t, it, run, "", "holdout")
                    if it == 5:
                        rows += resp("C", "v1.0", t, it, run, "", "holdout")
    os.makedirs(out, exist_ok=True)
    rpath, ppath = os.path.join(out, "demo_results.csv"), os.path.join(out, "demo_pairwise.csv")
    pd.DataFrame(rows).to_csv(rpath, index=False); pd.DataFrame(prows).to_csv(ppath, index=False)
    return rpath, ppath



def make_panel(d, it):
    """One composite PNG of the standard figure set (fig1..fig8 that exist), 2 columns, identical layout each iteration."""
    from PIL import Image, ImageDraw, ImageFont
    names = ["fig1_total_by_iteration", "fig2_criteria_by_version", "fig3_task_heatmap", "fig4_winrate",
             "fig5_dev_vs_holdout", "fig6_distribution", "fig7_elements_violations", "fig8_models"]
    present = [n for n in names if os.path.exists(os.path.join(d, n + ".png"))]
    ims = [Image.open(os.path.join(d, n + ".png")).convert("RGB") for n in present]
    w = max(i.width for i in ims); h = max(i.height for i in ims); cols = 2; rows = (len(ims) + 1) // 2; pad = 30; th = 90
    panel = Image.new("RGB", (cols * w + (cols + 1) * pad, rows * h + (rows + 1) * pad + th), "white")
    dr = ImageDraw.Draw(panel)
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 40)
    except Exception:
        font = ImageFont.load_default()
    missing = [n.split("_")[0] for n in names if n not in present]
    dr.text((pad, 25), f"E5 — Iteration {it}: standard figure set ({', '.join(n.split('_')[0] for n in present)}"
            + (f"; {', '.join(missing)} appear with hold-out / model data)" if missing else ")"), fill="black", font=font)
    for k, im in enumerate(ims):
        r, c = divmod(k, cols); panel.paste(im, (pad + c * (w + pad), th + pad + r * (h + pad)))
    out = os.path.join(d, f"panel_iter_{it}.png"); panel.save(out, optimize=True); print("panel ->", out, panel.size)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    d = sub.add_parser("demo"); d.add_argument("--out", default="figures_demo")
    pn = sub.add_parser("panel", help="compose fig1-fig8 (those present) into one PNG, same layout every iteration")
    pn.add_argument("--dir", required=True); pn.add_argument("--iter", type=int, required=True)
    r = sub.add_parser("run"); r.add_argument("--results", required=True); r.add_argument("--pairwise", default=None)
    r.add_argument("--out", default="figures"); r.add_argument("--tag", default="")
    a = ap.parse_args()
    if a.cmd == "panel":
        make_panel(a.dir, a.iter); return
    if a.cmd == "demo":
        rp, pp = make_demo(a.out)
        analyze(rp, pp, a.out, tag="  [DEMO: synthetic data]")
    else:
        analyze(a.results, a.pairwise, a.out, tag=(f"  [{a.tag}]" if a.tag else ""))


if __name__ == "__main__":
    main()
