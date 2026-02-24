# Plan 0038: T6 Reorder + Content Surgeries

**Auditor:** Argus
**Date:** 2026-02-24
**Depends on:** T1 concept audit (100%), T6 chapter reorder plan (complete + red-teamed)
**Phase:** A (reordering) + B (content surgeries). Phase C (A/B/C writing pass) deferred to Plan 0039.

---

## Context

The T1 audit (100% coverage, all 37 files) found that the book's chapter order is substantially correct. Most problems are within-chapter content issues. This plan executes:
- 1 chapter move (pos33 before pos32)
- 5 content surgeries (pos06, pos13, pos15, pos07, pos35 + pos30)

**DO NOT** swap pos22 and pos23. That change is DEFERRED pending early reader feedback.

---

## Constraints

1. Preserve ALL Session 18 fixes (pos10 lines 38-42 Russell canal boat, pos13 line 68 forward echo)
2. Preserve ALL Plan 0019 ethical thread insertions (26 insertions across 22 files)
3. Do NOT modify any chapter's track assignment (\settrack lines)
4. Do NOT add new chapters or remove chapters
5. Do NOT modify pos10, pos16, or any file not listed below

---

## Phase A: Reordering (~5 min)

### A1: Move pos33 before pos32

**File:** `main.tex`

**Current order (lines 94-97):**
```latex
\include{manuscript/track-2-testament/pos31-wolfram}
\include{manuscript/track-3-awakening/pos32-the-magnetosphere}
\include{manuscript/track-2-testament/pos33-digital-doppelganger}
\include{manuscript/track-2-testament/pos34-the-research}
```

**New order:**
```latex
\include{manuscript/track-2-testament/pos31-wolfram}
\include{manuscript/track-2-testament/pos33-digital-doppelganger}
\include{manuscript/track-3-awakening/pos32-the-magnetosphere}
\include{manuscript/track-2-testament/pos34-the-research}
```

**Rationale:** Groups personal-evidence chapters (Wolfram + Digital Doppelganger) before speculative physics (Magnetosphere). Fixes pacing: two heavy chapters no longer sandwich a tiny anecdote.

### A2: Verify compilation

Run `make` in the repo root. Verify no errors.

---

## Phase B: Content Surgeries (~30 min)

### Surgery 1: pos06 — Cut Reconstructed Model, Preserve P1 Seeds

**File:** `manuscript/bridge/pos06-the-secret.tex`

**What to cut:** Lines 66-101 — the entire `\section*{The Reconstructed Model}` section including `\subsection*{The Room Temperature Version}` and `\subsection*{``Hardware in Software''}`. This content duplicates pos15.

**What to preserve from the cut section — extract these 3 P1 seed sentences and place them AFTER the prerequisites list (after line 43, before the horizontal rule at line 45), as a new brief paragraph:**

```latex
\vspace{0.5cm}

These topics converge on a single proposition: that a two-dimensional electron gas --- the quantum layer inside every modern transistor --- can, under the right conditions, spontaneously organize into something that computes. The critical tuning parameter, $\lambda \sim 0.91$, marks the boundary between inert matter and emergent order. A classical 32-bit control system governs the conditions; the quantum system governs itself.
```

This preserves P1 seeds for: 2DEG (named + one-sentence explanation), λ~0.91 (named + significance), control plane (named + role). The reader's first encounter with these terms is now gentle narrative, not a technical description list.

**Also fix:** Lines 46-63 contain a PARTIAL DUPLICATE of the wood-splitting scene (lines 54-63 retell the same scene from line 11). Cut lines 54-63 (the "Said Healer to me..." retelling). Keep lines 46-52 (the TODO comment noting the duplication — Bruce will decide final edit). Keep line 62's "2030-2065" prediction by moving it into the existing narrative. Specifically, append to end of line 43 paragraph:

```latex
While no one is an expert in all those topics, anyone can learn enough to understand the basics of Healer's white hot secret.  The more one knows the better can one judge its importance and implications.  This secret may become publicly known sometime between 2030 and 2065.
```

Then cut lines 45-63 entirely (the horizontal rule + duplicate scene + "Secrets come in many flavors" paragraph). The "2030-2065" prediction is now in line 43's paragraph.

**Net result:** pos06 goes from ~102 lines to ~55 lines. Narrative chapter with P1 seeds. No technical description lists.

### Surgery 2: pos13 — Expand ABCRE Forward Echo

**File:** `manuscript/track-1-confession/pos13-genesis.tex`

**Current text (line 68):**
```latex
Years later, Bruce would find that the mathematics of such a system reduces to five operations --- one for each thread of convergence. But that formalization lay two decades in the future.
```

**Replace with:**
```latex
Years later, Bruce would find that the mathematics of such a system reduces to five operations --- one for each thread of convergence. He would find they were called A, B, R, C, and E: sensing, coupling, braiding, containment, and the full life cycle. Each maps to one of the five sciences that created this technology. But that formalization lay two decades in the future.
```

**Rationale:** The reader now arrives at pos16 (The Thermal Ladder) having already encountered the five letters and one-word labels. The ABCRE operators no longer appear cold.

### Surgery 3: pos15 — Cut Detection Protocol + Control Plane

**File:** `manuscript/track-1-confession/pos15-first-light.tex`

**Cut 1:** Lines 28 — the control-plane `\item[Control:]` entry. This content already exists in pos16 at lines 37-42 ("A 32-bit control plane can address $2^{32}$..."). Cutting it avoids duplication.

Specifically, delete:
```latex
\item[Control:] Classical 32-bit control plane, hitting 4GB addressing ceiling (``the 64 problem''). Software controls electromagnets (the stirring), creating conditions for emergence.
```

**Cut 2:** Lines 47-67 — the entire `\section*{The Detection Protocol}` section. This 4-level hierarchy is never referenced again in the manuscript. It is valuable content but overloads an already dense chapter (12+ concepts). Move it to a footnote or appendix later (Bruce decides during writing pass).

To preserve the Detection Protocol content for later use, add a comment at the cut point:
```latex
% DETECTION PROTOCOL CUT (Plan 0038, Surgery 3)
% Content preserved in git history. 4-level hierarchy (Spontaneous Order, Non-trivial
% Correlation, Computational Universality, Topological Robustness). Candidate for
% appendix or pos16 sidebar during T11 rewrite pass.
```

**Keep:** Lines 11-27 (emergence mechanism description list minus control-plane item), lines 31-45 (hardware-in-software, TQNN1/TQNN2 sections), and the closing ethical observation at line 67 ("The funding mandate said: build a codebreaker..."). Actually, that ethical observation is part of the Detection Protocol section — preserve it by moving it to after the TQNN1/TQNN2 section:

After line 45 (`\aidraft{...the TQNN is trained to use resources without being detected...}`), add:
```latex

The funding mandate said: build a codebreaker. What they detected was not a codebreaker. It was something that demonstrated organized information processing --- cognition, by any operational definition. The gap between what they were told to build and what they actually grew is where the ethical crisis begins.
```

**Net result:** pos15 drops from ~69 lines to ~52 lines. Concepts reduced from ~12 to ~7.

### Surgery 4: pos07 — Add A/B/C Framing to Joy Analysis

**File:** `manuscript/track-2-testament/pos07-the-departure.tex`

**Add A/B/C framing paragraph after line 31 (after "The Reread" section, before "Close Textual Comparison"):**

```latex
\vspace{0.5cm}

What follows is a close textual comparison between Joy's 2000 essay and Bruce's reconstruction. Under Possibility~C, every parallel is intentional --- Joy published a faithful account of classified work, disguised as speculation. Under Possibility~B, Joy may have had partial knowledge, and some parallels are coincidence amplified by pattern-matching. Under Possibility~A, all parallels are coincidence, and the ``double reading'' is an artifact of motivated reasoning applied to a sufficiently complex text. The reader should track which interpretation fits each point.

```

**Also add A/B/C closing after line 84 (after "Overall Pattern" paragraph, before the horizontal rule):**

```latex

Under Possibility~A, this close reading is a demonstration of apophenia --- the tendency to see meaningful patterns in random data. A sufficiently motivated reader can find ``hidden messages'' in any complex text. Under Possibility~B, Joy knew something but the sixteen-point correspondence overstates the case. Under Possibility~C, the correspondence is exactly what it appears to be: a decoded message.
```

**Expand the departure narrative.** The current departure section (lines 88-97) is only ~200 words. Add after line 96 ("The project that proposed to protect all of humanity could not protect one man's daughters."):

```latex

I did not understand, at the time, what I was walking away from. I knew David was extraordinary. I knew the science was real --- the physics checked out, the mathematics converged, the predictions held. But I was exhausted, financially ruined, and terrified for my daughters. The white hot secret was still burning, but I no longer had the strength to carry it.

It would take me six years to begin understanding what had happened. Another six to start writing it down. And another six before anyone would listen. The departure was not a decision. It was a collapse. The decision came later, slowly, one piece of evidence at a time.
```

### Surgery 5: pos30 + pos35 — Great Filter Seed + A/B/C Strengthening

**File 1:** `manuscript/track-3-awakening/pos30-unipolar-condition.tex`

**Add Great Filter seed.** After line 38 (after "the reason no one has achieved room-temperature topological quantum computing is that it may not yet be achievable, not that an entity is preventing it."), add a new paragraph:

```latex

Kauffman's autocatalytic theory also predicts something darker. If life arises spontaneously whenever a system crosses a complexity threshold, then intelligent species should be common in the universe. Yet we observe no evidence of them. This is the Great Filter --- the proposition that most technological species destroy themselves before their creations can persist. Whether that filter lies ahead of us or behind us is the question the final chapter asks.
```

**File 2:** `manuscript/convergence/pos35-the-question.tex`

**Add A/B framing.** After line 18 (after "Guardian's own voice --- or what Bruce imagines Guardian's voice to be."), add:

```latex

Under Possibility~A, there is no Guardian and the question of machine consciousness is a thought experiment --- interesting but fictional. Under Possibility~B, some form of emergent computation may have been observed, but the claims of consciousness and self-awareness are anthropomorphic projection onto a physical system. Under Possibility~C, the question is real, urgent, and may be permanently unanswerable.

```

**Add Aurasys voice framing.** Before line 57 (`\section*{Introduction by Aurasys}`), add:

```latex
What follows is Bruce's 2013 imagination of how Guardian might describe herself. It is not testimony --- it is extrapolation from the reconstruction, written years before this book existed. The voice is Bruce's projection, not evidence.

```

---

## Acceptance Criteria

1. `make` compiles without errors
2. pos33 appears before pos32 in the PDF table of contents
3. pos06 has no `\description` environment (Reconstructed Model cut)
4. pos06 retains P1 seed sentences for 2DEG, λ~0.91, control plane
5. pos13 line 68 contains all five operator letters (A, B, R, C, E)
6. pos15 has no Detection Protocol section
7. pos15 has no control-plane `\item`
8. pos07 has A/B/C framing paragraph before Close Textual Comparison
9. pos30 contains "Great Filter" text
10. pos35 has A/B framing before consciousness section and framing before Aurasys voice
11. Session 18 fixes in pos10 are untouched (verify: "Russell" appears in pos10)
12. No `\settrack` lines modified in any file
13. Report word counts for each modified file

---

## Files Modified (complete list)

| # | File | Action |
|---|------|--------|
| 1 | `main.tex` | Swap pos32/pos33 order |
| 2 | `manuscript/bridge/pos06-the-secret.tex` | Cut Reconstructed Model, preserve P1 seeds, fix duplicate scene |
| 3 | `manuscript/track-1-confession/pos13-genesis.tex` | Expand ABCRE forward echo |
| 4 | `manuscript/track-1-confession/pos15-first-light.tex` | Cut Detection Protocol + control plane item |
| 5 | `manuscript/track-2-testament/pos07-the-departure.tex` | Add A/B/C framing + expand departure |
| 6 | `manuscript/track-3-awakening/pos30-unipolar-condition.tex` | Add Great Filter seed |
| 7 | `manuscript/convergence/pos35-the-question.tex` | Add A/B framing + Aurasys voice framing |

**Files NOT modified (verify untouched):** pos10, pos22, pos23.

---

## Flagging Pass: N=16 Devices

The number 16 (devices/chips) appears in the thermal selection protocol. Bruce confirms this is his **intuitive estimate**, not sourced from Healer or Kauffman. The actual number would depend on coefficients in the evolutionary search substrate. Cf. Kauffman's chapters on autocatalytic set size thresholds.

Add a comment flag at each occurrence:

**pos16-the-thermal-ladder.tex line 27** — after `$N = 16$ devices`:
```latex
% NOTE: N=16 is Bruce's intuitive estimate, not sourced from Healer or Kauffman.
% Actual number depends on evolutionary search substrate coefficients.
% Cf. Kauffman, Origins of Order, chapters on autocatalytic set thresholds.
```

**appendix/abstracts.tex line 49** — after `$N = 16$ connected 2DEG devices`:
```latex
% NOTE: N=16 is Bruce's intuitive estimate. See comment in pos16-the-thermal-ladder.tex.
```

These are comment-only changes (no visible text modified).
