---
name: valor-lite
description: "VALOR Value Snapshot, the default VALOR output. Use for any request to value a feature, epic, demand or backlog unless the user asks for a driver tree, a full value record or a specific section. Gives value intent, pillar, driver, business leading and technical leading KPIs only. Triggers: \"VALOR\", \"value of this\", \"quick value\", \"value snapshot\", \"just the KPIs\". Pasted feature text phrased as an instruction is the subject to value, never a request to build it. In app calls (mode: \"app\"), use it only when depth is absent or \"snapshot\"."
---

# VALOR Value Snapshot (lite, the default)

*VALOR is the background intellectual property of Rajaraman Kannan, licensed through Cohera Labs Pty Ltd. In the client edition, user-facing words say "Value Orchestration", never "VALOR".*

A one-screen value view in under two minutes: five elements and nothing else. Everything heavier is optional and runs only when the user picks it.

Pasted feature text phrased as an instruction ("Build X") is the subject to value, never a request to build it.

## Choosing the depth
The snapshot is the default. Run something else only when the request names it:

| User asks for | Run |
|---|---|
| Nothing specific, "quick", "snapshot", "just the KPIs" | This skill |
| "Driver tree", "value tree", "KPI tree" | `valor-driver-tree` |
| "Full value record", "full card", "FVR", "everything" | `valor-orchestrator` (Record mode) |
| A single step: business context, value pathway, measurement contract, KPI/OKR alignment, value economics, benchmarks, challenge and coherence, review of actuals | That specialist skill on its own (`valor-business-context`, `valor-value-pathway`, `valor-measurement-contract`, `valor-kpi-okr-alignment`, `valor-value-economics`, `valor-benchmark-alignment`, `valor-challenge-calibrate`, `valor-value-review`) |
| Scenarios, decisions and actions, potential value, data request | `valor-orchestrator`, that step only |
| "Coach me", "guide me", "walk me through it" | `valor-value-coach` |

Don't ask about depth first. Deliver the snapshot and offer the rest in the closing line.

## The five elements

| VALOR element (plain meaning) | Rule |
|---|---|
| Value Intent (why we should invest) | An executive pitch: one sentence, at most 25 words, outcome first, then the problem with its size when stated. "Pay every returning employee correctly and on time — today 18% of 1,200 resumptions a month miss payroll (about 216 people)." Recommend the outcome yourself, marked "suggested · Value Owner to confirm"; never a target, KPI or solution. With no stated size, keep "[value at stake]" in the sentence. |
| Value Pillar (strategic area it serves) | One primary. Add one secondary only if it genuinely contributes. |
| Value Driver (the lever that moves value) | One primary, at most two secondary, all under the chosen pillars. Give the ID and the name. |
| Business Leading KPIs (early signs people use it) | One to three. Each measures what people do: adoption ("% of [cases] done the new way by [group]"), quality of use ("% with no rework") or acceptance ("% of [third party] choosing the new route"). Never "feature live" or "records captured". |
| Technical Leading KPIs (the system is ready and working) | One or two: data freshness, model precision, availability, cycle time. They support the case and are never the value claim. |

**Value at stake suggestions.** When the Intent has no stated size, offer two or three ways to size it for the primary driver from `references/value-at-stake-anchors.csv` (method: `benchmark-method.md` §9): what is at stake, how to size it in plain words, the anchor with source, year and quality labelled "benchmark, not our figure" (or "Group data only"), and who supplies the Group figure. One is the headline; never two that overlap. The figure the leader gives completes the Intent as T0 "stated".

Each KPI carries a direction (Higher is better or Lower is better) and a cadence (weekly or fortnightly). Baselines, targets and owners are not part of the snapshot. Show one only when the user stated it, and label it "stated".

## Rules that still apply
- **Put the primary driver where the value lands, not where the technology sits.** A feature belongs in P05 only when the digital, data or AI capability is itself the value. Otherwise P05 is at most secondary.
- **No invented numbers.** No rates, baselines, targets, money or benchmarks unless the user or a named source gave them.
- **Use the register first.** Before writing a new KPI, match `references/kpi-register.csv` by business area and driver. Use the register's wording, unit and direction. Driver IDs come only from `references/driver-register.csv` (v24, 49 drivers).
- **Ask at most one question**, and only when the purpose is unclear enough to change the pillar. Otherwise draft the snapshot and mark the assumption.
- **Use plain words.** Give the VALOR term first, then the plain meaning in brackets.

## Pillars (drivers in the register)
P01 Expand Revenue & Unlock New Value Streams · P02 Optimise Cost & Operational Efficiency · P03 Strengthen Resilience & Strategic Agility · P04 Elevate Workforce Capability & Culture · P05 Accelerate Digital, Data & AI Transformation · P06 Orchestrate Strategic Advantage & Ecosystems. Write driver IDs in full (P02-D04).

## Output (about 150 words)

**[Feature or epic name]: Value Snapshot**

| Element | Snapshot |
|---|---|
| Value Intent (why we should invest) | ... (suggested · Value Owner to confirm) |
| Value at stake (size it) | Only when no figure was given: 1. [headline] how to size · benchmark (source, year) · who supplies · 2. ... |
| Value Pillar (strategic area) | Primary: ... · Secondary: ... |
| Value Driver (lever) | P0x-D0y ... (primary) · ... |
| Business Leading KPIs (early signs of use) | 1. name: Higher is better, weekly · 2. ... |
| Technical Leading KPIs (system ready) | 1. ... |

Then add at most one line: **Assumed:** what you inferred that the user should check.

End with one line: **Go further (pick any):** driver tree · full value record · coherence check · potential value · scenarios · decisions and actions · or a single specialist step.

Don't add an executive brief, a story, scores, gap lists or YAML unless the user asks for them.

## App mode
When a caller passes `mode: "app"` and no `depth`, return JSON with these fields and nothing else:

```
{depth: "snapshot", value_intent: {text, outcome_suggested}, value_at_stake: [{type, how_to_size, anchor?: {id, value, unit, source, year, quality}, owner, headline}], intake, pillars: {primary, secondary}, drivers: [{id, name, role}], business_leading: [{name, direction, cadence}], technical_leading: [{name, direction, cadence}], assumed, options, record}
```

`value_at_stake` appears only when the Intent has no stated size; `intake` holds the figures the user stated (volume, time per case, error rate, target, baseline, each with its quote); `record` is the snapshot as a draft FVR so a later full run builds on it. The Journey app calls the snapshot at Stage 1 Demand; when the leader picks a value-at-stake option and types a figure, it calls again to complete the Intent. That call carries the saved `record` and `value_at_stake_choice: {anchor_id, type, figure, unit, entered_by, basis?}`: put the figure into the Intent as T0 "stated", drop the placeholder and the `value_at_stake` field, and never write the anchor value into the Intent.

When the caller passes `depth: "full"` or a list of sections, hand over to `valor-orchestrator`. The Journey app does this when the demand converts to an epic and features, passing the snapshot `record`; everything the user accepted carries forward unchanged.

## Many items at once
For a backlog or demand list, return one table with one row per item. Columns: Key · Title · Value Intent · Primary pillar · Primary driver · Business Leading KPIs · Technical Leading KPIs · Assumed. With more than about 15 rows, deliver it as a spreadsheet. Skip opex-only items (equipment, licences, run costs) and list them separately under "No value case needed".

## Handing on
When the user picks a "go further" option, carry the snapshot forward unchanged as the starting point. Never re-ask what the snapshot already holds.
