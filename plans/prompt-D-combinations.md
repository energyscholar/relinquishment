You are the Generator.

**Repo:** ~/software/relinquishment/ (branch: main)

Read Plan 0290 in ~/software/relinquishment/plans/0290-pictogram-language-system.md for context.

## Idempotency guard

Check: does `inject_concept_symbols()` in ~/software/relinquishment/build/preprocess.py already contain combination handling logic? Grep for `combination` or `adjacent` in the function. If found, report "Phase D already applied" and exit.

Also verify prerequisite:
```bash
cd ~/software/relinquishment
grep -c 'data-concept="emergence"' Relinquishment.html
```
Must return > 0. If not, report "Phase C not applied — run Phase C first" and exit.

## Regression baseline

Record current counts:
```bash
grep -c 'data-concept="flat"' Relinquishment.html       # Expected: 14
grep -c 'data-concept="emergence"' Relinquishment.html   # Record
grep -c 'data-concept="custodian"' Relinquishment.html   # Record
```

## Task 1: Combinations

In `inject_concept_symbols()` in ~/software/relinquishment/build/preprocess.py, ensure combination handling exists for chapters where BOTH symbols are Tier 1:
- **the-wrong-substrate:** ⬡◈ (inject both adjacent at first anchor of either)
- **instantiation:** ◈◉ (same)

For combination chapters: inject both symbols at ONE anchor point. Skip individual injection for those concepts in that chapter.

Identify chapters by matching HTML heading id/text to the chapter keys in ~/software/relinquishment/build/concept-symbols.yaml.

## Task 2: Chapter-header signatures

For each chapter in ~/software/relinquishment/build/concept-symbols.yaml, ensure a `<span class="chapter-symbols">` exists inside the chapter's `<summary>`, after the title. Show assigned concept glyphs as small muted markers.

If `.chapter-symbols` spans are already present in the output, skip.

Preserve the existing guard: inline concept spans must NOT go inside `<summary>`. Header signatures use a DIFFERENT span class (.chapter-symbols).

## Verify

```bash
cd ~/software/relinquishment
make html
grep -c 'data-concept="flat"' Relinquishment.html       # Must match baseline
grep -c 'data-concept="emergence"' Relinquishment.html   # Must match baseline
grep -c 'data-concept="custodian"' Relinquishment.html   # Must match baseline
```

- In Wrong Substrate: ⬡◈ adjacent (not in two separate locations)
- In Instantiation: ◈◉ adjacent
- Chapter headers show symbol clusters when collapsed
- visual-plain toggle hides all signatures

## Push to website

```bash
cd ~/software/relinquishment
git add build/preprocess.py docs/downloads/Relinquishment.html docs/downloads/Relinquishment.zip
git commit -m "Plan 0290 phase 3: concept symbol combinations and chapter signatures"
git push
```

If already applied: no commit needed.
