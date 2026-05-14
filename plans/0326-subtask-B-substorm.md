# Subtask B: Substorm Cycle

**Parent:** Plan 0326 rev 3
**Depends on:** Subtask A complete and working
**Output:** Add `substormLoop` to the animation JS in `build/preprocess.py`
**Commit:** `Plan 0326B: substorm cycle — Growth/Onset/Expansion/Recovery/Quiet`
**Read first:** This spec, then tutorial source lines 880–1021 and 1343–1405.

## Source

`~/software/persistent-ai-collaboration/tutorial-magnetosphere.html`
- Lines 880–890: Flow particle pool (already built by Subtask A)
- Lines 894–1021: `substormLoop(ts2)` function
- Lines 1343–1356: Completion handler (transition from camera → substorm)
- Lines 1359–1405: Play/pause/reset with substorm awareness

## What to Add

### 1. `substormLoop` function (tutorial lines 894–1021)

Port the entire function inside the existing IIFE, after `updateOpen`. Translate to ES5. Use `mso-` IDs throughout.

The function runs a 22-second repeating cycle (`var SUBSTORM_CYCLE=22000`):

| Phase | t range | Visuals |
|-------|---------|---------|
| Growth | 0–0.36 | Tail stretches (50→70 RE), plasma sheet thins (gap 1.5→0.7), flow particles appear one-by-one drifting tailward, plasma sheet glow intensifies (0.3→0.8), energy note fades in |
| Onset | 0.36–0.41 | NENL flash (sine pulse), tail at max extension |
| Expansion | 0.41–0.55 | Flow particles burst earthward (color orange→yellow), discharge note appears, "Substorm" label fades in, tail retracts (70→50) |
| Recovery | 0.55–0.73 | Aurora brightens (N+S ellipses expand rx 8→14), "Substorm" label fades out |
| Quiet | 0.73–1.0 | Return to baseline, aurora fades, all notes gone, plasma sheet glow back to 0.4 |

Per-frame updates inside substormLoop:
- `mso-substorm` group opacity → 1
- Magnetopause path recomputed with `breathAmp` + `tailLen`
- Bow shock path recomputed
- Plasma sheet gap modulated
- NENL opacity (sine pulse during Onset)
- Flow particles: Growth=accumulate tailward, Expansion=burst earthward
- Plasma sheet stroke opacity + width (glow intensifies during Growth)
- Aurora N/S opacity + rx (brighten during Recovery)
- Phase label text (Growth/Onset/Expansion/Recovery/Quiet)
- Substorm label opacity
- Energy note + discharge note opacity
- Moon orbit continues
- Wind particles continue with deflection (using substorm's breathAmp for MP radius)
- Wind label repositioned to `(1030, 350)` with gentle pulse
- Scale bar: fixed `Time: 245×` and `127k km` during substorm view
- `requestAnimationFrame(substormLoop)` for next frame

### 2. Modify Completion Handler

Replace the Subtask A completion (simple pause at t>=1.0) with:

```js
if(t >= 1.0 && !openDone){
  openDone = true;
  playBtn.innerHTML = '&#9654;';
  for(var i=0;i<heroParticles.length;i++) heroParticles[i].el.setAttribute('opacity','0');
  document.getElementById('mso-wind-label').setAttribute('opacity','0');
}
if(t < 1.0 && running){
  requestAnimationFrame(msUpdate);
} else if(openDone && running){
  substormStart = 0;
  requestAnimationFrame(substormLoop);
}
```

### 3. One Cycle Then Auto-Pause

The tutorial loops substormLoop forever. For the book: after ONE complete cycle (22s), auto-pause and return to poster frame. Add at the top of substormLoop:

```js
if(substormCycleCount >= 1){
  running = false;
  container.classList.remove('ms-playing');
  playBtn.innerHTML = '&#9654;';
  resetState();
  return;
}
```

And increment `substormCycleCount` when `ph` wraps past 1.0:

```js
var prevPh = lastSubstormPh || 0;
if(ph < prevPh) substormCycleCount++;
lastSubstormPh = ph;
```

Add `var substormCycleCount=0, lastSubstormPh=0, substormStart=0;` near the top of the IIFE.

### 4. Update resetState

Add to the existing `resetState()` function:
```js
document.getElementById('mso-substorm').setAttribute('opacity','0');
document.getElementById('mso-wind-label').setAttribute('x','700');
document.getElementById('mso-aurora-label').setAttribute('opacity','0');
substormStart = 0;
substormCycleCount = 0;
lastSubstormPh = 0;
openDone = false;
for(var i=0;i<frontWindEls.length;i++) frontWindEls[i].el.setAttribute('opacity','0');
for(var i=0;i<flowParts.length;i++) flowParts[i].el.setAttribute('opacity','0');
for(var i=0;i<heroParticles.length;i++){
  heroParticles[i].el.setAttribute('opacity','0');
  heroParticles[i].phase = 'approach';
}
```

### 5. Update Play/Pause Toggle

When resuming after camera journey is done (openDone=true), resume substormLoop instead of updateOpen:

```js
function msPlay(){
  if(running) return;
  running = true;
  container.classList.add('ms-playing');
  playBtn.innerHTML = '&#9208;';
  animStart = null;
  if(openDone) requestAnimationFrame(substormLoop);
  else requestAnimationFrame(msUpdate);
}
```

### 6. Progress Bar

Update progress to span the full ~70s (48s camera + 22s substorm):
- During camera (t 0→1): progress = `t * (48/70)` = 0–68.6%
- During substorm (ph 0→1): progress = `0.686 + ph * (22/70)` = 68.6–100%

## ES5 Translation

Same rules as Subtask A. No `const`, `let`, arrows, template literals, `for...of`.

## Verify

```bash
cd ~/software/relinquishment && make html 2>&1 | tail -10
```

Open in browser. Verify:
1. Camera journey plays as before (Subtask A)
2. At camera end: transitions smoothly to substorm view
3. Growth phase: tail stretches visibly, plasma sheet thins, flow particles accumulate, glow intensifies, "Energy accumulates..." text appears
4. Onset: NENL flashes (red-orange ellipse)
5. Expansion: flow particles burst earthward (color shifts), "Substorm" label appears, "...discharges as a substorm" text
6. Recovery: aurora ellipses brighten at poles, substorm label fades
7. Quiet: return to baseline
8. After one cycle: auto-pauses, returns to poster frame
9. Can replay from beginning (full camera + substorm again)
10. Progress bar fills continuously over ~70s
11. No console errors

## Do NOT

- Modify SVG markup (Subtask A already placed all elements)
- Change camera keyframes or narration
- Change scale bar computation (stays fixed during substorm at 245× / 127k km)
- Change any other code in preprocess.py outside the IIFE
- Loop substorm forever (one cycle only)

## Report

Confirm: substorm cycle runs with all 5 phases visible, aurora brightens, NENL flashes, flow burst earthward, phase labels cycle, auto-pauses after one cycle. Note total animation duration.
