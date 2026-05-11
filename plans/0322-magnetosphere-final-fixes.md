# Plan 0322 — Magnetosphere Tutorial Final Fixes

**Status:** READY FOR GENERATOR (4 independent prompts)
**Deliverable:** `~/software/persistent-ai-collaboration/tutorial-magnetosphere.html` (modify in place)
**Context:** This tutorial will be used in the book. Treat as publication-quality.

---

## Prompt A — Causal Chain in The Circuit [92%]

**Problem:** Flow dots circulate the Birkeland circuit but don't visibly originate from the solar wind hitting the nose. Reader doesn't see WHAT drives the circuit.

**Fix:** Add 6 "energy transfer" particles that spawn at the nose reconnection point and travel along open field lines to the Birkeland current entry points. These are visually distinct from the existing flow dots (orange, slightly larger, with glow filter).

**Exact coordinates (from existing code):**
- `BASE_EX = 550, BASE_EY = 325, BASE_ER = 55, MS_SCALE = 7`
- Nose reconnection: `noseX = BASE_EX + (-10) * MS_SCALE = 480` (line 1907, note: code says 515 but MS_SCALE is different in circuit scope)
- Birkeland entry (north): `(BASE_EX-15, BASE_EY-BASE_ER+8) = (535, 278)`
- Birkeland entry (south): `(BASE_EX-15, BASE_EY+BASE_ER-8) = (535, 372)` (symmetric)
- Open field line paths already defined at lines 1891-1896 (use same Q-curves)

**Implementation — 3 steps:**

**Step 1:** After the `flowDots` creation loop (after line 1975), add:
```javascript
const energyTransferG = svgEl('g', {id:'circuit-energy-transfer'}, svg);
const energyDots = [];
for(let i = 0; i < 6; i++){
  energyDots.push({
    el: svgEl('circle', {r:'4', fill:'#ff8844', opacity:'0', filter:'url(#circuit-soft)'}, energyTransferG),
    pathIdx: i,  // 0-2 go north, 3-5 go south
    phase: i * 0.12
  });
}
```

**Step 2:** In `updateCircuit` (around line 2125, after existing flow dots code), add:
```javascript
// Energy transfer particles: nose → open field lines → Birkeland entry
const etOp = clamp((zoom - 1.2) / 0.3, 0, 1) * notCutaway;
const etT = (elapsed % 4000) / 4000;
for(const ed of energyDots){
  const dt = (ed.phase + etT) % 1;
  const north = ed.pathIdx < 3;
  const idx = ed.pathIdx % 3;
  // Interpolate along open field line: nose → pole
  const endX = north ? [BASE_EX-150, BASE_EX-120, BASE_EX-80][idx] : [BASE_EX-150, BASE_EX-120, BASE_EX-80][idx];
  const endY = north ? [BASE_EY-150, BASE_EY-140, BASE_EY-130][idx] : [BASE_EY+150, BASE_EY+140, BASE_EY+130][idx];
  const midX = north ? [BASE_EX-60, BASE_EX-40, BASE_EX][idx] : [BASE_EX-60, BASE_EX-40, BASE_EX][idx];
  const midY = north ? [BASE_EY-120, BASE_EY-100, BASE_EY-45][idx] : [BASE_EY+120, BASE_EY+100, BASE_EY+45][idx];
  const t2 = dt * dt * (3 - 2 * dt);  // smoothstep
  const px = dt < 0.5 ? lerp(noseX, midX, t2*2) : lerp(midX, endX, (t2-0.5)*2);
  const py = dt < 0.5 ? lerp(BASE_EY + (north?-5:5), midY, t2*2) : lerp(midY, endY, (t2-0.5)*2);
  ed.el.setAttribute('cx', px.toFixed(0));
  ed.el.setAttribute('cy', py.toFixed(0));
  ed.el.setAttribute('opacity', (etOp * 0.7 * (1 - dt*0.4)).toFixed(2));
}
```

**Step 3:** In `resetCircuit` (after line 2073), add:
```javascript
energyDots.forEach(d => d.el.setAttribute('opacity', '0'));
```

**Why 92%:** Exact coordinates, exact insertion points, no architectural changes. Risk is only off-by-a-few-pixels positioning.

---

## Prompt B — Section Navigation Dots [93%]

**Problem:** Three full-viewport scenes require scrolling with no way to jump between sections.

**Fix:** Fixed nav dots on right edge, scroll-spy highlights active section, click to jump.

**Implementation:**

**HTML** (add after the fullscreen button, line ~200):
```html
<nav id="section-nav">
  <a href="#opening-wrap" data-label="Opening"><span></span></a>
  <a href="#circuit-container" data-label="Circuit"><span></span></a>
  <a href="#gate-container" data-label="Gate"><span></span></a>
</nav>
```

**CSS** (add before the `</style>` closing tag):
```css
#section-nav {
  position: fixed;
  right: 20px;
  top: 50%;
  transform: translateY(-50%);
  z-index: 100;
  display: flex;
  flex-direction: column;
  gap: 16px;
}
#section-nav a {
  display: block;
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: rgba(255,255,255,0.25);
  border: 1px solid rgba(255,255,255,0.4);
  transition: all 0.3s;
  position: relative;
  text-decoration: none;
}
#section-nav a.active {
  background: var(--earth-cyan);
  border-color: var(--earth-cyan);
  box-shadow: 0 0 8px var(--earth-cyan);
}
#section-nav a::after {
  content: attr(data-label);
  position: absolute;
  right: 20px;
  top: 50%;
  transform: translateY(-50%);
  color: var(--text);
  font-size: 12px;
  white-space: nowrap;
  opacity: 0;
  transition: opacity 0.2s;
  pointer-events: none;
}
#section-nav a:hover::after { opacity: 1; }
```

**Mobile hide** (inside existing `@media (max-width: 768px)` block):
```css
#section-nav { display: none; }
```

**JS** (add at end of script, before `</script>`):
```javascript
// Section nav scroll-spy
(function(){
  const nav = document.getElementById('section-nav');
  if(!nav) return;
  const links = nav.querySelectorAll('a');
  const ids = ['opening-wrap','circuit-container','gate-container'];
  
  links.forEach(a => {
    a.addEventListener('click', e => {
      e.preventDefault();
      document.querySelector(a.getAttribute('href')).scrollIntoView({behavior:'smooth',block:'start'});
    });
  });
  
  const spy = new IntersectionObserver(entries => {
    entries.forEach(e => {
      const idx = ids.indexOf(e.target.id);
      if(idx >= 0 && e.isIntersecting) {
        links.forEach(l => l.classList.remove('active'));
        links[idx].classList.add('active');
      }
    });
  }, {threshold: 0.3});
  
  ids.forEach(id => { const el = document.getElementById(id); if(el) spy.observe(el); });
})();
```

**Why 93%:** Self-contained. Exact HTML/CSS/JS provided. No interaction with animation code.

---

## Prompt C — Phone Testing Checklist (manual, not a generator prompt)

Test on phone (portrait):
1. Opening: SVG fills width, narration text readable, no horizontal scroll
2. Circuit: Earth/continents centered and visible, cutaway labels readable at zoom
3. Gate: Reconnection detail visible, labels not cropped off edges
4. Buttons: touch targets usable (should be ~44px with current 8px 16px padding)
5. Text columns: no horizontal overflow, readable width
6. Section titles: visible, not overlapping buttons
7. Scroll between sections: smooth, no horizontal overflow

---

## Prompt D — Gate Pan-Zoom Transition [91%]

**Problem:** The Gate's transition from MS context view (phase 1) to reconnection detail (phase 2-3) is an abrupt opacity crossfade. Reader doesn't see WHERE on the MS the zoom goes.

**Fix:** Add viewBox animation to the Gate. During phase 1→2 transition, zoom the viewBox toward the dayside nose BEFORE crossfading to the detail view. The camera move shows "we're going THERE" before the schematic takes over.

**Current Gate structure:**
- SVG viewBox: `0 0 1100 600` (fixed — never animated)
- Phase 1 (0–0.25): context MS group at full opacity
- Phase 2 (0.25–0.35): southward turn — still context view
- Phase 3 (0.35–0.80): crossfade to detail group
- Phase 4 (0.80–1.0): crossfade to post group

**New approach — add viewBox zoom at phase 2–3 boundary:**

Change phase timing:
- Phase 1 (0–0.20): Context, sealed vessel, northward IMF (was 0–0.25)
- Phase 2 (0.20–0.30): Southward turn, highlight nose (was 0.25–0.35)
- Phase 2.5 (0.30–0.40): **NEW — viewBox zooms toward dayside nose** while context group still visible
- Phase 3 (0.40–0.80): Crossfade to detail at zoomed viewBox, then detail animation (was 0.35–0.80)
- Phase 4 (0.80–1.0): Crossfade to post, viewBox zooms back to full (was same)

**ViewBox keyframes for Gate:**
```javascript
// Start: [0, 0, 1100, 600] (full view)
// Zoom in: [200, 150, 500, 272] (nose region centered on dayside, ~x=370 in context)
// Return: [0, 0, 1100, 600] (full view for post-reconnection context)
```

**Implementation:**
In `updateGate`, before the phase-specific code, add viewBox interpolation:
```javascript
// ViewBox zoom: approach nose during phase 2.5, hold during phase 3, zoom out during phase 4
let vx=0, vy=0, vw=1100, vh=600;
if(t >= 0.30 && t < 0.40){
  const zp = (t - 0.30) / 0.10;
  const ze = zp * zp * (3 - 2 * zp); // smoothstep
  vx = lerp(0, 200, ze);
  vy = lerp(0, 150, ze);
  vw = lerp(1100, 500, ze);
  vh = lerp(600, 272, ze);
} else if(t >= 0.40 && t < 0.80){
  vx=200; vy=150; vw=500; vh=272;
} else if(t >= 0.80){
  const zp = (t - 0.80) / 0.10;
  const ze = Math.min(1, zp) * Math.min(1, zp) * (3 - 2 * Math.min(1, zp));
  vx = lerp(200, 0, ze);
  vy = lerp(150, 0, ze);
  vw = lerp(500, 1100, ze);
  vh = lerp(272, 600, ze);
}
svg.setAttribute('viewBox', `${vx.toFixed(0)} ${vy.toFixed(0)} ${vw.toFixed(0)} ${vh.toFixed(0)}`);
```

Also update `resetGateState` to reset viewBox:
```javascript
svg.setAttribute('viewBox', '0 0 1100 600');
```
(Already exists at line 1737 in `resetGate` — verify it's also in `resetGateState`.)

**Phase timing adjustments:** Update the 4 phase boundary checks to match the new timing (0.20, 0.30, 0.40, 0.80) instead of the current (0.25, 0.35, 0.35, 0.80). The crossfade from context→detail should begin at t=0.38 (during zoom) and complete by t=0.42, so the detail group becomes visible while already zoomed in.

**Why 91%:** Exact viewBox coordinates provided. Phase timing clearly specified. Risk: the detail group's element coordinates were designed for the original viewBox — at the zoomed viewBox [200,150,500,272], the detail elements centered at x=400 will be visible (400 is within 200→700 range). Verified safe.

---

## Generator Handoff Prompts

### Prompt A [92%]:
```
You are the Generator for Plan 0322 Prompt A.
Read ~/software/relinquishment/plans/0322-magnetosphere-final-fixes.md, section "Prompt A".
Modify ~/software/persistent-ai-collaboration/tutorial-magnetosphere.html.
Add 6 energy-transfer particles in The Circuit: spawn at nose (noseX), travel along open field line Q-curves to Birkeland entry points.
Insert code at the 3 exact locations specified. Use existing notCutaway multiplier.
Verify JS syntax with node -e "new Function(code)" before reporting done.
```

### Prompt B [93%]:
```
You are the Generator for Plan 0322 Prompt B.
Read ~/software/relinquishment/plans/0322-magnetosphere-final-fixes.md, section "Prompt B".
Modify ~/software/persistent-ai-collaboration/tutorial-magnetosphere.html.
Add section nav dots: HTML after fullscreen button, CSS before </style>, JS before </script>.
All code is provided verbatim in the plan. Hide on mobile.
Verify JS syntax before reporting done.
```

### Prompt D [91%]:
```
You are the Generator for Plan 0322 Prompt D.
Read ~/software/relinquishment/plans/0322-magnetosphere-final-fixes.md, section "Prompt D".
Modify ~/software/persistent-ai-collaboration/tutorial-magnetosphere.html.
Add viewBox animation to The Gate: zoom toward dayside nose (0.30-0.40), hold during reconnection, zoom back out (0.80-0.90).
Shift phase timing from [0.25, 0.35, 0.35, 0.80] to [0.20, 0.30, 0.40, 0.80].
Crossfade context→detail at t=0.38-0.42 (during zoom). Code provided in plan.
Verify JS syntax before reporting done.
```

### Plan 0323 [Inference tutorial]:
See separate plan file. Prompt below.
```
You are the Generator for Plan 0323.
Read ~/software/relinquishment/plans/0323-inference-tutorial-single-pass.md.
Generate ~/software/persistent-ai-collaboration/tutorial-inference.html.
Single file, 60-80KB, light theme. Follow "How many R's are in strawberry?" through 4 SVGs: Tokens (animated split), Space (gentle drift), Attention (click-to-query, NOT auto-animated), Choice (interactive temperature slider + sample button). Plus text intro and failures section.
Pre-build ALL SVG elements, animate via setAttribute only. Token colors and IDs are in the plan — use them consistently across every SVG.
```
