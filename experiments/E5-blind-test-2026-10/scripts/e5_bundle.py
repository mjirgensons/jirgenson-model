#!/usr/bin/env python3
"""
E5 — bundle / unbundle working files so every stage can be stored in the project and reconstructed exactly.

bundle:   python3 e5_bundle.py bundle --dir responses/iter_0 --out bundles/responses_iter_0_A.md --prefix A_
          Packs every file in --dir whose name starts with --prefix (all files if omitted) into one markdown bundle.
          Each file is framed as:   ===== FILE: <name> =====   ...content...   ===== END FILE =====
          A content line that itself starts with "===== " is escaped with a leading backslash.
unbundle: python3 e5_bundle.py unbundle --bundle bundles/responses_iter_0_A.md --dir restored/responses/iter_0
          Recreates the files byte-for-byte (after unescaping). Verified by sha256 per file written into the bundle header.
"""
import argparse, hashlib, os, re, sys


def sha(b):
    return hashlib.sha256(b).hexdigest()


def bundle(d, out, prefix):
    names = sorted(f for f in os.listdir(d) if os.path.isfile(os.path.join(d, f)) and (not prefix or f.startswith(prefix)))
    lines = [f"# E5 bundle of {d} (prefix: {prefix or '*'}) — {len(names)} files", "", "| file | sha256 | bytes |", "|---|---|---|"]
    bodies = []
    for n in names:
        raw = open(os.path.join(d, n), "rb").read()
        lines.append(f"| {n} | {sha(raw)} | {len(raw)} |")
        text = raw.decode("utf-8")
        esc = "\n".join(("\\" + l if l.startswith("===== ") else l) for l in text.split("\n"))
        bodies.append(f"===== FILE: {n} =====\n{esc}\n===== END FILE =====")
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    open(out, "w", encoding="utf-8").write("\n".join(lines) + "\n\n" + "\n\n".join(bodies) + "\n")
    print(f"bundled {len(names)} files -> {out}")


def unbundle(bpath, d):
    text = open(bpath, encoding="utf-8").read()
    expected = dict(re.findall(r"^\| (\S+) \| ([0-9a-f]{64}) \| \d+ \|$", text, flags=re.MULTILINE))
    os.makedirs(d, exist_ok=True)
    n_ok, n_bad = 0, 0
    for m in re.finditer(r"===== FILE: (.+?) =====\n(.*?)\n===== END FILE =====", text, flags=re.DOTALL):
        name, body = m.group(1), m.group(2)
        unesc = "\n".join((l[1:] if l.startswith("\\===== ") else l) for l in body.split("\n"))
        raw = unesc.encode("utf-8")
        open(os.path.join(d, name), "wb").write(raw)
        if expected.get(name) == sha(raw):
            n_ok += 1
        else:
            n_bad += 1; print("HASH MISMATCH:", name, file=sys.stderr)
    print(f"restored {n_ok} files to {d}; mismatches: {n_bad}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("bundle"); b.add_argument("--dir", required=True); b.add_argument("--out", required=True); b.add_argument("--prefix", default="")
    u = sub.add_parser("unbundle"); u.add_argument("--bundle", required=True); u.add_argument("--dir", required=True)
    a = ap.parse_args()
    bundle(a.dir, a.out, a.prefix) if a.cmd == "bundle" else unbundle(a.bundle, a.dir)


if __name__ == "__main__":
    main()
