# VALOR ↔ Jira Field Schema

Puts value data where delivery data lives, so the Portfolio Control Tower and eazyBI can roll it up. Custom field IDs are client-specific: fill in the `Field ID` column during setup. Do not reuse IDs from another tenant.

## Issue hierarchy
Strategic Theme → Initiative → Epic → Feature → Story → Task (six levels; see `valor-core.md` §13). Value fields live on Epic and Feature only. KPI issues link to Features via the "is measured by" link type.

**Confirm before mapping:** many Jira sites use the "Epic" issue type for what this hierarchy calls a Feature, with custom types above it (Jira Premium/Enterprise plan levels). Map by meaning, not by issue-type name: the level funded at the annual Portfolio Forum is the VALOR epic; the level prioritised at the quarterly forum is the VALOR feature.

| Level | VALOR role | Gate (Track 2) |
|---|---|---|
| Strategic Theme | Rollup only (pillars served) | — |
| Initiative | Rollup only; overlap check across epics | — |
| Epic | Investment case, annual verdict | Cannot move to "Funded" until Commit is complete |
| Feature | Behaviour change, KPIs, quarterly verdict | Cannot enter the quarter's plan until Commit is complete |
| Story, Task | No value fields; stories trace to feature KPIs in acceptance criteria | — |

## Epic-level fields (proposed)
VALOR Value Intent · VALOR Primary Pillar · VALOR Secondary Pillars · VALOR Value Hypothesis · VALOR Falsifier · VALOR Impacts (long text) · VALOR Benefits (long text) · VALOR Lifecycle Stage · VALOR Annual Verdict · VALOR Coherence % · VALOR Confidence · VALOR Agreement Log (long text, or comments tagged `VALOR-AGREE`).

## Feature-level fields (proposed)

| FVR path | Jira field name | Type | Field ID |
|---|---|---|---|
| formation.primary_driver | VALOR Primary Driver | Select (P0x-D0y list) | |
| formation.secondary_drivers | VALOR Secondary Drivers | Multi-select | |
| formation.value_intent | Value Intent | Text (short) | |
| conversion.pathway.required_operational_change | Required Operational Change | Paragraph | |
| conversion.pathway.change_owner | Conversion Owner | User picker | |
| record.evidence_tier | Value Evidence Tier | Select (T0–T3) | |
| record.record_status | Value Record Status | Select | |
| record.lifecycle_stage | VALOR Lifecycle Stage | Select (Shape…Capture) | |
| — | VALOR Quarterly Verdict | Select | |
| record.agreements | VALOR Agreement Log | Long text or tagged comments | |
| economics.results.annual_benefit_risk_adj | Projected Annual Benefit (risk-adj) | Number | |
| economics.results.npv | Projected NPV | Number | |
| economics.benefits[].category | Value Categories | Multi-select (CS…NF) | |
| challenge.defensibility | Value Defensibility | Select | |
| challenge.overlap_with | Benefit Overlap With | Issue links ("overlaps benefit of") | |
| capture.reviews[-1].recommendation | Last Capture Decision | Select | |
| capture.reviews[-1].realised_value | Realised Value to Date | Number | |
| — | VALOR Record (full YAML) | Attachment or long text | |

## KPI issue fields

| FVR path | Jira field | Type |
|---|---|---|
| kpi_id | KPI ID | Text |
| type | KPI Type | Select (4 types) |
| guardrail | Guardrail | Checkbox |
| contract.baseline_value / target_value | Baseline / Target | Number |
| contract.target_date | Target Date | Date |
| contract.outcome_owner | Outcome Owner | User |
| contract.validation_status | Validation Status | Select |

## Existing fields to respect
- Weighted DVF++ (prioritisation score on Epics): VALOR does not overwrite it. The orchestrator may *recommend* a revised score with rationale.
- Strategic Program field: strategic programmes (e.g. DDA&I, Atlas, Innovation, AI Labs) are reported as their own tier, never summed into BU or CoE value.

## Rollup rules
- Roll up only T2+ values into Board/GCEO totals; T0–T1 shown separately as "pipeline value".
- Never sum across features with an unresolved `overlap_with` link.
- Realised (T3) and projected values are separate series, never added together.
