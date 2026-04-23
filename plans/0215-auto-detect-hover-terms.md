# Plan 0215 — Auto-detect hover terms from YAML (no manual `\hovertip{}` required)

## Status
**Status:** COMPLETE (verified S63 audit)
COMPLETE (verified S63 audit). Originally: Ready for Generator.

## Problem

`\hovertip{term}` macros are manually placed in .tex source files. Most terms are only wrapped at their first-ever mention in the book. Plan 0213 built per-chapter dedup (tooltips re-fire each chapter), but the `\hovertip{}` macros were never added to later chapters. Result: the chapter *about* wormholes and quantum teleportation has no tooltips on those terms.

The hover-definitions.yaml has ~90 definitions. The manuscript has ~15 chapters. Manual sprinkling is labor-intensive and rots when chapters change.

## Solution

Add a second pass to `preprocess.py`'s hover processing: after all explicit `\hovertip{}` markers are resolved (line 1653), scan each chapter's HTML for bare occurrences of yaml-defined terms and auto-wrap the first unseen occurrence per chapter.

This makes `hover-definitions.yaml` the single source of truth for *what gets a tooltip* AND *where it appears*. The `\hovertip{}` macro in .tex becomes optional (override/force-specific-location only).

## Critical constraints

### No tooltip-in-tooltip recursion

The auto-detection must NEVER scan inside:
1. **The hover-data JSON `<script>` block** — tooltip definitions contain terms that are also yaml keys. Wrapping them would create tooltips inside tooltips.
2. **Existing `<span class="hover-term" ...>` elements** — already processed.
3. **`<em>` elements from prior hovertip dedup** — already-seen terms rendered as italic.
4. **HTML tags and attributes** — never match inside `<...>`.
5. **`<script>` and `<style>` blocks** — never scan code.
6. **Tooltip panel HTML in the yaml `html:` fields** — these are emitted via `_register_hover()` into the JSON blob, not into chapter flow, so they're safe by architecture. But the auto-detect pass must run BEFORE the JSON injection (line 2082+), which it does naturally (hover processing is at line 1653, JSON injection at 2082).

### Term matching rules

1. **Longest match first.** Sort yaml keys by length descending before scanning. "quantum teleportation" must match before "quantum".
2. **Word boundaries.** Match whole words only (`\b` or equivalent). "the Flat" must not match inside "the Flatness" (if that existed).
3. **Case sensitivity.** Match the yaml key's exact case. "The Flat" (capitalized) matches "The Flat" in text. "quantum teleportation" (lowercase) matches case-insensitively.
4. **First occurrence per chapter only.** Use the existing `hover_seen[ch]` dict — if a term was already fired by an explicit `\hovertip{}`, don't auto-fire it again.
5. **Skip terms already in `hover_seen[ch]`** from the explicit pass. This means explicit `\hovertip{}` always takes priority.

### What not to auto-detect

Some yaml entries are structural, not terms that appear in prose:
- Title-bar entries (`relinquishment-title`, `wormholes-title`, `the-flat-title`)
- Stack chart entries (`stack-fire`, `stack-candle`, etc.)
- Interlude entries (`interlude-custodian:home`, etc.)
- Eval buttons (`eval-step-1`, `eval-step-2`)
- `buttons` entry

These should be excluded from auto-detection via a skip list or a naming convention filter (keys containing `-title`, `stack-`, `interlude-`, `eval-`, `buttons`).

## Implementation

### Where in preprocess.py

Insert after line 1656 (after the explicit `HOVERSTART` regex replacement and its summary print), before line 1658 (Custodian interludes). The auto-detect pass uses the same `hover_seen`, `hover_lower`, `hover_defs`, `chapter_starts`, `_chapter_of()`, and `_register_hover()` infrastructure.

### Pseudocode

```python
# --- Plan 0215: Auto-detect hover terms from YAML ---
# Second pass: for each chapter, find bare occurrences of yaml-defined
# terms and wrap the first unseen occurrence with tooltip HTML.
# Runs AFTER explicit \hovertip{} processing, using the same hover_seen dict.

# Keys to skip (structural, not prose terms)
AUTO_SKIP_PATTERNS = {'-title', 'stack-', 'interlude-', 'eval-', 'buttons'}

def _should_auto_detect(key):
    """Return False for structural yaml entries that aren't prose terms."""
    for pat in AUTO_SKIP_PATTERNS:
        if pat in key:
            return False
    return True

# Build sorted term list (longest first to prevent partial matches)
auto_terms = []
for key in hover_defs:
    if _should_auto_detect(key):
        auto_terms.append(key)
auto_terms.sort(key=len, reverse=True)

# Build regex for each term (word-boundary, case handling)
auto_patterns = []
for term_key in auto_terms:
    # Escape regex specials in term
    escaped = re.escape(term_key)
    # Word boundaries — use \b for most, but handle leading/trailing
    # non-word chars (e.g., terms starting with uppercase)
    pattern = rf'\b{escaped}\b'
    auto_patterns.append((term_key, re.compile(pattern, re.IGNORECASE)))

# Regions to exclude from scanning:
# - Inside HTML tags: <...>
# - Inside existing hover spans: <span class="hover-term"...>...</span>
# - Inside <em> tags (already-processed hovertips)
# - Inside <script> or <style> blocks
# - Inside <blockquote> with class="custodian-interlude" (Custodian voice)

def _find_scannable_regions(chapter_text):
    """Return list of (start, end) tuples of text safe to scan."""
    # Strategy: find all "forbidden" regions, return the gaps
    forbidden = []
    # HTML tags
    for m in re.finditer(r'<[^>]+>', chapter_text):
        forbidden.append((m.start(), m.end()))
    # Script/style blocks
    for m in re.finditer(r'<(script|style)[^>]*>.*?</\1>', chapter_text, re.DOTALL):
        forbidden.append((m.start(), m.end()))
    # Sort and merge overlapping forbidden regions
    forbidden.sort()
    merged = []
    for start, end in forbidden:
        if merged and start <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))
    # Return gaps
    regions = []
    prev_end = 0
    for start, end in merged:
        if prev_end < start:
            regions.append((prev_end, start))
        prev_end = end
    if prev_end < len(chapter_text):
        regions.append((prev_end, len(chapter_text)))
    return regions

auto_count = 0

# Process each chapter
for ch_idx in range(len(chapter_starts)):
    ch_start = chapter_starts[ch_idx]
    ch_end = chapter_starts[ch_idx + 1] if ch_idx + 1 < len(chapter_starts) else len(text)
    chapter_text = text[ch_start:ch_end]
    
    replacements = []  # (abs_pos, abs_end, replacement_html)
    
    for term_key, pattern in zip(auto_terms, auto_patterns):
        lookup = term_key.lower().replace('\u2019', "'").replace('\u2018', "'")
        
        # Skip if already seen in this chapter (from explicit \hovertip{} or prior auto-detect)
        if lookup in hover_seen[ch_idx]:
            continue
        
        # Skip always_rich terms — they're handled specially
        if lookup in always_rich:
            continue
        
        # Find first occurrence in scannable regions
        scannable = _find_scannable_regions(chapter_text)
        found = False
        for region_start, region_end in scannable:
            region_text = chapter_text[region_start:region_end]
            m = pattern.search(region_text)
            if m:
                abs_start = ch_start + region_start + m.start()
                abs_end = ch_start + region_start + m.end()
                matched_text = m.group(0)
                
                # Build the replacement span (same as hover_replace)
                value = hover_lower[lookup]
                if isinstance(value, dict):
                    raw_def = value.get('text', '')
                    target = value.get('target', '')
                    target_attr = f' data-hover-target="{html_mod.escape(target)}"' if target else ''
                    rich_html = value.get('html', '').rstrip('\n') or None
                else:
                    raw_def = str(value)
                    target_attr = ''
                    rich_html = None
                hover_id = re.sub(r'[^a-z0-9]+', '-', lookup).strip('-')
                _register_hover(hover_id, text=raw_def or None, html=rich_html)
                
                replacement = f'<span class="hover-term"{target_attr} data-hover-id="{hover_id}">{matched_text}</span>'
                replacements.append((abs_start, abs_end, replacement))
                hover_seen[ch_idx].add(lookup)
                auto_count += 1
                found = True
                break
            
        if found:
            continue  # next term
    
    # Apply replacements in reverse order (so positions don't shift)
    replacements.sort(key=lambda r: r[0], reverse=True)
    for abs_start, abs_end, replacement in replacements:
        text = text[:abs_start] + replacement + text[abs_end:]

if auto_count:
    print(f"  Auto-detect hover: {auto_count} additional tooltips sprinkled across {len(chapter_starts)} chapters")
```

### Key design decisions

1. **Scannable regions.** Instead of a complex negative-lookahead regex, split text into "safe to scan" regions (gaps between HTML tags). Simple, robust, handles all tag types including self-closing.

2. **Reverse-order replacement.** Apply replacements from end to start so earlier positions don't shift. Same technique used in many editor implementations.

3. **Shared infrastructure.** Uses the same `hover_seen`, `hover_lower`, `_register_hover()`, `_chapter_of()`, `chapter_starts`, and `always_rich` as the explicit pass. No duplication.

4. **Explicit wins.** If `\hovertip{term}` is in the .tex source, it fires first (line 1653). The auto-detect pass (this plan) runs second, respecting `hover_seen`. Manual placement always takes priority.

5. **No recursion possible.** The auto-detect scans chapter HTML text nodes only. Tooltip definitions live in the JSON blob (injected at line 2082, after this pass). Rich HTML panels are in `_hover_dict`, not in the chapter flow. The architecture prevents tooltip-in-tooltip by construction.

## Phases (3)

### Phase 0 — Pre-flight

```bash
cd ~/software/relinquishment

# Confirm current hover processing location
grep -n 'HOVERSTART' build/preprocess.py | head -5
# expect lines ~229, 258-259, 1653

# Confirm Plan 0213 infrastructure present
grep -n 'hover_seen = defaultdict' build/preprocess.py
# expect line 1615

# Confirm JSON injection is AFTER hover processing
grep -n '_hover_dict' build/preprocess.py | tail -5
# expect line 2082+ (well after 1653)

# Count current explicit hovertip instances
grep -c 'HOVERSTART' build/preprocess.py
# baseline

# Count terms in YAML that would be auto-detected
python3 -c "
import yaml
defs = yaml.safe_load(open('build/hover-definitions.yaml'))
skip = {'-title', 'stack-', 'interlude-', 'eval-', 'buttons'}
auto = [k for k in defs if not any(p in k for p in skip)]
print(f'{len(auto)} terms eligible for auto-detection out of {len(defs)} total')
"
```

### Phase 1 — Implement

Insert the auto-detection pass into `build/preprocess.py` after line 1656 (after the `Hover tooltips:` print statement), before line 1658 (Custodian interludes comment). Follow the pseudocode above.

**Implementation notes:**
- Import `bisect` is already present (Plan 0213)
- `html_mod` alias for `html` module is already present
- `_register_hover()` is defined at line 41
- `hover_lower`, `hover_seen`, `chapter_starts`, `_chapter_of()`, `always_rich` are all in scope
- The `text` variable is being mutated in place (string reassignment)

### Phase 2 — Build + verify

```bash
cd ~/software/relinquishment

# Build
make html

# Check auto-detect output
# expect: "Auto-detect hover: NN additional tooltips sprinkled across MM chapters"

# Verify no tooltip-in-tooltip
# The hover-data JSON should NOT contain any <span class="hover-term"> elements
python3 -c "
import json
with open('docs/downloads/Relinquishment.html') as f:
    text = f.read()
# Find the hover-data JSON
import re
m = re.search(r'<script[^>]*id=\"hover-data\"[^>]*>(.*?)</script>', text, re.DOTALL)
if m:
    data = json.loads(m.group(1))
    nested = [k for k, v in data.items() if 'hover-term' in json.dumps(v)]
    if nested:
        print(f'ERROR: tooltip-in-tooltip found in: {nested}')
    else:
        print('PASS: no nested tooltips in hover-data JSON')
"

# Verify key terms now have tooltips in The Flat chapter
python3 -c "
import re
with open('docs/downloads/Relinquishment.html') as f:
    text = f.read()
# Find The Flat chapter section
flat_start = text.find('Wormholes in the Flat')
flat_end = text.find('<details class=\"chapter-section', flat_start + 1)
if flat_end == -1: flat_end = len(text)
flat_text = text[flat_start:flat_end]
for term in ['quantum-teleportation', 'entanglement', 'anyon', 'classical-backchannel']:
    count = flat_text.count(f'data-hover-id=\"{term}\"')
    status = 'PASS' if count >= 1 else 'MISS'
    print(f'  {status}: {term} — {count} tooltip(s) in The Flat chapter')
"

# Verifier
python3 build/verify-deep-links.py    # expect OK

# Spot-check: open HTML, hover over "quantum teleportation" in The Flat chapter
# Should show tooltip: "Transferring quantum information from one place to another..."
```

**Smoke test in browser:**

1. Open HTML. Navigate to "Wormholes in the Flat" chapter.
2. Hover over "quantum teleportation" (line 33 area) — tooltip should appear.
3. Hover over "wormhole" — rich SVG panel should appear (always_rich).
4. Check that "The Flat" still has its tooltip (explicit `\hovertip{}` from .tex).
5. Navigate to a different chapter. Verify the same terms re-fire there.
6. Check that tooltip text is selectable/copyable.
7. Mobile: tap terms — panel should toggle.
8. Kill switch: disable tooltips, verify auto-detected terms also hidden.

### Commit

```bash
git add build/preprocess.py docs/downloads/Relinquishment.html
git commit -m "Plan 0215: auto-detect hover terms from YAML — tooltips sprinkle automatically

hover-definitions.yaml is now the single source of truth for tooltip
placement. After explicit \hovertip{} markers are processed, a second
pass scans each chapter for bare occurrences of yaml-defined terms and
wraps the first unseen occurrence with tooltip HTML. Longest-match-first
prevents partial matches. Scannable-region filtering prevents matching
inside HTML tags. No tooltip-in-tooltip recursion by architecture.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

## Eigenvalue assessment

**This is infrastructure, not content.** No prose changes. Readers see more tooltips on terms that already had definitions — just never displayed.

| Persona | Before | After | Δ |
|---|---|---|---|
| Jane (generalist) | Misses most tooltips (only fires at first-ever mention) | Key terms tooltipped in every chapter she reads | +strong |
| Rachel (working parent) | Same | Same improvement | +strong |
| Chen (physicist) | Tooltips mostly redundant for him | Neutral — more tooltips, still skippable | Neutral |
| Pastor Mike | Limited tooltip exposure | More gentle definitions available | +slight |

**F-mode check:** No triggers. Tooltips are reader-initiated (hover/tap). More available tooltips ≠ more intrusive.

**C-violation check:** N/A — infrastructure only, no prose.

## Risks

- **Low.** Single-file change (preprocess.py). Build-time only. Reversible.
- **Term matching false positives.** "Flat" as adjective vs. "the Flat" as noun. Mitigated: yaml keys include articles where needed ("the Flat", "The Flat"), and word-boundary matching prevents substring hits.
- **Performance.** ~70 terms × ~15 chapters × region scanning. Negligible vs. the rest of preprocess.py.
- **Scannable-region edge cases.** Malformed HTML could confuse region splitting. Mitigated: pandoc produces well-formed HTML, and our post-processing maintains it.
- **`always_rich` interaction.** The auto-detect pass skips `always_rich` terms (currently just 'wormholes') — these are handled exclusively by explicit `\hovertip{}` in .tex. If no explicit `\hovertip{wormholes}` exists in a chapter, wormholes won't auto-fire there. This is intentional: always_rich terms have special dedup behavior that the auto-detect pass shouldn't replicate without explicit authorial intent.

## Acceptance

1. Build produces "Auto-detect hover: NN additional tooltips" message
2. No "tooltip-in-tooltip" in hover-data JSON (verification script passes)
3. Key terms (quantum teleportation, entanglement, anyon) have tooltips in The Flat chapter
4. Explicit `\hovertip{}` still takes priority (test: check a term with both explicit and auto)
5. Per-chapter dedup still works (second occurrence in same chapter = italic only)
6. HTML builds clean, verifier passes
7. Browser smoke test: hover, tap, kill switch all work on auto-detected terms
8. No visual difference between explicit and auto-detected tooltips
