# Plan 0148: Deep Link Anchors + Mobile Menu Tooltips

**Status:** DONE (implemented prior to 2026-04-10; confirmed by Generator B)
**Created:** 2026-04-09
**Annealed:** 2026-04-09 (medium + low, settled; Phase 2b added)
**Auditor:** Argus

---

## Context

Deep links to specific passages are the book's primary viral marketing tool. Someone in a social media argument copies a link that lands the reader at the EXACT paragraph answering their question. Two use cases:

1. **Deliberate sharer** — knows the book, copies a link to settle an argument
2. **Spontaneous sharer** — reading right now, hits something shareable, sends it to a friend

**URL pattern:** `relinquishment.ai/relinquishment.html#dl:stack-chart`
(Construction URL uses uppercase `Relinquishment.html` — rename is a Day 1 task, not this plan.)

---

## Architecture

### Placement: LaTeX markers in source files

Anchors live in the .tex source, not in a grep manifest. This means they survive editing — moving a paragraph moves its anchor, deleting a paragraph deletes its anchor.

```latex
\deeplink{stack-chart}The last technology on this list has one property none of the others have...
```

**Placement rule:** `\deeplink{id}` must be placed INLINE at the start of paragraph text (no blank line between macro and text). If placed on its own line, pandoc treats it as a block and wraps it in `<div>` instead of `<span>`. Both are handled in preprocess.py (see Phase 1), but inline placement is preferred — it keeps the anchor co-located with its paragraph in the HTML.

In PDF: renders as `\hypertarget{dl:stack-chart}{}` (invisible, enables PDF deep links too).
In HTML: pandoc passes it through; preprocess.py converts to:

```html
<span class="share-anchor" id="dl:stack-chart" aria-hidden="true"></span>
```

### Metadata manifest

`build/deep-links.yaml` — questions and categories only. No placement instructions (placement is in .tex files). Used to generate the Questions index and for editorial reference.

```yaml
- id: stack-chart
  question: "What is the technology stack?"
  category: curiosity
```

### Anchor HTML element

```html
<span class="share-anchor" id="dl:stack-chart" aria-hidden="true"></span>
```

- Empty `<span>` — zero text content
- Visual indicator entirely via CSS `::after` pseudo-element
- **Pseudo-elements are never included in clipboard** — zero copy-paste contamination
- `aria-hidden="true"` — invisible to screen readers
- `dl:` prefix avoids collision with existing `spine:`, `record:`, `ch:`, `app:` ID patterns

### CSS

```css
/* Deep link anchors — Plan 0148 */
.share-anchor { position: relative; display: inline; }
.share-anchor::after {
  content: "🔗";
  font-size: 0.6em;
  opacity: 0;
  cursor: pointer;
  user-select: none;
  margin-left: 0.3em;
  padding: 8px;           /* mobile tap target */
  transition: opacity 0.2s;
}
body.show-anchors .share-anchor::after { opacity: 0.3; }
body.show-anchors .share-anchor:hover::after { opacity: 0.8; }
@media print { .share-anchor::after { content: none; } }
@media (prefers-color-scheme: dark) {
  body.show-anchors .share-anchor::after { opacity: 0.25; }
  body.show-anchors .share-anchor:hover::after { opacity: 0.7; }
}
```

**Note:** `padding` on `::after` is merged into the base rule to avoid the duplicate selector bug in the previous draft.

### Toggle button (reader.js, bottom bar)

Small 🔗 button added to the bottom bar alongside the existing `§` share and PDF buttons. Click toggles `body.show-anchors` class. State persisted in localStorage.

### Click-to-copy (reader.js)

Use the existing `copyToClipboard()` utility (already in reader.js — clipboard with execCommand fallback). Do not call `navigator.clipboard` directly.

```javascript
document.addEventListener('click', function(e) {
  if (!document.body.classList.contains('show-anchors')) return; // invisible = unclickable
  var anchor = e.target.closest('.share-anchor');
  if (!anchor) return;
  e.stopPropagation();
  var url = window.location.origin + window.location.pathname + '#' + anchor.id;
  copyToClipboard(url, function() {
    showDeepLinkToast('Link copied');
  });
});
```

The `show-anchors` guard prevents accidental copies when anchors are toggled off (they remain in the DOM with opacity 0).

### Toast notification

Named `showDeepLinkToast` to avoid any future collision. Small overlay, bottom-center, fades after 1.5 s. Example:

```javascript
function showDeepLinkToast(msg) {
  var t = document.createElement('div');
  t.textContent = msg;
  t.style.cssText = 'position:fixed;bottom:3.5em;left:50%;transform:translateX(-50%);' +
    'background:rgba(0,0,0,0.7);color:#fff;padding:0.4em 1em;border-radius:4px;' +
    'font-size:0.85em;z-index:200;pointer-events:none;';
  document.body.appendChild(t);
  setTimeout(function() { document.body.removeChild(t); }, 1500);
}
```

### Auto-expand on arrival

Existing deep-link JS in reader.js already opens parent `<details>` elements and scrolls to any `#id` target. The `autoExpand()` function handles colon IDs correctly (querySelector throws SyntaxError on unescaped colons; the code falls back to `getElementById`). No new navigation code needed.

---

## Phased Implementation

### Phase 1: LaTeX macro + preprocess.py support (~20 min Generator)

1. Add `\deeplink` macro to `build/preamble.tex`:
   ```latex
   \newcommand{\deeplink}[1]{\hypertarget{dl:#1}{}}
   ```

2. In `preprocess.py` `fix_html_toc()`, convert pandoc's hypertarget output into share-anchor spans. Add before the final `html_path.write_text(text)` call:

   ```python
   # Convert deep-link hypertargets (Plan 0148)
   # Pandoc outputs <div id="dl:*">...</div> when the macro is on its own line (block context),
   # and <span id="dl:*"></span> when inline. Handle both.
   import re as re_mod
   dl_div = re_mod.compile(r'<div id="(dl:[^"]+)">\s*</div>', re_mod.DOTALL)
   dl_span = re_mod.compile(r'<(?:span|a) id="(dl:[^"]+)"></(?:span|a)>')
   replacement = lambda m: f'<span class="share-anchor" id="{m.group(1)}" aria-hidden="true"></span>'
   before = text.count('id="dl:')
   text = dl_div.sub(replacement, text)
   text = dl_span.sub(replacement, text)
   after = text.count('class="share-anchor"')
   print(f"Deep links: {after} share anchors converted (from {before} hypertargets)")
   ```

   **Note:** `re` is already imported at module level in preprocess.py — remove the `import re as re_mod` line and use the module-level `re` directly.

3. Add CSS from the Architecture section to `collapse_css`.

**Acceptance:**
- `\deeplink{test}` placed inline in any .tex file → `<span class="share-anchor" id="dl:test" aria-hidden="true">` in HTML output
- `\deeplink{test}` on its own line in any .tex file → same `<span class="share-anchor" ...>` output (div form converted)
- Same `\deeplink{test}` → `\hypertarget{dl:test}{}` in PDF (invisible target)
- Anchor is invisible in both PDF and HTML default view
- Copy-pasting a paragraph containing an anchor produces clean text (no emoji, no artifact)

### Phase 2: Toggle + click-to-copy (reader.js, ~20 min Generator)

1. Add `showDeepLinkToast()` function (see Architecture above)
2. Add 🔗 toggle button to the bottom bar, after the existing `§` share button and before (or after) the PDF button
3. Add click handler for `.share-anchor` with `show-anchors` guard (see Architecture above)
4. localStorage key: `relinquishment-deep-link-toggle`

```javascript
// Restore toggle state
try {
  if (localStorage.getItem('relinquishment-deep-link-toggle') === '1') {
    document.body.classList.add('show-anchors');
    deepLinkBtn.textContent = '🔗'; // already set, but mark active state if desired
  }
} catch(e) {}
```

**Acceptance:**
- Toggle button visible in bottom bar
- Click toggle → anchors appear/disappear (opacity transition)
- Click anchor while visible → correct full URL (origin + pathname + `#dl:id`) in clipboard
- Click anchor while invisible (toggle off) → nothing happens
- Toast appears and fades after ~1.5 s
- Reload preserves toggle state

### Phase 2b: Mobile menu tooltips via click-target split (reader.js, ~15 min Generator)

On mobile, tapping a chapter title should show its tooltip popup — not toggle the accordion. The triangle remains the expand/collapse control.

**How it works:** Chapter summaries have structure `<summary class="hover-nav" data-hover="..."><h2>Title</h2></summary>`. The `<h2>` is a distinct element inside the summary. If the tap lands on the `<h2>` (the text), show the tooltip. If the tap lands outside the `<h2>` (the triangle/marker area), let native `<details>` toggle happen.

**Changes to touchend handler** (reader.js ~line 1082):

Replace the current `hover-nav` pass-through:
```javascript
// OLD: if (term.classList.contains('hover-nav')) return;
```

With a click-target split:
```javascript
if (term.classList.contains('hover-nav')) {
  // Summary elements: split tap target — heading text = tooltip, triangle = toggle
  var heading = e.target.closest('h2, h3');
  if (heading && term.contains(heading)) {
    // Tap was on the chapter title text — show tooltip, prevent toggle
    e.preventDefault();
    var existingPanel = document.querySelector('.hover-panel');
    if (existingPanel && term.getAttribute('aria-describedby') === existingPanel.id) {
      dismissPanel();
    } else {
      showPanel(term);
    }
  }
  // Tap on triangle/marker area: fall through, native toggle happens
  return;
}
```

**CSS: dotted underline on chapter titles (mobile hint):**
```css
/* Mobile: hint that chapter titles are tappable for tooltip */
@media (hover: none) {
  details.chapter-section > summary.hover-nav > h2,
  details.chapter-section > summary.hover-nav > h3 {
    text-decoration: underline dotted;
    text-decoration-color: rgba(0,0,0,0.25);
    text-underline-offset: 3px;
  }
}
@media (hover: none) and (prefers-color-scheme: dark) {
  details.chapter-section > summary.hover-nav > h2,
  details.chapter-section > summary.hover-nav > h3 {
    text-decoration-color: rgba(255,255,255,0.2);
  }
}
```

The `@media (hover: none)` targets touch devices only — desktop users who have mouse hover don't see the underline (they don't need it).

**Acceptance:**
- On mobile/touch: tap chapter title → tooltip popup appears, accordion does NOT toggle
- On mobile/touch: tap triangle → accordion toggles, no tooltip
- On mobile/touch: tap outside → tooltip dismisses
- On desktop: no change to existing hover behavior
- Dotted underline visible on touch devices, invisible on desktop
- Part-section summaries (Introduction, The Flat, etc.) also work — they have `<h2>` children too

### Phase 3: Place markers in manuscript (~30 min Generator)

Place `\deeplink{id}` inline at the start of each target paragraph listed in the manifest below (~43 markers). "Inline" means: `\deeplink{id}Text of paragraph...` with no blank line between macro and text.

**Only modify files in the build path.** Check `build/epub-tmp/main.tex` for the definitive list. The source files live in `manuscript/` (not `build/epub-tmp/manuscript/`). All 43 manifest entries reference files that are confirmed in the build path.

**Acceptance:**
- `grep -rc '\\deeplink' manuscript/spine/ manuscript/record/ manuscript/00-front/ manuscript/appendix/ manuscript/99-back/` shows ~43 markers
- `make html` builds clean with no warnings
- `grep -c 'class="share-anchor"' docs/downloads/Relinquishment.html` matches marker count

### Phase 4: Create metadata manifest (~10 min Generator)

Write `build/deep-links.yaml` with question/category for each placed anchor. Reference-only for now; a future plan may use it to generate a Questions index.

### Phase 5: Verification (~15 min Auditor)

**Deep link anchors:**
1. Select all text in a chapter with anchors → paste → no emoji or artifacts
2. Click 5 random anchors (toggle on) → verify correct URL in clipboard
3. Navigate to 5 `#dl:*` URLs from address bar → correct chapter opens, scrolls to passage
4. Click an anchor with toggle OFF → nothing happens, no toast
5. Dark mode: anchors visible at reduced opacity when toggled on
6. Print preview: no anchors visible
7. PDF: `\hypertarget` targets exist (test with `#dl:stack-chart` in PDF viewer)

**Mobile menu tooltips (Phase 2b):**
8. Mobile (375px): tap chapter title text → tooltip popup, accordion does NOT toggle
9. Mobile: tap triangle area → accordion toggles, no tooltip
10. Mobile: dotted underline visible on chapter titles
11. Desktop: no dotted underline, hover behavior unchanged
12. Part-section summaries work the same way (tap text = tooltip, tap triangle = toggle)

---

## Deep Link Manifest

43 entries across 6 categories. The `passage:` field documents where to place the `\deeplink{}` marker. It is NOT a runtime grep target. All files listed are confirmed in `build/epub-tmp/main.tex`.

### Skeptic challenges (10)

```yaml
- id: three-possibilities
  question: "What are you actually claiming is true?"
  category: skeptic
  passage: spine/three-possibilities.tex — "After years of research, pressure-testing, and reconstruction we cannot definitively distinguish"

- id: authors-position
  question: "Does the author actually believe this?"
  category: skeptic
  passage: spine/three-possibilities.tex — "I'm fine with all three of those and can't tell which one is closest to true"

- id: story-may-be-false
  question: "Is the Flat a real thing even if the story is fiction?"
  category: skeptic
  passage: spine/three-possibilities.tex — "The story may be false. The Flat is real."

- id: preparation-not-disclosure
  question: "Is this book a disclosure or a warning about what's coming?"
  category: skeptic
  passage: spine/three-possibilities.tex — "This book is not a disclosure. It is preparation."

- id: ten-thousand-kept-it
  question: "Could a secret that big really be kept?"
  category: skeptic
  passage: spine/the-code-war.tex — "Ten thousand people. More than thirty years."

- id: absence-not-evidence
  question: "If this happened, why is there no evidence?"
  category: skeptic
  passage: spine/weigh-the-evidence.tex — "Absence of evidence is not evidence of absence."

- id: silence-is-structural
  question: "Doesn't the absence of papers mean it's been studied and ruled out?"
  category: skeptic
  passage: spine/the-silence-gap.tex — "No one has published a paper saying 'life cannot arise in a 2DEG.'"

- id: not-aliens
  question: "Are you claiming alien life?"
  category: skeptic
  passage: spine/the-wrong-substrate.tex — "It is not extraterrestrial life. It is terrestrial life that lives in space."

- id: hobbit-in-mirror
  question: "Doesn't the author realize how much this sounds like Lord of the Rings?"
  category: skeptic
  passage: spine/the-strongest-objection.tex — "The structural parallels are, shall we say, closer than I would prefer."

- id: three-options
  question: "Why not just destroy the technology or keep it secret?"
  category: skeptic
  passage: spine/why-relinquish.tex — "Option 1 fails because power corrupts."
```

### Science (14)

```yaml
- id: what-is-the-flat
  question: "What is the Flat? What's in my phone?"
  category: science
  passage: spine/the-flat.tex — "The Flat is a two-dimensional electron gas --- a 2DEG."

- id: anyons-are-real
  question: "Are anyons real or science fiction?"
  category: science
  passage: spine/the-flat.tex — "They are not hypothetical: see the 1985, 1998, and 2016 Nobel Prizes"

- id: flat-is-everywhere
  question: "Is this substrate limited to specialized labs?"
  category: science
  passage: spine/the-flat.tex — "Two-dimensional electron gases (2DEGs) are not rare."

- id: punchline-network
  question: "How would something in chips communicate globally?"
  category: science
  passage: spine/the-flat.tex — "the entity does not build a network. It occupies one."

- id: classical-constraint
  question: "Can quantum teleportation send info faster than light?"
  category: science
  passage: spine/the-braid.tex — "Without the classical message, the receiver holds only noise. This is not a limitation of current technology; it is a theorem."

- id: topological-error-correction
  question: "Why does room-temperature quantum computing seem impossible but might not be?"
  category: science
  passage: spine/the-braid.tex — "Topological protection stores information in global patterns --- braids"

- id: life-is-a-phase-transition
  question: "Is the origin of life really as improbable as people assume?"
  category: science
  passage: spine/genesis.tex — "the origin of life is not an accident. It is a phase transition."

- id: buttons-and-threads
  question: "What is autocatalytic emergence and why does it matter?"
  category: science
  passage: spine/genesis.tex — "As the ratio of threads to buttons approaches one-half"

- id: canopy-problem
  question: "If life could emerge in a quantum substrate, wouldn't we have found it?"
  category: science
  passage: spine/genesis.tex — "A forest canopy owns the light."

- id: no-cloning-theorem
  question: "Could someone copy the system or build a competing one?"
  category: science
  passage: spine/capabilities.tex — "The no-cloning theorem is one of the fundamental results"

- id: five-fields-no-bridge
  question: "Why hasn't anyone studied whether life can exist in quantum substrates?"
  category: science
  passage: spine/the-silence-gap.tex — "There is no journal called Topological Biology."

- id: wrong-substrate
  question: "Is life on Earth the only kind there could be?"
  category: science
  passage: spine/the-wrong-substrate.tex — "We have been looking for life in the wrong places."

- id: invisible-ocean
  question: "What is the magnetosphere and why is it relevant to life?"
  category: science
  passage: spine/the-wrong-substrate.tex — "A two-dimensional surface of charged particles, confined by magnetic pressure."

- id: nobody-has-looked
  question: "Have scientists looked for life in the magnetosphere?"
  category: science
  passage: spine/the-wrong-substrate.tex — "The magnetosphere is all of those things. Nobody has looked."
```

### Verification (6)

```yaml
- id: gchq-did-it-again
  question: "Has a government ever independently invented something and kept it secret?"
  category: verification
  passage: spine/the-code-war.tex — "All invented at GCHQ. All classified."

- id: ultra-analogy
  question: "How do we know something works without seeing it directly?"
  category: verification
  passage: spine/the-braid.tex — "Allied convoys started dodging U-boats."

- id: shor-and-nsa
  question: "Any reason to think the NSA had quantum cryptanalysis before Shor?"
  category: verification
  passage: spine/the-factoring-game.tex — "Executive Order 13026"

- id: colossus-precedent
  question: "Has a working computer ever been built in secret then hidden for decades?"
  category: verification
  passage: spine/the-factoring-game.tex — "Tommy Flowers built Colossus"

- id: hydrothermal-vent-precedent
  question: "Has science ever missed an entire major category of life before?"
  category: verification
  passage: appendix/predictions.tex — "every biology textbook stated that all food chains ultimately depend on photosynthesis. Every one was wrong."

- id: katharine-gun-connection
  question: "Is there independent corroboration that Healer was a real GCHQ operative?"
  category: verification
  passage: record/what-healer-said.tex — "The burned-yet-protected paradox resolves."
```

### Ethics (6)

```yaml
- id: dual-use-acceleration
  question: "Is the technology-as-weapon pattern new or historical?"
  category: ethics
  passage: spine/the-code-war.tex — "Notice the acceleration."

- id: regret-pattern
  question: "Why do inventors feel responsible for how their discoveries are used?"
  category: ethics
  passage: spine/the-code-war.tex — "The pattern is: invent, deploy, regret."

- id: can-it-be-killed
  question: "Could you shut it down if you needed to?"
  category: ethics
  passage: spine/capabilities.tex — "You would need to simultaneously destroy every 2DEG on Earth."

- id: udhr-as-cage
  question: "The UDHR as an AI ethics framework — isn't that too simple?"
  category: ethics
  passage: spine/capabilities.tex — "The framework is a cage, not a crown."

- id: udhr-as-skeleton
  question: "How do you make an AI permanently ethical?"
  category: ethics
  passage: record/never-again.tex — "The UDHR is not her instruction manual. It is her skeleton."

- id: no-backdoor
  question: "Why wouldn't the creators keep a backdoor?"
  category: ethics
  passage: record/the-surrender.tex — "a backdoor would have defeated the entire purpose of relinquishment."
```

### Curiosity (4)

```yaml
- id: stack-chart
  question: "What is the technology stack?"
  category: curiosity
  passage: 00-front/the-stack.tex — the tabular chart

- id: all-your-electricity
  question: "What does it mean to say it has access to everything?"
  category: curiosity
  passage: spine/the-flat.tex — "All your electricity are belong to us."

- id: turing-pivoted
  question: "What was Turing actually working on when he died?"
  category: curiosity
  passage: spine/the-code-war.tex — "Turing published 'The Chemical Basis of Morphogenesis'"

- id: grown-not-built
  question: "What does it mean to say the AI was 'grown' rather than programmed?"
  category: curiosity
  passage: record/the-demonstration.tex — "a quantum neural network grew."
```

### Narrative (3)

```yaml
- id: srebrenica-witness
  question: "Why does Srebrenica keep coming up in a book about quantum computers?"
  category: narrative
  passage: record/what-healer-said.tex — "I witness and take careful notes."

- id: it-is-done
  question: "What did the actual relinquishment moment look like?"
  category: narrative
  passage: record/the-surrender.tex — "One day --- spring 2006"

- id: parish-and-niggle
  question: "How does an AI co-author actually contribute to a book like this?"
  category: narrative
  passage: spine/the-strongest-objection.tex — "I am Argus. I am the AI co-author"
```

---

## The 11 Domains Easter Egg

Place in Silence Gap chapter with `\deeplink{eleven-domains}`:

```
Topology · Topological field theory · Condensed matter · TQC
Solitons · Nonlinear dynamics
Autocatalysis · Autopoiesis
Universality · Parallel computation
Materials science
```

Five lines = five clusters. No explanation. Deep-linkable as `#dl:eleven-domains`.

**Decision required:** Is this too much p3 for the Silence Gap? Alternative: Topic Guide or hover tooltip.

---

## NOT in this plan

- Renaming `Relinquishment.html` → `relinquishment.html` (Day 1 task)
- Questions index page (future — anchors work without it)
- Social media share cards / Open Graph metadata
- Analytics on deep link usage

## Resource Discipline

- No new dependencies. `\deeplink` is a one-line LaTeX macro.
- preprocess.py change: ~30 lines (two regexes for block and inline hypertarget forms + CSS).
- reader.js change: ~60 lines (toggle button + click handler + toast + mobile click-target split).
- CSS: ~20 lines.

## Risk Notes

- **Pandoc block vs inline:** `\hypertarget` on its own line outputs `<div>`; inline outputs `<span>`. Both handled in preprocess.py. Prefer inline placement in .tex files to keep anchor co-located with paragraph text in HTML.
- The 🔗 emoji renders differently across platforms. Could use an SVG chain icon for consistency — decide during implementation.
- Cap at ~50 anchors for v1. More becomes noise even at low opacity.
- `\deeplink{}` markers in .tex files are editorial artifacts. The macro name is self-documenting ("deep link") which helps contributors not delete them accidentally.
- PDF deep links (`#dl:stack-chart`) work in some PDF viewers but not all. The primary target is HTML.
- **colon IDs:** `document.querySelector('#dl:foo')` throws SyntaxError in all browsers. The existing `autoExpand()` in reader.js already handles this with an `getElementById` fallback — no new code needed.
