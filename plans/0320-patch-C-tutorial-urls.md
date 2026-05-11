---
Plan-UID: 0320-v6 Patch C
Status: READY FOR GENERATOR
---

# Patch C: Fix Tutorial Catalog URLs

## What to modify

File: `~/software/persistent-ai-collaboration/index.html`

## Change

All 12 tutorial links in Accordion 5A point to the private `has-anyone-looked` repo. The tutorials have been copied to the public `persistent-ai-collaboration` repo under `tutorials/`.

Find-and-replace the base URL across all 12 links:

**Old:** `https://github.com/energyscholar/has-anyone-looked/blob/main/tutorials/`
**New:** `https://github.com/energyscholar/persistent-ai-collaboration/blob/main/tutorials/`

## Constraints

- This is a mechanical URL substitution. Do NOT modify any surrounding text, descriptions, or HTML structure.
- All 12 occurrences must be changed. Verify count matches before and after.
- Do NOT modify any other links in the document.

## Report format

"Plan-UID: 0320-v6 Patch C complete. 12 URLs updated."
