#!/usr/bin/env python3
"""E5 — after a judge/gen batch: copy given files into the archive staging, write a delta bundle, print device commit JSON.
Usage: python3 e5_save_batch.py --iter 2 --kind judgments --tag b02 FILE [FILE ...]"""
import argparse, json, os, shutil, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = "/mnt/user-data/outputs/E5_eksperiments"
ap = argparse.ArgumentParser(); ap.add_argument("--iter", type=int, required=True); ap.add_argument("--kind", required=True)
ap.add_argument("--tag", required=True); ap.add_argument("files", nargs="+"); a = ap.parse_args()
dst = os.path.join(OUT, f"iter_{a.iter}", a.kind); os.makedirs(dst, exist_ok=True)
tmp = os.path.join(ROOT, "buffer", f"_tmp_{a.tag}"); shutil.rmtree(tmp, ignore_errors=True); os.makedirs(tmp)
files = []
for f in a.files:
    shutil.copy(f, dst); shutil.copy(f, tmp)
    files.append({"stagedPath": f"{dst}/{os.path.basename(f)}", "devicePath": "E:\\GitHub\\E5_eksperiments\\" + f"iter_{a.iter}\\{a.kind}\\" + os.path.basename(f)})
out = os.path.join(ROOT, "buffer", f"iter_{a.iter}_{a.kind}_delta_{a.tag}.md")
subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "e5_bundle.py"), "bundle", "--dir", tmp, "--out", out], check=True, stdout=subprocess.DEVNULL)
shutil.rmtree(tmp)
# always ship the current run log with every batch
log_dst = os.path.join(OUT, "00_kopejais", "registrs"); os.makedirs(log_dst, exist_ok=True)
shutil.copy(os.path.join(ROOT, "registry", "e5_run_log.md"), log_dst)
files.append({"stagedPath": f"{log_dst}/e5_run_log.md", "devicePath": "E:\\GitHub\\E5_eksperiments\\00_kopejais\\registrs\\e5_run_log.md"})
print(out); print(json.dumps(files))
