# Plan 0146: Title Page into Book Summary (Disappearing Cover)

**Status:** DONE (implemented prior to 2026-04-10; confirmed by Generator C)

## Context

Title Page takes a whole menu line delivering little value. The reader should see the title page on first load (cover experience), but it should vanish when they open the book and not take menu space. Copyright/license boilerplate moves to Appendices near Colophon.

## UX

**Page loads (collapsed):**
```
▶ Relinquishment — Wormholes in the Flat
  by Bruce Stephenson, Genevieve Prentice & Argus
  Three narrative threads. Real science. Real people.
  Three possible explanations. You decide.
  © 2026 Bruce Stephenson & Genevieve Prentice · CC BY-ND 4.0
```
Must fit on a phone with room to spare. Compact typography.

**User clicks triangle (expanded):**
```
▼ Relinquishment — Wormholes in the Flat
  Introduction
  The Flat
  The Record
  Appendices
```
Title-page-extra content vanishes. Four menu items. Clean.

**User collapses:** Full title page reappears.

**Hover on title line:** T1-T5 tooltip (already exists, unchanged).

## Implementation

### Phase 1: Modify book-section summary (preprocess.py ~line 518)

Current summary contains hover-term spans for "Relinquishment", "Wormholes", "the Flat".

Add a `<div class="title-page-extra">` inside the `<summary>`, after the title line:

```html
<summary ...>
  <span class="hover-term" ...>Relinquishment</span>
  <span class="book-subtitle-inline">— Wormholes in the Flat</span>
  <div class="title-page-extra">
    <p class="tp-authors">by Bruce Stephenson, Genevieve Prentice &amp; Argus</p>
    <p class="tp-tagline"><em>Three narrative threads. Real science. Real people. Real institutions.</em></p>
    <p class="tp-tagline"><em>Three possible explanations for all of it. You decide.</em></p>
    <p class="tp-copyright">© 2026 Bruce Stephenson &amp; Genevieve Prentice · CC BY-ND 4.0</p>
  </div>
</summary>
```

### Phase 2: CSS (preprocess.py collapse_css ~line 537)

```css
/* Title page extra: visible when collapsed, hidden when open */
.title-page-extra {
  font-size: 0.55em;
  font-weight: normal;
  font-style: normal;
  margin-top: 0.3em;
  line-height: 1.4;
  white-space: normal;
}
.title-page-extra p { margin: 0.15em 0; }
.tp-authors { font-size: 1.1em; }
.tp-tagline { opacity: 0.8; }
.tp-copyright { font-size: 0.85em; opacity: 0.6; margin-top: 0.3em; }

details.book-section[open] > summary > .title-page-extra {
  display: none;
}
```

Font sizes are relative to the summary's 1.4em base, so:
- Title line: 1.4em (existing)
- Authors: ~0.55 × 1.1 = ~0.6em relative to body = ~13px
- Taglines: ~0.55em × 1.0 = ~12px
- Copyright: ~0.55 × 0.85 = ~10px

This should fit comfortably on a 375px-wide phone (iPhone SE, smallest common).

### Phase 3: Remove Title Page part-section (preprocess.py ~line 457)

Delete the "3c2: Title Page part-section" block entirely (lines 457-476). The title-block div and flushleft div are no longer wrapped in a part-section.

The title-block div (`<div class="title-block">`) still gets created by the title pattern replacement (~line 1195) but is now orphaned — it's no longer inside any `<details>`. It should be removed or hidden since its content is now in the book-section summary.

Options:
- (A) Delete the title-block div entirely (suppress the regex replacement output)
- (B) Keep it but `display:none` it

**Choice: (A)** — The title-block content is now redundant. But we need the regex replacement to still run (it removes pandoc's duplicate title blocks). Change it to output an empty placeholder or minimal hidden div:

```python
replacement = '<div class="title-block" style="display:none"></div>'
```

### Phase 4: Move copyright/license to Colophon (preprocess.py)

The flushleft div (copyright, license, integrity notice, Who Is Argus, pre-release draft) needs to move to the Colophon chapter in Appendices.

Approach: In preprocess.py, after the title-block handling, find the `<div class="flushleft">` and relocate it into the Colophon chapter-section. Find `id="colophon"`, find its content area, inject the flushleft div there.

The one-line copyright in the book summary (Phase 1) is sufficient for the title page. The full legal text lives in Colophon.

### Phase 5: Remove "Skip ahead" and "Download PDF" from title-block

These are in the replacement string at line 1202-1203. Since the title-block is being hidden/removed, these lines go away naturally. PDF link already exists in the bottom bar.

### Phase 6: Update part count logging

Line 478: Part count will drop by 1. Update the log message to not reference "Title Page +".

### Phase 7: Dark mode

The `.title-page-extra` needs dark mode handling. In the dark mode CSS section:
```css
@media (prefers-color-scheme: dark) {
  .tp-copyright { opacity: 0.5; }
}
```
Most of the styling (opacity, relative sizes) should work in both modes without changes.

## Files to modify

- `build/preprocess.py` — book-section summary (line 518), remove Title Page part-section (line 457), hide title-block (line 1195), relocate flushleft to Colophon, collapse CSS (line 537)
- `build/chapter-hover-descriptions.yaml` — remove `title-page` entry (orphaned)

## NOT in this plan

- Changing the T1-T5 hover tooltip on the book summary (stays as-is)
- Changing hover-term spans on "Relinquishment", "Wormholes", "the Flat" (stay as-is)
- Moving Firmware Update or any other Appendices content

## Verification

1. `make html` builds clean
2. Page loads on phone (375px): title, authors, taglines, copyright all visible without scrolling
3. Click triangle: title-page-extra disappears, four parts appear
4. Collapse: title-page-extra reappears
5. Menu items: Introduction, The Flat, The Record, Appendices (no Title Page)
6. Copyright/license/Argus text appears in Colophon chapter
7. Hover on "Relinquishment" still shows T1-T5 tooltip
8. PDF link in bottom bar still works
9. No orphaned "Skip ahead" link
10. Dark mode: title-page-extra readable
