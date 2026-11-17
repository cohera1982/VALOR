# Domain Pack — Foods & Resources (CPG manufacturing and distribution)

Status: **[draft — requires validation with Foods Sales, Distribution, Credit Control and Finance]**. Contains reasoning structures and placeholders only. No client figures.

## 1. Core processes
Demand planning & forecasting → Procurement of raw and packaging materials → Production & quality → Warehousing & inventory (FEFO) → Order capture (sales reps, van sales, EDI, B2B portal) → Route planning & dispatch → Delivery & proof of delivery → Invoicing → Credit control, disputes & collections → Returns, expiry & waste → Trade promotions & retailer terms → Sales performance & customer service.

## 2. Stakeholders
Modern trade key accounts (hypermarkets, supermarkets, chains) · Traditional trade (groceries, small outlets) · HoReCa and B2B customers · Sales reps and van salesmen · Drivers and distribution · Warehouse · Credit control / accounts receivable · Key Account Managers · Trade marketing · Production & quality · Finance · Customers' receiving staff (external).

## 2a. Operating-model variables (establish first)
- **Channel mix:** modern vs traditional trade vs HoReCa. Disputes, payment terms, adoption and margin differ sharply by channel.
- **Route-to-market:** own fleet, van sales, distributors or 3PL. Decides who must change behaviour and who captures value.
- **Payment terms:** cash on delivery vs credit terms (often long with key accounts). Decides whether cash timing matters.
- **Key-account processes:** retailers often impose their own goods-received, invoicing and deduction processes; assume they won't change for you unless confirmed.

## 3. Value drivers and VALOR mapping

| Domain value driver | Typical VALOR pillar | Notes |
|---|---|---|
| Revenue leakage: disputes, deductions, credit notes conceded | P01 / P02 | Cash retained; count only conceded amounts that proof would have won |
| Days sales outstanding (DSO), disputed receivables | P01 / P02 | Working capital (WC): one-off cash timing, never added to annual P&L |
| On-time-in-full (OTIF) | P01 | Retailer penalties and lost listings; tie to fines or volume before monetising |
| Fill rate and lost sales from stock-outs | P01 | Needs evidence that demand went unserved |
| Forecast accuracy | P02 / P01 | Value lands in inventory, waste and stock-outs, not accuracy itself |
| Inventory days, expiry and waste write-offs | P02 | CS when write-offs fall; check FEFO discipline |
| Cost to serve per drop or case | P02 | Drops per route, fuel, drop time |
| Trade spend effectiveness | P01 | Incremental volume vs baseline; promotions are hard to attribute |
| Back-office effort (scanning, reconciliation, order entry) | P02 | Usually CR unless headcount, temps or overtime actually fall |
| Food safety and traceability | P03 | RR; rare events, so use frequent proxies (holds, non-conformances) |

## 4. Causal relationships
- Durable proof of delivery → disputes settled with evidence → fewer credit notes conceded (P&L) and faster payment on disputed invoices (one-off cash). **Two categories; never sum.**
- **Value-concentration check:** disputes and deductions concentrate in modern trade, which is also the channel least likely to adopt your process. Design for that channel's constraints (e.g. photograph their goods received note) or the value won't land.
- Longer drop time (capture, signatures) → fewer drops per route → higher cost to serve. A common hidden trade-off of delivery features.
- Better forecasts → lower safety stock and fewer stock-outs → less waste and fewer lost sales. Only if planners act on the forecast.
- Promotions → volume uplift, part of which is pulled forward or cannibalised. Never claim gross uplift.

## 5. Metric definitions

| Metric | Formula | Notes |
|---|---|---|
| Delivery-dispute credit notes | value of credit notes with reason short/missing/damaged | By channel and customer; monthly |
| Dispute settlement time | median(settled date − raised date) | |
| Disputed receivables | value of invoices on hold for disputes | Snapshot; WC effect |
| DSO | receivables ÷ credit sales × days | By channel; seasonality |
| Proof-of-delivery completeness | drops with complete proof ÷ drops | By channel, route, driver |
| OTIF | orders delivered on time and in full ÷ orders | Use the customer's definition where penalties apply |
| Drops per route-day; time per drop | — | Baseline before any capture step is added |
| Waste / expiry write-off | value written off ÷ sales | By SKU family |
| Forecast accuracy | 1 − WMAPE | Value only through inventory and waste |

## 6. Evidence sources (confirm system names with client)
ERP (orders, invoices, credit notes, receivables) · Distribution or route-planning system · Van sales / POD app · Telematics · WMS · Customer portals and EDI · Deduction and claims logs from key accounts · Finance GL.

## 7. Unit-economics placeholders (Finance supplies values)
- Credit notes conceded for delivery disputes, by channel: `REQUIRES VALIDATION — Credit Control`
- Cost of capital for working-capital effects: `REQUIRES VALIDATION — Group Finance`
- Back-office loaded cost per hour: `REQUIRES VALIDATION — HR / Finance`
- Cost per drop and per route-day: `REQUIRES VALIDATION — Logistics / Finance`
- Waste write-off by SKU family: `REQUIRES VALIDATION — Finance`

## 8. Misleading proxies
- Number of PODs captured (activity, not disputes won).
- Total credit notes (includes pricing and promo deductions unrelated to delivery).
- Gross promotion uplift.
- Forecast accuracy as the value claim.
- DSO improvement reported as annual profit.

## 9. Unintended consequences (guardrail candidates)
- Drivers skip or fake capture under time pressure.
- Slower drops, fewer drops per route.
- Key accounts reject new proof formats.
- No connectivity at drop sites, so offline capture is needed.
- Personal data (signatures, photos of customer staff) stored without the right handling.

## 10. Worked examples
- Digital proof of delivery → `examples/coach-dialogue-digital-pod.md` in the valor-value-coach skill

## 11. Previously rejected reasoning
| Date | Claim | Why rejected |
|---|---|---|
| 2026-10-18 | "Faster payment on disputed invoices + credit notes avoided, summed as annual benefit" | One is one-off cash timing (WC), the other P&L; never added |
| 2026-10-18 | "All delivery credit notes will disappear" | Disputes concentrate in modern trade, where adoption of new proof is hardest |
