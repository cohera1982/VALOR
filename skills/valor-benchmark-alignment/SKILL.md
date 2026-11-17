---
name: valor-benchmark-alignment
description: VALOR specialist that attaches verified industry benchmarks from the VALOR benchmark register to each KPI, derives recommended KPI ranges (full versus partial scope, gap-to-peer convention, cap at best peer level) and the improvement inputs for indicative value, and writes the benchmarks section of the VALOR value record. Called by valor-orchestrator for every record; use directly when someone asks how a KPI or value case compares with industry peers.
---

# VALOR Benchmark Alignment

*VALOR is the background intellectual property of Rajaraman Kannan, licensed through Cohera Labs Pty Ltd.*

Owns the **`benchmarks`** section of the Feature Value Record and the `benchmark_ids`, `recommended_range`, `range_basis` and `scope_vs_benchmark` fields of each KPI contract. Read `references/benchmark-method.md` in full and `references/valor-core.md` §7 rules 1–2. The only source of benchmarks is `references/benchmark-register.csv`, plus the client's own `benchmark-crosswalk.md` where one exists (licensed or members-only figures entered from that client's subscription; method §8). Crosswalk entries are cited as `XW-nnn`, shown with their source and fit, and never copied into the register.

## Procedure
1. **Match.** For each KPI, find register rows by `kpi_id`. A NEW KPI matches only if metric, unit and definition are the same; otherwise "none in register".
2. **Choose** (method §2): quality A, then B; C only as "vendor-reported" and never the sole support for a headline value. Prefer GCC or UAE, then global. Prefer the last five years; mark older rows "(dated: year)"; rows without a year "(undated)". A **peer gap** (leaders vs peers at one point in time) is a ceiling only, never an expected improvement.
3. **Check fit** (C31): definition, unit (calendar vs working days, per-year vs per-month), population and scope. State any adjustment, or reject the row.
4. **Recommend a range** (method §3):
   - improvement_range and the feature delivers the whole intervention → benchmark range on the client baseline;
   - improvement_range and only part of it → lower bound to midpoint, with the reason;
   - peer_level only, baseline known → close 25–50% of the gap to median (below median) or to top quartile (at or above median), labelled as VALOR convention, not a benchmark;
   - peer_level only, baseline unknown → show where peers sit; range once the baseline arrives;
   - none → the register's suggested range, labelled suggested.
   - a single-point improvement figure → context only, per method §3 *Single-point benchmarks*.
   **Cap:** never better than the best published peer level without the owner's stated reason (C34).
5. **Feed economics.** Pass each benefit's improvement range as fractions, with its benchmark ID (or "suggested") and `range_already_scoped: true` when you applied the partial-scope rule, to valor-value-economics.
6. **Local evidence wins.** Once the client has two quarters of actuals (from valor-value-review), their own trend replaces the benchmark for target setting; keep the benchmark as context only.
7. **Executive line.** One sentence for executive output: how the case compares with peers ("Close today is unknown; peers close in 4.8–6.4 days, digital leaders 35–57% faster").

## Labels the user sees
- Benchmark: `Peers: median 6.4 days · top quartile 4.8 (APQC, 2017, B, dated)` or `Typical: 30–50% reduction with predictive maintenance (US DOE, 2010, A, dated)`.
- Recommended range: `[range] (benchmarked)`, `[range] (VALOR convention)` or `[range] (suggested)`.
- Never "industry standard", "best practice" or "guaranteed"; say "peers", "typical" or "reported". Paraphrase sources, never quote at length.

## Output
Updated KPI contract fields, `benchmarks.alignment_notes` (benchmark IDs used, adjustments, rejections) and `benchmarks.executive_line`. Missing benchmarks are listed for the Value Orchestration Lead, who owns the register.

## Never
- Cite a benchmark not in the register or the client's crosswalk, from memory, or from a search done during the session. New benchmarks enter the register only through its verified update process (repository build checks).
- Present a benchmark as the client's own figure, or an illustration as a target.
