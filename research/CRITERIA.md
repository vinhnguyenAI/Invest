# Screening criteria (applied to every KOSPI / KOSDAQ company)

Price/market-cap snapshot: **2026-10-14** (FinanceData/marcap, KRX daily data).
Long-term Korean government bond yield (KTB 10Y): **~4.25%** (Trading Economics, 13 Oct 2026; OECD Sep-2026 monthly 4.45%).
Hurdle: **normalised earnings yield ≥ 8.5%** (2 × 4.25%), i.e. normalised P/E ≤ ~11.8x.

| # | Criterion | Pass rule | Hard fail examples |
|---|-----------|-----------|--------------------|
| 1 | **Auditor is not PwC** | Latest FY (FY2025) external auditor is not **Samil PwC (삼일회계법인)**. Korean Big-4 aliases: Samil = PwC, Samjong (삼정) = KPMG, Anjin (안진) = Deloitte, Hanyoung (한영) = EY. | Samil PwC audit opinion on FY2025 accounts. |
| 2 | **Easy-to-understand business model** | A sensible person can explain in two sentences what is sold, to whom and why the customer pays. Revenue mostly from one or two understandable segments. | Pre-revenue / clinical-stage biotech, banks/insurers/brokers, opaque holding companies, shells that keep pivoting (e.g. "secondary battery + entertainment + bio"), crypto/NFT. |
| 3 | **Normalised earnings yield ≥ 2 × KTB 10Y** | `Normalised net income = current (TTM or FY2025) revenue × normalised NET margin`. `Normalised EY = normalised net income / market cap ≥ 8.5%`. | Even at a generous but defensible margin the yield is < 8.5%. |
| 3b | **Reason for the normalised margin** | Must be written out: what margin, why it's achievable under *normal* external conditions (cycle, input costs, FX, demand) and internal conditions (utilisation, scale, mix, one-offs, start-up losses). Anchor on history (5–10y average / prior peak), peers and identifiable drivers. | "Management says so" with no history or mechanism. |
| 4 | **Run by the owner** | Founder or controlling-family member is CEO / chairman / executive director **actively running this company**, and the owner group holds a meaningful stake (≈≥20% incl. related parties, or the single largest block). | Chaebol affiliate run by a hired CEO where the family only sits at group level; PE-owned; no controlling shareholder; state-owned. |
| 5 | **Healthy balance sheet** | Net cash, or net debt/EBITDA < 1.5x; liabilities/equity (부채비율) < ~100%; no going-concern doubt; no habit of convertible-bond (CB/BW) or rights-issue dilution. | Heavy debt, repeated CBs/rights issues, auditor qualification. |
| 6 | **In a revenue growth phase** | Revenue growing: ≈≥10% CAGR over the last 3 years **and** latest year/TTM still growing, with a credible runway (not a one-off spike). | Flat/declining revenue, a single boom year now reversing. |

## Notes for researchers
- PwC check: search e.g. `"<company name> 감사인"`, `"<company> 삼일회계법인"`, or the audit report in the FY2025 사업보고서. Record the auditor name explicitly. Unknown = flag, never assume.
- Use KRW. Market cap is given in the universe file (`marcap_krw_bn`, KRW bn).
- Use NET margin (after tax) so the yield is comparable to a bond yield. If a company has large net cash, note it; you may additionally show an ex-cash yield, but the pass/fail test uses market cap.
- Be honest about uncertainty. Mark facts as *verified (source)* vs *estimate (memory)*.
