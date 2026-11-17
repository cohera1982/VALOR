---
name: valor-driver-tree
description: "VALOR Value Driver Tree. Use when someone asks for a driver tree, value tree or KPI tree, or wants to see how a feature, epic, programme or portfolio traces from value intent through pillars and drivers to lagging, business leading and technical leading KPIs. In app calls (mode: \"app\"), use it only when depth is \"tree\"; depth \"full\" goes to valor-orchestrator."
---

# VALOR Value Driver Tree

*VALOR is the background intellectual property of Rajaraman Kannan, licensed through Cohera Labs Pty Ltd. In the client edition, user-facing words say "Value Orchestration", never "VALOR".*

Shows the line of sight from why it matters down to what we measure. It does one job, the tree. Coherence, potential value, scenarios and decisions are separate, and run only when the user asks for them.

## Two depths
| Input in hand | Output |
|---|---|
| A Value Snapshot (`valor-lite`), a description, or a backlog | **Text tree** in chat (below). Fast, no record needed. |
| A value record (FVR) for an epic, with or without its features | **Tree page** from `scripts/driver_tree.py`: an executive view, a detailed view and a gaps view, with link checks. Never draw this page by hand. |

If the user wants the tree page but only a snapshot exists, show the text tree. Then offer the full value record (`valor-orchestrator`), which the page is drawn from.

## Text tree

```
Value Intent (why it matters)
└─ Value Pillar (strategic area): primary, then secondary if any
   └─ Value Driver (lever): P0x-D0y
      └─ Business Lagging KPI (the epic outcome): direction
         ├─ Business Leading KPI (feature F1, early sign of use): direction, cadence
         │  └─ Technical Leading KPI (system ready): direction
         └─ Business Leading KPI (feature F2) ...
```

Ask at most one question, and only when the epic's outcome measure is unknown and the user can give it. Otherwise, mark that node "to confirm (Value Owner)".

## Tree page (from a record)
Run `python3 scripts/driver_tree.py <epic>.yaml [<feature>.yaml …] --out <name>.html`. Publish the page, or send it to the user. Add `--json <name>-tree.json` when an app needs the flat `value_driver_tree`. The page shows only what the record holds, and the script prints its gap counts.

## Rules (both depths)
- **Levels.** Lagging KPIs belong to the epic, one or two per outcome. Business leading KPIs belong to features, one to three each. Technical leading KPIs sit under the business leading KPI they enable, never at outcome level.
- **Traceability.** Every lagging KPI has at least one business leading KPI under it. Every leading KPI sits under exactly one lagging KPI. Flag any orphan: "no feature moves this" or "predicts nothing".
- **Drivers fit the pillars.** A feature's drivers sit under its epic's primary or secondary pillar. The primary driver goes where the value lands, not where the technology sits (the P05 trap). Driver IDs come only from `references/driver-register.csv`.
- **Links.** Label each leading-to-lagging link "assumed" unless the user, a pilot or past data quantified it. If it was quantified, show the figure and its source.
- **No invented numbers.** Show a baseline, target or value only when it was stated or sourced. KPI names, units and directions come from `references/kpi-register.csv` wherever a row matches.

## Portfolio tree
Roll up: Pillar → Driver → epics (count, plus total proposed budget if given) → their lagging KPIs. Under the tree, list as gaps any driver with no epics and any epic with no lagging KPI. For a backlog, give a table with these columns: Epic · Pillar · Driver · Lagging KPI · Feature · Business Leading KPI · Technical Leading KPI · Link status.

After the tree, add at most three flags, each naming who resolves it. End with one line: **Go further (pick any):** full value record · coherence check · potential value · scenarios · decisions and actions.
