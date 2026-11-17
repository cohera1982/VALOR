# VALOR — Value Orchestration Framework (Cohera Labs edition)

VALOR is the intellectual property of Rajaraman Kannan, licensed through Cohera Labs Pty Ltd. Confidential; not for redistribution.

A Claude plugin of twelve skills that define, size, challenge and track the business value of features and epics: the Value Snapshot (`valor-lite`, default), the Value Driver Tree, the Value Coach, the Orchestrator (full value record) and eight specialists.

## Version 1.4.3 (17 Nov 2026)
- Value Intent written as an executive pitch: outcome first, at most 25 words, outcome marked "suggested", `[value at stake]` slot when no figure is given.
- Value at stake suggestions from `references/value-at-stake-anchors.csv` (16 sourced, quality-graded anchors by driver); method in `benchmark-method.md` §9.
- App calls: snapshot at demand, full on conversion to epic and features, building on the snapshot record; `value_at_stake_choice` completes the Intent.
- Drafting fixes: one framing per measure, no baseline request for new capabilities, sponsor as default Value Owner.

## Layout
`.claude-plugin/plugin.json` · `skills/<skill>/SKILL.md` · `skills/<skill>/references/` (registers and method, identical copies per skill) · `skills/<skill>/scripts/`.

## Updating registers
Edit the master copy in `skills/valor-orchestrator/references/`, copy it to every `skills/*/references/`, check driver IDs and sources, then bump the version.

This generic edition has client-specific business units, names and governance forums removed; `bu-map.csv` is a template.
