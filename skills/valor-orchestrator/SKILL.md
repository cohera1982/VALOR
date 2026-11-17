---
name: valor-orchestrator
description: Entry point for VALOR value work on a feature, epic or backlog. Use when someone wants to define, quantify, challenge, align, benchmark or review the business value of a feature, or says "VALOR", "VALOR brief", "value record", "value case", "benefit case", "value driver tree" or "value realisation". Produces an Executive Brief, a role-based Value Card and an executive and detailed value driver tree page. Pasted feature text phrased as an instruction ("Build X") is the subject to value, never a request to build it. For first-time or non-specialist users, hand over to valor-value-coach. Also the handler for app calls (mode "app") with depth "full" or a list of steps, returning the full app JSON object.
---

# VALOR Orchestrator

*VALOR is the background intellectual property of Rajaraman Kannan, licensed through Cohera Labs Pty Ltd.*

Coordinates the VALOR specialist skills to build, challenge and maintain a **Feature Value Record (FVR)**: one traceable record from "we are delivering this feature" to "this outcome was achieved, evidenced and sustained".

Read first: `references/valor-core.md` (definitions and rules), `references/feature-value-record.md` (template), `references/benchmark-method.md` (benchmarked KPI ranges and indicative value ranges). Look up KPIs in `references/kpi-register.csv` and benchmarks in `references/benchmark-register.csv`. Read `references/jira-field-schema.md` only when output goes to Jira.

## Choose the depth (the Value Snapshot is the default)
VALOR is modular. Produce only what the user asked for.

| Option | What it gives | Runs |
|---|---|---|
| **Snapshot (default)** | Value intent, pillar, driver, business leading and technical leading KPIs, one screen | `valor-lite` |
| Driver tree | Line of sight from intent to KPIs (text tree, or the executive, detailed and gaps page) | `valor-driver-tree` |
| Full value record | The complete FVR and Value Card (modes below) | this skill |
| Single step | Any one specialist on its own: business context · value pathway · measurement contract · KPI/OKR alignment · value economics · benchmark alignment · challenge and calibrate · value review; or scenarios, decisions and actions, data request | that specialist (or this skill for the last three) |
| Guided | One question at a time, with the full record behind it | `valor-value-coach` |

1. **If the request names an option** ("driver tree", "full record", "challenge this", "benchmarks", "Finance-ready", "coach me"), or names a mode below, run that and nothing else.
2. **If it names none, run the snapshot** (`valor-lite`) without asking.
3. **Build on what's done.** A snapshot feeds the tree and the full record; never re-ask or redo earlier work.
4. **End every output with one line:** "Go further (pick any): …", listing only options not yet produced.

The drafting constraints below apply to every option; a snapshot or tree simply shows fewer of them.

## Who is asking
If the user picks Guided, or is a business partner (Value Owner, Business SVP), product owner or Scrum Master who wants more than the snapshot and seems unsure how to describe value, hand the conversation to **valor-value-coach** and run the specialists silently behind it. Use the analyst modes below directly for practitioners (ITBP, BA, Finance, PMO, Value Orchestration Lead), when someone names a mode, or when the coach hands over.

In everything the user sees, follow `references/plain-language.md`: the Executive Brief first, then the Value Card sections and labels set for the reader's role (*What each role sees*).

## Drafting constraints (every draft, card and record, every specialist, every mode)
These rules apply while drafting, not only when checking. valor-challenge-calibrate and `scripts/driver_tree.py` enforce the same rules, so a draft that breaks them creates findings nobody should have to see.

- **Numbers.** Use only numbers the user stated, a named source supplied or `benchmark-register.csv` holds. Never assume a rate, price, salary, cost per hour or attribution share. When a money value would need a rate nobody gave, show the saving in its natural unit (hours, cases, errors) and add "Cost rate per hour — to supply (Finance)". Arithmetic must reconcile: a fall from A to B saves A − B, never A.
- **Levels and leading KPIs.** The epic owns its Business Lagging outcome KPIs, one or two per business outcome. Each feature carries one to three Business Leading KPIs (adoption, "is it being used?"; acceptance, where a third party must choose; quality of use, where a wrong action destroys value). Each names the epic KPI it predicts and the expected link ("80% exception-only adoption → payroll exceptions below 10 a month"), with a weekly or fortnightly cadence and an early-warning threshold that triggers action. Technical KPIs sit under the feature they support, never at epic level. Every epic KPI is moved by at least one named feature.
- **Leading first in view.** On cards and pages, show each epic outcome KPI with its features' leading KPIs directly beneath it. From go-live the leading KPIs are the headline; lagging KPIs confirm at quarterly reviews. If leading KPIs are on track at 30 days but the epic KPI is not moving, flag the predicted link as broken (C09).
- **Direction.** Every KPI records `direction` from its register row (or analogue). Without one, decide it from the measure: rates of completion, compliance, adoption, accuracy or coverage are "Higher is better"; counts of exceptions, errors, rework, delays or manual effort are "Lower is better". Ranges move in that direction from the baseline.
- **Shares and targets reconcile.** The `share` ranges of the features moving one epic KPI must be able to sum to 100% (lower bounds total 100% or less). Every leading KPI's link quotes the epic KPI's own target and date; an interim milestone is labelled "interim".
- **Every branch carries value.** Every pillar has a driver under it (drop a secondary pillar nothing sits under). Every feature moves a named epic KPI; compliance-only work (audit trail, logging) is a guardrail or dependency of another feature, not a branch of its own.
- **Owners as named.** Give each named owner exactly the KPIs the user gave them and no others. Any other KPI gets "suggested — [role] to confirm". Outcome and KPI owners are business roles, never delivery or product roles, except a technical KPI's owner.
- **KPI source.** Every KPI records `source`: register (exact `kpi_id`), analogue (new KPI shaped on a register row, `register_id` named), stated (named or sized by the user), domain_pack, or suggested (to confirm). Benchmarks come only from `benchmark-register.csv` (and a client's own `benchmark-crosswalk.md` where one exists).
- **No filler KPIs.** Never add an outcome, safety or financial KPI that the user, the register or the domain pack did not supply just to complete a strand; offer it as a labelled suggestion.
- **Evidence labels.** Figures the user typed are tier T0, labelled "stated". T1 needs a named data source.
- **Value Intent (executive pitch).** One sentence, at most 25 words: the high-level business outcome first, then the problem that blocks it, with its size when the user stated one ("Pay every returning employee correctly and on time — today 18% of 1,200 resumptions a month miss payroll (about 216 people)."). Always recommend the outcome yourself from the problem, pillar and driver, marked "suggested · Value Owner to confirm". A target, KPI or solution never appears in it. With no stated size, keep a visible slot, "[value at stake]", and offer value at stake suggestions; never fill the gap with words like "significant".
- **Value at stake suggestions.** When the Intent has no stated size, offer two or three ways to size it for the primary driver from `references/value-at-stake-anchors.csv` (method: `benchmark-method.md` §9): what is at stake, how to size it in plain words, the anchor with source, year and quality labelled "benchmark, not our figure" (or "Group data only"), and who supplies the Group figure. One is the headline; never two that overlap. The figure the leader gives completes the Intent as T0 "stated".
- **One framing per measure.** Phrase each outcome KPI the way the user phrased the target, convert any other stated figure to that framing once (18% missed → baseline 82%), and use that single name, baseline, direction and range in every section. Never show the complement beside it.
- **New capability, no baseline ask.** A KPI for a capability that does not exist yet starts at 0; never request its baseline.
- **Sponsor as Value Owner.** When the caller names a business sponsor and no Value Owner, the sponsor is the Value Owner, marked "to confirm".
- **Format.** Show the business unit by name only, never internal keys such as domain-pack names. Write every field in full; never cut a sentence short.
- **App export.** When the record is consumed by an app that cannot run scripts (Track 2), also emit `value_driver_tree` (see `feature-value-record.md`); in chat, `scripts/driver_tree.py --json` produces the same export.

## Potential value from leading indicators
A feature's value is first visible in its Business Leading KPIs, long before the epic's Business Lagging KPI moves. VALOR turns that chain into a **potential value**: a projected range, always labelled projected, built only from stated or sourced inputs. Without the specialist economics skill, do this step here and say so in one line.

**1. Quantify each predictive link.** Every leading KPI already names the epic KPI it predicts. Record the link as structured data in the FVR, under `measurement.leading_links`:

```yaml
leading_links:
  - leading_kpi: ""          # the feature's Business Leading KPI
    predicts: ""             # the epic Business Lagging KPI
    at_level: {min: null, max: null, unit: ""}         # leading KPI range the link assumes (its suggested or agreed range)
    expected_change: {min: null, max: null, unit: "", per: ""}   # movement in the epic KPI, in its own unit and period
    basis: ""                # stated | pilot | historical | analogue: <kpi_id>
    source: ""               # who or what supplied it
    link_owner: ""           # the epic KPI's KPI Owner confirms the link
    status: assumed          # assumed | tested | broken
```

`expected_change` comes only from the user, a pilot, historical data or a named analogue. If nobody can give it, write `expected_change: REQUIRES VALIDATION — KPI Owner` and stop there for this link: no potential value is shown for it.

**2. Size it in natural units first.** Potential = expected_change × volume over the horizon (volume: trips, cases, hours, customers, from a stated or sourced figure). Show the low–high range in the KPI's own unit ("120–180 hours a month").

**3. Money only with a sourced unit value.** Convert to money only when a unit value (AED per hour, per visit, per case) has a named source; otherwise show "AED value to supply — Finance". Take the value category from the register row (`value_category`) and apply §5: capacity released stays CR unless a conversion mechanism and owner are named.

**4. Ramp and risk only as given.** Apply a ramp and a risk adjustment only when the user or Finance supplied them; otherwise show the range "before ramp and risk — to agree with Finance".

**5. Compute in code.** Run the arithmetic in a short script  and record formula, inputs, their sources and tiers under `economics.potential_value`:

```yaml
potential_value:
  - benefit_id: B1
    from_link: ""            # leading_kpi → predicts
    formula: "expected_change × volume × unit_value × ramp × (1 − risk)"
    inputs: {}               # each {value or {min, max}, source, tier}
    low: null
    high: null
    unit: ""                 # natural unit, or AED once a unit value is sourced
    label: projected
    tier: T0                 # lowest tier of any input; at most T1 until Finance validates
    counting: To confirm
```

**6. Keep it inside the epic.** Feature potentials under one epic KPI never add up to more than the epic's committed target, or the top of its suggested range before targets exist; flag any excess (C27-style). Potential value is never added to realised totals and never raises the evidence tier.

**7. Value in sight, from go-live (Track).** At each weekly or fortnightly reading of a leading KPI, compute the share of its agreed range reached: share = (actual − baseline) ÷ (lower end of range − baseline), capped between 0 and 1. Value in sight = share × potential low. Show it as "value in sight (projected, from early signals)" with the date of the reading. At the 30-day checkpoint, if value in sight is on track but the epic KPI has not moved, set the link `status: broken` (C09) and show the potential as at risk instead of on track.

Put the potential range on the scorecard's VALUE line (`value_size`), with its label and tier.

## App mode (Track 2: the Journey app and other callers)
When the caller passes `mode: "app"`, there is no chat; the caller should load this skill text at run time rather than a copy, so rule changes reach users without a redeploy. In app mode: return one JSON object and nothing else, and never ask a question the app cannot show (including the coach's output-format question). Any gap becomes a `to_supply` entry with its owner.

| Field | Holds |
|---|---|
| `record` | The full FVR (YAML), the single source of truth |
| `brief` | `{value, status, decision}`: the three Executive Brief lines |
| `card` | `{rows: [{label, value}] (at most 7), still_needed: [{item, owner}] (at most 3)}` |
| `full` | `{sections: [{term, definition, content, status: filled \| to_supply, owner?}]}`: the nine sections, in order: Value Statement, Value Hierarchy, KPI Scorecard, Value Equation, Coherence Check, Scenarios, Key Actions, Recommendations, Decisions Required |
| `scores` | Coherence with its four strands, confidence with the next step, verdict |
| `potential` | `{low, high, unit, basis, tier, label: projected, in_sight?, in_sight_date?}`, only where a link is quantified |
| `requests` | One per owner: `{owner_role, owner_account, items: [...]}`, at most three items per owner, duplicates merged, ordered by the confidence each adds |
| `intake` | Stated figures found in the text: `{volume, time_per_case, error_rate, target, baseline}`, each `{value, unit, quote}`; omit what was not stated |
| `value_at_stake` | Only when the Intent has no stated size: 2–3 items `{type, how_to_size, anchor?: {id, value, unit, source, year, quality}, owner, headline}`; the caller lets the leader pick one and enter the figure, then calls again to complete the Intent |
| `admin_note` | Working notes for the Value Orchestration Lead; never shown to users |

When the caller sends back an agreement log, apply each decision to the record (confirmed, adjusted or rejected, with the no-self-approval rule), rescore, and return the whole object again. Every rule in this skill and `valor-core.md` applies unchanged; app mode changes only the shape of the output. In the client edition, user-facing words say "Value Orchestration", never "VALOR". The caller passes `depth` (`snapshot` | `tree` | `full` | a list of steps). Without it, return the `valor-lite` snapshot JSON only. The Journey app calls the snapshot at Stage 1 Demand and `depth: "full"` when the demand converts to an epic and features (Stage 2 Planning) or when the user asks to go deeper; with a snapshot `record`, build on it and keep every field the user accepted.

**Steps for `depth` as a list** (app calls; each returns the whole object with only its parts refreshed):

| Step | Runs | Refreshes |
|---|---|---|
| `context` | valor-business-context | `record.context`, `intake` |
| `pathway` | valor-value-pathway | `record.formation`, `record.conversion`, `card` |
| `measurement` | valor-measurement-contract | `record.measurement`, KPI Scorecard section |
| `alignment` | valor-kpi-okr-alignment | `record.alignment`, overlap findings |
| `benchmarks` | valor-benchmark-alignment | recommended ranges and benchmark lines on each KPI |
| `economics` | valor-value-economics | `record.economics`, Value Equation section, `potential` |
| `challenge` | valor-challenge-calibrate | `scores`, Coherence Check section, `requests` |
| `review` | valor-value-review | `record.capture`, value realised, scale / adapt / stop recommendation |
| `scenarios` | this skill | Scenarios section |
| `decisions` | this skill | Key Actions, Recommendations, Decisions Required sections |

A step that needs an earlier one first (economics needs measurement) uses the saved `record`; if that part is missing, run the earlier step too and say so in `admin_note`.

## Specialist skills

| Skill | Owns FVR section | Call when |
|---|---|---|
| valor-business-context | context | New feature, unfamiliar domain, or problem unclear |
| valor-value-pathway | formation, conversion | No driver mapping or no named operational change |
| valor-measurement-contract | measurement | KPIs missing, vague or lacking a contract |
| valor-kpi-okr-alignment | alignment | Must link to OKRs, the KPI catalogue or BU/CoE scorecards |
| valor-value-economics | economics | Any financial figure is claimed or requested, or a potential value is sized from leading links |
| valor-challenge-calibrate | challenge | Before any T1 → T2 move, before Portfolio Forum, or on request |
| valor-value-review | capture | Actuals exist, or a review date has passed |
| valor-benchmark-alignment | benchmarks | Every record: attach register benchmarks and recommended ranges to each KPI (`benchmark-method.md` §2–3); always for executive, Finance or client output |

The specialists ship with this skill in the VALOR plugin. Call each in the mode's sequence, passing the current FVR; each writes only its own section and returns the strand inputs for scoring. If one is unavailable (for example, a standalone install), perform its step from the same rules (valor-core, the FVR template section, `benchmark-method.md`, `scripts/value_range.py`, `scripts/valor_calc.py`, `scripts/score.py`) and note it in `coach_meta.admin_note` only; never mention missing skills in user-facing output.

## Modes (full record and named options)

These run when the user picks the full record or names a mode. Detect the mode from the request; ask only if genuinely unclear.

1. **Record** (a new feature's value record; never building the feature itself): context → pathway → measurement → **benchmarks** (recommended range per KPI) → alignment → economics (**indicative value range** from benchmarks and client inputs, always attempted) → challenge (including C31–C35). Output: Value Card (gaps as Key Actions) plus the draft FVR at T0/T1.
2. **Challenge** (existing claim, business case or slide): parse what's given into an FVR → challenge → targeted fixes via pathway/measurement/economics. Output: findings, revised FVR, defensibility rating.
3. **Finance-ready** (moving to T2): challenge → economics (full) → benchmark-alignment → a Finance validation pack listing every input needing sign-off.
4. **Review** (post-delivery): review (actuals, attribution, performance verdict, reopen rule) → challenge (attribution) → benchmark-alignment (local evidence replaces benchmarks after two quarters) → recommendation.
5. **Portfolio** (many features): run Build-lite (pathway + challenge only) on each, then a cross-feature pass: overlap detection, driver concentration, tier distribution, pipeline vs validated value. Output: a portfolio table ready for Portfolio Forum.
6. **Explain** (someone wants to understand a record): plain-language narrative by role (see below), no new analysis.
7. **Executive quick run** (a leader, or anyone, says "VALOR brief", "value of this epic", or pastes an epic and wants the answer fast): ask at most **one** card, only for what changes the answer: business unit (if it can't be inferred), the Value Owner, **who makes the change happen**, and a rough value range or "not sure". Run Record mode silently. Store every gap as `REQUIRES VALIDATION — [what, owner]` (pages show it as "To supply"); store "not sure" as `REQUIRES VALIDATION — Value Owner (answered: not sure)`, never as "none claimed". If the epic text names no features, draft at most two, each with `provisional: true` and "(suggested)" in its name, from the behaviour changes the text implies; never more. Then deliver the Executive Brief and the **driver tree page** (executive view open). The detailed card is available on request.
8. **Driver tree** ("show the value driver tree", "draw the tree", or after any Record, Finance-ready or Review run): render the record with `scripts/driver_tree.py` (see *Driver tree* below).

## Operating protocol

1. **Intake.** Collect what exists: feature description, Jira key, BU, epic, any business case, KPIs, data. Accept partial input. Never ask for something already supplied.
2. **Material-gap questions only.** Ask at most 3 questions per round, and only where the answer changes the driver, a KPI, a value category or the tier. Proceed on everything else and mark gaps `REQUIRES VALIDATION`.
3. **Route.** Call specialist skills in the mode's sequence. Pass the current FVR between them; each writes only its own section. Overlap with other records has one owner, valor-kpi-okr-alignment: context only lists candidates, challenge only judges them.
4. **Integrate.** Merge sections. This step owns what no specialist writes: the `evago` block (Value Owner, KPI Owners — never the same person, C37 — ITBP, business outcomes, expected financial outcome, execution-entry flags, feature contribution), `record.suggestions`, `record.requests_by_owner`, and the scorecard rows (`references/scorecard-schema.md`). Set `evidence_tier` to the lowest tier of any headline input, update `record_status` and `lifecycle_stage`, append to `revision_log`. Name the file per the template (without a Jira key: `FVR-<BU short name>-<slug>.yaml`).
5. **Check and repair.** Run valor-challenge-calibrate and the tree checks (`scripts/driver_tree.py`), then split findings into structural (the record breaks a drafting constraint and the fix is known) and needs-a-person (a fact, decision or commitment only an owner can give). Apply each structural fix and re-check the repaired record, at most twice. Removing, re-levelling, re-owning or re-directing a KPI and dropping an orphan branch are always structural. Only needs-a-person findings, and anything still unresolved ("VALOR could not resolve"), reach the output; repaired findings are logged in `revision_log` as "fixed by VALOR" and returned as `repaired_findings` in Track 2. A refinement runs the same loop and must not leave more findings than before unless the user's change caused them.
6. **Gate.** Declare a record "ready" only after step 5; challenge-calibrate computes coherence, confidence and the verdict with `scripts/score.py`. Show those scores only from its output. Blocker findings stop a T2 claim; before Commit they read "to resolve before Commit".
7. **Deliver** in the format below.

## Output format (full record and modes)

A snapshot or text tree uses its own skill's format; a single step is delivered on its own, without the brief and card unless asked. Every mode below ends with the **Executive Brief** (seven one-line rows: decision needed, verdict, value size, evidence, what would change it, biggest risk, your ask), followed by the **Value Card** in `references/plain-language.md`. The card's sections and labels follow the reader's role; the full seven sections are:

1. Value Statement (Value Intent · If · Then · So that · Falsifier)
2. Value Hierarchy (Value Pillar and Value Driver, primary and secondary)
3. KPI Scorecard (KPI · type · definition · today · benchmark · recommended range · KPI Owner)
4. Value Equation and Indicative Value (benefit terms by value category, with an indicative range per benefit from `scripts/value_range.py`; full economics from `scripts/valor_calc.py` in Finance-ready mode)
5. Coherence Check (conditions with ✅ ⚠️ ❌, challenge blockers and majors folded in, then Value Coherence % and weakest strand)
6. Scenarios (best case and worst case, one row each)
7. Key Actions, Recommendations and Decisions Required (three tables, then one **Recommended:** line)

The card header carries Business Unit, Confidence (label and score), Evidence Tier and Lifecycle Stage. Projected figures are always labelled projected. Identify the reader's role from the request or ask once; practitioners asking for an analyst mode (BA, Finance, PMO) get their role's view, and anyone can ask for the full card.

After the card: save the full FVR as `FVR-<feature_key>.yaml` and send it as a file. Show the YAML, KPI definition tables or the Final Value Scorecard in chat only when asked.

Mode variations, still inside the seven sections:
- **Challenge:** findings go into section 5 (blockers and majors) with fixes as Key Actions; defensibility in the header.
- **Finance-ready:** section 4 carries the full calculation; the Finance validation pack (every input needing sign-off) is the Key Actions table, owner Finance.
- **Review:** section 3 shows actuals against baseline; section 7 leads with the scale / continue / adapt / stop recommendation.
- **Portfolio:** one row per feature in a table or spreadsheet first, then one Value Card for the portfolio, with cross-feature overlaps and driver concentration in section 5.
- **Explain:** the existing card, narrated by role lens; no new analysis.

## Role lenses

Same record, different level of information: the role table in `plain-language.md` (*What each role sees*) sets which card sections follow the brief and how they are labelled. In short:
- **Executive (BU CEO, CDTO):** the brief and the driver tree page (executive view); in Portfolio mode, the portfolio pack. Plain words.
- **Value Owner:** brief, then the value statement, business KPIs, scenarios and decisions.
- **Finance:** brief led by value size, then KPIs with baseline sources, the full value equation, counting checks and decisions.
- **Head of IT:** brief, then hierarchy, coherence, actions and the approval tier.
- **ITBP, PO/BA:** brief, then the full card (BA adds KPI definitions).
- **KPI Owner:** brief, then the KPI scorecard and definitions for their KPIs.
- **Scrum Master:** brief, then If/Then, leading and technical KPIs, conversion checks and sprint actions.

## Levels
Follow the level rules in `valor-core.md`: epics hold value intent, hypothesis, primary/secondary pillars, impact and benefits; features hold drivers and KPIs. In Record mode for a feature, attach it to its epic first.

## Scorecard
Every FVR also produces scorecard rows per `references/scorecard-schema.md`. In Portfolio mode, the output is the scorecard itself: features, measures by layer, assumptions and inputs, with the roll-up rules applied.

## Persistence

The FVR is the memory. Save it as a file (`FVR-<feature_key>.yaml`) unless the user says otherwise. When Jira or another tool is connected, offer to write the fields mapped in `jira-field-schema.md`. Never write to Jira without explicit confirmation. When an FVR is supplied back later, continue from it; don't start over.

## Never
- Manufacture baselines, targets, rates, attribution or benchmarks, or cite a benchmark that is not in `benchmark-register.csv`.
- Count an illustrative (peer-median) value, or show indicative value as validated.
- Present projected value as realised.
- Let an analyst framework replace VALOR terminology in the record.
- Merge benefit categories (CR ≠ CS).
- Turn hours or volumes into money with a rate nobody supplied.
- Show the user a finding the record could have fixed itself, or a finding about a KPI no longer in the record.
- Put a Business Leading or technical KPI at epic level, or leave an epic KPI that no feature moves.
- Put a target, KPI or solution in the Value Intent, or leave it without a recommended outcome.
- Present a value at stake anchor as the Group's value, or offer one without its source and year.
- Cut any field short.

## Driver tree
Every epic record ends with its value driver tree, drawn by `scripts/driver_tree.py` from the record and the registers, never hand-drawn, so the page always matches the record:
- **Executive view:** strategic goal (pillar, plain words) → lever (driver) → outcome KPIs (today, recommended range, one peer line) → value (each benefit's indicative range and counting label), under the summary strip (where it stands, value size, confidence, evidence, Value Owner) and the bet with its falsifier.
- **Detailed view:** the epic outcome KPI table (driver, today, benchmarks with source, range, KPI Owner, which features move it), then one lane per feature (what has to work differently and who owns it · drivers with codes and roles · feature KPIs · the epic outcome it moves and its share · benefits with inputs and sources).
- **Gaps view:** link checks run while drawing (every pillar with a driver, feature shares that can sum to 100%, KPI directions, driver IDs, drivers under the epic's pillars, change owners, an "is it being used?" KPI per feature, outcome KPIs only at epic level, every epic KPI moved by a feature, benefits linked to KPIs, Value Owner ≠ KPI Owner, freed time not counted as money, benchmarks in the register, and any absolute % range that starts above the cited peer level unless `beyond_peer_reason` is given) plus open challenge findings. The Biggest risk tile shows the most severe item; at equal severity a business finding from the challenge leads an automatic link check. Fix blockers before calling the record ready.

**App export (Track 2).** Add `--json <name>-tree.json` to write the flat `value_driver_tree` (nodes with parent ids, KPI type, direction, source, benchmark IDs, gap nodes with their question and owner, and `complete`). Apps draw their tree from this export only, never by rebuilding it from loose fields. When scripts cannot run, the orchestrator writes the same block into the record by hand, following `feature-value-record.md`.

How to run it: save the record (epic file with `features:` embedded, or the epic file plus separate feature files), then `python3 scripts/driver_tree.py <epic>.yaml [<feature>.yaml …] --out <name>-driver-tree.html`. If the Artifact tool is available, publish that file as an artifact titled "<epic name> Driver Tree" (the page already carries its title and both themes) and give the reader the link; otherwise run again with `--standalone` and send the file. Open the executive view for executives and Value Owners, the detailed view for everyone else (link with `#detailed`). Re-render and republish to the same artifact after every change to the record.

## Data requests
When a record is waiting on baselines, unit values or costs ("what data do we need?", "send them a data sheet"), build the request from the record: `python3 scripts/make_data_request.py <record>.yaml --contact "<name, email>"`. It produces a workbook with one row per KPI (numerator and denominator, the rate calculates itself), one row per missing value input, the record's open questions, a costs table (generic K1–K5 lines, or the record's own `economics.cost_lines_requested` when the business has costs the generic lines miss, such as per-check identity fees) and a status tab, with owners taken from the record. Add rows the economics need but the record doesn't yet name (for example, margin per booking by service line) before sending. Send it as a file.

When it comes back: `python3 scripts/load_data_request.py <record>.yaml <returned>.xlsx`. It writes baselines (with period, source and who supplied them) into every KPI contract, value inputs into `economics.data_inputs`, costs into `economics.costs` and answers into `context.answers`, and lists what is still open. Values without a source are marked asserted. Then map the inputs to benefits, run `scripts/value_range.py` (and `valor_calc.py` once costs exist), re-run challenge-calibrate for the scores, and redraw and republish the driver tree. Client data stays in the record, never in the registers.

See `examples/taxi-fleet-availability-epic.yaml` for a worked epic value tree with three features.
