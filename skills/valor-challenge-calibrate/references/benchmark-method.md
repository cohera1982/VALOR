# VALOR Benchmark Method — benchmarked KPI ranges and indicative value ranges

Every VALOR skill reads this file before recommending a KPI range or a value range. Benchmarks give leaders an outside-in view: where peers perform and what similar changes have typically achieved. They never replace the client's own baseline, unit costs or Finance validation.

## 1. The benchmark register
`benchmark-register.csv` holds every benchmark the skills may cite. Each row is sourced from a page that was opened and checked.

| Column | Meaning |
|---|---|
| benchmark_id | `BM-<kpi_id>-n` |
| kpi_id | The KPI register entry it informs |
| benchmark_type | **peer_level** (where organisations perform: median, top quartile, typical level) or **improvement_range** (typical change achieved by a named intervention) |
| statistic | e.g. median · top quartile · typical range · reported reduction |
| value_low / value_high | In the KPI's unit; equal for a single figure. Improvements are positive magnitudes; the statistic gives the direction |
| context | Peer group, or the intervention behind the improvement |
| sector · region | Region matters: GCC or UAE figures are preferred when available |
| source_org · source_title · source_url · year | Citation |
| quality | **A** independent dataset, regulator, standards body or peer-reviewed · **B** major consultancy or association study with a stated sample · **C** vendor or case-study claim |
| notes | How it maps to the KPI; caveats |
| verified | Date an independent check confirmed the figure on the source page |

Only rows in this register may be called a benchmark. Coverage is partial (release 3: 271 benchmarks across 196 of 285 KPIs, 98 with an improvement range, all independently checked against their source pages on 26 Oct 2026); "none in register" is a normal answer. Never cite a benchmark from memory, and never cite one the register doesn't hold. If a KPI has no row, use the register's suggested range and label it *suggested*. The Value Orchestration Lead owns the register, reviews it each year, and adds rows only with a checked source.

## 2. Choosing the benchmark
1. Match on `kpi_id`. If the KPI is NEW, match only where the metric, unit and definition are the same; otherwise there is no benchmark.
2. Prefer quality A, then B. Quality C may inform a range but is shown as "vendor-reported", and may never be the only support for a headline value.
3. Prefer GCC or UAE, then global. Say which region it is.
4. Prefer figures from the last five years. Older rows are shown with "(dated: [year])".
5. A **peer gap** (statistic starting "peer gap": leaders vs peers at one point in time) is not an improvement result. Use it only as a ceiling, never as an expected change.
6. Check scope. A benchmark for a whole intervention (end-to-end close automation) is not a benchmark for one part of it (COGS only). See §3.

## 3. Recommending a KPI range (the recommended range)
Each KPI shows three things: **Today** (the client baseline, or "to supply"), the **Benchmark** and the **Recommended range**.

| Situation | Recommended range |
|---|---|
| improvement_range exists, and the feature delivers the whole intervention | The benchmark range, applied to the client baseline |
| improvement_range exists, but the feature delivers only part of it | From the benchmark's lower bound up to its midpoint, and say why ("COGS is one step of the close") |
| Only peer_level exists, and the baseline is known | Baseline below median → close 25–50% of the gap to median within the horizon. Baseline at or above median → close 25–50% of the gap to top quartile. Show the gap in units |
| Only peer_level exists, and the baseline is unknown | Show where peers sit; set the range once the baseline arrives ("Peers: median 6.4 days, top quartile 4.8") |
| No benchmark | The register's suggested range, labelled *suggested* |

**Single-point benchmarks.** When an improvement_range row has one figure (low = high), it can't define a range on its own: show it as context ("Typical: 2 days faster with close automation") and use the suggested range, unless the feature delivers the whole intervention, in which case the figure is the top of the range and the suggested range's lower bound is the bottom.

**Cap rule:** a recommended target never goes beyond the best published peer level (top quartile or top decile) without a reason the owner states. Flag any range that would.

The 25–50% gap-closure rule is VALOR's convention for one planning horizon. Say so when you use it ("VALOR convention: close a quarter to half the gap per horizon"). It is a planning rule, not a benchmark.

Ranges remain recommendations until the KPI Owner agrees them (valor-core §12). Agreed ranges become targets only at target setting.

## 4. Recommending a value range (indicative value)
An indicative value range turns a KPI range into money, or into natural units, before Finance validates it. It always runs in code: `scripts/value_range.py` (input and output in the script header). The arithmetic is never done in prose.

**Formula by value category**

| Category | Indicative annual value |
|---|---|
| CS · CA | baseline cost (or volume × unit cost) × improvement low/high |
| CR | baseline hours × improvement × loaded hourly cost. Shown, but **not counted** unless a conversion mechanism is named |
| RV | incremental volume × **contribution margin** per unit (never revenue; C06) |
| MG | volume × margin change per unit |
| WC | balance × improvement: a **one-off** cash release, shown separately and never added to annual value |
| RR | expected-loss reduction = event frequency × cost per event × improvement. Needs client loss data |
| NF | Natural units only (days, incidents, NPS points); never monetised |

**Inputs and their evidence**

| Inputs available | Label | Evidence tier |
|---|---|---|
| Client baseline + benchmark improvement + client unit cost | **Indicative (estimated)** | T1 |
| Client baseline + benchmark improvement, but no unit cost | Natural units only; money "to size — Finance" | T1 for units |
| No client baseline: peer-median baseline from the register + benchmark improvement + benchmark unit cost | **Illustrative at peer median, not your data** | T0, never counted, never in totals |
| Nothing sourced | "To size — [owner]" | T0 |

Currency: show the source currency and the converted figure. Use the pegs AED 3.6725 = USD 1 and SAR 3.75 = USD 1, and state them.

**Where it shows**
- The Executive Brief's Value size row: "Indicative AED x–y a year (benchmarked, to validate — Finance)", or "Illustrative at peer median: …".
- Value Card section 4: one row per benefit, showing formula, inputs with source, range, counting label.
- The record: `economics.benefits[].inputs` (each with source and tier) and `results` (written by the script only).

Indicative value is never Board-reportable. Board and executive totals still include only T2 and above (scorecard roll-up rules).

## 5. Labels the user sees
- Benchmark cell: `Peers: median 6.4 days · top quartile 4.8 (APQC, 2024, A)`, or `Typical: 20–30% reduction with close automation (Hackett, 2023, B)`.
- Recommended range cell: `5.5–6.0 days (benchmarked)`, or `20–40% below today (suggested)` when no benchmark exists.
- Value size: `Indicative AED 1.2–2.1m a year (benchmarked; to validate — Finance)`.
- Quality C: add "(vendor-reported)".
- Never write "industry standard", "best practice" or "guaranteed". Write "peers", "typical" or "reported".

## 6. When local evidence wins
Once the client has two quarters of actuals, their own trend replaces the benchmark for target setting. The benchmark stays only as context. Never keep a benchmark-based target that the client's data contradicts.

## 7. Challenge checks (added to the checklist)
- **C31 Benchmark mismatch:** the definition, unit, population or scope differs from the KPI, and no adjustment is stated. Major.
- **C32 Stale benchmark:** older than five years and not marked dated. Minor.
- **C33 Vendor-only headline:** the headline value rests only on quality C. Major.
- **C34 Benchmark beyond peers:** the recommended target is better than the best published peer level, with no stated reason. Major.
- **C35 Illustrative counted:** a peer-median illustration has entered a total, a business case or Board reporting. Blocker.

## 8. Adding benchmarks: sources and access
New register rows follow the same checks as release 3 (source page opened, figure confirmed, quality graded). Look for sources in this order:

| Order | Source type | Examples | Grade |
|---|---|---|---|
| 1 | Open, method published | APQC Open Standards Benchmarking public summaries and measure definitions, government and statistics bodies (OECD, ILO, World Bank, UAE FCSC), regulators, public-sector benchmarking reports | A or B |
| 2 | Professional body survey with stated sample and year | CIPP, Australian Payroll Association, SHRM, IFMA | B |
| 3 | Licensed or members-only (Gartner, Forrester, Hackett, IDC, APQC member data) | Only from the client's own subscription | Client crosswalk only |
| Never | Vendor blogs, marketing "statistics" pages, figures with no method or sample | — | Excluded |

- **Licensed and members-only figures never enter `benchmark-register.csv`,** because the register ships inside the plugin to every client. They go into a client's own `benchmark-crosswalk.md` (one per client, kept with that client's records, never in the plugin), entered by an admin from the client's licence with report name, date and fit. Records cite them as crosswalk IDs (`XW-nnn`) alongside register IDs.
- **Fit** for every new row: definition, industry, region, scale and recency. Weak fit is context only and never sets a range.
- **Definitions without figures** (for example APQC measure lists) may be used to align a KPI's definition with a benchmark measure; they are not benchmarks.

## 9. Value at stake anchors (sizing the Value Intent)
`value-at-stake-anchors.csv` holds problem-size benchmarks by value driver (what a breach, an hour of downtime or a payroll error costs), used only to help a leader size the **value at stake** in a Value Intent when they have no figure. They are not KPI benchmarks and never set a KPI range.

- Offer two or three anchors for the epic's primary driver, one marked headline, never two that overlap (lost business already sits inside breach cost).
- Show each with how to size it, its source, year and quality, labelled **"benchmark, not our figure"**; rows older than five years show "(dated: year)". With no row for the driver, say "Group data only".
- The figure the leader types is the value at stake (T0 "stated"). An anchor never becomes the value claim, never raises the tier and is replaced with Group data before Commit.
- Same rules as §1: rows only with a checked source; the Value Orchestration Lead owns the file and refreshes it each year.
