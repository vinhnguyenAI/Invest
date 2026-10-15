"""Build the KRX screening universe from the FinanceData/marcap daily snapshot.

Usage: python scripts/build_universe.py /path/to/marcap-2026.parquet
Writes data/universe_all.csv, data/universe.csv (investable) and triage batch inputs.
"""
import sys
from pathlib import Path

import pandas as pd

MIN_MARCAP = 50e9      # KRW 50bn
MIN_ADV = 100e6        # KRW 100m median daily traded value (last ~45 days)
BATCH_SIZE = 100
EXCLUDE_NAME = r"스팩|리츠|인프라|선박투자|맥쿼리|우$|우B$|우C$"

root = Path(__file__).resolve().parents[1]
df = pd.read_parquet(sys.argv[1])
last = df.Date.max()
adv = df[df.Date > last - pd.Timedelta(days=45)].groupby("Code").Amount.median()

d = df[df.Date == last].copy()
d["adv_krw_m"] = (d.Code.map(adv) / 1e6).round(0)
d["marcap_krw_bn"] = (d.Marcap / 1e9).round(1)
d = d[d.Market.isin(["KOSPI", "KOSDAQ", "KOSDAQ GLOBAL"])]
d = d[d.Code.str.endswith("0") & ~d.Name.str.contains(EXCLUDE_NAME)]
cols = ["Code", "Name", "Market", "Close", "Stocks", "marcap_krw_bn", "adv_krw_m"]
d = d.sort_values("Marcap", ascending=False)[cols]
d.insert(0, "asof", last.date().isoformat())
d.to_csv(root / "data/universe_all.csv", index=False)

inv = d[(d.marcap_krw_bn * 1e9 >= MIN_MARCAP) & (d.adv_krw_m * 1e6 >= MIN_ADV)]
inv.to_csv(root / "data/universe.csv", index=False)
d[~d.Code.isin(inv.Code)].to_csv(root / "data/excluded_size_liquidity.csv", index=False)

out = root / "research/triage/input"
out.mkdir(parents=True, exist_ok=True)
for i in range(0, len(inv), BATCH_SIZE):
    inv.iloc[i:i + BATCH_SIZE].to_csv(out / f"batch_{i // BATCH_SIZE + 1:02d}.csv", index=False)
print(f"asof {last.date()}: all={len(d)} investable={len(inv)} batches={-(-len(inv) // BATCH_SIZE)}")
