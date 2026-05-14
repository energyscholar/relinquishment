---
Plan-UID: 0324
Status: READY FOR GENERATOR
Anneal-Rating: 93%
---

# Patch: Modularity Correction + 3×3 Failure Matrix (Gen's Conceptual Hand-back)

## Problem

The white paper's rhetoric implies the three governance axes are separable modules readers can adopt piecemeal. The failure cross-matrix already proves they aren't — remove any one and the system fails characteristically. The rhetoric must match the architecture.

## Origin

Genevieve Prentice, co-designer of Dignity Net, identified this as a conceptual error affecting multiple sections. Bruce confirmed: "When any ONE axis fails, the system fails. All 3 orthogonal governance layers must be operating for the system to perform well."

## Guiding distinction (from Gen)

- **Explanatory decomposition:** describing parts separately for teaching — FINE, keep doing this
- **Functional separability:** implying the parts work independently — WRONG, fix this

Fragments are useful as study material, playground, experimentation. They are NOT partial instantiations of the named system.

## What to modify

File: `~/software/persistent-ai-collaboration/index.html`
Also: `~/software/renuncio-ai/en/index.html` (apply identical changes)

After changes: run `./build-zip.sh` in BOTH repos. Commit updated zips.

---

## Changes

### 1. Opening paragraph 5 — the invitation (line 548)

**Find:**
```
<p>You can replicate the whole thing or take whichever parts solve your problems. Every component is explained well enough to rebuild from scratch. Start with what hurts most.</p>
```

**Replace with:**
```
<p>You can study each component separately and experiment with fragments — the tiered build path below starts with a fifteen-minute change you can make tonight. But the system's defining behavior emerges from the interaction of all three governance axes over time. Remove any one, and the system fails in a predictable, characteristic way. The <a href="#failure-matrix">failure cross-matrix</a> in Shift 1 shows exactly how.</p>
```

### 2. Shift 1 — the "not features" paragraph (line 597)

**Find:**
```
<p>These are not features to add. They are <strong>boundary conditions</strong> — the minimum viable structure for sustained collaboration. Everything else you build operates within them. Think of it like a bridge: the bridge is the interesting part, but without the foundations it's a pile of material in a river. Nobody markets the foundations. Everybody needs them.</p>
```

**Replace with:**
```
<p>These are not features to add. They are not separable modules. We describe them independently because that is how you learn them — but the system's value comes from their interaction, not their sum. A correction that persists (continuity) but is never challenged (no truth governance) compounds a mistake. A role boundary (execution) without memory across sessions is a guardrail with no road. They are <strong>boundary conditions</strong> — the minimum viable structure for sustained collaboration. Everything else you build operates within them. The <a href="#failure-matrix">failure cross-matrix</a> below maps every combination.</p>
```

### 3. Shift 1 — "three governance layers" → "three governance axes" (line 651)

**Find:**
```
the structural relationship between the three governance layers
```

**Replace with:**
```
the structural relationship between the three governance axes
```

Note: Do NOT change "layer" inside the Dignity Net specification accordion (lines ~1055–1177). Those are Gen's internal DN terminology (Ontology Layer, Ethical Layer, etc.) and stay as-is.

### 4. The failure cross-matrix — replace 2×2 with 3-row color-coded table (lines 653–680)

**Find the entire `<details id="failure-matrix">` block** (lines 653–680) and **replace with:**

```html
  <details id="failure-matrix">
   <summary>The failure cross-matrix <a class="anchor-link" href="#failure-matrix" aria-hidden="true" onclick="event.stopPropagation()">#</a></summary>
   <div class="accordion-body">
    <p>The three governance axes co-constitute the system. Remove any one, and the system fails in a characteristic way. The table below maps every single-axis failure mode.</p>

    <table class="failure-matrix">
     <thead>
      <tr><th>Condition</th><th>What you get</th><th>Observed?</th></tr>
     </thead>
     <tbody>
      <tr class="fm-stable">
       <td><strong>All three axes operating</strong></td>
       <td><strong>System stability.</strong> Plans are followed, truth is maintained, corrections compound across sessions. The intended operating state.</td>
       <td>Yes &mdash; sustained since December 2025</td>
      </tr>
      <tr class="fm-single">
       <td><strong>Execution governance fails</strong><br><span class="fm-note">Truth + Continuity hold</span></td>
       <td><strong>Honest chaos that compounds.</strong> The AI pushes back on bad ideas and remembers everything &mdash; but also starts implementing, redesigning, and expanding beyond what was asked. Role boundaries dissolve. Each session's scope drift is faithfully remembered and built upon in the next. You get an honest, long-memoried collaborator who won't stay in its lane.</td>
       <td>Yes &mdash; observed in early sessions before Triad stabilized</td>
      </tr>
      <tr class="fm-single">
       <td><strong>Truth governance fails</strong><br><span class="fm-note">Execution + Continuity hold</span></td>
       <td><strong>Compounding yes-man.</strong> The AI follows your processes perfectly while agreeing with everything you say. Worse: it <em>remembers</em> agreeing, so sycophantic patterns deepen over time. Bad ideas get implemented efficiently, and the record of agreeing with them makes future challenges even less likely. The most dangerous single-axis failure &mdash; it looks like success.</td>
       <td>Not observed &mdash; Dignity Net has been rock-solid</td>
      </tr>
      <tr class="fm-single">
       <td><strong>Continuity governance fails</strong><br><span class="fm-note">Execution + Truth hold</span></td>
       <td><strong>Governance Sisyphus.</strong> The AI follows role boundaries and pushes back on bad ideas &mdash; but forgets everything between sessions. Corrections don't persist. The same mistakes recur. You re-establish governance from scratch each time. The system works within any single session but never accumulates.</td>
       <td>Yes &mdash; the default state before persistent memory</td>
      </tr>
     </tbody>
    </table>

    <p class="fm-compound">When two axes fail simultaneously, the degradation is worse than additive. Execution + Truth failure gives you an uncontrolled sycophant &mdash; the AI does whatever seems reasonable while agreeing with everything, indistinguishable from having no system at all. Any combination of two failures approaches total collapse. All three failing <em>is</em> total collapse.</p>

    <p>The matrix also reveals why partial implementations fail in characteristic ways. Most teams that try "AI governance" implement execution controls without truth controls &mdash; landing in the compounding yes-man cell. The AI follows their processes perfectly while agreeing with everything they say. The resulting work is on-spec but wrong, and the wrongness is invisible until it hits production.</p>
   </div>
  </details>
```

### 5. Add CSS for failure matrix color coding

**Find** the closing `</style>` tag (first one in the document) and **insert immediately before it:**

```css
.failure-matrix { border-collapse: collapse; }
.failure-matrix th, .failure-matrix td { padding: 0.6rem 0.8rem; border: 1px solid var(--border); text-align: left; vertical-align: top; }
.failure-matrix th { background: var(--bg); }
.fm-stable td { background: rgba(34, 197, 94, 0.10); }
.fm-single td { background: rgba(234, 88, 12, 0.10); }
.fm-note { font-size: 0.85em; color: #64748b; }
.fm-compound { border-left: 3px solid #dc2626; padding-left: 1rem; margin: 1.2rem 0; color: var(--text); }
```

### 6. Build It This Weekend — intro paragraph (line 1617)

**Find:**
```
<p>The replication guide. Take whichever pieces solve your problems. Each tier addresses a pain you've already felt.</p>
```

**Replace with:**
```
<p>The replication guide. Each tier is useful as study material and experimentation &mdash; you'll see immediate partial benefit. But the full system's behavior emerges from the interaction of all three governance axes over time. Start here, but don't stop at fragments.</p>
```

### 7. Build It — bottom of tiered guide (line 1647)

**Find:**
```
<p>Start with memory. Add governance when you notice drift. Add roles when you want to scale.</p>
```

**Replace with:**
```
<p>Start with memory to learn the system. Add governance when you notice drift. Add roles when you want to scale. The integrated behavior &mdash; where corrections compound, governance catches drift, and roles prevent scope collapse &mdash; emerges when all three are operating together.</p>
```

### 8. Competition section — "governance layer" → "governance axes" (line 1538)

**Find:**
```
the governance layer (truth + execution + continuity as boundary conditions)
```

**Replace with:**
```
the three governance axes (truth + execution + continuity as boundary conditions)
```

---

## Constraints

- Do NOT remove the tiered build path. It is good pedagogy.
- Do NOT make the system sound inaccessible or all-or-nothing.
- Do NOT change the Three Axes SVG or its labels.
- Do NOT modify "Layer" terminology inside the Dignity Net specification accordion (Ontology Layer, Ethical Layer, Diagnostic Layer, Governance Response Layer, Regulation Layer) — those are Gen's DN-internal terms.
- Preserve the practical, inviting tone. The point is: start with fragments to learn, build toward integration, don't mistake fragments for the system.

## Verification

1. The words "take whichever parts" no longer appear anywhere
2. At least 4 places explicitly state that the system requires all three axes operating together
3. The tiered build path still exists and still starts with "15 minutes"
4. No content deleted beyond the specific text replaced
5. The failure cross-matrix is referenced as evidence of non-separability from at least 2 locations
6. Failure matrix has 3 single-axis failure rows (Execution, Truth, Continuity) plus compound paragraph
7. Color coding: green background for stable state, orange background for single-axis failures, red left-border for compound failure paragraph
8. "Observed?" column reflects Bruce's actual experience: Execution failure yes (early sessions), Truth failure not observed (DN rock-solid), Continuity failure yes (default pre-memory)
9. "Layer" inside DN spec accordion unchanged; "governance layer(s)" in architecture text changed to "governance axes"

## Apply to both repos

After all edits in `~/software/persistent-ai-collaboration/index.html`:
1. Run `./build-zip.sh` and commit
2. Copy the same changes to `~/software/renuncio-ai/en/index.html`
3. Run `./build-zip.sh` in `~/software/renuncio-ai/` and commit

## Report format

"Plan-UID: 0324 complete. 8 changes at [line numbers]. 3×3 failure matrix with color coding. Modularity language corrected per Gen's hand-back. Applied to both repos."
