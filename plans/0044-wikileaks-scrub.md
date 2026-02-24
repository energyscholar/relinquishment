# Plan 0044: WikiLeaks Scrub + Redacted Chapter

**Auditor:** Argus
**Date:** 2026-02-24
**Depends on:** None (can execute independently). Plan 0041 has its own WL-related edits noted below.
**Phase:** Single phase

---

## Context

Bruce's decision: remove ALL mention of WikiLeaks, Julian Assange, and Daniel Domscheit-Berg from the entire rendered manuscript. Replace with ONE visible redacted chapter that signals "something is here" without stating what.

**Rationale (Bruce's words):** "If someone makes claims that THE TQNN GUY IS ASSOCIATED WITH WIKILEAKS that claimant looks like the crazy conspiracy theorist, because there's no THERE there."

**Principle:** The absence is visible. The content is absent. The reader sees a gap and knows something is missing. The book itself provides zero textual support for the WL connection. Anyone who makes the connection did it on their own.

---

## Constraints

1. The word "WikiLeaks" must NOT appear anywhere in the rendered PDF (including TOC, chapter titles, timeline, footnotes, srcnotes visible in output)
2. "Julian Assange" must NOT appear anywhere in the rendered PDF
3. "Domscheit-Berg" must NOT appear anywhere in the rendered PDF
4. The redacted chapter MUST be visible in the table of contents — the gap must be obvious
5. Staging/raw (.md) files are NOT scrubbed — they don't render. Leave them for historical record.
6. `\srcnote` lines are NOT rendered in the PDF (they're comments/metadata). Change them for consistency but they're low priority.
7. Do NOT modify any `\settrack` lines
8. Do NOT modify any content unrelated to the WL scrub

---

## Files to Modify

### 1. wikileaks.tex — Rename + rewrite redaction notice

**File:** `manuscript/track-2-testament/wikileaks.tex`

**Current:**
```latex
\chapter{WikiLeaks}
\label{ch:wikileaks}

The author has material on this topic that he has chosen not to include in this edition...
```

**Replace entire file with:**
```latex
\settrack{tracktwo}

\chapter{[Redacted]}
\label{ch:redacted-chapter}

\vspace{2cm}

\begin{center}
\large\textit{This chapter has been removed from the current edition.}

\vspace{1cm}

\normalsize
The author possesses material relevant to this position in the narrative. He has chosen not to include it due to the safety of people who may still be at risk and the sensitivity of ongoing events. The material concerns a project the author was invited to participate in and declined --- a decision he describes elsewhere as his greatest regret.

\vspace{0.5cm}

Under Possibility~A, this redaction is theater --- there is nothing to redact. Under Possibility~B, there may be something, but the claimed sensitivity is overstated. Under Possibility~C, the author's caution is well-founded, and the material will appear when circumstances permit.

\vspace{0.5cm}

The reader will notice gaps in the surrounding chapters where this material would naturally connect. Those gaps are intentional.
\end{center}

\chapterreturn
```

### 2. pos09-the-factoring-game.tex — Remove Assange epigraph

**File:** `manuscript/bridge/pos09-the-factoring-game.tex`

**Lines 7-13, current:**
```latex
\begin{quote}\small
\textit{``Cryptography is the ultimate form of non-violent direct action.''}

\hfill --- Julian Assange
\end{quote}
```

**Replace with a different cryptography epigraph:**
```latex
\begin{quote}\small
\textit{``Privacy is necessary for an open society in the electronic age.''}

\hfill --- Eric Hughes, ``A Cypherpunk's Manifesto'' (1993)
\end{quote}
```

**Rationale:** Eric Hughes is a cDc-adjacent cypherpunk. The quote is thematically appropriate for the chapter (factoring/cryptography). It removes the Assange attribution without leaving a gap. The Cypherpunk's Manifesto is a real document (March 9, 1993).

### 3. pos29-the-silence.tex — Remove DMSRedacted WL references

**File:** `manuscript/track-2-testament/pos29-the-silence.tex`

**NOTE:** If Plan 0041 has already been executed (replacing the entire file), these lines won't exist. Verify before editing. If Plan 0041 has NOT been executed yet, apply these changes to the current file.

**Line 23:** `\DMSRedacted{subsequent transparency initiatives --- see WikiLeaks chapter}`
**Replace with:** `\DMSRedacted{subsequent events --- see redacted chapter}`

**Line 31:** `\DMSRedacted{subsequent transparency initiatives --- see WikiLeaks chapter}`
**Replace with:** `\DMSRedacted{subsequent events --- see redacted chapter}`

### 4. pos20-the-network.tex — Remove DMSRedacted WL references

**File:** `manuscript/track-1-confession/pos20-the-network.tex`

**Line 75:** `\DMSRedacted{subsequent transparency initiatives --- see WikiLeaks chapter}`
**Replace with:** `\DMSRedacted{subsequent events --- see redacted chapter}`

**Line 109:** `\DMSRedacted{subsequent transparency initiatives --- see WikiLeaks chapter}`
**Replace with:** `\DMSRedacted{subsequent events --- see redacted chapter}`

### 5. pos31-wolfram.tex — Scrub srcnote

**File:** `manuscript/track-2-testament/pos31-wolfram.tex`

**Line 55:** `\srcnote{HEALER-RECONSTRUCTION.md lines 807-838 | staging/raw/pos31-wolfram.md | 2026-02-15 | WikiLeaks veto, thank-you letter, ``the human condition'' linguistic transfer}`

**Replace with:** `\srcnote{HEALER-RECONSTRUCTION.md lines 807-838 | staging/raw/pos31-wolfram.md | 2026-02-15 | Veto, thank-you letter, ``the human condition'' linguistic transfer}`

### 6. timeline.tex — Remove WL entries

**File:** `manuscript/appendix/timeline.tex`

**Line 192:** `\item[Aug 2006] Julian Assange founds WikiLeaks.`
**Action:** DELETE this line entirely.

**Line 220:** `\item[2016] Russiagate scandal begins when WikiLeaks publishes emails leaked from the DNC that reveal dishonest electoral behavior during the 2016 Democratic Primary elections.`
**Action:** DELETE this line entirely.

### 7. main.tex — Rename include (optional)

**File:** `main.tex`

**Line 92:** `\include{manuscript/track-2-testament/wikileaks}`

**Option A:** Leave as-is (the filename doesn't appear in the PDF).
**Option B:** Rename file to `redacted-chapter.tex` and update include.

**Recommendation:** Option A (simpler, filename is internal only).

---

## Plan 0041 Coordination

Plan 0041 (pos29 complete rewrite) must ALSO be scrubbed before Generator execution. The following changes are needed in the plan file (NOT in the manuscript — the plan file contains the text the Generator will write):

### Already applied (this session):
- Phone Call: "He spoke in vague terms --- no group name, no specifics"
- Phone Call: "I came to believe that the project was what became WikiLeaks" → needs further scrub (see below)
- Recognition: "I became convinced that WikiLeaks was David's project" → needs further scrub

### Still needed in Plan 0041:

**Phone Call section — remove "WikiLeaks":**

Current (after earlier edit):
```
Years later, after the block broke, I came to believe that the project was what became WikiLeaks --- or something like it. That the role Julian Assange later took, or something like the role Daniel Domscheit-Berg played, had been offered to me first. I cannot prove this. Nothing about that phone call, taken on its own, rules out Possibility~A.
```

Replace with:
```
Years later, after the block broke, I came to believe that the project became something far larger than either of us. What it became --- and why I believe that --- belongs to a chapter that has been redacted from this edition. I cannot prove the connection. Nothing about that phone call, taken on its own, rules out Possibility~A.
```

**Recognition section — remove "WikiLeaks":**

Current (after earlier edit):
```
I became convinced that WikiLeaks was David's project --- or that it became what David's project had been meant to become. That Julian Assange had done the job I'd been vetoed from doing, or something like it. This is my interpretation, not something David told me.
```

Replace with:
```
I became convinced that Healer's project became something I could see in the news --- something large and consequential that matched what he had described in vague terms. Someone else had done the job I'd been vetoed from doing. This is my interpretation, not something Healer told me. The specifics belong to the redacted chapter.
```

**Recognition A/B/C block — remove "whistleblowing platform":**

Current:
```
Under Possibility~A, a man with an overactive pattern-matching faculty connected an Australian acquaintance to a famous whistleblowing platform based on nationality and timing. Under Possibility~B, David may have been peripherally connected to transparency activism, and Bruce inflated the connection. Under Possibility~C, the connection is exactly what it appears to be. The reader should note that the WikiLeaks chapter, when it is written, will examine this claim in detail.
```

Replace with:
```
Under Possibility~A, a man with an overactive pattern-matching faculty saw a vague invitation and a public event and connected them after the fact. Under Possibility~B, Healer may have been peripherally connected to the events Bruce later identified, but the connection is inflated. Under Possibility~C, the connection is exactly what it appears to be. The redacted chapter, when it is eventually published, will examine this claim in detail.
```

**Europe section — remove "WikiLeaks associates":**

Current (after earlier edit):
```
By 2010 the CIA was tracking WikiLeaks associates. I recognized the signs --- or thought I did. There was zero electronic record between me and Healer --- every interaction in person, that single phone call the only exception. But I was scared. Easy prey if I stayed.
```

Replace with:
```
By 2010 there were reasons to be scared that I cannot fully explain in this edition. I recognized signs --- or thought I did --- that intelligence services were paying attention to people connected to the events described in the redacted chapter. There was zero electronic record between me and Healer --- every interaction in person, that single phone call the only exception. But I was scared. Easy prey if I stayed.
```

---

## Acceptance Criteria

1. `make` compiles without errors
2. The string "WikiLeaks" does NOT appear in ANY rendered .tex file
3. The string "Assange" does NOT appear in ANY rendered .tex file
4. The string "Domscheit" does NOT appear in ANY rendered .tex file
5. A chapter titled "[Redacted]" appears in the table of contents
6. The redacted chapter contains A/B/C framing
7. The redacted chapter references "a project the author was invited to participate in and declined"
8. All DMSRedacted references updated from "WikiLeaks chapter" to "redacted chapter"
9. Timeline has no WikiLeaks entries
10. pos09 has a cypherpunk epigraph (not Assange)
11. Plan 0041's text (if not yet executed) contains zero WL/Assange/Domscheit references
12. Staging/raw files are UNTOUCHED (historical record)
13. Report: grep -r "WikiLeaks\|Assange\|Domscheit" across all .tex files shows zero hits

---

## Execution Order

1. Apply Plan 0044 edits (this plan) to all .tex files
2. Apply Plan 0041 WL scrub edits to the plan file (if not yet executed)
3. Then execute Plan 0041 (which will write the scrubbed pos29)
4. Verify with grep

**IMPORTANT:** If Plan 0039 (A/B/C pass) has already been executed on pos29, those insertions will be overwritten by Plan 0041 anyway. If Plan 0039 has NOT been executed, its pos29 insertions (4A, 4B, 4C) contain WL references and should be skipped — Plan 0041 supersedes them.

---

## Generator Handoff Prompt

```
You are the Generator. Read the plan at:
~/software/relinquishment/plans/0044-wikileaks-scrub.md

Execute all edits in sections 1-6 (7 is optional, recommendation: skip).

Constraints:
- The word "WikiLeaks" must not appear in ANY .tex file after execution
- "Assange" and "Domscheit" must not appear in ANY .tex file
- Do NOT modify staging/raw (.md) files
- Do NOT modify \settrack lines
- Verify with: grep -ri "wikileaks\|assange\|domscheit" manuscript/**/*.tex

Files to modify (6):
1. wikileaks.tex — full rewrite (redacted chapter)
2. pos09-the-factoring-game.tex — replace epigraph
3. pos29-the-silence.tex — 2 DMSRedacted edits (if Plan 0041 not yet executed)
4. pos20-the-network.tex — 2 DMSRedacted edits
5. pos31-wolfram.tex — 1 srcnote edit
6. timeline.tex — delete 2 lines

After execution:
1. Run `make` and verify compilation
2. Run grep verification (criterion 13)
3. Report results

Report completion.
```
