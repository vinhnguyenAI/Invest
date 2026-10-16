"""Merge Stage-2 deep-dive CSVs into results/final_scorecard.csv.

Later groups override earlier ones for the same Code (group_13 holds re-runs).
Usage: python scripts/merge_deep.py
"""
from pathlib import Path

import pandas as pd

root = Path(__file__).resolve().parents[1]
parts = []
for f in sorted((root / "research/deep/output").glob("group_*.csv")):
    d = pd.read_csv(f, dtype={"Code": str})
    d["Code"] = d.Code.str.zfill(6)
    d["group"] = f.stem
    parts.append(d)
df = pd.concat(parts, ignore_index=True).drop_duplicates("Code", keep="last")
df["verdict"] = df.verdict.str.strip().str.upper().str.extract(r"(PASS|WATCH|FAIL)")[0]
order = {"PASS": 0, "WATCH": 1, "FAIL": 2}
for c in ["norm_ey_pct", "bear_ey_pct"]:
    df[c] = pd.to_numeric(df[c], errors="coerce")
df = df.sort_values(["verdict", "norm_ey_pct"], key=lambda s: s.map(order) if s.name == "verdict" else -s)
df.to_csv(root / "results/final_scorecard.csv", index=False)
print(df.verdict.value_counts().to_string())
print(df[["Code", "Name", "English_name", "verdict", "norm_ey_pct", "bear_ey_pct", "failed_or_open"]].to_string(index=False))
