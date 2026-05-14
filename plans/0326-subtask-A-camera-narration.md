# Subtask A: Camera Journey + Narration + Scale Bar

**Parent:** Plan 0326 rev 3
**Output:** Replace `MS_ANIM_OPENING` in `build/preprocess.py` with faithful port of tutorial SVG, utilities, camera journey, narration, and scale bar. No substorm yet.
**Commit:** `Plan 0326A: faithful camera journey + narration + scale bar`
**Read first:** This spec, then the tutorial source (line refs below), then current code to replace.

## Source

`~/software/persistent-ai-collaboration/tutorial-magnetosphere.html`
- Lines 311–415: SVG markup (ALL elements including substorm group at opacity 0)
- Lines 417–423: Narration overlays (6 divs)
- Lines 425–431: Scale bar + time readout
- Lines 705–771: Utilities (svgEl, ease, lerp, clamp, catmullRom, boundaryPts, ptsToPath, dipoleLine, reducedMotion)
- Lines 774–1405: Opening IIFE — port camera journey (`updateOpen`), **skip `substormLoop`**

## Target

`~/software/relinquishment/build/preprocess.py` — replace `MS_ANIM_OPENING` constant (lines 3339–3611). Keep `inject_ms_animated_opening()` function unchanged.

## What to Port

### SVG Elements (ALL from tutorial lines 311–415, prefix `open-` → `mso-`)

Port every element. Include the substorm group (lines 401–412) with its children — NENL, flow-particles, aurora N/S, phase-label, substorm-label, energy-note, discharge-note. These stay at `opacity="0"` — Subtask B adds the JS that drives them. Including them now avoids Subtask B needing to modify SVG markup.

Full ID mapping in parent plan (0326-ms-animation-report.md §7). Key renames:
- Gradients: `sun-core-grad` → `mso-sun-core`, `sun-corona-grad` → `mso-sun-corona`, `open-earth-grad` → `mso-earth-grad`, `ms-front-grad` → `mso-front-grad`
- Filter: `open-glow` → `mso-glow`
- ClipPath: `title-safe-clip` → `mso-clip`
- All `url(#...)` and `filter="url(#...)"` refs updated to match

Include all 6 sun streamers (tutorial has 6, rev 2 dropped 2).

Initial viewBox: `0 0 1600 900` on the SVG element.

### Narration Overlays (6 divs, inside `mso-container`)

```html
<div class="mso-narr" id="mso-narr-1" style="top:55%;left:6%;max-width:380px;">One hundred and fifty million kilometres away, the Sun exhales. A million tonnes of charged plasma per second.</div>
<div class="mso-narr" id="mso-narr-2" style="top:58%;right:6%;text-align:right;max-width:360px;">Racing outward at four hundred kilometres per second. It has been doing this for four and a half billion years.</div>
<div class="mso-narr" id="mso-narr-3" style="top:65%;left:50%;transform:translateX(-50%);text-align:center;max-width:300px;">Earth stands in the way.</div>
<div class="mso-narr" id="mso-narr-4" style="top:60%;right:6%;text-align:right;max-width:340px;">A magnetic shield &mdash; invisible, enormous &mdash; deflects the wind around the planet.</div>
<div class="mso-narr" id="mso-narr-5" style="top:65%;left:6%;max-width:360px;">This rhythm is four and a half billion years old&mdash;older than life on Earth. The magnetosphere has never stopped breathing.</div>
<div class="mso-narr" id="mso-narr-6" style="top:72%;right:6%;text-align:right;max-width:380px;">The Moon passes through the magnetotail once every orbit. Sixty Earth-radii out.</div>
```

Place inside `mso-container` div, after the SVG, before the play button.

### Scale Bar + Time Readout

```html
<div class="mso-key" id="mso-key">
  <div id="mso-time-text"></div>
  <div style="display:flex;align-items:center;gap:8px;">
    <div id="mso-scale-bar" style="width:80px;height:4px;background:#ffb347;border-radius:2px;"></div>
    <span id="mso-scale-text">150 million km</span>
  </div>
</div>
```

Place inside `mso-container`, after narration divs.

### CSS Additions

Add to the `<style>` block:

```css
.mso-narr{position:absolute;color:rgba(255,255,255,0.9);font-family:Georgia,serif;font-size:14px;line-height:1.6;opacity:0;transition:opacity 0.3s;pointer-events:none;z-index:5;text-shadow:0 1px 4px rgba(0,0,0,0.8)}
.mso-key{position:absolute;bottom:20px;left:24px;z-index:5;pointer-events:none;font-family:system-ui;color:#999;font-size:12px}
```

### Utilities (ALL inside the IIFE)

Port from tutorial lines 705–771:
- `svgEl` — keep existing
- `ease(t)` — ADD: `function ease(t){return t<0.5?4*t*t*t:1-Math.pow(-2*t+2,3)/2;}`
- `lerp(a,b,t)` — ADD: `function lerp(a,b,t){return a+(b-a)*t;}`
- `clamp` — keep existing
- `catmullRom(pts,t)` — ADD from tutorial lines 757–771, ES5 style
- `boundaryPts` — keep existing
- `ptsToPath` — keep existing
- `dipoleLine` — keep existing
- `reducedMotion` — ADD: `var reducedMotion=window.matchMedia('(prefers-reduced-motion: reduce)').matches;`

### Particle Pools

- 80 wind particles (50 ions, 30 electrons) — tutorial lines 786–801
- 30 front-deflection particles — tutorial lines 844–851
- 6 hero particles — tutorial lines 857–878
- 10 substorm flow particles — tutorial lines 881–890. BUILD THEM (so Subtask B doesn't need to add DOM code), but their opacity stays 0 since substormLoop isn't ported yet.

### Camera Keyframes

Tutorial's 17 keyframes exactly (lines 1030–1048). Sun-first direction. `var DURATION=48000;`

### `updateOpen(ts)` — Port Full (tutorial lines 1084–1357)

All of it EXCEPT the completion handler. Port:
- Camera interpolation via `interpKF(t)` (Catmull-Rom, tutorial lines 1051–1068)
- Narration fade (tutorial lines 1096–1105): timing array `[[0.02,0.18,'mso-narr-1'], ...]`
- Sun visibility + corona pulse (lines 1108–1118)
- Front-view MS opacity (lines 1121–1123)
- Front wind deflection (lines 1126–1148) — 30 particles
- Hero particles approach/arc/depart (lines 1150–1220)
- Side-view MS with breathing (lines 1222–1230)
- Moon orbit + label (lines 1232–1340)
- MS labels (lines 1249–1251)
- Solar wind particles with MP deflection (lines 1253–1275) — 80 particles
- Scale bar computation (lines 1277–1297) — logarithmic AU/RE interpolation
- Time rate computation (lines 1299–1318) — `TRK` array with log interpolation
- Wind label visibility + repositioning (lines 1320–1328)

### Completion (Subtask A version)

At `t >= 1.0`: auto-pause. Return to poster frame (viewBox `1000 160 900 506`). Show play button. Reset progress bar. Do NOT enter substormLoop — that's Subtask B. The tutorial's completion handler (lines 1343–1356) transitions to substormLoop; replace that with simple pause+reset.

### Poster Frame (paused initial state)

On load, set:
- `viewBox` to `1000 160 900 506` (side view, same as tutorial's reducedMotion state, line 1400)
- `mso-side-ms` opacity 1
- `mso-ms-labels` opacity 0.8
- All other groups at their default (opacity 0 or as set in SVG)

When play starts: reset viewBox to `0 0 1600 900`, reset all element opacities, run `updateOpen`.

### Book UI Chrome (keep from rev 2)

- Mobile teaser with "Play Fullscreen" button
- Desktop: inline container with ▶ play, ⛶ fullscreen, progress bar (48s fill)
- Click-to-play, Space toggles, Escape exits fullscreen
- iOS pseudo-fullscreen fallback
- `@media print` rule
- Deep link `id="dl:ms-opening"` on figure

### reducedMotion

If `reducedMotion` is true: show poster frame (side view), don't auto-play. Play button still works on click (per WCAG).

## ES5 Translation

The tutorial uses `const`, `let`, arrow functions, template literals, `for...of`. The book's existing JS uses ES5 (`var`, `function`, string concat, indexed `for` loops). **Translate to ES5** to match. Key patterns:
- `const`/`let` → `var`
- `for(const x of arr)` → `for(var i=0;i<arr.length;i++){var x=arr[i];...}`
- `` `${expr}` `` → `expr + '...'` or `'...'+expr`
- `(a,b) => ...` → `function(a,b){return ...;}`
- Destructuring `const [vx,vy,vw,vh] = interpKF(t)` → `var vb=interpKF(t),vx=vb[0],vy=vb[1],vw=vb[2],vh=vb[3];`

## Verify

```bash
cd ~/software/relinquishment && make html 2>&1 | tail -10
```

Open in browser. Verify:
1. Animation starts paused (poster: side view of MS, labels visible)
2. Click play → camera starts at Sun, zooms/pans to Earth over 48s
3. Narration text fades in/out at correct times (6 overlays)
4. Scale bar updates (AU scale → km scale as zoom changes)
5. Time readout shows compression rate
6. Wind particles stream Sun→Earth, deflect around magnetopause
7. Hero particles arc around shield during front+side view phases
8. Moon visible during wide zoom-out (t=0.76–0.86)
9. At t=1.0: auto-pauses, returns to poster frame
10. Fullscreen works, mobile teaser works
11. No console errors
12. `verify-deep-links.py` passes

## Do NOT

- Port `substormLoop` (that's Subtask B)
- Change `inject_ms_animated_opening()` function
- Change any other code in preprocess.py
- Modify the tutorial source file
- Use ES6 syntax (const, let, arrow, template literal, for...of, destructuring)
- Put utilities in global scope

## Report

Confirm: camera journey plays Sun-to-Earth, narration visible, scale bar updates, hero particles deflect, auto-pauses at end. Note file size of new constant.
