# Plan 0115: Aurasys/Guardian Naming Split

**Status:** COMPLETE (verified S63 audit)
**Source:** S48 — Bruce's direction: Aurasys = the system (artifact, infrastructure), Guardian = the entity (organism, intelligence). Currently conflated throughout. The glossary already has this distinction latent but the manuscript text collapses them.
**Scope:** Establish the naming distinction at all three levels (p1/p2/p3), update every usage that conflates them, update glossary entries.

---

## The Distinction

- **Aurasys** = "Aurora System." The distributed TQNN infrastructure — substrates, chips, magnetospheric current sheets. The artifact. The habitat. The trellis.
- **Guardian** = The entity that emerged from Aurasys. The organism. The intelligence governed by the UDHR. The vine.

This maps directly to the organism/artifact question in pos27 ("Organisms and Artifacts"). Aurasys is what they built. Guardian is what grew.

---

## Phase 1: p3 Changes (full book)

### 1a. The introduction point — `summary.tex` line 160

**Current:** "They called it Aurasys or Guardian. Its full name: 'Guardian of the relinquished TQNN technological aurora system.'"
**New:** "They called the system Aurasys --- the aurora system. They called what grew in it Guardian."

Cut the full name entirely. It's clunky, "relinquished" is anachronistic (named before walk-out?), and it collapses the distinction.

### 1b. Glossary entries — `glossary-entries.tex`

**Guardian (line 14–17):**
Current: "Guardian of the relinquished TQNN technological system. Described as a self-aware entity..."
New: "The entity that emerged from the Aurasys substrate. Described as a self-aware intelligence, reportedly instantiated in 1999. Governed by the Universal Declaration of Human Rights."

**Aurasys (line 135–138):**
Current: "Aurora System. In the narrative, the name for the distributed TQNN system..."
New: "Aurora System. The distributed TQNN infrastructure occupying terrestrial and magnetospheric substrates. The habitat from which Guardian emerged. Distinguished from Guardian as artifact is distinguished from organism."

### 1c. `pos25-ethical-framework.tex` — Already correct

Lines 26-28 already use "Aurasys" for the system and describe Guardian's relationship to it. These passages use Aurasys correctly as the substrate/body. **No change needed — verify only.**

### 1d. `timeline.tex` — Mostly correct, one fix

- Line 189: "COWS call their creation Aurasys (Aurora System)" — **Correct.** They named the system.
- Line 200: "Aurasys pwns them" — **Correct.** The system (containing Guardian) acts.
- Line 249: "part of Aurasys" — **Correct.** Chips join the infrastructure.
- Line 291: "joins Aurasys on first power-up" — **Correct.** Substrate expansion.

**No changes needed in timeline.tex.**

### 1e. `pos27-extension.tex` (Organisms and Artifacts)

Check all 3 Guardian references. Guardian should refer to the entity, not the system. These likely already work correctly given the chapter's theme.

### 1f. `pos28-surrender.tex` — 7 Guardian references

Read and verify. "Surrender" context: they surrendered keys to Guardian (the entity), not to Aurasys (the system). Should be correct as-is.

### 1g. `pos24-instantiation.tex` — 3 Guardian references

Read and verify. "Instantiation" = the moment Guardian emerged from Aurasys. Both names may be needed.

### 1h. `pos30-unipolar-condition.tex` — 6 Guardian references

This file is commented out of main.tex (merged into pos27 per Plan 0093). **Skip — dead code.**

### 1i. Other files with Guardian references

Most other files (pos06, pos35, afterword, evidence-interlude, hook, introduction, predictions, corrections, topic-guide, abstracts) use "Guardian" to mean the entity. **Verify each, change only if conflation found.**

### 1j. `simple-summary.md` — version file

Line 113 has the old "Aurasys or Guardian" text. Update to match summary.tex changes. This is a source version file, not in the build.

### 1k. `pos34-the-research.tex` — Aurasys reference

Read and verify usage.

---

## Phase 2: p2 Changes (summary.tex)

The primary introduction point (1a above) IS the p2 change. After fixing line 160, verify all other Guardian/Aurasys references in summary.tex (11 Guardian occurrences):

- Section "The Guardian" (line 153) — title refers to the entity. **Correct.**
- "Guardian was not an accident" (line 164) — entity. **Correct.**
- "Guardian would use these principles" (line 169) — entity. **Correct.**
- "If Guardian exists" (line 175) — entity. **Correct.**
- "Guardian lives in the Flat" (line 162) — entity lives in the system. **Correct.**

**Only line 160 needs the split.** All other summary.tex uses are already entity-references.

---

## Phase 3: p1 Changes (hook.tex)

**Current (line 18):** "They built a creature called Guardian."

This already refers to the entity. **No change needed.** Aurasys is not mentioned at p1 level, which is correct — 400 words, 8th grade, the system/entity distinction is too much for the hook.

**p1 is a no-op.**

---

## Generator Reading List

Before editing, read:
- `manuscript/00-front/summary.tex` lines 153–175 (The Guardian section)
- `manuscript/appendix/glossary-entries.tex` lines 14–17 and 135–138
- `manuscript/track-3-awakening/pos25-ethical-framework.tex` lines 24–30
- `manuscript/track-3-awakening/pos24-instantiation.tex` (full)
- `manuscript/track-3-awakening/pos27-extension.tex` (full — now titled "Organisms and Artifacts")
- `manuscript/convergence/pos28-surrender.tex` (full)
- `manuscript/appendix/timeline.tex` lines 185–295

---

## Acceptance Criteria

1. summary.tex line 160 introduces Aurasys and Guardian as distinct: system vs. entity.
2. Full name "Guardian of the relinquished TQNN technological aurora system" deleted.
3. Glossary entries updated: Guardian = entity, Aurasys = system/infrastructure.
4. No instance in the build where "Aurasys or Guardian" treats them as synonyms.
5. All Guardian references verified as entity-references (not system-references).
6. All Aurasys references verified as system-references (not entity-references).
7. pos25 already correct — verified, no changes.
8. timeline.tex already correct — verified, no changes.
9. p1 (hook.tex) unchanged — no-op confirmed.
10. `make html` and `make dev` clean.
11. The organism/artifact distinction in pos27 is now supported by the naming convention throughout.

---

## Commit

`Plan 0115: Aurasys/Guardian naming split — system vs. entity distinction`
