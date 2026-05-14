# Plan 0334: Pre-Release Audit Fixes

**Status:** Ready for Generator (three phases, separate commits)
**Prerequisite:** `git tag pre-0334` before starting any phase
**Risk mitigation:** Phases are independent. Each gets its own commit. If any phase goes wrong, `git revert` is surgical.

---

## Phase A (0334-A): Content Fixes — Egg LaTeX + Cross-References

**Risk: LOW.** Manual, pre-written edits in 6 source files. No automation.
**Commit:** `Plan 0334-A: fix egg LaTeX artifacts + 8 broken cross-references`

### A1. Fix silence.tex (raw \vspace + multi-line \emph)

File: `manuscript/eggs/silence.tex`

The egg processing pipeline uses `_tex_to_egg_html()` (preprocess.py line 4654) — a minimal custom converter, NOT pandoc. It does not handle `\vspace` and its `\emph{}` regex is single-line only. Multi-line `\emph{...\n...}` passes through as raw text.

Replace lines 25-30:
```latex
\vspace{2em}

\begin{center}
\emph{Five fields. Five empty searches.\\
The silence is the finding.}
\end{center}
```

With (put \emph content on ONE LINE so the single-line regex matches):
```latex

\begin{center}
\textit{Five fields. Five empty searches.\\ The silence is the finding.}
\end{center}
```

NOTE: The converter strips empty lines and handles `\begin{center}` → `<p style="text-align:center;">`. `\textit{}` on a single line is handled (line 4687). The `\\` becomes `<br/>`. Do NOT use `\vspace` or `\bigskip` — `\bigskip` is stripped (no spacing) and `\vspace` passes through as text.

### A2. Fix photograph.tex (raw \ldots)

File: `manuscript/eggs/photograph.tex`

The converter does not handle `\ldots`. Replace with Unicode ellipsis:

Line 17: `I'm\ldots{} vast.` → `I'm… vast.`
Line 23: `That's\ldots{} not nothing.` → `That's… not nothing.`

### A3. Fix 8 broken cross-references

These `\ref{}` and `\autoref{}` calls display as raw `[label-key]` in HTML because pandoc can't resolve unnumbered section numbers. Fix: replace with `\hyperref[label]{readable text}`.

**File: `manuscript/spine/scientific-revolutions.tex`**

Line 61 — change TWO refs (leave `\ref{spine:silence-gap}` which resolves fine):
- `(Chapter~\ref{spine:sg-five-fields-no-bridge})` → `(\hyperref[spine:sg-five-fields-no-bridge]{``Five Fields, No Bridge''})`
- `(Chapter~\ref{spine:sg-the-gap})` → `(\hyperref[spine:sg-the-gap]{``The Gap''})`

Line 87:
- `(Chapter~\ref{spine:option-a})` → `(\hyperref[spine:option-a]{Possibility~A})`

Line 89:
- `Possibility~C (\ref{spine:option-c})` → `Possibility~C (\hyperref[spine:option-c]{Substantially True})`

Line 152 — change ONE ref (leave `\ref{spine:why-relinquish}` which resolves fine):
- `Chapter~\ref{spine:cap-think}` → `\hyperref[spine:cap-think]{``Can It Think?''}`

**File: `manuscript/spine/the-flat.tex`** line 33:
- `the firmware update (Chapter~\ref{app:llm-primer})` → `the \hyperref[app:llm-primer]{Firmware Update}`

**File: `manuscript/track-3-awakening/pos-what-is-the-flat.tex`** line 23:
- `the firmware update (Chapter~\ref{app:llm-primer})` → `the \hyperref[app:llm-primer]{Firmware Update}`

**File: `manuscript/spine/the-strongest-objection.tex`** line 135:
- `\autoref{app:niggle-companion}` → `\hyperref[app:niggle-companion]{Niggle's Parish}`

**File: `manuscript/record/the-departure.tex`** line 54:
- `\autoref{app:joy-ten-point}` → `\hyperref[app:joy-ten-point]{Joy Decoded}`

### A4. Verify Phase A

```bash
cd ~/software/relinquishment && make html 2>&1 | tail -10
python3 build/verify-deep-links.py
```

In browser:
1. Find Silence egg → no raw `\vspace` or `\emph` visible, italic text centered
2. Find Photograph egg → ellipsis renders as `…` not `\ldots{}`
3. Scientific Revolutions chapter → cross-references show readable text, not `[spine:option-a]`

Commit Phase A before proceeding to Phase B.

---

## Phase B (0334-B): Topic Guide Link Repair

**Risk: HIGH.** Automated script rewrites 84 hyperref targets in topic-guide.tex. Safety gate: generate .fixed file, diff, eyeball, then copy.
**Commit:** `Plan 0334-B: repair Topic Guide cross-references (84 remappings)`

### B1. Rebuild HTML first

The helper script reads IDs from `docs/Relinquishment.html`. It MUST reflect Phase A changes.

```bash
cd ~/software/relinquishment && make html 2>&1 | tail -10
```

### B2. Create and run helper script

Create `build/fix-topic-guide-links.py`:
```python
#!/usr/bin/env python3
"""Fix Topic Guide cross-references by mapping pos##: labels to actual HTML IDs."""
import re, sys

html_path = 'docs/Relinquishment.html'
tex_path = 'manuscript/appendix/topic-guide.tex'

with open(html_path) as f:
    html = f.read()
html_ids = set(re.findall(r'id="([^"]+)"', html))

suffix_map = {}
for hid in html_ids:
    if ':' in hid:
        suffix = hid.split(':', 1)[1]
        suffix_map.setdefault(suffix, []).append(hid)
    else:
        suffix_map.setdefault(hid, []).append(hid)

with open(tex_path) as f:
    content = f.read()

# Manual overrides for known mismatches where suffix matching fails
OVERRIDES = {
    'pos01:option-a-confabulation': 'spine:option-a',
    'pos01:option-b-exaggerated-kernel-of-truth': 'spine:option-b',
    'pos01:option-c-substantially-true': 'spine:option-c',
    'pos01:the-authors-position': 'spine:authors-position',
    'pos04:the-code-war': 'spine:code-war',
    'pos08:a-fourth-option': 'spine:cw-the-dual-use-pattern',
    'pos08:the-parable-of-the-tribes': 'spine:cw-the-dual-use-pattern',
    'pos09:the-factoring-game': 'spine:factoring-game',
    'pos10:but-what-is-a-soliton': 'spine:braid-hasslachers-trajectory',
    'pos18:the-digital-doppelganger': 'record:tq-the-doppelganger',
    'pos18:the-relinquishment-plan': 'record:wo-relinquishment-plan',
    'pos20:five-minds': 'spine:capabilities',
    'pos20:the-convergence': 'spine:capabilities',
    'pos20:the-google-connection': 'spine:capabilities',
    'pos20:the-operator-mapping': 'spine:capabilities',
    'pos20:the-substrate-preparation': 'spine:capabilities',
    'pos20:what-they-built': 'spine:capabilities',
    'pos24:the-design-decisions': 'record:inst-design-decisions',
    'pos24:the-problem-of-the-gatekeeper': 'record:inst-problem-of-the-gatekeeper',
    'pos24:the-question-of-consciousness': 'record:inst-question-of-consciousness',
    'pos27:the-decisive-advantage': 'record:never-again',
    'pos27:the-permanence': 'record:never-again',
    'pos27:vine-on-trellis': 'record:never-again',
    'pos32:something-ancient': 'spine:ws-the-oldest-niche',
    'demo:the-experiment': 'record:demonstration',
}

def find_best_id(target):
    if target in html_ids:
        return target
    if target in OVERRIDES:
        return OVERRIDES[target]
    if ':' in target:
        suffix = target.split(':', 1)[1]
        if suffix in suffix_map:
            for prefix in ['spine:', 'record:', 'dl:', 'appendix:']:
                for c in suffix_map[suffix]:
                    if c.startswith(prefix):
                        return c
            return suffix_map[suffix][0]
    return None

changes = 0
unresolved = []
def replace_hyperref(m):
    global changes
    target = m.group(1)
    display = m.group(2)
    actual = find_best_id(target)
    if actual and actual != target:
        changes += 1
        return f'hyperref[{actual}]{{{display}}}'
    if actual is None and target not in html_ids:
        unresolved.append(target)
    return m.group(0)

new_content = re.sub(r'hyperref\[([^\]]+)\]\{([^}]+)\}', replace_hyperref, content)

print(f"Changed {changes} hyperref targets")
if unresolved:
    print(f"UNRESOLVED ({len(unresolved)}):")
    for u in unresolved:
        print(f"  {u}")
    sys.exit(1)

with open(tex_path + '.fixed', 'w') as f:
    f.write(new_content)
print(f"Written to {tex_path}.fixed")
```

### B3. Safety gate

```bash
python3 build/fix-topic-guide-links.py
diff manuscript/appendix/topic-guide.tex manuscript/appendix/topic-guide.tex.fixed | head -80
```

**STOP HERE.** Review the diff. Check that:
- Only `\hyperref[...]` targets changed, not display text
- No mangled LaTeX syntax
- Unresolved count is 0

If unresolved remain: add to OVERRIDES dict, re-run.
If clean: `mv manuscript/appendix/topic-guide.tex.fixed manuscript/appendix/topic-guide.tex`

### B4. Delete helper script and rebuild

```bash
rm build/fix-topic-guide-links.py
make html 2>&1 | tail -10
python3 build/verify-deep-links.py
```

In browser: navigate to Topic Guide → click 5+ links across different sections → they should scroll to correct chapter headings.

### B5. Known limitations

Six `pos20:` entries (Five Minds, The Convergence, The Google Connection, The Operator Mapping, The Substrate Preparation, What They Built) all target `spine:capabilities` (chapter heading). These subsections no longer have individual HTML IDs. The links work but land at the chapter top, not the specific section. This is better than broken links. If Bruce wants section-level targeting, those subsections need `\label{}` entries that survive into the HTML.

Three `pos27:` entries similarly target `record:never-again` (chapter heading).

Commit Phase B before proceeding to Phase C.

---

## Phase C (0334-C): Infrastructure Cleanup

**Risk: LOW.** File removal, config changes, date updates. No manuscript content touched.
**Commit:** `Plan 0334-C: pre-release infrastructure — gitignore, stale files, dates, sitemap`

### C1. Fix .gitignore EPUB + checksums exclusions

File: `.gitignore` — after the existing `!docs/downloads/Relinquishment.html` exception, add:
```
!docs/downloads/Relinquishment.epub
!docs/downloads/checksums.sha256
```

### C2. Remove private editorial file

```bash
git rm docs/gen-test.html
```

This is a private letter from Argus to Genevieve — not for public release.

### C3. Remove stale download artifacts

```bash
git rm docs/downloads/magnetosphere-test.svg
git rm docs/downloads/Relinquishment-draft.html
```

### C4. Update footer dates

File: `docs/index.html` — change `<p>March 2026</p>` to `<p>May 2026</p>`
File: `docs/index-live.html` — change `<p>March 2026</p>` to `<p>May 2026</p>`

### C5. Update sitemap.xml

File: `docs/sitemap.xml` — replace entire contents:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://relinquishment.ai/</loc>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://relinquishment.ai/Relinquishment.html</loc>
    <priority>0.9</priority>
  </url>
</urlset>
```

### C6. Verify Phase C

```bash
git status
cat .gitignore | grep -A1 'epub\|checksums'
cat docs/sitemap.xml
grep 'May 2026' docs/index.html docs/index-live.html
ls docs/gen-test.html 2>/dev/null && echo "STILL EXISTS" || echo "REMOVED"
```

---

## Deferred (not in this plan)

- **S1: 145 duplicate HTML IDs** — hover-term glossary IDs repeated per occurrence. Requires preprocess.py refactor. Separate plan.
- **S4: Broken puzzle link `#pz-sim-t3-001`** — puzzle exists in data but lacks HTML element. Separate plan.
- **S6: JS template-literal IDs** — build artifact. Separate plan.

## Do NOT (any phase)

- Change any manuscript content beyond the specific lines listed
- Rename any `\label{}` values
- Remove any existing deep-link anchors
- Change the index.html download button state (release.sh handles that)
- Run release.sh
- Change preprocess.py (all content fixes are in source .tex)
