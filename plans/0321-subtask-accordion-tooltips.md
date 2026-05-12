# Subtask: Section 3 Accordion + PhD Seed Accordions

**Output:** Modify `build/images/scientific-revolutions-chapter.html` to wrap
physicist-level detail in collapsible `<details>` elements. Add CSS for the
new accordion class.
**Commit:** `Plan 0321: accordion physicist detail in Anomaly Accumulation + PhD seeds`
**Read first:** The chapter HTML, especially Section 3 (lines 267–285) and
all `phd-seed` blockquotes.

## Rationale

Section 3 "Anomaly Accumulation" re-summarizes four research programs that
GA readers already know from "Three Possibilities," "The Flat," and "The
Silence Gap." The Kuhnian framing (intro + closing) is new and essential.
The program descriptions are physicist-level detail — valuable for specialists,
skippable for general readers who've been following the argument.

The existing tooltip system covers the key terms: "autocatalytic," "fractional
quantum Hall effect," "topological quantum computation," "anomaly accumulation."
A GA reader who hovers over these terms in the visible summary gets the
essential information without needing the full paragraphs.

PhD seed blockquotes are physicist bait — paper titles for graduate students.
Valuable but not load-bearing for the chapter's argument.

## Section 3 Accordion

### What Stays Visible (OPEN)

The following paragraphs remain outside any `<details>` element — always
visible, forming the section's readable spine:

1. **Opening definition** (line 269):
   "Kuhn's anomalies are not errors. They are published facts..."

2. **One-line summary** (line 271):
   "The current paradigm in quantum computing has its own anomalies —
   not errors, but gaps. Four research programs, each well-established,
   converge on a question none of them has asked."

3. **Disciplinary seams** (line 281):
   "This is not unusual. Kuhn observed that anomalies often hide in
   disciplinary seams..."

4. **Kuhnian vocabulary** (line 283):
   "In Kuhn's terminology, these are anomalies..."

### What Collapses (CLOSED by default)

Wrap lines 273–279 (the four program descriptions) in:

```html
<details class="tech-section">
  <summary>The four converging research programs</summary>

  <p><strong>Autocatalytic set theory.</strong> Stuart Kauffman's work...</p>
  <p><strong>Fractional quantum Hall anyons.</strong> The fractional quantum...</p>
  <p><strong>Topological quantum computation.</strong> Kitaev's 2003 proposal...</p>
  <p><strong>The unstudied intersection.</strong> A literature search across...</p>

</details>
```

The `<summary>` text — "The four converging research programs" — echoes
the visible paragraph above it. A GA reader sees the summary, understands
four programs converge, and can skip to the Kuhnian analysis. A physicist
clicks to read the detail.

### Resulting Flow for GA Reader

> Kuhn's anomalies are not errors...
>
> The current paradigm has its own anomalies... Four research programs
> converge on a question none of them has asked.
>
> ▸ The four converging research programs [closed]
>
> This is not unusual. Kuhn observed that anomalies often hide in
> disciplinary seams...
>
> In Kuhn's terminology, these are anomalies...

The argument flows without interruption. The detail is one click away.

## PhD Seed Accordions

Three `<blockquote class="phd-seed">` elements exist in the chapter.
Wrap each in a `<details>` with summary "Research opportunity":

```html
<details class="phd-seed-section">
  <summary>Research opportunity</summary>
  <blockquote class="phd-seed">
    <em>"Autocatalytic dynamics in fractional quantum Hall substrates:
    a computational feasibility study"</em> — a paper title waiting
    for an author.
  </blockquote>
</details>
```

These are closed by default. They're gifts for physicists, not
structural elements of the argument.

## CSS

Add to the existing `<style>` block:

```css
/* Collapsible physicist detail */
.tech-section {
  margin: 1rem 0;
  border-left: 2px solid rgba(140, 140, 160, 0.25);
  padding-left: 1rem;
}
.tech-section summary {
  cursor: pointer;
  color: #a09890;
  font-style: italic;
  font-size: 0.95rem;
  margin-bottom: 0.5rem;
}
.tech-section summary:hover {
  color: #c8b898;
}
.tech-section[open] summary {
  margin-bottom: 1rem;
}

/* PhD seed accordions */
.phd-seed-section {
  margin: 1rem 0;
}
.phd-seed-section summary {
  cursor: pointer;
  color: #5c7c9c;
  font-style: italic;
  font-size: 0.85rem;
}
.phd-seed-section summary:hover {
  color: #7c9cbc;
}
```

The `.tech-section` style matches the existing `tech-section` pattern
used 24 times in the book build (closed by default, left-border accent,
italic summary). The `.phd-seed-section` style uses the PhD-seed blue
accent (#5c7c9c) for visual consistency with the existing `phd-seed`
blockquote styling.

## Tooltip Dependencies

These tooltips already exist in `build/hover-definitions.yaml` and will
be auto-injected by `preprocess.py` when the chapter is built:

| Term | Status |
|------|--------|
| autocatalytic | Exists |
| fractional quantum Hall effect | Exists |
| topological quantum computation | Covered by "topological protection" |
| anomaly accumulation | Exists (added this session) |
| Kuhn cycle | Exists (added this session) |
| paradigm shift | Exists (added this session) |
| Possibility A1 | Exists (added this session) |
| Possibility A2 | Exists (added this session) |
| non-abelian anyon | Exists |
| poised realm | Exists |

No new tooltips needed. The existing set covers every technical term
that appears in the visible (non-collapsed) text.

**Note:** "topological quantum computation" as a standalone phrase does
not have its own tooltip entry — it's covered conceptually by
"topological protection." If this proves insufficient after testing,
add a dedicated entry in a follow-up. Not blocking.

## What NOT to Accordion

Everything else stays open. Specifically:

- **Section 1 (The Pattern):** Entry point + animation. Must be visible.
- **Section 4 (Life in the Flat):** Emotional core, A1/A2 fork, humor
  beat. Collapsing any of this would destroy the chapter's rhythm.
- **Section 4b (Beyond the Lab):** 100 words. Too short to collapse.
- **Section 5 (How It Plays Out):** Structural argument. Needs to flow.
- **Section 6 (Social Process):** Contains the F1-armored conditional
  conclusion — the chapter's payoff. Must be visible.
- **Section 7 (Reader's Position):** 60-word closing. Must be visible.
- **SVG-055 (Spectrum):** Already in `<details open>`. Leave as-is.

Over-accordioning fragments reading flow. One tech-section collapse
and three PhD-seed collapses is the right amount.

## Do NOT

- Collapse any text outside Section 3's program descriptions
- Collapse any part of Sections 4–7
- Change the SVG-055 accordion (already `<details open>`, leave it)
- Modify any text content — only wrap in `<details>` elements
- Add new tooltips (existing set is sufficient)
- Change the chapter's visual style beyond the new CSS classes

## Report

Confirm: Section 3 accordion collapses/expands correctly, summary text
visible when closed, four program paragraphs appear when opened. PhD
seed accordions collapse correctly with "Research opportunity" summary.
Verify no text was lost or reordered. Open in browser and test both
states (open/closed) for each accordion.
