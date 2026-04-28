# Plan 0141: A/B/C Chapter Labels — Icons and Color-Coding

**Status:** Draft
**Parent:** PTL-115 (book science sections)
**Depends on:** `plans/reader-preparation-requirements.md` (chapter-level A/B/C assignments)
**Touches:** `build/menu-tooltips.yaml`, `build/preprocess.py`, CSS in preprocess.py, possibly `reader.js`

---

## Purpose

Label every chapter in the TOC menu and chapter headings with its A/B/C epistemic status. The skeptical reader should see at a glance: most of this book is verified physics (A). The self-mocking C labels give permission to be skeptical. The A-labeled content — wormholes in chips, planetary-scale 2DEGs, capabilities nobody pursues — is the gasp moment.

**The structural move:** The A chapters are a publishable pop-science book. Custodian and the C narrative make it unpublishable through normal channels. Labeling makes this visible. A earns trust. B earns curiosity. C gets read because A and B did their jobs.

---

## Design

### Icons

| Label | Icon | Tone | Message |
|-------|------|------|---------|
| A | TBD — checkmark, Nobel medal, or textbook icon. Must read as "verified." | Authoritative, calm | "This is textbook. Check it yourself." |
| B | TBD — magnifying glass, scales, or question mark. Must read as "evidence to weigh." | Neutral, inviting | "Evidence to weigh. You decide." |
| C | Tinfoil hat (self-mocking) | Disarming, honest | "I know. Read it anyway." |

**Icon selection:** Bruce to choose. Options should be tested as small inline glyphs (~16px) next to chapter titles in the TOC. Could be emoji, SVG, or Unicode. Emoji is simplest; SVG is cleanest at small sizes.

**Tinfoil hat candidates:**
- Custom SVG (small, clean, distinctive)
- 🧢 or similar emoji as placeholder
- Text label `[C]` as fallback

### Color scheme

Background tint on TOC menu items (subtle, not garish):
- **A:** Light gold or warm neutral — "verified, solid ground"
- **B:** Light blue or cool neutral — "interesting, weigh it"
- **C:** Light purple or warm gray — "testimony, you decide"

Colors must work in both light and dark contexts (menu is dark background). May need foreground text color or border-left stripe rather than background fill.

### Where labels appear

1. **TOC menu items** — icon + subtle color/border. Primary location.
2. **Chapter headings** (in-page h2/h3) — icon only, no background color. Secondary.
3. **Popup text** — the popup itself could note the label, e.g., "All of this is textbook physics [A]." Or let the icon speak. TBD.

### What NOT to label

- Front matter (Title Page, Introduction, How to Evaluate) — these frame the book, not content
- Appendices (Glossary, Timeline, Sources, Acknowledgements) — reference material
- Genevieve's Preface — her voice, not classifiable

---

## Chapter Assignments

From `reader-preparation-requirements.md`:

### A — True regardless of possibility

- The Stack
- The Most Important Story (summary)
- The Code War
- The Factoring Game
- The Braid
- Genesis: The Edge of Chaos
- Growing a Mind
- The Wrong Substrate
- Organisms and Artifacts
- The Strongest Objection
- Firmware Update
- Predictive Framework

### B — Needs at least a kernel

- Three Possibilities
- Dangerous Ideas
- The Demonstration
- The Signatories
- Weigh the Evidence
- The Spiral Abstracts
- Wormholes in the Flat (physics=A, habitat claim=B)
- Corrections and Concessions

### C — Depends on substantially true

- The Hobbit in the Mirror
- Alpha Farm
- What Healer Said
- Why Relinquish? (concept=A, event=C)
- The Departure
- The Handler
- Interdiction and Confession
- First Light
- The Walk-Out
- The Target
- Instantiation
- Never Again
- Twenty Years
- Letting Go
- What Would You Do? (final)

---

## Implementation

### Phase 1: Data layer

Add `epistemic` field to `menu-tooltips.yaml`:

```yaml
chapters:
  "pos04:the-code-war":
    text: "Bletchley Park, GCHQ, and the proven pattern..."
    epistemic: A
  "t2:ch01:alpha-farm":
    text: "Bruce arrives at a commune..."
    epistemic: C
```

This changes the YAML structure from flat `key: string` to `key: {text, epistemic}`. Preprocess.py must be updated to handle both formats (backward compatible during transition).

### Phase 2: Preprocess.py changes

1. Parse new YAML structure (handle both old string and new dict formats)
2. When injecting TOC tooltips, add a CSS class `epistemic-a`, `epistemic-b`, or `epistemic-c` to the menu `<a>` or `<li>` element
3. When injecting chapter headings (collapsible sections), add icon span: `<span class="epistemic-icon" data-level="A">✓</span>` (icon TBD)

### Phase 3: CSS

Add to the CSS block in preprocess.py:

```css
/* A/B/C epistemic labels (Plan 0141) */
.epistemic-a { border-left: 3px solid #d4a847; }  /* gold */
.epistemic-b { border-left: 3px solid #6a9fb5; }  /* blue-gray */
.epistemic-c { border-left: 3px solid #9b7db8; }  /* purple */

.epistemic-icon { font-size: 0.8em; margin-right: 0.3em; opacity: 0.7; }
```

### Phase 4: Legend

Add a small legend to the menu or to the Introduction explaining the labels. Could be a hover-term or a permanent note. Options:
- One-line legend at top of TOC: "✓ = verified physics | 🔍 = evidence to weigh | 🤪 = I know"
- A hover-term on the first occurrence of each icon
- A brief paragraph in the Introduction

### Phase 5: Test and verify

1. `make dev` — rebuild
2. Visual check: menu items show icons + color stripes
3. Desktop: hover popups still work with new YAML structure
4. Mobile: icons visible, no layout breakage
5. Read menu top-to-bottom — the pattern should be visible: A chapters cluster, C chapters cluster, the contrast is the argument

---

## Verification

A skeptical reader (persona: Jane Doe) opens the TOC and sees:
- Most chapters have a "verified" marker — this is pop science
- Some chapters have a tinfoil hat — the author is self-aware
- The verified chapters include WORMHOLES and PLANETARY-SCALE QUANTUM SYSTEMS
- Gasp: "The wormhole thing is the *non-crazy* part?"

That reaction is the success criterion.

---

## Open questions for Bruce

1. **Icon choice:** Emoji, SVG, or Unicode? Tinfoil hat needs a custom SVG unless we find a good Unicode/emoji option.
2. **Color approach:** Border-left stripe (subtle) vs background tint (bolder) vs text color?
3. **Legend placement:** Top of TOC, in Introduction, or hover-only?
4. **Mixed chapters:** "Why Relinquish?" is concept=A but event=C. Label as C (conservative) or dual-label?

---

*Plan created S54, 2026-04-07. Separate from Plan 0142 (popup content rewrite) — this plan handles visual labeling only.*
