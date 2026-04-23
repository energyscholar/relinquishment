# Plan 0220: Visual Language System

**Purpose:** Systematize the book's visual vocabulary — colors, patterns, icons — so every visual element communicates content type without words. Reduce cognitive burden on GA readers by using every available communication channel.

**Motivation:** The book already has epistemic color stripes (Gold/Blue/Purple for A/B/C content) but they're too subtle for most readers to notice, and there's no key explaining the correspondence. Colors are a wasted signal. We're not in 1977 CLI anymore — we have the full visual palette. Use it.

**Relationship to other plans:**
- **0219** (collapsible tech sections): builds the HIDE/SHOW mechanics. 0220 wraps visual language around it (e.g., gold background on collapsed A-content sections).
- **0148** (deep links): shares the questions-index infrastructure. Visual cues on deep link anchors would use the same color system.

**Scope:** Design + implement a visual language the reader acquires through progressive immersion. HTML reader gets full interactive treatment. PDF gets a simpler version (colors carry, interactivity doesn't).

---

## Core Insight: Lapine Pedagogy

The reader learns the visual vocabulary the way readers of Watership Down learn Lapine --- through immersion, not instruction. Symbols are planted early with full verbal context. By mid-book, the reader recognizes them without translation. By late chapters, symbols alone carry meaning.

This mirrors the book's own pedagogy: Healer taught Bruce through guided deduction, not explanation. The visual language teaches the reader the same way.

**Three phases of reader acquisition:**
1. **Introduction** (front matter, early chapters): symbol appears WITH the word, every time. Reader doesn't need the symbol --- the word is right there.
2. **Reinforcement** (middle chapters): symbol appears near the concept but not always adjacent. Reader starts recognizing the pattern.
3. **Fluency** (late chapters): symbols appear in margin notes, section markers, navigation cues. Reader decodes without thinking. The symbol IS the concept.

**Copy-paste constraint:** All symbols are CSS `::before` / `::after` content or `aria-hidden="true"` spans. Visual layer only. Copy-paste yields clean prose. Same architecture as deep link share anchors, which are already invisible to copy.

---

## Design Principles

1. **One signal per channel.** Color carries epistemic status. Icon carries content type. Symbol carries concept identity. Position carries hierarchy. Don't overload any channel.

2. **Color = trustworthiness signal.** Gold = established science (holds under A/B/C). Blue = narrative/deduction (Bruce's account, interpretation). Purple = Possibility-C claims (speculative under A/B). The reader learns: gold is safe to trust, blue is one person's experience, purple is the claim you're evaluating.

3. **Epistemic icons (paired with color, accessible without it):**
   - ✔ (U+2714) Gold --- verified, established
   - ✎ (U+270E) Blue --- personal account, authored
   - ✦ (U+2726) Purple --- extraordinary claim, your call

4. **Content-type icon:** ⚙ (U+2699) Gear --- "technical machinery, safe to skip." Used on collapsed tech sections. Coexists with epistemic icons.

5. **Concept symbols (progressive vocabulary --- Lapine set, TBD):**
   Recurring concepts get Unicode symbols that the reader learns through immersion. Candidates (to be refined):
   - ⬡ --- the Flat (2D geometry, hexagonal lattice)
   - ⇌ --- wormhole / nonlocal connection
   - ⚡ --- classical backchannel (electrical signal)
   - ❊ --- autocatalytic emergence (flowering)
   - ⊘ --- the silence gap (void, nothing said)
   - ♚ --- Custodian
   - (more TBD --- keep set small, ~8-12 max)

6. **Legend exists but isn't primary.** A legend is available (nav bar or front matter) but the real teaching is immersion. By the time the reader finds the legend, they already know most of the symbols.

7. **Accessibility first.** ~8% of men are deuteranopic. Gold/Blue/Purple is a reasonable palette. Always pair color with icon or symbol --- never color-only.

8. **Subtlety gradient.** Early appearances: subtle, beside the word. Later appearances: more prominent. The visual hierarchy reinforces the reading hierarchy.

---

## Inventory: What We Have

### Epistemic color stripes
- Currently in the text as colored markers on certain passages
- Gold (A-content), Blue (narrative), Purple (C-content)
- No legend or explanation anywhere in the reader
- Rendering mechanism: TBD — need to audit current CSS/HTML implementation

### Collapsed tech sections (Plan 0219)
- Currently: left border, italic title, muted gray
- Opportunity: gold background tint on summary line (all 15 sections are A-content)
- Signals "established science" before the reader reads a word

### Custodian interludes
- Currently styled distinctively (italic, different voice)
- Opportunity: could use a subtle color accent to mark Custodian voice

### Deep link share anchors
- Currently: `#` icon
- Opportunity: could be color-coded by category (skeptic, science, verification, ethics, curiosity, narrative)

### Chapter headers in navigation
- Currently: plain text in accordion
- Opportunity: color dot or stripe indicating primary content type of each chapter

---

## Phases (high-level — detailed sub-plans TBD)

### Phase 1: Audit & Design
- Audit current color implementation (CSS classes, where applied, consistency)
- Design the unified palette (exact hex values for Gold/Blue/Purple in light and dark mode)
- Design the legend (placement, format)
- Design accessibility fallbacks (icons, labels)
- Create a style guide document or section in the build README

### Phase 2: Legend & Introduction
- Add color legend to the reader (location TBD — nav bar, front matter, or both)
- Ensure the legend is visible on first visit and accessible on demand

### Phase 3: Collapsed Section Styling
- Apply gold background tint to `details.tech-section summary` (all tech-collapse sections are A-content)
- Verify the color + existing left-border + italic doesn't become too busy
- Test on phone

### Phase 4: Chapter Navigation Cues
- Add color indicators to chapter headers in the accordion nav
- Spine chapters (A-content) get gold marker
- Record chapters (blue) get blue marker
- Interludes (purple/Custodian) get their own marker

### Phase 5: Deep Link & Inline Polish
- Color-code deep link share anchors by category
- Review inline epistemic stripes for consistency with the new palette
- Ensure hover panels / rich panels use consistent color language

---

## Open Questions

1. **Where does the legend live?** Nav bar (always visible) vs. front matter (read once) vs. tooltip on first encounter (contextual). All three?

2. **How prominent?** The gold background on collapsed sections — a subtle tint or a clear wash? The risk of too-strong is that it feels garish; too-weak and it's invisible again.

3. **PDF treatment.** Colors work in PDF but interactivity doesn't. Should the PDF have a color legend in the front matter? Should collapsed sections (which render expanded in PDF) still have the gold marker?

4. **Interlude color.** Custodian voice is... what color? It's not A (science), not B (narrative), not C (claim). It's its own epistemic category — the voice of the entity being described. A fourth color? Or a variation on purple?

5. **How many colors total?** Three (A/B/C) is clean. Four (+ Custodian) is manageable. Five or more is noise. Where's the line?

---

## Risk Assessment

**Medium risk.** This is a UX/design project, not a code architecture project. The risk is aesthetic: too much color = circus, too little = invisible. Iterative testing on Bruce's phone is the real feedback loop. No structural risk to the build pipeline — it's CSS and possibly minor HTML class additions.

**Dependency:** Plan 0219 pilot must pass evaluation first. The visual language wraps around existing features; it doesn't change their mechanics.
