# Plan 0225 — Visual Language Deployment

**Status:** PARTIALLY COMPLETE — Phases 0-1 shipped; phases 2-5 pending (verified S63 audit)
**Author:** Auditor (Argus S59)
**Priority:** High
**Scope:** `build/preprocess.py`, `build/reader.js`, `build/tech-collapse.yaml`, `manuscript/*.tex` (concept symbol spans only)
**Supersedes:** Plan 0220 (Visual Language System — design document, now incorporated here)
**Related plans:**
- **0219** — Collapsible tech sections (infrastructure, piloted with "But It's Hot")
- **0220** — Visual Language System (design doc — vision incorporated into this plan)
- **0222a/b/c** — Kauffman filmstrip (inline SVG pattern, parallel effort)
- **0224** — "One More Layer" rewrite + collapse visual polish (DONE — gold background + ✔ shipped)

---

## System Architecture — How Everything Connects

This plan deploys a **single unified visual language system** in six gated phases (Phase 0 through Phase 5). Every element shares:

1. **One CSS layer** — all visual cues are CSS-driven (backgrounds, borders, `::before`/`::after` pseudo-elements)
2. **One toggle mechanism** — master switch on `<body>` class, localStorage persistence, one nav-bar button
3. **One copy-paste immunity pattern** — CSS pseudo-elements + `aria-hidden="true"` spans (same as deep link anchors)
4. **One color vocabulary** — Gold (#d4a847) = A-content/verified science, Blue (#6a9fb5) = B-content/narrative, Purple (#9b7db8) = C-content/testimony
5. **One tooltip infrastructure** — event-delegated `data-hover` system (reader.js), no per-element wiring needed
6. **One info-symbol pattern** — ⓘ after titles/terms = "tap here for tooltip." Consistent on phone and desktop.

### Dependency Chain

```
Phase 0 (Tooltip Symbol Fix)
    ↓ fixes mobile chapter-open bug, establishes info-symbol pattern
Phase 1 (Collapse at Scale)
    ↓ teaches "gold = science" through 15 repetitions
Phase 2 (Toggle Infrastructure)
    ↓ safety valve — makes everything else safe to try
Phase 3 (Epistemic Body Tints)
    ↓ extends color vocabulary from navigation to reading
Phase 4 (BORDERLINE Sections)
    ↓ nuanced middle — open-by-default, closeable
Phase 5 (Concept Symbol Pilot)
    ↓ most experimental — only proceed if Phase 3 passed
```

**No phase starts until the previous gate passes.** This prevents Christmas-tree accumulation.

### What Connects to What

| Element | Introduced | Color | Icon | Functional | Togglable |
|---|---|---|---|---|---|
| Deep link anchors | Already exists | — | 🔗 (::after) | Copy-paste share link | No (always functional) |
| TOC epistemic borders | Already exists (Plan 0141) | Gold/Blue/Purple | — | Navigation | Yes (Phase 2) |
| Chapter info symbols | Phase 0 | — | ⓘ | Tooltip trigger (replaces title hover) | No (always functional) |
| Collapsed tech sections | Phase 1 (infra from Plan 0219) | Gold background | ✔ checkmark | Skip/expand | Yes (Phase 2) |
| Tech section tooltips | Phase 1 | — | ⓘ | p2 distillation | Always on |
| Epistemic body tints | Phase 3 | Gold/Blue/Purple | — | Epistemic signal | Yes (Phase 2) |
| Epistemic legend | Phase 3 | Gold/Blue/Purple | — | Color key for readers | Yes (Phase 2) |
| BORDERLINE sections | Phase 4 | Gold background (lighter) | — | Open-by-default, closeable | Yes (Phase 2) |
| Concept symbols | Phase 5 | — | ⬡ ⇌ | Memory anchors | Yes (Phase 2) |

### The Christmas Tree Guard

**Rule: No element ever carries more than 2 visual signals simultaneously.**

| Element | Signal 1 | Signal 2 | Never |
|---|---|---|---|
| Collapsed tech section | Gold background | ✔ checkmark | No concept symbols, no extra icons |
| Body section | Faint color tint | Left border | No icons, no symbols |
| Concept term | Symbol only | — | No color, no icon |
| TOC entry | Color border | Text | No icons, no symbols |
| Deep link anchor | 🔗 icon | — | No color, no extra decoration |

### Copy-Paste Immunity Inventory

All visual-language icons use the same pattern — CSS pseudo-elements that don't appear in clipboard text:

| Element | Implementation | Immune |
|---|---|---|
| Deep link 🔗 | `.share-anchor::after { content: "🔗" }` + `aria-hidden="true"` | ✓ |
| Tech section ✔ | `.tech-grade::after { content: '\2714' }` + `aria-hidden="true"` | ✓ |
| Info symbol ⓘ | `.info-tip::after { content: 'ⓘ' }` + `aria-hidden="true"` | ✓ |
| Concept symbols | `[data-concept]::before { content: '⬡' }` + `aria-hidden="true"` | ✓ |

### Toggle Design

One button in the nav bar. Label: **Visual** (text, not a symbol — ships in Phase 2 before concept symbols have meaning). Tooltip: "Visual cues on/off."

CSS implementation:
```css
body.visual-plain .tech-section { background: none; border-left-color: #ccc; }
body.visual-plain .tech-grade { display: none; }
body.visual-plain .epistemic-tint { background: none; }
body.visual-plain [data-concept]::before { content: none; }
body.visual-plain .epistemic-legend { display: none; }
```

Collapse mechanics (▸/▾) survive toggle — they're functional, not decorative.
Info symbols ⓘ survive toggle — they're functional, not decorative.
Tooltips survive toggle — they're informational, not decorative.
TOC epistemic borders survive toggle — they're structural navigation.
Deep link 🔗 anchors survive toggle — they're functional.

localStorage key: `relinquishment-visual-language` (values: `on`, `off`).

---

## Vision: What Each Reader Should See

### Jane (GA reader, phone)
Clean prose. No symbols in early chapters. She taps ⓘ next to chapter titles to get one-sentence descriptions. She hits collapsed gold boxes every few pages in science chapters. Each has ✔ and an ⓘ giving her a one-sentence takeaway. She skips 15 sections and loses nothing. By chapter 5, gold = physics = skip is automatic. Purple sections feel different — she pauses on bold claims. Around chapter 8, ⬡ appears near "the Flat." By chapter 12, ⬡ alone triggers recognition. If she finds it distracting: one button, all visual cues gone.

### Chen (physicist)
Gold boxes are his navigation. He expands every one. TOC gold stripes let him jump to science chapters. He ignores concept symbols. The visual system helps him navigate but never intrudes.

### Rachel (phone, 10-minute sessions)
Collapsed sections are lifesavers. She taps ⓘ, gets key facts, moves on. Concept symbols help across sessions — ⬡ reminds her "the Flat thing" when she picks up after 3 days.

### Amir (security/intelligence)
Purple stripes navigate him to Record chapters. Gold collapsed sections are correctly marked "not for him." Visual system is navigation infrastructure.

### Bruce's mom (boomer, phone)
Tapping chapter titles opens/closes them — exactly what she expects. The ⓘ is small, out of the way, there if she notices it. Nothing jumps out. Nothing confuses the basic navigation.

---

## What NOT To Do (Decided)

These were considered in Plan 0220 and explicitly killed during S59 annealing:

- **No ✎ or ✦ icons in prose.** ✔ works because it's paired with a functional element (collapse). ✎/✦ in body text would be decorative noise. Color tints carry epistemic status better.
- **No ⚙ gear icon.** ✔ already signals "technical content." Doubling the signal overloads the element.
- **No more than 2 concept symbols initially.** "Experiment" means start small. If ⬡ and ⇌ work, add more later.
- **No concept symbols in collapsed section titles.** Gold + ✔ + symbol = Christmas tree.
- **No paragraph-level epistemic marking.** Section-level tints only.
- **No hover-on-titles.** Tooltip on `<summary>` conflicts with expand/collapse on mobile. Use ⓘ info symbol instead.

---

## Phase 0: Tooltip Symbol Fix (Mobile Chapter Bug)

### Purpose
Fix a pre-existing bug: on mobile, tapping a chapter title shows a tooltip instead of expanding the chapter. The `<summary>` element carries both `data-hover-id` (tooltip) and native toggle (expand/collapse). These conflict. This phase establishes the info-symbol pattern that all later phases will use.

### The Bug (reader.js lines 1144-1162)

Current code splits the `<summary>` touch target: tap on h2/h3 text → tooltip (prevents toggle), tap on triangle → native toggle. In practice, the heading IS the tap target — users don't aim for the triangle. Result: chapters won't open on phones.

### 0a. Add info-symbol span to chapter summaries

In `preprocess.py`, after the `convert_summary_title()` function (line ~2162), modify: instead of putting `data-hover-id` on the `<summary>` element itself, strip it and inject an info-symbol span AFTER the heading text inside the summary:

```html
<summary>
  <h2 id="chapter-id">Chapter Title</h2>
  <span class="info-tip" data-hover-id="chapter-description-key" aria-hidden="true"></span>
</summary>
```

The `<summary>` loses `data-hover-id` and the `hover-nav` class. The `<span class="info-tip">` gets both.

CSS:
```css
.info-tip { cursor: help; display: inline-block; vertical-align: middle; }
.info-tip::after {
  content: 'ⓘ';
  font-size: 0.7em;
  opacity: 0.4;
  margin-left: 0.3em;
  color: #888;
}
.info-tip:hover::after { opacity: 0.8; }
```

Dark mode: `color: #aaa;`

### 0b. Simplify reader.js touch handling

The split-target logic (lines 1144-1162) is no longer needed. With `data-hover-id` on the info-symbol span (not the summary), the event delegation handles it naturally:
- Tap chapter title → no `data-hover` on summary → falls through → native toggle fires
- Tap ⓘ → `data-hover-id` found → tooltip shows

Remove or simplify the `hover-nav` special-case block. The `info-tip` span is a normal hover target — no special touch handling needed.

### 0c. Apply to tech section summaries too

The `.tech-grade` span already serves this purpose for collapsed tech sections. Rename consideration: keep `.tech-grade` for ✔ checkmark, add `.info-tip` for ⓘ after the title. OR: combine — `.tech-grade` gets both ✔ and ⓘ. Decision: keep them separate. ✔ = "verified science" (togglable). ⓘ = "tap for details" (always functional).

Tech section summary line becomes:
```html
<summary>
  <span class="tech-title" ...>Section Title</span>
  <span class="tech-grade" aria-hidden="true"></span>
  <span class="info-tip" data-hover="[tooltip text]" aria-hidden="true"></span>
</summary>
```

### 0d. Print CSS

```css
@media print { .info-tip { display: none; } }
```

### Gate: Bruce phone-test

1. Can you open/close chapters by tapping the title? (YES = fixed)
2. Can you tap ⓘ to see a tooltip? (YES = working)
3. Does the ⓘ feel unobtrusive? (Too big/bright = adjust)
4. Desktop: does mouseover on ⓘ show tooltip? Does click on title still toggle?

**If gate fails:** Adjust symbol size/opacity. The interaction model (separate targets) is correct — only the visual presentation needs tuning.

**Connection to later phases:** This info-symbol pattern is reused in Phase 1 (tech section tooltips), Phase 4 (BORDERLINE tooltips), and potentially Phase 5 (concept symbol info). Establishing it first means all later phases inherit a tested pattern.

---

## Phase 1: Collapse at Scale

### Purpose
Deploy all 15 GA-AVERSE sections with gold background + ✔ + p2 tooltips via ⓘ. This is the foundation — it teaches "gold = science" through repeated exposure across the book.

### 1a. Write 14 remaining tooltips

Each tooltip is a p2 (12th-grade reading level) distillation of the technical section. One to two sentences. Format: what the section proves or explains, in language Jane can absorb from the collapsed state.

The `conclusion` field in tech-collapse.yaml already has draft conclusions for all 14 (written during Plan 0219 survey). Review each for:
- Jane-accessible language (no jargon)
- Accuracy (does it correctly represent the section?)
- Completeness (does it give Jane the key fact she needs?)

Update `tooltip` and `status` fields in tech-collapse.yaml.

### 1b. Verify section labels

Each entry in tech-collapse.yaml has `spine_label` and `bridge_label` fields. The `collapse_tech_sections()` function in preprocess.py uses these to find sections in the built HTML. Verify all 14 labels exist in the HTML output:

```bash
for label in $(grep spine_label tech-collapse.yaml | awk '{print $2}' | tr -d '"'); do
  grep -c "$label" docs/downloads/Relinquishment.html
done
```

Fix any missing labels in the .tex source.

### 1c. Deploy

Set all 14 entries to `status: approved` in tech-collapse.yaml. Build. Verify all 15 sections are collapsed in the HTML output.

### 1d. Verify build + print CSS

- `make clean && make` — zero errors
- Deep-link verifier passes
- Count collapsed sections in HTML (expect 15)
- Spot-check: expand 3 sections, verify content renders inside gold container
- Check dark mode
- **Print CSS:** `details.tech-section { background: none !important; }` — no gold boxes in print. Verify sections expanded, no icons.

### Gate: Bruce phone-review

Bruce reviews all 15 collapsed sections on his phone. Questions:
1. Are the tooltips accurate and useful? (Tap ⓘ to see each one)
2. Does the repetition of gold boxes feel natural or cluttered?
3. Any sections that should NOT be collapsed?
4. Any BORDERLINE sections (Phase 4) that should be added to this batch?

**If gate fails:** Adjust tooltips, remove problematic sections. Re-test. Do not proceed to Phase 2 until this is stable.

---

## Phase 2: Toggle Infrastructure

### Purpose
Add the safety valve. Without this, adding more visual elements risks trapping readers who find them distracting.

### 2a. Toggle button in nav bar

Add a small button to the existing nav/menu area:
- Default state: visual language ON
- Button label: **Visual** (plain text — no symbol; ⬡ has no meaning until Phase 5)
- Tooltip: "Visual cues on/off"
- `aria-label="Toggle visual language cues"`

### 2b. CSS class system

All togglable elements respect `body.visual-plain`:
```css
body.visual-plain .tech-section { background: none !important; border-left-color: #ccc; }
body.visual-plain .tech-grade { display: none; }
body.visual-plain .epistemic-tint { background: none !important; }
body.visual-plain [data-concept]::before { content: none; }
```

**Gold-on-gold guard:** Tech sections override ambient chapter tints:
```css
details.tech-section { background: linear-gradient(135deg, #faf6e8, #f5f0dc) !important; }
```
(Already present from Plan 0224. The `!important` ensures it wins over any future `.chapter-tint-a` parent.)

### 2c. localStorage persistence

```javascript
var vlState = localStorage.getItem('relinquishment-visual-language') || 'on';
if (vlState === 'off') document.body.classList.add('visual-plain');

toggleBtn.addEventListener('click', function() {
  document.body.classList.toggle('visual-plain');
  var state = document.body.classList.contains('visual-plain') ? 'off' : 'on';
  localStorage.setItem('relinquishment-visual-language', state);
});
```

### 2d. Print CSS

```css
@media print {
  .toggle-visual { display: none; }
}
```

### Gate: Toggle verification

- Toggle off: gold backgrounds disappear, ✔ disappears, collapse ▸/▾ survives, ⓘ info symbols survive, tooltips survive
- Toggle on: everything returns
- Reload page: state persists
- Phone test: button is tappable, not too small

---

## Phase 3: Epistemic Body Tints

### Purpose
Extend the color vocabulary from navigation (TOC borders) to reading (body sections). The reader learns to associate colors with trust levels without explicit instruction.

### 3a. Design

Very faint background washes at the **chapter level**, not section or paragraph:
```css
.chapter-tint-a { background: rgba(212, 168, 71, 0.06); }  /* barely-there gold — start at 0.06, not 0.04 */
.chapter-tint-b { background: rgba(106, 159, 181, 0.06); }  /* barely-there blue */
.chapter-tint-c { background: rgba(155, 125, 184, 0.06); }  /* barely-there purple */
```

Dark mode: same hues, adjusted opacity.

**Starting at 0.06 not 0.04:** Cheap phone screens and TN panels can't render opacity 0.04. Start higher — there's room to reduce if it's too strong, but there's no room to increase if Bruce can't see it.

These tints are applied to `<details class="chapter-section">` elements that already have `epistemic-a/b/c` classes.

**Gold-on-gold nesting:** Collapsed tech sections inside gold-tinted A-chapters get their own stronger gradient (Plan 0224 CSS). The `!important` on `details.tech-section` background ensures the gold box is always visible against the ambient tint.

### 3b. Epistemic legend

CSS for `.epistemic-legend` exists in preprocess.py but the HTML element is **never rendered**. Phase 3 must inject a small legend:

Location: bottom of the TOC area or top of body content, visible when all chapters are collapsed.

```html
<div class="epistemic-legend" aria-label="Color guide">
  <span class="legend-a">■</span> Published physics
  <span class="legend-b">■</span> Narrative
  <span class="legend-c">■</span> Testimony
</div>
```

CSS: small, understated, uses the same Gold/Blue/Purple colors. Togglable via `body.visual-plain .epistemic-legend { display: none; }` (already in toggle CSS).

### 3c. Pilot

Apply to ONE chapter that has adjacent A, B, and C content visible in the same reading session. Candidate: the TOC view itself (all chapters visible, all three colors present).

### 3d. Print CSS

```css
@media print {
  .chapter-tint-a, .chapter-tint-b, .chapter-tint-c { background: none !important; }
  .epistemic-legend { display: none; }
}
```

### Gate: Bruce phone-test

- Can you see the tints? (Too subtle = wasted. Too strong = garish.)
- Does the color difference between A/B/C chapters register subconsciously?
- Does it feel like information or decoration?
- Does the legend make the colors self-explanatory?
- Toggle off: tints + legend disappear cleanly?

**If gate fails:** Adjust opacity or kill this phase. Collapse system carries the mission alone. Concept symbols (Phase 5) can still proceed — they don't depend on body tints.

**Connection to Phase 1:** The gold tech-section backgrounds (Phase 1) are STRONGER than the body tints. This is intentional: the collapsed box is a deliberate signal ("this is for Chen"), while the body tint is ambient ("you're in A-territory"). Two levels of the same color vocabulary, different intensities.

---

## Phase 4: BORDERLINE Sections

### Purpose
Seven sections identified as "not full jargon but slightly technical" — the ones where Jane MIGHT benefit from reading them, and the collapse-with-tooltip gives her a hint.

### 4a. Evaluate each section

The 7 BORDERLINE candidates from tech-collapse.yaml:
1. Freedman's Independent Conception (1988)
2. Kitaev and the Russian Question
3. Non-Abelian Anyons: Operational Proof
4. The GCHQ Precedent
5. But What Is a Soliton?
6. From Emergence to Function
7. The Thread Continues

For each, decide:
- **Collapse (default closed):** Jargon-heavy enough to bury Jane. Treat like GA-AVERSE.
- **Open-by-default (closeable):** Worth Jane reading, but she should know she CAN close it.
- **Leave alone:** Not technical enough to warrant any treatment.

### 4b. Open-by-default variant

For sections marked "open-by-default":
```html
<details class="tech-section tech-borderline" open>
```

CSS:
```css
details.tech-borderline { background: rgba(212, 168, 71, 0.06); }  /* lighter gold than GA-AVERSE */
details.tech-borderline > summary .tech-grade::after { content: ''; }  /* no checkmark — not "safe to skip" */
```

The lighter gold + no checkmark signals: "this is slightly technical but we think you can handle it." The open state + close option signals: "if it's too much, close it."

**Mobile tap:** BORDERLINE summary lines get ⓘ info symbol for tooltip (same as Phase 0), NOT `data-hover` on the summary itself. Same interaction model everywhere.

### 4c. Print CSS

```css
@media print {
  details.tech-borderline { background: none !important; }
}
```

### Gate: Per-section decision

Bruce reviews each BORDERLINE section and decides its treatment. This is editorial judgment, not mechanical.

**Connection to Phase 1:** Same CSS infrastructure, same collapse mechanism. Phase 4 extends the vocabulary: full gold + ✔ = "skip confidently" vs. lighter gold + no ✔ = "try it, close if needed."

---

## Phase 5: Concept Symbol Pilot

### Purpose
Test whether readers can learn visual symbols through immersion (Lapine pedagogy). Start with TWO symbols only. If they work, expand later. If not, kill the idea.

### 5a. Symbol selection

| Symbol | Concept | Why this one |
|---|---|---|
| ⬡ (U+2B21) | The Flat / 2DEG | Hexagonal — evokes lattice geometry. The book's central substrate. |
| ⇌ (U+21CC) | Wormhole / nonlocal connection | Bidirectional arrows — evokes quantum teleportation's two-way channel. |

These are the book's two most important physics concepts. If readers can't learn these two, they won't learn any.

**Font rendering risk:** U+2B21 has poor coverage on Android system fonts, older iOS, cheap Kindles. May show as □. **Mitigation:** Declare a font-stack with fallback, or use inline SVG for concept symbols instead of Unicode characters. Test on Bruce's actual phone before gate. If □ appears, switch to SVG — same `::before` injection, `content: url(data:image/svg+xml,...)` instead of character.

### 5b. Lapine deployment plan

**Introduction phase (chapters 1-5):** Symbol appears WITH the word, every time. Reader doesn't need the symbol.

In .tex files, add `\concept{flat}` or `\concept{wormhole}` macros. In preprocess.py, convert to:
```html
<span data-concept="flat" aria-hidden="true"></span>the Flat
```

CSS:
```css
[data-concept="flat"]::before { content: '⬡ '; font-size: 0.8em; opacity: 0.5; }
[data-concept="wormhole"]::before { content: '⇌ '; font-size: 0.8em; opacity: 0.5; }
```

Low opacity in early chapters. The symbol is present but quiet.

**Reinforcement phase (chapters 6-10):** Symbol appears near the concept but not always adjacent. Opacity increases to 0.7.

**Fluency phase (chapters 11+):** Symbol can appear alone (in section markers, margin cues). Full opacity.

Implementation: `data-concept-phase="intro|reinforce|fluent"` attribute, CSS adjusts opacity per phase.

**Screenreader note:** In intro/reinforce phases, `aria-hidden="true"` is correct (symbol is decorative, word is adjacent). In fluent phase where symbol appears WITHOUT the word, switch to `aria-label="the Flat"` so screenreaders announce the concept.

### 5c. Placement

Not every mention gets a symbol. Rule: **first mention per chapter** gets the symbol. Subsequent mentions in the same chapter are plain text. Same dedup logic as the hover system (Plan 0213).

Per-chapter dedup prevents symbol fatigue within a single reading session.

**Pipeline ordering:** Concept symbol injection must run AFTER `collapse_tech_sections()`. A symbol inside a collapsed section title would violate the Christmas Tree Guard (gold + ✔ + symbol). Safety rule: `details.tech-section summary [data-concept]::before { content: none; }` — kills any symbol that leaks into a collapsed title.

### 5d. Print CSS

```css
@media print {
  [data-concept]::before { content: none; }
}
```

### Gate: Bruce tests with someone

Bruce describes the Flat and wormholes to someone while showing them a chapter with symbols. Does the person pick up the symbol-concept association without being told? If yes: expand to 2-3 more symbols. If no: kill Phase 5 entirely.

**Connection to Phases 1-3:** Concept symbols are the LIGHTEST visual element. They only work because the heavier elements (gold backgrounds, color tints) have already trained the reader to attend to visual cues. Without the foundation, symbols are invisible marks. With it, they're the capstone of a graduated system.

**Connection to toggle:** `body.visual-plain [data-concept]::before { content: none; }` — one line kills all symbols.

---

## Acceptance Criteria (Full System)

1. All 15 GA-AVERSE sections collapsed with gold + ✔ + ⓘ tooltip
2. Chapter titles open/close on phone tap (no tooltip conflict)
3. ⓘ info symbols provide tooltips on tap (phone) and hover (desktop)
4. Toggle button works: visual cues on/off, state persists across reloads
5. No element carries more than 2 visual signals
6. All visual elements are copy-paste immune
7. Print CSS: all sections expanded, no icons, no tints, no symbols, no toggle button, no legend
8. Dark mode: all elements have dark variants
9. HTML builds clean, deep-link verifier passes
10. Bruce phone-test passes at each gate
11. Gold tech-section backgrounds visible against any ambient chapter tint (gold-on-gold guard)

## Eigenvalue Assessment (Full System)

| Persona | Before | After | Δ |
|---|---|---|---|
| Jane | Hits walls in 30% of book | Skips or absorbs via ⓘ tooltip; symbols aid memory | +strong |
| Chen | Scans for physics manually | Gold boxes mark physics; TOC stripes navigate | +positive |
| Rachel | Gets stuck, loses place between sessions | ⓘ tooltips, concept symbols as memory anchors | +strong |
| Arjun | Fine without it | Cleaner epistemic marking validates rigor | +slight |
| Yusuf | Fine without it | Color vocabulary aids fact-checking | +slight |
| Doctorow | Fine without it | Neutral | Neutral |
| Reeves | Fine without it | Epistemic color = his language | +positive |
| Pastor Mike | Struggles with jargon | Collapse + ⓘ tooltips help | +positive |
| Amir | Navigates by memory | Purple stripes navigate to Record | +positive |
| Bruce's mom | Can't open chapters (BUG) | Tap title = open, tap ⓘ = info | **+critical fix** |

**F-mode:** F-crank reduced (engineering discipline visible). F-scifi neutral. No regressions.
**C-violation:** N/A — infrastructure only, no prose changes (except concept symbol spans).

---

## Anneal Results (S59 Failure Mode Analysis)

13 gotchas identified. Mitigations incorporated into phase specs above.

### Critical (mitigated in plan)
1. **Epistemic legend missing from HTML** — CSS exists, HTML doesn't. → Added to Phase 3b.
2. **Gold-on-gold nesting** — tech section inside gold-tinted chapter. → `!important` guard in Phase 2b.
3. **Unicode ⬡ rendering** — poor font coverage on Android/Kindle. → Font-stack or SVG fallback in Phase 5a.
4. **Pipeline ordering** — concept symbols inside collapsed titles = Christmas tree. → Safety CSS rule in Phase 5c.

### Moderate (mitigated in plan)
5. **BORDERLINE tap conflict** — summary with tooltip AND toggle. → ⓘ pattern from Phase 0 in Phase 4b.
6. **Opacity 0.04 invisible on cheap screens** — too subtle. → Start at 0.06 in Phase 3a.
7. **Toggle button ⬡ meaningless before Phase 5** — symbol has no meaning yet. → Changed to text "Visual" in Phase 2a.
8. **Print CSS accumulation** — each phase adds print rules. → Print CSS section added to every phase.

### Low (documented, no action needed)
9. **Deep link 🔗 outside visual language** — now documented in "What Connects to What" table.
10. **localStorage collision** — single-book deployment, low risk.
11. **Concept symbol dedup vs hover dedup** — separate systems, document coupling.
12. **Screenreader fluent-phase symbols** — `aria-label` needed when symbol appears alone. → Added to Phase 5b.
13. **Toggle default for first visitors** — ON is correct (gold boxes are Phase 1's teaching mechanism; OFF hides the lesson).

---

## Risks

- **Christmas tree** — guarded by 2-signal-max rule + gated phases + toggle + pipeline ordering
- **Mobile chapter bug (Phase 0)** — pre-existing, currently blocking phone readers. Highest priority.
- **Phase 3 too subtle** — if nobody notices the tints, it's wasted work (but harmless). Starting at 0.06 gives room.
- **Phase 5 doesn't land** — expected possible outcome. Kill it cleanly. No dependencies on it.
- **Tooltip quality** — Phase 1's 14 tooltips are the highest-effort item. Each requires reading and distilling a technical section to p2. Auditor work, not mechanical.
- **Build regression** — preprocess.py gets more post-processing steps. Each must be idempotent and order-independent. Concept symbols must inject AFTER collapse.
- **Font rendering** — ⬡ may be □ on some devices. Phase 5 gate catches this. SVG fallback ready.
