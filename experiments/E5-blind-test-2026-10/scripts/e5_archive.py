#!/usr/bin/env python3
"""
E5 — build the human-readable archive tree (deterministic, same layout for every iteration).

Usage: python3 e5_archive.py --out /mnt/user-data/outputs/E5_eksperiments [--iters 0,1]

Layout (mirrors E:\\GitHub\\E5_eksperiments on Martin's disk):
  README.md
  00_kopejais/
     protokols/   29_*.md, 29a–29d, 30_*.md
     prompti/     02a_canon_v1.0.md, 02b_v1.0.md, 02b_v1.1-c.md, ...
     uzdevumi/    tasks.json
     skripti/     e5_*.py
     registrs/    e5_run_log.md, e5_run_config.json, e5_STATUS_*.md, E5_RESTORE.md
     kalibracija/ packs/*.md, judgments/*.md (+ bundles)
  iter_0/ … iter_4/ final/      SAME layout for every iteration (see STANDARD below); every folder exists even when empty and
                                carries _STATUSS.md (what is there / why empty), rewritten on every run so it never goes stale
     README.md  SALIDZINAJUMS.md  decisions.md
     prompt/  packs/{gen,judge}/ + gen_index.csv, judge_index.csv  responses/ (+INDEX.csv)  hardchecks/
     judgments/ (+INDEX.csv)  judgments_rejudge/  judgments_J2_gemini/  analysis/{figure_data}/  error_analysis/
Nothing is rewritten: files are copied byte-for-byte from the working directory.
"""
import argparse, csv, glob, os, shutil, hashlib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def cp(src, dst_dir, name=None):
    """Copy src into dst_dir unless an identical file is already there (PNG: identical pixel data — the export mount
    re-stamps every rewritten PNG with a new provenance chunk, so rewriting unchanged figures would churn the archive)."""
    if not os.path.exists(src):
        return 0
    os.makedirs(dst_dir, exist_ok=True)
    dst = os.path.join(dst_dir, name or os.path.basename(src))
    if os.path.exists(dst):
        same = png_pixel_sha(src) == png_pixel_sha(dst) if src.lower().endswith(".png") else sha(src) == sha(dst)
        if same:
            return 1
    shutil.copy2(src, dst)
    return 1


def cp_glob(pattern, dst_dir):
    return sum(cp(p, dst_dir) for p in sorted(glob.glob(pattern)))


def png_pixel_sha(p):
    """SHA-256 of the concatenated IDAT chunks only: stable identity of a PNG regardless of provenance (caBX) or text chunks."""
    import struct
    d = open(p, "rb").read(); pos = 8; h = hashlib.sha256()
    while pos + 8 <= len(d):
        L = struct.unpack(">I", d[pos:pos + 4])[0]; typ = d[pos + 4:pos + 8]
        if typ == b"IDAT":
            h.update(d[pos + 8:pos + 8 + L])
        pos += 12 + L
    return h.hexdigest()


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


ALL_ITERS = [0, 1, 2, 3, 4, "final"]

# The standard layout of EVERY iteration folder: (relative path, description). Same list for iter_0 … iter_4 and final.
STANDARD = [
    ("README.md", "iterācijas karte: stāvoklis, skaiti, šī struktūra ar katras daļas statusu"),
    ("SALIDZINAJUMS.md", "standarta salīdzinājums: iepriekšējā → izmaiņas → rezultāts → paturēt/atgriezt (iter_0: bāzes līnija pret A un B)"),
    ("decisions.md", "iterācijas lēmumi ar pamatojumu"),
    ("prompt/", "testējamā operatīvā prompta versija (02b_vN.md)"),
    ("packs/", "gen_index.csv (kas ģenerēts), judge_index.csv (kas ar ko pārots, kurā kārtībā)"),
    ("packs/gen/", "ģenerēšanas pakas: SYSTEM + ATTACHMENT + USER, tieši tas, ko saņēma ģenerators"),
    ("packs/judge/", "tiesneša pakas: tiesneša prompts + uzdevums + atslēga + 2 anonīmas atbildes"),
    ("responses/", "katra atbilde atsevišķā failā {nosacījums}_{uzdevums}_{atkārtojums}.md + sainis(-ņi) + INDEX.csv"),
    ("hardchecks/", "automātiskās cietās pārbaudes (vārdi, jautājumi, valoda, iekšējie marķieri)"),
    ("judgments/", "katrs J1 tiesneša vērtējums (6 soļi prozā + JSON) {pāris}_{kārtība}.md + sainis + INDEX.csv"),
    ("judgments_rejudge/", "tie paši pāri vērtēti atkārtoti (test–retest); iesaldēto rezultātu nemaina"),
    ("judgments_J2_gemini/", "otrā tiesneša (Gemini, cita modeļu saime) vērtējumi tām pašām pakām"),
    ("analysis/", "summary.md, task_means.csv, iesaldētie momentuzņēmumi, fig1…fig8, panel_iter_N.png"),
    ("analysis/figure_data/", "skaitļi aiz katra attēla (CSV)"),
    ("error_analysis/", "kļūdu analīze + izmaiņu paka nākamajai versijai (.md apraksts, .json precīzi aizstājumi, .diff teksta starpība)"),
]

GEN_PROVENANCE = {
    0: "Ģenerēšanas pakas `gen/` ir **atjaunotas 2026-10-17** ar `00_kopejais/skripti/e5_packs.py regen --iter 0` no `gen_index.csv` un iesaldētajiem ievaddatiem (uzdevumi `tasks.json`, kanons `02a_canon_v1.0.md`, prompts `02b_v1.0.md`, kontroles prompts 29d). Oriģinālās pakas netika arhivētas (zaudētas konteinera maiņā 2026-10-16). Determinisms pārbaudīts: `regen` iterācijai 2 dod 30/30 baitu identiskas pakas ar oriģinālajām, un A/B/C ceļi dod 150/150 identiskas pakas ar `gen` komandu.",
    1: "Ģenerēšanas pakas `gen/` ir **atjaunotas 2026-10-17** ar `00_kopejais/skripti/e5_packs.py regen --iter 1` no `gen_index.csv` un iesaldētajiem ievaddatiem (uzdevumi, kanons, prompts `02b_v1.1-c.md`). Oriģinālās pakas netika arhivētas. Determinisms pārbaudīts kā iterācijai 0 (iter. 2: 30/30 baitu identiskas).",
}
LOST_PROSE = {0: "proza zaudēta 2026-10-16 konteksta zudumā (07:41–10:09); skaitļi saglabāti iesaldētajā momentuzņēmumā (rakstīts 07:12)"}


def it_name(it):
    return it if isinstance(it, str) else f"iter_{it}"


def copy_iteration(it, o):
    n = 0
    n += cp_glob(os.path.join(ROOT, "responses", f"iter_{it}", "*.md"), os.path.join(o, "responses"))
    n += cp_glob(os.path.join(ROOT, "bundles", f"responses_iter_{it}_*.md"), os.path.join(o, "responses"))
    n += cp_glob(os.path.join(ROOT, "judgments", f"iter_{it}", "*.md"), os.path.join(o, "judgments"))
    n += cp(os.path.join(ROOT, "bundles", f"judgments_iter_{it}.md"), os.path.join(o, "judgments"))
    n += cp_glob(os.path.join(ROOT, "judgments", f"iter_{it}_rejudge", "*.md"), os.path.join(o, "judgments_rejudge"))
    n += cp(os.path.join(ROOT, "bundles", f"judgments_iter_{it}_rejudge.md"), os.path.join(o, "judgments_rejudge"))
    n += cp_glob(os.path.join(ROOT, "index", f"rejudge_iter_{it}_*.csv"), os.path.join(o, "judgments_rejudge"))
    n += cp_glob(os.path.join(ROOT, "judgments", f"iter_{it}_J2_gemini", "*.md"), os.path.join(o, "judgments_J2_gemini"))
    n += cp_glob(os.path.join(ROOT, "packs", f"iter_{it}", "gen", "*.md"), os.path.join(o, "packs", "gen"))
    n += cp_glob(os.path.join(ROOT, "packs", f"iter_{it}", "judge", "*.md"), os.path.join(o, "packs", "judge"))
    n += cp(os.path.join(ROOT, "packs", f"iter_{it}", "gen_index.csv"), os.path.join(o, "packs"))
    n += cp(os.path.join(ROOT, "packs", f"iter_{it}", "judge_index.csv"), os.path.join(o, "packs"))
    n += cp(os.path.join(ROOT, "index", f"hardchecks_iter_{it}.csv"), os.path.join(o, "hardchecks"))
    for f in ["summary.md", "task_means.csv"]:
        n += cp(os.path.join(ROOT, "figures", f"iter_{it}", f), os.path.join(o, "analysis"))
    n += cp_glob(os.path.join(ROOT, "figures", f"iter_{it}", "fig*.png"), os.path.join(o, "analysis"))
    n += cp(os.path.join(ROOT, "figures", f"iter_{it}", f"panel_iter_{it}.png"), os.path.join(o, "analysis"))
    n += cp_glob(os.path.join(ROOT, "figures", f"iter_{it}", "figure_data", "*.csv"), os.path.join(o, "analysis", "figure_data"))
    n += cp(os.path.join(ROOT, "index", f"e5_results_iter_{it}_snapshot.csv"), os.path.join(o, "analysis"))
    n += cp(os.path.join(ROOT, "index", f"e5_pairwise_iter_{it}_snapshot.csv"), os.path.join(o, "analysis"))
    n += cp_glob(os.path.join(ROOT, "index", f"error_analysis_iter_{it}*.md"), os.path.join(o, "error_analysis"))
    for ext in ("md", "json", "diff"):
        n += cp(os.path.join(ROOT, "index", f"changes_v1.{it + 1}.{ext}"), os.path.join(o, "error_analysis"))
    # standard comparison document (iteration 0: baseline against the controls) and decisions
    comp = os.path.join(ROOT, "index", "comparison_iter_0_baseline.md" if it == 0 else f"comparison_iter_{it - 1}_to_{it}.md")
    n += cp(comp, o, "SALIDZINAJUMS.md")
    n += cp(os.path.join(ROOT, "index", f"decisions_iter_{it}.md"), o, "decisions.md")
    # prompt under test = the version(s) named in gen_index
    gi = os.path.join(ROOT, "packs", f"iter_{it}", "gen_index.csv")
    if os.path.exists(gi):
        for v in sorted({r["prompt_version"] for r in csv.DictReader(open(gi, encoding="utf-8")) if r["prompt_version"]}):
            n += cp(os.path.join(ROOT, "prompts", f"02b_{v}.md"), os.path.join(o, "prompt"))
            # a version not derived from the previous iteration's change pack (e.g. v1.3-pb, iter 4) carries its own change description
            n += cp_glob(os.path.join(ROOT, "index", f"changes_{v}.*"), os.path.join(o, "prompt"))
            n += cp_glob(os.path.join(ROOT, "index", f"changes_{v}*_draft.md"), os.path.join(o, "error_analysis"))
    n += cp_glob(os.path.join(ROOT, "figures", f"iter_{it}", f"iter{it}_*_check.txt"), os.path.join(o, "analysis"))
    return n


def n_files(n):
    return f"{n} fails" if n % 10 == 1 and n % 100 != 11 else f"{n} faili"


def data_files(d):
    return sorted(f for f in os.listdir(d) if os.path.isfile(os.path.join(d, f)) and f not in ("_STATUSS.md", "INDEX.csv")) if os.path.isdir(d) else []


def write_indexes(it, o):
    """responses/INDEX.csv and judgments/INDEX.csv: one row per planned item, present or not, with SHA-256."""
    gi = os.path.join(o, "packs", "gen_index.csv")
    if os.path.exists(gi):
        rows = []
        for r in csv.DictReader(open(gi, encoding="utf-8")):
            p = os.path.join(o, "responses", r["response"])
            rows.append({"response_file": r["response"], "condition": r["condkey"], "task_id": r["task_id"], "run": r["run"],
                         "gen_pack": "packs/gen/" + r["pack"], "present": "jā" if os.path.exists(p) else "nē",
                         "sha256": sha(p) if os.path.exists(p) else "", "words": len(open(p, encoding="utf-8").read().split()) if os.path.exists(p) else ""})
        with open(os.path.join(o, "responses", "INDEX.csv"), "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    ji = os.path.join(o, "packs", "judge_index.csv")
    if os.path.exists(ji):
        snap = os.path.join(o, "analysis", f"e5_results_iter_{it}_snapshot.csv")
        frozen = {(r["pairid"], r["order"]) for r in csv.DictReader(open(snap, encoding="utf-8"))} if os.path.exists(snap) else set()
        rows = []
        for r in csv.DictReader(open(ji, encoding="utf-8")):
            p = os.path.join(o, "judgments", r["judgment"]); have = os.path.exists(p)
            rj = os.path.join(o, "judgments_rejudge", r["judgment"]); j2 = os.path.join(o, "judgments_J2_gemini", r["judgment"])
            note = "" if have else LOST_PROSE.get(it, "trūkst")
            rows.append({"judgment_file": r["judgment"], "pairid": r["pairid"], "order": r["order"], "judge_pack": "packs/judge/" + r["pack"],
                         "present": "jā" if have else "nē", "sha256": sha(p) if have else "",
                         "in_frozen_snapshot": "jā" if (r["pairid"], r["order"]) in frozen else "nē",
                         "rejudge": "judgments_rejudge/" + r["judgment"] if os.path.exists(rj) else "",
                         "J2_gemini": "judgments_J2_gemini/" + r["judgment"] if os.path.exists(j2) else "", "note": note})
        with open(os.path.join(o, "judgments", "INDEX.csv"), "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)


def folder_status(it, o, rel, started):
    d = os.path.join(o, rel); files = data_files(d)
    if not started:
        return f"Iterācija `{it_name(it)}` vēl nav sākta; šī mape tiks aizpildīta tajā."
    if rel == "packs/gen/" and it in GEN_PROVENANCE:
        return f"{len(files)} pakas. " + GEN_PROVENANCE[it]
    if rel == "judgments/":
        ji = os.path.join(o, "packs", "judge_index.csv")
        planned = len(list(csv.DictReader(open(ji, encoding="utf-8")))) if os.path.exists(ji) else 0
        have = len([f for f in files if not f.startswith("judgments_")])
        s = f"{have} no {planned} plānotajiem vērtējumiem kā atsevišķi faili (+ sainis). Katrs plānotais vērtējums ar SHA-256: `INDEX.csv`."
        if have < planned and it in LOST_PROSE:
            idx = list(csv.DictReader(open(os.path.join(d, "INDEX.csv"), encoding="utf-8")))
            miss = [r for r in idx if r["present"] == "nē"]; rj = sum(1 for r in miss if r["rejudge"])
            s += (f" Trūkstošie {len(miss)}: {LOST_PROSE[it]}. {rj} no {len(miss)} ir atkārtoti novērtēti — teksts `judgments_rejudge/`"
                  " (sk. INDEX.csv kolonnas `note`, `rejudge`).")
        return s
    if rel == "judgments_J2_gemini/" and files:
        return (f"{n_files(len(files))}: Gemini (J2) vērtējumi, ko Martins veica manuāli ar to pašu tiesneša promptu un pakām; "
                "pārējās izlases pakas vēl gaida (izlase un procedūra: `00_kopejais/kalibracija/j2_gemini/`).")
    if not files and not (rel.endswith("/") and any(os.path.isdir(os.path.join(d, x)) for x in os.listdir(d))):
        if rel == "judgments_rejudge/":
            return "Šajā iterācijā atkārtotā vērtēšana (test–retest) netika veikta. Tiesneša atkārtojamība mērīta iterācijā 0 (`iter_0/judgments_rejudge/`) un, salīdzinot tās pašas atbildes pārvērtētas nākamajā iterācijā (sk. `SALIDZINAJUMS.md`)."
        if rel == "judgments_J2_gemini/":
            return "Gemini (J2) vērtējumi šai iterācijai vēl nav saņemti. Martins tos veic manuāli ar to pašu tiesneša promptu un pakām (procedūra: `00_kopejais/kalibracija/j2_gemini/README_J2_GEMINI.md`)."
        return "Mape vēl tukša."
    return n_files(len(files)) + "."


def write_standard_layout(it, o, started):
    for rel, desc in STANDARD:
        if rel.endswith("/"):
            d = os.path.join(o, rel); os.makedirs(d, exist_ok=True)
            if started and rel in ("responses/", "judgments/"):
                write_indexes(it, o)
            body = [f"# `{it_name(it)}/{rel}`", "", f"**Kas šeit ir (standarta struktūra, vienāda visām iterācijām):** {desc}.", "",
                    f"**Statuss:** {folder_status(it, o, rel, started)}", ""]
            open(os.path.join(d, "_STATUSS.md"), "w", encoding="utf-8").write("\n".join(body))


def iteration_card(it, o, started):
    """README for one iteration: the standard layout with the status of each part, derived from what is on disk."""
    rows = []
    for rel, desc in STANDARD:
        p = os.path.join(o, rel)
        if rel.endswith("/"):
            cnt = len(data_files(p)); st = n_files(cnt) if cnt else "tukša (sk. `_STATUSS.md`)"
        else:
            st = "ir" if os.path.exists(p) else ("šis fails" if rel == "README.md" else "vēl nav")
        rows.append(f"| `{rel}` | {desc} | {st} |")
    jidx = os.path.join(o, "packs", "judge_index.csv")
    n_planned = len(list(csv.DictReader(open(jidx, encoding="utf-8")))) if os.path.exists(jidx) else 0
    n_judg = len([f for f in data_files(os.path.join(o, "judgments")) if not f.startswith("judgments_")])
    n_resp = len([f for f in data_files(os.path.join(o, "responses")) if not f.startswith("responses_")])
    conds = sorted({f.rsplit("_", 2)[0] for f in data_files(os.path.join(o, "responses")) if not f.startswith("responses_")})
    status = ("vēl nav sākta" if not started else
              "pabeigta" if n_planned and os.path.exists(os.path.join(o, "analysis", "summary.md")) else "procesā")
    lines = [f"# {it_name(it)} — iterācijas karte", "",
             f"- Stāvoklis: **{status}**",
             f"- Ģenerētās atbildes šajā iterācijā: {n_resp} ({', '.join(conds) if conds else '—'})",
             f"- Tiesneša J1 vērtējumi: {n_judg} / {n_planned} plānoti (kurš pāris, kurā kārtībā: `packs/judge_index.csv`; katrs ar SHA-256: `judgments/INDEX.csv`)",
             "- Tiesnesis J1: Claude Opus 5.5; ģenerators: Claude Sonnet 5.5 (sk. `00_kopejais/registrs/e5_run_config.json`)", "",
             "## Standarta struktūra (vienāda iter_0 … iter_4 un final)", "",
             "| Daļa | Kas tā ir | Šajā iterācijā |", "|---|---|---|", *rows, "",
             "Katrā mapē `_STATUSS.md` pasaka, kas tur ir un kāpēc tā var būt tukša. Izpildes žurnāls ar laika zīmogiem: `00_kopejais/registrs/e5_run_log.md`.",
             "Ceļš no skaitļa līdz avotam: `analysis/e5_results_iter_N_snapshot.csv` (pairid, order) → `judgments/{pairid}_{order}.md` → `packs/judge/…` → `responses/…` → `packs/gen/…`.", ""]
    open(os.path.join(o, "README.md"), "w", encoding="utf-8").write("\n".join(lines))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True); ap.add_argument("--iters", default="0,1")
    a = ap.parse_args()
    out = a.out; os.makedirs(out, exist_ok=True)
    n = 0
    # 00_kopejais
    k = os.path.join(out, "00_kopejais")
    n += cp_glob(os.path.join(ROOT, "29*.md"), os.path.join(k, "protokols"))
    n += cp_glob(os.path.join(ROOT, "30_*.md"), os.path.join(k, "protokols"))
    n += cp_glob(os.path.join(ROOT, "prompts", "*.md"), os.path.join(k, "prompti"))
    n += cp(os.path.join(ROOT, "tasks", "tasks.json"), os.path.join(k, "uzdevumi"))
    n += cp_glob(os.path.join(ROOT, "scripts", "e5_*.py"), os.path.join(k, "skripti"))
    n += cp_glob(os.path.join(ROOT, "registry", "e5_run_log.md"), os.path.join(k, "registrs"))
    n += cp_glob(os.path.join(ROOT, "registry", "e5_run_config.json"), os.path.join(k, "registrs"))
    n += cp_glob(os.path.join(ROOT, "registry", "e5_STATUS_*.md"), os.path.join(k, "registrs"))
    n += cp_glob(os.path.join(ROOT, "registry", "decisions_*.md"), os.path.join(k, "registrs"))
    n += cp(os.path.join(ROOT, "E5_RESTORE.md"), os.path.join(k, "registrs"))
    n += cp_glob(os.path.join(ROOT, "packs", "calib", "*.md"), os.path.join(k, "kalibracija", "packs"))
    n += cp_glob(os.path.join(ROOT, "judgments", "calib", "*.md"), os.path.join(k, "kalibracija", "judgments"))
    n += cp_glob(os.path.join(ROOT, "bundles", "*calib*.md"), os.path.join(k, "kalibracija"))
    # J2 (Gemini) pack sets, selections and instructions
    for dp, _, fns in os.walk(os.path.join(ROOT, "j2_gemini")):
        rel = os.path.relpath(dp, os.path.join(ROOT, "j2_gemini"))
        for fn in fns:
            n += cp(os.path.join(dp, fn), os.path.join(k, "kalibracija", "j2_gemini", "" if rel == "." else rel))
    # current collected tables (derived, regenerable with e5_collect.py; kept for convenience)
    n += cp(os.path.join(ROOT, "registry", "e5_results.csv"), os.path.join(k, "registrs"))
    n += cp(os.path.join(ROOT, "registry", "e5_pairwise.csv"), os.path.join(k, "registrs"))
    # iterations — every iteration folder (iter_0 … iter_4, final) gets the SAME standard layout (STANDARD below);
    # folders are created even when empty and each carries a _STATUSS.md that says what is there and why (overwritten on every run,
    # so it never goes stale). Iterations named in --iters get their data copied; the rest get the skeleton only.
    data_iters = [int(x) for x in a.iters.split(",") if x.strip() != ""]
    for it in ALL_ITERS:
        o = os.path.join(out, it if isinstance(it, str) else f"iter_{it}")
        if it in data_iters:
            n += copy_iteration(it, o)
        write_standard_layout(it, o, it in data_iters)
        iteration_card(it, o, it in data_iters)
    # process trace: working batch bundles from the project buffer (redundant with judgments/, kept as evidence of the save rhythm)
    n += cp_glob(os.path.join(ROOT, "buffer", "*"), os.path.join(k, "registrs", "buferis"))

    # manifest with hashes for everything in the archive.
    # NOTE: the export mount (/mnt/user-data/outputs) appends a C2PA content-credentials chunk ("caBX") to PNG files a
    # moment after they are written (pixel data unchanged, +5 770 bytes). Wait, then hash the files as they really are.
    import time; time.sleep(3)
    rows = []
    for dp, _, fns in os.walk(out):
        for fn in sorted(fns):
            if fn == "MANIFEST_sha256.csv":
                continue
            p = os.path.join(dp, fn)
            rows.append((os.path.relpath(p, out).replace("\\", "/"), sha(p), os.path.getsize(p), png_pixel_sha(p) if fn.lower().endswith(".png") else ""))
    with open(os.path.join(out, "MANIFEST_sha256.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(["path", "sha256", "bytes", "pixel_sha256"]); w.writerows(sorted(rows))
    print(f"{n} files copied; manifest {len(rows)} entries -> {out}")


if __name__ == "__main__":
    main()
