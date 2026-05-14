# Plan 0333: Hasslacher Correction → "What I Got Wrong"

**Status:** Ready for Generator
**PTL:** (none — small fix)
**Files:** `build/hover-definitions.yaml`, `manuscript/appendix/corrections.tex`
**Problem:** The `lattice dynamics` tooltip contains an 80-word correction narrative. Tooltips should be ≤15 words. The correction belongs in the Corrections chapter.
**Solution:** Replace tooltip with brief definition. Add error #8 to corrections.tex. Clean up soliton tooltip.

---

## Context

In `pos29-twenty-years.tex` line 101, the text reads:
```
Hasslacher to \hovertip{lattice dynamics}
```

The tooltip currently tells the story of a twenty-year mistake. That story is important — it belongs in the book — but not in a tooltip.

## Changes

### 1. Replace `lattice dynamics` tooltip (hover-definitions.yaml line 502)

Current (80 words, correction narrative):
```yaml
lattice dynamics: "Correction: until 2026, this line read 'Hasslacher to solitons.' The author spent twenty years thinking solitons were Hasslacher's key contribution. They weren't. Hasslacher's lattice gas automata — how discrete crystal structures produce collective wave behavior — led to phonon physics: the mechanism by which a quantum system in the Flat talks to the classical world. Solitons were a twenty-year wild goose chase. The real trail was phonons all along."
```

Replace with:
```yaml
lattice dynamics: "How discrete crystal structures produce collective wave behavior. Hasslacher's lattice gas automata led to phonon physics — the mechanism by which a quantum system in the Flat talks to the classical world. See Corrections #8 for the twenty-year soliton detour."
```

### 2. Trim soliton tooltip (hover-definitions.yaml line 299)

Current (last sentence bleeds into correction territory):
```yaml
soliton: "A wave that holds its shape — doesn't spread out or break apart. Self-reinforcing. Found in oceans, fiber optics, and plasma. One of the first physics concepts in the mentorship sequence. Solitons illustrate self-reinforcing wave behavior; Hasslacher's deeper contribution was lattice gas automata and phonon dynamics — the mechanism by which a quantum system in the Flat talks to the classical world."
```

Replace with:
```yaml
soliton: "A wave that holds its shape — doesn't spread out or break apart. Self-reinforcing. Found in oceans, fiber optics, and plasma. One of the first physics concepts in the mentorship sequence."
```

The Hasslacher correction now lives in one place (corrections.tex), not spread across two tooltips.

### 3. Add error #8 to corrections.tex (before line 26)

Insert before `\vspace{1cm}` (the "What these errors tell you" block):

```latex
\textbf{8. Hasslacher's contribution: solitons vs.\ phonons.} For twenty years I believed Hasslacher's key contribution to the convergence was solitons --- self-reinforcing waves. I was wrong. His lattice gas automata work addressed something more fundamental: how discrete structures in a crystal lattice produce collective wave behavior. The key physics is phonons --- quantized lattice vibrations. Electron-phonon coupling bridges the quantum 2DEG to classical electronics; phonon-photon coupling bridges the chip to electromagnetic radiation. The mechanism by which a quantum system in the Flat talks to the classical world. Solitons were a twenty-year wild goose chase. The real trail was phonons all along. I discovered this error in 2026 while writing this book. The corrected text appears in ``Twenty Years'' and ``The Braid.''

```

### 4. Update meta-analysis count (line 28)

The sentence "Every error listed above is peripheral" still applies — no change needed to the meta-analysis text. The new error is peripheral (misidentifying which Hasslacher contribution mattered, not misidentifying Hasslacher's relevance).

## Verify

```bash
cd ~/software/relinquishment && make html 2>&1 | tail -10
python3 build/verify-deep-links.py
```

Then in browser:
1. Hover over "lattice dynamics" in Twenty Years chapter — should show brief definition + "See Corrections #8"
2. Hover over "soliton" anywhere — should show clean definition, no correction narrative
3. Navigate to Corrections chapter — error #8 visible between #7 and "What these errors tell you"

## Do NOT

- Change the manuscript text at pos29-twenty-years.tex line 101 (it already says "lattice dynamics", not "solitons")
- Change the-braid.tex content (the phonon text there is already correct)
- Modify hover-generated.tex directly (it's generated from YAML on build)
- Add or remove any other tooltips
- Change numbering of errors 1–7

## Commit

`Plan 0333: Hasslacher soliton correction → Corrections chapter + clean tooltips`
