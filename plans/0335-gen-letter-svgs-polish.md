# Plan 0335: Gen Letter — SVG Deployment + Link Polish

**Source plan:** `~/.claude/plans/quizzical-floating-wreath.md`
**Status:** Phase 1 DONE. Phase 2 partially done. Phases 3-4 TODO.

---

## What's Already Done

### Phase 1 — SVG-046 (Five Thread Convergence) inline deployment: COMPLETE
- `inject_convergence_illustrations()` function added to `build/preprocess.py` (after `inject_genesis_illustrations`, before `inject_ms_diagrams`)
- Full SVG inline with namespaced gradient IDs: `ftc-nexus-glow`, `ftc-nexus-core`
- Chapter: `pos21:convergence-revisited`, marker: `"These are the scientific disciplines of the scientists"`
- Figure ID: `fig-five-thread-convergence`
- Call added to `__main__` block at line 5170 (between `inject_genesis_illustrations` and `inject_ms_diagrams`)
- Gallery manifest updated: SVG-046 status `draft` → `live`, source → `preprocess.py`

### Phase 2 — SVG-050 (Substrate Trinity) file created
- `build/images/raf-substrate-trinity.svg` exists (780×280 viewBox, three panels)
- Panel 1 Chemistry (warm: #c4a97d/#d4a574/#b8956a), nodes A/B/C
- Panel 2 Intellect (purple: #7d3c98/#2471a3/#27ae60), nodes TOPO/ACS/NKS
- Panel 3 Ethics (bronze/teal: #1A6B6A/#C4913B), nodes Mirror/Web/Integrity
- All three use identical 2.4s animation with 0/0.8/1.6s stagger — same as SVG-025/027
- Footer: "Same structure. Different substrates." in Georgia italic
- Namespaced marker IDs: `st-arr-warm`, `st-arr-intl`, `st-arr-eth`

---

## What Remains

### Phase 2 (continued) — Wire SVG-050 into book

1. **Add SVG-050 inline to `inject_genesis_illustrations()` in `build/preprocess.py`:**
   - Read `build/images/raf-substrate-trinity.svg` and embed as a Python string constant `SUBSTRATE_TRINITY`
   - Wrap in `<figure id="fig-substrate-trinity" class="inline-svg" style="text-align:center;margin:1.5em auto;">`
   - Figcaption: `"The same self-sustaining loop — in chemistry, intellectual phase space, and ethical phase space. Three substrates, one mathematical structure."`
   - Add to `svgs` list (line ~3044) with marker: `'the same process in different substrates'`
   - Insert AFTER the existing `SUBSTRATE_PARALLEL` entry (they're in different paragraphs; trinity goes at end of chapter)

2. **Add SVG-050 to `build/gallery-manifest.yaml`:**
   ```yaml
   - id: SVG-050
     name: raf-substrate-trinity
     status: live
     source: preprocess.py
     category: The Stack / Genesis
     chapter: genesis
     figure_id: fig-substrate-trinity
     marker: "the same process in different substrates"
     animated: true
     animation: "Synchronized cycling dots on three A→B→C loops — chemistry, intellect, ethics — all on identical 2.4s timing."
     description: "Three-panel figure showing the same autocatalytic loop structure operating in three different substrates."
     notes: "Visual proof of substrate independence. Synchronized timing IS the argument."
   ```

3. **Verify:** `make html` then check `docs/Relinquishment.html` for `fig-substrate-trinity` anchor.

### Phase 3 — Letter Content Polish

**File:** `~/software/aurasys-memory/response-gen-raf-emergence.md`

**File:** `~/software/aurasys-memory/response-gen-raf-emergence.md`

Exact edits (old → new). Use Edit tool with these exact strings:

**Edit 1 — Opening, add emergence deep link (line 5):**
```
OLD: A RAF set is emergence with a mathematical definition
NEW: A RAF set is [emergence with a mathematical definition](https://relinquishment.ai/Relinquishment.html#dl:life-is-a-phase-transition)
```

**Edit 2 — Q1 blurb, add animated loop link. Insert after line 13 ("It lives only in the network."):**
```
OLD: It lives only in the network.
NEW: It lives only in the network. There's an [animated version](https://relinquishment.ai/Relinquishment.html#fig-autocatalytic-loop) in the Genesis chapter — watch the dots cycle.
```

**Edit 3 — Puzzle section, full URL + add description (line 77):**
```
OLD: [UDHR Service Compatibility](Relinquishment.html#pz-log-t7-001) puzzle. You mostly work on the PDF, so you may not have seen the interactive puzzles yet. This one is a logic grid — six services, three UDHR articles, mark which violates which.
NEW: [UDHR Service Compatibility](https://relinquishment.ai/Relinquishment.html#pz-log-t7-001) puzzle. You mostly work on the PDF, so you may not have seen the interactive puzzles yet. This one is a logic grid — six services, three UDHR articles, mark which violates which. It's the kind of thing that looks simple until you start filling in the cells.
```

**Edit 4 — Q8 buttons-and-threads, full URL (line 85):**
```
OLD: [a sudden transition](Relinquishment.html#dl:buttons-and-threads)
NEW: [a sudden transition](https://relinquishment.ai/Relinquishment.html#dl:buttons-and-threads)
```

**Edit 5 — Q8 Five Thread Convergence, gallery → inline (line 89):**
```
OLD: [Five Thread Convergence](gallery.html#SVG-046) in the gallery
NEW: [Five Thread Convergence](https://relinquishment.ai/Relinquishment.html#fig-five-thread-convergence) in the book
```

**Edit 6 — Q8 substrate reference, parallel → trinity (line 91):**
```
OLD: [substrate parallel](Relinquishment.html#fig-substrate-parallel) figure showing the same autocatalytic loop in chemistry and quantum physics — two panels, same topology, different labels. You'd be the third panel.
NEW: [substrate trinity](https://relinquishment.ai/Relinquishment.html#fig-substrate-trinity) figure showing the same autocatalytic loop in chemistry, intellectual phase space, and ethics — three panels, same topology, different labels. You ARE the third panel.
```

### Phase 4 — Build + Verify

1. `make html` from `~/software/relinquishment/`
2. Click-test every deep link from the letter:
   - `#dl:life-is-a-phase-transition`
   - `#fig-autocatalytic-loop`
   - `#dl:buttons-and-threads`
   - `#fig-five-thread-convergence` (Phase 1)
   - `#fig-substrate-trinity` (Phase 2)
   - `#pz-log-t7-001`
3. Verify gallery manifest: SVG-046 live, SVG-050 registered
4. Final letter read-through as Gen would experience it

---

## Files to Modify

| File | Action |
|------|--------|
| `build/preprocess.py` | Add SUBSTRATE_TRINITY inline SVG + injection entry |
| `build/gallery-manifest.yaml` | Add SVG-050 entry |
| `~/software/aurasys-memory/response-gen-raf-emergence.md` | Full URL conversion + deep links + polish |

## Acceptance Criteria

- `make html` succeeds with no errors
- All 6 anchors resolve in `docs/Relinquishment.html`
- All animated SVGs play (and respect `prefers-reduced-motion`)
- Letter contains only full `https://relinquishment.ai/` URLs
- No gradient/marker ID collisions (all namespaced with `st-` prefix)
