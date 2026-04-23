# Plan 0213 — Per-chapter tooltip re-triggering

## Status
**Status:** COMPLETE (verified S63 audit)
COMPLETE (verified S63 audit). Originally: Ready for Generator.

## Problem

The hover system uses a document-global `hover_seen` set (preprocess.py:1606). The first `\hovertip{term}` occurrence gets a full tooltip span; all subsequent occurrences get italic-only styling. This made sense for linear reading but not for the HTML's collapse/expand architecture.

**The HTML is not read linearly.** Readers expand individual chapters. A reader who opens "Wormholes in the Flat" without first reading the Summary never sees tooltips for `topological order`, `2DEG`, `five fields`, or other terms that first-fire in `summary.tex`. They get unexplained italic text — worse than no styling at all, because italics imply *emphasis* rather than *defined term*.

**Scale:** 51 `\hovertip{}` uses across the manuscript. 26 fire in `summary.tex`. Terms like `topological order` (summary.tex:32 → the-flat.tex:21,49), `2DEG` (summary.tex → why-relinquish.tex), `lattice dynamics` (twenty-years.tex in record vs track-2), and `buttons` (genesis.tex, growing-a-mind.tex, pos13-genesis.tex) lose their tooltips in every chapter after the first.

**Exception:** `wormholes` is in the `always_rich` set (preprocess.py:1624) and already re-triggers everywhere. This plan generalizes that behavior to all terms, scoped per chapter.

## Design

Change `hover_seen` from a document-global set to a **per-chapter set**. Each `<details class="chapter-section">` gets its own tooltip scope. First occurrence of a term *within that chapter* gets the full tooltip span; subsequent *within the same chapter* get italic-only.

### Why per-chapter (not per-section or per-paragraph)

- Chapters are the independently navigable unit (expand one, read it, close it).
- Per-section would fire tooltips too aggressively — a reader scrolling through a chapter doesn't need `the Flat` re-explained every few paragraphs.
- Per-chapter matches the mental model: "I opened this chapter; I should be able to understand it without opening other chapters."

### Implementation

**Single file edit:** `build/preprocess.py`, Fix 8b section (lines ~1598–1651).

**Step 1 — Find chapter boundaries.** Before the `re.sub` call, locate all `<details class="chapter-section` start positions in the HTML text:

```python
chapter_starts = [m.start() for m in re.finditer(r'<details class="chapter-section', text)]
```

**Step 2 — Chapter-index lookup.** A helper that maps a text position to a chapter index (or -1 for pre-chapter content like title/TOC):

```python
def _chapter_of(pos):
    """Return chapter index for a position, or -1 for pre-chapter content."""
    idx = bisect.bisect_right(chapter_starts, pos) - 1
    return idx if idx >= 0 else -1
```

(Import `bisect` at top of file — already a stdlib module, no new dependency.)

**Step 3 — Per-chapter `hover_seen`.** Replace the global `hover_seen` set with a defaultdict of sets:

```python
hover_seen = defaultdict(lambda: {'relinquishment'})
```

Each chapter's set is pre-seeded with `'relinquishment'` (the book title's tooltip is always accessible from the title bar, so in-chapter occurrences should remain italic-only).

**Step 4 — Modify `hover_replace`.** Change the lookup from:

```python
if lookup in hover_lower and (lookup not in hover_seen or lookup in always_rich):
    if lookup not in always_rich:
        hover_seen.add(lookup)
```

to:

```python
ch = _chapter_of(m.start())
if lookup in hover_lower and (lookup not in hover_seen[ch] or lookup in always_rich):
    if lookup not in always_rich:
        hover_seen[ch].add(lookup)
```

**Step 5 — Update log message.** Change:

```python
print(f"Hover tooltips: {hover_count} first-occurrence terms")
```

to:

```python
n_chapters = len(chapter_starts)
print(f"Hover tooltips: {hover_count} tooltip instances across {n_chapters} chapters (per-chapter scoping)")
```

### What doesn't change

- `_register_hover()` — idempotent (first writer wins). Multiple chapters registering the same `hover_id` is a no-op after the first.
- `always_rich` set — `wormholes` still bypasses `hover_seen` entirely. Unchanged behavior, now redundant (since per-chapter scoping already re-triggers), but harmless to keep.
- Rich panel rendering — panels are shared (one per `hover_id`). All chapters reference the same panel. No duplication in the DOM.
- PDF behavior — `generate-hover.py` handles PDF footnotes independently. No change needed.
- `hover-definitions.yaml` — no changes.
- LaTeX sources — no changes. `\hovertip{}` macro unchanged.

### Pre-seeded terms

Only `'relinquishment'` is pre-seeded (in every chapter's set). Rationale: the book title in the top-level `<summary>` already renders a rich tooltip for "Relinquishment." In-chapter uses should be italic-only since the tooltip is always one click away.

No other terms are pre-seeded. `'wormholes'` and `'the-flat-title'` are title-level hovers with their own `hover_id` (e.g., `wormholes-title`, `the-flat-title`), distinct from the in-text `hover_id` (e.g., `wormholes`, `the-flat`). No collision, no need to suppress.

## Eigenvalue assessment

**This is a presentation-layer change.** No manuscript text changes. No term definitions change. The same tooltips appear — just in more places.

| Persona | Before | After | Δ |
|---|---|---|---|
| Chen (physicist) | Skipped summary, opened Flat chapter — no tooltip for "topological order" | Gets tooltip | +positive |
| Reeves (phil-of-science) | Similar pattern; key terms italic-only in later chapters | Gets tooltips | +positive |
| Arjun (CS, Bangalore) | Same | Gets tooltips | +positive |
| Doctorow | Likely reads linearly → no change | No change | Neutral |
| Jane (generalist, L1) | **Most affected.** Expands one chapter at a time. Currently sees undefined italic terms. | Gets tooltips where they're needed most | +significant |
| Rachel (working parent) | Same as Jane — dips into chapters non-linearly | Gets tooltips | +positive |
| Pastor Mike | Same pattern | Gets tooltips | +positive |
| Amir | Same pattern | Gets tooltips | +positive |
| Yusuf | Same pattern | Gets tooltips | +positive |

**F-mode check:** No triggers. Tooltips are factual definitions. More tooltips = more grounding.

**C-violation check:** N/A — no content changes.

**Verdict: universally positive eigenvalue.** Jane and Rachel (non-linear readers) benefit most. No persona regresses.

## Scope

**Edit:** `build/preprocess.py` — Fix 8b section only (~15 lines changed).

**No other files touched.**

**Regenerate:** `docs/downloads/Relinquishment.html`

## Phases (3)

### Phase 0 — Pre-flight

```bash
cd ~/software/relinquishment

# Confirm current global hover_seen
grep -n 'hover_seen = set()' build/preprocess.py
# expect line 1606

# Confirm hover_seen.add pattern
grep -n 'hover_seen.add' build/preprocess.py
# expect line 1627

# Confirm hover_seen membership check
grep -n 'not in hover_seen' build/preprocess.py
# expect line 1625

# Confirm chapter-section pattern exists
grep -c 'chapter-section' build/preprocess.py
# expect >10 (many references)

# Confirm bisect not already imported
grep -c 'import bisect' build/preprocess.py
# expect 0

# Count current tooltip instances (baseline)
make html 2>&1 | grep 'Hover tooltips:'
# Record this number as BASELINE_TOOLTIPS (expect ~16-20)
```

### Phase 1 — Edit

In `build/preprocess.py`:

**1a.** Add `import bisect` near the top imports (after existing stdlib imports).

**1b.** Add `from collections import defaultdict` if not already imported. (Check first — may already be there.)

**1c.** In the Fix 8b section (around line 1598–1651), make these changes:

1. After `hover_defs` is loaded and `hover_lower` is built, **before** the `hover_replace` function definition, add chapter-boundary detection:

```python
# Per-chapter tooltip scoping (Plan 0213): find chapter boundaries
chapter_starts = [m.start() for m in re.finditer(r'<details class="chapter-section', text)]

def _chapter_of(pos):
    """Return chapter index for a position, or -1 for pre-chapter content."""
    idx = bisect.bisect_right(chapter_starts, pos) - 1
    return idx if idx >= 0 else -1
```

2. Replace `hover_seen = set()` with:

```python
hover_seen = defaultdict(lambda: {'relinquishment'})
```

3. Remove `hover_seen.update(['relinquishment'])` (the defaultdict factory handles this).

4. In `hover_replace`, change:
   - `lookup not in hover_seen` → `lookup not in hover_seen[_chapter_of(m.start())]`
   - `hover_seen.add(lookup)` → `hover_seen[_chapter_of(m.start())].add(lookup)`

5. Update the log line to include chapter count:
   ```python
   n_chapters = len(chapter_starts)
   print(f"Hover tooltips: {hover_count} tooltip instances across {n_chapters} chapters")
   ```

### Phase 2 — Build + verify

```bash
cd ~/software/relinquishment

make html 2>&1 | grep 'Hover tooltips:'
# Expect: tooltip count HIGHER than BASELINE_TOOLTIPS
# Expect: chapter count matches known chapter count (~30+)

# Verify topological order now has tooltip in the-flat chapter
grep -c 'hover-term.*data-hover-id="topological-order"' docs/downloads/Relinquishment.html
# expect ≥2 (one in summary, one+ in later chapters)

# Verify 2DEG has tooltip in multiple chapters
grep -c 'hover-term.*data-hover-id="2deg"' docs/downloads/Relinquishment.html
# expect ≥2

# Verify relinquishment is still italic-only in chapters (not tooltip)
# The title-bar tooltip uses hover_id="relinquishment-title" (different ID),
# so in-text "relinquishment" should still be suppressed
grep -c '<em>relinquishment</em>' docs/downloads/Relinquishment.html
# expect ≥1

# Verifier still passes
python3 build/verify-deep-links.py
# expect OK

# Spot-check: wormholes still renders (always_rich unchanged)
grep -c 'data-hover-id="wormholes"' docs/downloads/Relinquishment.html
# expect ≥2 (unchanged from before)
```

**Smoke test:** Open HTML, test non-linear reading:

1. Collapse everything. Expand "Wormholes in the Flat" (skip Summary).
2. "topological order" should have tooltip (not just italic).
3. "the Flat" should have tooltip.
4. Now expand Summary — "topological order" ALSO has tooltip there.
5. Both tooltips show the same panel content.
6. "relinquishment" in any chapter body → italic only (suppressed — title bar has it).
7. Phone: tooltips render correctly on tap.

### Commit

```bash
git add build/preprocess.py docs/downloads/Relinquishment.html
git commit -m "Plan 0213: per-chapter tooltip re-triggering

The hover system used a document-global dedup set, so terms that first
appeared in the Summary lost their tooltips in all later chapters. Non-
linear readers (the primary HTML reading mode) saw unexplained italics.
Changed to per-chapter scoping: each independently navigable chapter gets
its own first-occurrence tracking. Same tooltip panels, more entry points.

Eigenvalue: universally positive — Jane/Rachel (non-linear readers) gain
most. No persona regresses, no F-mode triggers.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

## Acceptance

1. Tooltip count in build output is higher than baseline (more terms re-triggered)
2. `topological order` has tooltip spans in both summary.tex AND the-flat.tex regions of HTML
3. `relinquishment` remains italic-only in chapter bodies (pre-seeded suppression)
4. `wormholes` still renders everywhere (`always_rich` unchanged)
5. Deep-link verifier passes (50 entries)
6. Non-linear reading smoke test passes (open chapter without Summary → tooltips work)

## Risks

- **Very low.** Single-file edit, presentation-layer only. No manuscript changes, no definition changes.
- **Tooltip density.** Chapters with many hovertip terms now show more tooltips. Could feel "busy." Mitigated: the dedup still works *within* a chapter (second occurrence of `the Flat` in the same chapter → italic only). Only cross-chapter duplication changes.
- **`always_rich` redundancy.** `wormholes` in `always_rich` is now redundant (per-chapter scoping already re-triggers it). Keeping it is harmless — removing it is a micro-optimization for a future cleanup, not this plan.
- **Build performance.** `bisect.bisect_right` on ~30 chapter starts per hovertip match — negligible cost.
- **`defaultdict` side effect.** Accessing `hover_seen[ch]` for a new chapter auto-creates the set. This is the desired behavior (each new chapter starts with only `'relinquishment'` suppressed).
