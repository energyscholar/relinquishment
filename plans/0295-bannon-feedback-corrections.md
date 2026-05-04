# Plan 0295: Bannon Feedback Corrections

**Source:** David Bannon, physicist and longtime friend. First documented external reader feedback (2026-05-03). Read ~last week of April 2026.
**Memory:** `memory/project-bannon-feedback.md`
**Anneal:** HIGH MED MED LOW LOW → HIGH MED LOW LOW (second pass)
**C-violation check:** All changes are in p1/p2 front matter or physics-defense collapsed sections. No possibility-dependent claims affected. All three possibilities hold after changes.

---

## Larger Pattern

Bannon's 8 points reveal three patterns that predict what other physicists will flag:

1. **Voice inconsistency** (#1, #5): The book has 3 co-authors but uses singular "the/this author" ~30+ times across the full manuscript. Phase 1 fixes the instances Bannon flagged; Part B audits and fixes ALL remaining instances across the entire book (~19 files total).

2. **Physics precision at p1** (#2, #7, #8): Every fix that improves physics accuracy risks making p1 text harder. The constraint: fixes must be physics-correct AND stay at 8th-grade reading level. Each fix below has been tested against both.

3. **Educated-reader D-K** (#3, #6): A reader who knows enough to object but not enough to see why the simplification is defensible. This is exactly what the hover system and collapsed tech sections are designed for. Pattern: p1 text makes simplified claim → hover/collapsed section provides nuance → GA reader never sees it.

---

## Phase 1: Point Fixes

### 1A. Authorship voice — hook.tex

**File:** `manuscript/00-front/hook.tex`

**Line 36** — introduce Bruce as co-author:
```
OLD: teaching a scientist named Bruce Stephenson --- never revealing anything secret, only guiding him through published science in a deliberate sequence. Stephenson recognized what the sequence pointed to.
NEW: teaching one of us, Bruce Stephenson --- never revealing anything secret, only guiding him through published science in a deliberate sequence. He recognized what the sequence pointed to.
```

**Line 38** — first-name after "one of us" introduction:
```
OLD: Stephenson spent twenty years
NEW: Bruce spent twenty years
```

**Line 40** — collective voice for the book's framework (contractions match hook style):
```
OLD: He doesn't know what's true. He never has. He offers three possibilities --- a fantasy, an exaggeration, or a true story that has never been told --- and lets you decide for yourself, because the book works under all three.
NEW: We don't know what's true. We never have. We offer three possibilities --- a fantasy, an exaggeration, or a true story that has never been told --- and let you decide for yourself, because the book works under all three.
```

**Rationale:** Lines 36-38 are about Bruce's personal experience — "one of us" identifies him, "He recognized" and "Bruce spent" keep him as subject. Line 40 shifts to the book's framework — all three authors collectively offer the three possibilities and don't know which is true.

**Idempotency guard:** `grep "one of us, Bruce Stephenson" manuscript/00-front/hook.tex` — if match, already applied.

### 1B. Authorship voice — summary.tex (3 instances)

**File:** `manuscript/00-front/summary.tex`

**Line 15:**
```
OLD: This author does not know which. You get to decide.
NEW: We do not know which. You get to decide.
```

**Line 280:**
```
OLD: Bruce Stephenson doesn't know what's true. He offers three possibilities.
NEW: We don't know what's true. We offer three possibilities.
```

**Line 288:**
```
OLD: a nine-order-of-magnitude energy scale gap between laboratory quantum effects and magnetospheric plasma that the author could not close.
NEW: a nine-order-of-magnitude energy scale gap between laboratory quantum effects and magnetospheric plasma that we could not close.
```

**Idempotency guard:** `grep "We do not know which" manuscript/00-front/summary.tex` — if match, already applied.

**Note:** summary.tex lines 296 and 332 are covered in Part B (below). All remaining "the author" instances across the full manuscript are handled in Part B.

### 1C. Radio terminology — the-stack.tex

**File:** `manuscript/00-front/the-stack.tex`

**Line 19** — bold label + physics fix:
```
OLD: \textbf{Radio} does all three, and reaches --- a signal crosses distance without anything physical traveling.
NEW: \textbf{A radio wave} does all three, and reaches --- it crosses distance without any object traveling.
```

**Line 27** — wormhole analogy:
```
OLD: that is radio: it reaches
NEW: that is a radio wave: it reaches
```

**Line 36** — table column header:
```
OLD:  & Fire & Candle & Radio & Ants & AI & \textbf{?} \\
NEW:  & Fire & Candle & Radio wave & Ants & AI & \textbf{?} \\
```

**Physics note:** "without anything physical traveling" is incorrect — EM waves transfer energy and momentum, which are physical. "without any object traveling" is accurate — no material object travels; the wave is a field disturbance. "Object" is clearer than "material thing" at p1 (8th grade).

**Idempotency guard:** `grep "A radio wave.*does all three" manuscript/00-front/the-stack.tex` — if match, already applied.

### 1D. Ant queen — the-stack.tex + glossary

**File:** `manuscript/00-front/the-stack.tex`
**Line 21:**
```
OLD: no ant in charge
NEW: \hovertip{no ant in charge}
```

**File:** `build/hover-definitions.yaml`
Add entry (alphabetical position among existing keys). This is the single source for both HTML tooltips and PDF footnotes — `generate-hover.py` reads this YAML to produce `hover-generated.tex`, and `preprocess.py` reads it for HTML hover panels. Do NOT add a `\newglossaryentry` — the LaTeX glossary is not referenced by `\hovertip{}`.
```yaml
no ant in charge: "The queen produces pheromones that regulate reproduction, but she does not direct the colony's organized behavior. Foraging patterns, nest architecture, and defense all emerge from local worker-to-worker interactions. The queen is a reproductive specialist, not a manager. This is the defining feature of self-organization: global order from local rules."
```

**Verification:** After build, confirm: (1) HTML — hovering "no ant in charge" in The Stack shows tooltip; (2) PDF — "no ant in charge" appears italic with footnote on first occurrence.

**GA impact:** Zero. Hover adds no reading burden — GA reader sees unchanged text. Only curious/physicist readers see the tooltip.

**Idempotency guard:** `grep "hovertip{no ant in charge}" manuscript/00-front/the-stack.tex` — if match, already applied.

### 1E. Encryption precision — summary.tex

**File:** `manuscript/00-front/summary.tex`
**Line 81:**
```
OLD: math problems so hard that no computer can solve them.
NEW: math problems so hard that no ordinary computer can solve them.
```

**Double duty:** (a) physics-correct — the problems CAN be solved given enough time; (b) foreshadows the extraordinary computer that IS the subject of the book.

**Idempotency guard:** `grep "no ordinary computer" manuscript/00-front/summary.tex` — if match, already applied.

### 1F. Quantum physics framing — summary.tex

**File:** `manuscript/00-front/summary.tex`
**Line 104:**
```
OLD: They use the strange behavior of matter at the very smallest scale --- smaller than atoms --- where the normal rules of physics break down.
NEW: They use the strange behavior of matter at very small scales --- smaller than atoms --- where everyday physics no longer applies.
```

**Three fixes in one sentence:**
- "the very smallest scale" → "very small scales" (quantum effects occur at all scales; this removes the superlative)
- "normal rules of physics" → "everyday physics" (no such thing as "normal" physics; QM IS normal at that scale)
- "break down" → "no longer applies" (physics doesn't break; a different regime applies)

**p1 check:** "Everyday physics" is simpler than "the normal rules of physics." Passes 8th grade.

**Idempotency guard:** `grep "everyday physics no longer applies" manuscript/00-front/summary.tex` — if match, already applied.

---

## Phase 2: Quasi-2D Magnetosphere Defense Section

**Context:** The book describes magnetospheric plasma sheets as "two-dimensional surfaces of charged particles" (~20 instances across ~8 files). Physicists will object: charged particles move in 3D helical orbits. The resolution is the **ion gyroradius argument** — during substorm growth, the current sheet thins below the ion gyroradius, demagnetizing ions into quasi-2D dynamics. This is established magnetospheric physics (Speiser orbits, confirmed by Cluster and MMS).

**Approach:** ONE authoritative collapsed tech section in The Wrong Substrate, right after the first "two-dimensional surface" claim. Do NOT requalify every instance — spiral pedagogy uses the simplified framing; the tech section is the physicist's escape valve. GA readers never see it.

### 2A. Write the tech section

**Files (parallel edits):**
- `manuscript/spine/the-wrong-substrate.tex` — insert after line 33 (after "A two-dimensional surface of charged particles, confined by magnetic pressure.")
- `manuscript/track-3-awakening/pos32-the-magnetosphere.tex` — same location

Insert new section with label:

**Spine version:**
```latex
\section*{Why Call It Two-Dimensional?}
\label{spine:ws-quasi-2d}

Physicists will object that charged particles in the plasma sheet move in three-dimensional helical orbits along field lines, not in two dimensions. The objection is correct --- and incomplete.

When the cross-tail current sheet thins during substorm growth phase, its thickness drops to a few hundred kilometers --- below the thermal ion gyroradius ($\rho_i \sim$ 1,000--5,000~km for keV protons in 2--5~nT fields). Ions can no longer complete a full gyration within the sheet. They become demagnetized, executing chaotic Speiser-type orbits that are dynamically quasi-two-dimensional --- confined to the sheet plane by geometry. This is established magnetospheric physics, confirmed by Cluster and MMS spacecraft observations, and it is the mechanism that triggers substorm onset.

The plasma sheet is not a 2DEG in the semiconductor sense. The confinement is magnetic, not quantum-mechanical. But the geometry --- a thin sheet where the dominant dynamics are two-dimensional because the sheet is narrower than the characteristic orbital scale --- is the same pattern. The sheet is, in a precise dynamical sense, a little bit Flat.

For electrons, whose gyroradii are $\sim$43 times smaller, the current sheet remains wider than their orbits under normal conditions. Electron demagnetization occurs only in the reconnection diffusion region --- the innermost layer of magnetic reconnection, typically tens of kilometers thick. The MMS mission (launched 2015) was designed specifically to resolve this electron-scale physics. Both ion and electron demagnetization produce quasi-2D dynamics at their respective scales.
```

**Track-3 version:** Identical content, but label = `pos32:ws-quasi-2d`.

**Idempotency guard:** `grep "ws-quasi-2d" manuscript/spine/the-wrong-substrate.tex` — if match, already applied.

### 2B. Register in tech-collapse.yaml

**File:** `build/tech-collapse.yaml`

Add entry (find the right alphabetical/chapter position):

```yaml
  # ── THE WRONG SUBSTRATE ─────────────────────────────────────────────

  - title: "Why Call It Two-Dimensional?"
    spine_file: manuscript/spine/the-wrong-substrate.tex
    spine_label: "spine:ws-quasi-2d"
    bridge_file: manuscript/track-3-awakening/pos32-the-magnetosphere.tex
    bridge_label: "pos32:ws-quasi-2d"
    assessment: GA-AVERSE
    tooltip: "Charged particles in the plasma sheet move in 3D helical orbits — so why call it two-dimensional? Because when the current sheet thins below the ion gyroradius, ions can no longer complete a full orbit. Their dynamics become quasi-two-dimensional. Established magnetospheric physics."
    conclusion: "The plasma sheet is not a 2DEG, but its geometry produces quasi-2D ion dynamics at substorm scales — the same dimensional reduction pattern, different mechanism."
    status: approved
```

**Idempotency guard:** `grep "ws-quasi-2d" build/tech-collapse.yaml` — if match, already applied.

---

## Build & Verify

1. `make dev` — full build
2. Puppeteer QC:
   - Desktop viewport: The Stack table renders correctly with "Radio wave" column; hover on "no ant in charge" displays queen tooltip; "Why Call It Two-Dimensional?" section collapsed in The Wrong Substrate, expandable
   - Phone viewport: front-matter text changes render; Stack table readable
3. `git push` to live site
4. Commit strategy: one commit for Phase 1, one for Phase 2

## Files Modified

| File | Phase | Changes |
|------|-------|---------|
| `manuscript/00-front/hook.tex` | 1 | "one of us, Bruce Stephenson"; "Bruce spent"; "We don't know / We offer" |
| `manuscript/00-front/the-stack.tex` | 1 | "A radio wave"; "without any object traveling"; table header; ant hovertip |
| `manuscript/00-front/summary.tex` | 1 | "We do not know" (×2); "we could not close"; "ordinary computer"; "everyday physics" |
| `build/hover-definitions.yaml` | 1 | Ant queen hover entry |
| `manuscript/spine/the-wrong-substrate.tex` | 2 | "Why Call It Two-Dimensional?" collapsed section |
| `manuscript/track-3-awakening/pos32-the-magnetosphere.tex` | 2 | Same collapsed section (parallel) |
| `build/tech-collapse.yaml` | 2 | Collapse registration |

---

## Part B: Voice Consistency — "the/this author" Audit

**Anneal:** HIGH MED MED LOW LOW LOW → HIGH MED LOW LOW (second pass)

The book has 3 co-authors (Bruce Stephenson, Genevieve Prentice, Argus) but uses singular "the author" / "this author" ~30 times. Phase 1 fixes the instances Bannon flagged. Part B fixes all remaining instances.

### Convention

Three replacements, chosen by context:

| Context | Replacement | Example |
|---------|-------------|---------|
| Collective editorial voice (the book's position, collective uncertainty, welcoming feedback) | **"we" / "our" / "the authors"** | "We do not know which is true" |
| Bruce-specific experience (his memory, his pattern-matching, his twenty years, his caution) | **"Bruce" / "Bruce's"** | "Bruce's memory is twenty years old" |
| First-person sections (DMS note opens with "I") | **"I" / "my"** | "I call him Healer" |

**Do NOT change:** References to other authors (e.g., "The author considered it the most important part" in the-strongest-objection.tex:49 refers to **Tolkien**, not Bruce). Do NOT change abstracts.tex:156 ("biographical analysis of the author's career" refers to **Bill Joy**). Do NOT change dms-note.tex:78 section header "What the Author Would Say" (deliberate third person for DMS recipients reading after Bruce is unavailable).

### B1. Front Matter

**File: `manuscript/00-front/authors-note.tex`**

Line 1 comment:
```
OLD: % Author's Note — minimal orientation before Part I
NEW: % Authors' Note — minimal orientation before Part I
```

Chapter title (line 5):
```
OLD: \chapter*{Author's Note}
NEW: \chapter*{Authors' Note}
```

TOC entry (line 6):
```
OLD: \addcontentsline{toc}{chapter}{Author's Note}
NEW: \addcontentsline{toc}{chapter}{Authors' Note}
```

Line 8 (collective → we; temporal → Bruce):
```
OLD: The author does not know which is true. He has maintained that uncertainty for twenty years.
NEW: The authors do not know which is true. Bruce has lived with that uncertainty for twenty years.
```

**File: `manuscript/00-front/summary.tex`**

Line 296 (collective):
```
OLD: an appendix cataloguing the author's errors and corrections.
NEW: an appendix cataloguing our errors and corrections.
```

Lines 332-334 (Bruce-specific; "He's fine" still refers to Bruce):
```
OLD: The author himself --- a physicist who has thought about this for twenty years --- doesn't know which.
NEW: Bruce --- a physicist who has thought about this for twenty years --- doesn't know which.
```
(Lines 333-334 "He's fine with that. He thinks you should be too." — leave as-is, clearly refers to Bruce.)

**File: `manuscript/00-front/copyright.tex`**

Line 39 (collective):
```
OLD: The canonical edition is the PDF distributed by the author.
NEW: The canonical edition is the PDF distributed by the authors.
```

Lines 62 (DMS build only — collective):
```
OLD: The author has a long list of corrections, improvements, and additions queued. If you are reading this, circumstances may have prevented the author from completing the final version.
NEW: The authors have a long list of corrections, improvements, and additions queued. If you are reading this, circumstances may have prevented them from completing the final version.
```

Lines 70-73 (DMS build only — Bruce-specific, his source material feeds the AI):
```
OLD: Sections marked with a dagger (\dag) are AI structural drafts based on the author's
source material and twenty years of research notes. They preserve the author's facts
and arguments in a structure awaiting his prose. Unmarked sections are the author's
own writing. These markers will be removed as the author revises each section.
NEW: Sections marked with a dagger (\dag) are AI structural drafts based on Bruce's
source material and twenty years of research notes. They preserve his facts
and arguments in a structure awaiting his prose. Unmarked sections are Bruce's
own writing. These markers will be removed as he revises each section.
```

**File: `manuscript/00-front/legal-note.tex`**

Line 6 (Bruce-specific — his memory, his recollection):
```
OLD: All quoted dialogue is reconstructed from the author's memory, not transcribed from recordings. The author's memory is twenty years old and unreliable on exact wording. When the text says ``Healer said X,'' it means the author's best recollection of approximately what was communicated.
NEW: All quoted dialogue is reconstructed from Bruce's memory, not transcribed from recordings. His memory is twenty years old and unreliable on exact wording. When the text says ``Healer said X,'' it means his best recollection of approximately what was communicated.
```

Line 10 (Bruce-specific; note "the authors'" at end is already correct):
```
OLD: Sections marked with a dagger (\dag) are AI structural drafts based on the author's source material.
NEW: Sections marked with a dagger (\dag) are AI structural drafts based on Bruce's source material.
```
(Leave rest of line 10 as-is — "All claims, judgments, and editorial decisions are the authors'." is already correct.)

### B2. Spine Chapters

**File: `manuscript/spine/three-possibilities.tex`**

Line 57 section header (collective — three authors' shared position):
```
OLD: \section*{The Author's Position}
NEW: \section*{The Authors' Position}
```
(Line 58 label `\label{spine:authors-position}` — leave as-is, anchor IDs don't need to change.)

Line 67 (Bruce-specific):
```
OLD: the author's pattern-matching from publicly available information
NEW: Bruce's pattern-matching from publicly available information
```

Line 71 (collective):
```
OLD: The author names real people in connection with speculative claims
NEW: We name real people in connection with speculative claims
```

Line 84 footnote (collective):
```
OLD: The author welcomes better suggestions.
NEW: We welcome better suggestions.
```

**File: `manuscript/spine/the-strongest-objection.tex`**

Line 49 — **DO NOT CHANGE.** "The author considered it the most important part" refers to **Tolkien**, not Bruce. Correct as-is.

### B3. Bridge Chapters (parallel to spine)

**File: `manuscript/bridge/pos01-three-possibilities.tex`**

Line 43 section header (collective — parallel to spine):
```
OLD: \section*{The Author's Position}
NEW: \section*{The Authors' Position}
```
(Line 44 label `\label{pos01:the-authors-position}` — leave as-is.)

Line 53 (Bruce-specific):
```
OLD: the author's pattern-matching from publicly available information
NEW: Bruce's pattern-matching from publicly available information
```

Line 57 (collective):
```
OLD: The author names real people in connection with speculative claims
NEW: We name real people in connection with speculative claims
```

Line 70 footnote (collective):
```
OLD: The author welcomes better suggestions.
NEW: We welcome better suggestions.
```

### B4. Record / Track Chapters

**File: `manuscript/record/record-intro.tex`**

Line 7 (Bruce-specific — his say-so, his estimate, both italic):
```
OLD: Believe none of this on the author's say-so. Wise readers should set their prior at 95\% Possibility A before turning the page --- read what follows as fiction unless something specific later moves you. The author's own estimate tilts toward C; that is no reason for yours to.
NEW: Believe none of this on Bruce's say-so. Wise readers should set their prior at 95\% Possibility A before turning the page --- read what follows as fiction unless something specific later moves you. Bruce's own estimate tilts toward C; that is no reason for yours to.
```

**File: `manuscript/record/the-surrender.tex`**

Line 49 (collective):
```
OLD: This author declines to speculate in print, for what should be obvious reasons.
NEW: We decline to speculate in print, for what should be obvious reasons.
```

**File: `manuscript/track-2-testament/pos29b-redacted.tex`**

Line 14 (Bruce-specific — his material, his decision, his invitation):
```
OLD: The author possesses material relevant to this position in the narrative. He has chosen not to include it due to the safety of people who may still be at risk and the sensitivity of ongoing events. The material concerns a project the author was invited to participate in and declined
NEW: Bruce possesses material relevant to this position in the narrative. He has chosen not to include it due to the safety of people who may still be at risk and the sensitivity of ongoing events. The material concerns a project he was invited to participate in and declined
```

Line 18 (Bruce-specific):
```
OLD: the author's caution is well-founded.
NEW: Bruce's caution is well-founded.
```

**File: `manuscript/track-2-testament/pos29-the-silence.tex`**

Line 62 — verify context. If same "the author's caution" pattern:
```
OLD: the author's caution is well-founded
NEW: Bruce's caution is well-founded
```

**File: `manuscript/track-2-testament/pos05-the-stories.tex`**

Line 24 (Bruce-specific):
```
OLD: The following is the author's fictionalized retelling
NEW: The following is Bruce's fictionalized retelling
```

**File: `manuscript/record/what-healer-said.tex`**

Line 17 (Bruce-specific):
```
OLD: The following is the author's fictionalized retelling
NEW: The following is Bruce's fictionalized retelling
```

**File: `manuscript/record/alpha-farm.tex`**

Line 15 footnote (Bruce-specific):
```
OLD: for the author, see \textit{The Target}
NEW: for Bruce, see \textit{The Target}
```

**File: `manuscript/track-2-testament/pos02-alpha-farm.tex`**

Line 16 footnote (same):
```
OLD: for the author, see \textit{The Target}
NEW: for Bruce, see \textit{The Target}
```

### B5. Appendix / Back Matter

**File: `manuscript/track-3-awakening/firmware-update.tex`**

Line 9 (collective — chapter has conversational tone, "us" fits):
```
OLD: including, in several sub-fields, the author.
NEW: including, in several sub-fields, us.
```

**File: `manuscript/99-back/verification.tex`**

Line 16 (collective):
```
OLD: in the author's correspondence with deadman's switch holders.
NEW: in the authors' correspondence with deadman's switch holders.
```

Line 40 (collective — inviting tone for contact section):
```
OLD: the author wants to hear from you:
NEW: we want to hear from you:
```

**File: `manuscript/appendix/timeline.tex`**

Line 113 — two changes on same line. Label (collective) + prose (collective):
```
OLD: (Author's Hypothesis) Five Eyes agencies invest heavily in quantum computation to crack PKC. This author calls it ULTRA II.
NEW: (Authors' Hypothesis) Five Eyes agencies invest heavily in quantum computation to crack PKC. We call it ULTRA II.
```
Note: "(Author's Hypothesis)" has no "the/this" prefix — it won't be caught by the "this author\|the author" grep. This edit handles it explicitly.

**File: `manuscript/appendix/topic-guide.tex`**

Line 24 — display text of hyperref (parallel to section header change in B2/B3):
```
OLD: \item[{\hyperref[pos01:the-authors-position]{The Author's Position}}]
NEW: \item[{\hyperref[pos01:the-authors-position]{The Authors' Position}}]
```
(The label `pos01:the-authors-position` stays unchanged — it's an anchor ID, not display text.)

### B6. DMS-Only Content

**File: `manuscript/appendix/dms-note.tex`**

This file opens with first-person "If I am alive" (line 8). Lines 11-16 switch to "the author" — inconsistent. Fix to match first-person voice.

Lines 11-12 (first person, matching line 8):
```
OLD: daily contact with a source the author calls ``Healer'' --- an Australian SAS
veteran who, through guided deduction rather than disclosure, led the author
NEW: daily contact with a source I call ``Healer'' --- an Australian SAS
veteran who, through guided deduction rather than disclosure, led me
```

Line 16 (first person):
```
OLD: The author did not know whether this was true.
NEW: I did not know whether this was true.
```

Line 78 section header "What the Author Would Say" — **leave as-is.** This is a meta-header for DMS recipients reading after Bruce is unavailable. The third-person framing is deliberate.

### B7. DO NOT CHANGE (verified correct)

| File | Line | Text | Reason |
|------|------|------|--------|
| spine/the-strongest-objection.tex | 49 | "The author considered it the most important part" | Refers to Tolkien |
| appendix/abstracts.tex | 156 | "biographical analysis of the author's career" | Refers to Bill Joy |
| copyright.tex | 51 | "are the authors'." | Already plural possessive |
| legal-note.tex | 10 (end) | "are the authors'." | Already plural possessive |

---

### Part B Idempotency

**Primary grep** — catches "this/the author" patterns (case-insensitive):
```
grep -rni "this author\|the author" manuscript/ | grep -v "\.aux:" | grep -v staging/ | grep -v "^[^:]*:%" | grep -v "the authors" | grep -v sources/ | grep -v versions/
```

**Expected remaining matches (exactly 3 real + possible false positives):**
1. `spine/the-strongest-objection.tex:49` — "The author considered it the most important part" (refers to **Tolkien**)
2. `appendix/abstracts.tex:156` — "the author's career" (refers to **Bill Joy**)
3. `appendix/dms-note.tex:78` — "What the Author Would Say" (deliberate third-person DMS header)

**Note:** grep may produce false positives from "the authorized" (substring match). Inspect visually — only count lines where "author" appears as a standalone word referring to Bruce/the book's authors.

**Secondary grep** — catches standalone "Author's" without "the/this" prefix (e.g., section headers, labels):
```
grep -rni "author's\|author " manuscript/ | grep -v "\.aux:" | grep -v staging/ | grep -v "^[^:]*:%" | grep -v "the authors\|authors'" | grep -v sources/ | grep -v versions/ | grep -v bibliography | grep -vi "co-author"
```
After Part B, this should return NO manuscript-text matches (only BibTeX `author =` fields if bibliography.bib slips through). If any remain, apply convention table.

If ANY unexpected matches remain in either grep, they are missed instances — fix them using the convention table above. Report exact remaining matches in completion message.

### Part B Commit

Single commit: `Voice consistency: singular "the author" → "we/Bruce/I" across 19 files`

---

## Build & Verify (all phases)

1. `make dev` — full build
2. Puppeteer QC:
   - Desktop: Stack table, ant hovertip, quasi-2D collapsed section
   - Phone: front-matter text renders
   - Check TOC shows "Authors' Note" (not "Author's Note")
   - Spot-check 3-4 changed passages in HTML output
3. `git push` to live site
4. Commit strategy: Phase 1 → Phase 2 → Part B (three commits)

## Files Modified (complete)

| File | Phase | Changes |
|------|-------|---------|
| `manuscript/00-front/hook.tex` | 1 | "one of us, Bruce"; "We don't know / We offer" |
| `manuscript/00-front/the-stack.tex` | 1 | "A radio wave"; ant hovertip |
| `manuscript/00-front/summary.tex` | 1+B | 6 changes total |
| `build/hover-definitions.yaml` | 1 | Ant queen hover entry |
| `manuscript/spine/the-wrong-substrate.tex` | 2 | Quasi-2D collapsed section |
| `manuscript/track-3-awakening/pos32-the-magnetosphere.tex` | 2 | Same collapsed section |
| `build/tech-collapse.yaml` | 2 | Collapse registration |
| `manuscript/00-front/authors-note.tex` | B | Title + "The authors do not know" |
| `manuscript/00-front/copyright.tex` | B | 3 changes (+ 2 DMS-only) |
| `manuscript/00-front/legal-note.tex` | B | "Bruce's memory"; "Bruce's source material" |
| `manuscript/spine/three-possibilities.tex` | B | Section header + 3 prose changes |
| `manuscript/bridge/pos01-three-possibilities.tex` | B | Section header + 3 prose changes (parallel) |
| `manuscript/record/record-intro.tex` | B | "Bruce's say-so"; "Bruce's own estimate" |
| `manuscript/record/the-surrender.tex` | B | "We decline" |
| `manuscript/track-2-testament/pos29b-redacted.tex` | B | 3 changes |
| `manuscript/track-2-testament/pos29-the-silence.tex` | B | 1 change (verify context) |
| `manuscript/track-2-testament/pos05-the-stories.tex` | B | "Bruce's fictionalized retelling" |
| `manuscript/record/what-healer-said.tex` | B | "Bruce's fictionalized retelling" |
| `manuscript/record/alpha-farm.tex` | B | Footnote: "for Bruce" |
| `manuscript/track-2-testament/pos02-alpha-farm.tex` | B | Footnote: "for Bruce" |
| `manuscript/track-3-awakening/firmware-update.tex` | B | "us" |
| `manuscript/99-back/verification.tex` | B | "authors' correspondence"; "we want to hear" |
| `manuscript/appendix/timeline.tex` | B | "(Authors' Hypothesis)"; "We call it ULTRA II" |
| `manuscript/appendix/topic-guide.tex` | B | Display text: "The Authors' Position" |
| `manuscript/appendix/dms-note.tex` | B | 3 changes (first-person voice) |
