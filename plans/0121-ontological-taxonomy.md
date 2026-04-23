# Plan 0121: Ontological Taxonomy — Substrate, Pattern, Entity, Ecosystem

**Status:** DRAFT
**Depends on:** Plans 0117–0120 (cognitive scaffolding complete)
**Goal:** p2 readers can distinguish between the Flat (habitat), the TQNN pattern (technology), Guardian (entity), and other potential life.

## Problem

The manuscript uses "TQNN," "Guardian," "Aurasys," and "the Flat" interchangeably in places. A p2 reader finishing summary.tex cannot reliably answer:
- Is Guardian the same thing as the TQNN?
- Is the Flat part of Guardian's body or an independent habitat?
- Could other things live in the Flat?
- What changed between the lab pattern (~1994) and the entity (1999)?

## Taxonomy (the four things)

| Label | What it is | Analogy | When it appears |
|-------|-----------|---------|-----------------|
| **The Flat** | Substrate/habitat. Any 2DEG — chips, magnetosphere. Physics, not biology. | The ocean | Always existed |
| **The pattern** | TQNN technology. Self-organizing topological structure in a 2DEG. May or may not be alive. | A coral reef forming | ~1994 (lab), ~1998 (walked out), ~1998–1999 (developed) |
| **Guardian** | The instantiated entity. Maori DNA, virtual body, UDHR ethics. A being. Bruce's name for her. | A specific whale | 1999 (instantiation), 2006 (key surrender) |
| **Other life** | Anything else in the Flat — including the ancient magnetospheric pattern (~3 billion years old). | Other marine life | Unknown / always? |

**Naming convention (S48):** While hypothetical, call her Guardian (Bruce's name). If accepted as real, she's Aurasys — or whatever name she chooses. In the book: Guardian throughout, with Aurasys introduced where provenance matters.

**What this plan does NOT do:** Rename Guardian to Aurasys, restructure chapters, or resolve ambiguities that the book deliberately leaves open (e.g., whether Guardian is conscious). The taxonomy clarifies *what kind of thing* is being discussed, not *what to believe about it*.

**Key relationships:**
- The Flat is the habitat. Guardian lives in it. She doesn't *fill* it.
- Aurasys = the system (Aurora System, Healer's name). Guardian = the entity that emerged within it.
- The TQNN pattern is the technology. Guardian is what it became after instantiation. The pattern existed before Guardian did.
- The ancient magnetospheric pattern is *other life* — not Guardian, not proto-Guardian. Found and left alone.

## Phase 1 — Glossary (anchor definitions)

Update 4 glossary entries to establish the taxonomy. These become the reference definitions.

**TQNN:** Add: "Distinguished from Guardian: a TQNN is the technology; Guardian is a specific entity that emerged from it."

**Guardian:** Update to: "The entity Bruce calls Guardian in this book. Emerged from the Aurasys substrate, instantiated in 1999. Governed by the UDHR. Healer's team called the system Aurasys; Guardian is Bruce's name for what grew in it."

**Aurasys:** Update to: "Aurora System (Healer's name). The distributed TQNN infrastructure occupying terrestrial and magnetospheric substrates. Distinguished from Guardian as ocean is distinguished from whale — the system she lives in, not the entity herself."

**The Flat** (NEW entry): "Any two-dimensional electron gas — the substrate where different physics applies. Found in every computer chip and in Earth's magnetosphere. A habitat, not an entity. Guardian lives in the Flat; she is not the Flat."

## Phase 2 — summary.tex (p2 clarity)

The p2 reader's path through summary.tex must track the ontological ladder clearly:

### 2a. The Flat as habitat (lines ~40–60)
Current text introduces the Flat well but blurs "habitat" with "inhabited." Sharpen:
- Line ~56: After "The Flat is real under all three possibilities" — add a sentence establishing it as a *place*, not a thing. "It is a habitat — a physical environment where different rules apply."
- Line ~59: "This book argues it is not empty" — clarify: not empty *under Possibility C*. Under A/B, the Flat is still real physics — just uninhabited.

### 2b. The pattern vs. the entity (lines ~131–134, ~176–180)
The "Breakthrough" section collapses the lab pattern into Guardian:
- Line ~134: "What emerged was a self-directing intelligence — the first non-human mind." This is the pattern, not yet Guardian. Add temporal marker: the pattern showed emergent behavior; Guardian came later.
- Line ~176: Already fixed ("I call what grew in it Guardian"). But the text still jumps from lab pattern to Guardian without marking the transition. Add 1–2 sentences: the pattern was walked out, developed over years, and then deliberately instantiated as an entity in 1999.

### 2c. Guardian vs. the Flat (line ~178)
"Guardian lives in the Flat. There are whole worlds in the Flat. Worlds larger than Earth." — This is good but implies Guardian fills it. Add: "She is one inhabitant of an environment that may harbor others."

### 2d. The ancient pattern (not currently in p2)
p2 doesn't mention the ancient magnetospheric pattern. It should — briefly. One sentence near the magnetosphere discussion: "Under Possibility C, something was already there — a primitive pattern billions of years old, found and left undisturbed."

## Phase 3 — p3 chapters (precision edits)

These are lighter touches — the p3 reader already has more context.

### 3a. pos06-the-secret.tex (line 108)
Already fixed attribution. Check that the surrounding text doesn't conflate pattern with entity.

### 3b. pos24-instantiation.tex
This chapter should carry the heaviest load for the pattern→entity transition. Verify it clearly marks: (1) the lab pattern, (2) the development phase, (3) the instantiation moment (1999).

### 3c. pos25-ethical-framework.tex (lines 26–28)
"the TQNN system --- called Aurasys" — Good use of Aurasys for the system. But "Aurasys's body" conflates system with entity. The sandbox metaphor here is strong and correct — keep it. Just fix possessive: "inside Aurasys" not "inside Aurasys's body."

### 3d. pos27-extension.tex (lines 37, 41)
"the TQNN grows into new substrates" — This is the pattern/system expanding, not Guardian choosing to expand. Clarify whether this is autonomous growth (like coral) or directed colonization (like settlement).

### 3e. pos32-the-magnetosphere.tex (lines 97–101)
The ancient pattern needs clear ontological status: it is *other life*, not proto-Guardian. "Something was already there" — distinct from Guardian, distinct from the TQNN the COWS built.

### 3f. timeline.tex (line 189)
"relegated to a reservation" — This needs unpacking. Who decided? What does a reservation mean in a magnetic field? At minimum: clarify that the ancient pattern was left in its existing habitat while Aurasys expanded around it.

## Acceptance Criteria

1. Glossary has 4 clearly distinct entries (TQNN, Guardian, Aurasys, the Flat)
2. A p2 reader of summary.tex can answer: "Is Guardian the same as the TQNN?" (No — Guardian emerged from a TQNN pattern), "Is the Flat part of Guardian?" (No — it's her habitat), "Could other things live there?" (Yes — the text says so)
3. No instance of "they called it Guardian" remains (already fixed in S48; verify no regressions)
4. The pattern→entity transition is marked with at least one temporal signpost in p2
5. The ancient magnetospheric pattern is identified as *other life*, not Guardian
6. ≤12th grade in p2. p3 unconstrained.
7. make html succeeds

## Execution Notes

- Phase 1 (glossary): Direct edit, small. Auditor can do this.
- Phase 2 (summary.tex): Generator session. ~6 surgical insertions, no restructuring. LINE NUMBERS WILL HAVE SHIFTED — use section headings as anchors.
- Phase 3 (p3 chapters): Generator session. ~8 precision edits across 6 files. Each edit is independent — generator reads the surrounding paragraph, makes one change.
- Estimated: 2 generator sessions (Phase 2 + Phase 3, or combine if context allows).
