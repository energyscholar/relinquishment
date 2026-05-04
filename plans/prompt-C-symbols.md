You are the Generator.

**Repo:** ~/software/relinquishment/ (branch: main)

Read Plan 0290 in ~/software/relinquishment/plans/0290-pictogram-language-system.md for context.

## Idempotency guard

Check: does `inject_concept_symbols()` in ~/software/relinquishment/build/preprocess.py already handle "emergence" and "custodian" concepts (not just "flat")? Grep for `autocatalytic` or `"emergence"` in the function. If found, report "Phase C already applied" and exit.

## Regression baseline

BEFORE any changes, build and record counts:
```bash
cd ~/software/relinquishment
make html
grep -c 'data-concept="flat"' Relinquishment.html
```
Expected: 14. Record this number.

## Task: Generalize inject_concept_symbols()

In ~/software/relinquishment/build/preprocess.py (~line 4011), the function currently handles only "flat" (⬡) with anchor "the-flat".

GENERALIZE — do not rewrite from scratch. The existing logic is the template.

Ensure the function handles three concepts:
- "flat" with anchor "the-flat" (existing)
- "emergence" with anchor "autocatalytic" (add)
- "custodian" with anchor "custodian" (add)

Implementation:
1. Define a concept list: `[{"name": "flat", "anchor": "the-flat"}, {"name": "emergence", "anchor": "autocatalytic"}, {"name": "custodian", "anchor": "custodian"}]`
2. Loop over concepts. For each, use the same injection logic: first matching `data-hover-id` per chapter, skip inside `<summary>`, track `seen[chapter][concept]`.
3. Phase logic unchanged: ch < 8 = intro, ch < 18 = reinforce, else fluent.

## Regression gate

AFTER changes, rebuild and count:
```bash
cd ~/software/relinquishment
make html
grep -c 'data-concept="flat"' Relinquishment.html       # Must still be 14
grep -c 'data-concept="emergence"' Relinquishment.html   # Report count
grep -c 'data-concept="custodian"' Relinquishment.html   # Report count
```

If ⬡ count changed from baseline, REVERT and debug. Do not proceed.

## Verify

- No symbols inside collapsed `<summary>` elements
- Early chapters: symbols are faint (opacity 0.4). Late chapters: full opacity.

## Push to website

```bash
cd ~/software/relinquishment
git add build/preprocess.py docs/downloads/Relinquishment.html docs/downloads/Relinquishment.zip
git commit -m "Plan 0290 phase 2: concept symbol injection — emergence and custodian"
git push
```

If already applied: no commit needed.
