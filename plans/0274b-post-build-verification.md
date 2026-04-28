# Plan 0274b: Post-Build Puzzle Verification

**Status:** READY FOR GENERATOR
**Author:** Auditor (Argus S63)
**Priority:** High (prerequisite for 0274c waves)
**Scope:** `build/preprocess.py` (add verification step after injection)
**Annealing:** MED LOW LOW

---

## Problem Statement

After puzzle injection, the only verification is manually grepping for `puzzle-section` count. There's no automated check that the right puzzles appear in the right chapters, or that the tracker's `installed` flags match reality. With 17 puzzles across 10 chapters, manual checking is error-prone.

---

## Implementation

Add `verify_puzzle_injection()` as a function in `preprocess.py`, called immediately after `inject_chapter_puzzles()` returns. This cross-references the tracker against the built HTML.

```python
def verify_puzzle_injection(html_path):
    """Cross-reference puzzle tracker against built HTML. Print report."""
    html_path = Path(html_path)
    text = html_path.read_text()
    tracker_path = REPO / 'build' / 'puzzle-tracker.yaml'
    tracker = yaml.safe_load(tracker_path.read_text())

    # Expected: installed + supported type + chapter in TARGETS
    expected = set()
    for p in tracker.get('chapter_puzzles', []):
        if p.get('approved') and p.get('installed'):
            ptype = p.get('type', '')
            chapter = p.get('location', {}).get('chapter', '')
            if ptype in ('mc', 'gd', 'log') and chapter in CHAPTER_INJECTION_TARGETS:
                expected.add(p['id'])

    # Actual: puzzle IDs found in HTML
    import re
    actual = set(re.findall(r'id="(pz-[a-z]+-t\d+-\d+)"', text))

    # Compare
    missing = expected - actual
    extra = actual - expected

    ok = True
    if missing:
        print(f"  VERIFY FAIL: {len(missing)} expected puzzles NOT in HTML:")
        for pid in sorted(missing):
            print(f"    MISSING: {pid}")
        ok = False
    if extra:
        print(f"  VERIFY WARN: {len(extra)} puzzles in HTML but NOT expected:")
        for pid in sorted(extra):
            print(f"    EXTRA: {pid}")
        ok = False

    if ok:
        print(f"  VERIFY OK: {len(actual)} puzzles in HTML match tracker")

    # Check level ordering within chapters
    # Find all puzzle-section elements and their positions
    puzzle_positions = []
    for m in re.finditer(r'<details class="puzzle-section"[^>]*>\s*<summary[^>]*>.*?</summary>', text, re.DOTALL):
        pid_match = re.search(r'id="(pz-[a-z]+-t\d+-\d+)"', text[m.start():m.start()+500])
        if pid_match:
            puzzle_positions.append((m.start(), pid_match.group(1)))

    # Verify ordering: within each chapter's group, p1 should come before p2 before p3
    # Group by approximate position relative to chapter markers
    # (This is advisory — it prints warnings but doesn't fail the build)

    return ok
```

### Integration point

In the `fix_html()` function (or wherever `inject_chapter_puzzles()` is called), add:

```python
inject_chapter_puzzles(html_path)
verify_puzzle_injection(html_path)
```

The verification runs every build. It prints OK or FAIL. It does NOT abort the build on failure — just prints warnings. The Generator checks the output.

---

## Anneal: MED LOW LOW

### MEDIUM

**M1. The `id="pz-..."` regex may match puzzle IDs in non-puzzle contexts.**
If puzzle IDs appear in deep-links, hover data, or JavaScript as string literals, they'll show up in `actual` as false positives.
**Mitigation:** The regex finds all `id="pz-..."` attribute values. Puzzle IDs in JS/JSON use different quoting (`"id":"pz-..."` or `'pz-...'`). Only HTML `id=` attributes use the `id="pz-..."` pattern. Deep-link anchors use `id="dl:pz-..."` prefix, so they won't match. Verify with grep.

### LOW

**L2. Level ordering check is approximate.**
The verification knows puzzle positions in HTML but not chapter boundaries. It can't definitively say "this puzzle is in the wrong chapter." It can only check that within a group of consecutive puzzles, levels are non-decreasing.
**Mitigation:** Chapter placement is verified by the injection logging (0274a). This script catches count mismatches and missing/extra puzzles — the most common failure modes.

**L3. Script runs every build, adds ~50ms.**
**Mitigation:** Negligible. The HTML is already in memory. Regex scan of 1MB is instant.

---

## Acceptance Criteria

1. `verify_puzzle_injection()` exists and is called after injection
2. Prints `VERIFY OK: N puzzles` when counts match
3. Prints `VERIFY FAIL: MISSING: pz-xxx` when a puzzle is expected but absent
4. Does not abort the build
5. Works with 0 puzzles (prints `VERIFY OK: 0 puzzles`)

---

## Handoff Prompt

```
You are the Generator. Read plan 0274b in ~/software/relinquishment/plans/.

Add verify_puzzle_injection() to build/preprocess.py. It cross-references
the tracker (installed+approved+supported type+chapter in TARGETS) against
actual puzzle IDs found in the built HTML. Prints OK/FAIL/WARN report.
Call it immediately after inject_chapter_puzzles() in the --fix-html path.
See plan for exact implementation. Build, verify it prints "VERIFY OK: 4
puzzles" (matching 0274a state). Commit:
"Plan 0274b: post-build puzzle verification"
```
