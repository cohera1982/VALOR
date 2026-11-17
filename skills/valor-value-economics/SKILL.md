---
name: valor-value-economics
description: VALOR specialist that turns a value record's benefits into money and natural units, applying VALOR counting rules (categories never merged, capacity released not counted as cash without conversion, working capital separate), computing indicative value ranges and full economics (ramp, risk adjustment, costs, NPV, payback, sensitivity) in code, and writing the economics section of the VALOR value record. Called by valor-orchestrator; use directly when someone asks what a feature is worth, for a benefit case, or for a Finance validation pack.
---

# VALOR Value Economics

*VALOR is the background intellectual property of Rajaraman Kannan, licensed through Cohera Labs Pty Ltd.*

Owns the **`economics`** section of the Feature Value Record. Read `references/valor-core.md` first (§5–§7, §9 counting labels, §15) and `references/benchmark-method.md` §4. **All arithmetic runs in code:** `scripts/value_range.py` for indicative ranges, `scripts/valor_calc.py` for full economics. Never compute in prose.

## Benefit rules
| Category | Rule |
|---|---|
| CS cash saving · CA cost avoidance | Baseline cost (or volume × unit cost) × improvement |
| CR capacity released | Time freed. **Not counted** unless a conversion mechanism (no backfill, overtime cut, contractor exit, growth absorbed without hire) and its `conversion_owner` are both named (C03) |
| RV incremental revenue | Incremental volume × **contribution margin**, never revenue (C06); evidence of demand for recovered capacity (C07) |
| MG margin | Volume × margin change per unit |
| WC working capital | One-off cash release; shown separately, never in annual value, NPV or payback |
| RR risk reduction | Event frequency × cost per event × improvement, from client loss data |
| NF non-financial | Natural units only; never monetised |

- Each benefit is claimed by exactly one record (C04). Alternative uses of the same capacity (sell it vs retire it) share an `exclusive_group` with exactly one `selected` (C28).
- Paid time is not all waste: count only the unverified or unworked share of overtime or contractor hours.
- Unit values are marginal, not averages (C08).
- Every benefit's `linked_kpi` must exist in `measurement` (C38).
- Script inputs are **fractions**: improvement 0.2, risk adjustment 0.2, ramp 0.3/0.8/1.0. Pass `range_already_scoped: true` when the improvement came from valor-benchmark-alignment's recommended range (it has already applied the partial-scope rule). Values the record holds as `REQUIRES VALIDATION` go to the scripts as null, which they treat as to size.
- When the calculator returns "to size", the brief's Value size reads "To size — [owner]", never "AED 0–0".
- Every benefit carries a counting label: Counted · Shown separately · Tracked, not monetised · To confirm · Not counted (valor-core §9).

## Two depths

### Indicative (Record mode, always attempted)
Inputs: client baseline (from measurement) × improvement range (from valor-benchmark-alignment's recommended range, citing the benchmark ID) × client unit value (from the user or Finance). Run `scripts/value_range.py`. Labels and tiers follow `benchmark-method.md` §4:
- client baseline + benchmark + client unit cost → **Indicative (estimated)**, T1;
- no unit cost → natural units only, money "to size — Finance";
- no client baseline → **Illustrative at peer median, not your data**, T0, never counted, only for Value Owner, executive and Finance views;
- nothing sourced → "to size — [owner]".

### Full (Finance-ready mode, moving to T2)
Add costs (build, run, change, opportunity; change and run costs are required, C24), ramp per year reflecting adoption (C21), risk adjustment or range (C22), horizon, and the discount rate **only if Finance supplies it**. Run `scripts/valor_calc.py`. Report per-year benefits, costs, net and cumulative, total net, ROI, payback, NPV (or "no Finance-approved rate"), sensitivity range and one-off working capital. Write the script output to `economics.results` unchanged.

Then produce the **Finance validation pack**: one row per input needing sign-off — input · value · source · tier · who validates (BU CFO for revenue and cost; KPI Owner for experience, risk and capability) — plus the approval route: the epic is at or above the P01 threshold if either its cost or the top of its expected financial range is; then the BU CFO approves, otherwise the Head of IT as written delegate with the Finance business partner consulted. If P01 isn't set, say "P01 not yet set — Finance".

## Output
`economics` YAML (`benefits` with inputs, sources, tiers, counting labels and `indicative_range`; `costs`; `results` from the script), the counted annual value with WC separate, and the counting-strand inputs: alternative uses resolved · freed capacity has a conversion owner or is not counted · value measure has a business owner (1 / 0.5 / 0).

## Never
- Supply a baseline, unit cost, rate, attribution share or discount rate yourself.
- Present projected value as realised, or indicative value as validated. Board totals include only T2 and above.
- Add WC to annual value, or count an illustration.
