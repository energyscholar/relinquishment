# Plan 0228: BORDERLINE Section Collapse + Deep Link Infrastructure

**Parent:** Plan 0225 Phase 4
**Depends on:** Phase 0 (commit 255967c), Phase 1 (commit aee79d8), Plan 0226 (commit 67cd057)
**Objective:** A science teacher should be able to assign reading from the book entirely with deep links. Every collapsed tech section needs: (1) a URL that auto-opens the section when visited, and (2) a visible click-to-copy 🔗 icon in the summary bar.

---

## Step 1: Deep link infrastructure in preprocess.py

In `build/preprocess.py`, function `collapse_tech_sections()` (~line 2800-2811), modify the wrapper construction.

**Current code:**
```python
wrapper = (
    f'<details class="tech-section">'
    f'<summary><span class="tech-title">{title_text}</span>{grade_span}</summary>\n'
    f'{content}'
    f'</details>\n'
)
```

**New code:**
```python
link_span = f'<span class="share-anchor" data-link-id="{label}" aria-hidden="true"></span>'
wrapper = (
    f'<details class="tech-section" id="{label}">'
    f'<summary><span class="tech-title">{title_text}</span>{grade_span}{link_span}</summary>\n'
    f'{content}'
    f'</details>\n'
)
```

This gives every collapsed section:
- `id` on `<details>`: landing anchor for `autoExpand()` to find and open
- `data-link-id` on share-anchor: URL fragment for click-to-copy (NOT `id` — duplicate IDs would break DOM)
- The existing `.share-anchor::after` CSS renders the 🔗 icon automatically

**Applies retroactively to all existing collapsed sections (12 from Phase 1) plus the 5 new ones.**

---

## Step 2: Fix share-anchor click handler in reader.js

In `build/reader.js`, the share-anchor click handler (~line 1250-1258). Two changes:

**2a. Add `e.preventDefault()` (~line 1253).** Without this, clicking 🔗 inside a `<summary>` toggles the section open/closed. `preventDefault` is safe for all share-anchors (spans outside `<summary>` have no default action to prevent).

**2b. Read `data-link-id` attribute.** Current code reads `anchor.id`. Tech-section share-anchors have no `id` — they use `data-link-id`.

Change (~line 1254):
```javascript
// BEFORE
var url = window.location.origin + window.location.pathname + '#' + anchor.id;
// AFTER
var id = anchor.dataset.linkId || anchor.id;
var url = window.location.origin + window.location.pathname + '#' + id;
```

---

## Step 3: CSS fixes in preprocess.py

Add to the tech-section CSS block (~line 892-949 of preprocess.py, inside the inline `<style>` string):

**3a. Scroll margin** — prevents summary from hiding behind sticky nav on deep link arrival:
```css
details.tech-section[id] { scroll-margin-top: 3em; }
```

**3b. Arrival indicator** — pulse the summary, not the entire expanded section:
```css
details.tech-section.deep-link-target { animation: none; }
details.tech-section.deep-link-target > summary {
  animation: highlight-pulse 2s ease-out;
}
```

The `highlight-pulse` keyframes already exist in `build/html.css` (line 219-222). Do not duplicate them.

**3c. Share-anchor visual harmony** inside tech sections:
```css
details.tech-section .share-anchor { vertical-align: middle; }
```

---

## Step 4: Add label for "The Thread Continues"

In `manuscript/spine/growing-a-mind.tex`, after the line `\section*{The Thread Continues}` (line 42), add:
```latex
\label{spine:gam-the-thread-continues}
```

Note: the existing `morphogenesis-as-computation` label in the same file has no `spine:gam-` prefix (pre-existing inconsistency). Do NOT change it — that would break existing deep links.

---

## Step 5: Update tech-collapse.yaml

Uncomment and complete 5 BORDERLINE entries in `build/tech-collapse.yaml`. Add them after the existing GA-AVERSE entries, under a BORDERLINE comment header.

```yaml
  # ── BORDERLINE — approved Phase 4 ────────────────────────────────────

  - title: "Freedman's Independent Conception (1988)"
    spine_file: manuscript/spine/the-braid.tex
    spine_label: "spine:braid-freedmans-independent-conception-1988"
    bridge_file: manuscript/bridge/pos10-the-braid.tex
    bridge_label: "pos10:freedmans-independent-conception-1988"
    assessment: BORDERLINE
    tooltip: "Fields Medalist Michael Freedman independently conceived topological quantum computation in 1988 — nine years before Kitaev published. The fundamental insight was accessible to top mathematicians by the late 1980s, consistent with a 1989 DARPA proposal."
    status: approved

  - title: "Kitaev and the Russian Question"
    spine_file: manuscript/spine/the-braid.tex
    spine_label: "spine:braid-kitaev-and-the-russian-question"
    bridge_file: manuscript/bridge/pos10-the-braid.tex
    bridge_label: "pos10:kitaev-and-the-russian-question"
    assessment: BORDERLINE
    tooltip: "Kitaev's 1997 paper was the public blueprint for topological quantum computation. If Bruce could see the implications from Oregon, so could any competent Russian science director. If the insight was independently derivable, it was never containable."
    status: approved

  - title: "Non-Abelian Anyons: Operational Proof"
    spine_file: manuscript/spine/the-braid.tex
    spine_label: "spine:braid-non-abelian-anyons-operational-proof"
    bridge_file: manuscript/bridge/pos10-the-braid.tex
    bridge_label: "pos10:non-abelian-anyons-operational-proof"
    assessment: BORDERLINE
    tooltip: "Under Possibility C, the system's real-world behavior is itself the proof that its components exist — the same logic by which quarks and the Higgs were confirmed. You don't need to isolate the parts if the whole works as predicted."
    status: approved

  - title: "The GCHQ Precedent"
    spine_file: manuscript/spine/the-factoring-game.tex
    spine_label: "spine:fg-the-gchq-precedent"
    bridge_file: manuscript/bridge/pos09-the-factoring-game.tex
    bridge_label: "pos09:the-gchq-precedent"
    assessment: BORDERLINE
    tooltip: "Classified agencies have independently discovered and suppressed major mathematical breakthroughs before. GCHQ invented public-key cryptography four years before RSA — and kept it secret for twenty-four years. The pattern is documented history."
    status: approved

  - title: "The Thread Continues"
    spine_file: manuscript/spine/growing-a-mind.tex
    spine_label: "spine:gam-the-thread-continues"
    bridge_file: manuscript/bridge/pos14-growing-a-mind.tex
    bridge_label: null
    assessment: BORDERLINE
    tooltip: "Turing showed brains grow from chemistry. Kauffman showed that growth process is universal — not specific to carbon. Wolfram showed complex systems compute spontaneously. Together: what minimal conditions does a substrate need to grow a mind? The answer points to the Flat."
    status: approved
```

Leave the 2 dead BORDERLINE entries commented with explanation:
```yaml
  # DEAD — "But What Is a Soliton?" is bridge-only (pos10). In spine,
  # soliton content is the opening paragraph of Hasslacher's Lattice.

  # DEAD — "From Emergence to Function" is bridge-only (pos11-the-demo).
  # pos11 content was folded into First Light (Plan 0152). No spine equivalent.
```

---

## Step 6: Build and verify

```bash
cd ~/software/relinquishment && make clean && make
```

### Verification checklist:

1. Build output shows **17 collapsed sections** (12 existing + 5 new)
2. Deep link count stable (tech-section share-anchors use `data-link-id`, not `id`, so they don't appear in the `dl:` count)
3. **Test an EXISTING section's deep link:** Open HTML, navigate to `#spine:gen-from-chemistry-to-computation`. Verify: chapter opens, tech section auto-expands, summary pulses with arrival indicator, scrolls into view below nav bar
4. **Test a NEW section's deep link:** Navigate to `#spine:braid-freedmans-independent-conception-1988`. Same checks.
5. **Test click-to-copy:** Click the 🔗 icon on any collapsed section. Verify: URL copied to clipboard, section does NOT toggle open/closed
6. **Test The Thread Continues boundary:** Verify it collapses correctly — content ends at "the question the subsequent chapters address." No chapter-closing content consumed.
7. Spot-check 2-3 existing `dl:` share-anchors still work
8. All 51 existing deep links resolve (check build output)

---

## Step 7: Commit

```bash
git add build/preprocess.py build/reader.js build/tech-collapse.yaml manuscript/spine/growing-a-mind.tex
git commit -m "Plan 0228: 5 BORDERLINE sections + deep links for all collapsed sections"
```

---

## What NOT to do

- Do NOT modify html.css (arrival indicator CSS goes in preprocess.py's inline style block)
- Do NOT modify any manuscript content beyond the one `\label` addition in Step 4
- Do NOT change the hover/tooltip system
- Do NOT change existing share-anchor IDs or `dl:` deep link targets
- Do NOT change the `morphogenesis-as-computation` label (pre-existing, would break links)

---

## Known anneal results

| # | Issue | Mitigation |
|---|-------|------------|
| 1 | Click 🔗 toggles section | Step 2a: `preventDefault` |
| 2 | Duplicate ID if share-anchor has `id` | Architecture: `id` on `<details>`, `data-link-id` on span |
| 3 | Arrival pulse covers entire section | Step 3b: suppress on `<details>`, animate on `<summary>` |
| 4 | Summary hides behind sticky nav | Step 3a: `scroll-margin-top` |
| 5 | Thread Continues is last section in chapter | Verified safe: `\chapterreturn` is empty in HTML |
| 6 | `text.find()` could match wrong element | Safe: `dl:` prefix separates deep-link IDs from `spine:` labels |
| 7 | Existing 12 sections need deep links too | Automatic: template change applies to all entries |
| 8 | Mobile icon crowding | Three small icons (✔ 0.8em, 🔗 0.6em) — monitor but likely fine |
| 9 | Fragment flash on page load | Inherent to `<details>` + JS — no fix without SSR |

---

*Plan written S59, 2026-04-19. Anneal: HIGH→MEDIUM→LOW, 9 issues identified and mitigated.*
