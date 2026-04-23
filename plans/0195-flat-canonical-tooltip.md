# Plan 0195 — Canonical Flat Definition: Chapter First-Use + Chapter TOC Hover

**Auditor:** Argus
**Date:** 2026-04-14
**Track:** All (cross-cuts front matter, spine chapter, build config)
**Priority:** Medium. Small-surface, high-leverage edit on the book's most load-bearing term.

---

## Intent

The book coins "the Flat" as its core term. The canonical definition lives in `build/hover-definitions.yaml` under key `the-flat-title` (hover_id `the-flat-title`), and is wired to the book title/cover via `preprocess.py:522` (`_title_panel_attrs('the-flat-title')`).

Bruce noticed: after the title page, the canonical definition never appears again. Two places where it must:

1. **First prose use of "the Flat" inside the chapter `spine/the-flat.tex`** (chapter titled "Wormholes in the Flat"). Currently unannotated.
2. **The chapter-TOC hover** for that chapter. Currently `chapter-hover-descriptions.yaml` line 7 gives a different summary ("Published physics, true under all three possibilities..."). That entry should be replaced (or the chapter's hover logic should redirect) so the canonical rich panel is the TOC hover for this chapter.

The book's title, the chapter's TOC tooltip, and the first prose mention of "the Flat" inside the chapter should all show the reader the same canonical definition.

---

## Files

| File | Purpose |
|---|---|
| `manuscript/spine/the-flat.tex` | Add `\hovertip{the Flat}` on first prose use (line 11). Do NOT wrap the chapter title (`\chapter{Wormholes in the Flat}`); the macro runs in normal text only. |
| `build/hover-definitions.yaml` | Add a new key `the Flat` that mirrors the existing `the-flat-title` entry (same `html:` rich panel, same `hover_id: "the-flat-title"` so a reader hovering it on multiple pages gets the stable ID). |
| `build/chapter-hover-descriptions.yaml` | Replace the `"the-flat":` value (line 7) so the chapter-TOC tooltip uses the canonical definition. Two acceptable approaches — pick whichever matches existing chapter-hover infra with least friction: (a) inline the canonical plain-text definition, or (b) add a YAML directive that flags this chapter's hover as "use rich panel from hover-definitions.yaml: the-flat-title". **Prefer (b) if `preprocess.py` already supports it; otherwise (a) inlined.** If neither is supported cleanly, extend `preprocess.py` to support (b) — this is small and the pattern will be reused when other title-level panels get the same treatment. |
| `build/preprocess.py` | Only if (b) above requires it. See below. |

---

## Concrete edits

### Edit 1 — `manuscript/spine/the-flat.tex` line 11

Current:
```
The stack chart at the front of the book pointed to the last column --- the one with the checkmark for wormholes. This chapter names the substrate that gives it that property: the Flat.
```

Change to:
```
The stack chart at the front of the book pointed to the last column --- the one with the checkmark for wormholes. This chapter names the substrate that gives it that property: \hovertip{the Flat}.
```

That is the **first prose mention** of "the Flat" in the chapter. The next sentence (line 13, inside `\section*{The Substrate}`) already carries `\deeplink{what-is-the-flat}`; leave that as-is.

### Edit 2 — `build/hover-definitions.yaml`

Add a new top-level key `the Flat` mirroring the `the-flat-title` entry. Keep `hover_id: "the-flat-title"` so the reader's hover-state is consistent across title page, TOC, and chapter. Copy the full `html:` rich panel (including the inline SVG) from `the-flat-title` verbatim. Set `target: "#ch:what-is-the-flat"` so click-through lands on the chapter's section anchor.

The key must be `the Flat` (exact case, with leading "the ") to match `\hovertip{the Flat}` in Edit 1.

Do **not** remove or alter the existing `the-flat-title` or `flat worlds` entries. They are used elsewhere. This adds a third alias pointing at the same canonical content.

### Edit 3 — `build/chapter-hover-descriptions.yaml`

Current line 7:
```yaml
"the-flat": "Published physics, true under all three possibilities. Every chip contains a flat quantum world that supports quantum teleportation. Every planet with a magnetic field has one at planetary scale. The physics says what could live there — and what it could do. Five fields are needed to ask. No journal covers all five. Nobody asked."
```

Two options, pick the one the existing infra supports with the fewest extension points:

**Option A (preferred if supported):** convert the value to a marker that tells `preprocess.py` to pull the rich panel from `hover-definitions.yaml` under key `the-flat-title`. E.g.:
```yaml
"the-flat":
  rich_panel_from: "the-flat-title"
```

**Option B (fallback):** inline the canonical plain-text core of the definition (drop the SVG — `chapter-hover-descriptions.yaml` entries are read as plain strings by existing code, per `preprocess.py:267` context):
```yaml
"the-flat": "The Flat — this book coins 'the Flat' to mean any two-dimensional system embedded in three dimensions that can, under the right conditions, exhibit topological order. Different physics apply. In particular, it supports topological wormholes, so the Flat can be nonlocal in the technical physics sense. The Flat inside your computer chip is a 2DEG (two-dimensional electron gas). The Flat in Earth's magnetosphere is plasma confined to thin current sheets. This book calls those thin worlds the Flat."
```

### Edit 4 — `build/preprocess.py` (only if Option A in Edit 3)

If Option A is chosen and not yet supported, extend the chapter-hover loader (around lines 261–280, per the `hover_map` / `chapter-hover-descriptions.yaml` wiring) so that when a chapter-hover value is a dict with `rich_panel_from`, the loader:

1. Reads the referenced key from `hover-definitions.yaml`.
2. Substitutes the `html:` rich-panel payload (stripped/adapted for the TOC-tooltip context if a menu tooltip can't render SVG — see `menu-tooltips.yaml` for precedent) or the `text:` field if rich HTML is not allowed in the TOC surface.
3. Sets `hover_id` to `the-flat-title` (or whatever the source key's `hover_id` is).

Keep the change minimal. If it starts growing, switch to Option B and leave preprocess.py untouched.

---

## Acceptance criteria

1. Build (`cd ~/software/relinquishment && make` or the repo's standard build invocation) completes cleanly, no new warnings about undefined hover keys or broken targets.
2. In the generated HTML, hovering the word "the Flat" at the first prose occurrence in the chapter (`spine:the-flat` → `\section*{The Substrate}` and the preceding paragraph) shows the canonical rich panel (the 2DEG SVG + the "this book coins..." paragraph + the 2-paragraph expansion).
3. In the generated HTML, hovering the chapter link in the TOC / chapter menu for "Wormholes in the Flat" shows the canonical definition (rich panel if Option A, inlined text if Option B).
4. In the generated HTML, the book-title hover (title page / cover) still shows the same canonical definition as before. Unchanged.
5. `hover_seen` dedup in preprocess.py (line 129) does not eat the first-use marker. If the chapter file is processed before the front matter, the first-use may fire there instead; confirm order or explicitly place this first-use with priority. If needed, use `\hovertiphtml{the Flat}` (the longer-match variant at preprocess.py:198) to force rich-panel rendering even if `\hovertip` dedup would skip it. Confirm by inspecting the generated HTML for the rich-panel class around the first-occurrence anchor.
6. No regressions in other chapters that mention "the Flat" — they continue to render as plain text after the first hover fires. This is existing behavior, just verify.

---

## Commit

One commit:

```
Plan 0195: canonical Flat definition at chapter TOC + chapter first-prose-use

- Add \hovertip{the Flat} on first prose mention in spine/the-flat.tex
- Alias yaml key 'the Flat' → canonical panel (hover_id the-flat-title)
- Chapter-TOC hover for 'the-flat' now uses canonical definition
```

---

## Non-goals

- Do NOT add hovertips to "the Flat" in other chapters. First-occurrence dedup handles subsequent mentions.
- Do NOT modify `flat worlds` or `the-flat-title` existing entries.
- Do NOT touch the `\deeplink{what-is-the-flat}` that already exists on the next paragraph.
- Do NOT edit the chapter epigraph on line 7.
- Do NOT change book build infrastructure beyond the optional Edit 4.

---

## Post-completion

Report back:
1. Which Option (A or B) you used for Edit 3 and why.
2. Whether Edit 4 was required.
3. Build status + one sentence confirming the three hover points (title / TOC / chapter first-use) all resolve to the canonical rich panel.
