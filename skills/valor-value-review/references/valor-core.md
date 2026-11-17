# VALOR Core — Definitions and Reasoning Rules

VALOR (Value Orchestration Framework) is the background intellectual property of Rajaraman Kannan, licensed through Cohera Labs Pty Ltd. Ownership does not transfer. Confidential; not for redistribution. Every VALOR skill reads this file first. Where this file and a skill disagree, this file wins.

## 1. Value hierarchy

Value Intent → Value Pillar → Value Driver → KPI

Delivery hierarchy (Jira): Strategic Theme → Initiative → Epic → Feature → Story. Strategic Theme and Initiative are custom fields on Epics. A Feature's value claim must trace upward to at least one Value Driver (ID format `P0x-D0y`), and downward to measurable KPIs.

## 2. Value pillars

| ID | Pillar | Drivers |
|---|---|---|
| P01 | Expand Revenue & Unlock New Value Streams | 9 |
| P02 | Optimise Cost & Operational Efficiency | 9 |
| P03 | Strengthen Resilience & Strategic Agility | 7 |
| P04 | Elevate Workforce Capability & Culture | 7 |
| P05 | Accelerate Digital, Data & AI Transformation | 10 |
| P06 | Orchestrate Strategic Advantage & Ecosystems | 7 |

49 drivers in total. P01 also carries brand equity as a commercial multiplier.

**Level rules.** At **epic** level: value intent, value hypothesis, primary pillar and secondary pillars, impact and benefits. Each epic breaks down into features. At **feature** level: one primary driver and up to two secondary drivers, and the KPIs. A feature's drivers must sit under its epic's primary or secondary pillars (a coherence check). Full driver register (v24, 49 drivers; also in `driver-register.csv`):

**P01 Expand Revenue & Unlock New Value Streams**
- P01-D01 Increase Conversion Effectiveness
- P01-D02 Strengthen Pricing & Yield Discipline
- P01-D03 Expand Customer Lifetime Value
- P01-D04 Launch & Scale New Products, Services & Business Lines
- P01-D05 Monetise Digital Channels & Customer Experience
- P01-D06 Accelerate Cross-Sell & Revenue Synergy
- P01-D07 Expand Group Footprint into New Markets & Segments
- P01-D08 Demand Generation & Brand Equity
- P01-D09 Customer Advocacy & Revenue Referral

**P02 Optimise Cost & Operational Efficiency**
- P02-D01 Drive Operational Efficiency & Scale Leverage
- P02-D02 Maximise Workforce Output & Productivity
- P02-D03 Strengthen Group Procurement & Supplier Excellence
- P02-D04 Capture Value from Process Improvement & Intelligent Automation
- P02-D05 Reduce Structural Waste & Input Costs
- P02-D06 Maximise Asset & Capital Utilisation
- P02-D07 Optimise Working Capital & Cash Conversion
- P02-D08 Shared Services & GBS Efficiency
- P02-D09 Embed a Culture of Process Discipline & Ownership

**P03 Strengthen Resilience & Strategic Agility**
- P03-D01 Govern Operational & Service Continuity Risk
- P03-D02 Strengthen Regulatory Compliance & External Governance
- P03-D03 Enterprise Risk Sensing & Intelligence
- P03-D04 Accelerate Strategic Decision Velocity
- P03-D05 Build Organisational & Strategic Nimbleness
- P03-D06 Supply Chain Resilience & Continuity
- P03-D07 Regulatory Horizon Management

**P04 Elevate Workforce Capability & Culture**
- P04-D01 Sustain GCC Employer of Choice Leadership
- P04-D02 Build Leadership Pipeline & Advance Emiratisation
- P04-D03 Workforce Capability Development
- P04-D04 Culture, Engagement & Employee Experience
- P04-D05 Deliver Seamless, Compliant Employee Lifecycle Management
- P04-D06 Embed Multi-Jurisdiction Regulatory & Policy Compliance
- P04-D07 Build Enterprise Agility & High-Performance Culture

**P05 Accelerate Digital, Data & AI Transformation**
- P05-D01 Build Scalable Group Technology Platform
- P05-D02 Eliminate Technical Debt & Accelerate Change Velocity
- P05-D03 Strengthen Cyber & Data Security Resilience
- P05-D04 Build Enterprise Data Foundation & Governance
- P05-D05 Embed Analytics-Driven Decision Making
- P05-D06 Monetise Group Data as a Strategic Asset
- P05-D07 Deploy AI at Scale Across Operations & Workforce
- P05-D08 Build AI-Led Operating Model
- P05-D09 Build AI-Ready Organisation & Governance
- P05-D10 Build Group CX Experience Orchestration & Platform

**P06 Orchestrate Strategic Advantage & Ecosystems**
- P06-D01 Build Institutional ESG Credibility & Strategic Positioning
- P06-D02 Advance Circular Economy & Sustainable Operations
- P06-D03 Build Strategic Partnerships & Ecosystem Positioning
- P06-D04 Accelerate M&A & Portfolio Transformation
- P06-D05 Strengthen Group Innovation Pipeline & Ventures
- P06-D06 Build Strategic Technology Ventures & Transform Business Models
- P06-D07 Licence to Operate & Government Relations

Every feature has **one primary driver** (where most of its value lands, under the epic's primary or a secondary pillar) and **up to two secondary drivers** (genuine further contributions, each with a one-line role). A secondary driver signals contribution, not a second benefit: never count the same benefit under two drivers. Use only IDs from this register.

### P05 trap
Most features touch technology. A feature belongs in P05 only when its primary value is the digital, data or AI capability itself. If the capability serves an operational outcome (fewer breakdowns, faster bookings), the primary driver sits in the pillar of that outcome, and P05 is at most a secondary link. **Monitoring, dashboards and control towers** create value only through the decisions they change: the primary driver is the operational lever those decisions move, usually P02-D01 (operational efficiency) or P03-D01 (service continuity); P03-D04 only for executive decisions; P05-D05 only when the analytics capability itself is the product. They show, but don't claim, outcomes owned by the features they watch (C36).

## 3. KPI types (four-quadrant taxonomy)

| | Leading (predicts) | Lagging (confirms) |
|---|---|---|
| **Business** | Business Leading: early signs of business outcome (adoption by drivers, % alerts actioned) | Business Lagging: the outcome itself (repair visits per 100k km, revenue per vehicle-day) |
| **Technical** | Technical Leading: capability readiness (model precision, data freshness, release frequency) | Technical Lagging: technical result over time (uptime, incident rate, defect escape) |

**Epic and feature KPIs (EVAGO-aligned, §15).** The epic owns the Business Lagging KPIs: one or two per business outcome, identified at the annual definition with a baseline where available. Every feature needs at least one Business Leading KPI of its own: its adoption KPI ("is it being used?", proof its conversion is happening), plus an acceptance KPI where conversion depends on a third party choosing (C29) and names which of its epic's Business Lagging KPIs it contributes to, and its expected share of that movement. A feature never introduces a Business Lagging KPI that its epic does not carry; a new outcome KPI at feature level means the epic was framed badly and goes back to the Value Owner and KPI Owner. Technical KPIs are supporting evidence, never the headline value claim.

**Guardrail KPI**: a KPI of any type flagged `guardrail: true`, tracking an unintended consequence (false-alert interventions, driver complaints). It is a flag, not a fifth type.

## 4. Value lifecycle (systemic value orchestration)

> Working definitions. Confirm these match the definitions in the VALOR v24 deck and the Strategic Change manuscript before external use.

| Stage | Question it answers |
|---|---|
| Value formation | Whose problem matters, what strategic intent it serves, what outcome and investment rationale are expected, and on what assumptions |
| Value conversion | How the feature, the operational change it requires, adoption and dependencies turn capability into outcomes |
| Value capture | Whether the benefit materialised, who captured it, what evidence supports attribution, and whether it persists |
| Systemic orchestration (spans all three) | Which decisions, owners, resources and interdependencies need coordination or adjustment across features, BUs and CoEs |

The distinctive VALOR claim: value is lost at the **conversion** step more often than at formation. A feature that ships without the operational change it depends on produces no value. Skills must always name the required operational change and its owner.

## 5. Value categories (never merge)

| Code | Category | Cash-relevant? |
|---|---|---|
| CS | Cash saving (budget line reduces) | Yes |
| CA | Cost avoidance (future cost does not occur) | Indirect |
| CR | Capacity released (time freed, no cost removed unless redeployed or exited) | No, unless converted |
| RV | Incremental revenue | Yes |
| MG | Margin improvement | Yes |
| WC | Working capital | Yes (one-off) |
| RR | Risk reduction (expected-loss reduction) | Probabilistic |
| NF | Non-financial outcome (natural units: NPS, safety incidents, staff retention) | No |

Rule: **CR is not CS.** Released capacity becomes cash only when there is a named conversion mechanism (headcount not backfilled, overtime cut, contractor exit, volume absorbed without hire), with an owner.

## 6. Evidence tiers

Records progress through tiers. Lower tiers never block work; they limit what may be claimed.

| Tier | Name | Meaning | May appear in |
|---|---|---|---|
| T0 | Asserted | Stated by a proposer; no data | Team backlog only |
| T1 | Estimated | Calculated from a stated method and sourced inputs | Prioritisation, Portfolio Forum discussion |
| T2 | Finance-validated | Baseline, unit economics and method agreed by Finance | Business cases, fund release, Board reporting as *projected* |
| T3 | Realised | Observed actuals vs baseline, attribution reviewed | Board reporting as *realised* |

Projected figures are always labelled projected. Never present a T0–T2 figure as realised.

## 7. Non-negotiable reasoning rules

1. **Never manufacture a number.** Baselines, unit rates and attribution percentages come only from the user, a supplied source, or the client's approved economics. Benchmarks come only from `benchmark-register.csv` (sourced, checked rows). Otherwise write `REQUIRES VALIDATION — [what is needed, from whom]`. Three things are allowed, always as ranges, always labelled, and never counted until the owner agrees them: a **benchmarked range** (derived from a register benchmark by the rules in `benchmark-method.md` §3), a **suggested range** (the KPI register default where no benchmark exists, or for a NEW KPI a relative range set by the §9 rules), and an **indicative value range** (computed by `scripts/value_range.py` from benchmark and client inputs, per `benchmark-method.md` §4).
2. **Never invent a source or quote.** Benchmarks and analyst references come only from `benchmark-register.csv` (and `benchmark-crosswalk.md` where present). Cite the organisation, year and quality grade; paraphrase, never reproduce text.
3. **Name the conversion.** Every value claim states the operational change required and who owns it.
4. **One benefit, one home.** Each benefit is claimed by exactly one feature or initiative. Overlaps are surfaced, not split silently.
5. **Calculations run in code.** Use `valor-value-economics/scripts/valor_calc.py` (or show the formula and inputs explicitly). No mental arithmetic in financial claims.
6. **Ask only material questions.** Ask when the answer changes the driver, the KPI, the value category or the tier. Otherwise proceed and mark the gap.
7. **VALOR vocabulary is primary.** Analyst terms appear only as benchmark references, never as the record's terminology.

## 8. Roles

Role names follow the EVAGO Value Definition and Tracking Process. One person can hold more than one role, except that the Value Owner and the KPI Owner of the same epic must be different people.

| Role | Primary use |
|---|---|
| Value Owner (usually the Business SVP whose function benefits) | Accountable for an epic's value: intent, outcome, targets and realisation; confirms the hypothesis and targets |
| KPI Owner | Owns a measure: definition, data source and baseline; confirms KPI targets; validates non-financial results. Never the Value Owner of the same epic |
| ITBP | Defines value jointly with the Value Owner; prepares the financial case; owns the link from KPIs to the control-tower feed |
| Product owner / business analyst | Writes the record with the coach; builds the pathway and measurement contract; links features to early signals; records value realised |
| Scrum Master / delivery lead | Builds Business Leading KPIs into the Definition of Done, makes sure the data feed is live at release, supplies hypercare data |
| Head of IT | Accountable for Circle and monthly tracking; approves expected financial outcomes below P01 as the BU CFO's delegate, consulting the Finance business partner |
| BU CFO (and Finance business partner) | Approves expected financial outcomes and financial targets at or above P01; validates baselines, unit economics and method (T1 → T2) and realised financial value (T3) |
| BU CEO | Chairs the BU value workshop; owns the BU value submission |
| CDTO / Portfolio Forum | Chairs Annual and quarterly Portfolio Forum; decides epics, envelopes, KPI targets, priorities and scale or retire |
| Value Orchestration Lead | Owns the value process, value register, KPI register and this coach's content; samples non-financial validations |
| Portfolio Governance Lead | Owns gates, forums and packs; consolidates the portfolio before Portfolio Forum |

## 9. Review scores (shown on the Value Review page)

### Suggested ranges, baselines and frequency
Every KPI in the register carries a measurement frequency, a unit, a recommended baseline method (e.g. 'trailing 12 months, seasonally comparable'; 'first 4–6 weeks after go-live' for new processes; 'trailing 24 months' for rare events) and a suggested target range. Where `benchmark-register.csv` holds a matching benchmark, the KPI also shows the benchmark (peer level and/or typical improvement, with source) and a **recommended range** derived by `benchmark-method.md` §3, which takes precedence over the suggested range. Each KPI on a feature carries a suggested range (min–max, unit, horizon). Prefer relative ranges against the owner's baseline ("30–50% below baseline within 2 quarters") over absolute figures. Watch-outs use a ceiling ("keep below 15%"). Owners accept, adjust or reject (with a reason). Only agreed ranges become targets.

**Suggested ranges for NEW KPIs (VALOR conventions, from the KPI register's patterns).** Use the row that fits, labelled "suggested — VALOR convention":
| KPI kind | Suggested range |
|---|---|
| Adoption of a new digital step ("is it being used?") | 60–80% within 3–6 months of go-live |
| Uptake of an optional offer (plans, subscriptions, referral or community activation), as a share of eligible customers | +5 to +15 pts above baseline within 2–4 quarters; for a new offer, 10–25% of eligible customers within 4 quarters |
| Compliance with a defined process step | 90–98% within 2 quarters |
| Capability or data quality improvement | +10 to +20 pts above baseline within 2 quarters |
| Outcome rate or cycle time to reduce | 20–40% below baseline within 2–4 quarters |
| Unit cost to reduce | 5–15% below baseline within 4 quarters |
| Revenue or yield per unit to raise | 3–8% above baseline within 4 quarters |
| Rare harmful events | 30–50% below baseline within 4 quarters; zero for material events |
| Model quality before scaling | 80–90%; review below 70% |

### Value hypothesis
Every **epic** carries a falsifiable hypothesis, naming the features that deliver it: "We believe [the epic's change, naming the features that deliver it where they are known] will [move the outcome KPI by the suggested range] within [horizon], because [behaviour change]. If that holds, [value KPI] will [move]." Plus: "We'll know we're wrong if [falsifier]." The owner accepts it or challenges it with a reason. At the annual definition the ranges in the hypothesis are **suggested ranges**, labelled as such; they are not targets. Committed targets are set on the same KPIs during execution, once the solution approach is known, and approved at quarterly Portfolio Forum (§12 Baseline, §15).

### Benefit counting labels
Every benefit shows how it is counted: **Counted** (enters the money total) · **Shown separately** (one-off cash timing) · **Tracked, not monetised** (people or risk outcomes in natural units) · **To confirm** (depends on a fact not yet supplied) · **Not counted** (time redeployed, or an alternative use of the same capacity). Owners agree or challenge each benefit.

### Value coherence (0–100%), rubric v2
How well-formed the chain is from intent to value. Agreement is not part of coherence (it counts once, in confidence). Four strands, each link scoring 1 (in place), 0.5 (partial) or 0 (missing); each strand = average of its links × 100.

| Strand | Links |
|---|---|
| **Strategic** | Value intent linked to a primary pillar · feature drivers sit under the epic's pillars · hypothesis states a falsifier |
| **Conversion** | Behaviour change named · change owned by a business role · an "is it being used?" (Business Leading) KPI exists · where conversion depends on a third party choosing (drivers, customers, patients, brokers, suppliers), an acceptance KPI exists (C29) · adoption risk addressed where most of the value sits (C30) |
| **Counting** | Benefits counted once · alternative uses of the same capacity resolved to one · freed capacity has a conversion owner or is not counted · value measure has a business owner |
| **Data** | KPIs match the register or are flagged NEW · units and aggregation roll up to driver and pillar · baseline method comparable to the target horizon · a data source exists or a plan to create one |

Headline coherence = average of the four strands, equally weighted. **Conversion gate:** if the conversion strand is below 75%, headline coherence is capped at 60%. Always show the weakest strand beside the headline.

### Confidence (0–100)
How far the value is backed by evidence and agreement:
| Component | Points |
|---|---|
| Finance validation (evidence tier T0/T1/T2/T3) | 0 / 15 / 30 / 40 |
| Baselines supplied (share of KPIs) | up to 20 |
| Assumptions tested (proven = 1, partly = 0.5) | up to 20 |
| Hypothesis, KPI ranges and benefits agreed by owners (confirmed = full, recorded = half; see §12) | up to 10 |
| A way to prove attribution chosen (e.g. staggered rollout) | 10 |

The page always shows the next best step: the component the team can move soonest.

### Value verdict (conversion × confidence)
Every epic gets one verdict from two axes. **Entry check first:** if the strategic, counting or data strand is below 60%, the verdict is **Fix the logic first** and the epic is not placed on the grid.

Before funding (Value Readiness): conversion = the conversion strand.
| | Confidence < 50 | Confidence ≥ 50 |
|---|---|---|
| Conversion ≥ 75% | **Prove:** fund a pilot, collect baselines | **Fund:** proceed at full scope |
| Conversion < 75% | **Rework or stop:** design the adoption first | **Fix adoption:** the numbers hold but no one owns the change |

After delivery (Value Performance): conversion = Business Leading KPIs at or above the lower end of their agreed range; confidence high = T2 or above with an attribution method applied. Verdicts: on track + high → **Scale**; on track + low → **Continue, prove attribution**; lagging + high → **Adapt: fix adoption**; lagging + low → **Stop or redirect**. After delivery, conversion uses adoption KPIs only and confidence uses evidence tier and attribution only, so the axes stay independent.

The verdict never decides funding alone: always show it with the value size (the scorecard's VALUE line).

## 10. Impact categories

Impact is the change a stakeholder group experiences. Money belongs in benefits, not impact. Every impact is tagged with exactly one category:

| Code | Category | Who | Typical changes |
|---|---|---|---|
| CUS | Customer | Customers, patients, tenants, students, passengers, buyers | Access, waiting time, convenience, outcomes, trust |
| WRK | Workforce | Employees, drivers, clinicians, technicians, agents | Workload, safety, earnings, capability, experience |
| PTN | Partner and channel | Brokers, dealers, distributors, suppliers, payers, OEMs | Speed of doing business, disputes, terms, collaboration |
| OPS | Operations | Teams and processes | Speed, quality, capacity, reliability, control |
| CMP | Compliance and safety | Regulators, the public, the organisation's licence | Rules met, incidents avoided, auditability |
| SOC | Society and environment | Communities, environment | Emissions, waste, inclusion, community outcomes |

Each impact states: category, who, what changes for them (in their words), and the measure that shows it. Direction is always stated (better / worse for whom). An impact on a group the feature makes worse off (e.g. older patients who can't use an app) is recorded too, as a negative impact with a watch-out measure.

## 11. Explaining the scores (shown every time)

**Value coherence** measures how completely the chain from intent to value holds together, across four strands: strategic (intent, pillar, drivers, falsifier), conversion (the behaviour change, its owner and adoption), counting (each benefit counted once, with an owner) and data (KPIs that are defined, comparable and sourced). It tells you whether the value case is well-formed and traceable. It does not tell you how big the value is or whether it is proven.

**Confidence** measures how far the value is backed by evidence and agreement: Finance validation, baselines supplied, assumptions tested, owners agreeing KPIs and benefits, and a way to prove the feature caused the change. A well-formed case (high coherence) can still have low confidence until data arrives.

Read them together through the value verdict (§9): conversion and confidence place the epic on the grid; the other three strands are the entry check.

Standard one-line explanations to show with every score:
- Coherence: "How completely the chain from intent to value holds together. It shows the case is well-formed, not how big or proven the value is."
- Confidence: "How far the value is backed by evidence and agreement. It rises as baselines arrive, assumptions are tested and owners agree the measures."
- Verdict: "Where the epic stands on two questions: will behaviour change (conversion), and is the value backed (confidence)? It says what to do next, not how big the value is."

## 12. Lifecycle stages and agreements

### Stages
One person (usually the product or value owner) fills the record, across the lifecycle. Each stage asks only what can be known then. **The user chooses the pace:** stop after any stage, or go straight through as far as they can in one sitting. Anything not yet knowable is recorded as "to supply — [who]", never guessed.

| Stage | EVAGO moment | Completes when | Scores shown |
|---|---|---|---|
| 1 Shape | Annual budgeting: BU value workshop, then Annual Portfolio Forum (or Circle for in-year demand) | Value intent, primary pillar, business outcome, one or two Business Lagging KPIs per outcome, baseline where available, Value Owner and KPI Owner named (different people), expected financial outcome as a range or "none claimed", at least one impact, draft hypothesis with suggested ranges and a falsifier | Strategic strand; no verdict |
| 2 Commit | Execution entry, before the epic starts | Value definition confirmed jointly by the ITBP and the Value Owner; expected financial outcome approved by the BU CFO (at or above P01) or the Head of IT as delegate (below P01, Finance business partner consulted), or recorded as none claimed; features planned for the first cycle (by the first feature's Commit) with drivers, each with its own Business Leading KPI and its contribution to an epic KPI; every benefit has a counting label; behaviour change and its owner named | All strands, confidence, readiness verdict |
| 3 Baseline | During execution, before the quarterly Portfolio Forum after the epic's first quarter (P15) | Measured baseline and data source for every KPI; committed target values and dates confirmed by the KPI Owner, and by the BU CFO or delegate for financial targets within the approved range; attribution method chosen; targets approved at quarterly Portfolio Forum | As above, confidence rises |
| 4 Track | Each go-live, through hypercare (one to four weeks) and on to day 90 | Business Leading actuals against agreed ranges; value realised, impact and benefits first calculated per release | Performance verdict (conversion measured) |
| 5 Capture | Until the benefit window (P10) closes; G5 at epic close | Business Lagging actuals; validation (BU CFO for revenue and cost, KPI Owner for the rest); epic roll-up; hypothesis proven, partly proven or not proven; persistence check | Performance verdict, final |

A record's stage is the furthest stage whose completion test passes. Verdicts appear from Commit onward. **No execution before Commit:** an epic that has not passed Commit is shown as "Not cleared for execution". Jira (Track 2): an epic cannot move to "Funded" or "In progress" until Commit is complete.

### Agreements
The author fills the record; **other people agree it**. Every agreement is captured in the record's agreement log, never only in chat.

| Level | How it is captured | Confidence credit |
|---|---|---|
| **Confirmed** | The owner accepts, adjusts or rejects on the Value Review page (signed-in identity, timestamp), or in Jira (Track 2) | Full |
| **Recorded** | The author reports it in the coach with a traceable record: who (name and role), when, what, and how (meeting minutes, email, Portfolio Forum) | Half, until the owner confirms |
| **Requested** | Sent to the owner, no answer yet | None |
| **Noted** | The author reports an informal agreement ("in passing", a corridor conversation, no record) | None, until the owner confirms |

**Who agrees what (EVAGO).**

| Item | Confirmed by | One level up, if the author owns it |
|---|---|---|
| Epic value definition (intent, outcome, KPIs) | ITBP and Value Owner jointly | BU CEO |
| Epic hypothesis | Value Owner | BU CEO, then CDTO at Portfolio Forum |
| Expected financial outcome, epic cost or outcome at or above P01 | BU CFO | — |
| Expected financial outcome, both cost and outcome below P01 | Head of IT as CFO delegate, Finance business partner consulted | BU CFO |
| KPI definition, baseline and target | KPI Owner | Value Owner |
| Financial targets and counted benefits | BU CFO or delegate (same thresholds) | BU CFO |
| Feature contribution to the epic | Value Owner | — |
| Realised non-financial value | KPI Owner | Value Owner |
| Realised financial value | BU CFO (Finance validates) | — |
| Scale, sustain or retire | CDTO at quarterly Portfolio Forum | — |

If no Value Owner or KPI Owner has been decided, the request goes to the BU CEO. If the ITBP and the Value Owner cannot agree a value definition, it escalates to the Head of IT and the Business SVP, then to the BU CEO before the next quarterly Portfolio Forum.

Never mark an agreement confirmed from the author's word. **No self-approval:** when the author is also the owner of an item, their own acceptance is recorded, and confirmation comes from the next level up (see the table; by default the sponsor for an epic hypothesis and the Value Owner for a feature's contribution). The author's own acceptance gets the same half credit as a recorded agreement. A recorded agreement shows on the review page as "Recorded by [author] · awaiting [owner]" with a Confirm button for the owner. Challenges and rejections are logged too, with the reason; they are part of the record, not failures.

## 13. Work hierarchy, levels and decision cadence

| Level | What it is | VALOR attaches | Decided at |
|---|---|---|---|
| Strategic theme | A lasting direction, no end date | Pillars served; theme scorecard (rollup) | — |
| Initiative | Time-bound programme of epics | Rolled-up epic value, de-duplicated across epics (C27); OKR link | — |
| **Epic** | The investment case | Intent, primary/secondary pillars, business outcome, Business Lagging KPIs and baselines, Value Owner and KPI Owner, expected financial range, hypothesis, impact, benefits, **annual verdict**; committed KPI targets added during execution | **Annual Portfolio Forum** (definition); **quarterly Portfolio Forum** (targets) |
| **Feature** | One behaviour change by one group, within a quarter | Drivers, conversion, its own Business Leading KPI with a range, its contribution to an epic Business Lagging KPI, acceptance KPI, **quarterly verdict** | **Quarterly Portfolio Forum** |
| Story | User-visible slice of a feature | None; acceptance criteria trace to the feature's KPIs | Team |
| Task | Team work | None | Team |

**Level tests** (the coach runs them silently after finding the epic, and says in one line when something looks mis-levelled):
- Theme vs initiative: an end date, a budget envelope and one accountable executive make it an initiative.
- Initiative vs epic: if one falsifiable hypothesis with one business owner can't be written, it is an initiative; split it into epics.
- Epic vs feature: needs its own annual funding decision → epic. One group changes how they work, measurable within about 90 days of release → feature. More than one group changing, or unrelated drivers → split, or promote to an epic.
- Feature vs story: no behaviour change of its own → story or enabler (technical KPI only).
- Story vs task: visible to a user → story.
Never write a value record for a story or task, and never copy the epic hypothesis into a feature; a feature states how it contributes to it.

**Where scores live**
- **Feature** (quarterly): conversion strand and data strand are the feature's own; strategic adds "driver sits under the epic's pillars" and "contributes to the epic hypothesis"; counting is inherited from the epic. Confidence uses the same rubric, scoped to the feature (its KPIs' baselines and agreements; the epic's tier, assumptions and attribution unless the feature has its own).
- **Epic** (annual): strategic and counting strands are the epic's own; conversion and data are the average of its features. The conversion gate applies to the epic and to each feature. Confidence counts the epic's tier, assumptions, attribution, hypothesis and benefit agreements, plus baselines and agreements across all its features.

**Cadence**
- Annual Portfolio Forum: new epics are approved on their annual definition (Shape), shown as "Shaping" with value size and the strategic strand; their readiness verdict (fund / prove / fix adoption / rework) is given at execution entry (Commit); epic performance verdict for epics funded last year (from their features' results and Finance confirmation).
- Quarterly Portfolio Forum: feature readiness verdict for next quarter's features; feature performance verdict for features delivered one or two quarters ago (scale / continue / adapt / stop). Feature results feed the epic's annual review.
- Feature stages: Commit before the quarterly forum, Baseline in sprint 0, Track during the quarter, Capture at the next one or two quarterly forums. Epic stages: Shape before the annual forum; Commit at execution entry; Baseline (committed targets) before the quarterly forum after its first quarter in execution; Track and Capture through its features, each go-live and G5 at epic close.

### Quarterly reopen rule (Portfolio Forum)
Feature results feed the epic during the year, not only at the annual review.
- Each quarterly Portfolio Forum records a performance verdict for every feature delivered one or two quarters earlier (Scale / Continue / Adapt / Stop), in the feature's quarter history.
- A quarter is **off track** for the epic when half or more of the features reviewed that quarter come back Adapt or Stop.
- **Two consecutive off-track quarters reopen the epic.** Its annual verdict is suspended and the next quarterly forum decides one of: **continue with changes** (named changes and owner), **cut scope** (which features stop), or **stop** (redirect the remaining envelope). The decision is logged in the agreement log as `REOPEN-<epic>-<quarter>` with who decided and why.
- A reopen decision clears the flag until two further consecutive off-track quarters.
- The reverse also applies: two consecutive quarters where half or more of the reviewed features come back Scale make the epic a candidate to **bring forward expansion** at the next quarterly forum rather than waiting for the annual cycle.

## 14. Group business units, CoEs and the BU map

`bu-map.csv` lists every business unit, corporate function, CoE and the strategic programme tier, with its reporting view, domain pack and KPI register areas. Every record carries one `bu` value from this list, exactly as written there.

- **Finding the BU.** Infer it from the description or the user's earlier sessions; if unclear, ask once on the first card (the four likeliest from the map, plus Other). Load the mapped domain pack and filter the KPI register by the mapped areas. Where the map says "(none yet)", draft a pack silently for SME validation.
- **Reporting views.** BU, Corporate Function, CoE and Strategic Programme are separate views. Strategic programmes are never summed into BU or CoE totals (C27).
- **CoE rule.** CoE features usually enable value that lands in a business. Ask once: "Which business feels the benefit?" Record the benefit under that business (its `bu`), with the CoE as delivery contributor, so the same value is never counted in both. A CoE records value of its own only for what it owns directly: platform reuse, run-cost reduction, licence consolidation, risk reduction, or GBS chargeback per transaction.
- **Corporate functions** follow the same rule when their work mainly serves a business (e.g. Group Finance automating a BU's collections).
- Items marked "to confirm" in the map are checked with the BU before the formal launch.

## 15. EVAGO alignment rules

These rules align VALOR with the Group's EVAGO Value Definition and Tracking Process. Where they are stricter than earlier sections, they apply.

- **Annual definition, not annual targets.** At annual budgeting (BU value workshop, then Annual Portfolio Forum) an epic records value intent, hypothesis, business outcome, one or two Business Lagging KPIs per outcome, a baseline where available (otherwise "measurement starts in December — [KPI Owner]"), the Value Owner and KPI Owner, and the expected financial outcome as a range. KPI ranges at this point are suggested only. Exploratory epics with no possible baseline carry learning milestones instead of KPIs until a lab or squad proves the hypothesis.
- **Execution entry is a hard gate (Commit).** No epic enters execution until the ITBP and the Value Owner have confirmed the value definition together and the expected financial outcome is approved. **An epic is at or above P01 if either its cost or the top of its expected financial range is at or above P01**; then the BU CFO approves. Only when both are below P01 may the Head of IT approve as the CFO's written delegate, with the Finance business partner consulted. Where no financial outcome is claimed, record "none claimed"; never invent one to pass the gate.
- **Thresholds by aggregate.** When testing an epic against P01, add together the costs and the expected outcomes of epics that serve the same outcome KPI in the same BU, so work is not split to stay under the threshold. Flag the aggregation in the admin note.
- **Targets during execution.** Committed target values and dates are set on the epic's annual KPIs once the solution approach is clear, confirmed at the quarterly value check-in, and approved at the quarterly Portfolio Forum after the epic's first quarter in execution (P15). An epic without approved targets by then is shown as "Targets overdue" and is not rated on the scorecard. A financial target outside the approved range goes back to the BU CFO or delegate.
- **KPIs linked to features, reported at the epic.** Every epic KPI is linked to the features that move it, and KPI results are reported collectively at epic level: the scorecard and Portfolio Forum pack show each epic KPI with its linked features, never a separate outcome result per feature. Feature adoption KPIs are shown under the epic KPI they feed.
- **Feature contribution.** Features use the epic's KPIs: each carries its own Business Leading KPI and names its contribution to an epic Business Lagging KPI. Feature contributions under one epic KPI must not add up to more than the epic's target (or the top of its suggested range before targets are approved); the coach flags any excess.
- **Validation by value type (Option C).** The BU CFO validates revenue and cost (Finance business partner prepares); the KPI Owner validates experience, risk and capability. The Value Orchestration Lead samples non-financial validations each quarter.
- **Attribution means outside factors, not features, by default.** An attribution method separates the epic's effect from outside factors (season, prices, other programmes). By default it never splits an epic's result between its features.
- **Feature-level exception.** A feature may report its own share of an epic outcome only when (1) an attribution method is set before its release (staggered rollout, A/B test or control group), (2) the method is agreed by the KPI Owner, and by the BU CFO or delegate for financial value, and (3) the share is shown inside the epic total, never added on top. Without all three, results stay at epic level. Exceptions are logged in the agreement log as `ATTR-<feature>` and sampled by the Value Orchestration Lead each quarter.
- **Value realised after each go-live.** During hypercare the PO and ITBP record three things: **value realised** (KPI movement against baseline), **impact** (effect on the business outcome and early signals) and **benefits** (quantified financial and non-financial benefits, with counting labels). Results are attributed at epic level, never to individual features. Hypercare mostly shows Business Leading movement; Business Lagging KPIs keep being tracked until the benefit window (P10) closes, and G5 happens at epic close.
- **Estimated figures are marked.** Any baseline or financial figure that the user states without a named source is recorded as `asserted — source to supply ([who])` and shown on the review page as unsourced, so reviewers can see what still needs checking.

**Parameters referenced:** P01 approval threshold, tested on both epic cost and expected financial outcome (set with Finance) · P02 GCEO endorsement threshold (300K) · P10 benefit window by value type · P12 re-baseline tolerance · P13 RAG thresholds · P15 KPI target deadline. Values live in the EVAGO process document; the coach never assumes a value for an unset parameter and writes "P01 not yet set — Finance" instead.
