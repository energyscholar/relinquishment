# Plan 0274d: Puzzle Visibility Tiers and Consolidation

**Status:** READY FOR GENERATOR
**Author:** Auditor (Argus S63)
**Priority:** High
**Scope:** `build/puzzle-data.yaml`, `build/puzzle-tracker.yaml`, `build/preprocess.py`
**Prerequisites:** Plans 0274a, 0274b, 0274c (all complete)
**Annealing:** MED MED LOW LOW

---

## Problem Statement

After 0274c deployed 17 puzzles, two problems emerged:

1. **Too many puzzles at TITLE level.** 8 of 17 puzzles sit between chapter `<details>` elements (depth=3 in DOM), making them visible the moment a reader expands any part section. Only the strongest should be here — the rest belong inside their chapters (depth=4), visible when the reader actually reads that chapter.

2. **Silence puzzles overlap.** "The Silence" (pz-gd-t5-001, gd, 2 stages) and "The Silence Gap" (pz-mc-t5-002, mc, 1 question) ask nearly the same question. Both ask whether anyone has studied life in quantum substrates; both answer "no." They should be one 3-stage gd puzzle.

3. **Capabilities puzzle is mispositioned.** pz-mc-t6-001 is p2 and at TITLE level between chapters. It's a simple, clear puzzle that reinforces T4/T6/T7 takeaways. It should be p1, inside the capabilities chapter, rendered inline (default-open).

---

## Architecture: Why Puzzles Land at Different Depths

The injection algorithm (0274a) inserts each puzzle just BEFORE the target element listed in `CHAPTER_INJECTION_TARGETS`. The depth depends on where that target sits in the DOM:

**Early chapters** (story-never-told through wrong-substrate): targets are custodian interludes, which are INSIDE the chapter's `<details>` element. Puzzles land at depth=4 (CHAPTER level).

**Late chapters** (silence-gap through why-relinquish): targets are the NEXT chapter's `<details class="chapter-section">` element, which is a SIBLING of the current chapter. Puzzles land at depth=3 (TITLE level).

To move a late-chapter puzzle from TITLE to CHAPTER level: inject it inside the chapter's `<details>` (before its closing `</details>`) instead of between chapters.

---

## Changes

### Phase 1: Merge Silence Puzzles

Combine pz-gd-t5-001 ("The Silence") and pz-mc-t5-002 ("The Silence Gap") into a single 3-stage gd puzzle. Keep ID pz-gd-t5-001. Retire pz-mc-t5-002.

**New pz-gd-t5-001** (3 stages):

```yaml
- id: pz-gd-t5-001
    type: gd
    topic: t5
    level: p1
    category: science
    title: "The Silence"
    gateway_blurb: "Three questions. Each reveals a deeper layer of the same silence."
    stages:
      - question: "Has anyone studied whether life could exist in a quantum substrate?"
        options:
          - key: a
            text: "Yes — it's an active research area"
          - key: b
            text: "Yes — but the results are classified"
          - key: c
            text: "No — the question has apparently never been asked"
          - key: d
            text: "No — it was studied and ruled out decades ago"
        answer_key: c
        wrong_prompt: "Before you say 'ruled out' — by whom? In which journal? Can you name a single paper?"
        right_prompt: "Nobody has asked. Not 'asked and answered no.' Not 'asked and classified.' Simply never asked. But surely the published literature says SOMETHING?"

      - question: "Five scientific fields each hold a piece of this hypothesis. What does the published literature contain?"
        options:
          - key: a
            text: "A review article surveying the question and concluding the evidence is insufficient"
          - key: b
            text: "Several papers examining and rejecting the possibility"
          - key: c
            text: "A brief mention in a footnote, dismissed as speculation"
          - key: d
            text: "Nothing. No paper examines, proposes, or rejects the hypothesis."
        answer_key: d
        wrong_prompt: "You keep expecting to find a 'no.' What if there isn't even a 'no'?"
        right_prompt: "The literature contains no examination, no rejection, no dismissal — because it contains no proposal. But why? Surely someone in one of these five fields would have thought of it?"

      - question: "Why has no one studied this question?"
        options:
          - key: a
            text: "The relevant scientific fields don't talk to each other"
          - key: b
            text: "It's obviously impossible, so no one bothered"
          - key: c
            text: "Someone probably has, but hasn't published yet"
          - key: d
            text: "The technology to study it doesn't exist"
        answer_key: a
        wrong_prompt: "Which field would own this question? Biology studies carbon life. Physics studies 2DEGs. Whose job is it to study life in a quantum substrate?"
    abstract: "Five fields. Five empty searches. The silence isn't evidence of absence — it's evidence that the question falls between disciplines. Topologists don't read autocatalysis journals. Condensed matter physicists don't attend nonlinear dynamics conferences. Each field is rigorous within its boundaries. No individual scientist is negligent. But the system of academic specialization structurally prevents the question from forming. The question lives in a gap that no one owns. The silence is the finding."
```

**Tracker changes:**
- pz-mc-t5-002: set `installed: false` (retired — content merged into pz-gd-t5-001)
- pz-gd-t5-001: no change needed (already installed)

**VERIFY OK target: 16** (down from 17)

### Phase 2: Add Visibility and Inline Support to Injection Algorithm

Two changes to `inject_chapter_puzzles()` in `preprocess.py`:

#### 2a. Chapter-level injection (`visibility: chapter`)

Add `find_chapter_end()`:

```python
def find_chapter_end(text, chapter_section_id):
    """Find the closing </details> of a chapter section by its id.
    Returns character offset of the </details>, or -1 if not found."""
    start = find_injection_point(text, chapter_section_id)
    if start == -1:
        return -1
    depth = 0
    pos = start
    while pos < len(text):
        next_open = text.find('<details', pos)
        next_close = text.find('</details>', pos)
        if next_close == -1:
            return -1
        if next_open != -1 and next_open < next_close:
            depth += 1
            pos = next_open + 8
        else:
            depth -= 1
            if depth == 0:
                return next_close
            pos = next_close + 10
    return -1
```

Add `CHAPTER_SECTION_IDS` at module level (only chapters needing chapter-level injection):

```python
CHAPTER_SECTION_IDS = {
    'capabilities':    'spine:capabilities',
    'why-relinquish':  'spine:why-relinquish',
}
```

In the injection loop, after finding the default injection point, check visibility:

```python
visibility = tracker_entry.get('visibility', 'title')
if visibility == 'chapter' and chapter in CHAPTER_SECTION_IDS:
    chapter_end = find_chapter_end(text, CHAPTER_SECTION_IDS[chapter])
    if chapter_end != -1:
        pos = chapter_end
        print(f"  Puzzle: {pid} → inside {chapter} (chapter level)")
```

#### 2b. Inline rendering (`render: inline`)

In the puzzle HTML rendering section, check the `render` field:

```python
render_mode = tracker_entry.get('render', 'collapsible')
if render_mode == 'inline':
    puzzle_html = puzzle_html.replace(
        '<details class="puzzle-section">',
        '<details class="puzzle-section" open>'
    )
```

This makes the puzzle expanded by default — visible without clicking, still collapsible.

### Phase 3: Assign Visibility Tiers

Update puzzle-tracker.yaml with `visibility` and `render` fields:

| Puzzle | Chapter | Visibility | Render | Notes |
|--------|---------|-----------|--------|-------|
| pz-gd-t1-001 | story-never-told | title (default) | collapsible | KEEP — first puzzle, T1 |
| pz-gd-t5-001 | the-silence-gap | title (default) | collapsible | KEEP — T5 takeaway |
| pz-mc-t6-003 | why-relinquish | title (default) | collapsible | KEEP — core question |
| pz-log-t7-001 | why-relinquish | title (default) | collapsible | KEEP — per Bruce |
| pz-gd-t6-001 | capabilities | **chapter** | collapsible | DEMOTE — inside chapter |
| pz-mc-t6-001 | capabilities | **chapter** | **inline** | DEMOTE + INLINE, change level p2→p1 |
| pz-mc-t6-002 | why-relinquish | **chapter** | collapsible | DEMOTE — inside chapter |

All other puzzles: no change (already at CHAPTER or SECTION level).

**Result:**
- TITLE level (4): Method, Silence, Why Relinquish?, UDHR Service Compatibility
- CHAPTER level (10): Under Which Possibility?, Wormholes, 2DEG, The Braid, Fish Detecting Water, Canopy Problem, Accidental Habitat, Not a Deity, Not Chemistry, **Ethics** (demoted), **Why Srebrenica?** (demoted)
- INLINE inside chapter (1): **Capabilities** (demoted + inline)
- SECTION level (1): ~~The Braid, Canopy Problem already at depth=5~~

Wait — total check: 4 + 10 + 1 = 15. Plus Braid and Canopy at SECTION = 15 + 2 = 17. Minus 1 for Silence merge = 16. Correct.

Actually let me recount:
- TITLE (4): Method, Silence(merged), Why Relinquish?, UDHR
- CHAPTER (9): Under Which Possibility?, Wormholes, 2DEG, Fish Detecting Water, Accidental Habitat, Not a Deity, Not Chemistry, Ethics, Why Srebrenica?
- INLINE in chapter (1): Capabilities
- SECTION (2): Braid, Canopy Problem
Total: 4 + 9 + 1 + 2 = 16 ✓

### Phase 4: Build, Verify, Commit

1. Build (`make html`)
2. VERIFY OK: 16
3. Test merged Silence puzzle (3 stages work, reset works)
4. Test Capabilities inline (renders open, interaction works, positioned inside capabilities chapter)
5. Verify Ethics and Why Srebrenica are inside their chapters (not between chapters)
6. Verify Method, Silence, Why Relinquish, UDHR still at TITLE level
7. No JS errors
8. Commit: `Plan 0274d: puzzle visibility tiers + silence merge + capabilities inline`
9. Push

---

## Anneal: MED MED LOW LOW

### MEDIUM

**M1. `find_chapter_end()` tag counting could fail on malformed HTML.**
If the chapter section has unclosed `<details>` tags (e.g., from puzzle injection bugs or hand-edited content), the tag counter will find the wrong closing tag — or never find one.
**Mitigation:** Run `find_chapter_end()` on all entries in CHAPTER_SECTION_IDS during build and print WARNING if any return -1. Current HTML is well-formed (pandoc output + injection creates balanced tags). The function falls back gracefully: if it can't find the chapter end, the puzzle stays at TITLE level (existing behavior).

**M2. Merged Silence puzzle changes type for Stage 2 (was mc, now gd stage).**
The mc-format question ("What does the literature contain?") needs adaptation to gd format (question → options → right/wrong prompts instead of question → options → hint → background). The content transfers cleanly but the pedagogy shifts: mc gives hint-after-wrong, gd gives wrong_prompt-after-wrong and right_prompt-after-right. Need to verify the prompts work in gd's two-response format.
**Mitigation:** Stage 2's wrong_prompt and right_prompt are written above. Test in browser — the gd renderer handles 3 stages; no code change needed (gd supports N stages).

### LOW

**L3. Inline puzzle (`<details open>`) may auto-scroll on mobile.**
Some mobile browsers scroll to the first open `<details>` element. With one inline puzzle in a chapter, this could jump the reader past chapter content.
**Mitigation:** Bruce reads on phone — he'll catch this immediately in testing. If it happens, fallback is to use a `<div class="puzzle-inline">` instead of `<details open>`. That requires a small CSS addition but avoids the scroll issue.

**L4. Why Srebrenica? demotion reduces why-relinquish TITLE visibility.**
After demotion, why-relinquish has 2 puzzles at TITLE (Why Relinquish? + UDHR) and 1 inside the chapter (Why Srebrenica?). This is fine — the 2 at TITLE are the strongest.
**Mitigation:** No action needed. If Bruce wants Why Srebrenica? back at TITLE, just remove the `visibility: chapter` field.

---

## Acceptance Criteria

1. VERIFY OK: 16 (merged = 17 - 1)
2. Silence puzzle has 3 working stages
3. Capabilities puzzle renders inline (open by default) inside capabilities chapter
4. Ethics and Why Srebrenica are inside their chapters (not between chapters)
5. Method, Silence, Why Relinquish, UDHR remain at TITLE level
6. No JS errors
7. Level ordering preserved within multi-puzzle chapters

---

## Handoff Prompt

```
You are the Generator. Read plan 0274d in ~/software/relinquishment/plans/.

Three changes:

1. MERGE SILENCE PUZZLES in build/puzzle-data.yaml:
   Replace pz-gd-t5-001 with 3-stage version (see plan for exact YAML).
   Set pz-mc-t5-002 installed:false in puzzle-tracker.yaml.

2. ADD VISIBILITY SUPPORT to build/preprocess.py:
   - Add find_chapter_end() function (tag-counting, see plan)
   - Add CHAPTER_SECTION_IDS dict: capabilities→spine:capabilities,
     why-relinquish→spine:why-relinquish
   - In injection loop: if visibility=='chapter', inject before
     chapter's closing </details> instead of between chapters
   - If render=='inline', add open attribute to <details>

3. APPLY VISIBILITY ASSIGNMENTS in puzzle-tracker.yaml:
   - pz-gd-t6-001: add visibility: chapter
   - pz-mc-t6-001: add visibility: chapter, render: inline,
     change level: p2 → p1
   - pz-mc-t6-002: add visibility: chapter

Build, VERIFY OK: 16, test Silence (3 stages), Capabilities
(inline inside chapter), Ethics + Why Srebrenica (inside chapters).
No JS errors. Commit:
"Plan 0274d: visibility tiers + silence merge + capabilities inline"
Push.
```
