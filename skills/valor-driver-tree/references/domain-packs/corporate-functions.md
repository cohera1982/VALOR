# Domain Pack — Corporate Functions and GBS (HR, Finance, Procurement, Legal, Government Relations)

Status: **[draft — requires validation with Group HR, Government Relations / PRO, Finance, Legal and GBS]**. Drafted from the visa management session (19 Oct 2026). Contains reasoning structures and placeholders only. No client figures. Country-specific rules are flagged for Legal to confirm per jurisdiction.

## 1. Core processes
Hire to retire (recruitment, onboarding, payroll, leave, exit) · Immigration and government relations (visas, work permits, residence IDs, labour cards, renewals, cancellations) · Record to report · Procure to pay · Contract and legal matters · Employee services and requests · GBS shared services and chargeback to businesses.

## 2. Stakeholders
Employees and dependants · BU HR partners · HR operations · Government Relations / PRO team · Outsourced PRO agencies · Payroll · Finance and GBS · Legal and compliance · Line managers · Government authorities (external).

## 2a. Operating-model variables (establish first)
- **Who does the work:** in-house team · GBS (and whether GBS charges businesses per transaction) · outsourced agency (per-transaction fee). Decides whether effort saved is time freed or money.
- **Chargeback:** if GBS charges each business per transaction, fewer transactions are real cost to the business even when GBS time is only redeployed.
- **Jurisdictions:** which countries' immigration and labour rules apply. Penalties and obligations differ by country; never assume one country's rules.
- **Population size and churn:** employees under visa sponsorship, renewals per year, joiners and leavers. Sets the scale of every benefit.

## 3. Value drivers and VALOR mapping

| Domain value driver | Typical VALOR pillar | Notes |
|---|---|---|
| Fines for lapsed visas, late renewals or late cancellations | P03 / P02 | CA; count only fines caused by the process the feature fixes, confirmed by Finance |
| **Restrictions on the company itself** after repeated violations (e.g. a blocked establishment record stopping new hiring or renewals) | P03 | RR; often the largest exposure. **Rules vary by country: Legal confirms per jurisdiction before it enters the case** |
| Employee days unable to work or travel (lapsed status, passport held, pending renewal) | P03 / P04 | Tracked in natural units; monetise only with a cost-per-day agreed with Finance |
| HR, PRO or GBS effort (chasing, re-keying, follow-ups) | P02 | CR unless an agency fee, temp or planned hire actually stops; chargeback makes it real cost to the business |
| Agency fees per transaction | P02 | CS when transactions or fees fall |
| Employee experience (fewer trips, no chasing) | P04 | NF; measured in its own terms |
| Audit and data protection (passport and ID data) | P03 | RR; access logs, retention |

## 4. Causal relationships
- Early alerts plus one work queue → renewals started 60–90 days before expiry → fewer lapses → fewer fines, fewer lost working days, and lower risk of restrictions on the company.
- Employee self-upload → fewer email chases → time freed. **Becomes money only through an agency fee, temp, avoided hire or GBS chargeback.**
- **Attribution split:** delays at government portals sit outside the company's control. Split "renewed before expiry" by where the delay sat, so the system is not credited or blamed for authority delays.
- **Value-concentration check:** lapses concentrate in blue-collar and frequently travelling populations, often the least able to self-upload. Design an assisted route (HR desk, supervisor upload) for them.

## 5. Metric definitions

| Metric | Formula | Notes |
|---|---|---|
| Renewals completed before expiry | renewals completed before expiry ÷ renewals due | By BU and population; split by delay location |
| Renewal alerts raised on time | visas with an alert ≥ 60 days before expiry ÷ visas expiring | System KPI; target no misses |
| Employee self-upload rate | renewals with documents submitted by the employee ÷ renewals | Leading |
| Lapse fines | count and value per quarter, by cause | Finance; only process-caused fines count |
| Days unable to work or travel | employee-days with lapsed or pending status | Natural units |
| Expiry data accuracy | records verified against source documents ÷ records | Sprint check before go-live |

## 6. Evidence sources (confirm system names with client)
HRIS · Visa or immigration tracker (today often spreadsheets) · Government portals and receipts · Finance GL (fines, agency fees) · GBS ticketing and chargeback · Email archives for baseline effort.

## 7. Unit-economics placeholders (Finance supplies values)
- Lapse and late-renewal fines, last 12 months, by cause and country: `REQUIRES VALIDATION — Finance with HR`
- Agency fees per transaction: `REQUIRES VALIDATION — Procurement`
- GBS chargeback rates per transaction: `REQUIRES VALIDATION — GBS / Finance`
- Cost per employee-day unable to work: `REQUIRES VALIDATION — Finance`
- Company-level restriction exposure, per jurisdiction: `REQUIRES VALIDATION — Legal`

## 8. Misleading proxies
- Applications logged in the system (activity, not renewals on time).
- Total fines (includes causes the feature doesn't touch).
- HR hours saved, reported as cost savings without a conversion.

## 9. Unintended consequences (guardrail candidates)
- Alerts raised but ignored until the last week.
- Expiry dates migrated wrongly, so alerts fire late or not at all.
- Employees don't upload; HR chases by email anyway.
- Passport and ID data visible to more people than need it.
- Authority delays blamed on the system.

## 10. Worked examples
- Visa management system (simulation, 19 Oct 2026).

## 11. Previously rejected reasoning

| Claim | Why rejected | Better framing |
|---|---|---|
| "HR saves N hours, so we save N × cost" | In-house time is not cash unless something stops | Time freed for named work; money only via agency fee, temp, avoided hire or chargeback |
| "Fines fall" counted from total fines | Includes causes outside the process | Process-caused fines only, confirmed by Finance |
