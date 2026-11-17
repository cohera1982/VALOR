# Plain Language Guide

## Labelling rule: VALOR term first, plain definition in brackets

Labels depend on the reader's role (see *What each role sees*). By default, everything the user sees uses the **VALOR term**, followed by a short **generic definition in italic brackets** the first time it appears in a card: `**Value Intent** *(what this is for)*`. Later mentions in the same card use the term alone. Driver and pillar codes are shown with their names (`P02-D04 Process Improvement & Intelligent Automation`). Use the standard definitions below so every card reads the same; never invent new labels.

| VALOR term | Bracket definition |
|---|---|
| Value Intent | what this is for |
| Value Hypothesis | the testable bet: if we change this, that improves |
| Falsifier | what would prove us wrong |
| Value Pillar | strategic goal |
| Value Driver | specific lever that moves the goal |
| Required Operational Change | what must work differently |
| Change Owner | business role who makes the change happen |
| Value Owner | accountable for the value |
| KPI Owner | owns the measure |
| Business Leading KPI | is it being used? |
| Business Lagging KPI | is it working? |
| Technical Leading KPI | is the system doing its job? |
| Technical Lagging KPI | has the system held up over time? |
| Guardrail | watch-out for side effects |
| Baseline | where we are today |
| Suggested Range | starting point for the owner to accept or adjust, not a target |
| Benchmark | how peers perform, or what similar changes typically achieved (sourced) |
| Recommended Range | range we advise, derived from the benchmark and today's level |
| Indicative Value | money estimate from benchmarks and your data, before Finance validates |
| Illustrative Value | estimate at peer-median levels, not your data; never counted |
| Evidence Tier T0 / T1 / T2 / T3 | asserted, not yet checked with data / estimated from real numbers / confirmed by Finance / proven in results |
| Confidence | how far the value is backed by evidence and agreement |
| Value Coherence | how completely the chain from intent to value holds together |
| CS · CA | cash saving: a budget line reduces · cost avoidance: a future cost doesn't occur |
| CR | capacity released: time freed, money only if converted |
| Conversion Mechanism | how freed time becomes cash, e.g. no backfill or a contractor exit |
| RV · MG · WC | incremental revenue · margin improvement · working capital (one-off cash) |
| RR · NF | risk reduction · non-financial outcome, measured in its own units |
| Attribution | how we'll know it was this work and not something else |
| One Benefit, One Home | no double counting |
| Epic · Feature | funded investment case · one group changing how it works within a quarter |
| Lifecycle Stage | Shape / Commit / Baseline / Track / Capture: where the record is in its life |
| Commit | execution entry gate |
| P01 threshold | the approval threshold set by Finance |
| REQUIRES VALIDATION | to confirm with [owner] |

Confidence label (header only): **Low** below 40 · **Medium** 40–69 · **High** 70 and above, always with the score (`Low · 15/100`).

## Value story pattern (used while growing the story during the flow)
> When **[feature]** lets **[who]** **[do what differently]**, **[what improves]**, which **[saves money / earns more / reduces the risk of … / helps people]**. We'll know it's working when **[measure]**.

## How everything the user sees is formatted (all cards)

Chat output is rendered markdown, read on desktop and phone. **Never put cards, questions or the hypothesis in code blocks**: they render as grey monospace, can't show bold, scroll sideways on phones and look like code. Use only these building blocks:

- **Tables** for content; prose only for one-line framing. Bold labels in the left column; one item per row; each cell at most about 25 words. Never put line breaks or HTML (`<br>`) inside a cell.
- **Numbered list** for questions; options on the same line, letters in bold: `**a** One owner · **b** Each site manager · **c** Not decided`.
- **Bold lead-ins** for short notes (`**Crucial link:**`, `**Expect pushback:**`), one sentence each, at most three.
- **One reply hint** per question set, last, in inline code: Reply like `1: … · 2: a · 3: b`.

Headings: level 2 for the card title, level 3 for its numbered sections; nothing else. No horizontal rules. Status marks only in the Coherence Check (✅ in place · ⚠️ partial or untested · ❌ missing).

## Executive Brief (always first, above the Value Card)

Every output opens with the Executive Brief: the summary a leader reads in under a minute. It is drawn from the record and never adds anything the card does not hold.

**Executive Brief** · [feature or epic name] · [Business Unit]

| | |
|---|---|
| **Decision needed** | [one question] — **a** … · **b** … · [who decides, at which forum] |
| **Verdict** | [verdict, display name below] — [why, one line] |
| **Value size** | [Value Owner's range, labelled projected] · or "Indicative [currency] x–y a year (benchmarked; to validate — Finance)" · or "Illustrative at peer median: …" · or "to size — [owner]" |
| **Evidence** | [tier, plain name] · Confidence [Low/Medium/High] [nn]/100 → [next step] (+[n]) |
| **What would change it** | [the one condition that would move the verdict] |
| **Biggest risk** | [the conversion, adoption or overlap risk that most limits the value] |
| **Your ask** | [what this reader is asked to do, written for their role] |

**Brief rules**
- Seven rows, one line each, no codes. Pillars and value categories in plain words.
- **Decision needed** is the top item from Decisions Required; **Your ask** changes by role (the CEO approves or redirects, the CFO validates inputs, the PO supplies baselines).
- For Finance, **Value size** moves to the first row.
- Before Commit, **Verdict** reads "Shaping — [next need]"; never a readiness verdict.
- **Evidence** shows the trajectory: the score now and the step that raises it most, never the score alone. Where valor-benchmark-alignment wrote an executive line, append it after a dot ("· Peers close in 4.8–6.4 days").
- Pillars in plain words: P01 grow revenue · P02 run operations at lower cost · P03 stay resilient, compliant and agile · P04 build our people · P05 strengthen digital, data and AI · P06 win with partners and the ecosystem.
- Projected value is always labelled projected. Value size order: the Value Owner's own range; else the indicative range from `scripts/value_range.py` (client baseline × benchmark × client unit cost); else the illustrative peer-median range, labelled as not your data; else "to size — [Value Owner]". Never a figure written without one of these sources.

**Verdict display names** (the rubric in `valor-core.md` §9 is unchanged; only the words shown change)

| Rubric verdict | Shown as |
|---|---|
| Fund | Fund — proceed at full scope |
| Prove | Prove — fund a pilot, collect baselines |
| Fix adoption | Fix adoption — the numbers hold, the change needs an owner |
| Rework or stop | Redesign adoption — design the change before funding |
| Fix the logic first | Not yet ready to assess — [missing link] |
| Scale · Continue · Adapt · Stop (after delivery) | Scale · Continue, prove attribution · Adapt adoption · Stop or redirect |

## What each role sees (level of information)

The record is always complete. What changes by role is how much of the Value Card follows the brief, and how it is labelled. The role comes from `coach_meta.role` (asked once per person). If it is unknown, show the brief plus the full card.

| Role | After the Executive Brief | Labels |
|---|---|---|
| **Executive** (BU CEO, CDTO) | The driver tree page, executive view; the full card on request. In Portfolio mode, the portfolio pack instead of cards | Plain words; no codes, no brackets |
| **Value Owner** (Business SVP) | 1 Value Statement · 3 KPI Scorecard (business KPIs only) · 6 Scenarios · 7 Recommendations and Decisions Required | VALOR terms with brackets; no codes |
| **BU CFO / Finance partner** | 3 KPI Scorecard (Business Lagging KPIs with baseline source) · 4 Value Equation in full · 5 Coherence Check (counting rows) · 7 Decisions Required | VALOR terms with brackets; value category codes with names (CS cash saving…); evidence tier shown |
| **Head of IT** | 2 Value Hierarchy · 5 Coherence Check · 7 Key Actions and Decisions Required, with the approval tier as the first Key Action | VALOR terms with brackets |
| **ITBP** | Full Value Card | VALOR terms with brackets; codes with names |
| **Product owner / BA** | Full Value Card, then one KPI definition table per KPI | VALOR terms with brackets; codes with names |
| **KPI Owner** | 3 KPI Scorecard · KPI definition tables for their KPIs · 7 items they own | VALOR terms with brackets |
| **Scrum Master / delivery lead** | 1 Value Statement (If and Then rows) · 3 KPI Scorecard (Business Leading and Technical KPIs) · 5 Coherence Check (conversion rows) · 7 Key Actions as sprint checks | VALOR terms with brackets |
| **Value Orchestration Lead / Portfolio Governance Lead** | Full Value Card, KPI tables, Final Value Scorecard; admin note on "VALOR admin" | VALOR terms and codes |

**Role rules**
- Sections keep their numbers when some are left out, so people in different roles can refer to "section 4" and mean the same thing.
- End with one line naming what's left out: "Sections 2, 4 and 5 are in the full card; say 'full card' to see them."
- "Full card", "show the scorecard" or "show the KPI definitions" always works, for any role.
- Never drop a blocker for any role. A blocker finding from section 5 appears in the brief as **Biggest risk**, even for executives.

## Value Card (follows the Executive Brief; sections shown by role, always in this order)

## Value Card: [feature or epic name]
**Business Unit:** [BU] | **Confidence** *(how far the value is backed by evidence and agreement)*: [Low/Medium/High] · [nn]/100 | **Evidence Tier** *(strength of proof behind the numbers)*: [T0–T3 name] | **Lifecycle Stage** *(where the record is in its life)*: [stage, plus status, e.g. "Shape, baseline pending"]

### 1. Value Statement *(why this work exists and how it creates value)*
| | |
|---|---|
| **Value Intent** *(what this is for)* | [one sentence] |
| **If** *(the change we make)* | [capability plus the required operational change] |
| **Then** *(the result we expect)* | [operational outcome] |
| **So that** *(the benefit to the business)* | [enterprise value] |
| **Falsifier** *(what would prove us wrong)* | [one or two tests] |

### 2. Value Hierarchy *(how this links to strategy)*
| Level | Primary | Secondary |
|---|---|---|
| **Value Pillar** *(strategic goal)* | [P0x name] | [P0x name · P0x name] |
| **Value Driver** *(specific lever that moves the goal)* | [P0x-D0y name] | [up to two, each P0x-D0y name] |

An epic card shows pillars; a feature card shows both rows, its drivers under the epic's pillars.

### 3. KPI Scorecard *(how we measure it)*
| KPI | Type | Definition | Today *(baseline)* | Benchmark *(peers or typical improvement)* | Recommended Range | KPI Owner *(owns the measure)* |
|---|---|---|---|---|---|---|
| [name] | Business Lagging *(is it working?)* | [one line] | [value or "to supply — owner"] | Peers: median x · top quartile y ([org], [year], [A/B]) | [range] *(benchmarked)* | [role] |
| [name] | Business Leading *(is it being used?)* | [one line] | [value or "new process"] | Typical: x–y% [direction] with [intervention] ([org], [year], [grade]) | [range] *(benchmarked)* | [role] |
| [name] | Guardrail *(watch-out for side effects)* | [one line] | [value] | [benchmark or "none in register"] | [ceiling] *(suggested)* | [role] |

Three to five rows. A rare outcome is a row typed **Long-run proof** *(rare outcome, judged after [period])*. Benchmarks come only from `benchmark-register.csv`; recommended ranges follow `benchmark-method.md` §3 (full vs partial scope, gap-closure convention, cap at best peer level). Where no benchmark exists, write "none in register" and use the suggested range. Then one italic line: *Ranges are recommendations until the KPI Owner agrees them. Present them as projected.* Add the scope caveat in the same line when the feature delivers only part of the benchmarked intervention.

### 4. Value Equation and Indicative Value *(how the benefit is calculated, and roughly how big)*
**Benefit** = [term] **[category code – name** *(definition)***]** + … − (build + run + change cost)

| Benefit | Category | Formula | Inputs *(source)* | Indicative range | Counting |
|---|---|---|---|---|---|
| [plain words] | [code – name] | [baseline × improvement × unit value] | Baseline: [value, source] · Improvement: [range, BM id] · Unit value: [value, source or "to supply — Finance"] | [currency x–y a year, or natural units] | [Counted · Not counted (why) · Shown separately · Tracked] |

Ranges come only from `scripts/value_range.py` output (`benchmark-method.md` §4); never compute in prose. Missing inputs show as "to supply — [owner]" and the range stays in natural units or "to size". A peer-median illustration is labelled **Illustrative, not your data**, and never enters a total. Then one line on what is not counted and why, and the total of counted annual value with WC shown separately.

### 5. Coherence Check *(does the chain from intent to value hold together?)*
| Condition | Status |
|---|---|
| Required Operational Change has a named Change Owner | ✅ / ⚠️ / ❌ [note] |
| [the crucial link or key assumption] | … |
| CR has a Conversion Mechanism | … |
| One Benefit, One Home | … |
| [Epic, Value Owner and Falsifier agreed] | … |

Then one line: **Value Coherence** *(how completely the chain from intent to value holds together)*: [nn]% · weakest strand: [strand — link].

### 6. Scenarios *(range of outcomes)*
| Best case | Worst case |
|---|---|
| [one row] | [one row] |

### 7. Key Actions, Recommendations and Decisions Required

**Key Actions** *(who does what next)*
| # | Action | Owner | Due by |
|---|---|---|---|
| 1 | [action] | [role] | [lifecycle gate or forum, e.g. Before Commit · Sprint 0 · Quarterly Portfolio Forum] |

**Recommendations** *(what we advise and why)*
| # | Recommendation | Rationale |
|---|---|---|
| 1 | [recommendation] | [one line] |

**Decisions Required** *(who decides what)*
| # | Decision | Options | Decided by |
|---|---|---|---|
| 1 | [decision] | **a** … · **b** … · **c** … | [role] |

End with one line: **Recommended:** [option per decision, e.g. 1c · 2b] and why, in one sentence.

**Card rules**
- The Executive Brief always comes first. Card sections follow the role table, always in this order and keeping their numbers. Keep it to about one screen; feature-level detail goes to the record and the Jira export.
- Key Actions: at most six; everything formerly "Still needed", "Also noted" and Legal or Compliance checks goes here with an owner. Due dates are gates or forums, never invented calendar dates.
- Decisions Required: at most four, each with lettered options. Unpicked trade-offs and the crucial-link question go here with their owner.
- Never show a measure, owner or range the user didn't pick without *(suggested)*.
- When an executive asks for the full card, keep sections 3 and 5 to their three most important rows.
- Scores follow rubric v2 in `valor-core.md` §9. Never round up.

**Gap card (quick view).** The same Value Card, with each gap shown in its cell as **[n]** (e.g. `| **If** *(the change we make)* | **[1]** |`). Then:

**Fill the gaps** — fix anything else that's wrong too
1. **Who has to do what differently?** Your words: who acts, and when
2. **Who is the Change Owner** *(makes the change happen)*? **a** [role] · **b** [role] · **c** Not decided
3. …

Reply like `1: staff clock in, supervisors approve · 2: a · 3: not sure`

Words never shown to users: "light path", "light-path". Say "below the P01 threshold *(the approval threshold set by Finance)*" rather than a bare code.

## Value Hypothesis (shown for acceptance in epic sessions, above the Value Card)

| Value Hypothesis *(the testable bet)* | |
|---|---|
| **We believe** | [epic, naming its features where known] |
| **Will move** | [KPI] **[range]** · [KPI] **[range]** *(suggested)* |
| **Within** | [horizon] *(suggested)* |
| **Because** | [who does what differently] |
| **So that** | [the gain] |
| **Falsifier** *(what would prove us wrong)* | [test] · [test] · [test] |

**Accept** · **Change something**

Once accepted, the hypothesis becomes Section 1 of the Value Card.

## KPI definitions (in chat only on request)

| [KPI name] | [Is it being used? / Is it working? / Watch-out] |
|---|---|
| **Definition** | [one sentence] |
| **Formula** | [numerator ÷ denominator] |
| **Unit · frequency** | [unit] · [frequency] |
| **Today** | [baseline method] — *[who] to supply* |
| **Benchmark** | [peer level and/or typical improvement, with org, year, grade] or "none in register" |
| **Recommended range** | [range, horizon] *(benchmarked or suggested; a committed target only after target setting)* |
| **Data source** | [system] |
| **Owner** | [role] |

One table per KPI, three to five in total.

## Final Value Scorecard (produced every session for the review page; shown in chat only on request)

The Value Story Card is the conversation's summary; the Final Value Scorecard is the record people review and accept. Same content, structured by layer, with values and scores. In chat, render it as sections with bold lead-ins and tables, never a code block:

**Value Scorecard** · [Theme] › [Initiative] › [Epic] › [Feature] · [date]

| Stage | Shape ✓ · Commit ✓ · **Baseline (next)** · Track · Capture |
|---|---|
| **Verdict** | [Prove / Fund / Fix adoption / Rework or stop / Fix the logic first, from Commit onward; "Shaping: [next need]" before] — [what to do next] |
| **Value size** | [range or "to size"] |

**Value** (what the business keeps)
| Benefit | Category | Range | Evidence |
|---|---|---|---|
| [in plain words] | [value category] | [suggested range or "to size"] | [best thinking / estimated / confirmed by Finance / proven] |

**Epic hypothesis** — [hypothesis] *We'll know we're wrong if* [falsifier].

**Impact** (who is better off, or worse off)
| Category | Who | What changes | Measure |
|---|---|---|---|

**Benefits** (how each is counted)
| Benefit | Kind | Counting | Owner |
|---|---|---|---|

**KPIs**
| KPI | Today | Suggested range or target | Frequency |
|---|---|---|---|

**Scores**
| Score | Value | What it means |
|---|---|---|
| **Value coherence** | [nn]% | How completely the chain from intent to value holds together. It shows the case is well-formed, not how big or proven the value is. Strategic [nn]% · Conversion [nn]% · Counting [nn]% · Data [nn]%. Weakest: [strand] — [weak link]. [If conversion < 75%: "Capped at 60% until the behaviour change is designed and owned."] |
| **Confidence** | [nn]/100 | How far the value is backed by evidence and agreement. Next step that raises it most: [step] (+[n]) |
| **Verdict** | — | Where the epic stands on two questions: will behaviour change (conversion), and is the value backed (confidence)? It says what to do next, not how big the value is. |

**Agreements** — [n] confirmed · [n] recorded, awaiting owner · [n] requested
| Item | Who | Status | Date |
|---|---|---|---|

**Still needed** (next stage's needs first)
1. [item] — *[who]*

Labels follow the labelling rule at the top of this file (VALOR term, bracket definition). Rules: impact rows use the six impact categories in plain words (Customer, Workforce, Partner and channel, Operations, Compliance and safety, Society and environment) and include any group made worse off. Compute both scores and the verdict with rubric v2 in `valor-core.md` §9 (agreement counts only in confidence; conversion gate applies) and show the one-line explanations from §11 every time, exactly. Never round scores up to make a case look better. Driver and pillar codes appear with their names.

## Finalise card (always last)

**Before we finalise**

**A. Suggestions** — grouped by who confirms

| # | Suggestion | Confirms |
|---|---|---|
| 1 | Horizon: within 2 quarters | Value Owner |
| 2 | Overtime measure owner: Payroll Manager | Value Owner |
| 3 | Watch-out: whole-crew approvals | Head of FM Operations |
| 4 | Kiosk clock-in for staff without phones | Head of FM Operations |
| 5 | Watch-out: deductions per contract | Contracts Manager |

**a** Accept all (5) · **b** Accept all except [numbers] · **c** Leave them for the owners

**B. Finalise** — **a** Finalise and send to the owners · **b** Not yet · **c** Someone already agreed (say who)

Reply like `A: all except 4 · B: finalise`

After "finalise", the final card, then two lines:

**Sent to** Value Owner (2) · Measure owners (2) · Finance (1) · Other checks (1)
**Scorecard v1 finalised** — 4 accepted by you · 6 decisions with owners · 8 items still to supply
