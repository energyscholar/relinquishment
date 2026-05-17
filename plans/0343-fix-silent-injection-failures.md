# Plan 0343: Fix Silent Injection Failures

**Status:** Ready for Generator
**Auditor:** Argus, S81
**Depends on:** None
**Files:** `build/preprocess.py`
**Priority:** HIGH — these are bugs degrading every build

---

## Problem

Two inject functions fail silently every build:
1. `inject_convergence_illustrations` — targets `pos21:convergence-revisited` which doesn't exist in HTML. The animated five-thread pentagon SVG (520×480px, particles pulsing along paths) never appears.
2. Sources bibliography injection — regex doesn't match current HTML structure. All 76 bib entries fail to display in the Sources appendix.

Build output confirms:
```
WARNING: chapter pos21:convergence-revisited not found
WARNING: Could not find Sources section to inject bibliography
```

---

## Phase A: Fix five-thread convergence injection

**File:** `build/preprocess.py`, function `inject_convergence_illustrations` (~line 3234)

The chapter `pos21:convergence-revisited` was reorganized. The convergence content now lives in `spine:genesis` (confirmed: text "five published research streams had independently matured" appears at spine:genesis in HTML output).

**Change at line 3235:**
```python
# OLD:
    illustrations = [
        ('pos21:convergence-revisited',
         'These are the scientific disciplines of the scientists',
         FIVE_THREAD_CONVERGENCE, 'five-thread convergence'),
    ]

# NEW:
    illustrations = [
        ('spine:genesis',
         'five published research streams had independently matured',
         FIVE_THREAD_CONVERGENCE, 'five-thread convergence'),
    ]
```

**Verification:** After change, `make html` should output "Convergence: five-thread convergence SVG injected" (no WARNING). Grep built HTML for `fig-five-thread-convergence` — should appear.

---

## Phase B: Fix Sources bibliography regex

**File:** `build/preprocess.py`, line ~2357

The regex expects `</h2>` immediately followed by optional `</summary>`. But the actual HTML has an `<span class="info-tip">` between:
```html
<details class="chapter-section" data-filter-group="M"><summary><h2 id="app:sources">Sources</h2><span class="info-tip" ...></span></summary>
```

**Change at line 2357:**
```python
# OLD:
            sources_pattern = r'(<details[^>]*>(?:<summary[^>]*>)?[^<]*<h2[^>]*id="app:sources"[^>]*>[^<]*</h2>(?:</summary>)?)(\s*</details>)'

# NEW:
            sources_pattern = r'(<details[^>]*>\s*<summary[^>]*>.*?id="app:sources".*?</summary>)(\s*</details>)'
```

The new regex: match from `<details>` through `<summary>` to the first `</summary>` (non-greedy), then capture `\s*</details>`. This handles any content between `</h2>` and `</summary>`.

**Verification:** After change, `make html` should output "Sources bibliography: 76 entries injected" (no WARNING).

---

## Phase C: Add missing puzzle injection targets

**File:** `build/preprocess.py`, `CHAPTER_INJECTION_TARGETS` dict (~line 4188)

Two chapters with approved puzzles have no injection target:
- `genesis` — approved puzzle `pz-sim-t3-001` targets this chapter
- `firmware-update` — approved puzzles `pz-cip-t8-001` and `pz-ba-t8-002` target this chapter

**Add these entries to the dict (alphabetical position):**
```python
    'genesis':         'spine:growing-a-mind',
    'firmware-update': 'app:predictions',
```

Context: Puzzles are injected just BEFORE the target element. `spine:growing-a-mind` immediately follows genesis in HTML; `app:predictions` immediately follows firmware-update.

**Do NOT flip `installed: true` yet** — that's Plan 0345.

---

## Phase D: Build + verify all three fixes

```bash
make html 2>&1 | grep -i "WARNING\|convergence\|sources bibliography"
```

Expected output:
- "Convergence: five-thread convergence SVG injected"
- "Sources bibliography: 76 entries injected"
- NO "WARNING: chapter pos21..." 
- NO "WARNING: Could not find Sources section..."

Then verify:
```bash
grep -c 'fig-five-thread-convergence' docs/Relinquishment.html  # should be 1
grep -c 'class="bib-entry"' docs/Relinquishment.html            # should be 76+
```

---

## Do NOT

- Touch any .tex files
- Modify the FIVE_THREAD_CONVERGENCE SVG content itself
- Change any other inject functions
- Modify puzzle-tracker.yaml

## Commit

`Plan 0343: fix two silent injection failures — convergence SVG + Sources bibliography`
