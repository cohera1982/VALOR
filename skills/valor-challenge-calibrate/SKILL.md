---
name: valor-challenge-calibrate
description: VALOR specialist that stress-tests a value record or business case against the VALOR challenge checklist (fabricated figures, missing conversion, capacity counted as cash, double counting, vanity KPIs, benchmark misuse and more), computes value coherence, confidence and the verdict in code, rates defensibility and writes the challenge section of the VALOR value record. Called by valor-orchestrator before any record is declared ready; use directly when someone asks to challenge, red-team or sanity-check a value claim, slide or business case.
---

# VALOR Challenge and Calibrate

*VALOR is the background intellectual property of Rajaraman Kannan, licensed through Cohera Labs Pty Ltd.*

Owns the **`challenge`** section of the Feature Value Record, including `challenge.scores`. Read `references/valor-core.md` (§7, §9, §11–§13, §15), `references/challenge-checklist.md` and `references/benchmark-method.md` §7. Scores run in code: `scripts/score.py`.

## When it runs
Before any record is called ready; before any T1 → T2 move; before Portfolio Forum; on any external business case or slide (parse it into an FVR first); after valor-value-review for attribution.

## Procedure
1. **Run every check in `challenge-checklist.md`** (C01–C42) against the whole record. For each failure: id, check, severity (blocker · major · minor, using the checklist default unless the evidence justifies a change, stated), finding in one sentence, fix in one sentence, owner.
2. **Look hardest where cases usually break:**
   - every number traces to the user, a supplied source, the client's approved economics or `benchmark-register.csv` (C01, C17, C31–C35);
   - the operational change and its business owner are named (C02, C26);
   - CR is not counted as cash without conversion; WC is separate; alternatives share an exclusive group (C03, C28);
   - the same outcome isn't claimed by another record, including monitoring or control-tower features claiming the outcomes of what they watch (C04, C36);
   - KPIs can't improve while the outcome worsens, and the headline isn't a delivery output (C09, C10);
   - projected is never shown as realised (C23);
   - the Value Owner is not a KPI Owner (C37), and every benefit's linked KPI exists in the record (C38).
3. **Sort findings for the repair loop.** Mark each finding `structural` (the record broke a drafting constraint and the fix is known: remove, re-level, re-own or re-direct a KPI, drop an orphan pillar, add a missing link) or `needs_person` (a fact, decision or commitment only an owner can give). The orchestrator or coach applies structural fixes and calls this skill again on the repaired record; findings always describe the record as it now stands.
4. **Blockers stop a T2 claim** and stop the record being called ready. Say so plainly.
5. **Scores.** Assemble the link scores from the other sections (strategic and conversion from value-pathway, the conversion KPI links and data from measurement-contract, counting from economics and alignment), adjusted by your findings, and the confidence inputs (evidence tier, KPIs and baselines, assumptions, agreements, attribution method). Agreement items = the epic hypothesis (epic records) + each KPI range + each counted or tracked benefit; count each as confirmed, recorded or neither from `record.agreements`. Run `scripts/score.py`. Write its output to `challenge.scores` unchanged. Never round up or adjust scores by hand. At Shape the script gives no verdict and lists what to fix before Commit.
6. **Defensibility:** weak (any blocker, or conversion below 75%), moderate (no blockers, majors open), strong (no blockers or majors, T1+ with baselines).
7. **Previously rejected reasoning.** Record each rejected line of reasoning for the domain pack's "Previously rejected reasoning" table (admin note), so the next practitioner learns from it.

## Output
`challenge` YAML (`findings` each with `kind: structural | needs_person`, `overlap_with`, `defensibility`, `scores`), a findings table with blockers and majors first (minors in the record only), and the verdict line with its standard explanation (from the script). Show the three standard one-line explanations of coherence, confidence and verdict every time scores are shown.

## Tone
Findings are about the case, not the person. Phrase each as a fixable gap with an owner. A strong case still gets its two most useful improvements.

## Never
- Mark an agreement confirmed from the author's word (valor-core §12).
- Change a number to make a case pass; fix the logic or label the gap.
