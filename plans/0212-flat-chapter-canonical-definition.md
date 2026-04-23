# Plan 0212 — Replace "The Flat" chapter preamble with canonical definition + SVG; add missing hovertip

## Status
Ready for Generator.

## Problem

Three issues in "Wormholes in the Flat" (`manuscript/spine/the-flat.tex`):

1. **Preamble uses wrong text.** Line 8 says *"The Flat™ is real physics. No one has asked whether anything lives there..."* — epistemic framing. The canonical definition — *"this book coins the Flat to mean..."* — lives only in hover tooltips (`build/hover-definitions.yaml`, `the-flat-title` entry). Non-hover readers enter the chapter without seeing the coining frame. Bruce: *"We're STILL not using the with-image canonical definition that is OVER THE TITLE."*

2. **The SVG cross-section diagram is tooltip-only.** The rich-panel hover over the chapter title includes an SVG showing a chip cross-section (two semiconductor blocks sandwiching a thin 2DEG layer with electron dots). This diagram is pedagogically load-bearing — it makes "two-dimensional electron gas" concrete. It should appear in the chapter body, not just on hover.

3. **"Topological order" on line 21 has no `\hovertip{}`.** The term has a hover definition (`hover-definitions.yaml:67`) but line 21 uses it bare. Note: `\hovertip{topological order}` already fires in `summary.tex:32` (first occurrence), so `hover_seen` dedup means this occurrence gets italic-only styling, not a tooltip. Acceptable: the canonical definition in the new preamble already explains topological order in context. If per-chapter re-triggering is desired, that's a separate plan for the hover system.

## Proposed edits

### Edit 1 — Replace preamble (the-flat.tex:8)

**OLD (line 8):**
```latex
\textit{\hovertip{The Flat}™ is real physics. No one has asked whether anything lives there --- an empty intersection in the literature, not a refutation. The physics below holds under all three possibilities. You do not need the story to be true for the substrate to be real.}
```

**NEW:**
```latex
\textit{This book coins \hovertip{the Flat}\texttrademark{} to mean ``any two-dimensional system embedded in three dimensions that can, under the right conditions, exhibit \hovertip{topological order}.'' Say that three times fast. Or say ``Flat.'' Different physics apply. In particular, the Flat supports topological wormholes. The Flat can be nonlocal in the technical physics sense.}

\textit{The Flat inside your computer chip is a 2DEG (two-dimensional electron gas). The Flat in Earth's magnetosphere is plasma confined to thin current sheets. We call the ocean floor the Deep and the emptiness between galaxies the Void. This book calls those thin worlds \textbf{the Flat}.}
```

**What's preserved:** TM marker, `\hovertip{}` on "the Flat", italic preamble style.

**What's replaced:** Epistemic framing (all four elements are redundant with their home chapters — see eigenvalue assessment below).

### Edit 2 — SVG injection (preprocess.py)

After the canonical definition preamble in the HTML output (detected by grep for the coining-frame text or the chapter anchor), inject the Flat cross-section SVG inline. This is the same SVG from `hover-definitions.yaml` `the-flat-title` entry.

In `build/preprocess.py`, add a post-pandoc injection step. Pattern:

```python
def inject_flat_diagram(html):
    """Insert the Flat cross-section SVG after the canonical definition in the Flat chapter."""
    FLAT_SVG = '''<figure class="inline-svg" style="text-align:center;margin:1em auto;">
<svg xmlns="http://www.w3.org/2000/svg" width="300" height="130" viewBox="0 0 300 130" style="display:block;margin:0 auto;">
  <title>Cross-section of a computer chip. Two grey blocks of 3D semiconductor sandwich a thin blue layer — the two-dimensional electron gas (2DEG). Blue dots are electrons confined to this flat layer. They can move left and right but not up or down. This is the Flat.</title>
  <defs>
    <linearGradient id="flat-inline-glow" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#2471a3" stop-opacity="0.05"/>
      <stop offset="50%" stop-color="#2471a3" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="#2471a3" stop-opacity="0.05"/>
    </linearGradient>
    <marker id="flat-inline-arr" viewBox="0 0 6 6" refX="5" refY="3" markerWidth="5" markerHeight="5" orient="auto">
      <path d="M 0,0 L 6,3 L 0,6 Z" fill="#1a5276"/>
    </marker>
  </defs>
  <rect x="30" y="20" width="240" height="25" rx="2" fill="#e0e0e0" stroke="#999" stroke-width="0.8"/>
  <text x="150" y="36" text-anchor="middle" font-size="8" fill="#666" font-family="sans-serif">3D material (bulk semiconductor)</text>
  <rect x="30" y="50" width="240" height="8" rx="1" fill="url(#flat-inline-glow)" stroke="#2471a3" stroke-width="1.5"/>
  <rect x="30" y="63" width="240" height="25" rx="2" fill="#e0e0e0" stroke="#999" stroke-width="0.8"/>
  <text x="150" y="79" text-anchor="middle" font-size="8" fill="#666" font-family="sans-serif">3D material (bulk semiconductor)</text>
  <circle cx="70" cy="54" r="2.5" fill="#2471a3" opacity="0.9"/>
  <circle cx="100" cy="54" r="2.5" fill="#2471a3" opacity="0.7"/>
  <circle cx="135" cy="54" r="2.5" fill="#2471a3" opacity="0.9"/>
  <circle cx="165" cy="54" r="2.5" fill="#2471a3" opacity="0.6"/>
  <circle cx="195" cy="54" r="2.5" fill="#2471a3" opacity="0.8"/>
  <circle cx="225" cy="54" r="2.5" fill="#2471a3" opacity="0.7"/>
  <circle cx="115" cy="55" r="2" fill="#2471a3" opacity="0.4"/>
  <circle cx="180" cy="53" r="2" fill="#2471a3" opacity="0.5"/>
  <circle cx="245" cy="54" r="2" fill="#2471a3" opacity="0.5"/>
  <line x1="58" y1="54" x2="48" y2="54" stroke="#1a5276" stroke-width="0.8" marker-end="url(#flat-inline-arr)"/>
  <line x1="252" y1="54" x2="262" y2="54" stroke="#1a5276" stroke-width="0.8" marker-end="url(#flat-inline-arr)"/>
  <text x="18" y="56" text-anchor="middle" font-size="7" fill="#2471a3" font-family="sans-serif" transform="rotate(-90,18,56)">2DEG</text>
  <text x="285" y="56" text-anchor="middle" font-size="7" fill="#2471a3" font-family="sans-serif" transform="rotate(90,285,56)">2DEG</text>
  <text x="150" y="104" text-anchor="middle" font-size="9" fill="#2471a3" font-family="serif" font-style="italic">electrons confined to two dimensions</text>
  <text x="150" y="118" text-anchor="middle" font-size="9" fill="#888" font-family="serif" font-style="italic">different physics applies here</text>
</svg>
<figcaption style="font-size:0.85em;color:#666;margin-top:0.3em;">The Flat: a two-dimensional electron gas sandwiched between bulk semiconductor layers.</figcaption>
</figure>'''

    # Insert after the second preamble paragraph (the Deep/Void paragraph)
    # Detect by the unique "This book calls those thin worlds" string
    marker = 'This book calls those thin worlds'
    idx = html.find(marker)
    if idx == -1:
        return html  # marker not found; skip silently

    # Find the end of the enclosing <p> or <em> tag after the marker
    close_p = html.find('</p>', idx)
    if close_p == -1:
        return html
    insert_point = close_p + len('</p>')
    return html[:insert_point] + '\n' + FLAT_SVG + '\n' + html[insert_point:]
```

Generator: integrate this into the existing `postprocess()` function (or equivalent) in preprocess.py. The SVG uses unique `id` attributes (`flat-inline-glow`, `flat-inline-arr`) to avoid collision with the same SVG in the hover panel (which uses `flat-glow` / `flat-arr`).

**PDF behavior:** No SVG. The .tex source has no image reference for this diagram. Acceptable — hover-panel SVGs are also HTML-only. If Bruce wants a PDF figure, that's a TikZ or `\includegraphics` follow-up.

### Edit 3 — Add `\hovertip{topological order}` on line 21

**OLD (line 21, relevant fragment):**
```latex
The important property is topological order.
```

**NEW:**
```latex
The important property is \hovertip{topological order}.
```

**Note:** This is the second (or later) occurrence of `\hovertip{topological order}` across the document — `summary.tex:32` fires first. Due to `hover_seen` dedup, this gets italic styling only, not a tooltip. Acceptable: the canonical definition in the new preamble already explains the term in context. Per-chapter tooltip re-triggering is a hover-system improvement for a separate plan.

Also add `\hovertip{}` on the second occurrence at line 49 for styling consistency:

**OLD (line 49, relevant fragment):**
```latex
...as a property of its topological order.
```

**NEW:**
```latex
...as a property of its \hovertip{topological order}.
```

## Eigenvalue assessment

**Persona stability (9 core):**

| Persona | Before | After | Δ |
|---|---|---|---|
| Chen (physicist) | PASS | PASS — 2DEG cross-section diagram + concrete examples are more credible than "is real physics" assertion | +slight |
| Reeves (phil-of-science) | PASS | PASS — coining frame is explicit nomenclature | Neutral |
| Arjun (CS, Bangalore) | PASS | PASS — concrete chip example, diagram | +slight |
| Doctorow | PASS | PASS | Neutral |
| Jane (generalist, L1) | PASS | PASS — "Say that three times fast" is reading-level humor; Deep/Void analogy helps; diagram makes 2DEG visual | +positive |
| Rachel (working parent) | PASS | PASS | Neutral |
| Pastor Mike | PASS | PASS | Neutral |
| Amir | PASS | PASS | Neutral |
| Yusuf | PASS | PASS | Neutral |

**F-mode check:** No triggers. Diagram slightly reduces F-crank (concrete > vague).

**C-violation check:** New preamble makes no Possibility-C-only claim. PASS.

**Lost epistemic elements:** All four (see table below) are redundant with their home chapters.

| Lost element | Home chapter | Status |
|---|---|---|
| "is real physics" | The Substrate section (same chapter, line 17) | Redundant |
| "empty intersection in the literature" | The Silence Gap + The Wrong Substrate preamble | Relocated |
| "holds under all three possibilities" | This chapter's closing (lines 65–68) | Relocated |
| "you do not need the story to be true" | three-possibilities.tex:83 (`story-may-be-false`) | Relocated |

**Verdict: stable eigenvalue.** Slight positive for Chen, Arjun, Jane. No losses.

## Scope

**Edit:**
- `manuscript/spine/the-flat.tex` — preamble replacement + two `\hovertip{}` additions
- `build/preprocess.py` — SVG injection function

**Regenerate:** `docs/downloads/Relinquishment.html`

## Phases (3)

### Phase 0 — Pre-flight

```bash
cd ~/software/relinquishment

# Confirm current preamble
grep -n 'is real physics' manuscript/spine/the-flat.tex         # expect line 8

# Confirm canonical definition not yet in any .tex
grep -rl 'coins.*the Flat' manuscript/                          # expect empty

# Confirm bare topological order on line 21
grep -n 'important property is topological order' manuscript/spine/the-flat.tex
# expect line 21, no \hovertip wrapper

# Confirm hover definition exists
grep -c 'topological order:' build/hover-definitions.yaml       # expect 1

# Confirm existing hovertip in summary (first occurrence)
grep -c 'hovertip{topological order}' manuscript/00-front/summary.tex  # expect 1
```

### Phase 1 — Edits

**1a.** Replace the-flat.tex line 8 (preamble) with the canonical definition (see Edit 1 above).

**1b.** Wrap "topological order" on line 21 and line 49 in `\hovertip{}` (see Edit 3 above).

**1c.** Add SVG injection function to preprocess.py (see Edit 2 above). Wire into the post-pandoc processing pipeline — call `inject_flat_diagram(html)` after the existing `collapse_chapters()` call or equivalent.

### Phase 2 — Post-edit verification + build + smoke

```bash
cd ~/software/relinquishment

# Coining frame in chapter body
grep -c 'coins.*the Flat' manuscript/spine/the-flat.tex                # expect 1

# Old preamble gone
grep -c 'is real physics' manuscript/spine/the-flat.tex                # expect 0

# Hovertip added
grep -c 'hovertip{topological order}' manuscript/spine/the-flat.tex    # expect 2

# Build
make html

# SVG present in HTML
grep -c 'flat-inline-glow' docs/downloads/Relinquishment.html         # expect 1

# Verifier still passes
python3 build/verify-deep-links.py                                     # expect OK: 50 entries
```

**Smoke test:** Open HTML, expand "Wormholes in the Flat."
1. Preamble reads: *"This book coins the Flat™ to mean..."*
2. Second paragraph: *"The Flat inside your computer chip is a 2DEG..."*
3. SVG cross-section diagram appears below the preamble (chip sandwich, blue 2DEG layer, electron dots).
4. Hover on "the Flat" in preamble → rich panel (reinforcement, not sole carrier).
5. "topological order" on line 21 → italic (may or may not have tooltip depending on hover_seen state).
6. Chapter body continues with "The stack chart..." unchanged.
7. Phone: diagram fits width, caption readable.

### Commit

```bash
git add manuscript/spine/the-flat.tex build/preprocess.py docs/downloads/Relinquishment.html
git commit -m "Plan 0212: Flat chapter preamble → canonical definition + inline SVG + hovertip

The canonical definition ('this book coins the Flat to mean...') lived
only in hover tooltips — non-hover readers never saw it. Replaced the
chapter preamble with the canonical coining-frame text + 2DEG/magnetosphere
examples. Added the Flat cross-section SVG diagram inline (was tooltip-only).
Wrapped bare 'topological order' in \hovertip{} (lines 21, 49).

Eigenvalue: stable across 9 personas, no F-mode triggers.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

## Acceptance

1. `grep -c 'coins.*the Flat' manuscript/spine/the-flat.tex` → 1 (coining frame in body)
2. `grep -c 'is real physics' manuscript/spine/the-flat.tex` → 0 (old preamble gone)
3. SVG cross-section appears inline after preamble in HTML (`grep -c 'flat-inline-glow'` → 1)
4. `\hovertip{topological order}` present at both occurrences (lines 21 and 49)
5. HTML builds clean with 50-entry verifier passing
6. Preamble reads naturally in browser; SVG renders correctly

## Risks

- **Very low.** One chapter preamble replacement, one SVG injection, two hovertip additions.
- **SVG `id` collision.** The hover-panel SVG uses `flat-glow` / `flat-arr`; inline SVG uses `flat-inline-glow` / `flat-inline-arr`. No collision. Generator: verify ids are distinct.
- **`hover_seen` dedup.** `\hovertip{topological order}` on line 21 gets italic-only because summary.tex:32 fires first. Accepted — the canonical definition in the new preamble already teaches the term. Per-chapter re-triggering is a separate hover-system improvement.
- **Hover redundancy.** Readers who hover "the Flat" now see the definition twice (preamble + tooltip). Reinforcement, not redundancy.
- **PDF.** No SVG in PDF output. Acceptable — matches existing hover-panel behavior. TikZ or `\includegraphics` equivalent is a follow-up.
