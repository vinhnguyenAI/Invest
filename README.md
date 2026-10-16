# Invest: Korea (KRX) owner-operator value screen

Screens every KOSPI/KOSDAQ company against six criteria. The investor buys Korean shares directly via IBKR.

1. Auditor is not PwC (Samil 삼일회계법인)
2. Easy-to-understand business model
3. Normalised earnings yield ≥ 2 × KTB 10Y yield (≈ 8.5%), where normalised earnings = revenue × normalised net margin, with the **reason** for that margin written out
4. Run by the owner
5. Healthy balance sheet
6. In a revenue growth phase

**Start here → [`results/SUMMARY.md`](results/SUMMARY.md)**

## Layout
| Path | What |
|---|---|
| `research/CRITERIA.md` | Exact pass/fail rules |
| `data/universe_all.csv` | All 2,547 KOSPI/KOSDAQ common stocks (2026-10-14 snapshot) |
| `data/universe.csv` | 1,478 investable names (≥ ₩50bn cap, ≥ ₩100m daily traded value) |
| `data/excluded_size_liquidity.csv` | Names dropped for size/liquidity |
| `research/triage/output/` | Stage 1: verdict + reason for every investable company |
| `results/triage_all.csv` | Stage 1 merged with the universe |
| `research/deep/<code>_<name>.md` | Stage 2: deep-dive report per candidate (scorecard, financials, normalised-margin reasoning, sources) |
| `results/final_scorecard.csv` | Stage 2 merged scorecard |
| `results/SUMMARY.md` | Shortlist, near-misses, DART checklist |

## Re-running
```bash
# price/market-cap data: https://github.com/FinanceData/marcap (data/marcap-2026.parquet)
python scripts/build_universe.py /path/to/marcap-2026.parquet
python scripts/merge_triage.py
python scripts/merge_deep.py
```
Research was done by parallel AI sub-agents using web search; see the caveats in `results/SUMMARY.md`.
