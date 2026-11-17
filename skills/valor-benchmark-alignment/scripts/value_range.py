#!/usr/bin/env python3
"""VALOR indicative value range calculator (benchmark-method.md §4).

Usage:  python3 value_range.py input.json  >  results.json

Input JSON:
{
  "currency": "AED",                 # display currency
  "fx_to_display": {"USD": 3.6725},  # optional overrides (AED per unit of currency)
  "benefits": [
    {
      "id": "B1",
      "category": "CR",              # CS | CA | CR | RV | MG | WC | RR | NF
      "description": "Finance hours freed from COGS compilation",
      "basis": "client",             # client | peer_median  (peer_median => illustrative, never counted)
      "baseline": 9216,              # baseline quantity (hours, cost, volume, balance, events); null => to size
      "baseline_source": "Group FC, trailing 12m",
      "improvement_low": 0.20,       # FRACTION (0.20 = 20%); null => to size
      "improvement_high": 0.35,
      "improvement_source": "BM-FIN-BG-01-2",   # a BM- id => benchmarked; anything else => suggested
      "scope": "partial",            # full | partial  (partial => low .. midpoint, method §3)
      "range_already_scoped": false, # true when benchmark-alignment already applied the partial-scope rule
      "unit_value": 120,             # value per unit of baseline; omit for CS/CA/WC when baseline is money
      "unit_value_currency": "AED",
      "unit_value_source": "Finance BP",
      "conversion_mechanism": "",    # CR only: e.g. "no backfill of 2 roles on attrition"
      "conversion_owner": ""         # CR only: business role accountable; both needed for counting
    }
  ]
}

Output: per benefit low/high (display currency or natural units), counting label, tier, range basis;
totals of counted annual value and one-off WC kept separately; "to size" when nothing could be counted.
Errors (improvement above 1, unknown category) are reported in "errors" and the benefit is skipped.
"""
import json, sys

DEFAULT_FX = {"AED": 1.0, "USD": 3.6725, "SAR": 3.6725 / 3.75}
MONEY_BASELINE = {"CS", "CA", "WC"}
CATS = {"CS", "CA", "CR", "RV", "MG", "WC", "RR", "NF"}


def num(v):
    try:
        return None if v is None or v == "" else float(v)
    except (TypeError, ValueError):
        return None


def run(cfg):
    disp = cfg.get("currency", "AED")
    fx = dict(DEFAULT_FX)
    fx.update(cfg.get("fx_to_display", {}))
    if disp != "AED":
        base = fx[disp]
        fx = {k: v / base for k, v in fx.items()}
    out, errors = [], []
    counted_low = counted_high = wc_low = wc_high = 0.0
    any_counted = False
    for b in cfg["benefits"]:
        cat = str(b.get("category", "")).upper()
        r = {"id": b.get("id"), "category": cat, "description": b.get("description", "")}
        if cat not in CATS:
            errors.append(f"{b.get('id')}: unknown category '{cat}'"); continue
        lo, hi, base = num(b.get("improvement_low")), num(b.get("improvement_high")), num(b.get("baseline"))
        src = str(b.get("improvement_source", ""))
        r["range_basis"] = "benchmarked" if src.startswith("BM-") else ("suggested" if src else "unsourced")
        if lo is not None and hi is not None and (lo > 1 or hi > 1 or lo < 0 or hi < 0 or lo > hi):
            errors.append(f"{b.get('id')}: improvement must be fractions between 0 and 1 with low <= high "
                          f"(got {lo}, {hi}); 20% is 0.20"); continue
        if cat == "NF":
            if base is None or lo is None or hi is None:
                r.update(low=None, high=None, unit="natural units", counting="Tracked, not monetised",
                         tier="T0", note="to size in natural units — owner to supply baseline and range")
            else:
                if b.get("scope", "full") == "partial" and not b.get("range_already_scoped"):
                    hi = (lo + hi) / 2
                r.update(low=round(base * lo, 2), high=round(base * hi, 2), unit="natural units",
                         counting="Tracked, not monetised", tier="T1" if b.get("basis", "client") == "client" else "T0")
            out.append(r); continue
        if base is None or lo is None or hi is None:
            missing = [n for n, v in (("baseline", base), ("improvement range", lo if hi is not None else None)) if v is None]
            no_conv = cat == "CR" and not (b.get("conversion_mechanism") and b.get("conversion_owner"))
            r.update(low=None, high=None, unit="to size",
                     counting="Not counted (no conversion mechanism with an owner)" if no_conv else "To confirm", tier="T0",
                     note="to size — missing " + " and ".join(missing))
            out.append(r); continue
        if b.get("scope", "full") == "partial" and not b.get("range_already_scoped"):
            hi = (lo + hi) / 2.0
        r["improvement_applied"] = [round(lo, 4), round(hi, 4)]
        units_lo, units_hi = base * lo, base * hi
        uv = num(b.get("unit_value"))
        if uv is None and cat not in MONEY_BASELINE:
            r.update(low=round(units_lo, 2), high=round(units_hi, 2), unit="natural units", counting="To confirm",
                     tier="T1" if b.get("basis", "client") == "client" else "T0", note="unit value to supply — Finance")
            out.append(r); continue
        rate = (uv if uv is not None else 1.0) * fx.get(b.get("unit_value_currency", disp), 1.0)
        v_lo, v_hi = units_lo * rate, units_hi * rate
        illustrative = b.get("basis", "client") == "peer_median"
        if illustrative:
            counting, tier = "Not counted (illustrative at peer median, not your data)", "T0"
        elif cat == "CR" and not (b.get("conversion_mechanism") and b.get("conversion_owner")):
            counting, tier = "Not counted (no conversion mechanism with an owner)", "T1"
        elif cat == "WC":
            counting, tier = "Shown separately (one-off cash)", "T1"
        elif cat == "RR":
            counting, tier = "Counted (expected-loss, probabilistic)", "T1"
        else:
            counting, tier = "Counted", "T1"
        r.update(low=round(v_lo), high=round(v_hi), unit=disp + (" one-off" if cat == "WC" else " a year"),
                 counting=counting, tier=tier, natural_units=[round(units_lo, 2), round(units_hi, 2)])
        if counting.startswith("Counted"):
            counted_low += v_lo; counted_high += v_hi; any_counted = True
        elif cat == "WC" and not illustrative:
            wc_low += v_lo; wc_high += v_hi
        out.append(r)
    bases = {x.get("range_basis") for x in out if x.get("low") is not None and x["category"] != "NF"}
    label = ("Indicative, " + ("benchmarked" if bases == {"benchmarked"} else "partly benchmarked" if "benchmarked" in bases else "suggested ranges")
             + "; to validate — Finance. Not Board-reportable below T2.") if any_counted else "To size — no benefit could be counted yet."
    return {"currency": disp, "errors": errors, "benefits": out,
            "counted_annual_value": [round(counted_low), round(counted_high)] if any_counted else "to size",
            "one_off_working_capital": [round(wc_low), round(wc_high)] if (wc_low or wc_high) else None,
            "label": label}


if __name__ == "__main__":
    print(json.dumps(run(json.load(open(sys.argv[1]))), indent=2))
