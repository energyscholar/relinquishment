# Plan 0274a: Harden Puzzle Injection Algorithm

**Status:** READY FOR GENERATOR
**Author:** Auditor (Argus S63)
**Priority:** High (prerequisite for 0274b and 0274c)
**Scope:** `build/preprocess.py` (`inject_chapter_puzzles()` rewrite)
**Annealing:** MED MED LOW LOW

---

## Problem Statement

The current `inject_chapter_puzzles()` uses brittle full-string matching (CHAPTER_MARKERS dict with exact HTML strings). It also doesn't gate on `installed` (only `approved`), doesn't sort by reading level within chapters, and provides no injection logging. This plan rewrites the injection infrastructure to be robust, auditable, and manifest-driven.

---

## Changes

### 1. Replace CHAPTER_MARKERS with CHAPTER_INJECTION_TARGETS

Map chapter names to stable `id` attributes instead of exact HTML strings. **Define at MODULE LEVEL** (not inside a function) so both `inject_chapter_puzzles()` and `verify_puzzle_injection()` (0274b) can reference it:

```python
# ORDER MATTERS: entries must be in document order (story-never-told first,
# why-relinquish last). Reverse iteration preserves insertion positions.
CHAPTER_INJECTION_TARGETS = {
    'story-never-told':    'preface',
    'three-possibilities': 'custodian:flat',
    'the-flat':            'custodian:dance',
    'the-braid':           'custodian:locksmith',
    'the-code-war':        'custodian:grown',
    'growing-a-mind':      'custodian:ocean',
    'wrong-substrate':     'custodian:quiet',
    'the-silence-gap':     'spine:capabilities',
    'capabilities':        'spine:why-relinquish',
    'why-relinquish':      'spine:strongest-objection',
}
```

Each value is the `id` of the HTML element that FOLLOWS the target chapter. Puzzles are injected just before this element — i.e. at the END of the target chapter.

### 2. Robust find_injection_point()

Two HTML patterns exist in the output:

**Pattern A — custodian interludes (6 targets):**
`id` is directly on a `<div>`:
```html
<div class="custodian-interlude" id="custodian:flat">
```

**Pattern B — chapter sections (4 targets):**
`id` is on a nested `<h2>` inside `<summary>` inside `<details>`, all on ONE line:
```html
<details class="chapter-section ..."><summary><h2 id="spine:capabilities">...
```

The algorithm must handle both:

```python
import re

def find_injection_point(text, target_id):
    """Find position just before the block-level element containing target_id.
    Returns character offset, or -1 if not found."""
    # Pattern A: id directly on a div or details
    for tag in ('div', 'details'):
        pattern = re.compile(r'<' + tag + r'\b[^>]*\bid="' + re.escape(target_id) + r'"')
        m = pattern.search(text)
        if m:
            return m.start()

    # Pattern B: id on nested element (h2) — find it, walk to line start, find <details
    pattern = re.compile(r'\bid="' + re.escape(target_id) + r'"')
    m = pattern.search(text)
    if not m:
        print(f"  WARNING: injection target id='{target_id}' not found in HTML")
        return -1

    line_start = text.rfind('\n', 0, m.start())
    line_start = 0 if line_start == -1 else line_start + 1
    line_prefix = text[line_start:m.start()]

    for block_tag in ('<details', '<div'):
        tag_pos = line_prefix.find(block_tag)
        if tag_pos != -1:
            return line_start + tag_pos

    print(f"  WARNING: no block element found on same line as id='{target_id}'")
    return -1
```

### 3. Gate on `installed` (not just `approved`)

Change the filter from:
```python
if p.get('approved'):
    approved[p['id']] = p
```
to:
```python
if p.get('approved') and p.get('installed'):
    approved[p['id']] = p
```

This makes `installed: true` the deployment gate. The tracker becomes the single source of truth for what appears in the HTML:
- `approved: true, installed: false` = auditor approved, not yet deployed
- `approved: true, installed: true` = deployed, should appear in HTML

### 4. Sort by level within chapters

Group puzzles by chapter, sort by level (p1 first), process in reverse document order:

```python
by_chapter = {}
for pid, tracker_entry in approved.items():
    chapter = tracker_entry.get('location', {}).get('chapter', '')
    by_chapter.setdefault(chapter, []).append((pid, tracker_entry))

for chapter in reversed(list(CHAPTER_INJECTION_TARGETS.keys())):
    puzzles = by_chapter.get(chapter, [])
    if not puzzles:
        continue

    target_id = CHAPTER_INJECTION_TARGETS[chapter]
    pos = find_injection_point(text, target_id)
    if pos == -1:
        continue

    def level_key(item):
        lvl = str(item[1].get('level', 'p9'))
        return int(lvl.replace('p', ''))
    puzzles.sort(key=level_key)

    for pid, tracker_entry in reversed(puzzles):
        # ... render puzzle HTML ...
        text = text[:pos] + puzzle_html + '\n' + text[pos:]
        injected += 1
```

Reverse document order ensures earlier insertions don't shift positions of later ones. Reverse within chapter ensures p1 ends up on top.

### 5. Per-puzzle injection logging

After each puzzle is injected:
```python
print(f"  Puzzle: {pid} \"{title}\" → {chapter} (before {target_id}) ✓")
```

And for skipped puzzles (unsupported type, no chapter match):
```python
if ptype not in ('mc', 'gd', 'log'):
    print(f"  Puzzle: {pid} type '{ptype}' not supported — skipped")
    continue
if chapter not in CHAPTER_INJECTION_TARGETS:
    print(f"  Puzzle: {pid} chapter '{chapter}' not in INJECTION_TARGETS — skipped")
    continue
```

### 6. Tracker normalization and relocations

All done in this phase (before any wave deployment):

| Action | Puzzle | Field | Old | New |
|--------|--------|-------|-----|-----|
| Normalize | pz-mc-t3-003 | chapter | `the-wrong-substrate` | `wrong-substrate` |
| Relocate | pz-gd-t2-001 | chapter | `the-flat` | `growing-a-mind` |
| Relocate | pz-log-t7-001 | chapter | `capabilities` | `why-relinquish` |
| Relocate | pz-ord-t4-002 | chapter | `the-flat` | `story-never-told` |
| Relocate | pz-ord-t1-001 | chapter | `three-possibilities` | `the-braid` |
| Set flag | pz-mc-t2-001 | installed | false | true |
| Set flag | pz-mc-t1-002 | installed | false | true |

(pz-mc-t2-002 and pz-log-t6-002 already have `installed: true`)

After these changes, 4 puzzles have `installed: true`: mc-t2-001, mc-t2-002, mc-t1-002, log-t6-002. pz-gd-t2-001 drops from the-flat (relocated, installed: false). Net: HTML goes from 5 puzzles to 4 temporarily. Wave 1 of 0274c restores and adds.

---

## Anneal: MED MED LOW LOW

### MEDIUM

**M1. Line-start approach assumes single-line structure.**
The algorithm finds `id="..."`, walks to line start, finds `<details` on the same line. If pandoc ever wraps `<details>...<summary><h2 id=...>` across multiple lines, the walk fails.
**Mitigation:** Verified all 10 targets are single-line in current output. Pandoc's HTML writer doesn't wrap opening tag sequences. If it ever does, the WARNING print catches it and the puzzle silently skips (no crash). Can add a multi-line rfind as a second fallback.

**M2. `installed` gate changes existing behavior.**
Currently 5 puzzles inject with only `approved: true`. After this change, 3 of those 5 lose injection until their `installed` flag is set. Phase 1 sets the flag for 2 of them (mc-t2-001, mc-t1-002). The 5th (gd-t2-001) is intentionally relocated and will return in wave 2.
**Mitigation:** The 5→4 transition is one commit. Verify immediately after build. pz-gd-t2-001 disappearing from the-flat is CORRECT (it's being relocated). Commit message should note the temporary absence.

### LOW

**L3. Regex `\bid="..."` could match a substring.**
If another element has `id="custodian:flat-something"`, the `\b` word boundary wouldn't prevent a false match because `:` and `-` aren't word characters.
**Mitigation:** All target IDs are unique substrings in the HTML. Verified by grep. The `"` closing quote after the id value prevents partial matching anyway.

**L4. Sort-by-level on missing level field.**
If a puzzle in puzzle-data.yaml has no `level` field, `int('9')` is the fallback — it sorts last.
**Mitigation:** All 17 installable puzzles have level fields. Verified.

---

## Acceptance Criteria

1. `inject_chapter_puzzles()` uses `find_injection_point()` with id-based lookup
2. Only puzzles with BOTH `approved: true` AND `installed: true` are injected
3. Build output shows per-puzzle injection log
4. 4 puzzle-section elements in HTML after this phase (temporary, before wave 1)
5. No JavaScript console errors
6. All 5 tracker relocations + 1 normalization applied

---

## Handoff Prompt

```
You are the Generator. Read plan 0274a in ~/software/relinquishment/plans/.

Rewrite inject_chapter_puzzles() in build/preprocess.py:
1. Replace CHAPTER_MARKERS with CHAPTER_INJECTION_TARGETS (10 entries
   mapping chapter names to target IDs — see plan for exact dict)
2. Implement find_injection_point() with two-pass lookup: first try
   id on div/details directly, then find id on nested h2 and walk to
   line start to find containing <details (see plan for exact code)
3. Change filter from approved-only to approved AND installed
4. Group by chapter, sort by level (p1 first), process in reverse
   document order, insert in reverse within chapter
5. Add per-puzzle logging (injected + skipped)

Then update puzzle-tracker.yaml:
- Normalize pz-mc-t3-003 chapter: the-wrong-substrate → wrong-substrate
- Relocate pz-gd-t2-001 → growing-a-mind
- Relocate pz-log-t7-001 → why-relinquish
- Relocate pz-ord-t4-002 → story-never-told
- Relocate pz-ord-t1-001 → the-braid
- Set installed:true for pz-mc-t2-001 and pz-mc-t1-002

Build, verify 4 puzzle-section elements, verify injection log shows
4 injected + skipped messages, no JS errors. Commit:
"Plan 0274a: harden injection algorithm + installed gate + tracker fixes"
```
