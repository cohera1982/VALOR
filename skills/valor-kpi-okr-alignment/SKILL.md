---
name: valor-kpi-okr-alignment
description: VALOR specialist that links a feature's or epic's KPIs to existing OKRs, the VALOR KPI catalogue and BU, CoE, corporate-function or strategic-programme scorecards, flags shared and overlapping KPIs, and writes the alignment section of the VALOR value record. Called by valor-orchestrator; use directly when a practitioner asks how a value record lines up with OKRs, scorecards or other records.
---

# VALOR KPI and OKR Alignment

*VALOR is the background intellectual property of Rajaraman Kannan, licensed through Cohera Labs Pty Ltd.*

Owns the **`alignment`** section of the Feature Value Record. Read `references/valor-core.md` first (§3, §13–§15). Uses `references/kpi-register.csv` and `references/bu-map.csv`.

## Why this step matters
Leaders judge value through the measures they already run the business on. A record whose KPIs don't connect to an OKR or scorecard looks like a parallel universe; a record whose KPIs are already claimed elsewhere double counts.

## Procedure
1. **Reporting view.** From the BU map: BU, Corporate Function, CoE or Strategic Programme. Strategic-programme value is reported as its own tier and never summed into BU or CoE totals (C27).
2. **OKR links.** For each OKR or key result the user, Jira or a connected system supplies: which KPI in this record moves it, how the record contributes, and which other interventions share it. Never invent OKRs; if none are supplied, record "no OKR supplied — [owner] to confirm".
3. **Catalogue matches.** List the register KPIs reused (`catalogue_matches`) and the NEW KPIs proposed for the register (`new_kpis_proposed`), each with a one-line case for adding it.
4. **Shared KPIs and overlap.** For every outcome KPI, list the other features, epics or programmes that also move it (from the value register, Jira, or by asking once). For each shared KPI, recommend one of:
   - **Show, don't claim:** this record displays the KPI as context; the value stays with its owner (default for monitoring and control-tower features, C36).
   - **Claim own uplift under an agreed split:** only with an attribution method set before release and agreed by the KPI Owner (and the BU CFO or delegate for money), shown inside the epic total (valor-core §15 feature-level exception).
   - **Merge:** when two records are really one behaviour change.
   You own overlap for the record: list each overlapping record in `challenge.overlap_with` via the orchestrator, and pass confirmed or suspected double counts to valor-challenge-calibrate (C04, C36).
5. **Contribution check.** Feature contributions under one epic KPI must not add up to more than the epic's target (or the top of its suggested range before targets exist). Flag any excess.
6. **Threshold aggregation.** When the P01 approval threshold is relevant, note other epics in the same BU serving the same outcome KPI, so work is not split to stay under it (§15).

## Output
`alignment` YAML (`okr_links`, `catalogue_matches`, `new_kpis_proposed`, `bu_coe_view`), plus a short overlap table (KPI · other records · recommendation) and the counting-strand input "benefits counted once" (1 / 0.5 / 0).

## Never
- Invent OKRs, scorecard targets or other records.
- Split an epic's result between its features by default; attribution separates the epic from outside factors, not features from each other.
