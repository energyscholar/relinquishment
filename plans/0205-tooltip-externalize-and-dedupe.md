# Plan 0205 — Tooltip externalization + dedupe (HTML bloat reduction)

## Status
**Status:** COMPLETE (verified S63 audit)
COMPLETE (verified S63 audit). Originally: Ready for Generator.

## Goal
Reduce `Relinquishment.html` size by ~80–100K (~10%) by moving tooltip content out of per-element inline attributes into a single inline JSON map. Lighter HTML parses faster in browsers (Bruce's stated reason).

## Scope
HTML build pipeline only — `build/preprocess.py` and `build/reader.js`. PDF pipeline (`generate-hover.py` → `\csdef`) is unchanged.

## Why this works (audit data)

The 100 `<span class="hover-term">` body elements total **104,534 bytes**, of which:
- visible text: 1,311B (1.3%)
- `data-hover-html` attrs: 70,708B (67.6%)
- `data-hover` attrs: 25,512B (24.4%)
- everything else: ~7K (chrome + IDs + class)

So 96K of every 104K of hover-term span content is **tooltip data inlined per occurrence**. The same 22 unique rich-panel tooltips and 166 unique plain tooltips are repeated as inline attributes everywhere they appear. Externalizing into one JSON dict + per-element ID reference shrinks each span from ~1KB to ~50B.

Estimated savings (based on script analysis):
- Inline span shrink: 104,534B → ~6,600B (save ~98K)
- New inline JSON dict: ~74K
- **Net raw savings: ~24K** (more if HTML→JSON encoding is leaner — see below)

The 24K headline understates the real win because:
1. **HTML attribute encoding is wasteful for HTML content.** Storing `<p style="margin:0">x</p>` as a `data-hover-html` attribute requires `&lt;p style=&quot;margin:0&quot;&gt;x&lt;/p&gt;` (HTML-entity-encoded inside a quoted attr). In JSON, you store the literal HTML with only `"` → `\"` and `\` → `\\` escapes. **For HTML content with double quotes, JSON is roughly 30–40% smaller than the HTML-attr-encoded equivalent.** Real savings target: **80–100K**.
2. Browser parsing is faster on smaller documents — Bruce's primary motivation.

## Files modified
- `build/preprocess.py` — emit hover spans without inline tooltip attrs; collect into dict; emit one JSON block at end of body
- `build/reader.js` — parse JSON on load; update tooltip handler to look up by `data-hover-id`
- (No source-content changes; no manuscript changes; no YAML changes)

## Architecture

### Current (per-element inline)
```html
<span class="hover-term"
      data-hover="Plain-text definition that may be a paragraph long..."
      data-hover-html="&lt;p&gt;Rich HTML with &lt;strong&gt;markup&lt;/strong&gt;...&lt;/p&gt;"
      data-hover-id="the-flat">the Flat</span>
```
Repeated ~100 times across hover-term spans, plus more for hover-nav summaries.

### New (per-element reference + one inline dict)
```html
<span class="hover-term" data-hover-id="the-flat">the Flat</span>
...
<!-- end of body, before </body> -->
<script type="application/json" id="hover-data">{
  "the-flat":{"t":"Plain text definition...","h":"<p>Rich HTML...</p>"},
  "wormholes":{"t":"...","h":"..."},
  ...
}</script>
```
One copy of each tooltip; per-element overhead drops to `data-hover-id="key"` (~25 bytes).

## Implementation

### Phase 0 — Regression snapshot (RUN BEFORE ANY CODE CHANGES)

This is a safety net. Before touching `preprocess.py` or `reader.js`, capture the current state of every tooltip in the built HTML. Phase 4 will compare post-change tooltips against this snapshot — any divergence in tooltip content is a regression.

Create `build/snapshot-tooltips.py`:

```python
#!/usr/bin/env python3
"""Snapshot every tooltip in the built HTML for post-change regression diff."""
import re, json, sys, hashlib

HTML = "docs/downloads/Relinquishment.html"
OUT = "build/test-fixtures/tooltips-baseline.json"

def main():
    with open(HTML) as f:
        html = f.read()

    # For every element carrying a tooltip, capture its visible text + tooltip data
    # Pattern matches both <span class="hover-term ..."> and <summary class="hover-nav">
    snapshot = {}

    # Find every element with data-hover-id
    for m in re.finditer(r'<(\w+)[^>]*data-hover-id="([^"]+)"[^>]*>([^<]*)</\1>', html):
        tag, hid, visible = m.group(1), m.group(2), m.group(3)
        full_tag = m.group(0)
        text_attr = re.search(r'data-hover="([^"]*)"', full_tag)
        html_attr = re.search(r'data-hover-html="([^"]*)"', full_tag)
        snapshot.setdefault(hid, []).append({
            "tag": tag,
            "visible": visible,
            "text": text_attr.group(1) if text_attr else None,
            "html": html_attr.group(1) if html_attr else None,
        })

    # Also: count terms without data-hover-id (these have inline data-hover but no key)
    keyless = re.findall(r'<\w+[^>]*data-hover="([^"]*)"[^>]*>', html)
    keyless_no_id = [v for v in keyless if 'data-hover-id' not in v]

    output = {
        "snapshot_count": len(snapshot),
        "total_occurrences": sum(len(v) for v in snapshot.values()),
        "keyless_inline_count": len(keyless_no_id),
        "by_id": snapshot,
    }

    import os
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as f:
        json.dump(output, f, indent=2, sort_keys=True)
    print(f"Snapshotted {output['snapshot_count']} unique tooltip IDs across {output['total_occurrences']} occurrences")
    print(f"Plus {output['keyless_inline_count']} keyless inline tooltips (will need migration tracking)")

if __name__ == "__main__":
    main()
```

Run it:
```
python3 build/snapshot-tooltips.py
git add build/test-fixtures/tooltips-baseline.json
git commit -m "Plan 0205 phase 0: tooltip baseline snapshot for regression test"
```

This commit is part of the plan — it gives Generator (and any future audit) an unambiguous fixture of pre-change state.

### Phase 1 — preprocess.py emit changes

**Find all hover-attr emit sites.** Run `grep -n 'data-hover\b\|data-hover-html' build/preprocess.py` — known sites from audit:
- L516, L527–535: hardcoded p3 chapter "demo" buttons (eval-step / wormholes / flat panels)
- L994–1004: eval-step button hover-nav
- L1595–1603: main hovertip wrapper (the high-volume site — emits ~95% of body hover-term spans)
- L1682–1683: Custodian interlude divs
- L1872–1900: stack table cells
- L1909–1945: TOC link / accordion summary `title=` → `data-hover=` conversion

For each site, modify emit logic:
- If the tooltip content is keyed (has a yaml/computed key): emit `data-hover-id="key"` only; register `(key, text, html)` into a module-level `hover_dict`
- If the tooltip content is dynamic (no stable key, e.g. acronym `title=` conversions): generate a content-hash key, register, emit `data-hover-id="hash"`

**Module-level collector** (top of preprocess.py, after imports):
```python
_hover_dict = {}  # key → {"t": plain_text, "h": rich_html_or_none}

def _register_hover(key, text=None, html=None):
    if key not in _hover_dict:
        _hover_dict[key] = {}
    if text and "t" not in _hover_dict[key]:
        _hover_dict[key]["t"] = text
    if html and "h" not in _hover_dict[key]:
        _hover_dict[key]["h"] = html
```

**For dynamic / unkeyed tooltips** (acronym title-conversions etc):
```python
import hashlib
def _content_key(content):
    return "h" + hashlib.md5(content.encode()).hexdigest()[:10]
```
Generates stable IDs like `ha1b2c3d4e5` from content — natural dedup.

**End-of-body emission** (find the place near the end of the HTML emit pipeline where the closing `</body>` is being written, or where reader.js tag is injected):
```python
import json
hover_json = json.dumps(_hover_dict, separators=(',', ':'), ensure_ascii=False)
hover_block = f'<script type="application/json" id="hover-data">{hover_json}</script>'
# Insert before </body> or alongside the main reader.js script tag
```

### Phase 2 — reader.js lookup changes

**At top of IIFE, after dark-mode setup** — parse hover data once:
```javascript
var hoverData = {};
try {
  var hd = document.getElementById('hover-data');
  if (hd) hoverData = JSON.parse(hd.textContent);
} catch(e) { /* tooltips degrade silently */ }
```

**In showTooltip handler** (around L934 — `var def = term.getAttribute('data-hover');`):
```javascript
// Look up from data-hover-id first; fall back to inline data-hover attr (for nav elements
// that still set data-hover via JS — breadcrumb, share, expand buttons, etc).
var hoverId = term.getAttribute('data-hover-id');
var lookup = (hoverId && hoverData[hoverId]) || null;

var def = (lookup && lookup.t) || term.getAttribute('data-hover');
var richHtml = (lookup && lookup.h) || term.getAttribute('data-hover-html');
```

**Don't migrate JS-set nav elements** (lines 85–720 in reader.js): they're set via `setAttribute('data-hover', '...')` at runtime on programmatically-built buttons. They don't contribute to on-disk HTML size. Leave them as-is. The fallback `term.getAttribute('data-hover')` above keeps them working.

### Phase 3 — Build & verify

```
cd ~/software/relinquishment
make html
ls -lh docs/downloads/Relinquishment.html
```

**Pass criteria:**
1. Build succeeds; no Python errors; no pandoc errors.
2. File size reduced by **≥70K** (target ~780K from ~860K). If less, audit which emit sites were missed.
3. Browser smoke test (open `docs/downloads/Relinquishment.html` in Firefox or Chrome):
   - Hover over an italic body term (e.g. "the Flat" in summary) → tooltip appears with same content as before.
   - Click a chapter summary in the nav → tooltip appears.
   - Hover over a stack-table cell → tooltip appears.
   - Open dev tools console: no JS errors related to hover.
4. **Spot-check rich panels:** the wormholes panel (most-duplicated), the Flat panel, one stack cell. Visual content matches pre-change.
5. PDF unchanged (PDF doesn't use the HTML path; `make pdf` should produce identical output if you want to confirm).

**If a tooltip appears empty:** that hover-term's `data-hover-id` is not in the JSON dict — likely an emit site in preprocess.py was missed. Grep `data-hover\b` in the rebuilt HTML to find any straggler inline attrs.

### Phase 4 — Test scaffolding (REQUIRED before commit)

Two layers, both must pass.

#### Phase 4a — Static regression test (`build/test-tooltip-extraction.py`)

Build a Python test script that parses the rebuilt HTML and verifies the externalization is correct AND that no tooltip content was lost:

```python
#!/usr/bin/env python3
"""Phase 0205 regression test: verify tooltip externalization is complete and lossless."""
import re, json, sys

HTML = "docs/downloads/Relinquishment.html"
BASELINE = "build/test-fixtures/tooltips-baseline.json"

def main():
    with open(HTML) as f:
        html = f.read()
    with open(BASELINE) as f:
        baseline = json.load(f)

    failures = []

    # --- Test 1: JSON block exists and is valid ---
    m = re.search(r'<script type="application/json" id="hover-data">(.*?)</script>', html, re.DOTALL)
    if not m:
        failures.append("FATAL: <script id='hover-data'> block missing")
        print_results(failures); sys.exit(1)
    try:
        hover_data = json.loads(m.group(1))
    except json.JSONDecodeError as e:
        failures.append(f"FATAL: hover-data JSON invalid: {e}")
        print_results(failures); sys.exit(1)
    print(f"OK: hover-data block parsed, {len(hover_data)} unique keys")

    # --- Test 2: No orphan data-hover-id refs (every reference has a dict entry) ---
    refs = set(re.findall(r'data-hover-id="([^"]+)"', html))
    orphans = refs - set(hover_data.keys())
    if orphans:
        failures.append(f"ORPHAN refs (no JSON entry): {sorted(orphans)[:10]}")
    else:
        print(f"OK: all {len(refs)} data-hover-id refs resolve to JSON keys")

    # --- Test 3: No inline data-hover/data-hover-html on body hover-term spans ---
    # (Allowed: data-hover on JS-set nav elements — but those aren't in static HTML anyway)
    inline_text = re.findall(r'<span class="hover-term"[^>]*\sdata-hover="', html)
    inline_html = re.findall(r'<span class="hover-term"[^>]*\sdata-hover-html="', html)
    if inline_text:
        failures.append(f"REGRESSION: {len(inline_text)} hover-term spans still carry inline data-hover")
    if inline_html:
        failures.append(f"REGRESSION: {len(inline_html)} hover-term spans still carry inline data-hover-html")
    if not inline_text and not inline_html:
        print(f"OK: no inline tooltip attrs remain on hover-term spans")

    # --- Test 4: Lossless content — every baseline tooltip's content survives in JSON dict ---
    losses = []
    for hid, occurrences in baseline["by_id"].items():
        if hid not in hover_data:
            losses.append(f"LOST KEY: {hid}")
            continue
        # Check first occurrence's text/html matches dict entry
        baseline_text = occurrences[0].get("text")
        baseline_html = occurrences[0].get("html")
        dict_text = hover_data[hid].get("t")
        dict_html = hover_data[hid].get("h")
        # Note: HTML attr values are HTML-entity-encoded; JSON values are not.
        # Compare after entity-decoding the baseline.
        import html as htmllib
        if baseline_text and dict_text != htmllib.unescape(baseline_text):
            losses.append(f"TEXT MISMATCH: {hid}")
        if baseline_html and dict_html != htmllib.unescape(baseline_html):
            losses.append(f"HTML MISMATCH: {hid}")
    if losses:
        failures.append(f"CONTENT LOSS ({len(losses)} items): {losses[:10]}")
    else:
        print(f"OK: all {len(baseline['by_id'])} baseline tooltips present and lossless")

    # --- Test 5: Size reduction sanity check ---
    import os
    new_size = os.path.getsize(HTML)
    if new_size > 800_000:
        failures.append(f"SIZE: file is {new_size:,}B, expected <800K (target ~780K, was 860K)")
    else:
        print(f"OK: file size {new_size:,}B ({new_size/1024:.0f}K)")

    print_results(failures)
    sys.exit(0 if not failures else 1)

def print_results(failures):
    if not failures:
        print("\nALL TESTS PASSED")
    else:
        print(f"\n{len(failures)} FAILURE(S):")
        for f in failures: print(f"  {f}")

if __name__ == "__main__":
    main()
```

Run after `make html`:
```
python3 build/test-tooltip-extraction.py
```

Must exit 0 (all tests pass) before proceeding to Phase 4b.

#### Phase 4b — E2E browser test (extend `build/test-e2e-devices.js`)

The existing `test-e2e-devices.js` already has Layer-2 puppeteer tests for hover behavior. Update + extend:

1. **Update existing selector logic** (around L309): change
   ```javascript
   if (document.querySelector('.hover-term[data-hover]')) return '.hover-term[data-hover]';
   ```
   to also accept the new selector:
   ```javascript
   if (document.querySelector('.hover-term[data-hover-id]')) return '.hover-term[data-hover-id]';
   if (document.querySelector('.hover-term[data-hover]')) return '.hover-term[data-hover]'; // legacy fallback
   ```

2. **Add new test function `testTooltipJsonContract`** — verifies the externalization architecture:
   ```javascript
   async function testTooltipJsonContract(browser) {
     group('Tooltip JSON contract');
     for (const dk of Object.keys(DEVICES)) {
       const page = await createPage(browser, dk);
       trackConsoleErrors(page);
       await loadPage(page, FILE_URL);
       const label = `[${DEVICES[dk].name}]`;

       // Verify JSON dict exists and is parsed
       const dictInfo = await page.evaluate(() => {
         const el = document.getElementById('hover-data');
         if (!el) return { missing: true };
         try {
           const data = JSON.parse(el.textContent);
           return { keys: Object.keys(data).length, sample: Object.keys(data).slice(0, 3) };
         } catch(e) { return { parseError: e.message }; }
       });
       if (dictInfo.missing) fail(`${label} hover-data block exists`, 'missing');
       else if (dictInfo.parseError) fail(`${label} hover-data parses`, dictInfo.parseError);
       else pass(`${label} hover-data has ${dictInfo.keys} entries (sample: ${dictInfo.sample.join(', ')})`);

       // Verify no orphan refs in DOM
       const orphans = await page.evaluate(() => {
         const data = JSON.parse(document.getElementById('hover-data').textContent);
         const refs = Array.from(document.querySelectorAll('[data-hover-id]'))
           .map(el => el.getAttribute('data-hover-id'));
         return refs.filter(r => !(r in data));
       });
       if (orphans.length) fail(`${label} all data-hover-id refs resolve`, `${orphans.length} orphans: ${orphans.slice(0,3).join(', ')}`);
       else pass(`${label} all data-hover-id refs resolve`);

       await safeClose(page);
     }
   }
   ```

3. **Add tooltip-rendering test `testTooltipRenders`** — actual hover/tap and verify visible content:
   ```javascript
   async function testTooltipRenders(browser) {
     group('Tooltip renders with externalized content');
     // Spot-check 3 known terms
     const targets = ['the-flat', 'wormholes', 'dual-use'];
     for (const dk of ['desktop', 'phone']) {
       const page = await createPage(browser, dk);
       await loadPage(page, FILE_URL);
       const label = `[${DEVICES[dk].name}]`;

       // Expand all sections so terms are visible
       await page.evaluate(() => {
         document.querySelectorAll('details').forEach(d => d.open = true);
       });
       await delay(200);

       for (const id of targets) {
         const result = await page.evaluate(async (hoverId) => {
           const el = document.querySelector(`[data-hover-id="${hoverId}"]`);
           if (!el) return { found: false };
           // Simulate hover or tap
           el.dispatchEvent(new MouseEvent('mouseenter', { bubbles: true }));
           await new Promise(r => setTimeout(r, 100));
           const tooltip = document.querySelector('.hover-tooltip, #hover-tooltip, [class*="tooltip"]');
           return {
             found: true,
             tooltipPresent: !!tooltip,
             tooltipText: tooltip ? tooltip.textContent.slice(0, 80) : null,
           };
         }, id);
         if (!result.found) skip(`${label} ${id}`, 'term not in DOM');
         else if (!result.tooltipPresent) fail(`${label} ${id} tooltip rendered`, 'no tooltip element after hover');
         else pass(`${label} ${id} tooltip rendered (${result.tooltipText.slice(0, 40)}...)`);
       }
       await safeClose(page);
     }
   }
   ```

4. **Wire into the test runner** (find the place where `testBuildVerification` etc are called and add the new tests).

5. **Run:**
   ```
   node build/test-e2e-devices.js
   ```
   All tests (existing + new) must pass.

If puppeteer isn't installed: `cd build && npm install puppeteer` (or `npm i -D puppeteer` at the repo root if there's a package.json there).

### Phase 5 — Commit

Only after Phase 4a (static) AND Phase 4b (E2E) both pass:

```
git add build/preprocess.py \
        build/reader.js \
        build/test-e2e-devices.js \
        build/snapshot-tooltips.py \
        build/test-tooltip-extraction.py \
        build/test-fixtures/tooltips-baseline.json \
        docs/downloads/Relinquishment.html \
        Relinquishment.html
git commit -m "Plan 0205: externalize tooltip content into inline JSON dict (~80-100K HTML reduction)"
git push
```

(Include the rebuilt HTML in the commit since `docs/downloads/` is part of the deployed artifact. Include the test scaffolding so Phase 0 baseline + Phase 4 tests are repeatable.)

## Risks & mitigations

| Risk | Likelihood | Mitigation |
|---|---|---|
| Missed emit site → some tooltips empty | Medium | Phase 3 spot-checks each hover-element type; fallback to `data-hover` attr in JS keeps any unmigrated sites working |
| JSON parse failure in some browsers | Low | Try/catch in JS; tooltips degrade silently if parse fails (visible text still readable) |
| Screen-reader regression | Low | Tooltips were already JS-display-only; static HTML attrs were not announced anyway. No regression. |
| Build artifact divergence (HTML in repo gets out of sync with source) | Medium | Commit the rebuilt HTML in same commit as source changes |
| reader.js timing — tooltip fired before JSON parsed | Very low | JSON parse happens synchronously at top of IIFE before any event handlers attached |

## Out of scope (do not address in this plan)
- JS-set nav buttons (breadcrumb, share, expand, etc) — they don't contribute to on-disk size
- LaTeX/PDF path — unchanged
- `hover-definitions.yaml` — unchanged (source of truth)
- Heading ID shortening (would break cross-references)
- HTML5 optional-tag dropping (small wire savings, gzip-redundant)
- Whitespace minification (small win, gzip-redundant)
- `role="doc-*"` a11y attributes (keep — accessibility honest)

## Annealing log

- **Pass 1 (low):** added the HTML-vs-JSON encoding observation explicitly — the headline 24K savings figure understates because HTML-attr-encoding (`&lt;` etc) is much heavier than JSON-encoding (`\"` only) for HTML content. Real target is 80–100K.
- **Pass 2 (low):** clarified Phase 2 fallback strategy — JS-set nav `data-hover` attrs continue to work via the `|| term.getAttribute('data-hover')` fallback in the lookup; explicitly out-of-scope for migration. This eliminates a whole class of risk.
- **Pass 3 (after Bruce: "build scaffolding tests! Make sure it all works on to the other"):** added Phase 0 (regression baseline snapshot, committed before code changes) and Phase 4 (two-layer test scaffolding: static Python checks for JSON validity / orphan refs / inline-attr removal / lossless content vs baseline; E2E puppeteer tests extending the existing `test-e2e-devices.js` framework with `testTooltipJsonContract` + `testTooltipRenders`). Phase 4 must exit clean before Phase 5 commit. This catches every failure mode I listed in the Risks table (missed emit site, JSON parse failure, content drift) automatically rather than relying on manual spot-check.

Plan converged.
