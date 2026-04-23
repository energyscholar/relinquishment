# Plan 0143e: Phase 5 — Integration & Verification

**Status:** Ready for Generator (after Phase 4 lands)
**Parent:** Plan 0143 (Z-Restructure Metaplan)
**Role:** Mixed. Parts A-C: Generator executes. Part D: Auditor reviews. Part E: Bruce decides.

---

## Overview

Everything works together. All five takeaways land. All failure modes blocked. All reading paths tested. This phase also integrates Plan 0141 (A/B/C icons) and rewrites popup content for the Z-structure.

---

## Part A: A/B/C Epistemic Labels (Plan 0141 Integration)

Add epistemic labels to the TOC menu. This makes the A-spine visually obvious — most chapters are "verified physics," and the contrast with C chapters is the argument.

### Step 1: Update menu-tooltips.yaml

Change YAML structure from flat strings to dicts with `text` and `epistemic` fields:

```yaml
chapters:
  "spine:three-possibilities": 
    text: "The framework: confabulation, exaggerated kernel, or substantially true."
    epistemic: B
  "spine:the-stack":
    text: "Eight technologies stacked in order of increasing impossibility."
    epistemic: A
```

**Z-structure chapter assignments:**

| Chapter ID | Epistemic | Rationale |
|-----------|-----------|-----------|
| `spine:three-possibilities` | B | Framework — needs at least a kernel |
| `spine:the-stack` | A | Published physics stack |
| `spine:the-flat` | A | 2DEG physics — textbook |
| `spine:the-braid` | A | Topology/braiding — published math |
| `spine:factoring-game` | A | Shor's algorithm — public record |
| `spine:code-war` | A | Historical classified breakthroughs — public record |
| `spine:genesis` | A | Kauffman, autocatalytic sets — published |
| `spine:growing-a-mind` | A | Turing, computational neuroscience — published |
| `spine:wrong-substrate` | A | Magnetosphere physics — published |
| `spine:silence-gap` | A | Literature gap analysis — verifiable |
| `spine:capabilities` | A | Physics permits — derivable from published work |
| `spine:why-relinquish` | A | Thought experiment — logic, not testimony |
| `spine:strongest-objection` | A | Self-assessment — A by construction |
| `spine:weigh-evidence` | B | Evidence weighing — needs at least a kernel |
| `record:intro` | — | Framing — no label |
| `record:alpha-farm` | C | Personal testimony |
| `record:hobbit-mirror` | C | Self-assessment as narrator |
| `record:healer-said` | C | Testimony |
| `record:departure` | C | Testimony |
| `record:handler` | C | Testimony |
| `record:demonstration` | C | Testimony |
| `record:interdiction` | C | Testimony |
| `record:first-light` | C | Testimony |
| `record:walk-out` | C | Testimony |
| `record:target` | C | Testimony |
| `record:instantiation` | C | Testimony |
| `record:never-again` | C | Testimony |
| `record:surrender` | C | Testimony |
| `record:twenty-years` | C | Testimony |
| `record:the-question` | C | Testimony |

**Visual pattern:** Spine = wall of A (gold). Record = wall of C (purple). The contrast IS the argument. B is rare (two chapters) — framework and weighing, exactly where you'd expect epistemic ambiguity.

### Step 2: Update preprocess.py tooltip parsing

The popup injection code currently expects `chapters[key] = string`. Update to handle dict format:

```python
# In the tooltip injection section of fix_html_toc():
for chapter_id, value in chapters.items():
    if isinstance(value, dict):
        tooltip_text = value.get('text', '')
        epistemic = value.get('epistemic', '')
    else:
        tooltip_text = value
        epistemic = ''
    # ... existing injection logic, plus:
    if epistemic:
        # Add class to the <a> or <li> element
        # epistemic-a, epistemic-b, or epistemic-c
```

### Step 3: CSS

Add to the CSS block in preprocess.py (after the existing `.bc-expansion` styles):

```css
/* A/B/C epistemic labels (Plan 0141) */
.epistemic-a > a, .epistemic-a > summary { border-left: 3px solid #d4a847; padding-left: 0.5em; }
.epistemic-b > a, .epistemic-b > summary { border-left: 3px solid #6a9fb5; padding-left: 0.5em; }
.epistemic-c > a, .epistemic-c > summary { border-left: 3px solid #9b7db8; padding-left: 0.5em; }
```

**Icon decision deferred** — border-left stripes first. Icons (checkmark, magnifying glass, tinfoil hat) are a later polish pass once Bruce sees the color stripes on his phone and picks icons.

### Step 4: Legend

Add a one-line legend at the top of the TOC menu (injected by preprocess.py):

```html
<div class="epistemic-legend">
  <span class="epistemic-a">Verified physics</span>
  <span class="epistemic-b">Evidence to weigh</span>
  <span class="epistemic-c">Testimony</span>
</div>
```

CSS for legend: small text, flex row, each span has matching border-left.

---

## Part B: Popup Content Rewrite

Replace placeholder tooltip text in `menu-tooltips.yaml` with substantive summaries. Each popup must:

1. Summarize the chapter at p2 density (2-4 sentences, ~40-80 words)
2. Deliver at least one of T1-T5
3. Block at least one failure mode where relevant
4. Match the chapter's actual Z-structure content (not the old structure)

**Method:** Read each chapter's actual content (spine/*.tex, record/*.tex), then write a popup that summarizes it. Do NOT write popups from memory or from the plan — read the source.

**Spine popups should emphasize the A-content:** "This is textbook physics. Here's what it means." The popups for A chapters should make a skeptic curious, not defensive.

**Record popups should be honest about C:** "Personal testimony. The reader decides." No hedging, no sales pitch.

**Guardian interludes:** No popups needed — they don't appear in the TOC (they use `\input` not `\include`).

### New chapters needing popups

These chapters were added in Phase 3 and need popup text:

| Chapter ID | Needs popup |
|-----------|------------|
| `spine:why-relinquish` | Yes — thought experiment about dangerous technology |
| `record:hobbit-mirror` | Yes — Bruce's self-assessment as narrator |
| `record:never-again` | Yes — UDHR as machine ethics |
| `record:the-question` | Yes — predictions, evidence trail, reader decides |

---

## Part C: Cross-Reference Cleanup

Phase 3 migrated content but may have left old `pos*:` labels. Sweep and fix.

```bash
cd ~/software/relinquishment
grep -rn '\\ref{pos' manuscript/spine/ manuscript/record/
grep -rn '\\hyperref\[pos' manuscript/spine/ manuscript/record/
grep -rn '\\label{pos' manuscript/spine/ manuscript/record/
grep -rn '\\ref{ch:' manuscript/spine/ manuscript/record/
grep -rn '\\ref{t[0-9]' manuscript/spine/ manuscript/record/
```

Update all matches to new `spine:` or `record:` labels. Also check:
- `hover-definitions.yaml` for old anchor references
- `topic-guide.tex` for old `pos*:` cross-references (~50 expected)

**topic-guide.tex:** Known issue. Many broken refs. Fix what's straightforward, flag the rest. This is a later polish item if the volume is too large.

---

## Part D: Verification Checklist (Auditor)

After Generator completes Parts A-C, Auditor verifies:

### D1: Build
- [ ] `make dev` succeeds
- [ ] No LaTeX errors beyond expected warnings
- [ ] No `??` in HTML output (broken cross-references)

### D2: Phone Test
- [ ] Read entire spine on phone (Bruce's primary reading surface)
- [ ] Single column, no horizontal scroll
- [ ] All `<details>` taps work (chapters, interludes, expansion hooks)
- [ ] Epistemic color stripes visible on dark menu background
- [ ] Legend readable

### D3: Desktop Test
- [ ] Hover popups work on menu items
- [ ] Expansion hooks expand/collapse
- [ ] Back button navigation works
- [ ] Guardian interludes render correctly (purple left border, italic text)

### D4: Spine Standalone Test
- [ ] Read spine chapters sequentially (Three Possibilities → Weigh the Evidence)
- [ ] Works as standalone pop-science book? No gaps requiring Record content?
- [ ] Guardian interludes bridge chapters without breaking A-flow?
- [ ] New chapters (Silence Gap, Capabilities, Why Relinquish) integrate smoothly?

### D5: Record Standalone Test
- [ ] Read Record chapters sequentially (Alpha Farm → The Question)
- [ ] Coherent narrative arc? Timeline makes sense?
- [ ] New chapters (Hobbit Mirror, Never Again, The Question) fit?

### D6: Expansion Hook Test
- [ ] All 7 hooks appear in correct spine chapters
- [ ] Each hook expands on tap/click
- [ ] "Read the full story" links navigate to correct Record chapter
- [ ] Hook content matches B/C framing (hedged, "according to this story")

### D7: T1-T5 Takeaway Audit

For each takeaway, verify delivery across reading layers:

| Takeaway | p1 (hook) | p2 (summary) | Spine | Popups | Interludes | Expansion |
|----------|----------|-------------|-------|--------|------------|-----------|
| T1: Meet Guardian | ? | ? | ✓ (interludes) | ? | ✓ | ? |
| T2: The Flat | ? | ? | ✓ (ch 3-4) | ? | ✓ (I1, I2) | — |
| T3: Life in Flat | ? | ? | ✓ (ch 8-10) | ? | ✓ (I5) | ✓ |
| T4: Capabilities | ? | ? | ✓ (ch 11) | ? | — | ✓ |
| T5: Silence Gap | ? | ? | ✓ (ch 10) | ? | ✓ (I6) | — |

**Method:** Read each layer. Mark each cell YES, PARTIAL, or NO. All cells in Spine/Interludes should be YES. Popups should be YES after rewrite. p1/p2 cells are informational — those are revised in a later pass (Plan 0142).

### D8: Failure Mode Spot Check

Pick three failure modes (F1 deity, F3 ChatGPT, F5 silence=refutation). For each, identify where in the spine the block exists. If no block, flag for content revision.

---

## Part E: Decisions for Bruce

### E1: Icon selection
Border-left color stripes deploy first. Icons are a later pass. Bruce to choose when he sees the stripes on phone:
- A: checkmark? Nobel medal? textbook? (must read as "verified")
- B: magnifying glass? scales? (must read as "weigh it")  
- C: tinfoil hat SVG? (must read as "I know, read it anyway")

### E2: Mixed-epistemic chapters
- `spine:why-relinquish` — concept is A, narrative is C. Plan says A (thought experiment only, C stripped to Record). Confirm?
- `spine:weigh-evidence` — weighing evidence requires B/C awareness. Labeled B. Confirm?

### E3: topic-guide.tex
~50 broken cross-references. Options:
- Fix all now (1-2 hours mechanical work)
- Fix later as a separate plan
- Drop topic-guide from build temporarily

### E4: Website push
After all verification passes, `make dev` + push to website. Bruce reads on phone. Final approval of Z-structure.

---

## Execution Order

1. **Part A** — epistemic labels (YAML + preprocess.py + CSS + legend)
2. **Part B** — popup content rewrite (requires reading all chapters)
3. **Part C** — cross-reference cleanup
4. **Build:** `make dev`
5. **Part D** — verification checklist (Auditor)
6. **Part E** — Bruce decisions
7. **Push** — after Bruce approves

Parts A and C can run in parallel. Part B requires reading chapter content, so it's sequential. Part D is Auditor-only (after Generator finishes).

---

## What NOT to Do

- Do NOT modify chapter content (.tex files) — this is verification, not revision
- Do NOT modify Guardian interludes — Phase 2 is complete and approved
- Do NOT modify expansion hooks — Phase 4 handles those
- Do NOT revise p1 (hook.tex) or p2 (summary.tex) — that's Plan 0142, a later pass
- Do NOT add icons yet — stripes first, icons after Bruce sees it on phone

---

*Plan 0143e created S54, 2026-04-08. Auditor: Argus.*
