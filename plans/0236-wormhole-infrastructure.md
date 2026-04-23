# Plan 0236 — Track A: Wormhole Infrastructure (Tooltips Everywhere)

**Status:** COMPLETE (executed; status not updated at time of commit)
**Author:** Auditor (Argus)
**Date:** 2026-04-22
**Related:** Plan 0215 (auto-detect hover terms — ALREADY COMMITTED at 3b03603), Plan 0235 (superseded)
**Replaces:** Plan 0235 Phase 1a + Phase 2

---

## Problem

97 wormhole instances in HTML, only 8 hover-wrapped. Deep-link visitors land anywhere in the book. The auto-detect system (Plan 0215) is live but explicitly SKIPS wormholes:
- `auto_always_rich = {'wormholes'}` at `build/preprocess.py` line 1729
- Skip logic at lines 1777-1778: `if lookup in auto_always_rich: continue`

Also: no singular `wormhole:` YAML entry — the auto-detect regex `\bwormholes\b` misses all singular instances ("A wormhole in this substrate", "wormhole-prone", "wormhole technology"). And `wormholes-title:` has a weaker panel than the body `wormholes:` entry (no comparison table, no mechanism text).

---

## Phase 1 — Strengthen YAML Panels (build/hover-definitions.yaml)

### 1a. Add mechanism paragraph to `wormholes:` panel (line ~196)

Insert a NEW `<p>` element AFTER the existing opening `<p>` (the one ending "Not the science-fiction kind.") and BEFORE the `<table>`:

```html
<p style="margin:0 0 0.3em;font-size:0.85em;line-height:1.4;font-style:italic;">A topological wormhole works by braiding anyons — move one around another and the quantum state changes depending only on topology, not speed or precision. This is computation: input state in, braiding operation, output state out.</p>
```

### 1b. Mirror to `Wormholes:` (capitalized entry, line ~207)

Add the same mechanism `<p>` in the same position in the `Wormholes:` entry's `html:` field.

### 1c. Upgrade `wormholes-title:` (line 18-23)

Replace the `text:` and `html:` fields with the updated content from `wormholes:`. KEEP the existing `hover_id: "wormholes-title"` and `target: "#summary:story-never-told"` unchanged — only `text:` and `html:` change.

### 1d. Add singular `wormhole:` entry

After the `Wormholes:` block (after line ~221), add a new entry:

```yaml
wormhole:
  text: "(copy from updated wormholes: text field)"
  hover_id: "wormholes"
  target: "#wormhole-disambiguation"
  html: |
    (copy from updated wormholes: html field — full panel with mechanism paragraph, comparison table, and SVG)
```

Same `hover_id` and `target` as the `wormholes:` entry.

### Commit 1

Stage only `build/hover-definitions.yaml`.
Message: `Plan 0236 Phase 1: strengthen wormhole YAML panels + add singular entry`

---

## Phase 2 — Enable Auto-Detect for Wormholes (build/preprocess.py)

### 2a. Line 1692

Change: `always_rich = {'wormholes'}`
To: `always_rich = {'wormholes', 'wormhole'}`

This ensures BOTH singular and plural explicit `\hovertip{}` calls always get the rich (HTML) panel.

### 2b. Line 1729

Change: `auto_always_rich = {'wormholes'}`
To: `auto_always_rich = set()`

### 2c. Lines 1777-1778

Delete these two lines:
```python
                if lookup in auto_always_rich:
                    continue
```

Now dead code (empty set).

### Verification

Build HTML. Check build output for hover tooltip counts. Report:
- Total hover tooltip count (explicit + auto)
- How many chapters now have auto-detected wormhole wraps
- Spot-check: title page, the-flat, three-possibilities all show wormhole hover terms

### Commit 2

Stage only `build/preprocess.py`.
Message: `Plan 0236 Phase 2: enable wormhole auto-detect`

---

## Constraints

- Do NOT modify any .tex files. This plan is YAML + Python infrastructure only.
- Do NOT open a browser. Build and report counts. Bruce verifies visually.
- The `always_rich` set at line 1692 (explicit pass) STAYS and GAINS `'wormhole'`. Do not remove `'wormholes'` from it.
- Plan 0215 auto-detect is ALREADY COMMITTED. You are removing the wormhole-specific skip, not implementing auto-detect from scratch.
- The existing `wormholes-title` hover_id and target fields must be preserved (different from the body `wormholes` entry).
