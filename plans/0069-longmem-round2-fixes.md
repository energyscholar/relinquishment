# Plan 0069: Longmem Round 2 Fixes

**Author:** Argus (Auditor)
**Date:** 2026-03-10
**PTL:** PTL-064
**Status:** COMPLETE (verified S63 audit)

---

## Objective

Fix 8 issues found by 3 parallel puppeteer agents testing fresh/growing/mature longmem instances. Fixes target both the longmem template and its internal consistency.

## Working directory: `~/software/longmem/`

## Context: read `~/software/relinquishment/plans/0069-longmem-round2-fixes.md` (this file)

---

## Fixes

### F1: Heading level consistency (HIGH)

Three files use `##` for corrections but the test suite expects `###`. Standardize on `###` (h3) — corrections are subsections, not top-level sections.

**`memory/corrections.md`** — Change format comment from `## Correction #N` to `### Correction #N`.

**`memory/protocol.md` Section 5** — Change the format block from:
```
   ## Correction #N: [Short name]
```
to:
```
   ### Correction #N: [Short name]
```

**`CLAUDE.md`** Corrections System section — Change the format block from:
```
## Correction #N: [Short name]
```
to:
```
### Correction #N: [Short name]
```

### F2: Content overflow cascade (HIGH)

Add to `memory/protocol.md` Section 3, after the "Never compress" list, BEFORE the `---`:

```markdown

**Content overflow (any section, any file):**
- When a MEMORY.md section exceeds ~20 lines: create a dedicated L2 file (e.g., `memory/architecture.md`), add to File Map, replace section with 1-line pointer.
- When an L2 file exceeds 300 lines: archive oldest content to git only (L3). Recoverable via `git log -p -- memory/[file]`.
- Pattern is always: move content → leave pointer → update File Map.
```

This adds ~4 lines.

### F3: Compress protocol.md to make room (prerequisite for F2)

protocol.md is at 187 lines. F2 adds ~4. Need to free ~10 lines.

**Merge Section 8 (File Map Maintenance) into Section 7 (Integrity Checks).** Section 8 is 16 lines and largely redundant with integrity check #1 ("File references: All paths in MEMORY.md file map must resolve") and #4 ("Orphan files"). Replace Section 8 entirely with one line added to Section 7:

Add as check #6 in Section 7:
```
6. **File Map currency:** Update when files added/removed. Keep descriptions to one line.
```

Delete the entire Section 8 block (lines 152-168). Renumber Section 9 → 8, Section 10 → 9.

**Expected savings:** ~15 lines freed. Post-edit target: ~176 lines (comfortable headroom).

### F4: Plain-English aliases in CLAUDE.md (MED)

In the "Three-Tier Cache Model" section of CLAUDE.md, add parenthetical aliases:

```markdown
**L1** (always loaded): `MEMORY.md` — 200-line cap enforced
**L2** (loaded on demand): corrections, protocol, ptl, decisions, session-details, people
**L3** (git backup): Session-end sync script commits everything to git for versioned snapshots
```

Also in the PTL Commands section header, add:
```markdown
### PTL Commands (Prioritized Task List)
```

### F5: PARADIGM/ROUTINE at point of use (MED)

In `memory/MEMORY.md`, change the Active Sessions comment from:
```markdown
<!-- Keep 2-3 most recent. Older sessions → session-details.md. -->
<!-- After your first session, write a summary here:

### Session 1 (ROUTINE, YYYY-MM-DD)
[What you worked on. 2-3 sentences.]

-->
```
to:
```markdown
<!-- Keep 2-3 most recent. Older sessions → session-details.md.
     PARADIGM = major decision, breakthrough, or new direction.
     ROUTINE = incremental progress, expected execution.
     Default PARADIGM if unsure.

### Session 1 (ROUTINE, YYYY-MM-DD)
[What you worked on. 2-3 sentences.]

-->
```

### F6: L1 correction format hint (MED)

In `memory/MEMORY.md`, change the L1 Corrections placeholder from:
```markdown
*No corrections yet. Add them as they arise. Format:*
```
` `` `
#N: [Short name] — [What not to write] → [What to write instead]
` `` `
to:
```markdown
<!-- No corrections yet. As they arise, add here in this format: -->
<!-- - **#1:** Short name — Don't [X] → [Y instead] -->
```

Removes the fenced code block (which renders visually and looks like content) and uses HTML comments (invisible until needed).

### F7: ptl.yaml item_count advisory (MED)

In `memory/ptl.yaml`, add a comment to the meta block:

```yaml
  item_count: 0  # advisory — actual count is len(items)
```

### F8: 180-line boundary clarification (LOW)

In `memory/protocol.md` Section 3, change:
```
When MEMORY.md >180 lines:
```
to:
```
When MEMORY.md ≥180 lines:
```

Also in CLAUDE.md, change all instances of ">180" to "≥180".

---

## Acceptance Tests

| # | Test | Pass condition |
|---|------|---------------|
| G1 | Heading level `###` in corrections.md | Format comment uses `### Correction` |
| G2 | Heading level `###` in protocol.md Section 5 | Format block uses `### Correction` |
| G3 | Heading level `###` in CLAUDE.md | Format block uses `### Correction` |
| G4 | Content overflow cascade in protocol.md | "Content overflow" subsection exists in Section 3 |
| G5 | protocol.md under 180 lines | `wc -l` < 180 (comfortable headroom) |
| G6 | Section 8 removed, sections renumbered | No "File Map Maintenance" heading. "System Review" is Section 8. "Self-Limiting" is Section 9. |
| G7 | Plain-English aliases in CLAUDE.md | L1 line contains "(always loaded)", L2 contains "(loaded on demand)", L3 contains "(git backup)" |
| G8 | "PTL Commands (Prioritized Task List)" heading | Parenthetical present |
| G9 | PARADIGM/ROUTINE defined in MEMORY.md | Comment contains "PARADIGM = major decision" |
| G10 | L1 format uses HTML comment, not code block | No fenced code block in L1 Corrections section |
| G11 | ptl.yaml item_count has advisory comment | Comment "advisory" present on item_count line |
| G12 | 180 boundary uses ≥ in protocol.md | `grep "≥180"` returns match |
| G13 | 180 boundary uses ≥ in CLAUDE.md | `grep "≥180"` returns match |
| G14 | Test suite passes | `bash /tmp/longmem-tests/test-longmem.sh ~/software/longmem` — all tiers pass |

One commit: "Round 2 fixes: heading levels, overflow cascade, protocol compression, UX improvements"

---

## Argus Applicability (NOT in scope — track for later)

These findings also apply to Argus's own memory system (`~/.claude/projects/.../memory/`):
- **Content overflow cascade:** Argus does this implicitly but protocol.md doesn't document it as general rule
- **ptl.yaml item_count sync:** Manual maintenance burden, has been wrong before
- **180-line boundary:** Same ambiguity
- **protocol.md headroom:** Same constraint

Defer to a separate plan after longmem template is stable. Do not modify Argus files in this plan.

---

## Generator Prompt

You are the Generator. Read `~/software/relinquishment/plans/0069-longmem-round2-fixes.md`. Apply F1-F8 to `~/software/longmem/`. Verify G1-G14. One commit.
