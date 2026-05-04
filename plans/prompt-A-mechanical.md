You are the Generator.

**Repo:** ~/software/relinquishment/ (branch: main)

## Idempotency guard

Before any changes, check these indicators. If ALL are true, report "Phase A already applied" and exit.
- ~/software/relinquishment/build/concept-symbols.yaml exists
- `.tech-grade::after` in ~/software/relinquishment/build/preprocess.py already has `opacity: 1.0`
- ~/software/relinquishment/manuscript/00-front/hook.tex contains "Those same flat worlds also occur naturally"

If only SOME are true, a partial application occurred. Fix only the missing parts.

## Task 1: Badge visibility (preprocess.py CSS)

In ~/software/relinquishment/build/preprocess.py CSS block:

Ensure `.tech-grade::after` has: `font-size: 0.95em; opacity: 1.0;`
Ensure `.tech-grade` has `padding: 0 0.3em;`
Ensure all `border-left` for `details.tech-section` and `details.tech-borderline` are `4px` (3 occurrences: light mode ~line 902, dark mode ~line 955, borderline ~line 986).

## Task 2: First-occurrence badge explanation

In `collapse_tech_sections()` (~line 3688 of ~/software/relinquishment/build/preprocess.py), ensure that the FIRST tech-section wrapped gets this injected after `</summary>`:

```html
<p class="tech-first-note">Sections marked ✔ contain verified science — published, peer-reviewed physics. Expand if curious; skip without losing the story.</p>
```

If `tech-first-note` already exists in the function, skip. Add CSS if not already present:
```css
.tech-first-note { font-size: 0.82em; font-style: italic; color: #888; margin: 0.3em 0 0.5em 1em; }
```

## Task 3: Badge tooltip

In `collapse_tech_sections()`, ensure the tooltip/title string for tech-section summaries is:

"This section attempts scientific accuracy. Every claim is sourced to published, peer-reviewed, reproducible research. Where it speculates, it says so. Expand if curious; the story continues without it."

If this string is already present, skip.

## Task 4: Concept symbol CSS (preprocess.py)

Ensure the concept-symbol CSS block (currently ~lines 1011-1017) contains rules for all 7 symbols (flat, emergence, custodian, silence, capabilities, stewardship, services) plus phase/track/tier rules. If the block only has `[data-concept="flat"]::before`, replace it with the full block from Plan 0290 (~/software/relinquishment/plans/0290-pictogram-language-system.md) lines 286-347. If already has all 7, skip. Keep the dark-mode override at ~line 964.

## Task 5: Hook fix

In ~/software/relinquishment/manuscript/00-front/hook.tex, ensure line 30 area reads:

```
They are inside every computer chip you own.

Those same flat worlds also occur naturally. Earth's magnetic field has held them for billions of years.
```

If "Those same flat worlds" is already present, skip.

## Task 6: Create concept-symbols.yaml

If ~/software/relinquishment/build/concept-symbols.yaml exists, skip. Otherwise copy the manifest from Plan 0290 lines 85-228 exactly.

## Build, verify, push

```bash
cd ~/software/relinquishment
make html
grep -c 'data-concept="flat"' Relinquishment.html  # Must be 14
```

Check: ✔ bigger/brighter, new tooltip on hover, first-occurrence note visible, hook has breath between chip and magnetosphere.

Push to website:
```bash
cd ~/software/relinquishment
git add docs/downloads/Relinquishment.html docs/downloads/Relinquishment.zip
git add build/concept-symbols.yaml
git commit -m "Plan 0289B+D, 0290P1: badge visibility, hook pacing, concept symbol CSS and manifest"
git push
```

If no changes were made: report "Phase A already applied, no commit needed."
