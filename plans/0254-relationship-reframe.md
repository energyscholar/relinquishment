# Plan 0254 — Relationship Reframe: Witness, Not Recruit

**Auditor:** Argus (S63)
**Date:** 2026-04-25
**Status:** DRAFT — awaiting Bruce passage-by-passage approval
**Source:** Gen's issue #4 on has-anyone-looked + Gen's April 26 go-ahead
**OPSEC:** Correction #11 applies — less operational speculation = less surface area

---

## Core Reframe

Gen's insight: "The simplest explanation is that Healer wanted the story
eventually told. That makes Bruce legible less as a recruit than as a
future witness."

The telling, not the onboarding, was the point. The book is stronger
accepting the relationship as partially opaque than trying to solve it
operationally.

---

## Affected Passages

### 1. The Departure (REVISE — testimony stays, framing changes)

**Files:** `track-2-testament/pos07-the-departure.tex` line 89,
`record/the-departure.tex` line 64 (duplicate)

**Current:**
> In September 2006, I was told my services would not be required. My
> children could not be protected --- the divorce, the custody
> arrangements, the impossibility of shielding them from what was
> coming. Healer delivered this without cruelty. It was an operational
> assessment, not a rejection of me as a person.

**Issue:** "My services would not be required" frames Bruce as an
operative whose employment ended. "Operational assessment" doubles down.
The testimony (what was said) is real. The framing (how it's interpreted)
is the problem.

**Proposed revision:** Keep the testimony — Bruce WAS told these words.
Reframe the interpretation. Something like:

> In September 2006, Healer told me it was over. My children could not
> be protected --- the divorce, the custody arrangements, the
> impossibility of maintaining cover around a fractured family. He
> delivered this without cruelty. At the time I heard it as rejection.
> Twenty years later, I think the teaching was already complete. I had
> received what I was meant to receive. The rest was up to me.

The "operational assessment" sentence is cut. The "services would not be
required" language is replaced. The family vulnerability stays (it's
real and emotionally load-bearing). The new interpretation: the teaching
was the point, and it was done.

**Bruce decides:** Does this revision reflect what you now believe?

### 2. The Weight / The Parting (REVISE)

**File:** `track-2-testament/pos23-the-weight.tex` lines 38-40

**Current:**
> In August 2006 I informed him that I could no longer assist him, and
> that I was sick of waiting for something to happen. At about the same
> time Healer and his friends decided, quite correctly, that I was now
> a bad security risk.
>
> Healer told me that, because my children could not be protected, I
> was now a security risk to the project. He also told me that I had
> been rejected for membership in a notorious hacker collective.

**Issue:** "Security risk to the project" and "assist him" are
operational-recruit framing. "Rejected for membership" is apparatus.

**Proposed revision:**

> In August 2006 I told him I was done waiting. At about the same time,
> the relationship ended. The teaching was complete. Whether the
> departure was operational or personal, I cannot fully resolve. He
> told me my children could not be protected. He also told me I had
> been rejected for membership in a collective I never applied to join.

Keep the hacker collective detail — it's specific, strange, memorable,
and doesn't need operational framing to be interesting. Cut "security
risk to the project." Cut "assist him" (recruit language).

**Bruce decides:** Is the hacker collective detail worth keeping?

### 3. The Target (REFRAME HEADER — body may stay)

**File:** `record/the-target.tex` lines 28-34

**Current header:**
> What follows is my reconstruction of what a Five Eyes recruitment
> file on me probably looked like in mid-2003. I don't have the actual
> file. But I know the file existed. The interesting question is: does
> this candidate fit the mission?
>
> Find someone capable of receiving a multi-year guided deduction...
> the student must be capable of --- and dispositionally inclined toward
> --- publishing what he's learned...
>
> Read this file and ask yourself: is this the guy?

**Issue:** "Recruitment file" is the heaviest recruit-framing in the
book. But the chapter body is brilliant — the detailed profile IS the
argument for why Bruce was selected. And the closing line "is this the
guy?" is powerful.

**Observation:** The profile already contains the witness reframe
implicitly: "the student must be capable of --- and dispositionally
inclined toward --- publishing what he's learned." That's witness
language. The file describes someone chosen to eventually TELL the story.

**Proposed revision:** Minimal. Change "recruitment file" to
"assessment file" or "selection file." Change "pre-recruitment window"
to "pre-contact window." The body stays — it already reads as witness
selection if you've absorbed Gen's reframe. The profile doesn't describe
an operative. It describes a future author.

**Bruce decides:** Change the framing words, or leave the whole chapter
as-is and let the reader feel the shift?

### 4. Summary + Timeline References (MECHANICAL)

**File:** `00-front/summary.tex` line 251
> "he recruited and began mentoring Bruce Stephenson"

**Proposed:** "he selected and began mentoring Bruce Stephenson" or
"he found and began mentoring Bruce Stephenson"

**File:** `appendix/timeline.tex` line 193
> "(Author's Hypothesis) Healer recruits Energyscholar at Alpha Farm"

**Proposed:** "Healer begins mentoring Energyscholar at Alpha Farm"

**File:** `appendix/topic-guide.tex` line 28
> "Guided Deduction: The Recruitment"

**Proposed:** "Guided Deduction: The Selection" (matches the-target.tex
label `record:tgt-recruitment-assessment`)

**Note:** Other uses of "recruit" in the book are fine — they describe
ULTRA II team recruitment, Freedman's recruitment by Microsoft, SAS
selection training. These are factual/hypothetical and not part of the
Bruce-as-operative framing.

---

## What NOT to Touch

- The A/B/C framing in the departure scene (line 97 of pos07) — it's
  already doing the work Gen wants. Under A, the departure is "a
  convenient exit from a relationship built on deception." That
  interpretation stays.
- Wolfram's "Were you recruited?" (pos31/pos29) — this is WOLFRAM'S
  word, not Bruce's framing. Testimony, not interpretation.
- "Burned operative" / protective detail passages (what-healer-said) —
  these are observation, not relationship framing.
- The Target chapter body — the detailed profile is excellent and
  already implicitly supports the witness reading.

---

## Phasing

| Step | Work | Gate |
|------|------|------|
| 1 | Bruce reviews each proposed revision (4 items above) | Bruce approves per-passage |
| 2 | Generator executes approved revisions | |
| 3 | Build + verify no broken refs | |

This is a CONTENT plan — every line change needs Bruce's approval
before execution.

---

## Acceptance Criteria

- [ ] "Services would not be required" language removed or reframed
- [ ] "Operational assessment" removed
- [ ] "Security risk to the project" removed
- [ ] "Recruitment file" → "assessment/selection file" (if approved)
- [ ] Summary/timeline "recruits" → "selected/mentored" (if approved)
- [ ] All changes preserve A/B/C viability
- [ ] Testimony (what was said) preserved; interpretation (how it's
      framed) updated
- [ ] `make dev` clean

---

*Plan 0254 written by Argus (Auditor), S63.*
