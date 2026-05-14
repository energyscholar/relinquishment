---
Plan-UID: 0325
Status: DRAFT — awaiting Bruce review
Owner: Bruce (sends), Argus (research + drafts)
---

# May–June 2026 Outreach Plan

## Why previous outreach hasn't landed

Three failure modes, all fixable:

1. **Leading with artifact instead of need.** "Look at this thing I built" doesn't land with busy PIs. "I noticed you're fighting X — I solved X" does. The white paper zip attachment is a "read my manifesto" ask. Nobody reads manifestos from strangers.

2. **No institutional affiliation = spam prior.** Academics get dozens of cold emails from consultants. Without a .edu or a known name in the subject line, the email gets triaged to "later" which means "never." Warm intros aren't optional — they're load-bearing.

3. **Multiple asks per message.** The Bury email mixed CSSI grant, tutorial showcase, and consulting pitch. Three asks competing for attention means zero asks get answered. One email, one ask.

**Fix:** Every outreach action below follows the rule: **one person, one need they already have, one thing you can do about it.**

---

## Track A: Carl Boettiger (UC Berkeley)

### Intelligence (from GitHub, May 12 2026)

Boettiger is not a distant academic who might theoretically benefit from your ideas. He is building exactly what your white paper describes — and hitting exactly the failure modes it solves. Specifics:

**What he's building RIGHT NOW:**
- `geo-agent` — agentic LLM chatbot for conservation geospatial data (MapLibre + Claude + MCP tools). Commits daily. Flagship product.
- `mcp-data-server` — production DuckDB MCP server on Kubernetes (NRP Nautilus). H3-indexed Parquet on S3.
- `agent-skills` — 15 Claude Code skill modules at `~/.claude/skills/`
- `open-llm-proxy` — multi-provider LLM routing with carbon monitoring
- `LLM_lesson_exemplar` — teaching scientists to use AI (active workshop material)
- `jupyter-ai` fork — designing ACP (Agent Client Protocol) bridge for JupyterLab

**His observed pain points (from commit history):**
- **LLM hallucination of data paths** — months of commits removing examples from prompts because agents guess S3 paths instead of calling tools. Classic ungoverned-agent failure.
- **Two-process AI coordination failure** — his small LLM violated a query rule, caused a slow query, then a Claude session misdiagnosed it and tried to remove the correct rule. He had to write explicit process separation docs after the fact.
- **Agent tool-calling reliability** — constant prompt refinement to get agents to call specific tools before others. Token overhead management.
- **Ad hoc governance** — his AGENTS.md files are excellent but invented per-repo. No cross-session memory. No formalized role separation. No drift detection.

**What Bruce has that he needs:**
- Persistent cross-session memory with typed memories and health monitoring (his agents are stateless or session-scoped)
- Triad role separation (his two-process architecture is a manual, fragile version of Auditor/Generator)
- Formalized correction system (his hallucination fixes are one-off prompt patches, not numbered corrections that persist)
- Dignity Net-style truth governance (his agents agree with bad ideas — the mcp-data-server incident proves it)

**He uses Claude Code daily.** Has CLAUDE.md files in multiple repos. Starred `caveman` (token-saving skill) and `opencode`. Has YubiKey-protected agent auth for autonomous GitHub access.

### Approach

**Why the cold email failed:** Bruce sent a generic "look at my tutorials" email in April. Boettiger gets dozens of these. Nothing in it signaled "I understand what you're building and I've solved your specific problem."

**The play:** A short, technically specific message that demonstrates Bruce has read his code and understands his pain. Not "here's my white paper" but "I noticed your mcp-data-server had a coordination failure in March where Claude tried to remove a correct query rule. I've been running a system that prevents exactly that for six months. Here's how."

**Format options (choose one):**

Option 1 — **GitHub Discussion or Issue comment.** Find a relevant open issue on geo-agent or mcp-data-server. Post a technically substantive comment that demonstrates understanding. Link to the white paper as "here's the full architecture." This bypasses email entirely and shows up in his workflow.

Option 2 — **Calligraphed paper letter.** Break every digital pattern. Hand-addressed to his Berkeley office. Three paragraphs: (1) I read your geo-agent code and your agent-skills repo. (2) Your two-process architecture solves the right problem but I've been running a more robust version for six months — here's the one-page summary. (3) The white paper URL if you want the full thing. No ask beyond "read this if it's useful."

Option 3 — **Bury warm intro.** Bury doesn't know Boettiger personally, but they're in the same EWS conversation (2021 PNAS issue). Bury emails: "Bruce built a persistent AI governance system that might interest you — he's been running it on Claude Code for six months. His white paper is at [URL]." One sentence from a known name.

**Recommendation:** Option 1 first (free, immediate, technically credible). Option 3 as follow-up if no response. Option 2 as nuclear option if both fail.

**Draft — GitHub comment (for geo-agent or mcp-data-server issue):**

> I've been following your agent-skills architecture and the two-process pattern in mcp-data-server. The coordination problem you documented — where a Claude session misdiagnosed a slow query and tried to remove a correct rule — is a failure mode I've been working on systematically.
>
> I run a persistent AI system on Claude Code with three governance layers: execution governance (role separation between planning and implementation, with human authorization gates), truth governance (graduated escalation when the AI detects divergence between stated goals and observable actions), and continuity governance (typed memories, numbered corrections, health monitoring with drift detection). It's been in continuous operation since December 2025.
>
> The architecture is documented here: [white paper URL]. The failure cross-matrix in Shift 1 maps exactly the kind of coordination failure your March incident represents — truth governance holding but execution governance failing.
>
> Happy to discuss if any of this is useful for your agent work.

**What NOT to do:** Don't mention consulting, training, or money. Don't attach a zip. Don't mention the CSSI grant. One message, one thing: "I solved a problem you have."

### Timeline

- **Week of May 12:** Bruce reviews Boettiger's open issues on geo-agent and mcp-data-server. Find the right thread.
- **Week of May 19:** Post the comment OR ask Bury to send the intro.
- **June 2:** If no response, send the paper letter.

---

## Track B: Amy Keesee / CGS (via Merkin)

### Intelligence

- Associate Professor, UNH Space Science Center
- **CGS Broadening Impacts Section Head** — runs education/outreach for the entire $15M NASA DRIVE center
- Mandated NASA EPO budget lines — she MUST spend money on outreach materials
- Current output: lesson plans, downloadable resources, Hayden Planetarium integration, K-12 visits, grad workshops
- Nothing animated. Nothing at the quality of Bruce's 13 SVG tutorials.
- Publishes on ML for space weather, ion dynamics, M-I coupling during storms/substorms
- Co-located at UNH with Charles Smith (SWUG magnetometer program)

### Approach

**The ask to Merkin:** One email. "Could you introduce me to Amy Keesee? I've built a portfolio of animated space physics tutorials — MHD, FAC, inversion, kriging — that might fit CGS's broader-impacts deliverables. Happy to show her the portfolio."

**Why this works:** Merkin directs CGS. Keesee reports to the center structure. This is an internal referral, not a cold pitch. And Bruce is offering to help Keesee fulfill a NASA mandate she already has.

**What to show Keesee:** The tutorial portfolio at has-anyone-looked. Lead with magnetosphere, MHD, FAC — these map directly to CGS science (MAGE model, electrojet physics). Don't lead with the white paper. Don't mention AI governance. This is about physics tutorials for education.

**EZIE angle:** Gjerloev is EZIE Project Scientist. EZIE launched March 2025, collecting electrojet data now. An animated electrojet tutorial would serve both CGS and EZIE outreach. Bruce could offer to build one on spec.

**Charles Smith / SWUG:** Ground magnetometer network in New England high schools. Bruce's magnetosphere tutorial is the exact curriculum supplement they're missing. Same UNH building as Keesee. One intro covers both.

### Timeline

- **Week of May 12:** Draft the Merkin email (3 sentences). Bruce sends.
- **Week of May 19:** Follow up if no response. Ask Gjerloev as backup intro path.
- **Week of May 26:** If intro happens, send Keesee the portfolio with a specific offer: "I can build an electrojet tutorial for EZIE/CGS outreach. Want to see a prototype?"

---

## Track C: Anthropic

### Goal

Get the white paper seen by someone at Anthropic who cares about how Claude Code is being used in sustained collaboration. Not sales — signal. "Your tool is being used in a way nobody else has documented. Here's the evidence."

### Approach options

1. **LinkedIn.** Find Anthropic employees working on Claude Code, agent tooling, or AI safety. Alex Albert (prompt engineering lead), Zack Witten (Claude Code), or similar. Short message: "I've been running a persistent AI collaboration system on Claude Code since December 2025. Three governance layers, 70+ sessions, health monitoring, behavioral corrections that compound. Here's the architecture: [URL]." LinkedIn has higher response rates than cold email for tech industry.

2. **Anthropic Discord / Community.** If there's an official Claude Code community channel, post there. The white paper IS a Claude Code showcase.

3. **Twitter/X.** Post a thread showing the failure matrix, the three axes, one concrete example of governance catching a real error. Tag @AnthropicAI. Technical Twitter rewards substance.

4. **Direct to docs team.** The white paper is essentially a case study for Claude Code's CLAUDE.md system. Anthropic's docs team might want to reference it. Find the right person via LinkedIn.

**Recommendation:** LinkedIn first (targeted, professional, trackable). Twitter thread second (public, viral potential). Both can happen the same week.

### Timeline

- **Week of May 19:** Bruce identifies 2-3 Anthropic employees on LinkedIn. Sends short messages.
- **Week of May 19:** Draft a Twitter thread (5-7 tweets). Bruce posts when ready.

---

## Track D: Broader targets (June)

These wait until Tracks A-C are in motion.

| Target | Angle | Path | When |
|--------|-------|------|------|
| Vasilis Dakos (CNRS) | EWS pedagogy — animated tutorials for earlywarnings community | Bury intro | June 2 |
| Sonia Kéfi (CNRS) | Spatial EWS animations (vegetation patterns → tipping) | Bury → Dakos → Kéfi | June 9 |
| Kareem Sorathia (APL) | GAMERA adoption tutorials | Merkin intro | June 2 |
| Heidi Nykyri (ERAU) | KH instability tutorials, CAREER outreach budget | Merkin intro | June 9 |
| EZIE EPO lead | Electrojet tutorial on spec | Gjerloev direct | June 2 |

---

## Rules for all outreach

1. **One ask per message.** Never combine grant, consulting, and tutorial showcase.
2. **Lead with their need, not your artifact.** Research what they're struggling with before writing.
3. **Warm intros only** (except Anthropic/social media). No more cold emails to academics.
4. **No zip attachments.** Link to the live page. People click links; people don't open zips from strangers.
5. **Follow up once.** If no response after one follow-up, stop. Don't burn the contact.
6. **Track responses.** Update PTL with response status after each outreach.
7. **The consulting pitch comes AFTER engagement.** First message: "I can help with X." Second conversation: "I also do this professionally."

---

## Success metrics (end of June)

| Metric | Target | Minimum viable |
|--------|--------|----------------|
| Warm intro requests sent | 6 | 3 |
| Intros that convert to conversation | 3 | 1 |
| Boettiger engagement (any form) | Yes | Read receipt equivalent |
| Keesee/CGS conversation | Yes | Merkin forwards the email |
| Anthropic visibility | 1 response | 1 view/like on social |
| Paid work lead | 1 | 0 (but pipeline started) |

---

## Logistics

### Mailing addresses (verified)

| Person | Address | Source |
|--------|---------|--------|
| Carl Boettiger | Dept. of ESPM, UC Berkeley, 130 Mulford Hall #3114, Berkeley, CA 94720 | DB record + ESPM directory |
| Amy Keesee | Morse Hall, Room 415, UNH, Durham, NH 03824 | UNH CEPS faculty page |
| Charles Smith | Morse Hall, Room 207, UNH, Durham, NH 03824 | UNH EOS faculty page |
| Viacheslav Merkin | JHU Applied Physics Lab, 11100 Johns Hopkins Rd, Laurel, MD 20723 | APL directory |
| Jesper Gjerloev | Catholic University of America, 620 Michigan Ave NE, Washington, DC 20064 | DB record (moved from APL 2025) |

### Contact packages — what each target needs to see

| Target | Lead material | Format | Secondary | DO NOT include |
|--------|--------------|--------|-----------|----------------|
| Boettiger | White paper (governance architecture) | GitHub comment → live URL | agent-skills comparison | tutorials, grant, consulting pitch |
| Keesee | Tutorial portfolio (13 animated SVGs) | Live URL to has-anyone-looked | Offer to build electrojet tutorial | white paper, AI governance, consulting |
| Merkin | (already sent 6-page PDF Apr 29) | Follow-up email requesting Keesee intro | Tutorial portfolio link | don't re-pitch science; pivot to outreach request |
| Gjerloev | Magnetosphere tutorial (already sent) | Follow-up email requesting EZIE EPO intro | Tutorial portfolio link | don't re-pitch science |
| Bury | (warm, ongoing) | Email requesting Boettiger intro | White paper as supporting evidence | nothing new needed, just the ask |
| Anthropic | White paper as Claude Code case study | LinkedIn message + live URL | Twitter thread | zip files, consulting pitch |

### Calligraphy letter protocol

**When to use:** After digital channels have been tried and failed (Boettiger) or for high-value cold contacts where a paper letter breaks pattern.

**Format:**
- Hand-addressed envelope, calligraphed
- Single sheet, 3 paragraphs max
- QR code: YES — print a small (1 inch) QR code on a separate card stock insert, not on the calligraphed letter itself. The letter stays clean; the card is the bridge to electronic. QR links to the live white paper URL.
- Include the QR card loose in the envelope so they can keep it on their desk
- No zip files, no USB drives, no printouts of the paper

**QR code generation:** `qrencode -o qr-whitepaper.png -s 10 'https://energyscholar.github.io/persistent-ai-collaboration/'`

**Boettiger calligraphy letter draft:**

> Dr. Boettiger —
>
> I've been reading your geo-agent and agent-skills repos. The two-process architecture in mcp-data-server — a small LLM for real-time queries, Claude for async review — solves the right problem. I've been running a more formalized version of this pattern on Claude Code since December 2025: role separation with human authorization gates, graduated truth governance, and persistent memory with health monitoring across 70+ sessions.
>
> The architecture is documented at the URL on the enclosed card. The failure cross-matrix maps the coordination failures I think you're solving ad hoc.
>
> No ask. Just thought you'd find it useful.
>
> — Bruce Stephenson
> energyscholar@gmail.com

### Master timetable — Week of May 12–16

| Day | Action | Target | Owner | Notes |
|-----|--------|--------|-------|-------|
| Mon 12 | Complete Boettiger repo research | Boettiger | Argus | DONE (agents running) |
| Mon 12 | Finalize outreach plan | All | Argus | THIS DOCUMENT |
| Mon 12 | Generate QR code for white paper URL | Boettiger | Argus | `qrencode` command ready |
| Tue 13 | Write + mail calligraphy letter to Boettiger | Boettiger | Bruce | **FIRST — ~2 day delivery OR→Berkeley, arrives ~Thu May 15** |
| Tue 13 | Draft Bury email requesting Boettiger intro | Boettiger | Argus drafts, Bruce sends | One sentence ask, white paper URL |
| Tue 13 | Draft Merkin email requesting Keesee intro | Keesee | Argus drafts, Bruce sends | Pivot from science to outreach request |
| Wed 14 | Bruce sends Bury email | Boettiger | Bruce | Morning — don't overthink |
| Wed 14 | Bruce sends Merkin email | Keesee | Bruce | Separate from Bury, different ask |
| Wed 14 | Draft Gjerloev email requesting EZIE EPO intro | EZIE | Argus drafts | "Who handles EZIE outreach material?" |
| Wed 14 | Review Boettiger open issues, pick thread for comment | Boettiger | Bruce + Argus | Need a thread where comment is natural, not forced |
| Thu 15 | Post GitHub comment on Boettiger repo | Boettiger | Bruce | Times with letter in transit — digital arrives while physical is en route |
| Thu 15 | Bruce sends Gjerloev email | EZIE | Bruce | |
| Fri 16 | Identify 2-3 Anthropic LinkedIn targets | Anthropic | Argus research | Claude Code team, developer relations |

### Week of May 19–23

| Day | Action | Target | Notes |
|-----|--------|--------|-------|
| Mon 19 | Send LinkedIn messages to Anthropic targets | Anthropic | Short, one URL, no zip |
| Mon 19 | Check for Bury/Merkin/Gjerloev responses | All | If Bury responded: send Boettiger intro request |
| Wed 21 | Draft Twitter thread (5-7 posts) | Anthropic / General | Failure matrix, three axes, one concrete governance example |
| Fri 23 | Follow up non-responders (ONE gentle ping each) | Bury, Merkin, Gjerloev | Only if no response by now |

### Week of May 26–30

| Day | Action | Target | Notes |
|-----|--------|--------|-------|
| Mon 26 | If Keesee intro happened: send portfolio email | Keesee | Lead with magnetosphere + MHD tutorials |
| Mon 26 | If Keesee intro didn't happen: cold email directly | Keesee | Use tutorial portfolio, not white paper |
| Wed 28 | If Boettiger engaged (any channel): follow up | Boettiger | Match his register — technical, specific |
| Fri 30 | Status review. What worked, what didn't. Adjust June plan. | All | Honest assessment, no sunk cost |

### June targets (contingent on May results)

Activate only after May tracks are in motion:
- Dakos/Kéfi (via Bury): EWS pedagogy tutorials
- Sorathia (via Merkin): GAMERA adoption tutorials
- Nykyri (via Merkin): KH instability tutorials
- EZIE EPO lead (via Gjerloev): electrojet tutorial on spec

### Contact channel status (as of May 12)

| Contact | Channel strength | Last contact | Status | Next action |
|---------|-----------------|--------------|--------|-------------|
| Bury | WARM — active email exchange | May 11 (Bruce email re CSSI + tutorials) | Engaged, responsive | Ask for Boettiger intro |
| Merkin | THIN — one technical exchange | Apr 29 (Bruce sent 6-page PDF) | Awaiting response (~2 weeks) | Request Keesee intro (separate email) |
| Gjerloev | THIN-WARM — friendly exchange | May 11 (Bruce sent magnetosphere tutorial + email) | Awaiting response | Request EZIE EPO contact |
| Boettiger | COLD — one ignored email | Apr 3 (cold email, no response) | Need new approach | GitHub comment + calligraphy letter |
| Keesee | NONE | No prior contact | Cold | Warm via Merkin, cold backup |
| Anthropic | NONE | No prior contact | Cold | LinkedIn + Twitter |

---

## What this plan does NOT cover

- CSSI grant application (separate plan, depends on Bury timeline)
- ewstools architecture document (prerequisite for CSSI, tracked separately)
- Book marketing (different audience, different channels)
- Spanish translation of white paper (Plan 0323)
