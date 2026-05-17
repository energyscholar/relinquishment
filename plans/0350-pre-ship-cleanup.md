# Plan 0350: Pre-Ship Cleanup

**Status:** Ready for Generator
**Auditor:** Argus, S81
**Depends on:** Plans 0348 (SVG builds — update gallery statuses after)
**Files:** `build/images/magnetosphere-test.svg`, `build/images/placeholder-*.pdf`, `build/gallery-manifest.yaml`, `build/image-manifest.yaml`
**Priority:** LOW — housekeeping, no reader-facing impact

---

## Phase A: Delete dead files

Delete these files (they are not referenced by preprocess.py or any .tex file):

```bash
rm build/images/magnetosphere-test.svg
rm build/images/placeholder-magnetosphere.pdf
rm build/images/placeholder-network.pdf
rm build/images/placeholder-timeline.pdf
```

**Verify before deleting:** `grep -rn "magnetosphere-test\|placeholder-magnetosphere\|placeholder-network\|placeholder-timeline" build/preprocess.py manuscript/` should return nothing (only gallery/image manifests reference them, and we're updating those).

---

## Phase B: Update gallery-manifest.yaml

### B1: Remove magnetosphere-test entry

Find and delete the entry block for `SVG-024` (`name: magnetosphere-test`). It was a development artifact.

### B2: Update SVG-049 (spaces-between-fields) status

**Find:**
```
  status: draft
```
(in the SVG-049 block, `name: spaces-between-fields`)

**Replace with:**
```
  status: live
```

**Why:** This SVG is already inline in preprocess.py and displays correctly. Status is stale.

### B3: After Plan 0348 executes — update SVG-029, 030, 033 statuses

**Find (in each of the three blocks):**
```
  status: approved
```

**Replace with:**
```
  status: live
```

**Note:** Only do B3 if Plan 0348 has already been committed. If not, skip B3 and mark this phase incomplete.

---

## Phase C: Update image-manifest.yaml

### C1: Remove magnetosphere-test entry

Find and delete the `magnetosphere-test.svg` entry from the file-based SVGs section.

### C2: Add 5 missing figure entries

Add these to the inline SVGs section (they exist in preprocess.py but were missed in the original manifest creation):

```yaml
  - id: fig-consequence-fork
    inject_function: inject_consequence_fork
    chapter: why-relinquish
    status: live

  - id: fig-silence-gap
    inject_function: inject_silence_gap_illustration
    chapter: the-silence-gap
    status: live

  - id: fig-factor-vs-multiply
    inject_function: inject_factor_vs_multiply
    chapter: capabilities
    status: live

  - id: fig-network-resilience
    inject_function: inject_network_resilience
    chapter: capabilities
    status: live

  - id: fig-power-pattern
    inject_function: inject_power_pattern
    chapter: the-strongest-objection
    status: live
```

### C3: Fix spaces-between-fields entry

**Find:**
```
    status: not-yet-inline
```
(in the spaces-between-fields entry)

**Replace with:**
```
    status: live
```

---

## Phase D: Build verify

```bash
make html 2>&1 | grep -i "error\|WARNING"
```

No new errors expected — we only touched manifests and deleted unused files.

---

## Do NOT

- Delete any file referenced by preprocess.py
- Modify preprocess.py
- Touch .tex files
- Delete the epub-tmp copies (they regenerate on build)

## Commit

`Plan 0350: pre-ship cleanup — delete 4 dead files, update manifests`
