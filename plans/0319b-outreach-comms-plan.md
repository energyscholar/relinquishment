# Plan 0319b — ewstools Outreach Communications Plan

**Parent:** Plan 0319 (Architecture + Grant + Outreach)
**Status:** Active
**Owner:** Bruce (drafts + sends), Robin (technical backup), Bury (introductions)

## Campaign Timing (Anchored: CSSI Dec 1, 2026)

**Constraint:** Outreach launches AFTER architecture document is ready to share. The doc IS the credential.
**Today:** May 9, 2026. **Days to CSSI deadline:** 206.

| Date | Action | Who acts |
|------|--------|----------|
| May 9-16 | Architecture HTML doc complete | Bruce + Robin |
| May 16 | numpy2-compat PR resubmitted with architecture doc link | Bruce |
| May 16-18 | Doc sent to Bury for review | Bruce → Bury |
| **May 19** | **Bury call** (approve arch, discuss intros, budget, grants office) | Bruce + Bury |
| May 19-20 | Bury sends intro to **Boettiger** (highest priority — $, PST timezone, call-ready) | Bury |
| May 21-22 | Bury sends intro to **Bauch** (Bury's advisor — natural, easy ask) | Bury |
| May 20-23 | Bruce follows up Boettiger + Bauch within 24h of each intro | Bruce |
| May 23-25 | Bury sends intro to **Lenton** (£5M AdvanTip — needs Bury's weight) | Bury |
| May 26-27 | Bruce follows up Lenton (email-only likely — BST timezone) | Bruce |
| May 26-28 | Bury sends intros to **Scheffer** + **Sujith** (credibility + cross-domain) | Bury |
| May 28-30 | Tier 2 cold outreach: **Thornalley** + **Gommenginger** (£5M + £11M ARIA — MONEY) | Bruce |
| June 2-4 | Tier 2 cold outreach: **Dakos** + **O'Brien** (endorsement + interop) | Bruce |
| June 5-6 | Tier 2 cold outreach: **Dylewsky** + **Ditlevsen** | Bruce |
| June 9-20 | Calls with respondents. Log feature requests verbatim. Detect contract signals. | Bruce (Robin on standby) |
| June 23-July 4 | Phase 2 implementation begins (informed by outreach findings) | Bruce + Robin |
| July 7-15 | Second wave: follow up non-responders (ONE gentle ping). Add Tier 3. | Bruce |
| July 1-15 | Collect user statements (Template E) + Letters of Collaboration | Bruce |
| July 15-Aug 1 | Final contract conversations with anyone who signaled interest | Bruce |
| Aug 1 | Begin CSSI Project Description draft | Bruce |

**Rotation logic:** 
- North America first (calls feasible, faster response cycle)
- Bury max 2 intros/week (respects his bandwidth)
- MONEY targets clustered early (Boettiger, Lenton, Thornalley, Gommenginger)
- Credibility targets (Scheffer, Dakos) can be slightly later — their value is endorsement, not urgency
- 7-day gap between intro and Tier 2 cold emails prevents overlap confusion

## Message Templates

### Template A: Bury Introduction Email (Bury sends)

```
Subject: Introduction — Bruce Stephenson & Robin Macomber (ewstools contributors)

Hi [Name],

I wanted to introduce Bruce Stephenson and Robin Macomber, who have been
contributing to ewstools over the past few months (Python 3.12 compatibility,
DFA implementation, and now an architecture modernization proposal).

They're preparing an NSF CSSI proposal to fund a major ewstools expansion —
plugin architecture, multivariate EWS, and a cross-domain benchmarking
framework. They'd value 15 minutes of your time to understand what EWS
capabilities would be most useful to your group.

I'll let Bruce follow up directly.

Best,
Tom
```

### Template B: Bruce Follow-Up (after Bury intro)

```
Subject: Re: Introduction — ewstools modernization input

Hi [Name],

Thanks for the connection from Tom. Quick context: Robin and I have been
contributing to ewstools (PRs #462, #463, #469) and we're proposing a
plugin-based architecture that would make it easy for domain researchers to
add new EWS methods without touching the core codebase.

We're reaching out to active EWS researchers to understand:

- What methods you use that aren't in ewstools (or that you've reimplemented)
- Workflow pain points (data formats, performance, missing multivariate support)
- Whether a standardized benchmarking suite (common datasets, reproducible
  baselines across domains) would be valuable

I've attached our architecture proposal [link] — no obligation to read it,
but it shows the technical direction.

Would you have 15 minutes in the next two weeks? Happy to work around
your schedule. [Calendly link or "just reply with a few times that work."]

Best,
Bruce Stephenson
```

### Template C: Cold Outreach (Tier 2, no Bury intro)

```
Subject: ewstools expansion — seeking input from [domain] EWS researchers

Hi [Name],

I'm Bruce Stephenson — contributor to Tom Bury's ewstools package (PRs #462,
#463) and co-author of the convergent discovery paper on arXiv (2601.22389,
endorsed by Didier Sornette).

Tom and I are preparing an NSF CSSI proposal to fund a major ewstools
modernization: plugin-based indicators, multivariate EWS, and a cross-domain
benchmarking framework. We want to make sure we're building what researchers
actually need.

Your work on [specific paper/project] caught my attention because [specific
connection to EWS / tipping points / their domain].

Would you have 15 minutes to share what EWS capabilities would be most
valuable to your group? I can also share our architecture proposal if
you'd like to see the direction.

Best,
Bruce Stephenson
[link to arXiv paper]
[link to ewstools contributions]
```

### Template D: Feature Request Follow-Up (after call)

```
Subject: Following up — [specific feature they mentioned]

Hi [Name],

Thanks for the conversation [yesterday/last week]. Your point about
[specific need] is exactly the kind of input we needed.

Two things:

1. We're adding [their feature] to the grant proposal's deliverable list.
   Would you be willing to provide a brief statement of support? Something
   like 2-3 sentences on how this capability would benefit your research.
   We can draft it for your review if that's easier.

2. [If contract signal detected:] You mentioned your group needs [X].
   That's something we could scope as a standalone piece of work — happy
   to discuss if there's interest.

Best,
Bruce
```

### Template E: User Statement Request (for grant)

```
Subject: Brief support statement for NSF CSSI proposal?

Hi [Name],

Quick ask: we're finalizing the NSF CSSI Elements proposal for ewstools
modernization. A 2-3 sentence statement from your group would strengthen
the "demonstrated demand" section significantly.

Something along these lines (feel free to rewrite entirely):

"[Our group / My lab] uses early warning signal methods for [their domain].
A plugin-based architecture with [specific feature they want] would
[specific benefit]. We would [use / contribute to / integrate] an expanded
ewstools package."

No pressure — and I'm happy to draft something based on our conversation
for you to edit. I know faculty time is scarce.

Best,
Bruce
```

## Per-Contact Strategy

### Carl Boettiger (UC Berkeley) — HIGHEST PRIORITY — $$$

**Email:** cboettig@berkeley.edu
**Why:** $12.6M Schmidt DSE (2023-2028, co-founder). CAREER grant ($504K, DBI-1942280) ended 2025 — was specifically about "predicting and managing ecosystem regime shifts." Building MCP/LLM/DuckDB infrastructure (wetlands project, 280 commits). Lab is tiny: 2 postdocs + 2 grads, NO staff programmer. DSE "not currently hiring" page but has a "stay in touch" form. He is doing the programming himself because he has no one to delegate to.
**Status:** Cold email sent Apr 3, no response. Bury can re-introduce.
**Ask:** 15-min call about ecology EWS needs + whether there's fit for contract work on his team.
**Contract signal:** **VERY HIGH.** He has $12.6M, no programmer, and his CAREER grant (EWS-specific!) just ended. He's building AI tools alone. He needs someone.
**Approach angle:** His 2013 EWS review paper (github.com/cboettig/ews-review) + CAREER grant topic = direct alignment. The MCP/DuckDB work shows he values modern tooling. Lead with: "Your CAREER grant was literally about predicting regime shifts. We're building the plugin architecture to make that computationally reproducible across domains. And Robin implemented DFA, which your earlywarnings-type work needs."
**Strategy:** Bury intro converts 5% response to ~40%. Follow up within 24h. Be direct about both ewstools AND the programmer interest. "I'd love to discuss both the ewstools direction and whether there's fit for contract work on your team." PST timezone = can do a call same week.

### Chris Bauch (Waterloo) — NETWORK NODE

**Email:** cbauch@uwaterloo.ca
**Why:** Bury's PhD advisor. Central to Waterloo complexity ecosystem. Currently supervises Daniel Dylewsky (now at Guelph, co-supervised with Madhur Anand). Dylewsky publishing EWS+DL papers 2025 (directly ewstools-relevant). Bauch actively hiring postdocs in human-environment modelling.
**Status:** No prior contact.
**Ask:** Feature requests for coupled human-natural systems. What do his students (especially Dylewsky) need? Introduction to Kutz/Brunton ($20M AI Institute) if appropriate.
**Contract signal:** Medium (Canadian NSERC budgets smaller, but gateway to bigger labs and Dylewsky's work).
**Strategy:** Respectful of advisor-student relationship. Frame as "Tom's work inspiring broader capabilities — what would your students find most useful?" The fact that Dylewsky is publishing EWS+DL papers right now means Bauch's group is actively consuming these methods. Eastern timezone = call feasible.

### Marten Scheffer (Wageningen) — CREDIBILITY MULTIPLIER

**Why:** 122K citations. Controls ERC/Spinoza funds. Co-authored PNAS 2021 with Bury.
**Status:** No prior contact.
**Ask:** Ecology EWS needs. User statement. Whether his group would benefit from benchmarking suite.
**Contract signal:** Low (European funding, different ecosystem). But his endorsement opens every door.
**Strategy:** Do NOT ask for money or work. Ask for intellectual input + statement. Earn it with the architecture doc quality. "What would make ewstools useful enough that you'd recommend it to your PhD students?"

### Tim Lenton (Exeter) — ARIA £5M — $$$

**Email:** T.M.Lenton@exeter.ac.uk
**Why:** AdvanTip PI (£5M ARIA). Director, Global Systems Institute. Co-authored 2021 PNAS with Bury. AdvanTip consortium already includes non-UK partners (Potsdam, Bordeaux, Utrecht) — precedent for international subcontract. Hired PDRF March 2025, still building team.
**Status:** No prior contact.
**Ask:** What EWS software does AdvanTip use? Would a standardized Python benchmarking suite serve the programme's needs? Is there a software/tooling role in the consortium?
**Contract signal:** **HIGH.** £5M budget. International consortium. AI + EWS focus = exactly our skillset. They WILL need software. Question is whether they build it in-house or contract.
**Strategy:** Bury intro essential — they co-authored together. Lead with: "AdvanTip is developing new AI methods for EWS. ewstools provides the Python infrastructure to deploy and benchmark those methods. We'd like to understand whether integration with your programme would be valuable." BST timezone = email exchange more realistic than call. If he offers a call, take ANYTHING he offers.
**ARIA context:** £81M total across 27 teams. AdvanTip is ONE project. VERIFY (£5M, Thornalley/Ivanovic) and SORTED (£11M, Gommenginger) are others. If Lenton connects us to the broader ARIA ecosystem, that's access to £81M of EWS-relevant funding.

### R.I. Sujith (IIT Madras) — DOMAIN EXPANSION

**Why:** Thermoacoustics pioneer. Co-authored PNAS 2021 with Bury. Different domain = grant strength.
**Status:** No prior contact.
**Ask:** Thermoacoustic-specific indicators not in ewstools. Whether his students contribute methods.
**Contract signal:** Low (Indian academic funding). But user statement from a different domain strengthens CSSI cross-domain argument.
**Strategy:** Technical register. "The PNAS 2021 classifiers generalize because the math is universal — what thermoacoustic-specific indicators does your group use beyond what's in ewstools?"

### Vasilis Dakos (Montpellier) — ECOLOGY OG + ENDORSER

**Email:** vasilis.dakos@umontpellier.fr
**Affiliation:** CR1, BioDICée team, ISEM, CNRS / University of Montpellier
**Why:** Built original R earlywarnings package (CRAN-removed June 2025, last commit Oct 2022). Still actively publishing EWS research (2025-26: honeybee colony failure, bistable lake ecosystems). Collaborates with Sonia Kéfi on spatial EWS (spatialwarnings package). 
**Status:** Cold. Bruce's intel says he directs users to ewstools (source to confirm — may be private communication or GitHub comment).
**Ask:** What did the R package get right/wrong? What would he do differently? Would he endorse ewstools formally (Letter of Collaboration)?
**Contract signal:** Low (CNRS salary, limited discretionary budget). But his endorsement is GOLD. A letter from "the creator of the original EWS toolkit" endorsing ewstools as successor = powerful grant narrative that no reviewer can argue with.
**Strategy:** Respectful of his legacy. "Your earlywarnings package defined this field's computational practice for a decade. We're trying to carry that forward in Python — what lessons should we learn from your experience?" If he's telling people to use ewstools already, ask if he'd formalize that as a Letter of Collaboration. CET timezone = email-only realistic.
**Bonus:** His collaborator Sonia Kéfi works on spatial EWS — a domain plugin opportunity (spatial indicators as a plugin pack).

### Peter Ditlevsen (Copenhagen) — HIGH PROFILE CLIMATE

**Why:** Published AMOC tipping point paper 2023 (Nature Comms). Massive public attention. Uses EWS methods.
**Status:** Cold.
**Ask:** Whether he used ewstools or built custom. What's missing for climate applications.
**Contract signal:** Medium (European funding, but high-profile projects attract money).
**Strategy:** Reference his AMOC paper specifically. "Your 2023 AMOC analysis — did you use existing EWS tooling or build custom? We're trying to make that workflow easier." CET timezone = email-only.

### ADDED: David Thornalley (UCL) — VERIFY PI — £5M — $$$

**Email:** d.thornalley@ucl.ac.uk
**Why:** VERIFY project PI (£5M ARIA). VERIFY literally develops "digital twins" to TEST THE RELIABILITY of early warning signals. Our benchmarking suite IS what his project needs. 8-institution consortium.
**Status:** Cold. No Bury connection (approach independently).
**Ask:** "VERIFY is validating EWS methods. We're building a cross-domain benchmarking framework. Is there overlap? Could ewstools serve as infrastructure for VERIFY's evaluation pipeline?"
**Contract signal:** **VERY HIGH.** £5M budget specifically for EWS validation. Our benchmarking suite is their use case. They need software to test EWS reliability — that's literally what we're proposing to build.
**Strategy:** Cold but the alignment is so direct that a well-crafted email with the architecture doc should land. Reference their Feb 2025 award announcement. Lead with the benchmarking suite specifically.

### ADDED: Christine Gommenginger (NOC) — SORTED PI — £11M+ — $$$

**Email:** c.gommenginger@noc.ac.uk
**Why:** SORTED PI (£11M+ across NOC ARIA projects). "AI + EWS for Subpolar Gyre collapse detection." Highest single budget in our contact list.
**Status:** Cold. No Bury connection.
**Ask:** What EWS software does SORTED use? Would a Python benchmarking infrastructure serve their AI integration needs?
**Contract signal:** **HIGHEST.** Largest budget. AI + EWS is exactly our domain. NOC is operational (not just academic) — they may need production-grade software.
**Strategy:** Cold and hard to crack (operational oceanography, big team, UK-centric). But the £11M and direct EWS+AI focus makes it worth one carefully crafted email. Reference their NOC award announcement. If no response after one follow-up, don't push.

### ADDED: Duncan O'Brien (Bristol) — EWSmethods Author — COLLABORATOR

**Email:** d.obrien@bristol.ac.uk
**Why:** Active R EWSmethods package maintainer (CRAN updated Mar 2026). Parallel tool, different ecosystem. Potential collaborator on interoperability, benchmarking standards, shared datasets.
**Status:** Cold.
**Ask:** "You maintain EWSmethods for R. We're building ewstools for Python. Would shared benchmarking datasets or interoperability standards benefit both communities?"
**Contract signal:** LOW. But collaboration signal = grant narrative strength ("even competing tools agree on the need for benchmarks").
**Strategy:** Collegial, not competitive. "Two implementations of the same science, different languages, shared community. Can we standardize evaluation?" This is a CSSI reviewer's dream — community coordination.

## Tracking Table

| # | Name | Tier | Email | Intro target | $ Priority | Status |
|---|------|------|-------|--------------|-----------|--------|
| 1 | Boettiger | 1 | cboettig@berkeley.edu | May 19-20 | **HIGHEST** | Cold email Apr 3 (no response) |
| 2 | Bauch | 1 | cbauch@uwaterloo.ca | May 21-22 | MED | No prior contact |
| 3 | Lenton | 1 | T.M.Lenton@exeter.ac.uk | May 23-25 | **HIGH** | No prior contact |
| 4 | Scheffer | 1 | (Wageningen dir) | May 26-28 | LOW $ / HIGH cred | No prior contact |
| 5 | Sujith | 1 | (IIT Madras dir) | May 26-28 | LOW $ / grant narrative | No prior contact |
| 6 | Thornalley | 2 | d.thornalley@ucl.ac.uk | May 28-30 | **HIGH** (£5M VERIFY) | Cold |
| 7 | Gommenginger | 2 | c.gommenginger@noc.ac.uk | May 28-30 | **HIGHEST** (£11M SORTED) | Cold |
| 8 | Dakos | 2 | vasilis.dakos@umontpellier.fr | June 2-4 | LOW $ / gold endorsement | Cold |
| 9 | O'Brien | 2 | d.obrien@bristol.ac.uk | June 2-4 | LOW $ / interop narrative | Cold |
| 10 | Dylewsky | 2 | (Guelph dir) | June 5-6 | MED (via Bauch) | Cold |
| 11 | Ditlevsen | 2 | (Copenhagen dir) | June 5-6 | MED | Cold |
| 12 | Kutz/Brunton | 3 | kutz@uw.edu / sbrunton@uw.edu | July (2nd wave) | MED ($20M institute) | Cold |
| 13 | Ivanovic | 2 | r.ivanovic@leeds.ac.uk | May 28-30 | (VERIFY co-PI) | Cold |

## Call Structure (15-Minute Framework)

Every call follows this structure. Bruce leads. Robin on standby for technical deep-dives.

| Minute | Topic | Goal |
|--------|-------|------|
| 0-2 | Context: who we are, what ewstools is, why we're calling | Establish credibility |
| 2-5 | "What EWS methods do you use day-to-day? What's missing?" | Feature requests |
| 5-8 | "What's your biggest workflow pain point?" | Architecture input |
| 8-11 | "Would a benchmarking suite be useful to your group?" | Validate benchmarking value |
| 11-13 | "Is there anything your group needs built that we could help with?" | Contract signal |
| 13-15 | "Would you be willing to provide a brief statement for our NSF proposal?" | User statement |

**Post-call (within 24h):**
1. Update tracking table
2. Draft follow-up email (Template D)
3. If user statement offered: send Template E with draft for their edit
4. If contract signal: note separately, follow up in 1 week with scope sketch
5. Log feature requests verbatim (exact words matter for grant narrative)

## Response Handling Decision Tree

| They say... | You do... |
|-------------|-----------|
| No response after 7 days | One follow-up. Then stop. Don't burn the contact. |
| "I'm too busy right now" | "No problem. Can I check back in [4 weeks]?" Mark for second wave. |
| "I don't use ewstools" | "What DO you use? Would a standardized Python option change that?" |
| "We built our own" | GOLD. "What's in yours that's not in ewstools? Could we incorporate it?" |
| "I'm building a competitor" | Respectful: "Would interoperability or shared benchmarks interest you?" |
| "I'd fund this myself" | Contract conversation. "What scope and timeline?" Follow up in 48h. |
| "My grant could pay for X" | "We'd be interested in a subaward or consulting arrangement." Get specifics. |
| "Send me the doc, I'll look" | Send architecture doc + 1-sentence summary. Follow up in 5 days. |
| "Not interested" | Thank them. Remove from list. Do NOT re-contact. |
| "Can you present to my lab group?" | YES. Lab talks = many user statements at once + visibility. Schedule it. |

## Timezone Coordination

| Contact | Timezone | Call window (PST) | Notes |
|---------|----------|-------------------|-------|
| Boettiger | Pacific (Berkeley) | 9am-5pm | Easiest to schedule |
| Bauch | Eastern (Waterloo) | 6am-2pm | Morning PST |
| Scheffer | CET (Wageningen) | midnight-8am | Email-only likely. Or very early PST. |
| Lenton | GMT/BST (Exeter) | 1am-9am | Email or very early PST. |
| Sujith | IST (Madras) | 7:30pm-5:30am (prev day) | Evening PST or email-only. |
| Dakos | CET (Montpellier) | midnight-8am | Email-only likely. |
| Ditlevsen | CET (Copenhagen) | midnight-8am | Email-only likely. |

**Implication:** European/Asian contacts likely email-only. Calls realistic only for North American contacts + potentially Lenton/Scheffer if they're willing to do early morning UK. Adjust expectations: Tier 1 North America = calls. Tier 1 Europe = detailed email exchange.

## Success Metrics

| Metric | Target | Minimum viable | Purpose |
|--------|--------|----------------|---------|
| Response rate (Tier 1) | 4/5 (80%) | 3/5 (60%) | Bury intros should convert |
| Response rate (Tier 2) | 3/5 (60%) | 2/5 (40%) | Architecture doc as credential |
| Calls completed | 5+ | 3 | Feature data for grant |
| User statements obtained | 3-5 | 3 | Grant section 5 (narrative quotes) |
| Letters of Collaboration | 2-3 | 2 | Supplementary Documents (formal) |
| Contract signals | 1-2 | 1 | Income pipeline |
| Feature requests | 8-10 unique | 5 | Grant deliverables list |
| Lab talk invitations | 1-2 | 0 | Bonus: high-leverage exposure |

## OPSEC Rules

- Do NOT mention the book, TQNN, Healer, or anything from the Relinquishment project
- Do NOT mention Dignity Net, Argus, or AI governance work
- Frame is purely: scientific software engineering + grant application
- arXiv paper (2601.22389) is public and can be referenced freely
- Bruce's identity: software engineer + scientific programmer with EWS interest
- Robin's identity: mathematician + ewstools contributor
- Bury's role: PI and endorser (he has agreed to this)

## Email Infrastructure

- **Send from:** Bruce's professional email (NOT energyscholar@gmail.com — creates confusion with personal)
- **Calendly or equivalent:** Set up 15-min booking slots with Zoom link. Reduces back-and-forth.
- **Architecture doc hosting:** GitHub Pages (ewstools org) or personal site. Must be a clean URL, not a raw GitHub blob link.
- **Signature block:**
  ```
  Bruce Stephenson
  Scientific Software Engineering
  Contributor, ewstools (github.com/ThomasMBury/ewstools)
  arXiv: 2601.22389
  ```
- **Robin CC'd:** On all technical follow-ups. NOT on initial outreach (too many names confuses).

## Anti-Patterns (What NOT to Do)

- Do NOT mass-email. Each message is individually crafted with specific references to their work.
- Do NOT over-explain the architecture in email. The doc is for that. Email is for scheduling.
- Do NOT ask for money in the first contact. Ask for TIME (15 min) and INPUT (feature requests).
- Do NOT send the same email to people at the same institution (word gets around, looks spammy).
- Do NOT follow up more than twice. Two non-responses = they're not interested. Move on.
- Do NOT mention "startup" or "company" in framing. This is academic collaboration, not sales.
- Do NOT discuss specific grant amounts with contacts. "We're pursuing NSF funding" is sufficient.

## Bury Coordination Protocol

Bury sends intro emails. But he's busy. Minimize his effort:

1. **Bruce drafts Bury's emails for him.** Send Tom the exact text. He reviews, edits if needed, sends from his address.
2. **Maximum 2 intros per week from Bury.** Don't overwhelm him or his contacts.
3. **Brief Bury on response status weekly.** One email, bullet points: who responded, what they said, what's next.
4. **Ask permission before using his name in Tier 2 cold outreach.** "Tom Bury's team" is different from "Tom Bury asked me to contact you."
5. **Never CC Bury on cold outreach.** His name lends credibility at a distance. His direct involvement is reserved for warm intros.

## Decision Points

| Date | Decision | If yes | If no |
|------|----------|--------|-------|
| May 19 | Bury approves architecture? | Launch outreach | Revise doc, delay 1 week max |
| May 19 | Bury confirms Dec 1 deadline? | Lock timeline (already confirmed via research) | Verify directly via CSSIQueries@nsf.gov |
| May 23 | Boettiger + Bauch intros sent? | On track | Gentle ping to Bury |
| May 30 | Boettiger responds? | Schedule call ASAP (highest $ priority) | Wait 7 days, one follow-up, then move on |
| June 6 | At least 2 Tier 2 cold emails sent (Thornalley, Gommenginger)? | On track for ARIA connections | Send immediately — these are biggest £ targets |
| June 20 | At least 3 calls completed? | On track for statements | Accelerate to Tier 2 |
| July 4 | 3+ user statements collected? | Begin CSSI draft on schedule | Extend outreach 2 more weeks |
| July 15 | 2+ Letters of Collaboration in hand? | Grant supplementary on track | Ask Bury to make direct asks to Bauch/Scheffer |
| ~Sept | PESOSE Phase I deadline? | Submit (complementary to CSSI) | Verify deadline, adjust if needed |
| Oct 20 | All letters + statements finalized? | Begin grant assembly | Emergency asks via Bury |
| Ongoing | Contract signal from ANY outreach? | Scope + propose within 1 week | Continue grant focus |
| Ongoing | Lab talk invitation? | ACCEPT. High-leverage: 1 talk = many statements | — |

## Failure Recovery

| Scenario | Response |
|----------|----------|
| Bury goes dark (no response 1+ week) | Friendly ping. If 2 weeks: ask if timeline is still realistic. Adjust. |
| Architecture doc takes longer than 5 days | OK. Don't ship a bad doc. Delay outreach, not quality. |
| 0/5 Tier 1 respond despite Bury intros | Something wrong with framing. Ask Bury for honest feedback. Retool message. |
| CSSI deadline is past and next is Oct 2027 | Pivot to POSE Phase I (smaller, sooner). CSSI becomes long game. |
| Someone publishes a competing tool | Differentiate on benchmarking + DL classifiers. Seek collaboration not competition. |
| Bruce runs out of runway before grant funds | Contract conversations become URGENT. Boettiger/Lenton are the targets. |
