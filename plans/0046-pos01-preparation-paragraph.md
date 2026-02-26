# Plan 0046: Add "Preparation Not Disclosure" Paragraph to pos01

## Context

Session 24 breakthrough: the book is not a disclosure — it is preparation for a future that is coming regardless of which possibility is true. The physics (topological quantum computation) is converging in public science. Under all three possibilities, the book functions as preparation. The only scenario where it is irrelevant is A + the physics being permanently impossible (~2-5% probability).

This understanding needs to be in the A/B/C framing chapter (pos01) before shipping the DMS update.

## Target File

`manuscript/bridge/pos01-three-possibilities.tex`

## Insertion Point

After the "The Author's Position" section (line 44: "This book transmits dissonance to the reader..."), BEFORE the `\vspace{1cm}` and "You decide." block (line 46-50).

## Content

Insert the following paragraph after line 44 (`...as future events unfold.`):

```latex

This book is not a disclosure. It is preparation. The physics described here --- topological quantum computation --- is converging in public science regardless of which possibility is true. Microsoft demonstrated topological qubits in February 2025. Google crossed the quantum error correction threshold in December 2024. Whether someone built this technology thirty years ago or someone will build it ten years from now, the capability described in this book is approaching. Under A, the book is an ethical blueprint written before the technology arrives. Under B, it is that blueprint with a partial history attached. Under C, it is a record of what has already occurred. Under all three, the preparation matters. The only scenario where this book is irrelevant is one where the physics is permanently impossible --- a probability that shrinks with every published result.
```

Word count: ~120 words. (Slightly over the original ~95w target — the A/B/C breakdown requires the extra words.)

## Verification

1. [ ] Paragraph inserted after "The Author's Position" section, before "You decide."
2. [ ] No C-voice slippage — paragraph works under all three possibilities.
3. [ ] No duplication of introduction.tex "What the book is for" section.
4. [ ] Voice matches surrounding text (third person / direct address hybrid).
5. [ ] LaTeX compiles without errors.
6. [ ] PDF page count confirmed.
7. [ ] "You decide." still appears as the chapter's final line.

## Red Team (Auditor, 2026-02-25)

### PASS

- **C-voice slippage:** CLEAN. "Whether someone built this technology thirty years ago or someone will build it ten years from now" — works under all three. No privileging of C.
- **A/B/C coverage:** All three possibilities explicitly addressed with one sentence each. B is not neglected.
- **Redundancy with introduction:** The introduction says "make the model available" and "the architectural idea is coherent and implementable regardless." This paragraph says something DIFFERENT: "the physics is converging and the preparation matters." Complementary, not redundant.
- **Voice consistency:** pos01 uses a hybrid — third person ("Bruce has maintained...") and direct address ("You decide"). The new paragraph uses impersonal/third person ("This book is not a disclosure"), which matches.
- **Falsifiability:** The paragraph references specific, dated physics results (Microsoft Feb 2025, Google Dec 2024). These are verifiable.

### FLAGS

1. **MEDIUM: "shrinks with every published result" — is this too confident?** Under A, a permanently-impossible physics scenario doesn't shrink — it stays at whatever it is. The shrinking is Bruce's assessment, not objective fact. RECOMMENDATION: Keep as is. The sentence says "a probability that shrinks," which is Bruce's honest assessment. It's not claiming certainty.

2. **LOW: ~120 words vs ~95w target.** The A/B/C breakdown ("Under A... Under B... Under C...") adds ~25 words but is essential. The three-sentence breakdown is the load-bearing structure. Don't cut it.

3. **LOW: Should the paragraph mention the ethical framework (UDHR/DN)?** The introduction already covers this. pos01 is about the physics convergence making the book relevant. The ethical dimension is covered elsewhere. Don't overload.

4. **MEDIUM: Post-Tolkien consideration — should this paragraph acknowledge Bruce's own doubt?** The preceding line says "Bruce has maintained cognitive dissonance... for more than twenty years." The new paragraph shifts from uncertainty to "the preparation matters" — which could read as more confident than the preceding text. RECOMMENDATION: The paragraph is explicitly about the PHYSICS, not about Bruce's beliefs. The physics IS converging regardless of Bruce's doubt. No change needed.

5. **LOW: Post-MPI consideration — does this paragraph need anything about the author's vulnerability to self-deception?** No. That belongs in Steel-Man A. pos01 is architecture, not autobiography. Keep it clean.

6. **CONSIDERATION: The anti-monotonic shift.** Bruce noted that deeper investigation shifted him toward A. Should the "Author's Position" section be updated to reflect 20/15/65? RECOMMENDATION: Not in this plan. The current text ("I'm fine with all three and can't tell which one is closest to true") is the version that has held for years and is the right register for an early chapter. Specific numbers belong in the Steel-Man chapter. Separate plan if Bruce wants to add them.

### VERDICT: PASS. No changes required. Execute as written.

## Generator Handoff

You are the Generator. Read plan `plans/0046-pos01-preparation-paragraph.md`.

Task: Insert one paragraph into `manuscript/bridge/pos01-three-possibilities.tex` after the "Author's Position" section (after the line ending "...as future events unfold."), before the `\vspace{1cm}` and "You decide." block.

The paragraph text is in the plan. Insert it exactly as written.

After insertion, run `make` in the repository root to verify compilation. Report: page count, any LaTeX warnings, and confirm "You decide." is still the chapter's final line.
