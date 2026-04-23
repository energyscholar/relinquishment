# Plan 0154c: Menu Restructure (Eval → Appendix + Title Page → Cover)

**Status:** DONE — delivered via Plans 0145+0146 (commits 892b620, 5bd315a)
**Created:** 2026-04-10
**Plans:** 0145-evaluate-to-appendix.md + 0146-title-page-into-summary.md
**Dependency:** 0154a must be done — chapter count changed. Independent of 0154b and 0154d.

---

## Scope

Two plans, two commits. Both reshape part-section layout in preprocess.py. Related enough to pair — both remove a part-section and redistribute its content. Small enough for one context window.

## Commit 1: Plan 0145 — Move AI Evaluation into Firmware Update

Read `~/software/relinquishment/plans/0145-evaluate-to-appendix.md` for full spec.

- Rewrite `inject_evaluate_section()` in preprocess.py — inject into Firmware Update chapter, not standalone part-section
- Update bottom bar eval button target → `#ch:firmware-update`
- Update tooltip text in reader.js
- Update `build/chapter-hover-descriptions.yaml` and `build/menu-tooltips.yaml`

**VERIFY:** `make html` clean. Menu has no "How to Evaluate" line. AI Eval button opens Firmware Update. Copy buttons work.

## Commit 2: Plan 0146 — Title Page → Disappearing Cover

Read `~/software/relinquishment/plans/0146-title-page-into-summary.md` for full spec.

- Add `<div class="title-page-extra">` to book-section summary in preprocess.py
- CSS: visible when collapsed, hidden when open
- Remove Title Page part-section block in preprocess.py (find by content, not line number)
- Hide title-block div
- Move flushleft div (copyright/license) into Colophon chapter
- Dark mode support

**VERIFY:** `make html` clean. Page loads: title + authors + taglines + copyright visible. Click triangle: title-page-extra disappears, parts appear. Collapse: reappears. Copyright in Colophon. Test at 375px mental model.

## Interaction notes

- Both remove a part-section. After both commits, parts in menu: Introduction, The Flat, The Record, Appendices (4 total). Title Page and How-to-Evaluate both gone.
- Both modify preprocess.py but target different functions. Commit 1 rewrites `inject_evaluate_section()`. Commit 2 modifies the collapse/part-section creation block and title-block regex. No function overlap, but do Commit 1 first so line numbers don't shift under you.
