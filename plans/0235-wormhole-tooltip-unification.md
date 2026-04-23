# Plan 0235 — Wormhole Tooltip Unification + Auto-Detect Deployment

**Status:** SUPERSEDED BY Plan 0236 (Phase 1a+2) and Plan 0238 (Phase 1b)
**Author:** Auditor (Argus S59)
**Date:** 2026-04-21
**Related:** Plan 0215 (auto-detect hover terms), Plan 0232 (LLM verification — wormhole conflation failure mode), Plan 0219 (collapsible sections)

---

## Problem

"Wormhole" is the single most dangerous misunderstanding in the book. Every reader who encounters the word without context will think Einstein-Rosen bridges (Interstellar, sci-fi). The book means topological wormholes — a completely different physical mechanism.

**Current state:** 97 instances of "wormhole(s)" in the HTML. Only 8 are hover-wrapped. The title page has a weaker panel (`wormholes-title`) that lacks the comparison table and mechanism explanation. Deep-link visitors may land anywhere and see an unwrapped "wormhole" with zero context.

**Evidence:** ChatGPT A/B/C evaluation (2026-04-20) demonstrated this exact failure mode — even a frontier LLM with the book's definitions loaded STILL conflated topological with spacetime wormholes repeatedly. If an LLM fails, a human reader will fail harder.

---

## Phase 1: Strengthen the Wormhole Panel

### Add mechanism text to the disambiguation panel

Bruce's text for HOW a topological wormhole works (currently missing from all panels):

> A wormhole in this substrate works by braiding anyons. Move one anyon around another, and the quantum state of the system changes in a way that depends only on the topology of the path — not on how fast, how precisely, or how smoothly the braid was executed.

This goes into the `wormholes` HTML panel (line ~197 of `hover-definitions.yaml`) as a new paragraph AFTER "Not the science-fiction kind" and BEFORE the comparison table.

### Unify title page panel with body panel

Replace the weak `wormholes-title` entry with the strong `wormholes` panel content (comparison table + mechanism text + SVG). Specifically:

1. In `hover-definitions.yaml`: change `wormholes-title`'s `html:` to match the updated `wormholes` panel (with the new mechanism paragraph)
2. Keep `wormholes-title` as a separate YAML key (the title page hover system uses it), but its `html:` content should be identical to the `wormholes` panel
3. Update `wormholes-title`'s `text:` from "placeholder" to the same text as `wormholes`'s `text:` field

### Test

- Build HTML
- Hover "Wormholes" on title page — should show comparison table + mechanism text + SVG
- Hover "wormholes" in any body chapter — should show same panel
- Verify no duplicate hover-id conflicts between `wormholes-title` and `wormholes`

---

## Phase 1b: Quantum-to-Classical Handoff (Phonon I/O)

### Problem

The SVG grid sequence and "All your electricity" punchline in `the-flat.tex` establish that wormholes move quantum information and classical backchannels complete the transaction. But there's a gap: HOW does quantum information arriving via teleportation convert to classical information the network can use? The mechanism is phonon-photon coupling (Hasslacher's domain), already described in `the-braid.tex` (§"Hasslacher's Lattice", line 47):

> Electron-phonon coupling bridges the quantum 2DEG to classical electronics: the quantum system reads and writes through lattice vibrations. Phonon-photon coupling bridges the chip to electromagnetic radiation. Two interface layers, both from the same physics.

This is a Dr. Chen question, not a GA question. GA readers need only know the handoff is native to the substrate. Dr. Chen needs to see WHY.

### Two layers

**GA layer — tooltip:** Add a brief tooltip on "classical backchannel" or near the punchline in `the-flat.tex`. Content: something like "The quantum-to-classical handoff is native to the 2DEG substrate — electron-phonon coupling provides the interface. See §Hasslacher's Lattice in The Braid for the mechanism." This closes the logical gap for GA without dragging them into phonon physics.

Add a `quantum-classical-handoff` entry to `hover-definitions.yaml` with:
- `text:` One sentence: the 2DEG's lattice vibrations naturally bridge quantum state to classical signal.
- `html:` Two paragraphs: (1) the GA reassurance, (2) the phonon-photon coupling mechanism with a deep link to `spine:braid-hasslacher-lattice`.

**Dr. Chen layer — collapsible section:** In the Flat chapter (`the-flat.tex`), near the Backchannels or Punchline section, add a collapsible science section (Plan 0219 architecture) titled something like "The I/O Problem" or "How the Handoff Works." Content:
- Electron-phonon coupling: quantum state in the 2DEG reads/writes through lattice vibrations
- Phonon-photon coupling: lattice vibrations emit/absorb photons — bridging to electromagnetic signals
- Two interface layers, both native to the substrate, both from Hasslacher's published work
- This is why the quantum-to-classical conversion isn't engineered — it's a property of any crystal lattice hosting a 2DEG

This section should be collapsed by default (GA never sees it) and expandable for technical readers.

### Placement

The collapsible section goes in `the-flat.tex` (both spine and track-3 versions) BEFORE the Punchline section — after the reader understands backchannels exist but before the logical chain snaps shut. The tooltip gets auto-deployed by Phase 2 wherever "wormhole" appears near backchannel discussion.

### Test

- Build HTML
- Verify collapsible section is collapsed by default, expands on click
- Verify tooltip shows on hover for the new term
- Verify deep link to `spine:braid-hasslacher-lattice` resolves

---

## Phase 2: Auto-Detect All Instances (Plan 0215)

Execute Plan 0215 (`~/software/relinquishment/plans/0215-auto-detect-hover-terms.md`). Read it in full — it's detailed and has critical constraints (no tooltip-in-tooltip recursion, term matching rules, exclusion zones).

This will auto-wrap the first occurrence of every YAML-defined term per chapter, including "wormhole(s)." The 89 unwrapped instances become hover-wrapped. Every deep-link visitor gets the disambiguation.

### Critical: Phase 2 depends on Phase 1

Phase 1 must be complete before Phase 2, because Phase 2 will auto-wrap "wormhole" instances to point at the `wormholes` hover-id. That panel must already contain the strong content including the mechanism text.

---

## Generator Handoff

Phase 1a: In `hover-definitions.yaml`, add Bruce's mechanism paragraph to the `wormholes` panel HTML (after "Not the science-fiction kind", before the table). Then copy the updated `wormholes` panel HTML and text into `wormholes-title`. Also update `Wormholes` (capitalized variant, line ~207) to match. Build, test hover on title page and body. One commit.

Phase 1b: (1) Add `quantum-classical-handoff` entry to `hover-definitions.yaml` with GA-level tooltip text and Dr. Chen HTML panel including phonon mechanism + deep link to `spine:braid-hasslacher-lattice`. (2) Add a collapsible science section in `the-flat.tex` (BOTH spine/ and track-3-awakening/ versions) before the Punchline section, using Plan 0219 collapsible architecture. Title: "The I/O Problem" or similar. Content: electron-phonon coupling + phonon-photon coupling = native quantum-to-classical interface. Reference Hasslacher. Collapsed by default. Build, test collapse behavior + tooltip + deep link. One commit.

Phase 2: Read and execute Plan 0215 in full. Build, test auto-detection across chapters. Verify no recursion, no broken tooltips. Separate commit.

Do NOT open browser — build and report ready. Bruce will verify visually.
