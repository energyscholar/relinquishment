# Plan 0335: Image Quality Pass

**Status:** Ready for Generator (three phases, separate commits)
**Prerequisite:** `git tag pre-0335` before starting any phase
**Risk mitigation:** Phases are independent. Each gets its own commit. If any phase goes wrong, `git revert` is surgical.

---

## Phase A (0335-A): Ghost Comment Screenshot Migration

**Risk: LOW.** One figure insertion in one .tex file. No automation.
**Commit:** `Plan 0335-A: migrate ghost-comment screenshot to active manuscript`

### A1. Background

The Ghost Comment screenshot (`images/slashdot-ghost-comment-2026-02-28.png`, 208KB) was referenced by `\includegraphics` in `manuscript/track-2-testament/pos34-the-research.tex`. That file was commented out of main.tex when its content was merged into `manuscript/record/twenty-years.tex`. The figure was never migrated. The image file exists and is valid but unreferenced in the active manuscript.

### A2. Insert figure into twenty-years.tex

File: `manuscript/record/twenty-years.tex`

Find the paragraph containing (approximately line 111):
```
June 19, 2012: a comment on Slashdot under my real user ID, EnergyScholar (UID 801915).
```

That paragraph ends with:
```
I was right about that too, as it turned out.
```

The NEXT paragraph begins:
```
I built a toy neural network in JavaScript
```

Insert the following block BETWEEN those two paragraphs:

```latex

\begin{figure}[h!]
\centering
\includegraphics[width=0.9\textwidth]{images/slashdot-ghost-comment-2026-02-28.png}
\caption{The Ghost Comment at its direct URL (captured 2026-02-28). Scored 5 (Funny), with replies. Live and accessible --- but absent from the poster's own profile and account history.}
\label{fig:ghost-comment}
\end{figure}

```

NOTE: This is the ONLY `\includegraphics` in twenty-years.tex. The image path `images/slashdot-ghost-comment-2026-02-28.png` is relative to the repo root. Pandoc with `--self-contained` embeds it as base64 (~280KB addition to HTML). The image file already exists at that path and is already copied into `build/epub-tmp/images/` by preprocess.py (lines 276–282).

### A3. Verify Phase A

```bash
cd ~/software/relinquishment && make html 2>&1 | tail -10
```

Check that the image made it into the HTML:
```bash
grep -c '<img' docs/Relinquishment.html
# Expected: 1 (the ghost comment — there were 0 before)

grep -o 'ghost-comment\|slashdot' docs/Relinquishment.html | head -5
# Should find at least one reference near the img tag
```

Check file size impact:
```bash
ls -la docs/Relinquishment.html
# Note size — expect ~280KB increase from base64 image embed
```

In browser:
1. Navigate to "Twenty Years of Observation" chapter
2. Find the June 2012 Slashdot section
3. Confirm: screenshot of the Ghost Comment renders with caption below it
4. The caption reads: "The Ghost Comment at its direct URL…"

Commit Phase A before proceeding to Phase B.

---

## Phase B (0335-B): Mobile Responsive SVG Fix

**Risk: LOW.** One CSS rule in html.css. No Python code changes.
**Commit:** `Plan 0335-B: responsive SVG scaling for mobile viewports`

### B1. Problem

Four inline SVG figures have fixed pixel widths that overflow on mobile (390px viewport):

| Figure | SVG width | Mobile overflow |
|--------|-----------|-----------------|
| `fig-substrate-trinity` | 780px | 832px (severe — right half hidden) |
| `fig-domain-buttons` | 460px | 512px (moderate — nodes clipped) |
| `fig-substrate-parallel` | 420px | 472px (moderate — half hidden) |
| `fig-edge-of-chaos` | 400px | 432px (minor — edge clipped) |

All four use `class="inline-svg"` on the figure and have `viewBox` set on the SVG, so they scale proportionally when constrained.

### B2. Fix: Add responsive CSS rule

File: `build/html.css`

Add the following rule AFTER the existing `@media (max-width: 600px)` block (after the closing `}` near line 49) and BEFORE the `/* TOC */` comment at line 51:

```css

/* Responsive inline SVG figures — constrain to container width */
.inline-svg svg { max-width: 100%; height: auto; }
```

This is an unconditional rule (not inside a media query) because some SVGs are wider than the content column even on desktop. The `max-width: 100%` constrains the SVG to its container; `height: auto` lets the browser compute height from the SVG's `viewBox` aspect ratio. SVGs already narrower than their container are unaffected.

DO NOT modify preprocess.py or any SVG `viewBox` values. The CSS-only approach is safest.

### B3. Verify Phase B

```bash
cd ~/software/relinquishment && make html 2>&1 | tail -10
```

Run mobile overflow check (puppeteer required):
```bash
cd ~/software/relinquishment && node -e "
const puppeteer = require('puppeteer');
(async () => {
  const browser = await puppeteer.launch({headless: true, args: ['--no-sandbox']});
  const page = await browser.newPage();
  await page.setViewport({width: 390, height: 844});
  await page.goto('file:///home/bruce/software/relinquishment/docs/Relinquishment.html', {waitUntil: 'networkidle0', timeout: 60000});
  await page.evaluate(() => document.querySelectorAll('details').forEach(d => d.open = true));
  await new Promise(r => setTimeout(r, 2000));
  const overflow = await page.evaluate(() => {
    const vw = window.innerWidth;
    const results = [];
    document.querySelectorAll('figure.inline-svg svg').forEach(svg => {
      const r = svg.getBoundingClientRect();
      if (r.right > vw + 5) results.push({id: svg.closest('figure')?.id || '?', right: Math.round(r.right), vw});
    });
    return results;
  });
  if (overflow.length === 0) console.log('PASS: no SVG overflow on mobile');
  else { console.log('FAIL:'); overflow.forEach(o => console.log('  ' + o.id + ': right=' + o.right + ' > vw=' + o.vw)); }
  await browser.close();
})();
"
```

Expected: `PASS: no SVG overflow on mobile`

Also verify desktop rendering in browser:
1. Check fig-edge-of-chaos — three panels (frozen/edge/chaos) still readable
2. Check fig-substrate-parallel — both chemistry and quantum sides visible
3. Check fig-domain-buttons — all 7 domain nodes and legend visible

### B4. Known limitation

`fig-substrate-trinity` (780px SVG) scales to ~50% on 390px phones. Text labels may be hard to read at that size. A proper mobile-optimized redesign of this SVG would be a separate plan. The CSS fix makes it technically fit; it doesn't guarantee readability on small screens.

Commit Phase B before proceeding to Phase C.

---

## Phase C (0335-C): Duplicate Caption Removal

**Risk: LOW.** One string edit in preprocess.py.
**Commit:** `Plan 0335-C: remove duplicate consequence-fork caption`

### C1. Problem

`fig-consequence-fork` displays "Same evidence. Same silence. Different futures." twice:
1. Inside the SVG as a `<text>` element (line 416 of `build/images/scientific-revolutions-chapter.html`)
2. As an HTML `<figcaption>` injected by preprocess.py

### C2. Fix: Remove the figcaption

File: `build/preprocess.py`

Find the consequence-fork figure injection. Search for `fig-consequence-fork`. The code is:

```python
            svg056_html = (
                '<figure id="fig-consequence-fork" class="inline-svg" style="text-align:center;margin:1.5em auto;">\n'
                f'{m056.group(1)}\n'
                '<figcaption style="font-size:0.85em;color:#908878;margin-top:0.3em;font-style:italic;">'
                'Same evidence. Same silence. Different futures.</figcaption>\n'
                '</figure>'
            )
```

Replace with (remove the figcaption lines):

```python
            svg056_html = (
                '<figure id="fig-consequence-fork" class="inline-svg" style="text-align:center;margin:1.5em auto;">\n'
                f'{m056.group(1)}\n'
                '</figure>'
            )
```

### C3. Verify Phase C

```bash
cd ~/software/relinquishment && make html 2>&1 | tail -10
```

In browser:
1. Navigate to "The Structure of Scientific Revolutions" chapter
2. Scroll to the consequence-fork diagram (the A1/A2 decision tree near "Neither is a consolation")
3. Confirm: "Same evidence. Same silence. Different futures." appears ONCE (inside the SVG at the bottom of the diagram), not twice
4. Visual spacing below the diagram should look clean

Commit Phase C.

---

## Deferred (not in this plan)

- **D1: Three additional screenshots** — pos34-the-research.tex has three commented-out figures (Slashdot profile screenshot, two Substack screenshots). The image files don't exist. Bruce needs to capture these. Separate task.
- **D2: Substrate-trinity mobile readability** — Even with responsive scaling, the 780px SVG is very small on phones. Redesigning this SVG for mobile is a separate plan.
- **J2: Filmstrip whitespace** — Investigated: the empty space above the buttons in fig-buttons-filmstrip is needed for the 6-frame scatter/tie/net/snap animation. Not a bug.
- **S1/S4/S6 from Plan 0334** — Duplicate HTML IDs, broken puzzle link, JS template IDs — still deferred.

## Do NOT (any phase)

- Change any manuscript content beyond the specific figure insertion in A2
- Modify any existing SVG `viewBox` values or SVG source files
- Add CSS to preprocess.py — the html.css file is the right place for Phase B
- Change epub.css or the EPUB build path
- Remove or relocate the ghost-comment PNG from `images/`
- Add `\includegraphics` to any file other than `record/twenty-years.tex`
- Run release.sh
