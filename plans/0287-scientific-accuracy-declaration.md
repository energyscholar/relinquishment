# Plan 0287: Scientific Accuracy Declaration — F-woo Multi-Angle Defense

**Status:** DRAFT — Bruce reviewing angles
**Author:** Auditor (Argus S64)
**Priority:** HIGH — addresses 10th failure mode (F-woo), field-tested
**Origin:** Phoenix field test (2026-05). Gen explained concepts → he went directly to Dancing Wu Li Masters / crystals / quantum mysticism. Book never declares intent to be scientifically accurate. That's the gap.

---

## Problem

The book is full of real physics but never says "this book tries to be scientifically accurate." The reader cannot distinguish it from Zukav's *Dancing Wu Li Masters* (1979), which also describes "real physics" but uses it as metaphor for mysticism.

**F-woo** (quantum mysticism appropriation) is the mirror of **F-crank** (physicist dismissal). They amplify each other: every Phoenix-type enthusiast who embraces the book for woo reasons makes every Chen-type physicist more likely to dismiss it.

The word that kills F-woo is **accuracy** — stated as intent, not just demonstrated through citations.

**Current state:** The summary (line 48) says "Every claim above is published, peer-reviewed physics" — but this is buried 48 lines into the summary, and "published" is a claim Zukav could also make. Nowhere does the book say "this book attempts to be scientifically accurate" or equivalent.

---

## Defense Angles

### Angle 1: Title Tooltip (relinquishment-title)

**File:** `build/hover-definitions.yaml`, line 16
**Current:** "Real physics, real people, real institutions."

**Proposed:** Add accuracy declaration to the tooltip panel. Something like:
"This book attempts scientific accuracy throughout. Every physics claim is sourced to published, peer-reviewed, reproducible research. Where the author speculates, he says so."

**Why here:** The title tooltip fires on first interaction. Any reader who hovers on the title gets the accuracy frame before reading a word.

---

### Angle 2: Front Matter — Summary (early, prominent)

**File:** `manuscript/00-front/summary.tex`
**Placement:** Near the top, before any physics content. Currently line 48 has "Every claim above is published, peer-reviewed physics" but that's too late and too passive.

**Need:** An explicit statement of intent near the opening. Not buried. Not hedged. Something that says: this is not metaphor, not mysticism, not entertainment. This is an attempt at accuracy.

**Draft direction (Bruce to finalize voice):**
"This book attempts to be scientifically accurate. Every physics claim in it is sourced to published, peer-reviewed research that the reader can verify. Where the author speculates beyond what is established, he says so explicitly. This is not metaphor."

---

### Angle 3: Hinge 1 Strengthening (The Flat)

**File:** `manuscript/spine/the-flat.tex`
**Current Hinge 1 text (Plan 0283):**
"Nothing described here requires physics beyond what is already published and reproduced. The substrate, the confinement, the topological protection --- these arise from conditions that can be created and studied. Nothing about them lies outside known science. What remains open is what these conditions produce when sustained, at scale, without interruption."

**Possible strengthening:** Add one sentence that explicitly separates from quantum mysticism. Something like: "This is engineering physics, not metaphor." Or: "Every claim here can be tested in a laboratory."

**Trade-off:** Hinge 1 is already the most explicit of the four. Adding too much makes it a disclaimer rather than a clarification. Gen's design principle was "install once, let consequences propagate." May be better to let Angle 2 (front matter) carry the explicit F-woo disarm and leave H1 as-is.

---

### Angle 4: Entry Point Deep Links

Readers arriving via shared links may land at:
- `#the-flat` — highest F-woo risk (quantum language, 2DEG, wormholes)
- `#the-wrong-substrate` — F-woo risk (magnetosphere, "life in space")
- `#the-braid` — moderate (topological computing)
- `#firmware-update` — already has accuracy framing (LLM evaluation context)

**Mechanism:** The chapter-level `\section*` headers already have heading-link anchors. The p-level escalation system (onHover) provides grounding at each layer. Consider whether the p1 (8th grade) layer at these entry points explicitly says "real physics, not metaphor."

**Current p1 for The Flat:** Need to check — may already ground adequately or may need a one-line F-woo disarm.

---

### Angle 5: The Hook

**File:** `manuscript/00-front/hook.tex`
**Current:** No accuracy language at all.

The hook is the absolute first thing anyone reads. If "scientifically accurate" appears anywhere, it arguably belongs here — even as a single phrase. "A scientifically accurate account of..." or similar.

**Trade-off:** The hook is Bruce's most carefully crafted prose. Adding a disclaimer-like phrase could damage its rhythm. May be better to handle this in the subtitle/tagline or summary.

---

## Angles NOT Recommended

- **Subtitle change** — "Relinquishment" as a single-word title is too strong to dilute with a subtitle. The accuracy frame belongs in the content, not the packaging.
- **Footer/header on every page** — over-engineering. One clear declaration + strategic reinforcement is enough.
- **Repeating in every chapter** — violates Gen's "install once" principle.

---

## Recommended Priority

1. **Angle 2 (Summary)** — highest impact, most readers see it, Bruce controls voice
2. **Angle 1 (Title tooltip)** — second contact point, interactive readers
3. **Angle 5 (Hook)** — if it can be done without damaging rhythm
4. **Angle 4 (Entry points)** — check existing p1 layers first
5. **Angle 3 (Hinge 1)** — may not need strengthening if Angle 2 lands

---

## Acceptance Criteria

1. At least one prominent, unmistakable declaration of scientific accuracy intent
2. Declaration appears before any physics content in reading order
3. F-woo reader encounters "accuracy" frame before encountering "quantum"
4. No damage to Bruce's voice or the hook's rhythm
5. Consistent with Gen's hinge design principle (install once, let propagate)

---

## Open Questions for Bruce

1. What's your preferred phrasing? "Scientifically accurate" / "attempts accuracy" / "can be verified" / something else?
2. Hook: sacred, or open to a phrase?
3. Should Gen weigh in on this? (She saw Phoenix fail — she may have thoughts on phrasing)
