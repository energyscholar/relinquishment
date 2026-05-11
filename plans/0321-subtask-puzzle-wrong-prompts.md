# Subtask: Per-Option Wrong Prompts for Guided Deduction Puzzles

**Output:** Modify `build/puzzle-data.yaml` and `build/build-puzzles.py`
**Commit:** `Plan 0321: per-option wrong prompts for guided deduction puzzles`
**Read first:** Both files. Changes are small — 3 edits total.

## Problem

Guided deduction puzzles have one `wrong_prompt` per stage. Sometimes a wrong
answer deserves a specific response different from the generic one.

## Edit 1: puzzle-data.yaml (line ~841)

In puzzle `pz-gd-t1-001`, stage 2 (question: "Why would a teacher use questions
instead of just explaining?"), ADD a `wrong_prompts` dict ABOVE the existing
`wrong_prompt` line:

```yaml
        wrong_prompts:
          a: "Possibly true in this case but we're looking for the answer that helps the student learn best."
        wrong_prompt: "Is it really just avoidance or trickery? ..."
```

The existing `wrong_prompt` stays — it's the fallback for options b, c, d.

## Edit 2: build-puzzles.py (line ~306)

In the `gd` stage builder, add `wrong_prompts` to the dict. After line 306:

```python
                'wrong_prompt': st.get('wrong_prompt', ''),
                'wrong_prompts': st.get('wrong_prompts', {}),
```

## Edit 3: build-puzzles.py (line ~1878)

In the JS wrong-answer handler, check per-option prompt before generic.
Replace lines 1878-1881:

```javascript
                if (wrongEl && stage.wrong_prompt) {
                  wrongEl.textContent = stage.wrong_prompt;
                  wrongEl.classList.add("visible");
                }
```

With:

```javascript
                var wp = (stage.wrong_prompts && stage.wrong_prompts[key]) || stage.wrong_prompt;
                if (wrongEl && wp) {
                  wrongEl.textContent = wp;
                  wrongEl.classList.add("visible");
                }
```

That's it. Three edits, two files, no new files.

## Test

Run `python3 build/build-puzzles.py` — should complete without error.
Open the built puzzles.html, find "The Method", answer question 2 with option A.
Should see: "Possibly true in this case but we're looking for the answer that
helps the student learn best."
Answer with option C or D — should see the generic wrong_prompt instead.

## Report

State: build succeeded, confirm per-option prompt appears for option A.
