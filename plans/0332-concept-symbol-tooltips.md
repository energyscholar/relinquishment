# Plan 0332: Concept Symbol Tooltips

**Status:** Ready for Generator
**PTL:** PTL-168
**Files:** `build/preprocess.py`, `build/concept-symbols.yaml`, `manuscript/00-front/how-to-read.tex`
**Problem:** Concept symbols (⬡ ◈ ◉) are opaque — readers see a glyph with no explanation.
**Solution:** Add `title` attributes (browser-native hover tooltips) + brief legend in "How to Read This Book."

---

## Current State

- 3 active symbols: ⬡ flat, ◈ emergence, ◉ custodian (48 placements across 48 chapters)
- YAML already has `tooltip` field per symbol ("the Flat", "emergence", "Custodian")
- CSS already has `[data-concept][title] { cursor: help; }` — anticipating this exact change
- Python generates spans WITHOUT `title` attributes — the gap

## Phase 1: Add `title` to generated spans

In `inject_concept_symbols()` (~line 4800 of `build/preprocess.py`):

### 1A. Build tooltip lookup (after line 4817)

```python
symbol_tooltips = {}
for sname, sinfo in sym_cfg.get('symbols', {}).items():
    glyph = SYMBOL_GLYPHS.get(sname, '?')
    tip = sinfo.get('tooltip', sname)
    symbol_tooltips[sname] = glyph + ' ' + tip
```

### 1B. Combination spans (line 4909-4912)

Current:
```python
spans = ''.join(
    f'<span data-concept="{s}" data-concept-phase="{phase}" aria-hidden="true"></span>'
    for s in present
)
```

Add `title`:
```python
spans = ''.join(
    f'<span data-concept="{s}" data-concept-phase="{phase}" title="{symbol_tooltips.get(s, s)}" aria-hidden="true"></span>'
    for s in present
)
```

### 1C. Individual spans (line 4954-4955)

Current:
```python
return (f'<span data-concept="{cname_inner}" data-concept-phase="{phase}" '
        f'aria-hidden="true"></span>{m.group(0)}')
```

Add `title`:
```python
tip = symbol_tooltips.get(cname_inner, cname_inner)
return (f'<span data-concept="{cname_inner}" data-concept-phase="{phase}" '
        f'title="{tip}" aria-hidden="true"></span>{m.group(0)}')
```

### 1D. Chapter signature spans (line 4987)

Current:
```python
sig_span = f'<span class="chapter-symbols" aria-hidden="true">{glyphs}</span>'
```

Add `title` with all concept names joined:
```python
sig_tips = ' · '.join(symbol_tooltips.get(c, c) for c in assigned if c in symbol_tooltips)
sig_span = f'<span class="chapter-symbols" title="{sig_tips}" aria-hidden="true">{glyphs}</span>'
```

## Phase 2: Legend in "How to Read This Book"

In `manuscript/00-front/how-to-read.tex`, after the track stripe list (after line 35), add:

```latex
\vspace{0.5cm}

Small symbols mark recurring concepts: \textcolor[HTML]{b8860b}{$\hexagon$}\,the Flat\enspace \textcolor[HTML]{5b9bd5}{$\diamond$}\,emergence\enspace \textcolor[HTML]{c4a97d}{$\CIRCLE$}\,the Custodian. They appear faint in early chapters and grow stronger as concepts develop. In the interactive edition, hover over a symbol for its name.
```

NOTE to Generator: Check which LaTeX symbol commands are available. If `\hexagon` etc. don't work, use the Unicode characters directly: ⬡ ◈ ◉. Or use `\symbol{"2B21}` etc. with a Unicode-capable font. Match whatever the rest of the book does for these characters.

## Phase 3: Verify

```bash
cd ~/software/relinquishment && make html 2>&1 | tail -10
python3 build/verify-deep-links.py
```

Then in browser:
1. Hover over a ⬡ symbol — should show "⬡ the Flat" tooltip
2. Hover over a ◈ symbol — should show "◈ emergence" tooltip
3. Hover over a ◉ symbol — should show "◉ Custodian" tooltip
4. Hover over chapter header symbols — should show joined tooltip
5. Check "How to Read This Book" — legend visible
6. Check `cursor: help` appears on hover (dotted underline cursor)

## Do NOT

- Change which symbols are placed or where (that's concept-symbols.yaml, not this plan)
- Change the phase opacity system
- Add JavaScript for tooltip rendering (native `title` is sufficient)
- Change any other preprocess.py function
- Remove the visual-plain or print hiding rules

## Commit

`Plan 0332: concept symbol tooltips + reading guide legend`
