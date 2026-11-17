# Domain Pack — Facilities Management (B2B and B2C)

Status: **[draft — requires validation with FM Operations, Commercial, HR, Payroll and Finance]**. Drafted from the FM employee app session (attendance and time). Contains reasoning structures and placeholders only. No client figures.

## 1. Core processes
Bid and mobilisation → Contract and SLA set-up → Manpower deployment and rostering → Attendance and time capture → Work orders (planned, reactive, inspections) → Supervision and quality checks → Client reporting and sign-off → Invoicing (fixed fee, manpower hours, or per job) → Deductions, penalties and disputes → Payroll and overtime → Asset and consumables management → B2C service requests (homes, communities).

## 2. Stakeholders
Site staff (cleaners, technicians, security, hard and soft services) · Site supervisors · Planners and schedulers · Contract and account managers · Commercial / bids · Payroll and HR · Clients' facility managers (external) · B2C residents and homeowners · Subcontractors · Finance.

## 2a. Operating-model variables (establish first)
- **Billing model per contract:** fixed monthly fee · manpower hours · per job or call-out · mixed. Decides whether better time data changes revenue at all.
- **Contract terms on fixed fee:** deductions for short staffing or SLA misses · invoice released only after client sign-off of attendance or reports. **Ask this immediately after the billing question.** If neither applies, accurate hours do not change revenue on fixed-fee contracts.
- **Workforce profile:** own staff vs subcontracted; phone ownership and literacy; languages. Decides whether app-based capture is realistic and where assisted capture is needed.
- **Labour rules:** working-hour limits, rest and seasonal outdoor-work rules, wage-protection payroll. Attendance data is evidence for compliance.

## 3. Value drivers and VALOR mapping

| Domain value driver | Typical VALOR pillar | Notes |
|---|---|---|
| Paid hours not worked (padding, buddy clocking, unverified overtime) | P02 | CS. **Count only unverified or unworked hours, never all overtime**; approved overtime for real work is not a saving |
| Deductions for short staffing that proof would have contested | P01 | Revenue retained; only deductions where staff were present but unproven. Real shortfalls stay deducted |
| Invoice released sooner after sign-off | P02 | Working capital: one-off cash timing, shown separately |
| Billable hours or call-outs captured (hourly and per-job contracts only) | P01 | RV; zero on fixed-fee contracts |
| SLA compliance (response and fix times) | P01 / P03 | Penalties avoided; renewals |
| Technician productivity (jobs per shift, first-time fix) | P02 | Usually CR unless headcount, subcontract or overtime spend actually falls |
| Labour-law compliance (hours, rest, wage protection) | P03 | RR; frequent proxies such as breaches flagged per month |
| Contract renewal and retention | P01 | Slow; long-run proof only |

## 4. Causal relationships
- Site clock-in plus daily supervisor approval → hours paid match hours worked → lower paid-but-unworked hours. **Only the unverified share falls; approved overtime may not.**
- Attendance proof → contested deductions won → revenue retained. **The same proof also exposes real shortfalls, so deductions may rise at first.** Commercial confirms the net effect.
- Daily proof → client sign-off sooner → invoice sooner (cash timing, never added to annual P&L).
- **Value-concentration check:** the largest hourly workforce (cleaning, soft services, labour) is often the least app-ready. Design assisted capture (supervisor or kiosk clock-in) or the value will not land.
- **Hidden worse-off group:** account managers, whose accounts show more deductions once real shortfalls are visible. Expect resistance unless targets are adjusted for the first quarters.

## 5. Metric definitions

| Metric | Formula | Notes |
|---|---|---|
| Shifts clocked in on the app | shifts with app clock-in at site ÷ rostered shifts | Leading; by site and service line |
| Hours approved same day | hours approved ≤ 24h ÷ hours worked | Leading |
| Unverified overtime hours per employee | overtime hours without approved clock-in ÷ employees | Lagging; split from approved overtime |
| Disputed deductions lost | value of short-staffing deductions not overturned ÷ month | Lagging; by contract |
| Days from month-end to invoice | median(invoice date − period end) | Cash timing |
| Multiple clock-ins from one device | clock-ins sharing a device within minutes ÷ clock-ins | Watch-out |
| Bulk approvals | approvals of a full crew in one action without edits ÷ approvals | Watch-out |

## 6. Evidence sources (confirm system names with client)
HR and payroll system · Rostering or workforce system · CAFM / work-order system · Site registers and biometric devices · Client sign-off records · Invoicing and deduction logs · Contract register (billing model and terms).

## 7. Unit-economics placeholders (Finance supplies values)
- Paid hours not worked, by service line: `REQUIRES VALIDATION — Payroll`
- Short-staffing deductions, contested and lost, by contract: `REQUIRES VALIDATION — Commercial`
- Contracts by billing model and terms: `REQUIRES VALIDATION — Commercial`
- Loaded hourly cost by grade: `REQUIRES VALIDATION — HR / Finance`
- Cost of capital for cash timing: `REQUIRES VALIDATION — Group Finance`

## 8. Misleading proxies
- App downloads or registered users (activity, not hours captured).
- Total overtime reduction (includes legitimate work).
- Total deductions (includes real shortfalls).
- "Billable hours captured" on fixed-fee contracts.

## 9. Unintended consequences (guardrail candidates)
- One phone clocking in several people.
- Supervisors approving in bulk without checking.
- Staff without usable phones left out, or forced onto their personal phones.
- Location tracking beyond working hours or without consent.
- Real shortfalls exposed, deductions up at first.

## 10. Worked examples
- FM employee app, attendance and time (simulation, 18 Oct 2026).
- Facilities employee app epic: check-in, work management, leave and timesheets (coach session, 20 Oct 2026). Added register KPIs FMB-BL-03 to BL-06 and FMB-BG-10 to BG-12.

## 11. Previously rejected reasoning

| Claim | Why rejected | Better framing |
|---|---|---|
| "Bill every hour we deliver" on fixed-fee contracts | Hours don't change a fixed invoice | Deductions contested with proof; invoice released sooner |
| "Overtime falls" counted as a saving | Some overtime is real work | Count unverified or unworked hours only |
