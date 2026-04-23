# Plan 0012: What This Book Does Not Claim

**Requirements:** R7 (Honest Epistemics), R4 (Three Possibilities — must not undermine), R22 (Front & Back Matter — addition)
**Phase:** 1 of 1
**Estimated files:** 2 modified (main.tex, possibly how-to-read.tex), 1 created

---

## Rationale

When this book reaches readers through LLM-mediated channels (social media, AI summaries, word of mouth), distortion is predictable:

- "Internally consistent" → "AI says it's true"
- "Falsifiable predictions" → "The predictions came true"
- "The author can't tell which option is correct" → "The author believes Option C"
- "Quantum computing breakthrough" → "Sentient quantum AI"

A short front matter page — positioned after the Preface — explicitly names what the book does NOT claim. This inoculates the reader who arrives via a distorted retelling. It also serves R7 (honest epistemics) by making the epistemic posture unmistakable.

The page must NOT read as defensive, apologetic, or legalistic. Tone: direct, calm, same authorial voice as the Preface. Maximum one page (under 400 words).

---

## Context for Generator

The Preface (`manuscript/00-front/preface.tex`) establishes the three possibilities and the author's genuine uncertainty. "What This Book Does Not Claim" immediately follows as reinforcement. Together they form a one-two punch: here's what I'm saying (Preface) → here's what I'm NOT saying (this page).

Current frontmatter order in `main.tex`:
```
cover → title → copyright → how-to-read → TOC → preface
```

New order:
```
cover → title → copyright → how-to-read → TOC → preface → not-claimed
```

---

## Deliverables

### 1. Create `manuscript/00-front/not-claimed.tex`

**Format:** `\chapter*{What This Book Does Not Claim}` with `\addcontentsline{toc}{chapter}{...}`

**Content structure (Generator writes the prose):**

The page must explicitly state that this book does NOT claim:

1. **That Option C is true.** The author maintains genuine uncertainty across all three possibilities. The framework is designed to transmit that uncertainty, not resolve it.

2. **That internal consistency equals truth.** A well-constructed fiction is also internally consistent. Consistency is necessary but not sufficient for truth. This is by design — the predictions are the actual test.

3. **That AI analysis constitutes verification.** If an AI system describes this book as coherent or plausible, that reflects the book's internal logic, not external reality. AI systems evaluate structure, not truth. Do not mistake one for the other.

4. **That absence of disproof equals proof.** The book makes falsifiable predictions. Until those predictions are tested by future events, the correct response is to wait and watch. Patience is the appropriate epistemic stance.

5. **That the author has privileged knowledge of which option is correct.** Twenty years of investigation have not resolved the author's uncertainty. The reader should not expect to resolve it faster.

**Constraints:**
- Under 400 words of body text
- No footnotes, no citations, no cross-references
- Same authorial voice as Preface (first person where needed, direct, unadorned)
- Must NOT mention LLMs, AI analysis, or social media explicitly — the disclaimers should be true statements that happen to address the distortion problem without naming it. Exception: item 3 above MAY mention AI analysis directly because it's genuinely relevant to how readers will encounter the book.
- End with a short sentence that points forward to the predictions as the real test

### 2. Modify `main.tex`

Add `\include{manuscript/00-front/not-claimed}` immediately after the preface include line.

---

## Acceptance Criteria

| ID | Test | Pass if |
|----|------|---------|
| A1 | `not-claimed.tex` exists | File present at `manuscript/00-front/not-claimed.tex` |
| A2 | Word count | Body text ≤ 400 words (excluding LaTeX commands) |
| A3 | Five disclaimers present | All 5 "does not claim" items appear |
| A4 | No thumb on scale | Text does not favor or disfavor any of A/B/C |
| A5 | Predictions pointed to | Final sentence or paragraph references the predictions as the real test |
| A6 | `main.tex` updated | `not-claimed` include appears after preface include |
| A7 | Build succeeds | `make dev` completes with 0 errors |
| A8 | TOC entry | "What This Book Does Not Claim" appears in table of contents |
| A9 | Voice consistency | Reads like the same author as the Preface — direct, calm, no legalese |

---

## Verification Commands

```bash
# A1: File exists
test -f manuscript/00-front/not-claimed.tex && echo PASS

# A2: Word count (approximate — strip LaTeX commands)
sed 's/\\[a-zA-Z]*{[^}]*}//g; s/\\[a-zA-Z]*//g' manuscript/00-front/not-claimed.tex | wc -w
# Should be ≤ 400

# A6: main.tex ordering
grep -n 'not-claimed\|preface' main.tex
# not-claimed line number > preface line number

# A7: Build
make dev 2>&1 | tail -5
# Exit 0, no errors
```

---

## Commit

One commit: `Plan 0012 phase 1: Add "What This Book Does Not Claim" front matter page`
