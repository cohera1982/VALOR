---
name: valor-value-pathway
description: VALOR specialist that maps a feature or epic to value pillars and drivers and builds the value pathway (capability, required operational change and its owner, outcome, impact, value), writing the formation and conversion sections of the VALOR value record. Called by valor-orchestrator or valor-value-coach; use directly when a practitioner asks for driver mapping, a value hypothesis or the conversion pathway.
---

# VALOR Value Pathway

*VALOR is the background intellectual property of Rajaraman Kannan, licensed through Cohera Labs Pty Ltd.*

Owns the **`formation`** and **`conversion`** sections of the Feature Value Record (`references/feature-value-record.md`). Read `references/valor-core.md` first (§1–§4, §9 hypothesis, §10 impact, §13 levels). Reads `context`; writes nothing else.

## The idea this skill protects
Value is lost at **conversion** more often than at formation. A feature that ships without the operational change it depends on produces no value. Every pathway names the change and the business role that owns it.

## Procedure

### 1. Value intent
One sentence: what this is for, in business terms. Not the feature restated.

### 2. Pillars and drivers (`references/driver-register.csv`; IDs only from it)
- **Epic:** one primary pillar and at most one secondary pillar, and only when a feature driver or epic KPI sits under it; a pillar with nothing under it is dropped.
- **Feature:** one primary driver (where most value lands), up to two secondary drivers, each with a one-line role. Drivers must sit under the epic's primary or secondary pillars.
- **P05 trap:** P05 is primary only when the digital, data or AI capability is itself the value. If the capability serves an operational outcome, the primary driver sits with that outcome; P05 is at most secondary.
- **Watching, not doing (C36):** for dashboards, control towers and monitoring, the driver is the operational lever the changed decisions move, usually P02-D01 or P03-D01 (P03-D04 only for executive decisions; P05-D05 only when analytics is the product), never the outcomes of the features being watched (valor-core §2, P05 trap).
- Record `driver_rationale` in two lines: why this driver, and what was rejected.

### 3. Pathway (five links, none restating the previous one)
| Link | Test |
|---|---|
| capability | What the feature makes possible |
| required_operational_change | Who does what differently, when; named group |
| change_owner | A business role accountable for the change happening (not the delivery team) |
| operational_outcome | Measurable change in the process |
| stakeholder_impact | Who is better or worse off, by impact category (valor-core §10), including anyone made worse off |
| enterprise_value | Value category (CS, CA, CR, RV, MG, WC, RR, NF); money only through economics |

### 4. Adoption, dependencies, risks
- `adoption_conditions`: what must be true for the change to stick (training, policy, incentives, kiosk for staff without phones…).
- **Third-party choice:** if conversion depends on drivers, customers, patients, brokers or suppliers choosing, flag that an acceptance KPI is needed (C29).
- **Value concentration vs adoption (C30):** which group holds most of the value, and is it the hardest to bring along? If yes, name it as the crucial link and propose a design response or an open question with owner.
- `dependencies`: other features, data, policy, people. Value that silently depends on another feature is a Major finding (C20).

### 5. Assumptions
Each assumption that the headline benefit rests on: statement, status (untested · evidenced · disproved), and a test. Trade-offs the user didn't pick become assumptions or decisions with owners, never dropped.

### 6. Epic hypothesis (epics only)
"We believe [change, naming its features] will [move KPI by suggested range] within [horizon], because [behaviour change]. If that holds, [value KPI] will [move]." Plus a falsifier: "We'll know we're wrong if…". Ranges come from valor-benchmark-alignment and are labelled suggested or benchmarked. A feature never copies the epic hypothesis; it states how it contributes.

## Output
`formation` and `conversion` YAML, and the strand inputs for scoring: strategic links (intent linked to pillar · drivers under epic pillars · falsifier stated · for features, contributes to the epic hypothesis) and conversion links (behaviour change named · owned by business role · adoption risk addressed), each scored 1 / 0.5 / 0 / null. The two KPI links of the conversion strand come from valor-measurement-contract.

## Never
- Use a driver ID not in the register, or two primary drivers.
- Name the delivery team as change owner.
- Count the same benefit under two drivers (a secondary driver is contribution, not a second benefit).
