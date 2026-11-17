#!/usr/bin/env python3
"""VALOR scores: value coherence (rubric v2), confidence and verdict (valor-core.md §9, §11–§13).

Usage:  python3 score.py input.json  >  scores.json

Input JSON (link scores: 1 in place · 0.5 partial · 0 missing · null not applicable):
{
  "stage": "shape",                       # shape | commit | baseline | track | capture
  "strands": {
    "strategic":  {"intent_linked_to_pillar": 1, "drivers_under_epic_pillars": 1, "falsifier_stated": 0.5,
                   "contributes_to_epic_hypothesis": 1},   # last link: feature records only (valor-core §13)
    "conversion": {"behaviour_change_named": 1, "change_owned_by_business_role": 0.5, "business_leading_kpi": 1,
                   "acceptance_kpi_if_third_party": null, "adoption_risk_addressed": 0.5},
    "counting":   {"benefits_counted_once": 0.5, "alternative_uses_resolved": 1,
                   "freed_capacity_owner_or_not_counted": 1, "value_measure_business_owner": 0.5},
    "data":       {"kpis_match_register_or_flagged": 1, "units_roll_up": 1, "baseline_method_comparable": 1,
                   "data_source_or_plan": 0.5}
  },
  "confidence": {
    "evidence_tier": "T0",                # T0 | T1 | T2 | T3
    "kpis_total": 5, "baselines_supplied": 0,
    "assumptions_total": 4, "assumptions_proven": 0, "assumptions_partly": 1,
    "agreements": {"confirmed": 0, "recorded": 1, "items": 6},   # items = hypothesis (epics) + each KPI range + each counted or tracked benefit
    "attribution_method_chosen": false
  },
  "post_delivery": {"adoption_on_track": null}   # true/false once Business Leading actuals exist (track/capture)
}

Output: strand percentages, headline coherence (conversion gate applied), weakest strand and link,
confidence by component, next best step, verdict (rubric name and display name), and the standard explanations.
"""
import json, sys

EXPLAIN = {
    "coherence": "How completely the chain from intent to value holds together. It shows the case is well-formed, not how big or proven the value is.",
    "confidence": "How far the value is backed by evidence and agreement. It rises as baselines arrive, assumptions are tested and owners agree the measures.",
    "verdict": "Where the epic stands on two questions: will behaviour change (conversion), and is the value backed (confidence)? It says what to do next, not how big the value is.",
}
DISPLAY = {
    "Fund": "Fund — proceed at full scope",
    "Prove": "Prove — fund a pilot, collect baselines",
    "Fix adoption": "Fix adoption — the numbers hold, the change needs an owner",
    "Rework or stop": "Redesign adoption — design the change before funding",
    "Fix the logic first": "Not yet ready to assess",
    "Scale": "Scale", "Continue, prove attribution": "Continue, prove attribution",
    "Adapt: fix adoption": "Adapt adoption", "Stop or redirect": "Stop or redirect",
}
TIER_POINTS = {"T0": 0, "T1": 15, "T2": 30, "T3": 40}


def strand_score(links):
    vals = [v for v in links.values() if v is not None]
    if not vals:
        return 0, "not assessed"
    weakest = min((k for k, v in links.items() if v is not None), key=lambda k: links[k])
    return round(100 * sum(vals) / len(vals)), (weakest if links[weakest] < 1 else None)


def run(cfg):
    strands, weak = {}, {}
    for name in ("strategic", "conversion", "counting", "data"):
        strands[name], weak[name] = strand_score(cfg["strands"].get(name, {}))
    present = [v for v in strands.values() if v is not None]
    headline = round(sum(present) / len(present)) if present else 0
    capped = False
    if strands["conversion"] is not None and strands["conversion"] < 75 and headline > 60:
        headline, capped = 60, True
    weakest = min((k for k in strands if strands[k] is not None), key=lambda k: strands[k])

    c = cfg["confidence"]
    comp = {
        "finance_validation": TIER_POINTS[c.get("evidence_tier", "T0")],
        "baselines": round(20 * c.get("baselines_supplied", 0) / c["kpis_total"], 1) if c.get("kpis_total") else 0,
        "assumptions": round(20 * (c.get("assumptions_proven", 0) + 0.5 * c.get("assumptions_partly", 0))
                             / c["assumptions_total"], 1) if c.get("assumptions_total") else 0,
        "agreements": 0,
        "attribution": 10 if c.get("attribution_method_chosen") else 0,
    }
    a = c.get("agreements", {})
    if a.get("items"):
        comp["agreements"] = round(10 * (a.get("confirmed", 0) + 0.5 * a.get("recorded", 0)) / a["items"], 1)
    maxima = {"finance_validation": 40, "baselines": 20, "assumptions": 20, "agreements": 10, "attribution": 10}
    confidence = round(sum(comp.values()))
    steps = {
        "baselines": "Supply measured baselines for the KPIs",
        "attribution": "Choose an attribution method (e.g. staggered rollout) before release",
        "agreements": "Get owners to confirm the hypothesis, KPI ranges and benefits",
        "assumptions": "Test the open assumptions",
        "finance_validation": "Have Finance validate baseline, unit economics and method (T1 → T2)",
    }
    # soonest movable first: owner actions before Finance validation
    order = ["baselines", "attribution", "agreements", "assumptions", "finance_validation"]
    gaps = [(k, maxima[k] - comp[k]) for k in order if maxima[k] - comp[k] > 0]
    next_step = {"component": gaps[0][0], "step": steps[gaps[0][0]], "points_available": round(gaps[0][1], 1)} if gaps else None

    stage = cfg.get("stage", "shape")
    entry_fail = [k for k in ("strategic", "counting", "data") if strands[k] is not None and strands[k] < 60]
    post = cfg.get("post_delivery", {}) or {}
    if stage == "shape":
        verdict = None
        why = "no verdict before Commit" + (f"; fix before Commit: {', '.join(f'{k} ({weak[k]})' for k in entry_fail)}" if entry_fail else "")
    elif entry_fail:
        verdict = "Fix the logic first"
        why = f"{', '.join(entry_fail)} strand below 60% — weakest link: {weak[entry_fail[0]]}"
    elif stage in ("track", "capture") and post.get("adoption_on_track") is not None:
        high = c.get("evidence_tier") in ("T2", "T3") and c.get("attribution_method_chosen")
        on = post["adoption_on_track"]
        verdict = {(True, True): "Scale", (True, False): "Continue, prove attribution",
                   (False, True): "Adapt: fix adoption", (False, False): "Stop or redirect"}[(on, bool(high))]
        why = f"adoption {'on track' if on else 'lagging'}; confidence {'high' if high else 'low'} (T2+ with attribution)"
    else:
        conv_ok = (strands["conversion"] or 0) >= 75
        conf_ok = confidence >= 50
        verdict = {(True, True): "Fund", (True, False): "Prove", (False, True): "Fix adoption",
                   (False, False): "Rework or stop"}[(conv_ok, conf_ok)]
        why = f"conversion {strands['conversion']}% ({'≥' if conv_ok else '<'}75) · confidence {confidence} ({'≥' if conf_ok else '<'}50)"

    return {
        "strands": strands, "weakest_link_by_strand": weak,
        "coherence": {"headline": headline, "capped_by_conversion_gate": capped, "weakest_strand": weakest,
                      "weakest_link": weak[weakest], "explain": EXPLAIN["coherence"]},
        "confidence": {"score": confidence, "label": "Low" if confidence < 40 else "Medium" if confidence < 70 else "High",
                       "components": comp, "next_best_step": next_step, "explain": EXPLAIN["confidence"]},
        "verdict": {"rubric": verdict, "display": ("Shaping — " + why) if verdict is None else
                    (f"Not yet ready to assess — {weak[entry_fail[0]]}" if verdict == "Fix the logic first" else DISPLAY.get(verdict, verdict)),
                    "why": why, "explain": EXPLAIN["verdict"]},
    }


if __name__ == "__main__":
    print(json.dumps(run(json.load(open(sys.argv[1]))), indent=2, ensure_ascii=False))
