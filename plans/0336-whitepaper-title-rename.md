# Plan 0336: White Paper Title Rename — "Is Your AI Properly Governed?"

**Origin:** Bruce's direction during S80 (2026-05-14). The article says "The problem is no longer amnesia" in paragraph 3 — the old title contradicts the thesis. People's key takeaway is the multiple orthogonal governance layers. Title should reflect that.

**Scope:** 10 text edits across two files. No structural changes. SVG animations unaffected.

---

## Rationale

- **Question form** drives LinkedIn engagement — reader self-assesses before clicking
- **"Properly"** implies a standard exists (the article defines it via the three-layer architecture and failure matrix)
- **Subtitle** creates curiosity — "three layers" is the article's actual thesis
- The existing body text already supports the governance framing: "The problem is no longer amnesia" (line 551) now works as answer to the implicit question

---

## Files

1. `~/software/persistent-ai-collaboration/index.html` (primary)
2. `~/software/renuncio-ai/en/index.html` (internationalization copy — same edits, match by string)

---

## Edits — Primary File

All old→new strings verified by file read 2026-05-14.

**Edit 1 — Line 6, `<title>` tag:**
```
OLD: <title>Your AI Has Amnesia — A practitioner's guide to building one that doesn't</title>
NEW: <title>Is Your AI Properly Governed? — A practitioner's guide to the three layers that make it so</title>
```

**Edit 2 — Line 7, `<meta description>`:**
```
OLD: <meta name="description" content="Architecture patterns for persistent AI collaboration. No productivity claims — just the system, the evidence, and a replication guide.">
NEW: <meta name="description" content="Three governance layers for AI collaboration: role discipline, persistent memory, and ethical guardrails. No productivity claims — just the system, the evidence, and a replication guide.">
```

**Edit 3 — Line 486, `<h1>` heading:**
```
OLD: <h1>Your AI Has Amnesia</h1>
NEW: <h1>Is Your AI Properly Governed?</h1>
```

**Edit 4 — Line 487, subtitle:**
```
OLD: <p class="subtitle">A practitioner's guide to building one that doesn't</p>
NEW: <p class="subtitle">A practitioner's guide to the three layers that make it so</p>
```

**Edit 5 — Line 492, SVG `<title>` (hero diagram):**
```
OLD: <title>The Amnesia Loop vs. The Persistent System</title>
NEW: <title>The Ungoverned Loop vs. The Governed System</title>
```

**Edit 6 — Line 495, visible SVG text (left side of hero):**
```
OLD: THE AMNESIA LOOP
NEW: THE UNGOVERNED LOOP
```

**Edit 7 — Line 521, visible SVG text (right side of hero):**
```
OLD: THE PERSISTENT SYSTEM
NEW: THE GOVERNED SYSTEM
```

**Edit 8 — Line 1858, JSON-LD name:**
```
OLD: "name": "Your AI Has Amnesia",
NEW: "name": "Is Your AI Properly Governed?",
```

**Edit 9 — Line 1859, JSON-LD headline:**
```
OLD: "headline": "A practitioner's guide to building one that doesn't",
NEW: "headline": "A practitioner's guide to the three layers that make it so",
```

---

## What Does NOT Change

- Line 551: "The problem is no longer amnesia" — thesis sentence, stays as rhetorical pivot
- Line 601: "prevents amnesia" — describes the failure mode, correct usage
- SVG group IDs (`amnesia-group`, `amnesia-label-*`) — internal, invisible, no CSS/JS refs
- SVG `aria-label` (line 491) — minor accessibility, leave for now
- All body text, section headers, puzzles, reveals, tutorials — unchanged

---

## Renuncio Copy

Apply same edits to `~/software/renuncio-ai/en/index.html`. Match by string not line number (file has additional `<link rel="alternate">` tags that shift line numbers by ~3). The renuncio copy has slightly different footer/download/contact text — those are unrelated and untouched.

---

## Acceptance Criteria

- All 9 edits applied to both files
- Browser test: title bar shows new title, h1 displays question, hero SVG labels read "UNGOVERNED" / "GOVERNED", animation still plays
- `view-source:` check: JSON-LD matches new title/headline
- Body text "amnesia" references (lines 551, 601) preserved unchanged
