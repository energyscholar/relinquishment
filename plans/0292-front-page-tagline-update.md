# Plan 0292: Front Page Tagline Update + Image Layout Fix + Source Sync

**Status:** ANNEALED (MED MED)
**Author:** Auditor (Argus S65)
**Origin:** S64 landing page overhaul (commit c861e35) updated docs/index.html with framing phrase + physics-forward tagline. The same changes were never applied to the reader HTML title page (preprocess.py:574-575). Additionally, title.tex is out of sync (old word order + stale "for all of it"). The MS cover image overlaps with tagline text on desktop and is invisible on phone.
**Risk:** LOW-MEDIUM (text changes + JS layout fix, 9 files)
**Annealed:** MED MED — 3 issues found and fixed: (1) CSS % padding replaced with JS exact-pixel padding, (2) metadata.yaml uses science keywords not framing phrase, (3) hover prose paragraph updated.

---

## Problem 1: Stale Title Page Taglines

The landing page (docs/index.html) was overhauled in S64 commit c861e35:

**Landing page (CURRENT — correct):**
```
This is what truth-telling looks like when the truth is classified
and the classification will outlive everyone who knows it.

Real people. Real physics. Three possible explanations. You decide.
```

**Reader HTML title page (CURRENT — wrong, never updated):**
```
Three narrative threads. Real people. Real science. Real institutions.
Three possible explanations. You decide.
```

**title.tex / PDF (CURRENT — also wrong, doubly stale):**
```
Three narrative threads. Real science. Real People. Real institutions.
Three possible explanations for all of it.
You decide.
```

## Target Text

The reader HTML title page should match the landing page:

```
Relinquishment — Wormholes in the Flat
by Bruce Stephenson, Genevieve Prentice & Argus

This is what truth-telling looks like when the truth is classified
and the classification will outlive everyone who knows it.
Real people. Real physics. Three possible explanations. You decide.

© 2026 Bruce Stephenson & Genevieve Prentice · CC BY-ND 4.0
```

**Two tagline changes:**
1. "Three narrative threads. Real people. Real science. Real institutions." → "This is what truth-telling looks like when the truth is classified and the classification will outlive everyone who knows it."
2. "Three possible explanations. You decide." → "Real people. Real physics. Three possible explanations. You decide."

**C-violation check:** Framing phrase describes the book's purpose (truth-telling under classification constraint). True under A, B, and C. No violation.

## Problem 2: MS Cover Image Layout

The JS-injected magnetosphere SVG (`reader.js:489-794`, `#cover-magnetosphere`) is positioned `position:absolute; right:0; bottom:calc(100% - 15px)` relative to the sticky nav bar. It sits above-right of the nav.

**Desktop:** Image renders at ~280px (45% of nav width), but the tagline text (`.title-page-extra`) extends full-width, overlapping the image. "Real institutions" runs directly into the magnetosphere.

**Phone (390px):** Image renders at 163px in the DOM (confirmed via Puppeteer). But `.title-page-extra` fills the full 364px page width, completely covering the image. The image is invisible because text is on top of it.

**Root cause:** `.title-page-extra` has no width constraint. It fills 100% of the summary element, overlapping the absolutely-positioned image.

**Fix (annealed):** ~~CSS `padding-right: 42%`~~ → JavaScript exact-pixel padding in `reader.js`. After creating the MS image wrapper and appending it to nav, set exact padding on the title-page-extra element:

```javascript
var titleExtra = document.querySelector('.title-page-extra');
if (titleExtra) titleExtra.style.paddingRight = (msWidth + 10) + 'px';
```

This is better than CSS percentages because:
- Exact pixel match to the computed image width (no percentage mismatch)
- Only applies when the image actually exists (no empty gap if JS fails)
- Adapts to viewport size (msWidth is already responsive)

## Files to Change (9 total)

### 1. `build/preprocess.py` (line 574-575)
Visible title page in reader HTML. Replace both tp-tagline lines:
```python
'<p class="tp-tagline"><em>This is what truth-telling looks like when the truth is classified and the classification will outlive everyone who knows it.</em></p>'
'<p class="tp-tagline"><em>Real people. Real physics. Three possible explanations. You decide.</em></p>'
```

### 2. `build/preprocess.py` (line 1713-1714)
Regex that strips pandoc-generated tagline (prevents duplication). Must match NEW text.
Change first regex to match new framing phrase:
```python
r'<p><span><em>This is what truth-telling.*?</em></span></p>\s*'
r'<p><span><em>Real people\. Real physics\..*?</em></span></p>\s*'
```

### 3. `build/reader.js` (~line 760, after `nav.appendChild(wrapper)`)
Add exact-pixel padding to prevent text-image overlap:
```javascript
nav.appendChild(wrapper);

// Prevent title-page text from overlapping the MS image
var titleExtra = document.querySelector('.title-page-extra');
if (titleExtra) titleExtra.style.paddingRight = (msWidth + 10) + 'px';
```

### 4. `build/metadata.yaml` (lines 7-9)
Source of truth for pandoc meta description. **Use science keywords, not framing phrase** — meta description serves SEO, not emotional hook (Plan 0288 §4).
```yaml
description: >
  Real physics. A two-dimensional substrate in every chip and every magnetosphere.
  Three possible explanations. You decide.
```

### 5. `manuscript/00-front/title.tex` (lines 23-31)
LaTeX/PDF title page. **Currently doubly stale** — old word order AND "for all of it."
Replace lines 23-31 with:
```latex
{\normalsize\textit{This is what truth-telling looks like when the truth is classified}}

\vspace{0.2cm}

{\normalsize\textit{and the classification will outlive everyone who knows it.}}

\vspace{0.5cm}

{\normalsize\textit{Real people. Real physics. Three possible explanations. You decide.}}
```

### 6. `build/hover-definitions.yaml` (~line 16)
Two changes in the `relinquishment-title` entry:

**a) Prose paragraph** — update "Real physics, real people, real institutions" to match new framing:
```
<strong>Relinquishment</strong> — placing dangerous technology in the custody of a custodian
who cannot be corrupted. Not permanent surrender, but trust. This is what truth-telling looks
like when the truth is classified. Real people, real physics, three possible explanations.
```

**b) SVG `<text>` elements:**
- Line 1: "Three narrative threads. Real science." → "Real people. Real physics."
- Line 2: unchanged ("Three possible explanations. You decide.")
- `<title>` attribute: update to match.

### 7. `build/test-fixtures/tooltips-baseline.json` (~line 541)
Test fixture — must match hover-definitions.yaml. Same prose + SVG text substitutions.

### 8. `build/svg-sheet.html` (~line 732)
SVG visual reference. Same SVG text substitutions.

### 9. `docs/index.html`
Already correct for taglines. But triskellion image was removed in S65 — verify this is committed. No further changes needed if already committed.

## Build + Verify

```bash
cd ~/software/relinquishment
make dev
```

### Verification checklist:
- [ ] `grep "truth-telling" docs/downloads/Relinquishment.html` finds the title page framing phrase
- [ ] `grep "Real people. Real physics" docs/downloads/Relinquishment.html` finds the tagline
- [ ] `grep "Three narrative threads" docs/downloads/Relinquishment.html` returns ZERO results
- [ ] `grep "for all of it" docs/downloads/Relinquishment.html` returns ZERO results
- [ ] `grep "for all of it" manuscript/00-front/title.tex` returns ZERO results
- [ ] PDF title page shows new text
- [ ] Puppeteer screenshot at desktop (1400×900) shows text NOT overlapping MS image
- [ ] Puppeteer screenshot at phone (390×844) shows MS image visible beside text

### Puppeteer visual verification (both viewports):
```javascript
node -e "
const puppeteer = require('puppeteer');
(async () => {
  const browser = await puppeteer.launch({ headless: 'new', args: ['--no-sandbox','--disable-setuid-sandbox','--disable-dev-shm-usage','--disable-gpu'] });

  // Desktop
  var p = await browser.newPage();
  await p.setViewport({ width: 1400, height: 900 });
  await p.goto('file:///home/bruce/software/relinquishment/docs/downloads/Relinquishment.html', { waitUntil: 'networkidle2', timeout: 60000 });
  await new Promise(r => setTimeout(r, 3000));
  await p.screenshot({ path: '/tmp/0292-desktop.png' });

  // Phone
  p = await browser.newPage();
  await p.setViewport({ width: 390, height: 844 });
  await p.goto('file:///home/bruce/software/relinquishment/docs/downloads/Relinquishment.html', { waitUntil: 'networkidle2', timeout: 60000 });
  await new Promise(r => setTimeout(r, 3000));
  await p.screenshot({ path: '/tmp/0292-phone.png' });

  await browser.close();
  console.log('Screenshots: /tmp/0292-desktop.png, /tmp/0292-phone.png');
})();
"
```

Read BOTH screenshots to verify text and image don't overlap.

## Post-build

```bash
git add docs/downloads/ && git push
```

Website push required — Bruce reads on phone.
