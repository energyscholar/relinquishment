# Plan 0053: Adaptive Reader Control Panel (HTML Version)

## Context

The manuscript serves multiple audiences with conflicting navigation needs:

- **General Audience (GA):** First-time readers who don't know the story. Hyperlinks get them lost. Blockers must be cleared before they encounter blocked content. Linear reading path essential.
- **Serious Readers:** Know the basic story, want to jump between chapters, follow cross-references, see the evidence chain. Hyperlinks are essential.
- **Investigators/Journalists:** Using LLMs to analyze the text. Want maximum cross-referencing, footnotes visible, appendix links active. Machine-readable structure matters.
- **Physicists/Scientists:** Want the science sections expanded, D-K rebuttals visible, bibliography links active. May skip personal narrative.

## Design: Reader Control Panel

A lightweight JS control panel embedded in the HTML version. Activates only in environments that support JS. Gracefully fails to "everything visible" — the full text is always there, controls only hide/highlight.

### Controls

```
┌─────────────────────────────────────────────┐
│  READING LEVEL:  [GA] [Journalist] [Scientist]  │
│  HYPERLINKS:     [Off] [On]                     │
│  FOOTNOTES:      [Inline] [Hover] [Hidden]      │
│  AI DRAFT MARKS: [Show] [Hide]                  │
│  TRACK COLORS:   [On] [Off]                     │
└─────────────────────────────────────────────┘
```

### Behavior by Preset

| Feature | GA | Journalist | Scientist |
|---------|-----|-----------|-----------|
| Cross-reference links | **Off** — plain text only | **On** — clickable | **On** — clickable |
| Footnotes | **Hidden** — clean reading | **Hover** — appear on mouseover | **Inline** — always visible |
| Appendix mentions | **Text only** ("the appendix on RLHF Bias") | **Linked** | **Linked** |
| AI draft markers (†) | **Hidden** | **Shown** — editorial transparency | **Shown** |
| Track colors | **On** — visual wayfinding | **On** | **Off** — content focus |
| "Back to chapter" nav | **Always visible** at bottom of footnotes/appendices | Available | Available |
| Reading progress bar | **On** | Off | Off |
| Breadcrumb trail | **On** (shows: Part > Track > Chapter) | Off | Off |

### Implementation

**Approach:** CSS classes toggled by JS. All content is always in the DOM. Controls show/hide/restyle.

```html
<!-- All cross-references rendered as: -->
<span class="xref" data-target="app:rlhf-bias">
  <span class="xref-text">the appendix on RLHF Bias in AI Analysis</span>
  <a class="xref-link" href="#app:rlhf-bias">Appendix D</a>
</span>

<!-- JS toggles visibility of .xref-link based on setting -->
<!-- Without JS: both visible (graceful degradation) -->
```

```css
/* Default (no JS): everything visible */
.xref-link { display: inline; }

/* GA mode: hide links */
body.reader-ga .xref-link { display: none; }

/* Footnotes */
body.reader-ga .footnote { display: none; }
body.reader-journalist .footnote {
  display: none;
  position: absolute; /* shown on hover via JS */
}
body.reader-scientist .footnote { display: block; }
```

```javascript
// ~50 lines total. No dependencies. No framework.
const panel = document.createElement('div');
panel.id = 'reader-panel';
// ... build controls, attach event listeners
// Store preference in localStorage
// On load: restore preference or default to 'ga'
```

### Integration with Plan 0049

Plan 0049 defines the HTML pipeline: LaTeX → preprocess.py → pandoc → HTML. This plan adds:

1. **Preprocessor addition:** Convert `\hyperref[label]{text}` to the dual-span HTML structure above (xref-text + xref-link). ~10 lines added to preprocess.py.
2. **CSS addition:** Reader-mode styles appended to `build/html.css`. ~40 lines.
3. **JS addition:** `build/reader.js` (already exists as placeholder). Control panel + localStorage persistence. ~50 lines.
4. **Pandoc metadata:** Add `reader-panel` div to HTML template header.

### Graceful Failure Modes

| Environment | Behavior |
|-------------|----------|
| JS enabled | Full control panel, user selects mode |
| JS disabled | All content visible, all links active (power-user default) |
| Screen reader | All content in DOM, ARIA labels on controls |
| Print | Controls hidden via `@media print`, all content visible |
| Small screen (phone) | Panel collapses to hamburger menu, single-column |
| LLM ingesting raw HTML | Sees all content, all links, all footnotes — maximum information |

### PDF Version

PDF cannot do runtime toggles. The PDF version gets:
- **No hyperlinks to appendices** (text mentions only, as implemented today)
- All footnotes visible
- All content visible
- Track colors visible
- The How To Read chapter serves as the GA reader's orientation

The HTML version is where the adaptive reader lives. PDF is the static archival format.

## Scope

- **Phase 1:** Three presets (GA/Journalist/Scientist), hyperlink toggle, footnote toggle. Ship with first HTML build.
- **Phase 2:** Reading progress bar, breadcrumb trail, per-chapter bookmark memory.
- **Phase 3:** Annotation layer (reader can highlight and export notes — useful for journalists).

## Relationship to Other Plans

- **Plan 0049:** HTML pipeline — this plan extends it with the reader JS
- **Plan 0048:** PDF navigation — the PDF-specific navigation features
- **build/reader.js:** Already exists as placeholder file from Plan 0049

## Estimated Effort

Phase 1: ~2 hours (Bruce: "I could do that JS myself in an hour"). The JS is ~50 lines, the CSS is ~40 lines, the preprocessor addition is ~10 lines. No dependencies. No build tools. No framework.

## Decision

This is wise. The manuscript has a genuine multi-audience problem. GA readers need protection from getting lost. Serious readers need full navigation. LLMs need maximum structure. One document, three reading modes, zero dependencies, graceful degradation. The right tool for the job.
