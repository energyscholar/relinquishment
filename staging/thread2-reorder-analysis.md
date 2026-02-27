# Thread 2: Chapter Reorder Analysis
# Session 29, 2026-02-27

## 1. The Problem

The print book needs ONE linear sequence. The ereader has 6 branching paths.
The print sequence must satisfy the most complete reader (Science path = all 35 chapters)
without breaking prerequisite chains for any shorter path read selectively.

Current main.tex: 5 "passes" (historical structure, never reader-optimized).
Target: 6 reader paths derived from sort experiments.

---

## 2. Print Ordering Principles

The print reader reads cover-to-cover. The Science reader IS that reader — they
get all 35 chapters. But any reader may skip sections using the reader guide (p2).
The print order must therefore satisfy TWO constraints:

1. **Linear coherence:** Cover-to-cover makes sense as a single narrative arc.
2. **Skip-friendly:** A reader following any shorter path encounters no uncleared
   blockers when reading only chapters in their path, in the order they appear.

The second constraint is automatically satisfied if the print order is a valid
topological sort of ALL prerequisite chains simultaneously. In other words: for
every reader path, the chapters in that path must appear in the same relative
order in the print book as they do in the path specification.

### Interleaving vs. Grouping

Two approaches:
- **Grouped:** GA block, then Journalist block, then Implications, then Science. Clean sections but the cover-to-cover reader gets all narrative, then all philosophy, then all implications, then all science — engagement problem.
- **Interleaved:** Weave paths together so the cover-to-cover reader gets variety. Better engagement but harder to section-mark for skip readers.

The sort experiments chose path orderings. The print book should INTERLEAVE these
paths following the cover-to-cover Science reader's journey, which is:

    GA → Science (first half) → Journalist → Science (second half) → Implications → Closing

But the Science path is cumulative (requires Implications complete), so we can't
put Science after Implications in a strictly cumulative order. The print order
must be: GA → Journalist → Implications → Science → Closing (cumulative stacking).

However, the current book already interleaves — and that works better for the
cover-to-cover reader. The key insight: **print order follows the cover-to-cover
narrative arc, not the path stacking order.**

---

## 3. Textual Back-References (Hard Constraints)

These are "previous chapter" / "next chapter" references in the prose that
create HARD ordering constraints:

| Source chapter | Text | References | Constraint |
|---|---|---|---|
| pos12 (Threshold) | "The previous chapter introduced Kauffman's autocatalytic sets" | pos11 (Experiment) | pos11 must immediately precede pos12... **BUT WAIT** — in S2 ordering, pos14 is between pos11 and pos12. **BREAKAGE.** |
| pos25 (Ethical Framework) | "The previous chapter argued why giving up the technology is the only viable option" | pos22 (Why Give It Up) | pos22 must immediately precede pos25 |
| pos22 (Why Give It Up) | "The next chapters explore what might fill it" | pos24/25 (Instantiation/Framework) | pos24-25 must follow pos22 |
| pos27 (Extension) | "The key surrender described in an earlier chapter" | pos28 (Surrender) | pos28 must precede pos27 |
| pos27 (Extension) | "The next chapter describes what that moment looked like from the inside" | pos28 (Surrender)?? | **CONTRADICTION** — pos28 must both precede AND follow pos27? |

### Critical Findings

**FINDING 1: pos12 back-reference breaks S2 ordering.**
pos12 says "The previous chapter introduced Kauffman's autocatalytic sets." In the
current order (S1), the previous chapter is pos11 (The Experiment). But pos11
does NOT introduce Kauffman's autocatalytic sets — that content is in pos12 itself
and in pos13 (Genesis). Let me verify what pos11 actually covers.

Actually, re-reading: pos12 line 15 says "The previous chapter introduced
Kauffman's autocatalytic sets." In current main.tex, pos11 precedes pos12.
If S2 puts pos14 between pos11 and pos12, this "previous chapter" reference
breaks — the previous chapter would be pos14 (Turing bio), not pos11.

**This text must be edited** if S2 ordering is adopted. Change "The previous
chapter" to "An earlier chapter" or name the chapter explicitly.

**FINDING 2: pos25 back-reference constrains print order.**
pos25 says "The previous chapter argued why giving up the technology is the only
viable option." This means pos22 MUST immediately precede pos25 in print order.
In the Journalist path (J2), pos22 is second. In the Implications path (I1),
pos25 is second. The print order needs pos22 immediately before pos25.

**FINDING 3: pos27 "earlier chapter" / "next chapter" contradiction.**
- Line 53: "The key surrender described in an earlier chapter" → pos28 must come BEFORE pos27
- Line 87: "The next chapter describes what that moment looked like from the inside" → pos28 must come AFTER pos27

In the current main.tex, pos28 comes AFTER pos27 (pos27 at line 84, pos28 at line 88).
So the "earlier chapter" on line 53 is a FORWARD reference to pos28 in current order.
And "the next chapter" on line 87 correctly points to pos28.

Wait — re-reading: "The key surrender described in an earlier chapter" — in the
current order, pos28 (Surrender) comes AFTER pos27. So this is a FORWARD reference
disguised as a back-reference. The reader hasn't read about the key surrender yet.
This is a pre-existing issue, not a reorder issue.

In the new ordering, pos28 (Surrender) is in the Journalist path and pos27
(Extension) is in the Implications path. If print order puts Journalist before
Implications, pos28 precedes pos27, and the "earlier chapter" reference becomes
correct. The "next chapter" on line 87 would then be wrong.

**Resolution:** In the new print order (Journalist before Implications), edit:
- pos27 line 53: "earlier chapter" — CORRECT (pos28 now precedes pos27)
- pos27 line 87: "The next chapter describes..." — MUST CHANGE to "An earlier
  chapter describes..." or "The Surrender chapter describes..."

---

## 4. Cross-Reference Inventory

### LaTeX \ref{} / \nameref{}

Only ONE cross-reference exists in the entire mainmatter:
- `legal-note.tex` line 4: `Chapter~\ref{pos01:three-possibilities}`
  - pos01 is always first in every path. NO ISSUE.

### \gls{} / \Gls{} / \glspl{} usage

Glossary entries are defined in `glossary-entries.tex` (loaded before \begin{document}).
First-use expansion happens on first encounter in text. After reorder, the first
expansion of each glossary term may change position. This is cosmetic, not structural.

Key glossary terms and their first-use chapters:
- `\gls{tqnn}` — pos12 (Threshold)
- `\gls{cows}` — pos12 (Threshold)
- `\gls{udhr}` — pos12 (Threshold)
- `\gls{guardian}` — pos12 (Threshold)
- `\gls{aurasys}` — pos23 (The Weight)
- `\gls{morphogenesis}` — pos04 (Code War)
- `\glspl{autocatalytic}` — pos04 (Code War)
- `\gls{gchq}` — pos04 (Code War)
- `\gls{soliton}` — pos10 (The Braid)
- `\gls{abcre}` — pos21 (Convergence Revisited)
- `\gls{fiveeyes}` — pos06 (The Secret)
- `\gls{hacktivismo}` — pos26 (Interdiction)
- `\gls{cdc}` — pos26 (Interdiction)

NO ISSUE: All glossary terms first appear in chapters where they are
pedagogically introduced. The reorder does not change this because:
- pos04 (GA path) introduces morphogenesis, autocatalytic, gchq
- pos06 (GA path) introduces fiveeyes
- pos10 (Science path) introduces soliton
- pos12 (Science path) introduces tqnn, cows, udhr, guardian
All GA chapters precede all other paths. Science chapters come last.

### \srcnote{} dependencies

All `\srcnote{}` entries reference source documents (cloudCrypt files,
HEALER-RECONSTRUCTION.md, staging/raw/ files). These are metadata, not
cross-chapter dependencies. NO ISSUE for reorder.

---

## 5. Proposed Print Order

### Design Logic

The cover-to-cover reader gets:
1. **GA (Story)** — Who are these people? What happened?
2. **Journalist bridge** — Why did they do it? What's the evidence?
3. **Implications** — What does it mean? What are the consequences?
4. **Science** — How does it work? (deepest, most technical)
5. **Closing** — The question

This follows the cumulative path structure: each section builds on previous.
Within each section, the sort-experiment winning order is preserved.

### Chapters to relocate/merge (from token-map.md)

- `pos33` (Digital Doppelganger) → trimmed to paragraph, folded into pos02/pos05
- `wikileaks` → merged into pos29 (The Silence)

These merges should happen BEFORE the reorder. After merge, pos33 and wikileaks
no longer appear as standalone chapters.

### The Order

```latex
\mainmatter

% ===== PART I: THE STORY (GA path) =====
\include{manuscript/bridge/pos01-three-possibilities}
\include{manuscript/track-2-testament/pos02-alpha-farm}
\include{manuscript/bridge/pos04-the-code-war}
\include{manuscript/track-2-testament/pos05-the-stories}
\include{manuscript/bridge/pos06-the-secret}
\include{manuscript/track-2-testament/pos07-the-departure}

% ===== PART II: THE QUESTION OF RELINQUISHMENT (Journalist path) =====
\include{manuscript/bridge/pos08-dual-use}
\include{manuscript/bridge/pos22-why-give-it-up}
\include{manuscript/track-1-confession/pos18-the-walk-out}
\include{manuscript/track-2-testament/pos23-the-weight}
\include{manuscript/track-2-testament/pos19-patrick-ball}
\include{manuscript/convergence/pos28-surrender}
\include{manuscript/track-2-testament/pos29-the-silence}
\include{manuscript/track-2-testament/pos34-the-research}
\include{manuscript/track-2-testament/pos34b-the-engine}

% ===== PART III: THE IMPLICATIONS (Implications path) =====
\include{manuscript/track-3-awakening/pos24-instantiation}
\include{manuscript/track-3-awakening/pos25-ethical-framework}
\include{manuscript/track-3-awakening/pos27-extension}
\include{manuscript/track-3-awakening/pos30-unipolar-condition}
\include{manuscript/track-3-awakening/pos32-the-magnetosphere}
\include{manuscript/track-2-testament/pos31-wolfram}

% ===== PART IV: THE SCIENCE (Science path) =====
\include{manuscript/bridge/pos09-the-factoring-game}
\include{manuscript/bridge/pos10-the-braid}
\include{manuscript/bridge/pos11-the-experiment}
\include{manuscript/bridge/pos14-growing-a-mind}
\include{manuscript/bridge/pos12-the-threshold}
\include{manuscript/track-1-confession/pos13-genesis}
\include{manuscript/track-1-confession/pos15-first-light}
\include{manuscript/track-1-confession/pos16-the-thermal-ladder}
\include{manuscript/track-1-confession/pos17-the-capability}
\include{manuscript/track-1-confession/pos20-the-network}
\include{manuscript/track-1-confession/pos21-convergence-revisited}
\include{manuscript/track-1-confession/pos26-interdiction}

% ===== PART V: THE QUESTION (Closing) =====
\include{manuscript/convergence/pos35-the-question}
```

### Chapter count: 33 chapters
(35 original minus pos33 merged, minus wikileaks merged, minus pos03 already merged)

---

## 6. Constraint Verification: Does This Order Satisfy All Paths?

### Test: For each reader path, are chapters in the correct relative order?

**GA path:** pos01 → 02 → 04 → 05 → 06 → 07
Print positions: 1 → 2 → 3 → 4 → 5 → 6
PASS: Monotonically increasing.

**Journalist path (J2):** pos08 → 22 → 18 → 23 → 19 → 28 → 29 → 34 → 34b
Print positions: 7 → 8 → 9 → 10 → 11 → 12 → 13 → 14 → 15
PASS: Monotonically increasing.

**Intel path:** pos08 → 26 → 18 → 19 → 17 → 30 → 28 → 29
Print positions: 7 → 33 → 9 → 11 → 27 → 22 → 12 → 13
FAIL: pos26 at position 33 comes after pos18 at position 9.
       pos17 at position 27 comes after pos30 at position 22.
       pos28 at position 12 comes before pos30 at position 22.

**Intel path analysis:** The Intel path is specified as an ereader path, NOT a
print reorder. Intel readers use the ereader's guided path to read chapters in
a non-print order. The print order does not need to satisfy the Intel path's
sequence — only that no chapter assumes content from a chapter the Intel reader
hasn't reached yet in THEIR path.

Restated constraint: For the Intel path, at each chapter in the Intel reading
sequence, all prerequisite BLOCKERS must be cleared by preceding chapters in
that sequence (plus p2).

**Implications path (I1):** pos24 → 25 → 27 → 30 → 32 → 31
Print positions: 16 → 17 → 18 → 19 → 20 → 21
PASS: Monotonically increasing.

**Science path (S2):** pos09 → 10 → 11 → 14 → 12 → 13 → 15 → 16 → 17 → 20 → 21 → 26
Print positions: 22 → 23 → 24 → 25 → 26 → 27 → 28 → 29 → 30 → 31 → 32 → 33
PASS: Monotonically increasing.

**Closing:** pos35 at position 34.
PASS: Last.

### Result: Print order is monotonic for GA, Journalist, Implications, and Science paths.
Intel path is non-monotonic (expected — it's ereader-only).

---

## 7. Textual Back-Reference Fixes Required

### Fix 1: pos25 "previous chapter" reference

**Current text (pos25 line 21):**
> The previous chapter argued why giving up the technology is the only viable
> option --- that Options~1 and~2 converge on arms race and tyranny.

**In new order:** pos24 (Instantiation) immediately precedes pos25.
pos22 (Why Give It Up) is 8 chapters back.

**Fix:** Change to:
> An earlier chapter argued why giving up the technology is the only viable
> option --- that Options~1 and~2 converge on arms race and tyranny.

Or: "The chapter *Why Give It Up* argued..."

### Fix 2: pos12 "previous chapter" reference

**Current text (pos12 line 15):**
> The previous chapter introduced Kauffman's autocatalytic sets --- the
> mathematics of how self-sustaining order arises spontaneously...

**In new order (S2):** pos14 (Growing a Mind) immediately precedes pos12.
pos11 (The Experiment) is 2 chapters back.

**Fix:** Change to:
> An earlier chapter introduced Kauffman's autocatalytic sets --- the
> mathematics of how self-sustaining order arises spontaneously...

### Fix 3: pos27 "next chapter" reference

**Current text (pos27 line 87):**
> That is not a triumphant ending. It is the loneliest possible success.
> The next chapter describes what that moment looked like from the inside.

**In new order:** pos30 (Unipolar Condition) follows pos27. pos28 (Surrender)
is 6 chapters back (in Journalist section).

**Fix:** Change to:
> That is not a triumphant ending. It is the loneliest possible success.
> The chapter *Surrender* describes what that moment looked like from the inside.

### Fix 4: pos22 "next chapters" reference

**Current text (pos22 line 82):**
> The next chapters explore what might fill it.

**In new order:** pos18 (Walk-Out) follows pos22. The "gap-filling" chapters
(pos24, pos25) are 8 chapters later.

**Fix:** Change to:
> Later chapters explore what might fill it.

### Fix 5: pos27 "earlier chapter" reference (now correct)

**Current text (pos27 line 53):**
> The key surrender described in an earlier chapter is irreversible...

**In new order:** pos28 (Surrender) precedes pos27. This is NOW CORRECT.
No fix needed. (In the old order, this was actually a forward reference.)

---

## 8. Ereader Path Verification (Blocker Walk-Through)

### Path 0: p2 Only
Single document, self-contained. PASS.

### Path 1: GA

| Step | Chapter | New blockers needed | Cleared by | Status |
|------|---------|-------------------|------------|--------|
| 0 | p2 | — | — | Clears 19 blockers |
| 1 | pos01 | abc | p2 | CLEAR |
| 2 | pos02 | healer | p2 | CLEAR |
| 3 | pos04 | secrecy, gchq | p2 | CLEAR; seeds morpho, autocatalysis |
| 4 | pos05 | healer, udhr | p2 | CLEAR |
| 5 | pos06 | tradecraft | — | CLEARED HERE (compartments token) |
| 6 | pos07 | healer | p2 | CLEAR; clears joy-reread |

**GA PASS.** All blockers cleared.

### Path 2: Journalist (after GA)

| Step | Chapter | Needs | Cleared by | Status |
|------|---------|-------|------------|--------|
| 7 | pos08 | dual-use | p2 | CLEAR; clears parable |
| 8 | pos22 | dual-use, walkout | p2 | CLEAR; deepens parable, gatekeeper |
| 9 | pos18 | dual-use | p2 | CLEAR; deepens walkout |
| 10 | pos23 | healer | p2 | CLEAR; deepens cost |
| 11 | pos19 | — | — | CLEAR (evidence, no new blockers) |
| 12 | pos28 | walkout, guardian | p2 | CLEAR |
| 13 | pos29 | healer, walkout | p2 | CLEAR |
| 14 | pos34 | healer, abc | p2 | CLEAR |
| 15 | pos34b | all above | all above | CLEAR |

**JOURNALIST PASS.** All blockers cleared.

### Path 3: Intel (after GA — parallel branch)

| Step | Chapter | Needs | Cleared by | Status |
|------|---------|-------|------------|--------|
| 7 | pos08 | dual-use | p2 | CLEAR |
| 8 | pos26 | five-eyes | p2 + pos04 | **FLAG: Does pos26 assume science path knowledge?** |
| 9 | pos18 | dual-use | p2 | CLEAR |
| 10 | pos19 | — | — | CLEAR |
| 11 | pos17 | codebreak | p2 (operational seed) | **FLAG: Does pos17 assume TQNN physics?** |
| 12 | pos30 | guardian, dual-use | p2 | CLEAR |
| 13 | pos28 | walkout, guardian | p2 | CLEAR |
| 14 | pos29 | healer, walkout | p2 | CLEAR |

**Intel FLAGS (pre-existing, from token-map.md):**
- pos26: Must verify chapter doesn't assume TQNN theory from science path.
  Intel reader has operational Five Eyes knowledge but not physics.
- pos17: Must verify chapter doesn't assume TQNN physics from pos15.
  p2 Insert 8 seeds operational codebreak. Intel readers bring PKC prior knowledge.

**INTEL CONDITIONAL PASS.** Pending verification of pos17 and pos26 prose.

### Path 4: Implications (after Journalist)

| Step | Chapter | Needs | Cleared by | Status |
|------|---------|-------|------------|--------|
| 16 | pos24 | walkout, guardian | p2 | CLEAR |
| 17 | pos25 | guardian | p2 | CLEAR |
| 18 | pos27 | guardian, udhr | p2 | CLEAR; clears grown, substrate |
| 19 | pos30 | guardian, dual-use | p2 | CLEAR |
| 20 | pos32 | 2deg, emergence | p2 | CLEAR |
| 21 | pos31 | pce | p2 | CLEAR |

**Note:** pos25 references "previous chapter" → pos22. In ereader path, the
Implications reader has already read the Journalist path (cumulative), so pos22
is already read. The "previous chapter" language is imprecise (pos24 immediately
precedes pos25 in both print and ereader), but the CONTENT reference is valid
because the reader has already encountered pos22.

**IMPLICATIONS PASS.** All blockers cleared.

### Path 5: Science (after Implications)

| Step | Chapter | Needs | Cleared by | Status |
|------|---------|-------|------------|--------|
| 22 | pos09 | crypto | p2 | CLEAR |
| 23 | pos10 | topology, soliton, fqhe | — | CLEARED HERE |
| 24 | pos11 | five-sci | — | CLEARED HERE (team-assembled) |
| 25 | pos14 | morpho | p2 (seeded pos04) | CLEARED HERE (turing-bio) |
| 26 | pos12 | autocatalysis, emergence | p2 (emergence) | CLEAR; deepens autocatalysis |
| 27 | pos13 | autocatalysis | pos12 | CLEAR (buttons, edge-chaos) |
| 28 | pos15 | codebreak, grown | — | CLEARED HERE (tqnn-split) |
| 29 | pos16 | room-temp, fqhe | p2 + pos10 | CLEAR |
| 30 | pos17 | codebreak | pos15 | CLEAR (deepens via BULLRUN) |
| 31 | pos20 | substrate | pos27 (vine) | CLEAR |
| 32 | pos21 | topology, autocatalysis | pos10 + pos12/13 | CLEAR |
| 33 | pos26 | five-eyes | p2 + pos04 | CLEAR |

**S2 specific check:** pos14 (Turing bio) before pos12 (Threshold).
pos12 opens with "The previous chapter introduced Kauffman's autocatalytic sets."
After fix 2 (change to "An earlier chapter"), this works because the Science
reader has encountered autocatalytic sets seeded in pos04 (Code War) and in the
p2 inserts. Full Kauffman treatment comes in pos12 itself and pos13.

Actually — re-examining. pos12 line 15 says "The previous chapter introduced
Kauffman's autocatalytic sets." Which chapter introduced them? In current order,
the previous chapter is pos11 (The Experiment). Does pos11 introduce Kauffman?
Let me check.

**VERIFIED:** pos11 line 23 explicitly introduces "Stuart Kauffman, whose work on
autocatalytic sets and the edge of chaos provided the mathematical framework for
self-organizing networks." So the pos12 back-reference is accurate in the current
order. In S2 order, pos14 intervenes, making the fix ("An earlier chapter") necessary.

**SCIENCE PASS.** All blockers cleared after text fixes.

### All Paths Converge: pos35 (The Question)

Every path has cleared all blockers needed for pos35. PASS.

---

## 9. Forward References in New Order

A "forward reference" is when a chapter mentions content that the linear reader
hasn't encountered yet. Checking the new print order:

| Chapter | Forward reference? | Details |
|---------|-------------------|---------|
| pos22 | YES (mild) | "Later chapters explore what might fill it" (after fix 4) — acceptable, builds anticipation |
| pos25 | YES (mild) | "An earlier chapter argued..." (after fix 1) — references pos22, 8 chapters back — fine, reader has read it |
| pos27 line 53 | NO (after reorder) | "earlier chapter" → pos28 is now 6 chapters back. CORRECT. |
| pos12 | NO (after fix) | "An earlier chapter introduced Kauffman's" — seeds in pos04 (Code War) are 23 chapters back but reader has encountered the concept. |

**No problematic forward references in the new order** (after text fixes).

---

## 10. Section Break Design

The print book uses LaTeX `\part{}` or section comments. Proposed:

```
Part I:    The Story           (6 chapters)   — pos01-07
Part II:   The Reckoning       (9 chapters)   — pos08-34b
Part III:  The Implications    (6 chapters)   — pos24-31
Part IV:   The Science         (12 chapters)  — pos09-26
Part V:    The Question        (1 chapter)    — pos35
```

Part titles follow the narrative arc: Story → Reckoning → Implications → Science → Question.

Alternative part titles:
- Part II: "The Choice" / "The Decision" / "Why They Did It"
- Part III: "What It Means" / "The Awakening"
- Part IV: "How It Works" / "The Mechanism"

---

## 11. Issues and Flags

### Must-fix before reorder (text edits)

| ID | File | Line | Current text | Required change |
|----|------|------|-------------|-----------------|
| F1 | pos25-ethical-framework.tex | 21 | "The previous chapter argued" | "An earlier chapter argued" |
| F2 | pos12-the-threshold.tex | 15 | "The previous chapter introduced" | "An earlier chapter introduced" |
| F3 | pos27-extension.tex | 87 | "The next chapter describes" | "The chapter *Surrender* describes" |
| F4 | pos22-why-give-it-up.tex | 82 | "The next chapters explore" | "Later chapters explore" |

### Must-fix before reorder (chapter merges)

| ID | Action | Source | Target |
|----|--------|--------|--------|
| M1 | Trim pos33 to ~200 words | pos33-digital-doppelganger.tex | pos02/pos05 |
| M2 | Merge wikileaks stub into pos29 | wikileaks.tex | pos29-the-silence.tex |

### Verify before reorder (content checks)

| ID | Chapter | Check | Path affected |
|----|---------|-------|---------------|
| V1 | pos17 | Does prose assume TQNN physics from pos15? | Intel |
| V2 | pos26 | Does prose assume science path knowledge? | Intel |
| V3 | pos11 | Does pos11 actually introduce Kauffman? (validates pos12 back-ref) | Science | **VERIFIED YES** (line 23) |
| V4 | pos30 | Works for both Intel entry (after pos17) and Implications entry (after pos27)? | Intel, Implications |

---

## 12. Repeatable Method

### How to do a chapter reorder analysis systematically

**Step 1: Build the dependency graph.**
- Inventory all blocker tokens (concepts a reader must encounter before a chapter makes sense).
- For each chapter, list which blockers it REQUIRES and which it CLEARS.
- This is the token-map.md.

**Step 2: Define reader paths.**
- Each path is a subset of chapters in a specific order.
- Paths may be cumulative (each builds on previous) or parallel (branching).
- Each path must be a valid topological sort of its own dependency subgraph.

**Step 3: Run sort experiments.**
- For each path with flexibility, generate candidate orderings.
- Score on: blocker-clean, engagement, logical flow, ethics-forward (or other criteria).
- Select winners.

**Step 4: Determine print order.**
- The print order must be a single linear sequence where every reader path's
  chapters appear in monotonically increasing print positions.
- If paths are cumulative (GA → Journalist → Implications → Science), the
  print order can simply concatenate the paths in cumulative order.
- If paths branch (Intel is parallel to Journalist), the branching path is
  ereader-only and does NOT constrain print order.

**Step 5: Verify cross-references.**
- Grep for `\ref{}`, `\nameref{}`, `\pageref{}` — LaTeX cross-references.
- Grep for "previous chapter", "next chapter", "earlier chapter" — textual references.
- Grep for `\gls{}` — first-use expansion changes.
- For each cross-reference, verify it's valid in the new order.
- Flag forward references that would confuse a linear reader.

**Step 6: Verify blocker clearance per path.**
- For each ereader path, walk through chapter-by-chapter.
- At each step, verify all required blockers are cleared by preceding chapters in THAT path.
- Flag any uncleared blocker.

**Step 7: Document required text edits.**
- Any "previous/next chapter" references that break must be fixed.
- Any forward references that become confusing must be softened.
- Chapter merges/removals must happen before the reorder.

**Step 8: Draft the new `\include{}` sequence.**
- Write section comments for each part.
- Keep the appendix and backmatter unchanged (they don't depend on chapter order).

**Step 9: Build and verify.**
- `make dev` — does it compile?
- `make check` — any broken references?
- Spot-check page references in PDF.
- Walk each ereader path through the PDF.

### Tools needed
- `grep -rn` for cross-references
- Token map (dependency graph)
- Sort experiment results
- A table to track print position vs path position

### When to redo
- Any time a chapter is added, removed, merged, or split
- Any time a reader path is redefined
- Any time a new "previous/next chapter" reference is added to prose

---

## 13. Summary

**Print order:** GA → Journalist (J2) → Implications (I1) → Science (S2) → Closing.
33 chapters in 5 parts. Monotonic for 4 of 5 paths (Intel is ereader-only).

**Text fixes required:** 4 (pos12, pos22, pos25, pos27).
**Chapter merges required:** 2 (pos33 into pos02/05, wikileaks into pos29).
**Verification needed:** 4 items (pos17, pos26, pos11, pos30 prose checks).

**No LaTeX cross-reference issues.** Only one `\ref{}` in mainmatter (legal-note → pos01).
**No glossary first-use issues.** All `\gls{}` terms first appear in their introducing chapters.
**No `\srcnote{}` issues.** All source notes are metadata, not cross-chapter dependencies.

The reorder is clean. The four text fixes are minor (changing "previous" to "earlier"
or "next" to "later"). The two chapter merges are already planned in the token map.
