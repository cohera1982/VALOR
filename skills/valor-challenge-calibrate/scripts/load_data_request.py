#!/usr/bin/env python3
"""Load a completed VALOR data request workbook into a value record.

Usage:  python3 load_data_request.py RECORD.yaml REQUEST.xlsx [--out RECORD.yaml]

Reads the standard tabs (recalculate the workbook first if it was edited outside Excel):
  Baselines     KPI ID | ... | Numerator value | ... | Denominator value | Today (calculated) | Unit | Period | Source | Supplied by | Date | Notes
  Value inputs  Ref | Item | Unit | Value | Source | Supplied by | Used for | Notes   (+ Context questions block)
  Costs         Ref | Cost | Type | Year 0 | Year 1 | Year 2 | Year 3 | Total | Source | Supplied by
Rows marked EXAMPLE / EX are ignored. Blank values stay as REQUIRES VALIDATION with the owner's name.

Writes:
  - KPI contracts (epic and feature KPIs): baseline_value, baseline_period, data_source, baseline_supplied_by
  - economics.data_inputs: every value input with unit, source and owner (economics maps them to benefits)
  - economics.costs: one entry per cost line with yearly values, type, timing and source
  - context.answers: the context questions
  - record.revision_log entry; evidence_tier is left for the challenge step to set
Prints a JSON summary of what was filled and what is still open.
"""
import argparse, datetime, json, sys
from pathlib import Path

import yaml
from openpyxl import load_workbook


def fmt(v, unit):
    if v is None or v == "":
        return None
    if unit == "%":
        return f"{float(v) * 100:.1f}%"
    if isinstance(v, (int, float)):
        return f"{v:,.2f}".rstrip("0").rstrip(".") + (f" {unit}" if unit else "")
    return str(v)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("record"); ap.add_argument("workbook"); ap.add_argument("--out")
    a = ap.parse_args()
    rec = yaml.safe_load(Path(a.record).read_text(encoding="utf-8"))
    wb = load_workbook(a.workbook, data_only=True)
    filled, open_items = [], []

    contracts = {}
    for k in (rec.get("measurement", {}) or {}).get("kpis", []) or []:
        contracts[k.get("kpi_id")] = k.setdefault("contract", {})
    for f in rec.get("features", []) or []:
        for k in f.get("kpis", []) or []:
            contracts[k.get("kpi_id")] = k.setdefault("contract", {})

    if "Baselines" in wb.sheetnames:
        for row in wb["Baselines"].iter_rows(min_row=2, values_only=True):
            kid = row[0]
            if not kid or str(kid).upper().startswith("EX"):
                continue
            num, den, today, unit, period, source, by, date, notes = row[4], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13]
            c = contracts.get(kid)
            if c is None:
                open_items.append(f"{kid}: in the sheet but not in the record (not loaded)")
                continue
            if today in (None, ""):
                if num not in (None, "") and den in (None, "", 0):
                    open_items.append(f"{kid}: numerator given but no denominator")
                c["baseline_value"] = f"REQUIRES VALIDATION — {by}" + (f" ({notes})" if notes else "")
                open_items.append(f"{kid} baseline — {by}")
                continue
            c["baseline_value"] = fmt(today, unit)
            c["baseline_counts"] = {"numerator": num, "denominator": den}
            c["baseline_period"] = period or ""
            c["data_source"] = source or "asserted — source to supply (" + str(by) + ")"
            c["baseline_supplied_by"] = by
            if date:
                c["baseline_date"] = str(date)[:10]
            filled.append(f"{kid} baseline {c['baseline_value']}" + ("" if source else " (no source: marked asserted)"))

    econ = rec.setdefault("economics", {})
    if "Value inputs" in wb.sheetnames:
        ws = wb["Value inputs"]
        inputs, answers, in_q = {}, {}, False
        for row in ws.iter_rows(min_row=2, values_only=True):
            ref = row[0]
            if ref == "Context questions":
                in_q = True; continue
            if not ref or str(ref).upper().startswith("EX") or ref == "Ref":
                continue
            if in_q:
                q, ans, by = row[1], row[3], row[5]
                answers[ref] = {"question": q, "answer": ans if ans not in (None, "") else f"REQUIRES VALIDATION — {by}"}
                (filled if ans not in (None, "") else open_items).append(f"{ref} {'answered' if ans else '— ' + str(by)}")
                continue
            item, unit, val, src, by, used = row[1], row[2], row[3], row[4], row[5], row[6]
            inputs[ref] = {"item": item, "unit": unit, "value": val if val not in (None, "") else f"REQUIRES VALIDATION — {by}",
                           "source": src or (f"asserted — source to supply ({by})" if val not in (None, "") else ""), "used_for": used}
            (filled if val not in (None, "") else open_items).append(f"{ref} {item}" + ("" if val not in (None, "") else f" — {by}"))
        econ["data_inputs"] = inputs
        rec.setdefault("context", {})["answers"] = answers

    if "Costs" in wb.sheetnames:
        costs = []
        for row in wb["Costs"].iter_rows(min_row=2, values_only=True):
            ref = row[0]
            if not ref or not str(ref).startswith("K"):
                continue
            years = [row[3], row[4], row[5], row[6]]
            if all(y in (None, "") for y in years):
                open_items.append(f"{ref} {row[1]} — {row[9]}")
                continue
            y0 = float(years[0] or 0)
            annual = [float(y or 0) for y in years[1:]]
            costs.append({"id": ref, "type": str(row[2]).lower(), "description": row[1],
                          "timing": "upfront" if y0 and not any(annual) else "annual",
                          "annual_value": y0 if y0 and not any(annual) else (sum(annual) / len([x for x in annual if x]) if any(annual) else 0),
                          "by_year": {"y0": y0, "y1": annual[0], "y2": annual[1], "y3": annual[2]},
                          "source": row[8] or f"asserted — source to supply ({row[9]})"})
            filled.append(f"{ref} {row[1]}")
        if costs:
            econ["costs"] = costs

    rec.setdefault("record", {}).setdefault("revision_log", []).append(
        {"date": datetime.date.today().isoformat(), "by": "load_data_request.py",
         "change": f"Loaded data request {Path(a.workbook).name}: {len(filled)} items filled, {len(open_items)} still open"})
    out = Path(a.out or a.record)
    out.write_text(yaml.safe_dump(rec, sort_keys=False, allow_unicode=True, width=120), encoding="utf-8")
    print(json.dumps({"output": str(out), "filled": filled, "still_open": open_items}, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()
