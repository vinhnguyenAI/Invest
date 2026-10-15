"""Merge Stage-1 triage outputs with the universe and list Stage-2 candidates.

Usage: python scripts/merge_triage.py
Writes results/triage_all.csv and results/stage2_candidates.csv.
"""
from pathlib import Path

import pandas as pd

root = Path(__file__).resolve().parents[1]
uni = pd.read_csv(root / "data/universe.csv", dtype={"Code": str})
parts = []
for f in sorted((root / "research/triage/output").glob("batch_*.csv")):
    t = pd.read_csv(f, dtype={"Code": str})
    t["Code"] = t.Code.str.zfill(6)
    t["batch"] = f.stem
    parts.append(t)
tri = pd.concat(parts, ignore_index=True).drop_duplicates("Code")
tri["verdict"] = tri.verdict.str.strip().str.upper()

m = uni.merge(tri.drop(columns=["Name"]), on="Code", how="left")
missing = m[m.verdict.isna()]
if len(missing):
    print(f"WARNING: {len(missing)} universe names without a triage verdict:")
    print(missing[["Code", "Name"]].to_string(index=False))
m.to_csv(root / "results/triage_all.csv", index=False)

cand = m[m.verdict == "PASS"].sort_values("est_norm_ey_pct", ascending=False)
cand.to_csv(root / "results/stage2_candidates.csv", index=False)
print(m.verdict.value_counts(dropna=False).to_string())
print(f"Stage-2 candidates: {len(cand)}")
