#!/usr/bin/env python3
"""Build a VALOR data request workbook (Read me, Status, Baselines, Monthly, Value inputs, Costs) from a value record.

Usage:  python3 make_data_request.py RECORD.yaml [--out FILE.xlsx] [--contact "name, email"]
The owner of each KPI, input and question comes from the record. Recalculate formulas afterwards
(e.g. LibreOffice) if the file must show values before Excel opens it.
"""
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.comments import Comment
from openpyxl.worksheet.datavalidation import DataValidation
import sys, csv, re, argparse, json
from pathlib import Path
import yaml

ap = argparse.ArgumentParser(description="Build a VALOR data request workbook from a value record.")
ap.add_argument("record"); ap.add_argument("--out"); ap.add_argument("--contact", default="the Value Orchestration Lead")
ap.add_argument("--refs", default=str(Path(__file__).resolve().parent.parent / "references"))
A = ap.parse_args()
REC = yaml.safe_load(Path(A.record).read_text(encoding="utf-8"))
KREG = {k["kpi_id"]: k for k in csv.DictReader(open(Path(A.refs) / "kpi-register.csv", encoding="utf-8"))}
R = REC.get("record", {}) or {}
NAME = R.get("epic_name") or R.get("feature_name") or "Value record"
CUR = R.get("currency") or (REC.get("economics") or {}).get("currency") or "AED"
out = A.out or str(Path(A.record).with_name(re.sub(r"[^A-Za-z0-9]+", "-", NAME).strip("-") + "-data-request.xlsx"))
OWN = {o.get("kpi_id"): o.get("role") or o.get("name") for o in (REC.get("evago") or {}).get("kpi_owners", []) or []}

def missing(v):
    t = str(v or "").strip().lower()
    return not t or t.startswith(("requires", "to supply", "not sure"))

def kpi_rows():
    rows = []
    allk = [(k, False) for k in (REC.get("measurement") or {}).get("kpis", []) or []]
    fowner = {}
    for f in REC.get("features", []) or []:
        allk += [(k, True) for k in f.get("kpis", []) or []]
        for k in f.get("kpis", []) or []:
            fowner[k.get("kpi_id")] = re.sub(r"\s*\(suggested\)", "", str(f.get("change_owner") or ""))
    for k, is_feat in allk:
        kid = k.get("kpi_id"); reg = KREG.get(kid, {}); c = k.get("contract", {}) or {}
        formula = reg.get("formula") or c.get("formula") or ""
        if "÷" not in formula and "÷" in str(c.get("definition") or ""):
            formula = re.sub(r",\s*by .*$|\s*\(.*\)\s*$", "", str(c["definition"]))  # NEW KPI: use the record's own definition
        if "÷" in formula:
            num, den = [x.strip() for x in formula.split("÷", 1)]
            den = re.sub(r"\s*×.*$", "", den)
        else:
            num, den = (formula or k.get("name")), ""
        unit = c.get("unit") or reg.get("unit") or ""
        if not den and str(unit).startswith("%"):
            num, den = k.get("name"), "Eligible total (say what you counted)"
        kind = "pct" if unit.startswith("%") else ("aed" if CUR in unit or unit.startswith("AED") else "ratio")
        newp = str(c.get("baseline_value", "")).lower().startswith("new process")
        bv = str(c.get("baseline_value", ""))
        m = re.search(r"—\s*([^,(]+)", bv) if bv.upper().startswith("REQUIRES") else None
        owner = OWN.get(kid) or (m.group(1).strip() if m else None) or c.get("outcome_owner") or reg.get("owner_role") or fowner.get(kid) or "KPI Owner"
        period = "First 4–6 weeks after go-live" if newp else (reg.get("recommended_baseline") or "Trailing 12 months")
        note = "Leave blank until go-live" if newp else ("" if den else "Enter the value in Numerator; leave Denominator blank")
        name = k.get("name") + (" (watch-out)" if k.get("guardrail") else "")
        rows.append((kid, name, c.get("definition") or reg.get("definition") or "", num, None, den or "(none: single value)", None, kind, unit, period, None, owner, None, note or None))
    return rows

def input_rows():
    rows = []
    n = 0
    for b in (REC.get("economics") or {}).get("benefits", []) or []:
        for key, v in (b.get("inputs") or {}).items():
            if isinstance(v, dict) and missing(v.get("value")):
                n += 1
                src = str(v.get("source", "")).strip()
                rows.append((f"V{n}", f"{b.get('description')}: {key.replace('_', ' ')}", v.get("unit") or "", None, None, src or "BU Finance", f"Benefit {b.get('id')}", None))
        if b.get("category") == "CR" and not b.get("conversion_owner"):
            n += 1
            rows.append((f"V{n}", f"{b.get('description')}: how freed time becomes cash, and who owns it", "text", None, None, "Value Owner", f"Benefit {b.get('id')}", None))
    return rows

def question_rows():
    qs = []
    for i, q in enumerate((REC.get("context") or {}).get("open_questions", []) or [], start=1):
        m = re.search(r"\(([^()]*)\)\s*$", str(q))
        by = m.group(1) if m else "Value Owner"
        qs.append((f"Q{i}", re.sub(r"\s*\([^()]*\)\s*$", "", str(q)).strip('"'), by))
    if missing((REC.get("evago") or {}).get("value_owner", {}).get("name")):
        qs.append((f"Q{len(qs)+1}", "Who is the Value Owner (name and role)?", "BU CEO"))
    return qs
F = "Arial"
H = Font(name=F, bold=True, color="FFFFFF", size=10)
HF = PatternFill("solid", fgColor="1D4F91")
B = Font(name=F, size=10)
BB = Font(name=F, size=10, bold=True)
IN = Font(name=F, size=10, color="0000FF")
EX = Font(name=F, size=10, italic=True, color="7F7F7F")
LINK = Font(name=F, size=10, color="008000")
Y = PatternFill("solid", fgColor="FFFF00")
EXF = PatternFill("solid", fgColor="F2F2F2")
thin = Side(style="thin", color="D5DDE2")
BOX = Border(left=thin, right=thin, top=thin, bottom=thin)
WR = Alignment(wrap_text=True, vertical="top")

def header(ws, row, cols, widths):
    for i, (c, w) in enumerate(zip(cols, widths), start=1):
        x = ws.cell(row=row, column=i, value=c); x.font = H; x.fill = HF; x.alignment = WR; x.border = BOX
        ws.column_dimensions[x.column_letter].width = w
    ws.freeze_panes = ws.cell(row=row + 1, column=3)

def put(ws, r, c, v, font=B, fill=None, fmt=None):
    x = ws.cell(row=r, column=c, value=v); x.font = font; x.alignment = WR; x.border = BOX
    if fill: x.fill = fill
    if fmt: x.number_format = fmt
    return x

wb = Workbook()
# ---------------- Read me
ws = wb.active; ws.title = "Read me"
ws.column_dimensions["A"].width = 26; ws.column_dimensions["B"].width = 90
rows = [
    (f"{NAME}: data request", None),
    ("Purpose", f"These figures turn the {NAME} value record from 'to size' into an indicative value range, and anchor each KPI's target range to where the business is today."),
    ("What to fill", "Only the yellow cells. Blue text is what you type; black cells are formulas that calculate themselves; green cells pull figures from another tab."),
    ("Period", "Trailing 12 months unless a row says otherwise. If you have monthly figures, add them on the 'Monthly (optional)' tab: they let VALOR check seasonality."),
    ("Every figure needs a source", "Name the system or report (e.g. 'Booking system export, Oct 2025–Sep 2026'). Figures without a source are recorded as asserted and shown as unsourced."),
    ("If you don't know", "Leave the value blank and write 'not sure' in Notes. It stays on the record as 'to supply' with your name; nothing is guessed."),
    ("Example rows", "Grey italic rows marked EXAMPLE show the expected format. They are not real data and are ignored when the sheet is loaded."),
    ("Percentages", "Enter the counts (numerator and denominator); the rate calculates itself. Don't type percentages."),
    ("Currency", f"{CUR}. Excluding VAT."),
    ("Return to", f"{A.contact}. VALOR loads the sheet into the value record (scripts/load_data_request.py) and redraws the driver tree."),
    ("Confidentiality", "Business data stays in this value record only; it is never added to the VALOR registers."),
]
for i, (a, b) in enumerate(rows, start=1):
    ca = ws.cell(row=i, column=1, value=a); cb = ws.cell(row=i, column=2, value=b)
    ca.font = Font(name=F, size=14 if i == 1 else 10, bold=True); cb.font = B; ca.alignment = WR; cb.alignment = WR
legend_r = len(rows) + 2
ws.cell(row=legend_r, column=1, value="Legend").font = BB
for j, (fill, font, label) in enumerate([(Y, IN, "Fill in"), (None, B, "Formula, calculates itself"), (None, LINK, "Linked from another tab"), (EXF, EX, "EXAMPLE row, not real data")], start=1):
    c = ws.cell(row=legend_r + j, column=1, value=label); c.font = font
    if fill: c.fill = fill
    c.border = BOX

# ---------------- Baselines
ws = wb.create_sheet("Baselines")
cols = ["KPI ID", "KPI", "Definition", "Numerator (what to count)", "Numerator value", "Denominator (what to divide by)", "Denominator value",
        "Today (calculated)", "Unit", "Period covered", "Source system or report", "Supplied by", "Date supplied", "Notes"]
header(ws, 1, cols, [11, 26, 38, 30, 14, 30, 14, 13, 11, 22, 28, 20, 13, 28])
kpis = [
    ("EXAMPLE", "Repeat customer rate (90 days)", "EXAMPLE ROW: format only", "Customers who booked again within 90 days", 1200, "Customers with a booking", 4000, "pct", "%", "Oct 2025–Sep 2026", "Booking system export", "Marketing Manager", None, "Not real data"),
]
kpis += kpi_rows()
for r, k in enumerate(kpis, start=2):
    ex = k[0] == "EXAMPLE"
    font_txt = EX if ex else B
    for c, v in enumerate(k[:4], start=1):
        put(ws, r, c, v, font_txt, EXF if ex else None)
    put(ws, r, 5, k[4], EX if ex else IN, EXF if ex else Y, "#,##0")
    put(ws, r, 6, k[5], font_txt, EXF if ex else None)
    put(ws, r, 7, k[6], EX if ex else IN, (EXF if ex else (None if str(k[5]).startswith("(none") else Y)), "#,##0")
    fmt = {"pct": "0.0%", "aed": "#,##0", "ratio": "0.0"}[k[7]]
    single = str(k[5]).startswith("(none")
    put(ws, r, 8, f'=IF(E{r}="","",E{r})' if single else f'=IF(OR(E{r}="",G{r}="",G{r}=0),"",E{r}/G{r})', EX if ex else B, EXF if ex else None, fmt)
    put(ws, r, 9, k[8], font_txt, EXF if ex else None)
    put(ws, r, 10, k[9], EX if ex else IN, EXF if ex else Y)
    put(ws, r, 11, k[10], EX if ex else IN, EXF if ex else Y)
    put(ws, r, 12, k[11], font_txt, EXF if ex else None)
    put(ws, r, 13, k[12], EX if ex else IN, EXF if ex else Y, "dd-mmm-yyyy")
    put(ws, r, 14, k[13], EX if ex else IN, EXF if ex else Y)
dv = DataValidation(type="decimal", operator="greaterThanOrEqual", formula1="0", allow_blank=True,
                    error="Enter a count or amount of zero or more", errorTitle="Not a valid number")
ws.add_data_validation(dv); dv.add(f"E3:E{len(kpis)+1}"); dv.add(f"G3:G{len(kpis)+1}")
ws.cell(row=1, column=8).comment = Comment("Calculated from the two values. Percentages are stored as fractions.", "VALOR")

# ---------------- Monthly
wm = wb.create_sheet("Monthly (optional)")
months = ["Oct-25", "Nov-25", "Dec-25", "Jan-26", "Feb-26", "Mar-26", "Apr-26", "May-26", "Jun-26", "Jul-26", "Aug-26", "Sep-26"]
header(wm, 1, ["KPI ID", "Line"] + months + ["12-month total"], [11, 30] + [10] * 12 + [14])
mr = 2
for k in kpis[1:]:
    for line in ("Numerator", "Denominator"):
        put(wm, mr, 1, k[0]); put(wm, mr, 2, f"{line}: {k[3] if line == 'Numerator' else k[5]}")
        for c in range(3, 15):
            put(wm, mr, c, None, IN, Y, "#,##0")
        put(wm, mr, 15, f'=IF(COUNT(C{mr}:N{mr})=0,"",SUM(C{mr}:N{mr}))', B, None, "#,##0")
        mr += 1
put(wm, mr + 1, 1, "Monthly figures are optional. If you fill them, the 12-month totals should match the Baselines tab.", B)
wm.freeze_panes = "C2"

# ---------------- Value inputs
wv = wb.create_sheet("Value inputs")
header(wv, 1, ["Ref", "Item", "Unit", "Value", "Source system or report", "Supplied by", "Used for", "Notes"], [7, 46, 20, 14, 28, 22, 36, 28])
items = [
    ("EX", "EXAMPLE: contribution margin per booking", f"{CUR} per booking", 85, "Finance P&L by service line", "BU Finance", "Format only", "Not real data"),
]
items += input_rows()
for r, it in enumerate(items, start=2):
    ex = it[0] == "EX"
    formula = isinstance(it[3], str) and it[3].startswith("=")
    for c, v in enumerate(it, start=1):
        if c == 4:
            if ex:
                put(wv, r, c, v, EX, EXF, "#,##0")
            elif formula:
                put(wv, r, c, v, LINK if "Baselines" in v else B, None, "#,##0.00" if "SUMPRODUCT" in v else "#,##0")
            else:
                put(wv, r, c, v, IN, Y, "@" if it[2] == "text" else ("#,##0.00" if " per " in str(it[2]) else "#,##0"))
        elif c in (5, 8) and not ex and not formula:
            put(wv, r, c, v, IN, Y)
        else:
            put(wv, r, c, v, EX if ex else B, EXF if ex else None)
qr = len(items) + 3
put(wv, qr, 1, "Context questions", BB)
header_q = ["Ref", "Question", "", "Answer", "", "Answered by"]
for i, h in enumerate(header_q, start=1):
    if h:
        x = wv.cell(row=qr + 1, column=i, value=h); x.font = H; x.fill = HF; x.border = BOX
qs = question_rows()
dvq = DataValidation(type="list", formula1='"Relaunch,New business,Not sure"', allow_blank=True)
wv.add_data_validation(dvq)
for i, (ref, q, by) in enumerate(qs, start=qr + 2):
    put(wv, i, 1, ref); put(wv, i, 2, q); put(wv, i, 4, None, IN, Y); put(wv, i, 6, by)
    wv.merge_cells(start_row=i, start_column=2, end_row=i, end_column=3)
    wv.merge_cells(start_row=i, start_column=4, end_row=i, end_column=5)
    if "relaunch" in q.lower():
        dvq.add(wv.cell(row=i, column=4).coordinate)
wv.freeze_panes = "C2"

# ---------------- Costs
wc = wb.create_sheet("Costs")
header(wc, 1, ["Ref", f"Cost ({CUR}, excl. VAT)", "Type", "Year 0 (build)", "Year 1", "Year 2", "Year 3", "Total", "Source or estimate basis", "Supplied by"],
       [7, 40, 10, 14, 13, 13, 13, 14, 32, 20])
# Generic cost lines (VALOR K1–K5); a record can replace them with economics.cost_lines_requested:
#   - {item: "e-KYC vendor fee per verification", type: Run, owner: Procurement}
costs = [("K1", "Build or licence set-up", "Build", "ITBP"),
         ("K2", "Hosting, licences and support", "Run", "ITBP"),
         ("K3", "Training, process change and launch", "Change", "Operations Manager"),
         ("K4", "Per-transaction fees (e.g. identity checks, payments, messaging, channel commissions)", "Run", "Procurement"),
         ("K5", "Partner or customer incentives and launch marketing", "Run", "Commercial Manager")]
_req = ((REC.get("economics") or {}).get("cost_lines_requested") or [])
if _req:
    costs = [(f"K{i}", str(x.get("item")), str(x.get("type", "Run")).capitalize(), str(x.get("owner", "ITBP")))
             for i, x in enumerate(_req, start=1)]
for r, (ref, name, typ, by) in enumerate(costs, start=2):
    put(wc, r, 1, ref); put(wc, r, 2, name); put(wc, r, 3, typ)
    for c in range(4, 8):
        put(wc, r, c, None, IN, Y, "#,##0;(#,##0);-")
    put(wc, r, 8, f"=SUM(D{r}:G{r})", B, None, "#,##0;(#,##0);-")
    put(wc, r, 9, None, IN, Y); put(wc, r, 10, by)
tr = len(costs) + 2
put(wc, tr, 2, "Total", BB)
for c, col in zip(range(4, 9), "DEFGH"):
    put(wc, tr, c, f"=SUM({col}2:{col}{tr-1})", BB, None, "#,##0;(#,##0);-")
put(wc, tr + 2, 2, "Run and change costs are required: enter 0 with a reason if there are none.", B)
wc.freeze_panes = "C2"

# ---------------- Status
st = wb.create_sheet("Status")
header(st, 1, ["Section", "Items to supply", "Supplied", "Still open"], [30, 16, 12, 12])
st.freeze_panes = None
n_k = len(kpis) - 1
status = [
    ("Baselines (both values)", f"={n_k}", f"=SUMPRODUCT((Baselines!E3:E{len(kpis)+1}<>\"\")*(Baselines!G3:G{len(kpis)+1}<>\"\"))"),
    ("Baseline sources", f"={n_k}", f"=COUNTA(Baselines!K3:K{len(kpis)+1})"),
    ("Value inputs", f"={len(items)-1}", f"=COUNTA('Value inputs'!D3:D{len(items)+1})"),
    ("Context questions", f"={len(qs)}", f"=COUNTA('Value inputs'!D{qr+2}:D{qr+1+len(qs)})"),
    ("Cost lines with a source", f"={len(costs)}", f"=COUNTA(Costs!I2:I{tr-1})"),
]
for r, (name, tot, done) in enumerate(status, start=2):
    put(st, r, 1, name); put(st, r, 2, tot, B, None, "0"); put(st, r, 3, done, B, None, "0"); put(st, r, 4, f"=B{r}-C{r}", BB, None, "0")
put(st, len(status) + 3, 1, "KPIs for new processes stay open until go-live; that's expected.", B)
wb.move_sheet("Status", offset=-(len(wb.sheetnames) - 2))
wb.save(out)
print(json.dumps({"output": out, "kpis": len(kpis) - 1, "value_inputs": len(items) - 1, "questions": len(qs)}))
