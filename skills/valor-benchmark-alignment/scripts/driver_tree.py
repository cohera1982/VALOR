#!/usr/bin/env python3
"""VALOR value driver tree: renders an epic value record (and its features) as one page with an
Executive view, a Detailed view and a Gaps view, and checks the tree's links while it does so.

Usage:
  python3 driver_tree.py EPIC.yaml [FEATURE.yaml ...] [--out tree.html] [--standalone] [--refs DIR]

  EPIC.yaml      an FVR with record_level: epic (features may be embedded under `features:`)
  FEATURE.yaml   optional separate feature FVRs whose record.epic_key matches the epic
  --out          output path (default: driver-tree-<epic_key>.html next to the epic file)
  --standalone   add <!doctype html> and <head> for opening as a local file; omit when publishing
                 as an Artifact (the Artifact tool adds its own skeleton)
  --json         also write the flat value_driver_tree export (nodes with parent ids) for apps
  --refs         folder holding driver-register.csv, kpi-register.csv, benchmark-register.csv
                 (default: ../references next to this script)

Everything on the page comes from the record and the registers; the script never computes value.
Indicative ranges are shown only as written by value_range.py / valor_calc.py into the record.
Prints a JSON summary (gap counts, output path) to stdout.
"""
import argparse, csv, html, json, re, sys
from pathlib import Path

try:
    import yaml
except ImportError:  # JSON records still work without PyYAML
    yaml = None

PILLAR_PLAIN = {"P01": "Grow revenue", "P02": "Run operations at lower cost", "P03": "Stay resilient, compliant and agile",
                "P04": "Build our people", "P05": "Strengthen digital, data and AI", "P06": "Win with partners and the ecosystem"}
CATEGORY = {"CS": "Saves money", "CA": "Avoids a future cost", "CR": "Frees up time", "RV": "Brings in more revenue",
            "MG": "Makes more profit per sale", "WC": "Releases cash (one-off)", "RR": "Reduces risk", "NF": "Tracked in its own units"}
CATEGORY_CODE = {"CS": "Cash saving", "CA": "Cost avoidance", "CR": "Capacity released", "RV": "Incremental revenue",
                 "MG": "Margin improvement", "WC": "Working capital", "RR": "Risk reduction", "NF": "Non-financial"}
TIER = {"T0": "Asserted, not yet checked with data", "T1": "Estimated from real numbers", "T2": "Confirmed by Finance", "T3": "Proven in results"}
MISSING = ("", None, "REQUIRES VALIDATION", "none claimed")
e = lambda x: html.escape("" if x is None else str(x))
LINK_PLAIN = {"intent_linked_to_pillar": "value intent linked to a goal", "drivers_under_epic_pillars": "drivers under the epic's goals",
              "falsifier_stated": "a test that would prove the bet wrong", "contributes_to_epic_hypothesis": "feature linked to the epic's bet",
              "behaviour_change_named": "the change in how people work", "change_owned_by_business_role": "a business owner for the change",
              "business_leading_kpi": "an 'is it being used?' measure", "acceptance_kpi_if_third_party": "an acceptance measure",
              "adoption_risk_addressed": "adoption risk where the value sits", "benefits_counted_once": "each benefit counted once",
              "alternative_uses_resolved": "one use per freed capacity", "freed_capacity_owner_or_not_counted": "freed time converted or left uncounted",
              "value_measure_business_owner": "a business owner for the value measure", "kpis_match_register_or_flagged": "KPIs from the register",
              "units_roll_up": "units that roll up", "baseline_method_comparable": "comparable baselines", "data_source_or_plan": "a data source for each KPI"}


def is_missing(v):
    s = str(v or "").strip().lower()
    return (not s or s.startswith(("requires", "to supply", "to size", "to confirm", "to name", "to define", "not sure", "tbd", "n/a"))
            or s == "none")


def shown(v, default="To supply"):
    s = str(v or "").strip()
    if not s:
        return default
    if s.upper().startswith("REQUIRES VALIDATION"):
        rest = s[len("REQUIRES VALIDATION"):].strip(" —-:")
        return "To supply" + (f" — {rest}" if rest else "")
    return s


def cap(s):
    s = str(s or "")
    return s[:1].upper() + s[1:]


def load(path):
    text = Path(path).read_text(encoding="utf-8")
    if path.endswith(".json") or yaml is None:
        return json.loads(text)
    return yaml.safe_load(text)


def read_csv(p):
    try:
        with open(p, encoding="utf-8", newline="") as f:
            return list(csv.DictReader(f))
    except FileNotFoundError:
        return []


def money(v, cur="AED"):
    v = float(v)
    if abs(v) >= 1e6:
        s = f"{v/1e6:.2f}".rstrip("0").rstrip(".") + "m"
    elif abs(v) >= 1e3:
        s = f"{v/1e3:.0f}k"
    else:
        s = f"{v:.0f}"
    return s


def rng(r, cur="AED", suffix=""):
    if not r or not isinstance(r, (list, tuple)) or len(r) != 2:
        return None
    return f"{cur} {money(r[0])}–{money(r[1])}{suffix}"


def direction(k, kreg):
    c = k.get("contract", {}) or {}
    return str(k.get("direction") or c.get("direction") or kreg.get(k.get("kpi_id"), {}).get("direction") or "").strip()


def kpi_source(k, kreg):
    c = k.get("contract", {}) or {}
    src = k.get("source") or c.get("source")
    if src:
        return src, k.get("register_id") or c.get("register_id") or (k.get("kpi_id") if k.get("kpi_id") in kreg else "")
    if k.get("kpi_id") in kreg:
        return "register", k.get("kpi_id")
    return "new", c.get("analogue") or ""


def export_nodes(t):
    """Flat value_driver_tree for apps that cannot run this script (Track 2). Same content as the page."""
    rec, form, ev, kreg = t["rec"], t["form"], t["ev"], t["kreg"]
    nodes = [{"id": "INT-1", "type": "intent", "label": form.get("value_intent") or "", "parent": "",
              "status": "gap" if is_missing(form.get("value_intent")) else "complete"}]
    owners = {o.get("kpi_id"): o.get("role") or o.get("name") for o in ev.get("kpi_owners", []) or []}
    for i, p in enumerate(t["pillars"]):
        nodes.append({"id": p, "type": "pillar", "label": PILLAR_PLAIN.get(p, p), "parent": "INT-1",
                      "role": "primary" if i == 0 else "secondary", "status": "complete"})
    dids = []
    for k in t["ekpis"]:
        d = k.get("driver") or kreg.get(k.get("kpi_id"), {}).get("driver_id")
        if d and d not in dids:
            dids.append(d)
    for f in t["feats"]:
        if f.get("primary_driver") and f["primary_driver"] not in dids:
            dids.append(f["primary_driver"])
    for d in dids:
        nodes.append({"id": d, "type": "driver", "label": t["drivers"].get(d, {}).get("driver_name", d), "parent": d[:3], "status": "complete"})
    for p in t["pillars"]:
        if not any(d[:3] == p for d in dids):
            nodes.append({"id": f"GAP-{p}", "type": "driver", "label": "No driver yet", "parent": p, "status": "gap",
                          "gap_question": f"Which driver under {p} does this epic move? Value Owner"})
    ben_by_kpi = {}
    for b in t["benefits"]:
        rngv = b.get("indicative_range")
        nodes.append({"id": b.get("id"), "type": "benefit", "label": b.get("description") or "", "parent": b.get("driver") or "",
                      "value": f"{b.get('category', '')} · " + (f"{rngv[0]}–{rngv[1]}" if rngv else (b.get("counting") or "to size")),
                      "status": "complete"})
        ben_by_kpi.setdefault(b.get("linked_kpi"), b.get("id"))
    def kn(k, parent, typ):
        src, rid = kpi_source(k, kreg)
        c = k.get("contract", {}) or {}
        return {"id": k.get("kpi_id"), "type": typ, "label": k.get("name") or "", "parent": parent, "kpi_type": k.get("type") or "",
                "direction": direction(k, kreg), "source": src, "register_id": rid, "benchmark": list(c.get("benchmark_ids", []) or []),
                "today": c.get("baseline_value") or "", "range": c.get("recommended_range") or "", "owner": owners.get(k.get("kpi_id"), ""),
                "link": k.get("link") or c.get("link") or "", "status": "complete"}
    for k in t["ekpis"]:
        d = k.get("driver") or kreg.get(k.get("kpi_id"), {}).get("driver_id") or ""
        nodes.append(kn(k, ben_by_kpi.get(k.get("kpi_id"), d), "lagging_kpi"))
        if not k.get("guardrail") and not any(ct.get("epic_kpi") == k.get("kpi_id") for f in t["feats"] for ct in f.get("contributes_to", []) or []):
            nodes.append({"id": f"GAP-F-{k.get('kpi_id')}", "type": "feature", "label": "No feature moves this outcome", "parent": k.get("kpi_id"),
                          "status": "gap", "gap_question": "Which feature moves this KPI, or should it be dropped? Value Owner"})
    for f in t["feats"]:
        cts = f.get("contributes_to", []) or []
        parent = cts[0].get("epic_kpi") if cts else ""
        nodes.append({"id": f.get("key"), "type": "feature", "label": f.get("name") or "", "parent": parent,
                      "expected_share": cts[0].get("share") if cts else "", "also_moves": [c.get("epic_kpi") for c in cts[1:]],
                      "owner": f.get("change_owner") or "", "status": "gap" if not cts else "complete",
                      **({"gap_question": "Which epic outcome does this feature move, and by what share? Value Owner"} if not cts else {})})
        ks = f.get("kpis", []) or []
        for k in ks:
            typ = "leading_kpi" if k.get("type") == "Business Leading" else "technical_kpi"
            nodes.append(kn(k, f.get("key"), typ))
        if not any(k.get("type") == "Business Leading" for k in ks):
            nodes.append({"id": f"GAP-L-{f.get('key')}", "type": "leading_kpi", "label": "No 'is it being used?' KPI", "parent": f.get("key"),
                          "status": "gap", "gap_question": "How will we see this feature being used each week? Change owner"})
    serious = [g for g in t["gaps"] if g["severity"] in ("Blocker", "Major")]
    return {"complete": not any(n["status"] == "gap" for n in nodes) and not serious, "nodes": nodes,
            "gaps": [{k: g[k] for k in ("severity", "check", "finding", "fix")} for g in t["gaps"]]}


def feature_from_fvr(f):
    rec, form, conv = f.get("record", {}), f.get("formation", {}), f.get("conversion", {}).get("pathway", {})
    sec = []
    for s in form.get("secondary_drivers", []) or []:
        if isinstance(s, dict):
            sec.append(s)
        else:
            parts = str(s).split(" ", 1)
            sec.append({"driver": parts[0], "role": parts[1] if len(parts) > 1 else ""})
    fc = f.get("evago", {}).get("feature_contribution", {}) or {}
    return {"key": rec.get("feature_key"), "name": rec.get("feature_name"), "primary_driver": form.get("primary_driver"),
            "secondary_drivers": sec, "required_operational_change": conv.get("required_operational_change"),
            "change_owner": conv.get("change_owner"), "kpis": f.get("measurement", {}).get("kpis", []),
            "contributes_to": [{"epic_kpi": fc.get("epic_kpi"), "share": fc.get("expected_share")}] if fc.get("epic_kpi") else [],
            "_benefits": f.get("economics", {}).get("benefits", [])}


def build(epic, extra, refs):
    drivers = {d["driver_id"]: d for d in read_csv(refs / "driver-register.csv")}
    kreg = {k["kpi_id"]: k for k in read_csv(refs / "kpi-register.csv")}
    breg = {b["benchmark_id"]: b for b in read_csv(refs / "benchmark-register.csv")}
    rec, ev, form = epic.get("record", {}), epic.get("evago", {}), epic.get("formation", {})
    feats = list(epic.get("features", []) or [])
    benefits = list(epic.get("economics", {}).get("benefits", []) or [])
    for f in extra:
        if f.get("record", {}).get("epic_key") == rec.get("epic_key"):
            ff = feature_from_fvr(f)
            feats.append(ff)
            for b in ff.pop("_benefits"):
                benefits.append(dict(b, feature=ff["key"]))
    ekpis = epic.get("measurement", {}).get("kpis", []) or []
    ekpi_ids = {k.get("kpi_id") for k in ekpis}
    pillars = [form.get("primary_pillar")] + list(form.get("secondary_pillars", []) or [])
    pillars = [p for p in pillars if p]
    gaps = []

    def gap(sev, check, finding, fix, src="auto"):
        gaps.append({"severity": sev, "check": check, "finding": finding, "fix": fix, "src": src})

    def dname(did):
        return drivers.get(did, {}).get("driver_name", "")

    def bench_check(kid, kname, c):
        """C31 unknown benchmark; C34 an absolute % range that starts above every cited peer level."""
        rows = []
        for bid in c.get("benchmark_ids", []) or []:
            if bid not in breg:
                gap("Major", "C31", f"{kid} cites {bid}, which is not in the benchmark register.", "Remove it or add it through the register's verified update.")
            else:
                rows.append(breg[bid])
        rr = str(c.get("recommended_range") or "")
        m = re.match(r"\s*(?:keep\s+)?(\d+(?:\.\d+)?)\s*(?:[–-]\s*(\d+(?:\.\d+)?))?\s*%", rr)
        if not m or "baseline" in rr.lower() or "below" in rr.lower() or c.get("beyond_peer_reason"):
            return
        peers = []
        for r in rows:
            try:
                if r.get("benchmark_type") == "peer_level" and r.get("unit", "").strip() == "%":
                    peers.append((float(r.get("value_high") or r.get("value_low")), r))
            except ValueError:
                pass
        if not peers:
            return
        top, r = max(peers, key=lambda x: x[0])
        if float(m.group(1)) > top:
            fit = (r.get("notes") or "").strip()
            gap("Major", "C34", f"{kid} {kname}: recommended range starts at {m.group(1)}%, above the cited peer level of {top:g}% "
                f"({r.get('benchmark_id')}, {r.get('sector')}).",
                "State why AG can beat peers (beyond_peer_reason), lower the range, or drop the benchmark if it doesn't fit"
                + (f" — register note: {fit}" if fit else "") + ".")

    if is_missing(form.get("value_intent")):
        gap("Major", "Strategic", "The epic has no value intent.", "Write one sentence: what this is for, in business terms.")
    if not pillars:
        gap("Major", "Strategic", "No primary pillar on the epic.", "Set formation.primary_pillar (P01–P06).")
    if is_missing((form.get("hypothesis") or {}).get("falsifier")):
        gap("Major", "Strategic", "The hypothesis has no falsifier.", "Add 'We'll know we're wrong if…'.")
    vo = (ev.get("value_owner") or {})
    owners = ev.get("kpi_owners", []) or []
    for o in owners:
        if vo.get("role") and o.get("role") == vo.get("role") or (vo.get("name") not in MISSING and o.get("name") == vo.get("name")):
            gap("Blocker", "C37", f"The Value Owner also owns {o.get('kpi_id')}.", "Name a different KPI Owner.")
    for k in ekpis:
        kid = k.get("kpi_id")
        if k.get("type") not in ("Business Lagging",) and not k.get("guardrail"):
            gap("Minor", "EVAGO §15", f"Epic KPI {kid} is {k.get('type')}; epics carry Business Lagging KPIs.", "Move it to the feature that drives it.")
        d = k.get("driver") or kreg.get(kid, {}).get("driver_id")
        if not d:
            gap("Major", "Data", f"Epic KPI {kid} has no driver, so it can't sit in the tree.", "Add `driver` from the driver register.")
        elif d not in drivers:
            gap("Blocker", "C17", f"Epic KPI {kid} names driver {d}, which is not in the register.", "Use a register driver ID.")
        c = k.get("contract", {}) or {}
        if is_missing(c.get("baseline_value")):
            gap("Minor", "C13", f"{kid} {k.get('name')} has no baseline yet.", "KPI Owner supplies trailing 12 months.")
        bench_check(kid, k.get("name"), c)
        if not any(kid == ct.get("epic_kpi") for f in feats for ct in f.get("contributes_to", []) or []) and not k.get("guardrail"):
            gap("Major", "Coherence", f"No feature moves epic KPI {kid}.", "Link a feature with contributes_to, or drop the KPI.")
    for f in feats:
        fk = f.get("key")
        allds = [f.get("primary_driver")] + [s.get("driver") for s in f.get("secondary_drivers", []) or []]
        for d in allds:
            if not d:
                gap("Major", "Strategic", f"{fk} has no primary driver.", "Pick one primary driver from the register.")
            elif d not in drivers:
                gap("Blocker", "C17", f"{fk} names driver {d}, which is not in the register.", "Use a register driver ID.")
            elif pillars and d[:3] not in pillars:
                gap("Major", "C16", f"{fk} driver {d} sits under {d[:3]}, outside the epic's pillars ({', '.join(pillars)}).", "Change the driver, or add the pillar to the epic.")
        if is_missing(f.get("change_owner")):
            gap("Blocker", "C02", f"{fk} names no owner for the change.", "Name the business role that makes the change happen.")
        if is_missing(f.get("required_operational_change")):
            gap("Blocker", "C02", f"{fk} doesn't say what has to work differently.", "Name who does what differently.")
        for k in f.get("kpis", []) or []:
            bench_check(k.get("kpi_id"), k.get("name"), k.get("contract", {}) or {})
        fk_types = [k.get("type") for k in f.get("kpis", []) or []]
        if "Business Leading" not in fk_types:
            gap("Major", "EVAGO §15", f"{fk} has no 'is it being used?' KPI.", "Add one Business Leading KPI.")
        if "Business Lagging" in fk_types:
            gap("Major", "EVAGO §15", f"{fk} carries a Business Lagging KPI; outcome KPIs belong to the epic.", "Move it to the epic or link to an epic KPI.")
        for ct in f.get("contributes_to", []) or []:
            if ct.get("epic_kpi") not in ekpi_ids:
                gap("Major", "Coherence", f"{fk} contributes to {ct.get('epic_kpi')}, which the epic doesn't carry.", "Use an epic KPI, or take it to the Value Owner.")
        if not f.get("contributes_to"):
            gap("Major", "Coherence", f"{fk} doesn't say which epic outcome it moves.", "Add contributes_to with a share range.")
        pd = f.get("primary_driver")
        kd = {k.get("kpi_id"): (k.get("driver") or kreg.get(k.get("kpi_id"), {}).get("driver_id")) for k in ekpis}
        lands = [kd.get(ct.get("epic_kpi")) for ct in f.get("contributes_to", []) or [] if kd.get(ct.get("epic_kpi"))]
        own_b = [b for b in benefits if b.get("feature") == fk]
        if pd and lands and pd not in lands and not any(b.get("driver") == pd for b in own_b):
            gap("Major", "C16", f"{fk}'s primary driver {pd} ({dname(pd)}) carries none of its value; the outcome it moves sits under "
                f"{', '.join(sorted(set(lands)))}.", f"Make {lands[0]} the primary driver and keep {pd} as secondary with its role.")
    # v1.3: every pillar carries a driver; feature shares can sum to 100%; KPI directions match the measure
    used = {(k.get("driver") or kreg.get(k.get("kpi_id"), {}).get("driver_id") or "")[:3] for k in ekpis}
    used |= {str(d or "")[:3] for f in feats for d in [f.get("primary_driver")] + [s.get("driver") for s in f.get("secondary_drivers", []) or []]}
    for p in pillars[1:]:
        if p not in used:
            gap("Major", "Tree", f"Secondary pillar {p} has no driver under it.", "Drop the pillar, or name the driver and the KPI it moves.")
    for k in ekpis:
        lows = []
        for f in feats:
            for ct in f.get("contributes_to", []) or []:
                m = re.match(r"\s*(\d+(?:\.\d+)?)", str(ct.get("share") or ""))
                if ct.get("epic_kpi") == k.get("kpi_id") and m:
                    lows.append(float(m.group(1)))
        if sum(lows) > 100:
            gap("Major", "Tree", f"Feature shares of {k.get('kpi_id')} start at {sum(lows):g}% in total.", "Lower the shares so their lower bounds total 100% or less.")
    for f in feats:
        lead = [k for k in f.get("kpis", []) or [] if k.get("type") == "Business Leading"]
        if len(lead) > 3:
            gap("Minor", "EVAGO §15", f"{f.get('key')} carries {len(lead)} Business Leading KPIs.", "Keep the one to three that teams steer by.")
    for k in ekpis + [k for f in feats for k in f.get("kpis", []) or []]:
        dr = direction(k, kreg)
        nm = str(k.get("name") or "").lower()
        if not dr:
            gap("Minor", "Direction", f"{k.get('kpi_id')} {k.get('name')} has no direction.", "Add Higher is better or Lower is better (register first).")
        elif dr.startswith("Lower") and re.search(r"(completion|compliance|adoption|accuracy|coverage|same-day|on[- ]time|first[- ]time)", nm):
            gap("Major", "Direction", f"{k.get('kpi_id')} {k.get('name')} is marked Lower is better.", "Rates of completion, compliance, adoption or accuracy are Higher is better.")
    all_kpis = ekpi_ids | {k.get("kpi_id") for f in feats for k in f.get("kpis", []) or []}
    for b in benefits:
        if b.get("linked_kpi") not in all_kpis:
            gap("Major", "C38", f"Benefit {b.get('id')} links to {b.get('linked_kpi')}, which isn't in the record.", "Link it to a KPI in the record.")
        if b.get("category") == "CR" and str(b.get("counting", "")).startswith("Counted"):
            gap("Blocker", "C03", f"Benefit {b.get('id')} counts freed time as money without conversion.", "Name the conversion mechanism and owner, or don't count it.")
    for fnd in (epic.get("challenge", {}) or {}).get("findings", []) or []:
        if not fnd.get("resolved"):
            gap(str(fnd.get("severity", "")).capitalize() or "Major", fnd.get("check", ""), fnd.get("finding", ""), fnd.get("fix", ""), src="challenge")
    order = {"Blocker": 0, "Major": 1, "Minor": 2}
    # severity first; at the same severity the challenge findings (business risks) lead the automatic link checks
    gaps.sort(key=lambda g: (order.get(g["severity"], 3), 0 if g["src"] == "challenge" else 1))
    return dict(rec=rec, ev=ev, form=form, feats=feats, benefits=benefits, ekpis=ekpis, pillars=pillars,
                drivers=drivers, kreg=kreg, breg=breg, gaps=gaps, epic=epic)


def bench_line(ids, breg):
    out = []
    for bid in ids or []:
        b = breg.get(bid)
        if not b:
            continue
        y = b.get("year", "")[:4]
        dated = ", dated" if y.isdigit() and int(y) < 2021 else (", undated" if not y.isdigit() else "")
        vc = "vendor-reported, " if b.get("quality") == "C" else ""
        kind = "Peers" if b.get("benchmark_type") == "peer_level" else "Typical"
        val = b["value_low"] if b["value_low"] == b["value_high"] else f"{b['value_low']}–{b['value_high']}"
        org = b.get("source_org", "").split(" (")[0]
        out.append(f"{kind}: {b.get('statistic')} ({val} {b.get('unit')}) · {vc}{org}, {y or 'n.d.'}, {b.get('quality')}{dated}")
    return out


CSS = """
:root{
  /* Layout: a left-to-right value chain (intent → pillar → lever → outcome → value) that stacks top-down on phones */
  --ground:#F4F7F8; --surface:#FFFFFF; --ink:#14222B; --muted:#5A6A75; --rule:#D5DDE2; --soft:#EAF0F3;
  --lapis:#1D4F91; --lapis-soft:#E3ECF8; --brass:#7E5A10; --brass-soft:#F5EEDD;
  --good:#1D7349; --good-soft:#E2F2E9; --warn:#8F5C00; --warn-soft:#FBF0DA; --crit:#AE2A20; --crit-soft:#FBE5E2;
  --f-sans:"IBM Plex Sans",system-ui,-apple-system,"Segoe UI",sans-serif;
  --f-cond:"IBM Plex Sans Condensed","Arial Narrow",system-ui,sans-serif;
  --f-mono:"IBM Plex Mono",ui-monospace,"SFMono-Regular",Menlo,monospace;
}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){
  --ground:#0E151A; --surface:#162027; --ink:#E4ECF0; --muted:#93A4AF; --rule:#2A3841; --soft:#1C2830;
  --lapis:#91B5EC; --lapis-soft:#1B2B42; --brass:#D8B36A; --brass-soft:#2E2617;
  --good:#6CC59A; --good-soft:#15291F; --warn:#E2B04C; --warn-soft:#2D2412; --crit:#EF8A80; --crit-soft:#331A18; color-scheme:dark}}
:root[data-theme="dark"]{
  --ground:#0E151A; --surface:#162027; --ink:#E4ECF0; --muted:#93A4AF; --rule:#2A3841; --soft:#1C2830;
  --lapis:#91B5EC; --lapis-soft:#1B2B42; --brass:#D8B36A; --brass-soft:#2E2617;
  --good:#6CC59A; --good-soft:#15291F; --warn:#E2B04C; --warn-soft:#2D2412; --crit:#EF8A80; --crit-soft:#331A18; color-scheme:dark}
[hidden]{display:none!important}
body{background:var(--ground);color:var(--ink);font:15px/1.5 var(--f-sans)}
.wrap{max-width:1240px;margin:0 auto;padding-block:28px 48px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));display:flex;flex-direction:column;gap:22px}
.eyebrow,.lbl{font:600 11.5px/1.3 var(--f-cond);letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
h1{font:600 clamp(24px,4vw,34px)/1.15 var(--f-sans);margin:4px 0 6px;text-wrap:balance;letter-spacing:-.01em}
h2{font:600 17px/1.3 var(--f-sans);margin:0;text-wrap:balance}
.intent{max-width:72ch;color:var(--ink);margin:0}
.code{font:500 12px/1.3 var(--f-mono);color:var(--muted)}
.num{font-family:var(--f-mono);font-variant-numeric:tabular-nums}
.summary{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:10px}
.stat{background:var(--surface);border:1px solid var(--rule);border-radius:8px;padding:12px 14px;display:flex;flex-direction:column;gap:4px;min-width:0}
.stat .v{font-weight:600}
.stat.value .v{color:var(--brass)}
.stat.risk{grid-column:1 / -1} .stat.risk .v{font-weight:600}

.tabs{display:flex;gap:4px;border-bottom:1px solid var(--rule);flex-wrap:wrap}
.tab{font:600 14px var(--f-sans);color:var(--muted);background:none;border:0;border-bottom:2px solid transparent;padding:10px 14px;cursor:pointer}
.tab[aria-selected="true"]{color:var(--lapis);border-bottom-color:var(--lapis)}
.tab:focus-visible{outline:2px solid var(--lapis);outline-offset:2px}
.count{font:600 11px var(--f-mono);background:var(--crit-soft);color:var(--crit);border-radius:10px;padding:1px 7px;margin-left:6px}
.chain-head{display:grid;grid-template-columns:minmax(150px,1fr) minmax(170px,1.2fr) minmax(240px,2fr) minmax(190px,1.3fr)}
.chain-row{display:grid;grid-template-columns:minmax(150px,1fr) minmax(0,4.5fr)}
.levers{display:flex;flex-direction:column;border-left:1px solid var(--rule)}
.lever-line{display:grid;grid-template-columns:minmax(170px,1.2fr) minmax(240px,2fr) minmax(190px,1.3fr)}
.lever-line+.lever-line{border-top:1px solid var(--rule)}
.chain-head>div{padding:0 14px 8px}
.chain-row{background:var(--surface);border:1px solid var(--rule);border-radius:10px;overflow:hidden}
.cell{padding:14px;display:flex;flex-direction:column;gap:8px;min-width:0;position:relative}
.cell+.cell{border-left:1px solid var(--rule)}
.cell+.cell::before{content:"";position:absolute;left:-6px;top:22px;width:10px;height:10px;background:var(--surface);border-top:1px solid var(--rule);border-right:1px solid var(--rule);transform:rotate(45deg)}
.pillar{background:var(--lapis-soft)}
.pillar h3{font:600 16px/1.3 var(--f-sans);margin:0;color:var(--lapis)}
.node{display:flex;flex-direction:column;gap:2px}
.node .t{font-weight:600}
.kpi{border:1px solid var(--rule);border-radius:7px;padding:9px 10px;display:flex;flex-direction:column;gap:4px;background:var(--surface)}
.kv{display:grid;grid-template-columns:auto 1fr;gap:2px 10px;font-size:13px}
.kv dt{color:var(--muted)} .kv dd{margin:0;min-width:0}
.peer{font-size:12.5px;color:var(--muted)}
.ben{display:flex;flex-direction:column;gap:2px;padding:8px 10px;border-radius:7px;background:var(--brass-soft)}
.ben .amt{color:var(--brass);font-weight:600}
.chip{display:inline-flex;align-items:center;gap:6px;font:600 11.5px/1 var(--f-cond);letter-spacing:.04em;text-transform:uppercase;border-radius:20px;padding:4px 9px;width:fit-content}
.chip.good{background:var(--good-soft);color:var(--good)} .chip.warn{background:var(--warn-soft);color:var(--warn)} .chip.crit{background:var(--crit-soft);color:var(--crit)} .chip.info{background:var(--soft);color:var(--muted)}
.rows{display:flex;flex-direction:column;gap:12px}
.lane{background:var(--surface);border:1px solid var(--rule);border-radius:10px;display:flex;flex-direction:column}
.lane-h{padding:14px 16px;border-bottom:1px solid var(--rule);display:flex;flex-wrap:wrap;gap:6px 14px;align-items:baseline}
.lane-b{display:grid;grid-template-columns:repeat(5,minmax(0,1fr))}
.lane-b .cell{padding:12px 14px}
.tblwrap{overflow-x:auto;background:var(--surface);border:1px solid var(--rule);border-radius:10px}
table{border-collapse:collapse;width:100%;font-size:13.5px;min-width:760px}
th,td{text-align:left;vertical-align:top;padding:10px 12px;border-bottom:1px solid var(--rule)}
th{font:600 11.5px var(--f-cond);letter-spacing:.06em;text-transform:uppercase;color:var(--muted);background:var(--soft)}
tr:last-child td{border-bottom:0}
.banner{margin:10px 0 0;padding:8px 12px;border-radius:7px;background:var(--warn-soft);color:var(--warn);font-weight:600;font-size:13.5px;width:fit-content}
.note{font-size:13px;color:var(--muted);max-width:90ch;margin:0}
.sev{font:600 11.5px var(--f-cond);text-transform:uppercase;letter-spacing:.05em}
.sev.Blocker{color:var(--crit)} .sev.Major{color:var(--warn)} .sev.Minor{color:var(--muted)}
.hyp{background:var(--surface);border:1px solid var(--rule);border-radius:10px;padding:14px 16px;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:16px}
.hyp p{margin:4px 0 0}
@media (max-width:900px){
  .chain-head{display:none}
  .chain-row,.lane-b,.lever-line{grid-template-columns:1fr}
  .levers{border-left:0;border-top:1px solid var(--rule)}
  .cell+.cell{border-left:0;border-top:1px solid var(--rule)}
  .cell+.cell::before{left:22px;top:-6px;transform:rotate(135deg)}
  .hyp{grid-template-columns:1fr}
}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}
"""

JS = """
(function(){
  const tabs=[...document.querySelectorAll('.tab')], panels=[...document.querySelectorAll('[role=tabpanel]')];
  function show(id){tabs.forEach(t=>t.setAttribute('aria-selected',String(t.dataset.p===id)));panels.forEach(p=>p.hidden=p.id!=='panel-'+id);
    try{localStorage.setItem('valor-tree-tab',id)}catch(e){}}
  tabs.forEach(t=>t.addEventListener('click',()=>show(t.dataset.p)));
  const h=(location.hash||'').slice(1); let saved=null; try{saved=localStorage.getItem('valor-tree-tab')}catch(e){}
  show(['executive','detailed','gaps'].includes(h)?h:(['executive','detailed','gaps'].includes(saved)?saved:'executive'));
})();
"""


def render(t):
    rec, ev, form, feats, benefits, ekpis = t["rec"], t["ev"], t["form"], t["feats"], t["benefits"], t["ekpis"]
    drivers, kreg, breg = t["drivers"], t["kreg"], t["breg"]
    sc = dict((t["epic"].get("challenge", {}) or {}).get("scores", {}) or {})
    # accept score.py output or a hand-written flat shape (coherence: 92, confidence: 15)
    for key, inner in (("coherence", "headline"), ("confidence", "score")):
        if not isinstance(sc.get(key), dict):
            sc[key] = {inner: sc[key]} if sc.get(key) is not None else {}
    if isinstance(sc.get("weakest_link"), str):
        sc["coherence"].setdefault("weakest_link", sc["weakest_link"])
    if not isinstance(sc.get("verdict"), dict):
        sc["verdict"] = {"display": sc["verdict"]} if sc.get("verdict") else {}
    cur = rec.get("currency") or (t["epic"].get("economics", {}) or {}).get("currency") or "AED"
    name = rec.get("epic_name") or rec.get("feature_name") or "Value record"
    res = (t["epic"].get("economics", {}) or {}).get("results", {}) or {}
    eo = (ev.get("expected_financial_outcome") or {}).get("range")
    if not is_missing(eo) and str(eo).strip().lower() != "none claimed":
        value_size, value_note = eo, "Value Owner's range, projected"
    elif isinstance(res.get("counted_annual_value"), list):
        value_size, value_note = rng(res["counted_annual_value"], cur, " a year"), "Indicative · to validate with Finance"
    elif str(eo).strip().lower() == "none claimed":
        value_size, value_note = "None claimed", "No financial outcome claimed; value tracked in its own units"
    else:
        value_size, value_note = "To size", "Value Owner to supply"
    verdict = (sc.get("verdict") or {}).get("display") or ("Shaping — no verdict before Commit" if rec.get("lifecycle_stage", "shape") == "shape" else "Not scored")
    conf = sc.get("confidence") or {}
    coh = sc.get("coherence") or {}
    tier = rec.get("evidence_tier", "T0")
    nb = len([g for g in t["gaps"] if g["severity"] == "Blocker"])

    def kpi_card(k, exec_view=True):
        c = k.get("contract", {}) or {}
        today = shown(c.get("baseline_value"))
        rngtxt = c.get("recommended_range") or kreg.get(k.get("kpi_id"), {}).get("suggested_target_range") or "to set"
        basis = c.get("range_basis") or "suggested"
        peers = bench_line(c.get("benchmark_ids"), breg)
        g = " · watch-out" if k.get("guardrail") else ""
        code = "" if exec_view else f'<span class="code">{e(k.get("kpi_id"))}</span>'
        peer_html = "".join(f'<div class="peer">{e(p)}</div>' for p in (peers[:1] if exec_view else peers))
        if exec_view and not peers:
            peer_html = '<div class="peer">No peer benchmark in the register</div>'
        return (f'<div class="kpi"><div class="node"><span class="t">{e(k.get("name"))}{e(g)}</span>{code}</div>'
                f'<dl class="kv"><dt>Today</dt><dd>{e(today)}</dd><dt>Range</dt><dd>{e(rngtxt)} <span class="code">({e(basis)})</span></dd></dl>{peer_html}</div>')

    def ben_card(b, exec_view=True):
        cat = b.get("category", "")
        r = rng(b.get("indicative_range"), cur, " a year" if cat != "WC" else " one-off")
        counting = b.get("counting") or ("To confirm" if not r else "")
        short, _, why = str(counting).partition(" (")
        why = why.rstrip(")")
        amt = f'<span class="amt num">{e(r)}</span>' if r else '<span class="amt">To size</span>'
        label = CATEGORY.get(cat, cat) if exec_view else f"{cat} – {CATEGORY_CODE.get(cat, cat)}"
        cls = "good" if str(counting).startswith("Counted") else ("info" if "Tracked" in str(counting) or "separately" in str(counting) else "warn")
        src = ""
        if not exec_view and b.get("inputs"):
            def fmt(k, v):
                val = v.get("value")
                if k == "improvement" and isinstance(val, list) and len(val) == 2:
                    val = f"{val[0]*100:g}–{val[1]*100:g}%"
                elif isinstance(val, (int, float)):
                    val = f"{val:,g}"
                if is_missing(val):
                    val = shown(val)
                return f"{cap(k.replace('_', ' '))}: {val} {v.get('unit', '')} ({shown(v.get('source', ''), '')})".replace(" ()", "").replace("  ", " ")
            parts = [fmt(k, v) for k, v in b["inputs"].items() if isinstance(v, dict)]
            src = "".join(f'<div class="peer">{e(p)}</div>' for p in parts)
        bid = "" if exec_view else f'<span class="code">{e(b.get("id"))} · {e(b.get("feature") or "whole epic")}</span>'
        return (f'<div class="ben">{bid}<span class="t">{e(b.get("description"))}</span><span class="lbl">{e(label)}</span>{amt}'
                f'<span class="chip {cls}">{e(short)}</span>{f"<span class=peer>{e(cap(why))}</span>" if why else ""}{src}</div>')

    # ---------- executive ----------
    rows = []

    def kpi_driver(k):
        return k.get("driver") or kreg.get(k.get("kpi_id"), {}).get("driver_id", "")

    for p in t["pillars"]:
        ds = []
        for f in feats:  # primary drivers first, then secondary, then KPI-only drivers
            d = f.get("primary_driver")
            if d and d.startswith(p) and d not in ds:
                ds.append(d)
        for f in feats:
            for sd in f.get("secondary_drivers", []) or []:
                d = sd.get("driver")
                if d and d.startswith(p) and d not in ds:
                    ds.append(d)
        for k in ekpis:
            d = kpi_driver(k)
            if d and d.startswith(p) and d not in ds:
                ds.append(d)
        for b in benefits:
            d = str(b.get("driver", ""))
            if d.startswith(p) and d not in ds:
                ds.append(d)
        lines = []
        for d in ds:
            via = [f"{f.get('key')}{' (suggested)' if f.get('provisional') else ''}" for f in feats if f.get("primary_driver") == d]
            roles = [(f.get("key"), sd.get("role")) for f in feats for sd in f.get("secondary_drivers", []) or [] if sd.get("driver") == d]
            ks = [k for k in ekpis if kpi_driver(k) == d]
            bs = [b for b in benefits if b.get("driver") == d]
            sub = (f'<span class="peer">Delivered by {e(", ".join(via))}</span>' if via else "") + \
                  "".join(f'<span class="peer">Also via {e(fk)}: {e(r)}</span>' for fk, r in roles)
            if ks:
                out_html = "".join(kpi_card(k) for k in ks)
            else:
                out_html = '<span class="peer">Supports the outcomes above; no outcome KPI of its own</span>'
            ben_html = "".join(ben_card(b) for b in bs) or '<span class="peer">No benefit claimed on this lever</span>'
            lines.append(f'<div class="lever-line"><div class="cell"><div class="node"><span class="t">{e(drivers.get(d, {}).get("driver_name", d))}</span>{sub}</div></div>'
                         f'<div class="cell">{out_html}</div><div class="cell">{ben_html}</div></div>')
        primary = " · primary" if p == form.get("primary_pillar") else ""
        body_lines = "".join(lines) or '<div class="lever-line"><div class="cell"><span class="peer">No lever mapped</span></div><div class="cell"></div><div class="cell"></div></div>'
        rows.append(f'<div class="chain-row"><div class="cell pillar"><span class="lbl">Pillar{e(primary)}</span><h3>{e(PILLAR_PLAIN.get(p, p))}</h3></div>'
                    f'<div class="levers">{body_lines}</div></div>')
    hyp = form.get("hypothesis") or {}
    xline = ((t["epic"].get("benchmarks") or {}).get("executive_line") or "")
    exec_html = ((f'<p class="note"><b>Against peers:</b> {e(xline)}</p>' if xline else "") + f'<div class="hyp"><div><span class="lbl">Our bet</span><p>{e(hyp.get("text"))}</p></div>'
                 f'<div><span class="lbl">We are wrong if</span><p>{e(hyp.get("falsifier"))}</p></div></div>'
                 '<div class="chain-head"><div class="lbl">Strategic goal</div><div class="lbl">Lever</div><div class="lbl">Outcome we measure</div><div class="lbl">Value</div></div>'
                 f'<div class="rows">{"".join(rows)}</div>'
                 f'<p class="note">{e(res.get("label", ""))} Freed time counts as money only when someone stops paying for something. Peer figures are context, not targets.</p>')

    # ---------- detailed ----------
    owners = {o.get("kpi_id"): o.get("role") or o.get("name") for o in ev.get("kpi_owners", []) or []}
    trs = []
    for k in ekpis:
        c = k.get("contract", {}) or {}
        d = k.get("driver") or kreg.get(k.get("kpi_id"), {}).get("driver_id", "")
        linked = ", ".join(f.get("key") for f in feats if any(ct.get("epic_kpi") == k.get("kpi_id") for ct in f.get("contributes_to", []) or [])) or "—"
        peers = "<br>".join(e(p) for p in bench_line(c.get("benchmark_ids"), breg)) or "None in register"
        today = shown(c.get("baseline_value"))
        trs.append(f'<tr><td><b>{e(k.get("name"))}</b><div class="code">{e(k.get("kpi_id"))}{" · watch-out" if k.get("guardrail") else ""}</div></td>'
                   f'<td>{e(k.get("type"))}</td><td><span class="code">{e(d)}</span><div>{e(drivers.get(d, {}).get("driver_name", ""))}</div></td>'
                   f'<td>{e(today)}</td><td class="peer">{peers}</td><td>{e(c.get("recommended_range") or "to set")}<div class="code">{e(c.get("range_basis") or "suggested")}</div></td>'
                   f'<td>{e(owners.get(k.get("kpi_id")) or c.get("outcome_owner") or "to name")}</td><td class="code">{e(linked)}</td></tr>')
    table = ('<div class="tblwrap"><table><thead><tr><th>Epic outcome KPI</th><th>Type</th><th>Driver</th><th>Today</th><th>Benchmark</th><th>Recommended range</th><th>KPI Owner</th><th>Moved by</th></tr></thead>'
             f'<tbody>{"".join(trs)}</tbody></table></div>')
    lanes = []
    for f in feats:
        drs = [(f.get("primary_driver"), "Primary", "")] + [(s.get("driver"), "Secondary", s.get("role", "")) for s in f.get("secondary_drivers", []) or []]
        dhtml = "".join(f'<div class="node"><span class="code">{e(d)} · {e(kind)}</span><span class="t">{e(drivers.get(d, {}).get("driver_name", "not in register"))}</span>'
                        f'{f"<span class=peer>{e(role)}</span>" if role else ""}</div>' for d, kind, role in drs if d)
        khtml = "".join(kpi_card(k, exec_view=False) for k in f.get("kpis", []) or []) or '<span class="peer">No feature KPI</span>'
        chtml = "".join(f'<div class="node"><span class="t">{e(next((k.get("name") for k in ekpis if k.get("kpi_id") == ct.get("epic_kpi")), ct.get("epic_kpi")))}</span>'
                        f'<span class="code">{e(ct.get("epic_kpi"))}</span><span class="peer">Share: {e(ct.get("share") or "to confirm")}</span></div>' for ct in f.get("contributes_to", []) or []) or '<span class="peer">Not linked</span>'
        bhtml = "".join(ben_card(b, exec_view=False) for b in benefits if b.get("feature") == f.get("key")) or '<span class="peer">No benefit claimed</span>'
        lanes.append(f'<div class="lane"><div class="lane-h"><span class="code">{e(f.get("key"))}</span><h2>{e(f.get("name"))}{" (suggested)" if f.get("provisional") else ""}</h2></div><div class="lane-b">'
                     f'<div class="cell"><span class="lbl">What has to work differently</span><span>{e(shown(f.get("required_operational_change"), "To define"))}</span>'
                     f'<span class="lbl">Makes it happen</span><span class="t">{e(shown(f.get("change_owner"), "To name"))}</span></div>'
                     f'<div class="cell"><span class="lbl">Value drivers</span>{dhtml}</div>'
                     f'<div class="cell"><span class="lbl">Feature KPIs</span>{khtml}</div>'
                     f'<div class="cell"><span class="lbl">Moves epic outcome</span>{chtml}</div>'
                     f'<div class="cell"><span class="lbl">Benefits</span>{bhtml}</div></div></div>')
    unlinked = [b for b in benefits if not b.get("feature")]
    extra_b = ("<h2>Epic-level benefits</h2><div class=\"rows\">" + "".join(ben_card(b, False) for b in unlinked) + "</div>") if unlinked else ""
    detail_html = (f'<h2>Epic outcomes</h2>{table}<h2>Features</h2><div class="rows">{"".join(lanes)}</div>{extra_b}'
                   f'<p class="note">Coherence {e(coh.get("headline", "–"))}% (weakest: {e(coh.get("weakest_strand", "–"))} — {e(LINK_PLAIN.get(coh.get("weakest_link"), coh.get("weakest_link") or "none"))}). '
                   'How completely the chain from intent to value holds together; it shows the case is well-formed, not how big or proven the value is.</p>')

    # ---------- gaps ----------
    if t["gaps"]:
        grows = "".join(f'<tr><td><span class="sev {e(g["severity"])}">{e(g["severity"])}</span></td><td class="code">{e(g["check"])}</td><td>{e(g["finding"])}</td><td>{e(g["fix"])}</td></tr>' for g in t["gaps"])
        gaps_html = ('<p class="note">Checked automatically against the VALOR rules while drawing the tree. Blockers stop the record being called ready.</p>'
                     f'<div class="tblwrap"><table><thead><tr><th>Severity</th><th>Check</th><th>Finding</th><th>Fix</th></tr></thead><tbody>{grows}</tbody></table></div>')
    else:
        gaps_html = '<p class="note">No gaps found in the tree\'s links.</p>'

    gap_count = f'<span class="count">{len(t["gaps"])}</span>' if t["gaps"] else ""
    top = t["gaps"][0] if t["gaps"] else None
    if top and top["severity"] in ("Blocker", "Major"):
        risk_text, risk_note = top["finding"], f'{top["severity"]} · fix: {top["fix"]}'
    else:
        risk_text, risk_note = "No blockers or major gaps found", "See the Gaps view for minor items"
    vclass = "crit" if nb else ("warn" if verdict.startswith(("Shaping", "Not yet", "Prove", "Fix", "Redesign")) else "good")
    head = (f'<title>{e(name)} Driver Tree</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n'
            '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
            '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@500&family=IBM+Plex+Sans+Condensed:wght@600&family=IBM+Plex+Sans:wght@400;600&display=swap">\n'
            f'<style>{CSS}</style>\n')
    body = (f'<div class="wrap"><header><div class="eyebrow">{e(" · ".join(x for x in ["VALOR value driver tree", rec.get("business_unit"), rec.get("epic_key") or rec.get("feature_key")] if x and not is_missing(x)))}</div>'
            f'<h1>{e(name)}</h1><p class="intent">{e(form.get("value_intent"))}</p>'
            f'{"<p class=banner>Worked example: value figures are illustrative, not client data.</p>" if rec.get("example") else ""}</header>'
            '<section class="summary" aria-label="Summary">'
            f'<div class="stat"><span class="lbl">Where it stands</span><span class="chip {vclass}">{e(verdict.split(" — ")[0])}</span>'
            f'{f"<span class=peer>{e(cap(verdict.split(chr(8212),1)[1].strip()))}</span>" if " — " in verdict else ""}</div>'
            f'<div class="stat value"><span class="lbl">Value size</span><span class="v num">{e(value_size)}</span><span class="peer">{e(value_note)}</span></div>'
            f'<div class="stat"><span class="lbl">Confidence</span><span class="v">{e(conf.get("label", "–"))} · <span class="num">{e(conf.get("score", "–"))}/100</span></span>'
            f'<span class="peer">{e((conf.get("next_best_step") or {}).get("step", ""))}</span></div>'
            f'<div class="stat"><span class="lbl">Evidence</span><span class="v">{e(TIER.get(tier, tier))}</span><span class="peer">Stage: {e(str(rec.get("lifecycle_stage", "shape")).capitalize())}</span></div>'
            f'<div class="stat"><span class="lbl">Value Owner</span><span class="v">{e((ev.get("value_owner") or {}).get("role") or "To name")}</span>'
            f'<span class="peer">{len(feats)} features · {len([k for k in ekpis if not k.get("guardrail")])} outcome KPIs'
            f'{" · " + str(len([k for k in ekpis if k.get("guardrail")])) + " watch-out" if any(k.get("guardrail") for k in ekpis) else ""}</span></div>'
            f'<div class="stat risk"><span class="lbl">Biggest risk</span><span class="v">{e(risk_text)}</span>'
            f'<span class="peer">{e(risk_note)}</span></div></section>'
            '<nav class="tabs" role="tablist" aria-label="Views">'
            '<button class="tab" role="tab" data-p="executive" id="t-exec">Executive</button>'
            '<button class="tab" role="tab" data-p="detailed" id="t-det">Detailed</button>'
            f'<button class="tab" role="tab" data-p="gaps" id="t-gaps">Gaps{gap_count}</button></nav>'
            f'<section id="panel-executive" role="tabpanel" aria-labelledby="t-exec" class="rows">{exec_html}</section>'
            f'<section id="panel-detailed" role="tabpanel" aria-labelledby="t-det" class="rows" hidden>{detail_html}</section>'
            f'<section id="panel-gaps" role="tabpanel" aria-labelledby="t-gaps" class="rows" hidden>{gaps_html}</section>'
            f'</div><script>{JS}</script>')
    return head + body


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("epic")
    ap.add_argument("features", nargs="*")
    ap.add_argument("--out")
    ap.add_argument("--standalone", action="store_true")
    ap.add_argument("--refs")
    ap.add_argument("--json", help="also write the flat value_driver_tree (for apps) to this path")
    a = ap.parse_args()
    refs = Path(a.refs) if a.refs else Path(__file__).resolve().parent.parent / "references"
    epic = load(a.epic)
    tree = build(epic, [load(f) for f in a.features], refs)
    page = render(tree)
    if a.standalone:
        page = '<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n' + page.replace("</style>\n", "</style>\n</head><body>\n", 1) + "\n</body></html>"
    key = tree["rec"].get("epic_key") or tree["rec"].get("feature_key") or "record"
    out = Path(a.out) if a.out else Path(a.epic).with_name(f"driver-tree-{key}.html")
    out.write_text(page, encoding="utf-8")
    if a.json:
        Path(a.json).write_text(json.dumps(export_nodes(tree), indent=2, ensure_ascii=False), encoding="utf-8")
    sev = {s: sum(1 for g in tree["gaps"] if g["severity"] == s) for s in ("Blocker", "Major", "Minor")}
    print(json.dumps({"output": str(out), "features": len(tree["feats"]), "epic_kpis": len(tree["ekpis"]), "gaps": sev}))


if __name__ == "__main__":
    main()
