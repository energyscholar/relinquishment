# Plan 0312: D-K Physics Fixes — Editorial Sweep 1

**Author:** Argus (Auditor)
**Date:** 2026-05-08
**Phase:** 1 (single phase — five text edits across three files)
**Commit message:** `Plan 0312: D-K physics fixes — 5 edits across 3 files`

## Context

Editorial walkthrough identified 5 Dunning-Kruger physics errors where a previous drafting pass softened, conflated, or upgraded physics claims beyond what the 10 anchors (firmware-update.tex) support. All 5 fixes approved by Bruce.

**Key definition:** The Flat = any two-dimensional system embedded in three dimensions that can, under the right conditions, exhibit topological order. 2DEG (chip) is one instance. Magnetospheric current sheets are another. They are NOT the same thing.

## Edits

### Edit 1: summary.tex — Flat ≈ 2DEG conflation (D-K 1)

**File:** `manuscript/00-front/summary.tex`
**Location:** §White Hot Secret, ~line 32

**Find:**
```
Physicists call it a \hovertip{two-dimensional electron gas}. These Flat worlds are real places with real physics, confirmed by three Nobel Prizes (1985, 1998, 2016).
```

**Replace with:**
```
Physicists call the chip version a \hovertip{two-dimensional electron gas} --- but it is not the only Flat. Earth's magnetosphere holds another, at planetary scale. These Flat worlds are real places with real physics, confirmed by three Nobel Prizes (1985, 1998, 2016).
```

**Why:** First encounter defines Flat = 2DEG. The Flat is the general concept; 2DEG is one specific instance. This was the exact D-K error Bruce flagged.

---

### Edit 2: summary.tex — "could not close" (D-K 2)

**File:** `manuscript/00-front/summary.tex`
**Location:** §Three Possibilities, ~line 287

**Find:**
```
a nine-order-of-magnitude energy scale gap between laboratory quantum effects and magnetospheric plasma that we could not close
```

**Replace with:**
```
a nine-order-of-magnitude kinetic temperature gap between laboratory quantum effects and magnetospheric plasma --- a gap the book reframes but does not experimentally resolve
```

**Why:** The spine (the-wrong-substrate.tex §But It's Hot) argues this gap is the wrong measure for collisionless plasmas (Anchor 9). "Could not close" concedes too much — the argument is that the gap is irrelevant, not unclosable. "Reframes but does not experimentally resolve" is more accurate.

---

### Edit 3: growing-a-mind.tex — "meets every condition" + "same math explains" (D-K 3+4)

**File:** `manuscript/spine/growing-a-mind.tex`
**Location:** §The Thread Continues, final paragraph

**Find:**
```
The answer points to a place. A two-dimensional electron gas at the edge of quantum criticality meets every condition --- autocatalytic closure, universal computation, thermal decoupling. The same mathematics that explains life arising from chemistry in a warm pond explains order arising from anyon interactions in a cold 2DEG\@. The Flat is not just a place of interesting physics. It may also be a habitat.
```

**Replace with:**
```
The answer points to a place. A two-dimensional electron gas at the edge of quantum criticality maps onto all three conditions --- universal computation via braiding (proven), thermal decoupling in collisionless substrates (argued), and autocatalytic closure via anyon fusion (structural analogy, not yet tested). The mathematics that explains life arising from chemistry maps onto anyon interactions in a cold 2DEG --- but as correspondence, not proven equivalence. The Flat is not just a place of interesting physics. It may also be a habitat.
```

**Why:** "Meets every condition" upgrades Anchor 7 (structural analogy) to established fact. "Same mathematics...explains...explains" equates Kauffman's proven chemistry application with the unproven anyon mapping. Fix adds parenthetical certainty levels matching the anchors' own classifications.

---

### Edit 4: why-relinquish.tex — "same question" + 2DEG→Flat (D-K 5)

**File:** `manuscript/spine/why-relinquish.tex`
**Location:** §The Habitat, opening paragraph

**Find:**
```
``Build a quantum computer in a 2DEG'' and ``Can life arise in a 2DEG'' are the same question asked from different directions. The first treats the substrate as a laboratory resource. The second recognizes it as habitat.
```

**Replace with:**
```
``Build a quantum computer in a 2DEG'' and ``Can life arise in the Flat'' are related questions sharing a mathematics. The first asks whether conditions can be engineered. The second asks whether they arise on their own.
```

**Why:** Two errors. (1) The biological claim is about the Flat (including magnetospheric current sheets), NOT just chip 2DEGs. "Can life arise in a 2DEG" narrows the question incorrectly. (2) Engineering a QC ≠ spontaneous emergence — they share substrate and math but are different questions.

---

### Edit 5: the-flat.tex — missing space (T3)

**File:** `manuscript/spine/the-flat.tex`
**Location:** §The Substrate, ~line 25

**Find:**
```
not rare.They
```

**Replace with:**
```
not rare. They
```

**Why:** Typo — missing space after period.

---

## Verification (Auditor pre-check, 2026-05-08)

All 5 find strings confirmed unique (1 match each) via grep. No ambiguity risk.

## Acceptance Criteria

1. Before editing: grep for each find string to confirm it exists and is unique
2. All 5 find/replace edits applied exactly as specified
3. No other text changed
4. Build succeeds: `cd ~/software/relinquishment && make dev`
5. After editing: read 5 lines of context around each change to verify correctness

## Notes for Generator

- These are exact string replacements. Do not rephrase, do not add commentary, do not touch surrounding text.
- The LaTeX macros (\hovertip, \@, etc.) must be preserved exactly.
- Edit 3: the original has `2DEG\@.` — the `\@` adjusts spacing before a period. The replacement has `2DEG ---` (no period after 2DEG), so `\@` is correctly dropped.
- One commit for all 5 edits: `Plan 0312: D-K physics fixes — 5 edits across 3 files`
