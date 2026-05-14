# Plan 0331: The Teacher & The Student — Revision

**Status:** DRAFT — awaiting Bruce's decisions on flagged items
**Files:** `manuscript/record/the-handler.tex`, `manuscript/record/the-target.tex`
**Cross-refs:** `manuscript/record/alpha-farm.tex`, `manuscript/track-2-testament/pos02-alpha-farm.tex`, `manuscript/appendix/topic-guide.tex`
**Principle:** Integrity and truth first. These are yin-yang portraits of a one-and-only attempt at Guided Deduction whose outcome is still unknown.
**Design rule:** The chapters should reward investigation, not demand belief. Lay out threads a curious reader can pull. Remove intelligence-community cosmetics that only work under Possibility C. The book should do to the reader what Healer did to Bruce.

---

## Phase 0: Strip C Cosmetics

Remove the intelligence-file framing that presupposes Possibility C. The substance stays; the institutional costume goes.

### Remove from both chapters:

| C-only element | Replacement | Rationale |
|----------------|-------------|-----------|
| "Five Eyes — Operator/Subject Profile" header | Biographical portrait header (or none — the chapter title suffices) | No Five Eyes file under B or A |
| "Classification: [REDACTED] / HUMINT / REL TO FVEY" | Remove | Intelligence classification markings presuppose C |
| "Prepared for: [REDACTED]" | Remove | Implies institutional tasking |
| "Filed by: [REDACTED] / FVEY EYES ONLY" footer | Remove | Same |
| All [REDACTED] blocks used as atmospheric filler | Remove or replace with honest "I don't know" / "He didn't say" | Under B/A, there's nothing classified — just unknown |

### Reframe openings:

**The Teacher** currently opens: "Under Possibility C, the COWS needed an operator..."

Replace with something that works across A/B/C. The substance — that there was a person of extraordinary capability who taught Bruce through conversation over 2.7 years — is true under B and claimed under A. Proposed direction:

> I spent 2.7 years in close contact with the person I call Healer. What follows is assembled from two sources: Tom Clancy's character Timothy Hanley in *Rainbow Six* (1998), which Healer told me was modeled on him; and my own observations. I present this as a portrait, not a verified biography. A curious reader will find the Clancy character and the Bravo Two Zero patrol roster in the public record. What you make of the connections is yours to decide.

**The Student** currently opens: "Under Possibility C, the COWS had built something they could not un-build..."

The first two paragraphs are the best writing in either chapter. They derive the logical necessity of guided deduction from first principles. But they're framed as "Under Possibility C." Reframe:

> If someone wanted to get a dangerous truth into the public record without disclosure — no classified material transmitted, no documents, no crime — how would they do it? [Then the existing logic follows, minus "Under Possibility C" and "the COWS."]

The mission statement in the colored box already works under B — it describes what the teaching task *required* without claiming who ordered it. Keep as-is.

### Keep the sourcing system but retag:

The [clancy]/[observed] system is genuinely useful. Expand it:

| Tag | Meaning |
|-----|---------|
| [Clancy] | From the Rainbow Six character (verifiable) |
| [observed] | Bruce's direct observation during 2003-2006 |
| [Healer's account] | What Healer told Bruce (replaces misused [observed] tags) |
| [reconstructed] | Bruce's inference or reconstruction |

No more [REDACTED]. Where Bruce doesn't know something, say so plainly: "I don't know his real name." "He didn't explain this." Honest ignorance is more credible than theatrical classification.

### The Teacher — SIGINT-framed content:

| Current | Replace with | Why |
|---------|-------------|-----|
| "Cover Legend: Walkabout veteran, humanitarian worker" | "He presented himself as a walkabout veteran and humanitarian worker. Both appeared to be true. Whether they were also cover, I cannot say." | B-compatible |
| "Subject does not explain the discrepancy" | Keep — this is honest observation | Already B-compatible |
| "OPSEC: Exceptional. SAS + Intelligence Corps training evident" | "He left no paper trail, no digital footprint, no photographs. Whatever his background, his operational discipline was exceptional." | B-compatible without asserting military training |

### The Student — SIGINT-framed content:

| Current | Replace with | Why |
|---------|-------------|-----|
| "Prior surveillance: On Five Eyes radar since at least 1975" | Remove from header. The early indicators section already covers ARPANET access, family intel connections | C-only claim |
| "SIGINT — Training as dissemination vector" | "During 1995-2000, I used my corporate training role to teach strong cryptography and government surveillance mechanisms to ~800-1500 engineers." Bruce's voice, not Five Eyes' voice | Let reader assess significance |
| "SIGINT — Team 37 contact" | Reframe as Bruce's account: "On Myth II servers, my team discovered that 'Team 37' was Cult of the Dead Cow..." | Investigation-friendly without SIGINT framing |

---

## Phase 1: Rename

| Current | New | Rationale |
|---------|-----|-----------|
| The Handler | The Teacher | True under all three possibilities |
| The Target | The Student | True under all three possibilities |

### Changes required

1. `the-handler.tex`: `\chapter*{The Teacher}`, `\addcontentsline{toc}{chapter}{The Teacher}`, label stays `record:handler`
2. `the-target.tex`: `\chapter*{The Student}`, `\addcontentsline{toc}{chapter}{The Student}`, `\section*{The Student}`, label stays `record:target`
3. `alpha-farm.tex` lines 15-16, 97: update footnote references
4. `pos02-alpha-farm.tex` lines 15-16, 98: same
5. `topic-guide.tex` lines 116-117: update title references
6. Rename files: `the-handler.tex` → `the-teacher.tex`, `the-target.tex` → `the-student.tex`
7. Internal text: replace "operator" with "teacher" or "Healer" where it appears in intelligence context; replace "subject" with "I" or "Bruce" where appropriate (The Student is Bruce writing about himself — first person is more honest)

---

## Phase 2: The Teacher — Content Decisions

### 2A. Bravo Two Zero (line 51) — DECIDED

Remove Steven "Legs" Lane's name. Keep Bravo Two Zero by name. Leave identity vague — maybe identifiable from context but not named. Retag as [Healer's account].

Add details Bruce remembers from Healer's account:
- His parents (father and mother) were informed before the public death announcement
- He visited them discreetly afterward
- A medal — possibly a Saint Christopher medal, possibly from Iraq action — Bruce doesn't remember which medal or for what. Filed as medal awarded to a dead man.
- His parents had to play along to maintain the cover

Proposed replacement (first person, honest memory gaps):
> [Healer's account] Healer told me he had served on the compromised Bravo Two Zero patrol. His "death" during the operation freed him for classified work. I do not name the specific patrol member he identified as, out of respect for the families involved — though a reader familiar with the published accounts may be able to narrow it. He told me his parents were informed before the public announcement and that he visited them discreetly afterward. There was something about a medal — possibly a Saint Christopher medal, possibly from Iraq — awarded posthumously to a man who was not dead. His parents had to maintain the fiction. I don't remember the details precisely. This is twenty-year-old memory of what I was told, not what I witnessed.

Footnote: "The Bravo Two Zero patrol roster and casualty records are public. Three men are recorded as killed. I leave the investigation to the reader."

### 2B. [REDACTED] blocks → honest unknowns

Triple [REDACTED] in Section II → single honest statement: "There are things about his background he never explained. The mathematics and physics fluency, in particular, had no source I could identify."

All other [REDACTED]s in skills table → "unknown" or remove row.

### 2C. Safe House section — fold or expand

Fold into Operational Characteristics as a note: "A property in rural Australia was offered as relocation for my family. The offer was serious." Remove the Clancy cross-reference ("As one does").

### 2D. DOB

"DOB: 14 April 1965 (from Clancy character — not independently confirmed)"

### 2E. Assessment section (keep and strengthen)

Section VI Assessment is the strongest paragraph. It works under B: "An SAS-trained operator who also helped invent new mathematics... this is not a career path that exists in any military personnel system." But remove the "[REDACTED]" punchline. Replace with something like: "What fills that gap is the question this book asks."

---

## Phase 3: The Student — Content Decisions

### 3A. Five Eyes surveillance header — REMOVE

Move ARPANET and family intel details to where they already appear in body sections. The header claim that Five Eyes tracked a 6-year-old goes.

### 3B. IQ numbers — DECIDED

"Range 80 (hand-eye) to ~180 (math/spatial), median ~168."

Keep the numbers. Add context: tests administered by Psych 101 college students at Keene State College, Bruce approximately age 10. Multiple instruments required (initial tests topped out). Bruce stands by the numbers from eidetic memory but makes no claim about tester competence. Corroborated by intellectual peerage with Dave Bannon (~165). Reframe in first person:

> Tested at approximately age 10 by college students in an introductory psychology course at Keene State College. The numbers I remember: range 80 (hand-eye) to approximately 180 (math/spatial), mean around 168. Multiple instruments required; initial tests topped out. I make no claim about the testers' competence or the precision of these numbers. They are what I remember.

### 3C. FBI wanted list — DECISION NEEDED

Is this documented? "Wanted list" is a strong claim. If records exist, keep with citation. If memory, consider: "Selective Service opened a case. I was told I was on an FBI list until age 25."

### 3D. MIC bomb

Reframe: "At 7 or 8 I discovered the TTY message service could be used to flood a terminal. I tested it on myself first, then on someone else." Early aptitude + boundary-testing without anachronistic "attack script" / "DOS" framing.

### 3E. 2026 email update — REMOVE

Breaks the frame and adds nothing. The Orlov quote and Gmail signature are irrelevant to recruitment fitness.

### 3F. Voice

Consider shifting The Student partially or fully to first person. Currently it's written in third person as if by a Five Eyes analyst. With C cosmetics removed, third person becomes awkward. "White male, age 34" → "I was 34." This is Bruce's own story — first person is more honest and more powerful.

---

## Phase 4: Structural

### 4A. Shared opening language — keep the echo

"A teacher who asks the right questions commits no crime. A student who derives conclusions from public science has received nothing classified." — This appears in both. Keep it. The yin-yang mirror is intentional and true under all possibilities.

### 4B. Investigation threads

Ensure each verifiable claim is presented cleanly enough for a curious reader to find:
- Rainbow Six (1998), character Timothy Hanley → in print. NOTE: Bruce knew Rainbow Six only as a video game. He did not know the novel existed until ~April 2026, twenty years after last contact with Healer. This constrains confabulation paths and should be stated explicitly in The Teacher.
- Bravo Two Zero patrol → public record
- K2 summit records → exist
- Reed College, Richard Crandall → verifiable
- Sanders Associates, Halsey Powell DD-686 → military/corporate records
- Selective Service → FOIA-requestable
- dieoff.org → Wayback Machine
- AssetExchange.com → corporate records
- Cult of the Dead Cow / Team 37 → well-documented
- **Corvallis, Oregon** → named clearly as the location of the 2003-2006 period. Do NOT mention specific contacts, the South Corvallis rental, or suggest investigation paths. A competent investigator will start there on their own. The city name is the thread; the reader pulls it.

### 4C. Build verification

```bash
cd ~/software/relinquishment && make html 2>&1 | tail -10
python3 build/verify-deep-links.py
```

---

## Decision log

| Item | Question | Recommendation |
|------|----------|---------------|
| 2A | Bravo Two Zero | Remove name, keep claim as [Healer's account], add footnote |
| 3B | IQ numbers | DECIDED: Keep numbers, add KSC Psych 101 context, first person, no accuracy claim |
| 3C | FBI wanted list | DECIDED: Keep. Documented — FBI sent letters citing felony violation of Selective Service Act (fine + prison). Bruce's letters also exist (digitized). FOIA-verifiable. Reframe in first person: "The FBI sent me letters citing a felony violation. I had written letters to the Director of Selective Service and two officials. A check of my FBI file will show the correspondence." |
| 3F | Student voice | DECIDED: First person throughout. Bruce's own story. |
| 4A | Shared opening | Keep the mirror |

---

## Scope estimate

This is a medium-to-heavy rewrite — not line edits but structural reframing. Probably two Generator sessions:
- Session 1: The Teacher (shorter, fewer decisions)
- Session 2: The Student (longer, voice shift, more content decisions)

Each needs its own subtask plan with exact line-level instructions.

---

## Do NOT

- Remove the Clancy/Rainbow Six connection (verifiable, investigation-friendly)
- Remove the K2 / UDHR origin point (emotionally and structurally essential)
- Remove the [clancy]/[observed] sourcing concept (expand it, don't drop it)
- Remove Section VI Assessment from The Teacher (career-path impossibility)
- Remove the mission statement box from The Student (works under B)
- Remove the Recruitment Assessment from The Student (strongest section)
- Add new C-level claims to replace removed ones
- "Fix" the A/B/C uncertainty — these chapters should leave the reader more curious, not more certain
