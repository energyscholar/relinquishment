# Plan 0239 — Tooltip Single Source of Truth (Complete Fix)

**Status:** COMPLETE (verified S63 audit)
**Author:** Auditor (Argus)
**Date:** 2026-04-22
**Related:** Plans 0236/0237/0238 (wormhole mitigation), Plan 0172 (always-rich wormholes)
**Fixes:** (1) Tooltip drift from duplicate YAML entries, (2) partial coverage (first-per-chapter, not every instance)

---

## Outcome

After this plan, EVERY instance of "wormhole," "wormholes," "topological wormhole," "the Flat," and "The Flat" in the entire book renders the SAME rich tooltip panel. One canonical YAML entry per concept family. Edit once → propagates everywhere. No exceptions.

---

## Phase 1 — YAML: Wormhole Family Single Source of Truth

In `build/hover-definitions.yaml`, the canonical entry is `wormholes:` (line ~202). Add anchor `&wormhole-panel`:

```yaml
wormholes: &wormhole-panel
  text: "Not the sci-fi kind..."
  hover_id: "wormholes"
  target: "#wormhole-disambiguation"
  html: |
    (keep existing full panel — mechanism paragraph, comparison table, SVG)
```

Replace ALL other wormhole entries with merge-key aliases:

```yaml
Wormholes:
  <<: *wormhole-panel

wormhole:
  <<: *wormhole-panel

topological wormhole:
  <<: *wormhole-panel

wormholes-title:
  <<: *wormhole-panel
  hover_id: "wormholes-title"
  target: "#summary:story-never-told"
```

Each alias inherits text + hover_id + target + html from the anchor. Overrides (hover_id, target) are listed explicitly and take precedence.

**DO NOT TOUCH `stack-wormholes:` (line ~660).** Stack chart row label — intentionally separate semantic domain, skipped by `AUTO_SKIP_PATTERNS`.

---

## Phase 2 — YAML: Flat Family Single Source of Truth

Canonical entry is `the Flat:` (line ~42). Add anchor `&flat-panel`:

```yaml
the Flat: &flat-panel
  text: "This book coins the Flat..."
  hover_id: "the-flat-title"
  target: "#dl:what-is-the-flat"
  html: |
    (keep existing full panel — text paragraphs, chip cross-section SVG)
```

Replace variants:

```yaml
The Flat:
  <<: *flat-panel

the-flat-title:
  <<: *flat-panel
  target: "#summary:story-never-told"
```

`The Flat:` currently has NO html field (drifted — text-only tooltip). After this change it inherits the full rich panel.

---

## Phase 3 — preprocess.py: Wrap EVERY Instance of Critical Terms

This is the key behavioral change. Currently auto-detect wraps only the FIRST occurrence of each term per chapter. For critical terms, wrap ALL occurrences.

### 3a. Add wrap-all set (near line ~1729, after `auto_always_rich` removal):

```python
# Critical terms: wrap EVERY occurrence, not just first per chapter.
# These terms are the book's #1 reader-confusion risk.
auto_wrap_all = {'wormholes', 'wormhole', 'topological wormhole', 'the flat'}
```

### 3b. Update `always_rich` (line ~1692):

```python
always_rich = {'wormholes', 'wormhole', 'topological wormhole', 'the flat'}
```

### 3c. Modify the auto-detect loop (lines ~1773-1800):

Current behavior:
- Skip term if already seen in chapter (`hover_seen` check)
- Find FIRST match (`pattern.search` + `break`)

New behavior for terms in `auto_wrap_all`:
- Do NOT skip even if already seen
- Find ALL matches (`pattern.finditer` instead of `pattern.search`)
- Do NOT break after first match — continue through all scannable regions
- Before adding a replacement, check it doesn't OVERLAP with an already-collected replacement (longer terms are processed first due to length-sort, so they win ties)

The overlap check is necessary because "topological wormhole" contains "wormhole" — without it, a single text instance could produce nested/broken HTML. Since terms are sorted longest-first (line 1733), longer terms claim their ranges first. Shorter terms skip matches that fall inside claimed ranges.

Pseudocode for the modified loop:

```python
claimed_ranges = []  # list of (abs_start, abs_end) for this chapter

for term_key, pattern in auto_patterns:
    lookup = term_key.lower().replace(...)
    wrap_all = lookup in auto_wrap_all
    if lookup in hover_seen[ch_idx] and not wrap_all:
        continue

    found = False
    for region_start, region_end in scannable:
        region_text = chapter_text[region_start:region_end]
        if wrap_all:
            for m in pattern.finditer(region_text):
                abs_start = ch_start + region_start + m.start()
                abs_end = ch_start + region_start + m.end()
                # Skip if overlaps with already-claimed range
                if any(abs_start < ce and abs_end > cs for cs, ce in claimed_ranges):
                    continue
                # (build replacement span same as current code, lines 1784-1796)
                replacements.append((abs_start, abs_end, replacement))
                claimed_ranges.append((abs_start, abs_end))
                auto_count += 1
                found = True
        else:
            m = pattern.search(region_text)
            if m:
                abs_start = ch_start + region_start + m.start()
                abs_end = ch_start + region_start + m.end()
                # (build replacement span same as current code)
                replacements.append((abs_start, abs_end, replacement))
                hover_seen[ch_idx].add(lookup)
                auto_count += 1
                found = True
                break
    # For wrap_all terms, don't add to hover_seen (we want them to fire every time)
```

The existing replacement-application code (lines 1802-1804: sort reverse, splice) works unchanged — it handles multiple replacements per chapter already.

---

## Phase 4 — Build and Verify

Build HTML. Report:
- Total hover tooltip count (explicit + auto). Should increase significantly.
- Wormhole wrap count per chapter (should be ALL instances, not just first).
- Flat wrap count per chapter (should be ALL instances of "the Flat" / "The Flat").
- Spot-check: in The Flat chapter, every "wormhole" and "the Flat" has hover indicator.
- Spot-check: "topological wormhole" in the-stack.tex renders same panel as "wormholes" in body.
- Spot-check: "The Flat" (capitalized) now shows rich panel (previously text-only).
- Verify no nested/broken HTML from overlap handling.
- Verify no YAML parse errors from anchors.

---

## Commit

Stage: `build/hover-definitions.yaml`, `build/preprocess.py`
Message: `Plan 0239: tooltip single source of truth — YAML anchors + wrap every critical instance`

Do NOT open a browser. Build and report counts. Bruce verifies visually.

---

## Technical Notes

- **YAML anchors** (`&name`) and **merge keys** (`<<: *name`): supported by PyYAML `safe_load()`. Code sees resolved dicts — no parser changes needed.
- **SVG ID duplication:** Flat panels previously used different SVG IDs to avoid conflicts. With anchors, all Flat panels share IDs. Cosmetically harmless — identical SVGs render identically regardless of ID deduplication.
- **Overlap handling:** Terms sorted longest-first (existing behavior at line 1733). "topological wormhole" (21 chars) claims its range before "wormhole" (8 chars) tries to match inside it. The overlap check prevents double-wrapping.
- **`stack-wormholes`:** Intentionally excluded — different semantic domain (stack chart row labels), already skipped by `AUTO_SKIP_PATTERNS`.
- **Future-proofing:** To add a new variant (e.g., `Wormhole:` capitalized singular), add one line: `Wormhole: { <<: *wormhole-panel }`. The content inherits automatically.
