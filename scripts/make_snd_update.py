"""Build the one-page S&D (260970) stock update PDF.

Usage: python scripts/make_snd_update.py
Writes results/SnD_260970_stock_update_2026-10-17.pdf
"""
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (KeepInFrame, Paragraph, SimpleDocTemplate,
                                Spacer, Table, TableStyle)

root = Path(__file__).resolve().parents[1]
out = root / "results/SnD_260970_stock_update_2026-10-17.pdf"

INK = colors.HexColor("#1f2430")
RED = colors.HexColor("#c8102e")
MUTED = colors.HexColor("#5b6270")
TINT = colors.HexColor("#fff3f0")
LINE = colors.HexColor("#d9dce1")

base = ParagraphStyle("b", fontName="Helvetica", fontSize=8.3, leading=10.6, textColor=INK, alignment=TA_LEFT)
small = ParagraphStyle("s", parent=base, fontSize=7, leading=8.6, textColor=MUTED)
h1 = ParagraphStyle("h1", parent=base, fontName="Helvetica-Bold", fontSize=16.5, leading=19.5, textColor=INK)
sub = ParagraphStyle("sub", parent=base, fontSize=9, leading=11.5, textColor=MUTED)
h2 = ParagraphStyle("h2", parent=base, fontName="Helvetica-Bold", fontSize=9.6, leading=12, textColor=RED, spaceBefore=5, spaceAfter=2)
cell = ParagraphStyle("c", parent=base, fontSize=7.8, leading=9.6)
cellb = ParagraphStyle("cb", parent=cell, fontName="Helvetica-Bold")


def P(t, s=base):
    return Paragraph(t, s)


def bullets(items, s=base):
    return [P(f"&bull;&nbsp;{i}", s) for i in items]


story = [
    P("S&amp;D Co. (260970 KQ) &middot; Stock update &middot; 17 Oct 2026", sub),
    P("Will Buldak break up with its sauce guy?", h1),
    P("Price KRW 58,200 &middot; Mkt cap KRW 168bn &middot; TTM P/E 7.0x (about 4.5x net of ~KRW 59bn cash and "
      "short-term investments) &middot; Screen verdict: PASS (provisional)", sub),
    Spacer(1, 5),
]

verdict = Table([[P(
    "<b>Bottom line.</b> Our odds that Samyang Foods (Buldak) <b>fully drops</b> S&amp;D within 3 years: <b>~10%</b>. "
    "Odds it moves a <b>meaningful slice</b> (25%+ of S&amp;D's Samyang volume) in-house or to its new subsidiary G&amp;F: "
    "<b>~35%</b>. The share price, down 60% from its June-2025 peak while profits grew ~30%, already behaves as if "
    "the partial breakup is <i>certain</i>. Scenario-weighted value is roughly <b>KRW 85k/share (+45%)</b>. "
    "It is not dating advice, but the relationship looks like it's in 'it's complicated', not 'it's over'.", base)]],
    colWidths=[180 * mm])
verdict.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), TINT), ("BOX", (0, 0), (-1, -1), 0.8, RED),
                             ("LEFTPADDING", (0, 0), (-1, -1), 7), ("RIGHTPADDING", (0, 0), (-1, -1), 7),
                             ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 6)]))
story += [verdict]

story += [P("Relationship status", h2), P(
    "S&amp;D makes the flavour bases (liquid and powder) that go into Buldak sauce; industry sources say it supplies "
    "<i>all</i> of the core sauce ingredient. Samyang is an estimated <b>70-90% of S&amp;D's revenue</b>. "
    "In July 2025 Samyang agreed to buy sauce maker <b>G&amp;F</b> (~KRW 60bn) to bring outsourced soup production "
    "in-house. S&amp;D fell ~20% that day and kept falling. Samyang is also building a KRW 78bn liquid-soup plant "
    "in Wonju (Feb 2027) to feed its new China factory (Jan 2027).")]

red = bullets([
    "<b>It bought a new partner.</b> G&amp;F already supplies Nongshim and Ottogi, and reportedly some Buldak sauce ingredients too.",
    "<b>Industry playbook:</b> Nongshim bought its own Shin Ramyun soup supplier (Sewoo, ~KRW 100bn). Insourcing the "
    "'secret sauce' is in fashion; one insider says recipe security makes in-house production 'the norm'.",
    "<b>New capacity, new rules:</b> China volumes (1.1bn packs/yr planned) could be supplied by Samyang-owned "
    "plants rather than S&amp;D.",
    "<b>Concentration:</b> one customer, one product family. A fad cooling would hurt even if the contract stays.",
], cell)
green = bullets([
    "<b>Fifteen months after the G&amp;F deal, S&amp;D is still growing fast:</b> 2Q26 revenue +31%, operating profit "
    "+39%. There is no sign of lost volume yet.",
    "<b>Changing the taste is scary:</b> analysts note the cost saving is not worth the risk of fans noticing a "
    "different Buldak. You don't swap the spice in a global hit casually.",
    "<b>The Wonju plant makes soup, not the base</b> (on our reading). More Samyang soup lines may mean "
    "<i>more</i> S&amp;D base, not less.",
    "<b>S&amp;D doubled capacity</b> (22k to 43.5k t, Oct 2025). It would be brave to do that without a heads-up from its main customer.",
    "<b>Cheap to acquire:</b> S&amp;D's whole market cap is about 2% of Samyang's. Buying S&amp;D is easier than replacing it.",
], cell)
flags = Table([[P("Red flags (breakup risk)", cellb), P("Green flags (still in love)", cellb)], [red, green]],
              colWidths=[90 * mm, 90 * mm])
flags.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LINEBELOW", (0, 0), (-1, 0), 0.6, LINE),
                           ("LEFTPADDING", (0, 0), (-1, -1), 3), ("RIGHTPADDING", (0, 0), (-1, -1), 6)]))
story += [P("Evidence, both sides", h2), flags]

rows = [["Scenario (3 yrs)", "Odds", "What happens", "Value/share*"],
        ["Status quo: 'we're good'", "45%", "Buldak growth keeps flowing; NI ~KRW 24bn at 11x plus cash", "~112k"],
        ["Partial breakup: 'let's see other suppliers'", "35%", "S&amp;D's Samyang volume -30%, revenue -24%, net margin 10%", "~61k"],
        ["Full breakup: 'it's not you, it's my factory'", "10%", "Revenue falls to ~KRW 45bn, profit near zero, worth roughly book value", "~31k"],
        ["Samyang buys S&amp;D: 'put a ring on it'", "10%", "Nongshim-Sewoo-style vertical deal at a premium", "~100k"],
        ["Probability-weighted", "", "vs. today's KRW 58,200 (market is pricing about the partial-breakup case)", "<b>~85k</b>"]]
tbl = Table([[P(c, cellb if i == 0 else cell) for c in r] for i, r in enumerate(rows)],
            colWidths=[52 * mm, 12 * mm, 92 * mm, 24 * mm])
tbl.setStyle(TableStyle([("LINEBELOW", (0, 0), (-1, 0), 0.6, INK), ("LINEBELOW", (0, 1), (-1, -2), 0.3, LINE),
                         ("LINEABOVE", (0, -1), (-1, -1), 0.6, INK), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                         ("TOPPADDING", (0, 0), (-1, -1), 2), ("BOTTOMPADDING", (0, 0), (-1, -1), 2)]))
story += [P("Scenarios", h2), tbl,
          P("*Our rough estimates: earnings multiple on normalised net income plus ~KRW 59bn liquid assets, 2.89m shares. "
            "Odds are analyst judgement, not a model output.", small)]

story += [P("What would change our mind (the texts to watch for)", h2)] + bullets([
    "<b>Breakup signals:</b> S&amp;D quarterly revenue growth below Samyang's overseas growth for two quarters running; "
    "G&amp;F capex on liquid bases; Samyang job ads for 'sauce base' R&amp;D; the China plant's ingredient sourcing.",
    "<b>Reassurance signals:</b> a multi-year supply agreement disclosed on DART; S&amp;D winning non-Samyang K-sauce "
    "customers (management is talking up diversification); continued buybacks.",
    "<b>Housekeeping:</b> confirm the FY2025 auditor is not Samil PwC, and the debt ratio in the 1H26 report on DART.",
], base)

story += [Spacer(1, 4), P(
    "<b>Verdict:</b> keep it on the shortlist. The market has priced in a messy separation, but the evidence so far is "
    "a couple that redecorated the house, not one dividing the furniture. Position size should respect the "
    "one-customer risk. If you'd lose sleep over a Samyang press release, own it small or not at all.", base),
    Spacer(1, 4),
    P("Sources (Korean press via web search; DART not accessed): hankyung.com/article/202502273613L; dt.co.kr/article/12004849; "
      "smarttoday.co.kr/ko-kr/articles/85565 and /86937; ajunews.com/view/20250714095618167; sidae.com/article/2026012715542743518; "
      "metroseoul.co.kr/article/20250729500181; quartr.com (S&amp;D 2Q26). Prices: FinanceData/marcap (KRX). "
      "Not investment advice.", small)]

doc = SimpleDocTemplate(str(out), pagesize=A4, leftMargin=15 * mm, rightMargin=15 * mm,
                        topMargin=12 * mm, bottomMargin=10 * mm,
                        title="S&D (260970) stock update", author="Invest research")
frame_h = A4[1] - 22 * mm
doc.build([KeepInFrame(180 * mm, frame_h, story, mode="shrink")])
print(out)
