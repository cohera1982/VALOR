# Domain Pack — Property Management (leasing and tenancy)

Status: **[draft — requires validation with Property Management Leasing, Asset Management and Finance]**. Contains reasoning structures and placeholders only. No client figures.

## 1. Core processes
Listing & marketing → Enquiry & viewing → Application & tenant screening (KYC) → Offer & acceptance → Lease drafting & signing → Tenancy registration (per local rules) → Move-in & handover → Rent collection → Maintenance & service requests → Renewal or exit → Move-out, inspection & deposit settlement → Unit turnaround (refurbish, re-list).

## 2. Stakeholders
Prospective tenants · Current tenants · Brokers and agents (external channel, often commission-based) · Leasing team · Property / facilities managers · Maintenance contractors · Asset Management (portfolio strategy) · Finance (rent roll, receivables) · Compliance / Legal (tenancy and identity rules) · Owners or investors.

## 2a. Operating-model variables (establish first)
- **Portfolio mix:** residential vs commercial vs retail. Lease length, vacancy cost and renewal behaviour differ sharply.
- **Channel mix:** direct vs broker-led leasing. Broker-led means adoption depends on agents changing behaviour.
- **Occupancy level:** a near-full portfolio gains less from faster leasing than one with high churn or vacancy.
- **Lease and payment terms:** annual upfront, cheques or monthly. This changes working-capital effects.

## 3. Value drivers and VALOR mapping

| Domain value driver | Typical VALOR pillar | Notes |
|---|---|---|
| Vacant days per unit (turnaround + leasing time) | P01 | The core revenue lever: rent per unit-day × days avoided |
| Applicant-to-lease conversion | P01 | Drop-outs matter only through the vacant days they cause (see replaced-tenant rule) |
| Renewal / retention rate | P01 | Renewal avoids vacancy *and* re-letting cost; strong lever |
| Rent collection and arrears | P01 / P02 | Working capital (WC) and bad-debt reduction (CA) |
| Leasing and admin effort per lease | P02 | Usually CR unless staffing or agency costs actually fall |
| Broker commission and marketing cost per lease | P02 | Cash saving if a channel shifts to direct |
| Maintenance response and cost | P02 | Planned vs reactive; affects tenant satisfaction and renewal |
| Tenant experience | P01 / NF | Tie to renewal before monetising |
| Identity, fraud and regulatory compliance | P03 | RR; rare events, so use a frequent proxy |
| Digital tenant journey and data | P05 secondary | Enabler; value lands in the pillars above |

## 4. Causal relationships
- Faster screening and signing → shorter time to lease → fewer vacant days → more rent collected. Holds only where units are vacant or about to be.
- Fewer applicant drop-outs → fewer re-marketing cycles → fewer vacant days. **Replaced-tenant rule:** a lost applicant is usually replaced by another tenant later. The value is the *extra vacant days* the loss caused, never a full year's rent.
- Faster signing and fewer drop-outs are **two routes to one benefit** (vacant days). Measure both; count the benefit once.
- Better tenant experience → higher renewal → avoided vacancy and re-letting cost. Renewal effects take a full lease cycle to show.
- Online identity checks → fewer forged or borrowed identities → lower fraud, arrears and legal exposure. Rare events; use failed or flagged checks as the fast proxy.

## 5. Metric definitions

| Metric | Formula | Notes |
|---|---|---|
| Vacant days per unit | Σ days unit not under lease ÷ units | Split turnaround days (refurb) from leasing days |
| Applicant-to-lease conversion | signed leases ÷ accepted applicants | By channel (direct vs broker) |
| Drop-out rate by stage | applicants stopping at stage ÷ entering stage | Needs stage tracking in CRM |
| Days acceptance → signature | median(signed date − acceptance date) | Report P50 and P90 |
| Occupancy rate | leased units ÷ lettable units | Physical vs economic occupancy |
| Renewal rate | renewals ÷ leases expiring | |
| Arrears rate | overdue rent ÷ rent due | Define overdue threshold |
| e-KYC completion rate | completed online ÷ started | Without staff help |
| Manual review rate | checks sent to manual review ÷ checks | Watch for false rejections |

## 6. Evidence sources (confirm system names with client)
Property management system (lease, unit, rent roll) · CRM / leasing pipeline · Broker portal · e-KYC vendor dashboard · Finance GL and receivables · Tenancy registration records · Maintenance / CAFM system · Tenant surveys and complaints.

## 7. Unit-economics placeholders (Finance supplies values)
- Rent per unit-day, by property type: `REQUIRES VALIDATION — Finance`
- Re-letting cost per lease (marketing, commission, turnaround): `REQUIRES VALIDATION — Leasing / Finance`
- Leasing staff loaded cost per hour: `REQUIRES VALIDATION — HR / Finance`
- e-KYC vendor cost per verification: `REQUIRES VALIDATION — Procurement`
- Average arrears write-off per case: `REQUIRES VALIDATION — Finance`

## 8. Misleading proxies
- Applications received (volume, not leases).
- Full annual rent of "saved" tenants (breaks the replaced-tenant rule).
- Occupancy in a near-full portfolio (little room to move).
- e-KYC checks completed (activity, not conversion).
- Tenant app downloads.

## 9. Unintended consequences (guardrail candidates)
- Genuine tenants wrongly rejected or stuck in manual review.
- Abandonment of the online step, especially by older or non-digital tenants.
- Brokers bypassing the process and keeping paper.
- Vendor per-check fees outgrowing manual cost.
- Data protection exposure from stored identity documents.

## 10. Worked examples
- e-KYC for tenants → `examples/coach-dialogue-ekyc-tenants.md` in the valor-value-coach skill

## 11. Previously rejected reasoning
| Date | Claim | Why rejected |
|---|---|---|
| 2026-10-18 | "Each prevented drop-out = one year's rent" | Replaced-tenant rule: value is extra vacant days only |
| 2026-10-18 | "Faster signing saves X days AND fewer drop-outs saves Y days, add them" | Two routes to one benefit; count vacant days once |
