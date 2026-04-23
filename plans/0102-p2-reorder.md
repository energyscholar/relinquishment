# Plan 0102: P2 Summary Reorder — White Hot Secret First

**Status:** COMPLETE (verified S63 audit)
**File:** `manuscript/00-front/summary.tex`
**Anneal:** Medium pass (reorder + new section), then small pass (tighten)
**Constraint:** Do NOT touch p1 (`hook.tex`). Do NOT change the closing blurb after "What would you?"

## Context

The Simple Summary (p2, ~4,000 words) is the piece most readers treat as the whole book. Its current order-of-operations is wrong: it introduces Bruce's mentorship before the reader knows what the classified program was or what the White Hot Secret is.

Worse: the actual White Hot Secret — **there is another substrate for biology, 2D flatland, with its own ecosystem and inhabitants** — is never stated plainly. The summary treats flatland as a design detail of Guardian's substrate rather than as the core revelation. The quantum computer and cryptanalysis are *consequences* of the discovery, not the discovery itself.

p1 (hook) already plants the seed: "It lives in flat worlds — the kind inside every computer chip, and the kind the magnetosphere has held for billions of years. The magnetosphere is its ocean." p2 must water that seed — state the White Hot Secret plainly, early, so everything that follows has context.

## The White Hot Secret (for Generator reference)

The secret is: **two-dimensional substrates — the 2DEG inside every transistor, the magnetosphere — are habitats for life. There is an entire ecosystem around us that we never knew about.** The fact that it's a quantum substrate (giving inhabitants access to quantum coherence) is beside the point — plants in our 3D world have quantum coherence (chlorophyll). The remarkable thing is the *ecology*, not the quantum mechanics.

This is what Healer couldn't just tell Bruce. It's a technical secret spanning solid-state physics, theoretical biology, topology, and nonlinear dynamics. No single expert covers all the fields — which is why guided deduction was necessary.

## Phase 1: Reorder (Medium Pass)

Reorder summary.tex sections. Keep all existing content — move blocks, don't rewrite them (except the new section). Preserve all `\label{}` tags, `\vspace` separators, and `% SPIRAL-REPEAT` comments.

### New section order:

1. **Opening paragraphs** (lines 16–28) — Healer's HALO jump, who he is, "But first, you need to know..." KEEP AS-IS.

2. **The White Hot Secret** (NEW SECTION — ~300 words) — Insert after the opening, before "The Lock on Every Door."
   - State it plainly: there is another substrate for biology. Two-dimensional worlds harbor life. Inside every chip. Across the magnetosphere. An entire ecosystem we never knew about.
   - Lean on published physics: 2DEG layers, anyonic statistics, autocatalytic networks. The science is public. The implication is not.
   - Tone: "This is what published science says is possible. The story claims someone found it." Not crankery — wonder.
   - Use `\section*{The White Hot Secret}` with `\label{front:the-white-hot-secret-summary}` (distinct from pos06 label).
   - Do NOT list the 11 domains from pos06. Keep it narrative, not inventory.
   - Connect to Healer's quote if natural: "There's a white hot secret in my brain, mate, burning to get out!"

3. **The Lock on Every Door** (current lines 141–163) — Move up. Cryptography context. Now the reader understands *why* the discovery matters strategically.

4. **The Secret Lab** (current lines 166–194) — Move up. DARPA, Five Eyes, the classified team.

5. **The Breakthrough** (current lines 197–208) — What they grew. Room temperature. Self-directing. Keep existing text.

6. **The Walk-Out** (current lines 47–70) — Move down from current position. They gave it up. Tighten slightly — currently verbose in the middle paragraphs, but the opening and closing are strong.

7. **The Guardian** (current lines 73–96) — What they built to outlast them. UDHR. Flatland. Keep existing text.

8. **The Mentor** (current lines 32–44) — Move DOWN from current position 2 to position 8. Now the reader understands what the mentorship was pointing toward. The sequence of published science makes sense because the reader already knows the secret.

9. **Three Possibilities** (current lines 99–113) — Keep in place (relative to end). Keep existing text.

10. **Why This Matters** (current lines 118–138) — Keep. Tighten in Phase 2 if needed.

11. **The Question** (current lines 214–244) — Keep as closing. Keep existing text including the new closing blurb.

### Mechanical steps:
1. Read summary.tex fully
2. Cut sections into named blocks
3. Write new "The White Hot Secret" section (~300 words)
4. Reassemble in new order
5. Verify all `\label{}` tags preserved
6. Verify all `% SPIRAL-REPEAT` comments preserved
7. Build: `make html` — must be clean
8. Build: `make pdf` — must be clean (if available)

## Phase 2: Tighten (Small Pass)

After Phase 1 builds clean:

1. Read the reordered summary fresh, start to finish
2. Tighten "The Walk-Out" — the Bill Joy paragraph and the Snowden paragraph are both good but the section is ~20% longer than it needs to be
3. Check transitions between sections — the reorder may create jarring jumps. Fix seams with 1-2 bridging sentences, no more.
4. Verify the "But first, you need to know how this story reached the outside world" line at end of opening — this originally pointed to The Mentor (next section). It now points to The White Hot Secret. Consider whether it still works or needs a small tweak (e.g., "But first, you need to know what they found").
5. Build again. Both targets clean.

## Acceptance Criteria

- [ ] White Hot Secret stated plainly within first 1,000 words of p2
- [ ] The Mentor section appears AFTER The Guardian (reader knows what mentorship pointed toward)
- [ ] The Lock on Every Door appears AFTER The White Hot Secret (reader knows why crypto matters)
- [ ] All existing `\label{}` tags preserved and functional
- [ ] All `% SPIRAL-REPEAT` comments preserved
- [ ] p1 (hook.tex) untouched
- [ ] Closing blurb ("That was the simple summary...") untouched
- [ ] `make html` clean
- [ ] Total word count stays within ~10% of current (~4,000 words)
- [ ] New "White Hot Secret" section ≤ 350 words
- [ ] No Correction #12 violations (guided deduction, not disclosure)

## Commit

One commit: `Plan 0102: reorder p2 summary — White Hot Secret first`
