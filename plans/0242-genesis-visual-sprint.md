# Plan 0242 — Genesis Visual Sprint

**Status:** READY — Phases 4-9 of Plan 0244 (Master Execution Plan). All decisions locked S63.
**Author:** Auditor (Argus S63)
**Absorbs:** Plan 0232-genesis-illustrations (SUPERSEDED) — adds collapse tooltip mechanism + preview SVGs
**Depends on:** None (standalone)
**Chapter:** Genesis: The Edge of Chaos (1988–1992)

---

## What This Plan Does

Three things in one sprint:

1. **Builds 4 inline SVGs** for Genesis (from Plan 0232, never executed)
2. **Upgrades the collapse tooltip mechanism** to support rich HTML with SVG previews
3. **Creates 2 preview SVGs** for the Genesis collapsed-section tooltips

The reader experience after: hovering over a collapsed Genesis section shows a text summary PLUS a small illustration preview. The preview subtly signals "there's visual content inside." Expanding reveals the full chapter with inline diagrams.

---

## Why Genesis First

Genesis is the book's on-ramp to phase transitions, edge of chaos, and autocatalytic emergence. It has:
- 2 collapsed sections hiding the best illustration infrastructure in the book (filmstrip + domain buttons)
- A literal TODO in the source (line 46: TikZ figure, three-regime diagram)
- The highest concept density of any A-spine chapter
- A 6-panel filmstrip and 11-domain interactive diagram that no reader discovers unless they click

The visual gap: three concepts are text-only that need visual support (autocatalytic loop, substrate parallel, canopy problem) and one has a TODO placeholder (edge of chaos).

---

## Phase 1: Collapse Tooltip Mechanism Upgrade

**File:** `build/preprocess.py`, function `collapse_tech_sections()` (~line 2788)
**File:** `build/tech-collapse.yaml`

### Current behavior (line 2839-2840):
```python
grade_tooltip = html_mod.escape(tooltip) if tooltip else '...'
grade_span = f'<span class="tech-grade" data-hover="{grade_tooltip}"...'
```
Plain text only. HTML is escaped. No SVGs possible.

### New behavior:
tech-collapse.yaml entries gain an optional `hover_id` field. If present, `collapse_tech_sections()`:

1. Uses `data-hover-id="{hover_id}"` instead of `data-hover="{escaped_text}"`
2. After processing all sections, patches the hover-data JSON block in the HTML:
   - Parse the existing `<script id="hover-data">` JSON
   - Add entries for any `hover_id` that has a corresponding `html` field in tech-collapse.yaml
   - Re-serialize and replace

### Why patch the JSON (not modify patch()):
`collapse_tech_sections()` runs during `--fix-html`, a separate invocation from `patch()`. The `_hover_dict` was serialized to JSON during `patch()` and is already in the HTML. Adding entries requires modifying the serialized JSON. This is self-contained — no changes to `patch()` or hover-definitions.yaml loading.

### tech-collapse.yaml additions (Genesis entries only):

```yaml
  - title: "Buttons and Threads"
    # ... existing fields ...
    hover_id: "collapse-buttons-and-threads"
    html: |
      <p style="margin:0 0 0.5em;font-size:0.95em;line-height:1.5;">
      <strong>Buttons and Threads</strong></p>
      <p style="margin:0 0 0.4em;font-size:0.88em;line-height:1.4;">
      Scatter buttons on a floor and connect random pairs with thread.
      At a critical density, pulling one button lifts most of the room —
      not gradually, but all at once.</p>
      [PREVIEW SVG HERE — see Phase 3]
      <p style="margin:0;font-size:0.82em;line-height:1.3;font-style:italic;color:#888;">
      Expand for the full illustration sequence.</p>

  - title: "From Chemistry to Computation"
    # ... existing fields ...
    hover_id: "collapse-chemistry-to-computation"
    html: |
      <p style="margin:0 0 0.5em;font-size:0.95em;line-height:1.5;">
      <strong>From Chemistry to Computation</strong></p>
      <p style="margin:0 0 0.4em;font-size:0.88em;line-height:1.4;">
      If self-organization arises spontaneously above a complexity threshold
      in chemistry, the same principle applies to any substrate —
      including a quantum one.</p>
      [PREVIEW SVG HERE — see Phase 3]
      <p style="margin:0;font-size:0.82em;line-height:1.3;font-style:italic;color:#888;">
      Expand for the full illustration sequence.</p>
```

### Backward compatibility:
Entries without `hover_id` continue using `data-hover` with escaped text. Zero risk to existing collapsed sections.

### preprocess.py change (~15 lines):

```python
# In collapse_tech_sections(), replace:
grade_tooltip = html_mod.escape(tooltip) if tooltip else '...'
grade_span = f'<span class="tech-grade" data-hover="{grade_tooltip}"...'

# With:
hover_id = entry.get('hover_id')
if hover_id:
    grade_span = f'<span class="tech-grade" data-hover-id="{hover_id}" aria-hidden="true"></span>'
    rich_html = entry.get('html', '')
    if rich_html:
        rich_tooltips[hover_id] = {"t": tooltip, "h": rich_html}
else:
    grade_tooltip = html_mod.escape(tooltip) if tooltip else '...'
    grade_span = f'<span class="tech-grade" data-hover="{grade_tooltip}" aria-hidden="true"></span>'

# After all sections processed, patch hover-data JSON:
if rich_tooltips:
    json_pat = re.compile(r'(<script type="application/json" id="hover-data">)(.*?)(</script>)')
    m = json_pat.search(text)
    if m:
        hover_data = json.loads(m.group(2))
        hover_data.update(rich_tooltips)
        text = text[:m.start(2)] + json.dumps(hover_data, ensure_ascii=False) + text[m.end(2):]
```

### Acceptance tests (Phase 1):
1. Entries without `hover_id` still use `data-hover` (regression check)
2. Genesis entries use `data-hover-id` pointing to hover-data JSON
3. Hovering over collapsed "Buttons and Threads" shows rich panel (text for now — SVGs added in Phase 3)
4. `make html` exits 0

---

## Phase 2: Inline SVGs (4 new illustrations)

Build order: simplest first, validates pipeline.

### SVG-025: Autocatalytic Loop
**Placement:** After "The whole network sustains itself." (genesis.tex ~line 36)
**What:** Three molecules (A, B, C) in a circle with curved arrows. A→B→C→A. Self-sustaining loop.
**Colors:** Warm organic (amber/brown). Echoes filmstrip aesthetic.
**Size:** width="300" height="200"
**Jane test:** "Oh — the buttons with threads was THIS. Molecules helping each other exist."
**Difficulty:** Low. Clean geometry.

### SVG-026: Edge of Chaos (inline)
**Placement:** After Kauffman quote ending "best able to evolve as well." (genesis.tex ~line 51)
**What:** Hybrid — abstract shapes with tiny labels. Three regimes side by side:
- LEFT: rigid geometric grid, label "frozen"
- CENTER: narrow band with flexible interconnected nodes, label "edge"
- RIGHT: scattered dots flying apart, label "chaos"
Concept-first but oriented. No named substrates — the prose already names crystal and fire.
**Note:** Replaces the TODO comment at line 46-49. Remove the TODO.
**Colors:** Blue (frozen), green (edge), red (chaotic). Green band deliberately narrow.
**Size:** width="400" height="160"
**Jane test:** "Too stiff, too wild, juuust right."
**Difficulty:** Medium. Based on existing hover SVG-020 but richer.
**Decision:** Hybrid (Bruce S63).

### SVG-027: Substrate Parallel
**Placement:** After "the threshold was crossed." (genesis.tex ~line 62)
**What:** Split panel. Left: warm-colored beaker with molecules and catalytic arrows (echoes SVG-025). Right: cool-colored 2DEG substrate with anyonic quasiparticles and braiding arcs. Center: "same mathematics" with a threshold line.
**Colors:** Warm left (amber), cool right (blue), shared structure in middle.
**Size:** width="420" height="200"
**Jane test:** "Wait — the molecule thing and the computer chip thing are doing the SAME THING?"
**Difficulty:** Highest. Two visual systems unified. Must be clear without being reductive.

### SVG-028: Canopy Problem
**Placement:** After "the ecological niche is full." (genesis.tex ~line 75)
**What:** Cross-section of a forest. Two tall trees with full green crowns catching all sunlight (yellow rays). Below: a tiny seedling in deep shadow. No labels needed.
**Colors:** Green canopy, yellow light above, dark below. Simple, almost children's-book quality.
**Size:** width="350" height="220"
**Jane test:** "The little tree can't grow because the big trees got there first."
**Difficulty:** Low-medium. Organic shapes harder than geometric but composition is simple.

### Implementation:
Each SVG is a constant in `preprocess.py` with a new `inject_genesis_illustrations()` function. Pattern: same as `inject_flat_diagram()` and `inject_button_sequence()`. Insert after marker text, skip silently if marker not found.

Add to `--fix-html` pipeline between `inject_domain_buttons()` and `inject_questions_index()`.

### Deep Links for ALL SVGs (new requirement S63):

Every `<figure>` tag MUST have an `id` attribute. This enables:
- **Review:** Bruce navigates directly to each SVG via URL fragment
- **Sharing:** Readers can link to specific illustrations
- **Manifest:** svg-manifest.json tracks all SVGs with their anchors

**Add `id` to EXISTING SVGs in Phase B (while we're already modifying preprocess.py):**

| Existing SVG | Figure ID to add |
|-------------|-----------------|
| FLAT_SVG | `id="fig-flat-cross-section"` |
| FILMSTRIP | `id="fig-buttons-filmstrip"` |
| DOMAIN_SVG | `id="fig-domain-buttons"` |

**New SVGs get `id` at creation:**

| New SVG | Figure ID |
|---------|-----------|
| SVG-025 | `id="fig-autocatalytic-loop"` |
| SVG-026 | `id="fig-edge-of-chaos"` |
| SVG-027 | `id="fig-substrate-parallel"` |
| SVG-028 | `id="fig-canopy-problem"` |

Namespace: `fig-` prefix (NOT `dl:` or `custodian:` — those are for the questions index). The `verify-deep-links.py` script only checks `dl:`/`custodian:` namespaces and will not interfere.

After build, regenerate SVG manifest: `make svg-sheet`

### Review URLs (after build):
```
Relinquishment.html#fig-autocatalytic-loop   (SVG-025, Phase B)
Relinquishment.html#fig-edge-of-chaos        (SVG-026, Phase C)
Relinquishment.html#fig-substrate-parallel    (SVG-027, Phase C)
Relinquishment.html#fig-canopy-problem        (SVG-028, Phase C)
```
Bruce: open these in browser after each phase to review.

### CRITICAL — SVG Style Consistency (OOPS risk):
Before creating ANY new SVG, Generator MUST read the existing SVG constants in preprocess.py (FLAT_SVG, FILMSTRIP, DOMAIN_SVG) and extract:
- Exact hex color values (palette)
- Stroke widths
- Font family and size
- Corner radii and line-cap style
- Animation patterns (if any)

New SVGs must look like they belong to the same family. Visual inconsistency between existing and new illustrations makes the book look like it was illustrated by committee.

### SVG-027 "5-second test":
The split-panel (beaker left, 2DEG right) must pass a 5-second glance test: reader understands "these two things are doing the same thing" without studying. If the first draft is too busy, simplify. The insight is the parallel, not the detail. halt-and-report if SVG-027 needs iteration.

### Iteration Model:
SVGs rarely land on first draft. After each phase:
1. Generator builds HTML + pushes
2. Bruce opens review URLs (above) in browser
3. Bruce reviews: color, composition, clarity, consistency with existing SVGs, phone readability
4. If revision needed: Bruce pastes feedback to a new Generator session ("Phase B-rev" or "Phase C-rev")
5. Generator revises specific SVGs per feedback, rebuilds, pushes

Plan for ~1 revision cycle per phase. SVG-027 (split-panel) most likely to need iteration.

### Acceptance tests (Phase 2):
1. All 4 SVGs render in browser at correct positions
2. All 4 new SVGs have `id` attributes (`fig-*`) — verify with: `grep -c 'id="fig-' docs/downloads/Relinquishment.html`
3. All 3 existing SVGs also have `id` attributes (added in Phase B)
4. Total `fig-` count: 7 (3 existing + 4 new)
5. TODO comment removed from genesis.tex
6. No LaTeX changes (SVGs are HTML-only injection)
7. Filmstrip and domain buttons unaffected (verify by navigating to them via `#fig-buttons-filmstrip` and `#fig-domain-buttons`)
8. PDF renders normally (no SVG artifacts)
9. `make svg-sheet` regenerates manifest with updated asset count

---

## Phase 3: Collapse Tooltip Preview SVGs

Two small SVGs designed specifically for tooltip display. Not full diagrams — visual teasers that signal "illustrations inside."

### Preview A: "Buttons and Threads" tooltip
**What:** Ultra-compact 3-stage progression: 
- Left: 6 scattered dots (tan)
- Middle: same dots with 2 threads, one pair lifted
- Right: all dots lifted in a net, one red thread highlighted
**Size:** width="280" height="80" (fits tooltip panel)
**Style:** Same button colors as filmstrip. Minimal. Three snapshots of the phase transition.
**Purpose:** Reader sees the visual and thinks "oh, there are diagrams in there."

### Preview B: "From Chemistry to Computation" tooltip
**What:** Two circles side by side:
- Left circle: warm (amber), label "chemistry" in tiny text, 3 small arrows in a loop
- Right circle: cool (blue), label "quantum", 3 small braiding arcs
- Between: equals sign or "=" 
**Size:** width="260" height="90"
**Style:** Warm vs. cool, same concept as SVG-027 but radically simplified.
**Purpose:** Visual hint of the substrate parallel argument inside.

### Implementation:
These SVGs go directly into the `html` field of the tech-collapse.yaml entries (Phase 1). They're small enough to inline in YAML literal blocks.

### Acceptance tests (Phase 3):
1. Hover over collapsed "Buttons and Threads" → rich tooltip with text + mini filmstrip
2. Hover over collapsed "From Chemistry" → rich tooltip with text + substrate preview
3. Collapse tooltips on other sections unchanged (regression)
4. Mobile: tap shows tooltip correctly (existing reader.js touch handling)

---

## Phase Sequence

| Phase | What | Effort | Dependency |
|-------|------|--------|------------|
| 1 | Mechanism upgrade | ~1 hour | None |
| 2a | SVG-025 (autocatalytic loop) | ~1 hour | Phase 1 (for pipeline) |
| 2b | SVG-026 (edge of chaos inline) | ~1.5 hours | None |
| 3 | Preview SVGs in collapse tooltips | ~1.5 hours | Phase 1 |
| 2c | SVG-027 (substrate parallel) | ~2 hours | None |
| 2d | SVG-028 (canopy problem) | ~1 hour | None |

Phases 2a-2d are independent of each other. Phase 3 depends on Phase 1. Total: ~2 Generator sessions.

Recommended execution order: **1 → 2a → 3 → 2b → 2c → 2d**

Build the mechanism, build the simplest SVG to validate, deploy the collapse previews (Bruce's specific request), then build the remaining inline SVGs.

---

## Annealing Log (initial S63 + re-anneal S63 post-UQ)

### HIGH temperature (all candidates):
1. ✓ Mechanism upgrade for rich collapse tooltips
2. ✓ SVG-025 autocatalytic loop — **LOCKED: 3 molecules (A→B→C→A)**
3. ✓ SVG-026 edge of chaos inline (fills TODO) — **LOCKED: Hybrid (abstract shapes + labels)**
4. ✓ SVG-027 substrate parallel — **LOCKED: Full split-panel**
5. ✓ SVG-028 canopy problem — **LOCKED: Children's-book gentle**
6. ✓ Preview SVG for "Buttons and Threads" tooltip — **CONFIRMED**
7. ✓ Preview SVG for "From Chemistry" tooltip — **CONFIRMED**
8. ✗ Preview SVGs for ALL 18 collapsed sections — KILLED: scope creep. Do Genesis first, add others later.
9. ✗ Three-tier epistemic SVG (3→7→TQC) — DEFERRED to Plan 0230. Different concern.
10. ✗ Inline existing hover-only SVGs — PARTIALLY ABSORBED: SVG-026 handles edge of chaos.

### MEDIUM temperature (load-bearing test):
- SVG-025: Bridges filmstrip→chemistry. Without it, "catalytic reactions" is word salad. KEEP.
- SVG-026: Fills a literal TODO. Hybrid style: abstract shapes + tiny labels ("frozen," "edge," "chaos"). Concept-first but oriented. Prose already names crystal and fire — SVG should be complementary, not redundant. KEEP.
- SVG-027: Chapter's thesis in visual form. Full split-panel (Bruce S63): warm beaker left, cool 2DEG right, "same mathematics" center. Highest value, highest risk. KEEP.
- SVG-028: Strong text makes it optional. Image makes dark implication visceral. Children's-book gentle (fits p1). KEEP but lowest SVG priority.
- Preview SVGs: Bruce's specific request. The whole point of this plan. KEEP.
- Mechanism: One-time cost, reusable for all 23 collapsed sections. KEEP.

### LOW pass 1 (verify placements):
- SVG-025 marker: "The whole network sustains itself." — unique in genesis.tex ✓
- SVG-026 marker: "best able to evolve as well." — in Kauffman quote, unique ✓
- SVG-027 marker: "the threshold was crossed." — unique in line 62 ✓
- SVG-028 marker: "the ecological niche is full." — unique in line 75 ✓
- No marker collisions ✓
- TODO removal: lines 46-49 of genesis.tex ✓

### LOW pass 2 (interaction with 0244 master plan):
- Phases 4-9 of master plan. Phase 4 (mechanism) blocks 5-9. Phase 5 validates pipeline before Phase 6 deploys Bruce's request. SVGs 7-9 independent after mechanism. ✓
- No interaction with Plans 0165, 0241, 0223, 0185. Different files entirely. ✓
- genesis.tex: only the TODO removal (lines 46-49) modifies the .tex file. All SVGs inject at HTML level via preprocess.py. No LaTeX conflicts. ✓

**Rating: 9/10 (up from initial, all decisions locked).** All open questions resolved. Execution path clear. Phase 8 (SVG-027) remains highest risk — iterate rather than downgrade per Bruce's decision.

---

## Decisions (S63)

1. **SVG-025 molecule count:** Three (A→B→C→A). Auto-answered (cleanest).
2. **SVG-026 regime visuals:** Hybrid — abstract shapes with tiny labels ("frozen," "edge," "chaos"). Bruce S63.
3. **SVG-027 scope:** Full split-panel. Bruce S63.
4. **SVG-028 tone:** Children's-book gentle. Auto-answered (fits p1).
5. **Preview SVGs:** Confirmed — mini-filmstrip and mini-substrate-parallel. Auto-answered.

---

## Connection to Other Plans

- **Plan 0230 §3 (Unbuilt Bridge):** The three-tier argument (3→7→TQC) could eventually get its own illustration — a stepped diagram showing where proven ground ends and conjecture begins. NOT in this plan. Note for future.
- **Plan 0232-LLM (verification prompts):** Prompt #6 (Kauffman) asks about the edge of chaos. SVG-026 gives the reader a visual anchor before they ask their AI.
- **Plan 0241 (Engine tighten):** Independent. Can execute in parallel.
- **Plan 0223 (colophon):** Independent. Can execute in parallel.
- **Future:** Once mechanism works for Genesis, adding preview SVGs to The Braid, The Flat, and other chapters is a series of small independent tasks.

---

## Handoff Prompt (Phase 1 + 2a + 3)

```
You are the Generator. Read and execute plans/0242-genesis-visual-sprint.md,
Phases 1, 2a, and 3 only.

Phase 1: In build/preprocess.py function collapse_tech_sections(), add
support for hover_id field in tech-collapse.yaml entries. If present,
use data-hover-id instead of data-hover, and patch the hover-data JSON
block with the entry's html content. ~15 lines changed.

Phase 2a: Add inject_genesis_illustrations() function to preprocess.py.
Start with SVG-025 only (autocatalytic loop, 3 molecules A→B→C→A,
warm amber colors, ~300x200px). Inject after "The whole network
sustains itself." Add call in --fix-html pipeline.

Phase 3: Add hover_id and html fields to "Buttons and Threads" and
"From Chemistry to Computation" entries in tech-collapse.yaml. The html
contains existing tooltip text PLUS a compact preview SVG (~280x80px).
Design the preview SVGs per plan spec.

After: make html, verify in browser, commit, push. Report ≤5 lines.
```
