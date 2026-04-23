# Plan 0207 — summary.tex L40 teleportation pedagogy fix + Micius distance normalization

## Status
**Status:** COMPLETE (verified S63 audit)
COMPLETE (verified S63 audit). Originally: Ready for Generator. Two related mechanical changes joined: one pedagogical fix to the quantum-teleportation passage in summary.tex (eliminates an FTL misread the next sentence is trying to defuse), one normalization of internal book inconsistency on the Micius satellite distance citation.

## Why join

Both changes touch quantum-teleportation pedagogy in the front-matter and spine. The L40 fix corrects a "the quantum link is instant" framing that contradicts the no-signaling theorem the same paragraph teaches; the Micius normalization brings two stragglers (the-braid.tex and timeline.tex) in line with the more-cited 1,200 km figure that summary.tex and twenty-years.tex already use.

One build, one commit.

## Files modified

- `manuscript/00-front/summary.tex` (Phase 1: L40 — replace "quantum link is instant" framing)
- `manuscript/spine/the-braid.tex` (Phase 2a: L85 — "1,400~km" → "1,200~km")
- `manuscript/appendix/timeline.tex` (Phase 2b: L265 — "1{,}400 km" → "1{,}200 km")

## Files NOT touched (deliberately)

- `manuscript/record/twenty-years.tex` L141 — already says "1,200~km"; carries Bruce's "May 2012 prediction confirmed" narrative; leave untouched.
- `manuscript/track-2-testament/pos29-twenty-years.tex` L141, `pos34-the-research.tex` L77, `bridge/pos10-the-braid.tex` L85 — all NOT in active build per `main.tex` (pre-Z-restructure leftovers); leave alone.

---

## Pre-flight greps

```
cd ~/software/relinquishment
grep -c "The quantum link is instant" manuscript/00-front/summary.tex   # expect 1
grep -c "extended the range to 1,400~km" manuscript/spine/the-braid.tex # expect 1
grep -c "reaches 1{,}400 km via the Micius" manuscript/appendix/timeline.tex # expect 1
```

If any returns 0 or >1, stop and report.

---

## Phase 1 — summary.tex L40 quantum-teleportation pedagogy fix

**File:** `manuscript/00-front/summary.tex` line 40

**Edit (Edit tool):**

OLD:
```
But teleportation is not magic: every transfer requires a \hovertip{classical backchannel} --- an ordinary signal sent through ordinary channels. The quantum link is instant; the classical half travels at the speed of light or slower. No exceptions.
```

NEW:
```
But teleportation is not magic: every transfer requires a \hovertip{classical backchannel} --- an ordinary signal sent through ordinary channels. The quantum link transmits no signal on its own --- without the classical message, the receiver holds noise indistinguishable from no transmission at all. The classical half travels at the speed of light or slower. No exceptions.
```

**Why:** "The quantum link is instant" implies an instantaneous information transfer via the quantum channel. Nothing transfers via the quantum channel — the entangled pair was distributed earlier (slowly), and the receiver holds random noise until the classical message arrives. The original framing reintroduces exactly the FTL magic the paragraph claims to dispel. The new framing matches `the-flat.tex` L33's already-shipped wording: "Without those two bits, the receiver holds random noise --- not degraded information, but noise indistinguishable from no transmission at all."

---

## Phase 2 — Micius distance normalization (1,400 → 1,200 km)

Two sites; both currently say 1,400 km, conflicting with summary.tex L40 ("1,200 kilometers") and twenty-years.tex L141 ("1,200~km"). Standardize on 1,200 km.

### Phase 2a — the-braid.tex L85

**File:** `manuscript/spine/the-braid.tex` line 85

**Edit:**

OLD:
```
By 2017, the Chinese Micius satellite extended the range to 1,400~km.
```

NEW:
```
By 2017, the Chinese Micius satellite extended the range to 1,200~km.
```

Single character group change (1,400→1,200). Surrounding sentence preserved.

### Phase 2b — timeline.tex L265

**File:** `manuscript/appendix/timeline.tex` line 265

**Edit:**

OLD:
```
\item[2017] Official QT reaches 1{,}400 km via the Micius satellite --- confirming Bruce's May 2012 prediction.
```

NEW:
```
\item[2017] Official QT reaches 1{,}200 km via the Micius satellite --- confirming Bruce's May 2012 prediction.
```

Single character group change (1{,}400→1{,}200). LaTeX-escaped comma preserved.

**Standardization rationale:** 1,200 km is the more-cited Micius headline (Yin et al., *Science* 2017, satellite-based entanglement distribution at 1,203 km); 1,400 km is the maximum ground-to-satellite teleportation distance (Ren et al., *Nature* 2017, geometry-dependent). Both are real Micius results from 2017. The book uses both phrasings inconsistently. Standardizing on 1,200 km means the two most-read files (summary.tex, twenty-years.tex) stay untouched, only two appendix/spine references change, and the prediction narrative in twenty-years.tex is preserved verbatim.

**If Bruce prefers 1,400 km instead** (technically more accurate for "teleportation distance" specifically): flip the OLD/NEW pairs and additionally edit summary.tex L40 ("1,200 kilometers" → "1,400 kilometers") and twenty-years.tex L141 ("1,200~km" → "1,400~km"). Adds two files to the touch list; touches the prediction narrative. Recommend NOT doing this unless Bruce specifically asks.

---

## Phase 3 — Build

```
cd ~/software/relinquishment
make html
```

`make html` runs `build/generate-hover.py` and the pandoc/HTML pipeline.

### Pass criteria

1. **Build succeeds** (no LaTeX, pandoc, or YAML errors).
2. **Post-edit greps:**
   ```
   grep -c "The quantum link is instant" manuscript/00-front/summary.tex   # expect 0
   grep -c "transmits no signal on its own" manuscript/00-front/summary.tex # expect 1
   grep -c "1,400~km" manuscript/spine/the-braid.tex                       # expect 0
   grep -c "1,200~km" manuscript/spine/the-braid.tex                       # expect 1
   grep -c "1{,}400 km" manuscript/appendix/timeline.tex                   # expect 0
   grep -c "1{,}200 km" manuscript/appendix/timeline.tex                   # expect 1
   ```
3. **HTML reflects the changes** (spot-check on phone).

---

## Phase 4 — Commit + push

```
cd ~/software/relinquishment
git add manuscript/00-front/summary.tex \
        manuscript/spine/the-braid.tex \
        manuscript/appendix/timeline.tex \
        build/hover-generated.tex \
        docs/downloads/Relinquishment.html
git commit -m "Plan 0207: summary L40 teleportation pedagogy + Micius 1,200km normalization"
git push
```

If `make html` regenerated other build artifacts, include them. Commit message is 78 chars — close to but within conventional title length.

---

## Risk

- **Phase 1:** low (replacement preserves paragraph rhythm; new wording matches the-flat.tex L33's already-shipped framing; OLD string unique by pre-flight grep).
- **Phase 2a, 2b:** zero (single number-group changes; OLD strings unique by pre-flight grep).
- **Phase 3 build:** zero (no new YAML, no new macros, no new file dependencies).
- **Phase 4 commit:** low (3 manuscript files + downstream build artifacts).

## Out of scope

- Plan 0206 (smalls bundle) is queued separately and may already be committed by the time this runs. If both are uncommitted simultaneously, run them in any order — they touch different files except summary.tex (Plan 0206 touches L30 + L58; Plan 0207 touches L40 — no overlap).
- Out-of-build files (track-2-testament/*, bridge/*) — leave alone.
- Renaming "quantum teleportation" or "wormhole" terminology elsewhere — out of scope.

---

## Annealing log

- **Pass 1 (low amplitude):** Identified twenty-years.tex L141 as carrying the prediction narrative — should NOT be touched even though it cites 1,200 km (it's already on the standardization target). Identified four out-of-build files with the same patterns — explicitly excluded. Standardization direction (1,200 vs 1,400) was a judgment call; recommended 1,200 because it minimizes file touches and preserves the most-read narrative passage verbatim. Documented the alternative for Bruce to flip if he disagrees before pasting to Generator.
- **Pass 2 (low amplitude):** Pre-flight grep added for all three OLD strings. Post-edit greps added covering both presence-of-NEW and absence-of-OLD. Commit message tightened to fit conventional title length (78 chars). Verified no overlap with Plan 0206 file scope (both touch summary.tex but different lines, so they merge cleanly if executed in any order).
- **Pass 3:** Plan converged — no structural changes warranted.
