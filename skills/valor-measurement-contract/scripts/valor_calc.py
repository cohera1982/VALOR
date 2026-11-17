#!/usr/bin/env python3
"""VALOR full economics (valor-value-economics, Finance-ready mode).

Usage:  python3 valor_calc.py input.json  >  results.json

Input JSON (the FVR `economics` section, with numbers supplied by the client or Finance):
{
  "currency": "AED",
  "horizon_years": 3,
  "discount_rate": null,                 # Finance-approved only; null => NPV not computed
  "sensitivity_pct": 0.2,                # flex benefits and costs ±20% for the range
  "benefits": [
    {"id": "B1", "category": "CS", "annual_value": 400000, "risk_adjustment_pct": 0.2,
     "ramp": [0.3, 0.8, 1.0], "basis": "client", "tier": "T1",
     "conversion_mechanism": "", "exclusive_group": "", "selected": true}
  ],
  "costs": [
    {"id": "C1", "type": "build", "timing": "upfront", "annual_value": 250000},
    {"id": "C2", "type": "run", "timing": "annual", "annual_value": 40000},
    {"id": "C3", "type": "change", "timing": "upfront", "annual_value": 60000}
  ]
}

Counting rules applied (valor-core §5, §9; benchmark-method §4):
- NF never monetised; CR counted only with a conversion mechanism; peer-median (illustrative) never counted.
- WC is a one-off cash release: reported separately, never in annual value, NPV or payback.
- Exclusive groups (alternative uses of the same capacity): exactly one selected benefit counts; anything else is an error.
- Upfront costs fall in year 0; annual costs in years 1..horizon. Ramp defaults to 1.0 for missing years.
- risk_adjustment_pct and ramp values are FRACTIONS (0.2 = 20%); values above 1 are errors.
- Non-numeric values ("REQUIRES VALIDATION") are treated as to size: benefits are excluded, costs are errors.
- Run and change costs are required (C24): their absence is reported as an error.
"""
import json, sys


def num(v):
    try:
        return None if v is None or v == "" else float(v)
    except (TypeError, ValueError):
        return None


def schedule(cfg, b_mult=1.0, c_mult=1.0):
    H = int(cfg.get("horizon_years", 3))
    ben = [0.0] * (H + 1)
    cost = [0.0] * (H + 1)
    for b in cfg["_counted"]:
        ramp = [num(x) or 0 for x in (b.get("ramp") or [])]
        adj = 1 - (num(b.get("risk_adjustment_pct")) or 0)
        for y in range(1, H + 1):
            r = ramp[y - 1] if y - 1 < len(ramp) else 1.0
            ben[y] += num(b["annual_value"]) * r * adj * b_mult
    for c in cfg.get("costs", []):
        v = (num(c.get("annual_value")) or 0) * c_mult
        if c.get("timing", "annual") == "upfront":
            cost[0] += v
        else:
            for y in range(1, H + 1):
                cost[y] += v
    net = [ben[y] - cost[y] for y in range(H + 1)]
    return ben, cost, net


def npv(net, rate):
    return sum(v / (1 + rate) ** y for y, v in enumerate(net))


def payback(net):
    cum = 0.0
    for y, v in enumerate(net):
        prev = cum
        cum += v
        if cum >= 0 and y > 0:
            return round(y - 1 + (-prev / v if v else 0), 2)
    return None


def run(cfg):
    errors, counted, excluded, wc = [], [], [], []
    groups = {}
    for b in cfg.get("benefits", []):
        g = b.get("exclusive_group")
        if g:
            groups.setdefault(g, []).append(b)
    for g, items in groups.items():
        n = sum(1 for b in items if b.get("selected"))
        if n != 1:
            errors.append(f"exclusive_group '{g}' has {n} selected benefits; exactly one must be selected (C28)")
    for b in cfg.get("benefits", []):
        rp = num(b.get("risk_adjustment_pct"))
        if rp is not None and not 0 <= rp <= 1:
            errors.append(f"{b['id']}: risk_adjustment_pct {rp} must be a fraction (0.2 = 20%)")
        if any((num(x) or 0) > 1 for x in (b.get("ramp") or [])):
            errors.append(f"{b['id']}: ramp values must be fractions (1.0 = full realisation)")
    if errors:
        return {"errors": errors}
    types = {c.get("type") for c in cfg.get("costs", [])}
    for need in ("run", "change"):
        if need not in types:
            errors.append(f"no '{need}' cost supplied (C24): add it, or record it as 0 with a reason")
    for c in cfg.get("costs", []):
        if num(c.get("annual_value")) is None:
            errors.append(f"cost {c.get('id')} has no value ({c.get('annual_value')!r}): to supply — ITBP")
    for b in cfg.get("benefits", []):
        cat = b["category"].upper()
        why = None
        if num(b.get("annual_value")) is None:
            why = "no annual value (to size)"
        elif cat == "NF":
            why = "non-financial: tracked in natural units"
        elif b.get("basis") == "peer_median":
            why = "illustrative at peer median: never counted (C35)"
        elif cat == "CR" and not b.get("conversion_mechanism"):
            why = "capacity released without a conversion mechanism (C03)"
        elif b.get("exclusive_group") and not b.get("selected"):
            why = f"alternative use in '{b['exclusive_group']}' not selected (C28)"
        if cat == "WC" and why is None:
            wc.append({"id": b["id"], "one_off": num(b["annual_value"])})
            continue
        (excluded if why else counted).append(dict(b, _why=why) if why else b)
    cfg = dict(cfg, _counted=counted)
    ben, cost, net = schedule(cfg)
    rate = cfg.get("discount_rate")
    p = float(cfg.get("sensitivity_pct", 0.2))
    out = {
        "currency": cfg.get("currency", "AED"),
        "errors": errors,
        "counted_benefits": [b["id"] for b in counted],
        "excluded_benefits": [{"id": b["id"], "reason": b["_why"]} for b in excluded],
        "years": [{"year": y, "benefits": round(ben[y]), "costs": round(cost[y]), "net": round(net[y]),
                   "cumulative": round(sum(net[: y + 1]))} for y in range(len(net))],
        "total_benefits": round(sum(ben)), "total_costs": round(sum(cost)), "total_net": round(sum(net)),
        "roi": round(sum(net) / sum(cost), 2) if sum(cost) else None,
        "payback_years": payback(net),
        "npv": round(npv(net, rate)) if rate is not None else None,
        "npv_note": None if rate is not None else "No Finance-approved discount rate: NPV not computed",
        "one_off_working_capital": wc,
        "lowest_input_tier": min((b.get("tier", "T0") for b in counted), default="T0"),
    }
    lo = schedule(cfg, 1 - p, 1 + p)[2]
    hi = schedule(cfg, 1 + p, 1 - p)[2]
    out["sensitivity"] = {"pct": p, "total_net_range": [round(sum(lo)), round(sum(hi))],
                          "npv_range": [round(npv(lo, rate)), round(npv(hi, rate))] if rate is not None else None,
                          "payback_range": [payback(lo), payback(hi)]}
    out["label"] = ("Projected" + ("" if out["lowest_input_tier"] in ("T2", "T3") else ", not Finance-validated")
                    + ". Board totals include only T2 and above.")
    return out


if __name__ == "__main__":
    print(json.dumps(run(json.load(open(sys.argv[1]))), indent=2))
