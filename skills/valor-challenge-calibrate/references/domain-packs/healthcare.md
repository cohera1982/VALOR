# Domain Pack — Healthcare (clinics and hospitals)

Status: **[draft — started from the patient management simulation; requires validation with Medical Director, Operations, Revenue Cycle and Finance]**. Reasoning structures and placeholders only. No client figures.

## 1. Core processes
Appointment booking and access → Pre-registration and eligibility (insurance) → Arrival, check-in and triage → Consultation and orders (lab, radiology, pharmacy) → Results and clinician sign-off → Follow-up and care plans → Billing, coding and e-claims → Claim submission, rejection handling and resubmission → Collections (patient and payer) → Patient feedback and complaints.

## 2. Stakeholders
Patients and carers · Doctors and nurses · Front desk and contact centre · Revenue cycle (coding, claims, collections) · Insurers and e-claims platforms (external) · Medical Director · Quality and patient safety · Data protection officer · Health regulator (licensing, inspections).

## 2a. Operating-model variables (establish first)
- **Payer mix:** insured vs self-pay. Decides whether claim quality or patient payment is the cash lever.
- **Setting:** outpatient clinics vs hospital (inpatient, emergency). Throughput and follow-up dynamics differ.
- **Clinician model:** employed vs visiting doctors. Visiting doctors are harder to move onto new systems.
- **Patient mix:** age and digital literacy. Decides how much a patient app can carry, and who must keep an assisted route.

## 3. Value drivers and VALOR mapping

| Domain value driver | Typical VALOR pillar | Notes |
|---|---|---|
| Patient access and slot utilisation | P02 (asset utilisation) | Revenue only if demand fills recovered slots |
| No-show and late cancellation reduction | P02 / P01 | Same capacity logic as above |
| Follow-up completion and patient retention | P01 (customer lifetime value) | Clinical and financial at once; count returning-patient revenue once |
| Claim first-pass acceptance and denial reduction | P01 (pricing and yield, revenue leakage) | Often the largest, most bankable value of a patient management system |
| Days in accounts receivable | P02 (working capital) | Cash timing; never added to annual value |
| Front-desk and coding effort | P02 (process automation) | Time freed, not savings, unless cost is removed |
| Patient safety and data protection | P03 (regulatory compliance) | Risk reduction; rare events need frequent proxies |
| Digital front door (app, portal) | P01 (digital channels and CX) | Value lands in access, retention and claims, not in downloads |

## 4. Causal relationships
- Self pre-registration and check-in → shorter on-the-day waits → better experience → more follow-ups kept and patients retained.
- Results released quickly **only if clinicians sign off in the system during or soon after the visit**. Clinicians hold most of the value and are the hardest group to change (value concentration vs adoption).
- Accurate registration and eligibility data → fewer claim rejections → more revenue collected and faster cash. Faster cash is cash timing; recovered rejections are revenue retained. Never add them together.
- Follow-ups kept and patients retained overlap: count returning-patient revenue once.

## 5. Metric definitions
See register area "Healthcare" (HCR-…) for definitions, formulas and owners.

## 6. Evidence sources
Patient management system / HIS · EMR · Appointment system · Patient app analytics · Revenue cycle and e-claims platform · Patient surveys and complaints · Incident reporting system.

## 7. Unit-economics placeholders
- Average revenue per outpatient visit, by specialty: `REQUIRES VALIDATION — Finance`
- Value of rejected claims and recovery rate: `REQUIRES VALIDATION — Revenue Cycle`
- Front-desk loaded cost per hour: `REQUIRES VALIDATION — HR / Finance`

## 8. Misleading proxies
- App downloads or registrations (not visits booked or follow-ups kept).
- Total claims submitted (volume, not first-pass acceptance).
- Average satisfaction without the older or non-app patient segment.

## 9. Unintended consequences (guardrail candidates)
- Older or non-digital patients receive worse service.
- Desk queues move to app support calls.
- Duplicate or wrong patient records cause clinical risk and claim rejections.
- Clinicians double-document (paper and system).

## 10. Worked examples
- Patient management app and system (simulation, 18 Oct 2026).

## 11. Previously rejected reasoning
| Date | Claim | Why rejected |
|---|---|---|
| 2026-10-18 | "Patients retained and follow-ups kept, added together" | Same visits counted twice |
