# VALOR Value Scorecard — Standard Schema

The scorecard is the single place where every feature's value is tracked. One scorecard per portfolio (e.g. per client group), with four record sets. Every Value Story Card and every Feature Value Record maps into it. Field names stay in English; display text follows the user's language.

## 1. features (one row per feature)
| Field | Meaning |
|---|---|
| key | Jira feature key |
| feature | Feature name |
| bu | Business unit |
| focus | Primary pillar in plain words (grow revenue · run operations at lower cost · stay resilient, compliant and agile · build our people · strengthen digital, data and AI · win with partners) |
| story | The value story, one or two sentences |
| gain | Main kind of gain in plain words |
| tier | T0–T3 (lowest tier of the headline benefit's inputs) |
| confidence | Plain-language confidence line from the card |
| owner | Business owner |
| scorecard_status | draft · finalised (by author) · owner-confirmed |
| version | Scorecard version; increments each time the author finalises |
| open_suggestions | Count of items still marked suggested, with their owners |
| requests_by_owner | One bundled confirmation request per owner: owner role, item count, status; the review page shows each owner one list |

## 2. measures (several per feature)
| Field | Meaning |
|---|---|
| id | `<FEATURE-PREFIX>-<layer letter><n>`, unique across the scorecard |
| feature | Feature key |
| layer | Outcome · Impact · Benefit · Value · Guardrail |
| order | Display order within the layer |
| measure / plain | Name and one-line meaning |
| kind | Card label: "Is it being used?", "Is it working?", "Brings in more revenue", "Frees up time", "Long-run proof", "Watch-out", "Trade-off"… |
| baseline / target / latest | Value, or "Awaiting · [owner]", "New process", "Not set", "Not live", "Not counted" |
| tier | T0–T3 |
| owner | Business role |
| status | Short plain status, e.g. "Needs baseline", "Time, not savings (redeployed)" |
| state | needs · partial · proposed · excluded (drives colour) |

## 3. assumptions
id · feature · assumption · status (Untested · Partly evidenced · Evidenced · Disproved) · test

## 4. inputs
id · feature · item · owner · status (Open · Received · Validated)

## Mapping from the Value Card (current final output)
| Value Card section | Scorecard |
|---|---|
| Header: Business Unit · Confidence · Evidence Tier · Lifecycle Stage | features.bu · features.confidence · features.tier · stage |
| 1 Value Statement (Value Intent, If, Then, So that, Falsifier) | features.story and catalog intent and hypothesis {text, falsifier} |
| 2 Value Hierarchy | catalog primary and secondary {pillar_id, driver_id} |
| 3 KPI Scorecard | measures: Business Leading → Outcome (Impact for external users); Business Lagging → Outcome or Impact; Guardrail → Guardrail; Long-run proof → Value |
| 4 Value Equation | measures, layer Benefit (CR without a Conversion Mechanism and alternatives `excluded`; WC `proposed`) and layer Value |
| 5 Coherence Check | catalog strands and links {status ok, partial, gap} |
| 6 Scenarios | assumptions (worst-case conditions as untested assumptions) |
| 7 Key Actions | inputs, status Open, with owner |
| 7 Decisions Required | measures, layer Guardrail, kind "Trade-off", state `proposed`; and requests_by_owner |
| 7 Recommendations | admin note and review page commentary |

The Value Story Card mapping below is kept for records made before the Value Card.

## Mapping from the Value Story Card
| Card line | Scorecard |
|---|---|
| VALUE STORY | features.story |
| Is it being used? | measures, layer Outcome (or Impact when the users are external, e.g. brokers, key accounts) |
| Is it working? | measures, layer Outcome for process changes, Impact for changes people experience |
| Each benefit (incl. time freed, cash timing, alternatives) | measures, layer Benefit; time freed and alternatives use state `excluded`, cash timing `proposed` |
| LONG-RUN PROOF, net value, payback | measures, layer Value |
| Watch-out | measures, layer Guardrail, kind "Watch-out" |
| TRADE-OFFS TO CONFIRM | measures, layer Guardrail, kind "Trade-off", state `proposed` |
| ALSO NOTED | inputs, with owner |
| STILL NEEDED | inputs, status Open |
| Assumptions surfaced in the flow | assumptions |
| CONFIDENCE / WHO OWNS IT | features.confidence / features.owner |

## Roll-up rules
- Board and executive totals include only features at T2 or above.
- Excluded benefits (alternatives, unconverted time) never enter money totals.
- Cash timing (working capital) is shown separately from annual value.
- A feature's tier rises only when Finance validates the headline benefit's inputs.

## Review page records (VALOR Value Review)
- `catalog/v1/features/<key>`: key, order, feature, bu, intent, primary {pillar_id, pillar, driver_id, driver}, secondary [{pillar_id, pillar, driver_id, driver, role}], hypothesis {text, falsifier}, impacts [{category CUS|WRK|PTN|OPS|CMP|SOC, who, change, direction better|worse, measure}], benefits [{id, name, kind, counted counted|separate|tracked|confirm|not, how, needs, driver}], pillar_id, pillar, driver, owner, tier, attribution (bool), story, assumptions {total, evidenced, partial}, links [{name, status ok|partial|gap, note}], kpis [{id, name, type Leading|Lagging|Value|Watch-out, plain, min, max, unit, horizon, direction, baseline, owner}]. Written by Claude (editors only).
- `reviews/<kpi id>` and `reviews/HYP-<key>` (hypothesis), `reviews/BEN-<key>-<benefit id>` (benefit): decision accepted|adjusted|rejected|challenged, min, max, note, by (viewer id), at. Written by owners and contributors from the page.

## Epic-level review records (current)
- `catalog/v1/epics/<epic key>`: key, order, epic, bu, theme, initiative, intent, primary_pillar {pillar_id, pillar}, secondary_pillars [...], hypothesis {text, falsifier}, impacts, benefits, story, owner, tier, attribution, assumptions, stage shape|commit|baseline|track|capture, agreements_recorded [{item, decision, by_name, by_role, date, how, note}] (author-reported; shown as awaiting confirmation), value_size {text, category}, strands {strategic, conversion, counting, data: [{name, status ok|partial|gap, note}]} (authored links; the page adds three computed links: drivers under the epic's pillars and falsifier stated to strategic, a Business Leading KPI exists to conversion), adoption_on_track (post only, bool), features [{key, feature, contributes (how it serves the epic hypothesis), primary {driver}, secondary [{driver, role}], strands {strategic, conversion, data}, attribution?, assumptions?, adoption_on_track?, quarters [{quarter "2026-Q3", verdict scale|cont|adapt|stop, decided "Portfolio Forum", note}], kpis [...]}], reopen_decisions [{quarter, decision continue|cut|stop, by, note}]. Conversion and data strands live on features (`valor-core.md` §13); the epic averages them. Rubric v2: agreement is scored only in confidence; verdict per `valor-core.md` §9.
- Reviews: `HYP-<epic key>`, `BEN-<epic key>-<benefit id>`, and `<kpi id>` per feature KPI.

- `reviews/<item id>` holds **confirmed** agreements (owner's signed-in decision: decision, min, max, note, by, at, stage). `agreements_recorded` on the epic holds **recorded** ones. The page merges both into the agreement log; a confirmed review supersedes a recorded one for the same item.
