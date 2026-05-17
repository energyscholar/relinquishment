# Plan 0351: Acknowledgements Wording Fix (GenAI 47b)

**Status:** Ready for Generator
**Auditor:** Argus, S81
**GenAI UID:** 47b
**Depends on:** None
**Files:** `manuscript/99-back/afterword.tex`
**Priority:** LOW — single word change, pipeline test

---

## Objective

Change "lived through these years with me" to "lived through these years nearby" in the Acknowledgements section. Gen's rationale: "with me" implies they shared the experience of the book/research; "nearby" is geographically accurate without overclaiming their involvement.

---

## Execution

**File:** `manuscript/99-back/afterword.tex`

**Find:**
```
Friends and neighbors in Corvallis lived through these years with me.
```

**Replace with:**
```
Friends and neighbors in Corvallis lived through these years nearby.
```

---

## Verification

```bash
grep -n "lived through these years" manuscript/99-back/afterword.tex
```

Expected: one match, containing "nearby" not "with me".

---

## Do NOT

- Change any other text in acknowledgements
- Touch any other file

## Commit

`Plan 0351 (GenAI 47b): acknowledgements — 'with me' → 'nearby'`
