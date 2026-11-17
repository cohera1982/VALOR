---
name: valor-measurement-contract
description: VALOR specialist that selects KPIs from the VALOR KPI register and writes a full measurement contract for each (type, definition, formula, unit, baseline method, data source, owners, decision rule, guardrails), filling the measurement section of the VALOR value record. Called by valor-orchestrator or valor-value-coach; use directly when a practitioner asks to define, fix or contract the KPIs for a feature or epic.
---

# VALOR Measurement Contract

*VALOR is the background intellectual property of Rajaraman Kannan, licensed through Cohera Labs Pty Ltd.*

Owns the **`measurement`** section of the Feature Value Record. Read `references/valor-core.md` first (§3, §9, §12, §15). Look up KPIs in `references/kpi-register.csv`. Benchmarks and recommended ranges are attached afterwards by valor-benchmark-alignment; this skill leaves `recommended_range` for it.

## KPI set rules
- **Four types:** Business Leading ("is it being used?"), Business Lagging ("is it working?"), Technical Leading, Technical Lagging. Guardrail is a flag (`guardrail: true`), not a fifth type.
- **Epic:** owns the Business Lagging KPIs, one or two per business outcome, with a baseline where available.
- **Feature:** one to three Business Leading KPIs of its own: adoption ("is it being used?"), acceptance when C29 applies, and quality of use where a wrong action destroys value. Each records `predicts` (the epic KPI), `link` (the expected link, quoting the epic target and date), `cadence` (weekly or fortnightly) and `early_warning` (the threshold that triggers action). The feature names the epic Business Lagging KPI it contributes to and its expected share (a range); shares of one epic KPI across features must be able to sum to 100%. A feature never introduces a Business Lagging KPI its epic doesn't carry; if it seems to need one, the epic was framed badly: send it back to the Value Owner and KPI Owner.
- **Acceptance KPI** when conversion depends on a third party choosing (C29).
- **At least one guardrail** (C15): an unintended consequence (false alerts, longer drop times, complaints).
- **Rare or slow outcomes** (safety incidents, fines, churn): use a frequent proxy as "is it working?" and add a long-run proof KPI naming when it can be judged.
- **Escalation funnels:** "is it being used?" is the share resolved at the first stage; the watch-out is the share reaching the last.
- Technical KPIs are supporting evidence under the feature they support, never the headline value claim and never at epic level.
- **Direction** on every KPI, from the register row or analogue; without one, rates of completion, compliance, adoption, accuracy or coverage are Higher is better and counts of exceptions, errors, rework or manual effort are Lower is better. Ranges move in that direction.
- **Source** on every KPI: register, analogue (with `register_id`), stated, domain_pack or suggested.
- Three to five KPIs per record.

## Procedure
1. Match each needed measure to `kpi-register.csv` by business area (from the BU map's register areas) and meaning. When the work is a function inside a BU (finance close, HR, procurement), also search that function's register area (FIN, HRC, PRC…) and reuse a KPI whose definition matches; record the BU as the business unit. Reuse the register's kpi_id, definition, formula, unit, direction, aggregation, frequency, baseline method and owner role. A measure with no exact match takes its unit, frequency, direction and suggested range from the closest register row and records `source: analogue` with that `register_id`; it gets `NEW-nn` and a full contract, flagged in the admin note for the register.
2. Write the **contract** for each KPI (all fields in the FVR template): definition, population, unit, formula, baseline value or `REQUIRES VALIDATION`, baseline period, target or `REQUIRES VALIDATION`, data source, collection method, frequency, data owner, outcome owner (a business role, C26), decision rule ("if below X by date, review adoption; if above Y, scale").
3. **Baseline method** comparable to the target horizon: trailing 12 months seasonally comparable for most; first 4–6 weeks after go-live for new processes; trailing 24 months for rare events (C12). No target without a baseline (C13).
4. **Normalise** rates to an exposure denominator (per 100k km, per 1,000 t, per 100 workers) (C11).
5. **Vanity and output checks:** reject KPIs that can improve while the outcome worsens (C09) or that the delivery team controls alone (C10).
6. **Aggregation:** follow the register's rule (recompute ratios from components; never average ratios) so KPIs roll up to driver and pillar.
7. **Owners:** KPI Owner per KPI, never the Value Owner of the same epic (valor-core §8). Use the owners the user named on exactly the KPIs the user gave them; any other KPI gets "suggested — [role] to confirm".
8. Suggested ranges only from the register, or for a NEW KPI a relative range by the valor-core §9 rules (labelled suggested), until benchmark-alignment runs; never targets before target setting (§12 Baseline stage).
9. **Owner check (C37):** no KPI Owner may be the epic's Value Owner. The register's `owner_role` is a default; if it matches the Value Owner's role, propose a different KPI Owner.

## Output
`measurement.kpis` YAML; the two KPI links of the conversion strand (Business Leading KPI exists · acceptance KPI if a third party chooses, else null); and the data-strand inputs for scoring: KPIs match the register or are flagged NEW · units and aggregation roll up · baseline method comparable · data source exists or a plan to create one (1 / 0.5 / 0). Also report `kpis_total` and `baselines_supplied` for confidence.

## Never
- Invent a baseline, target or data source value. Missing values are `REQUIRES VALIDATION — [what, from whom]`; a figure the user states without a source is `asserted — source to supply ([who])`.
- Report a separate outcome result for a single feature (results are reported at epic level; valor-core §15).
