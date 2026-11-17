# Domain Pack — Mobility: Taxi Operations

Status: **[draft — requires validation with Mobility-Taxi Operations and Finance]**. Contains reasoning structures and placeholders only. No client figures.

## 1. Core processes
Fleet acquisition & retirement → Vehicle maintenance (planned / unplanned) → Driver onboarding, rostering & performance → Dispatch & booking (street hail, app, corporate accounts, airport) → Trip execution & fare collection → Customer service & complaints → Regulatory compliance (licensing, inspections, RTA-type requirements) → Fuel / energy management → Claims & incidents.

## 2. Stakeholders
Drivers (employed or franchise; check the model — it changes who captures value) · Fleet & maintenance teams · Dispatch / control centre · Customers (retail, corporate, airport) · Regulator · Finance · BU CEO · Group CoEs (Data, AI, Digital).

## 2a. Operating-model variables (establish first; they change who captures value)
- **Driver commercial model:** salaried, commission, vehicle-rental or franchise. Decides whether an extra shift adds company margin, driver income or both, and whether an idle driver costs the company money.
- **Shift model:** single-shift or double-shift (two drivers share one vehicle on complementary shifts). Double-shift utilisation depends on pairing, so partner allocation is a core lever.
- **Fixed per-driver costs:** accommodation, permits, insurance, transport. These continue when a driver is idle.
- **Depot structure:** pairing and allocation are usually depot-bound.

## 3. Value drivers and VALOR mapping

| Domain value driver | Typical VALOR pillar | Notes |
|---|---|---|
| Fleet availability (vehicle-days on road) | P02 or P01 | P01 only if demand exists to absorb added availability |
| Revenue per vehicle-day | P01 | Driven by utilisation, fare mix, dead-km |
| Utilisation (paid km ÷ total km) | P02 / P01 | Dead-km reduction is a cost lever; more paid trips is revenue |
| Maintenance cost per km | P02 | Planned vs unplanned mix matters |
| Fuel/energy cost per km | P02 | Watch confounders: fuel price, EV transition |
| Vehicle shift fill rate (double-shift) | P02 / P01 | Shifts worked ÷ (available vehicles × 2 × days); revenue only with demand at those shift times |
| Driver productivity & retention | P04 | Retention affects recruitment and training cost |
| Customer experience (wait time, completion, complaints) | P01 / P06 | Often NF unless tied to corporate contracts |
| Safety & compliance (duty hours, fatigue) | P03 | Usually RR or NF; overruns per 1,000 shifts as the fast measure |
| Data/AI capability (dispatch optimisation, predictive maintenance) | P05 secondary | Primary driver sits with the operational outcome (see P05 trap) |

## 4. Causal relationships
- Unplanned breakdown → vehicle off road → lost shift → lost revenue *only if* demand would have been served (check peak vs off-peak, spare-vehicle pool).
- Predictive alert → planned intervention → shorter repair and parts at planned cost → lower maintenance cost per km. Requires workshop capacity to act on alerts.
- Dispatch optimisation → lower dead-km → lower fuel cost and/or more trips per shift. The two claims overlap; choose one primary.
- Wait time ↓ → completion rate ↑ → revenue ↑ (app bookings). Street hail is weakly affected.
- Driver retention ↑ → recruitment/training cost ↓ and experienced-driver productivity ↑.

## 5. Metric definitions (normalise exposure)

| Metric | Formula | Denominator note |
|---|---|---|
| Unplanned repair visits per 100k vehicle-km | unplanned visits ÷ total vehicle-km × 100,000 | Use km, not vehicles, to control for usage |
| Unplanned downtime hours per 100k vehicle-km | hours off-road from unplanned events ÷ vehicle-km × 100,000 | Define "off-road" start/stop |
| Fleet availability % | vehicle-days available ÷ vehicle-days in fleet | Exclude vehicles in retirement |
| Utilisation % | paid km ÷ total km | |
| Revenue per available vehicle-day | fare revenue ÷ available vehicle-days | |
| Booking completion % | completed ÷ accepted bookings | App/corporate channels |
| Mean pickup wait (min) | avg(pickup − request) | Report P50 and P90 |
| Maintenance cost per km | maintenance spend ÷ vehicle-km | Split planned / unplanned |
| Driver attrition % (annualised) | leavers ÷ avg headcount | |

### Partner allocation causal chain
Idle driver + open shift slot → offer → acceptance (depends on shift fit, depot, language, pay impact) → stable pair → filled shift → revenue only if demand exists at that time. Freed capacity can alternatively support fleet right-sizing; never claim both.

### Duty hours and fatigue
Driver exceeds duty limit → fatigue risk ↑ → incident probability ↑ and regulatory breach. Overruns are frequent and measurable (telematics vs roster); incidents are rare. Use overruns per 1,000 shifts as the fast measure and incidents as long-run proof. Interventions often escalate (notify → control-room call → trip block); measure the share resolved at each stage. Trade-off to check: fewer end-of-shift trips.

## 6. Evidence sources (confirm system names with client)
Fleet management / telematics · Workshop / maintenance system · Dispatch & booking platform · Fare / payment system · HR system · Finance GL (maintenance, fuel cost centres) · Complaints / CRM · Regulatory inspection records.

## 7. Unit-economics placeholders (Finance supplies values)
- Average unplanned repair cost: `REQUIRES VALIDATION — Fleet Finance`
- Average planned repair cost (same fault class): `REQUIRES VALIDATION`
- Contribution margin per vehicle-day *at the margin* (not average revenue): `REQUIRES VALIDATION — BU Finance`
- Fuel/energy cost per km: `REQUIRES VALIDATION`
- Driver recruitment + training cost: `REQUIRES VALIDATION — HR`
- Cost of tow / roadside event: `REQUIRES VALIDATION`

## 8. Misleading proxies
- Alerts generated or model accuracy as the value KPI (Technical Leading only).
- Fleet availability without demand: an available but idle vehicle earns nothing.
- Average revenue per vehicle-day used as the marginal value of a recovered day.
- App downloads instead of completed bookings.
- Total fuel spend (confounded by price and fleet size).

## 9. Unintended consequences (guardrail candidates)
- False alerts → unnecessary workshop interventions and parts spend.
- Over-optimised dispatch → driver fatigue, complaints, attrition.
- Aggressive maintenance windows → availability loss at peak.
- Surge or pricing changes → regulatory or reputational exposure.

## 10. Worked examples
- Taxi fleet availability epic (predictive maintenance, partner allocation, parts pre-staging) → `examples/taxi-fleet-availability-epic.yaml` in the valor-orchestrator skill
- Automated sign-off alarms (safety-led) → `examples/coach-dialogue-signoff-alarms.md` in the valor-value-coach skill

## 11. Previously rejected reasoning (log entries here)
| Date | Claim | Why rejected |
|---|---|---|
| 2026-10-18 | "Extra shifts sold AND fleet reduced, from the same matching gains" | Same capacity counted twice; alternative uses |
| [example] | "Downtime saved × average revenue per vehicle-day" | Assumed every recovered hour is sold; average not marginal; overlapped with dispatch-optimisation claim |
