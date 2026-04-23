# Plan 0145: Move AI Evaluation into Firmware Update (Appendices)

**Status:** DONE (implemented prior to 2026-04-10; confirmed by Generator C)

## Context

"How to Evaluate This Book with AI" is a standalone part-section between Title Page and Introduction — prime menu real estate delivering low value. The Firmware Update chapter already lives in Appendices with the science anchors and DOIs. The bottom bar AI Eval button already exists. The social immune system handles enforcement. We just need the mechanism findable, not front-and-center.

## Goal

Remove the standalone "How to Evaluate" part-section from the menu. Merge its content (copy buttons + intro text) into the Firmware Update chapter in Appendices. Update the bottom bar button to navigate there.

## Dependency analysis

| Component | Location | Position-dependent? | Action |
|-----------|----------|-------------------|--------|
| `inject_evaluate_section()` | preprocess.py:873 | YES — creates part-section between Title Page and Intro | Rewrite: inject into Firmware Update chapter instead |
| `eval-step-1`, `eval-step-2` buttons | Created by `inject_evaluate_section()` | NO — JS finds by `data-eval-step` attribute | Move with parent |
| `llm-primer-text` hidden div | preprocess.py:1452 | NO — injected before `</body>`, found by ID | No change |
| `spiral-abstracts-text` hidden div | preprocess.py:1467 | NO — same | No change |
| Copy-button JS wiring | reader.js:709-745 | NO — `querySelector('[data-eval-step="1"]')` | No change |
| AI Eval bottom bar button | reader.js:305-319 | YES — `autoExpand('#how-to-evaluate')` | Change to `'#ch:firmware-update'` |
| Cold-landing primer links | preprocess.py:786 | NO — links to `#ch:firmware-update` already | No change |
| `evaluate-section` CSS class | preprocess.py:877 | Orphaned after removal | Remove from inject function |
| `evaluate-with-ai` ID | preprocess.py:877 | Used as anchor | Keep as invisible anchor inside Firmware Update |
| `how-to-evaluate` ID | preprocess.py:879 | Used by evalBtn `autoExpand` | Keep as invisible anchor inside Firmware Update |
| Appendices boundary detection | preprocess.py:411-412 | Searches for `id="ch:firmware-update"` | No change — content injected AFTER collapse_chapters runs |
| Part count log | preprocess.py:478 | Reports part count | Will drop by 1 (correct) |

## Phase 1: Rewrite `inject_evaluate_section()` (preprocess.py)

**Current:** Creates a `<details class="part-section evaluate-section">` and inserts before Introduction.

**New:** Inject a `<div>` with the eval intro + copy buttons at the TOP of the Firmware Update chapter-section content (after its `<summary>` closing tag). Include invisible anchors for `evaluate-with-ai` and `how-to-evaluate` so existing links don't break.

Find: `id="ch:firmware-update"` → find its parent `<details>` → find the `</summary>` → inject after it.

```python
def inject_evaluate_section(text):
    """Inject evaluate-with-AI content into Firmware Update chapter."""
    eval_html = (
        '<div class="evaluate-section" id="evaluate-with-ai">\n'
        '<span id="how-to-evaluate"></span>\n'  # backwards-compat anchor
        '<p><strong>Your AI doesn&#x27;t know enough to evaluate this book.</strong> '
        'It lacks five fields of cross-domain science. The fix takes thirty seconds. '
        'Copy the science upgrade below. Paste it into your AI. Then ask again.</p>\n'
        '<button ...>Copy Prompt 1</button>\n'
        '<button ...>Copy Prompt 2</button>\n'
        '<p class="eval-security-note">...</p>\n'
        '<hr style="margin:2em 0;" />\n'
        '</div>\n'
    )
    # Find Firmware Update chapter content start
    fw_id = text.find('id="ch:firmware-update"')
    if fw_id != -1:
        summary_close = text.find('</summary>', fw_id)
        if summary_close != -1:
            insert_pos = summary_close + len('</summary>')
            text = text[:insert_pos] + '\n' + eval_html + text[insert_pos:]
            print("  Evaluate section merged into Firmware Update chapter")
    return text
```

## Phase 2: Update bottom bar button (reader.js)

Line 319: Change `autoExpand('#how-to-evaluate')` → `autoExpand('#ch:firmware-update')`

Line 310: Update tooltip to: `'Your AI doesn\'t know enough to evaluate this book. It needs five fields of science. Click here — the fix takes thirty seconds.'`

## Phase 3: Update tooltips (YAML files)

**chapter-hover-descriptions.yaml** `ch:firmware-update`:
"Your AI doesn't know enough to evaluate this book. Five fields of science, two copy buttons, thirty seconds. Paste the upgrade and ask again."

**menu-tooltips.yaml** `ch:firmware-update`:
Same message, plus existing content about the ten physics anchors.

**Remove** `your-ai-may-need-a-firmware-update` from chapter-hover-descriptions.yaml (orphaned — was the Introduction-level entry).

## Phase 4: Clean up

- Remove `evaluate-section` from any CSS that styled it as a part-section (check html.css)
- Verify part count drops by 1 in build output (5→4 parts: Title Page, Introduction, The Flat, The Record, Appendices — no more evaluate)
- Verify `#how-to-evaluate` and `#evaluate-with-ai` anchors resolve inside Firmware Update chapter

## Verification

1. `make html` builds clean
2. Menu: Relinquishment > Title Page > Introduction > The Flat > The Record > Appendices (no "How to Evaluate")
3. Part count in build output: 4 (was 5)
4. Bottom bar AI Eval button opens Appendices → Firmware Update chapter
5. Copy buttons work (both prompts copy to clipboard)
6. `#how-to-evaluate` deep link opens Firmware Update chapter
7. Cold-landing "Evaluating with AI?" links still work
8. Hover tooltip on Firmware Update chapter reflects new role
