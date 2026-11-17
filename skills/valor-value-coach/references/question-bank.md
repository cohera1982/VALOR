# Question Bank

Ask one at a time. Each question has plain wording, quick options (adapt to the domain pack), and a rescue prompt for when the user is stuck.

## 1. The day after
**Ask:** "Imagine this has been live for a month. What's different?"
**Options:** Things happen faster · Fewer mistakes, breakdowns or incidents · We sell or earn more · People's day gets easier or safer · Something else
**Stuck?** "What do people complain about today that this would fix?"

## 2. Today
**Ask:** "What happens today when [the situation] occurs?" (multi-select)
**Options (adapt):** Someone handles it manually · It often goes unnoticed · We find out later, from reports, audits, fines or complaints · Not sure
**Why it matters (internal):** manual today → gain is speed, coverage and time freed; unnoticed today → gain is risk caught; found later → gain is avoided penalties or incidents.
**Stuck?** "If this happened right now, who would find out, and how?"

## 3. What has to work differently
**Ask:** "For that to happen, who has to do something differently?"
**Options:** A team changes how it works · Drivers, customers or staff have to respond to something · The system acts automatically · Not sure yet
**Probe once if "automatic":** "If everyone carried on exactly as today, would anything improve?"
**If they describe stages** (notify, then call, then block): play back the stages and note each one's owner.
**If people must accept or respond:** that response becomes "Is it being used?".

## 4. Which kind of gain, then branch
**Ask:** "Does that mostly make something cheaper, faster, sell more, or safer?" (multi-select allowed)
**Options:** Cheaper · Faster or frees time · Sell more · Safer or more compliant · Better for staff or customers

### Branch: time freed
"If [team] no longer does this, what happens to that time?"
Options: Redeploy to other work · Cut overtime or shifts · Absorb growth without hiring · Not sure yet (owner: the team's manager)
→ Only "cut overtime or shifts" or "absorb growth" (with a growth plan) can become money, and only with a named owner.

### Branch: sell more
"Is there demand waiting for it? How do we know?"
Options: We've seen it in our own data · Customers or staff tell us · It's a hunch so far · Not sure

### Branch: safer or compliant
"How often does the problem happen today, and what does one occurrence lead to?"
Options: Fines or penalties · Injuries or accidents · Insurance claims · Reputation or regulator attention · Not sure
→ Note frequency and consequence as to-dos with owners (Compliance, Health & Safety). Expect the outcome to be rare, so plan a frequent proxy measure (see "Fast evidence vs long-run proof").

### Branch: cheaper
"Which bill gets smaller, and who'd confirm it?"
Options: A supplier or contractor cost · Overtime or staffing · Fuel, parts or materials · Not sure

## 5. How we'd know
**Ask:** "What would we look at to see it working?"
**Offer** 3–4 measures from the domain pack in everyday words, with at least one that moves within weeks. Let the user pick any number; never cap the selection.
**Stuck?** "If you had to prove it to the CEO with one number, which would it be?"

## 6. What could go wrong (multi-select)
**Ask:** "What would tell us it's backfiring?"
**Always include at least one trade-off option** (lost revenue, extra work elsewhere, slower service) alongside risk options (people ignore it, workarounds, wrong alerts), so unpicked trade-offs can be carried to the card.
**Stuck?** "What's the worst headline about this feature six months from now?"

## Numbers, gently
If the user offers a number: "Great. Where does that come from?" If unknown: "No problem; who could confirm it?" Never supply a number yourself.

## Encouragements (sparingly, when earned)
- "That's the crucial link."
- "Good, that's exactly what Finance will ask."
- "Not knowing that yet is normal. I've noted who can confirm it."

## 7. Owners card (epic sessions)
**Ask:** "Who is accountable for this value, and who owns each measure?" If the user already said they own the epic, pre-fill them as Value Owner and ask only for their name and the measure owners.
**Measure owners in one answer.** List a suggested owner per measure, numbered, with options: "Accept all" · "Change: [number] — [new owner]" (e.g. "Change: 2 — Head of Commercial"; several allowed, comma-separated). The edit is made in the same reply. If the user picks "Change" without naming anyone, don't ask again: keep the suggestions as "to confirm — Value Owner" and say so in one line.
**Options:** the likeliest Business SVP as Value Owner (from the domain pack or the conversation) · a named measure owner per outcome KPI (e.g. Head of Customer Service for CSAT) · "Not decided yet"
**Rule:** the Value Owner and the KPI Owner must be different people. If the user names the same person: "The KPI Owner checks the Value Owner's numbers, so it needs to be someone else. [Likeliest alternative]?" "Not decided" becomes a requested agreement routed to the BU CEO.
**Stuck?** "Whose budget or target moves if this works? And who already reports that number?"

## 8. Financial range card (epic sessions)
**Ask:** "Is there a financial outcome we expect, roughly?"
**Options:** Give a rough range · No financial outcome claimed · Not sure yet (owner: Finance business partner)
**Then, if a range is given:** "Where does that come from?" Record a range with no named source as "asserted — source to supply ([who])". If the user gives a single figure, ask once: "What would the low and high ends be?"; if they can't say, record "about [figure], range to confirm — Finance business partner". Never supply or suggest a money figure.
**Approval tier (say it in one definite line):** if the epic's cost or the top of its expected range is at or above P01 → the BU CFO approves before execution; only if both are below P01 → the Head of IT approves as the CFO's written delegate, with the Finance business partner consulted. If P01 is not set: "The approval threshold isn't set yet; Finance confirms it, and the BU CFO approves meanwhile."
**Also ask, on the same card:** "Roughly what will the epic cost?" Options: I'll give a figure · Not sure yet (owner: ITBP). The tier needs both cost and outcome.
**Combine with the owners card (§7) on one card in epic sessions.**

## 9. Where is this in the cycle? (ask only if the mode isn't clear)
**Ask:** "Where is this in the cycle?"
**Options:** Annual planning or new demand · About to start delivery · Setting targets before Portfolio Forum · Planning features for the next cycle · It's just gone live
→ annual definition · execution entry · target setting · feature · value realised (`SKILL.md`, five modes)

## 10. Target-setting card (target-setting mode)
**Ask:** "Now that the solution is clear, what do you expect for [KPI]?" Show the measured baseline and the suggested range first.
**Options:** Keep the suggested range · Tighter: [narrower range] · Different, I'll say · Not sure yet (owner: KPI Owner)
**Then:** "By when?" and "What's the first sign it's working?" (one or two early signals).
**Stuck?** "If this went as well as you can realistically imagine, where would [KPI] be in two quarters?"

## 11. Value-realised cards (after a go-live)
1. "Which release went live, and when?"
2. "Is it being used? What does the data show so far?" Options: Above what we expected · About right · Below · Too early to tell
3. "Has the outcome moved yet?" Options: Yes, I'll give the numbers · Not yet, it's early · Not sure (owner: KPI Owner)
4. "Which benefits can we count now?" Show the epic's benefits with counting labels; mark each Counted · To confirm · Not yet
**Rule:** attribute at epic level; financial results go to the BU CFO, non-financial to the KPI Owner.

## 12. Which epic KPI does this feature move? (feature sessions, one card with the share)
**Ask:** "Which of [epic]'s outcome measures will this feature move?" (the share follows on the same card, below) Show only the epic's outcome KPIs as the record or the user gave them; if they aren't known, ask for them first (SKILL.md 0a) and never guess.
**Options:** each epic outcome KPI · "None of these really" · "Not sure"
**If "None of these":** "Then the epic may need another outcome. I'll ask [Value Owner] and [KPI Owner]." Log a requested agreement; the feature still gets its own "is it being used?" measure.
**Then, on the same card:** "Roughly what share of that movement comes from this feature?" Options: Most of it · About half · A smaller part · Not sure yet (owner: Value Owner)

## 13. Cross-business epics: what does each business get? (epic sessions)
**Ask:** "What does each business get from this?" One line per business named.
**Options per business:** Retire a system or licence · Stop a planned build · More conversions or sales · Only part of the journey (partial) · Not sure (owner: that business's Value Owner)
**Rule:** each business's benefit keeps its own value type and is counted once; "partial" carries into the hypothesis wording.
