# VALOR Feature Value Record (FVR) — Template

The FVR is the single record every VALOR skill reads and writes. Each skill owns specific sections (shown as `owner:`). Keep it as YAML so it can be pushed to Jira Feature fields (see `jira-field-schema.md`) and versioned.

```yaml
fvr_version: 1.1
# File name: FVR-<feature_key>.yaml; without a Jira key, FVR-<bu slug>-<record slug>.yaml, where the bu slug is the bu-map.csv name in
# lower case with spaces as hyphens (e.g. FVR-mobility-kabi-taxi-pulse.yaml).
# Gap marker: anything not yet known is stored as `REQUIRES VALIDATION — [what, owner]` (one marker only; pages show it as "To supply").
# A user's "not sure" is stored as `REQUIRES VALIDATION — [owner] (answered: not sure)`. "none claimed" means no financial outcome at all.
# Section owners: evago, record.suggestions, record.requests_by_owner and scorecard rows are written by valor-orchestrator's integrate step
# (or valor-value-coach); every other section names its owning specialist skill.
evago:                       # EVAGO alignment (valor-core §15); epic records fill all of it, feature records inherit from their epic
  record_level: feature      # epic | feature
  value_owner: {name: "", role: ""}     # accountable for value; usually the Business SVP
  kpi_owners: []             # [{kpi_id, name, role}]; never the same person as value_owner
  itbp: {name: ""}
  business_outcomes: []      # [{outcome, lagging_kpis: [kpi_id]}]; one or two KPIs per outcome
  expected_financial_outcome:
    range: "REQUIRES VALIDATION"        # e.g. "AED 1.2–1.8m a year"; or "none claimed"
    source: ""               # asserted — source to supply ([who]) | named source
    approval_tier: ""        # cfo (at or above P01) | head-of-it-delegate (below P01) | none-claimed
    approved_by: ""          # logged in record.agreements, never from the author's word
  execution_entry:
    joint_definition_confirmed: false   # ITBP and Value Owner
    financial_outcome_approved: false
    cleared_for_execution: false        # true only when both above are confirmed or recorded
  targets:
    status: not-set          # not-set | suggested | agreed | approved | overdue
    approved_at: ""          # quarterly Portfolio Forum, date
    deadline: ""             # P15
  feature_contribution:      # feature records only
    epic_kpi: ""             # the epic Business Lagging KPI this feature moves
    expected_share: ""       # share of the epic's target, as a range
    leading_kpis: []         # one to three kpi_ids of the feature's own Business Leading KPIs (adoption, acceptance, quality of use); older records with a single leading_kpi string are read as a one-item list
  releases:                  # value realised per go-live
    - release: ""
      go_live: ""
      value_realised: ""     # KPI movement against baseline
      impact: ""             # effect on the business outcome and early signals
      benefits: ""           # quantified, with counting labels
      validated_by: ""       # BU CFO (financial) | KPI Owner (non-financial)
  learning_milestones: []    # exploratory epics only, instead of KPIs
value_driver_tree:           # epic records, Track 2 export; written by scripts/driver_tree.py --json (or by hand when scripts cannot run). Apps draw the tree from this block only
  complete: false            # true only when no node is a gap and no blocker or major tree check is open
  nodes:                     # flat list; parent ids build the tree
    - id: ""                 # INT-1 | P02 | P02-D04 | B1 | kpi_id | feature key | GAP-...
      type: ""               # intent | pillar | driver | benefit | lagging_kpi | feature | leading_kpi | technical_kpi
      label: ""              # plain words, written in full
      parent: ""             # parent node id; empty only for intent
      role: ""               # pillars: primary | secondary
      value: ""              # benefits: category and size in its natural unit or indicative range
      kpi_type: ""           # KPIs: Business Lagging | Business Leading | Technical Leading | Technical Lagging
      direction: ""          # KPIs
      source: ""             # KPIs: register | analogue | stated | domain_pack | suggested | new
      register_id: ""        # KPIs
      benchmark: []          # KPIs: benchmark-register ids (and client crosswalk ids) only
      today: ""              # KPIs: baseline or "to supply"
      range: ""              # KPIs: recommended range
      link: ""               # leading KPIs: predicted link to the epic KPI
      expected_share: ""     # features: share of the parent KPI's target, as a range
      also_moves: []         # features: other epic KPIs the feature moves
      owner: ""              # KPI owner (business role) or feature change owner
      status: complete       # complete | gap
      gap_question: ""       # gap nodes: the question that closes the gap, with who answers
  gaps: []                   # the tree checks: severity, check, finding, fix
record:
  feature_key: ""            # Jira key, e.g. MOB-1234
  feature_name: ""
  epic_key: ""
  strategic_theme: ""
  initiative: ""
  business_unit: ""          # exactly as in bu-map.csv, e.g. "Mobility – Taxi Operator A"
  domain_pack: ""            # e.g. mobility-taxi; "none" when the BU has no pack
  draft_pack: ""             # file name of a pack drafted this session, if any
  record_status: draft       # draft | finalised | challenged | finance-validated | in-capture | closed
  scorecard_version: 0       # increments on each finalise; reopen + save = next version
  finalised: {by_role: "", date: "", accepted_by_author: 0, awaiting_owners: 0, to_supply: 0}
  requests_by_owner:         # one bundled confirmation request per owner
    - {owner_role: "", items: [], status: requested}
  suggestions:               # every item the coach suggested; status: suggested | accepted-by-author | rejected | confirmed
    - {id: "", item: "", suggested: "", confirms: "", status: suggested}
  evidence_tier: T0          # T0 | T1 | T2 | T3
  lifecycle_stage: shape     # shape | commit | baseline | track | capture (valor-core §12)
  agreements:                # agreement log (valor-core §12); never only in chat
    - item: ""               # HYP-<epic> | BEN-<epic>-<id> | <kpi id>
      level: recorded        # confirmed | recorded | noted | requested
      decision: accepted     # accepted | adjusted | rejected | challenged
      by_name: ""
      by_role: ""
      date: ""
      how: ""                # review page | Jira | meeting | email | Portfolio Forum
      range: ""              # agreed range, if adjusted
      note: ""
  revision_log:
    - date: ""
      by: ""
      change: ""

context:                     # owner: valor-business-context
  problem_statement: ""      # whose problem, in their terms
  affected_stakeholders: []
  process_touched: ""
  constraints: []
  existing_objectives: []    # OKRs / BU KPIs already in place
  open_questions: []

formation:                   # owner: valor-value-pathway
  value_intent: ""
  primary_driver: ""         # P0x-D0y
  secondary_drivers: []
  driver_rationale: ""
  assumptions:
    - id: A1
      statement: ""
      status: untested       # untested | evidenced | disproved

conversion:                  # owner: valor-value-pathway
  pathway:                   # capability → behaviour change → operational outcome → stakeholder impact → enterprise value
    capability: ""
    required_operational_change: ""
    change_owner: ""
    operational_outcome: ""
    stakeholder_impact: ""
    enterprise_value: ""
  adoption_conditions: []
  dependencies: []           # other features, data, policy, people
  conversion_risks: []

measurement:                 # owner: valor-measurement-contract
  kpis:
    - kpi_id: ""             # catalogue ID if exists, else NEW-xx
      name: ""
      type: ""               # Business Leading | Business Lagging | Technical Leading | Technical Lagging
      guardrail: false
      direction: ""          # Higher is better | Lower is better (register first)
      source: ""             # register | analogue | stated | domain_pack | suggested
      register_id: ""        # register kpi_id when source is register or analogue
      predicts: ""           # Business Leading only: the epic KPI it predicts
      link: ""               # Business Leading only: expected link, quoting the epic target ("80% adoption → exceptions below 10 a month")
      cadence: ""            # Business Leading only: weekly | fortnightly | each pay cycle
      early_warning: ""      # Business Leading only: threshold that triggers action ("below 60% after week 4")
      contract:
        definition: ""
        population: ""
        unit: ""
        formula: ""
        baseline_value: "REQUIRES VALIDATION"
        baseline_period: ""
        target_value: "REQUIRES VALIDATION"
        benchmark_ids: []    # rows in benchmark-register.csv, e.g. [BM-FIN-BG-01-1]
        recommended_range: ""   # from benchmark-method.md §3, e.g. "5.5–6.0 days within 2 quarters"
        range_basis: ""      # benchmarked | suggested | owner-agreed
        scope_vs_benchmark: ""   # full | partial (partial => lower half of benchmark range)
        beyond_peer_reason: ""   # only if the range starts above the cited peer level (C34); otherwise the tree flags it
        target_date: ""
        data_source: ""
        collection_method: ""
        frequency: ""
        data_owner: ""
        outcome_owner: ""
        decision_rule: ""    # e.g. "If < X by date, review adoption; if > Y, scale"
        validation_status: unvalidated

alignment:                   # owner: valor-kpi-okr-alignment
  okr_links:
    - objective: ""
      key_result: ""
      contribution: ""       # how this feature contributes; shared with which other interventions
  catalogue_matches: []      # existing VALOR catalogue KPIs reused
  new_kpis_proposed: []
  bu_coe_view: ""            # BU / CoE / Corporate Function / Strategic Programme

economics:                   # owner: valor-value-economics
  benefits:
    - id: B1
      category: ""           # CS | CA | CR | RV | MG | WC | RR | NF
      description: ""
      driver: ""
      linked_kpi: ""
      formula: ""
      inputs: {}             # each input: {value, source, tier}; improvement inputs cite a benchmark_id
      basis: client          # client | peer_median (illustrative, never counted)
      indicative_range: null # [low, high] from scripts/value_range.py only
      conversion_mechanism: ""   # required for CR
      exclusive_group: ""    # set when benefits are alternative uses of the same capacity
      selected: false        # exactly one benefit per exclusive_group is selected
      annual_value: null
      risk_adjustment_pct: null  # FRACTION: 0.2 = 20%
      ramp: []               # per-year realisation as FRACTIONS, e.g. [0.3, 0.8, 1.0]
      conversion_owner: ""   # CR only: business role accountable for the conversion mechanism
  cost_lines_requested: []   # optional: cost lines for the data request sheet, e.g. {item: "e-KYC fee per check", type: Run, owner: Procurement}
  costs:
    - id: C1
      type: ""               # build | run | change | opportunity
      timing: annual         # upfront | annual
      description: ""
      annual_value: null
      source: ""
  flexibility: []            # future options this creates (qualitative unless sized)
  horizon_years: 3
  discount_rate: null        # Finance-approved only
  results: {}                # populated by valor_calc.py only

challenge:                   # owner: valor-challenge-calibrate
  findings:
    - id: F1
      check: ""              # e.g. CR-as-CS, double count, vanity KPI
      severity: ""           # blocker | major | minor
      finding: ""
      fix: ""
      resolved: false
  overlap_with: []           # other feature keys claiming the same benefit
  defensibility: ""          # weak | moderate | strong
  scores: {}                 # written by scripts/score.py only: strands, coherence, confidence, verdict

capture:                     # owner: valor-value-review
  reviews:
    - date: ""
      period: ""
      kpi_actuals: {}
      variance_explanation: ""
      attribution_note: ""
      realised_value: null
      recommendation: ""     # continue | adapt | scale | stop
      verdict: ""            # Scale | Continue, prove attribution | Adapt: fix adoption | Stop or redirect (score.py)
      persistence: ""        # holding | fading | not yet assessable
      decided_by: ""

coach_meta:                  # owner: valor-value-coach
  role: ""                   # product-owner | itbp | value-owner | kpi-owner | delivery-lead | head-of-it | finance | executive (asked once per person)
  mode: ""                   # annual-definition | execution-entry | target-setting | feature | value-realised
  depth: ""                  # quick | deep
  first_draft_accepted: null
  turns_to_card: null
  trade_offs_to_confirm: []
  admin_note: ""            # coach's working notes for VALOR admins only; never shown to users

benchmarks:                  # owner: valor-benchmark-alignment
  alignment_notes: []        # benchmark IDs from benchmark-register.csv (and crosswalk IDs where benchmark-crosswalk.md exists)
  executive_line: ""        # one line for executive output: how the case compares with peers
```

## Epic value tree (record_level: epic)
An epic record carries the value intent, pillars, hypothesis, the epic's Business Lagging KPIs and all benefits, and lists its features. `scripts/driver_tree.py` draws the driver tree from exactly these fields.

```yaml
fvr_version: 1.2
record_level: epic
record: {epic_key: "", epic_name: "", business_unit: "", currency: AED, evidence_tier: T0, lifecycle_stage: shape}
evago: {value_owner: {role: ""}, kpi_owners: [{kpi_id: "", role: ""}], expected_financial_outcome: {range: "REQUIRES VALIDATION — Value Owner"}}   # or a range, or "none claimed"
formation:
  value_intent: ""
  primary_pillar: P02
  secondary_pillars: []
  hypothesis: {text: "", falsifier: ""}
measurement:
  kpis:                      # epic Business Lagging KPIs (and guardrails); `driver` places each in the tree
    - {kpi_id: "", name: "", type: Business Lagging, driver: P0x-D0y, guardrail: false,
       contract: {unit: "", baseline_value: "", benchmark_ids: [], recommended_range: "", range_basis: suggested}}
features:
  - key: ""
    name: ""
    primary_driver: P0x-D0y
    secondary_drivers: [{driver: P0x-D0y, role: ""}]
    required_operational_change: ""
    change_owner: ""           # business role
    provisional: false         # true when drafted by VALOR from epic text; names show "(suggested)" until the Value Owner confirms
    kpis: [{kpi_id: "", name: "", type: Business Leading, direction: "", source: "", predicts: "", link: "", cadence: "", early_warning: "",   # one to three Business Leading; technical KPIs may follow
            contract: {unit: "", baseline_value: "", benchmark_ids: [], recommended_range: "", range_basis: suggested}}]
    contributes_to: [{epic_kpi: "", share: ""}]
economics:
  benefits:                  # each benefit names the feature that delivers it and the KPI that shows it
    - {id: B1, feature: "", category: CS, description: "", driver: P0x-D0y, linked_kpi: "", inputs: {}, indicative_range: null, counting: ""}
  results: {counted_annual_value: null, label: ""}    # from scripts/value_range.py or valor_calc.py only
challenge: {findings: [], scores: {}}                  # scores from scripts/score.py only
benchmarks: {alignment_notes: [], executive_line: ""}  # from valor-benchmark-alignment; shown above the executive tree
```
Features may instead live in their own feature FVRs whose `record.epic_key` matches; pass them to the script after the epic file.

## Field rules
- Any unknown numeric field holds the string `REQUIRES VALIDATION` or `null`, never a guess.
- `results` is written only by the calculation script.
- `evidence_tier` is the lowest tier of any input used in the headline benefit.
- Every edit adds a `revision_log` entry.
