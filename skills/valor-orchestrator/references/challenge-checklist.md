# VALOR Challenge Checklist

| # | Check | Section | Test | Default severity |
|---|---|---|---|---|
| C01 | Fabricated figure | any | Every number traces to a named source or the user | Blocker |
| C02 | Missing conversion | conversion | Required operational change and owner named | Blocker |
| C03 | Capacity as cash | economics | CR has a conversion mechanism and owner, or is excluded from totals | Blocker |
| C04 | Double count | economics / portfolio | Benefit not claimed by another feature, initiative or category | Blocker if confirmed; Major if suspected |
| C05 | Category mixing | economics | CS, CA, CR, RV, MG, WC, RR, NF kept separate | Major |
| C06 | Revenue not margin | economics | Revenue benefits use incremental contribution margin | Major |
| C07 | Demand assumption | economics | Recovered capacity has evidence of demand | Major |
| C08 | Average vs marginal | economics | Unit values are marginal, not averages | Major |
| C09 | Vanity KPI | measurement | KPI can't improve while the outcome worsens | Major |
| C10 | Output as outcome | measurement | Headline KPI is not controlled by the delivery team alone | Major |
| C11 | Exposure normalisation | measurement | Rates use an appropriate denominator | Minor |
| C12 | Baseline quality | measurement | Comparable period, seasonality addressed | Major |
| C13 | Target without baseline | measurement | Every target has a baseline | Major |
| C14 | Weak attribution | measurement | Counterfactual method chosen; confounders listed | Major (Blocker for T3) |
| C15 | Missing guardrail | measurement | At least one unintended-consequence KPI | Minor |
| C16 | Driver mis-mapping | formation | Primary driver is where value lands (P05 trap) | Major |
| C17 | Invented driver ID | formation | Driver ID exists in the register | Blocker |
| C18 | Untested assumption load | formation | Headline benefit doesn't rest on an untested assumption without a test plan | Major |
| C19 | Pathway tautology | conversion | No link merely restates the previous one | Minor |
| C20 | Dependency risk | conversion | Value doesn't silently depend on another feature's delivery | Major |
| C21 | No ramp | economics | Realisation profile reflects adoption | Minor |
| C22 | No risk adjustment / range | economics | Range or adjustment shown | Major for executive output |
| C23 | Projected shown as realised | any | Labels correct for tier | Blocker |
| C24 | Costs incomplete | economics | Change-management and run costs included | Major |
| C25 | Benchmark overreach | benchmarks | No claim of endorsement, certification or "based on" analyst methods | Major |
| C26 | Outcome owner is delivery | measurement | Outcome owner is a business role | Major |
| C27 | Strategic programme rollup | alignment | Strategic programme value not summed into BU/CoE | Major |
| C28 | Alternative uses of capacity | economics | Benefits that use the same freed capacity (sell it vs retire it) share an exclusive_group with one selected | Blocker |
| C29 | Consent-dependent conversion | conversion | Where conversion depends on third-party choice (drivers, customers, suppliers accepting), an acceptance KPI is a Business Leading KPI | Major |
| C30 | Value concentrated where adoption is hardest | conversion | The stakeholder group holding most of the value is checked for adoption risk, with a design response or an open question | Major |
| C31 | Benchmark mismatch | measurement / benchmarks | Benchmark definition, unit, population and scope match the KPI, or the adjustment is stated | Major |
| C32 | Stale benchmark | benchmarks | Benchmark is five years old or less, or is marked dated | Minor |
| C33 | Vendor-only headline | economics / benchmarks | Headline value is not supported only by quality C (vendor) benchmarks | Major |
| C34 | Benchmark beyond peers | measurement | Recommended target is not better than the best published peer level without a stated reason | Major |
| C35 | Illustrative counted | economics | No peer-median illustration enters a total, business case or Board report | Blocker |
| C36 | Watching, not doing | formation / economics | A monitoring, dashboard or control-tower feature claims only the decisions it changes (its own Business Leading KPIs, e.g. alerts acted on in time); it shows, but does not claim, outcomes owned by the features it watches | Blocker when another live record owns the outcome; Major when overlap is suspected |
| C37 | Value Owner is KPI Owner | measurement / evago | The Value Owner of an epic is not also the KPI Owner of any of its KPIs (valor-core §8) | Blocker |
| C38 | Orphan benefit | economics | Every benefit's linked_kpi exists in the record's measurement section | Major |
| C39 | Wrong direction | measurement | Every KPI has a direction from the register or the measure; no completion, compliance, adoption or accuracy rate is marked Lower is better; ranges move in that direction | Major |
| C40 | Shares over 100% | formation / measurement | The lower bounds of the feature shares of one epic KPI total 100% or less; leading-KPI links quote the epic KPI's own target and date | Major |
| C41 | Orphan branch | formation | Every pillar has a driver under it; every feature moves a named epic KPI; compliance-only work is a guardrail, not a branch | Major |
| C42 | Owners not as named | measurement / evago | Owners the user named hold exactly the KPIs the user gave them; other KPIs carry "suggested — [role] to confirm" | Major |

Log every rejected line of reasoning in the domain pack's "Previously rejected reasoning" table, so the next practitioner learns from it.
