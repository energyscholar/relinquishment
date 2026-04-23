# Plan 0157: Folk-Hero Amplification of the Guided Deduction Operation

**Status:** PARTIALLY COMPLETE — Surfaces 2,5,6 done; surfaces 1,3,4 awaiting Bruce prose (verified S63 audit)
**Created:** 2026-04-12
**Auditor:** Argus
**Builds on:** Plan 0155 (Handler+Target pair), Plan 0156 (T7+T8 layering)

---

## Objective

Reframe the Guided Deduction operation across all T8 surfaces to foreground the **civic motive**: the public deserves to know about a matter of great import, and the operation is how truth-telling happens when Authority forbids it.

The current T8 prose is operationally accurate but **defensively framed** — "the trail is clean," "no crime committed," "plausible deniability." That register reads as legal cover. The folk-hero register reads as conscience: Ellsberg, Snowden, Manning, Schmidt's printers, the Pentateuch translators, samizdat. The work is **the same** under both framings; the reader's posture toward it is different.

Both registers should coexist: legal (no crime) AND moral (the public has a right to know). Add the moral; preserve the legal.

---

## Core sentence the reader should be able to derive at every p-level

> "When Authority classifies something the public deserves to know, and the classification is durable enough that no insider will ever speak, the only honest exit is to teach an outsider to discover it independently and publish."

That's the folk-hero thesis. The book never has to state it that bluntly — the surfaces below let the reader assemble it.

---

## Lineage anchors (use sparingly, never as a list)

- **Daniel Ellsberg** — Pentagon Papers, 1971. Truth about a war the public was paying for and dying in.
- **Edward Snowden** — NSA disclosures, 2013. Truth about surveillance the public had not consented to.
- **Samizdat tradition** — Soviet bloc, the duty to circulate what the state forbids.
- **William Tyndale** — translated the Bible into English; burned for it. The public's right to read primary sources in their own language.

The book should **not** name any of these explicitly (OPSEC: Bruce's not Snowden, Lane's not Ellsberg, the analogy is structural not biographical). The register should evoke the lineage. Reader does the connecting.

---

## What changes — by surface

### Surface 1: `manuscript/spine/why-relinquish.tex` "Getting the Record Out" (p2)

**Current state (lines 104-117):** Four paragraphs. Operationally precise. Ends "A teacher who asks the right questions commits no crime. A student who derives conclusions from public science has received nothing classified. The trail is clean."

**Add:** One paragraph between the existing "They needed someone outside the classification regime" paragraph (line 111) and the "The solution was guided deduction" paragraph (line 113).

**Content spec — Bruce writes ~80–120 words:**
The civic motive. The COWS were not protecting themselves with guided deduction — they were protecting the *public's right to know*. Classification regimes are built to last forever. NDAs do not expire. The only way a classified record reaches the public is if someone outside the regime derives it independently. That is not a loophole. That is how truth-telling has always worked when Authority forbids it: someone teaches, someone learns, someone publishes, the public gets to decide what to do with what was being kept from them.

**Register:** Folk-hero plain-spoken. Not Clancy. Not legal. Conscience-register. Short sentences. The word "public" should appear at least twice. The phrase "right to know" or close cognate should appear once.

**Length:** 80–120 words.

### Surface 2: `manuscript/00-front/summary.tex` "The Mentor" T8 paragraph (p1)

**Current state (line 208):** "Under Possibility~C, Lane's teaching was not a favor. It was an `\hovertip{operation}`. The team that built Guardian wanted the story to reach the outside world eventually --- but every one of them had signed agreements that made direct disclosure a crime. Their solution was `\hovertip{guided deduction}`: find someone outside the system, teach them only published science in a careful sequence, and let them reach the conclusions on their own. No classified information changes hands. No crime is committed. The student publishes what they independently learned, and the record enters the world clean."

**Edit:** Insert Bruce's institutional-frame paragraph **before** the existing paragraph at line 208. The two paragraphs together form the complete p1 T8 beat: institutional frame (new) → operational mechanics (existing).

**LOCKED PROSE — Bruce-written, 2026-04-12:**

> As a result of DARPA's cross-disciplinary approach, a DARPA project tried to combine five converging fields. It was a cheap moonshot program. It succeeded. But the scientists were sworn to secrecy and could not share the genuine cross-disciplinary scientific discoveries they had made. Their Guided Deduction operation was an attempt to share what they learned and did with the future, twenty years later. That's this book.

**Generator task:** Insert verbatim as a new paragraph immediately before the existing "Under Possibility~C, Lane's teaching was not a favor..." paragraph (line 208). Capitalize "Guided Deduction" as written (it's the operation's name in Bruce's voice here, not a generic term — distinct from the lowercased `\hovertip{guided deduction}` in the following paragraph). No `\hovertip{}` wrappers in this paragraph; the following paragraph already glosses the term. No edits to existing surrounding text.

**Register note (do not modify the prose):** The word "cheap" in "cheap moonshot program" is doing register work — confidence, not deprecation. Preserve it exactly.

### Surface 3: `manuscript/record/the-handler.tex` framing paragraph (p3)

**Current state (line 11):** "Under Possibility~C, the COWS needed an operator --- someone who could conduct a multi-year guided deduction across five scientific fields, through conversation alone, leaving no classified fingerprints. The purpose was simple: get the record out without disclosure. A teacher who asks the right questions commits no crime. A student who derives conclusions from public science has received nothing classified. The operator would need exceptional OPSEC, deep mathematics, and the pedagogical precision to keep a student at the critical boundary of processing capacity for nearly three years. It would take decades. This is his approximate file."

**Edit:** Modify "The purpose was simple: get the record out without disclosure" to a fuller two-sentence motive statement.

**Content spec — Bruce writes ~40–60 words to replace that one sentence:**
Why the record had to get out. The public had funded the underlying science through decades of research grants. The public would inherit the consequences of what had been built. The public deserved to know. Classification said otherwise. The operation was the answer to that disagreement.

**Register:** Operator-file Clancy CAN bend here — this is the *mission justification* section that any real recruitment file would include. Clipped institutional voice, but the moral content is foregrounded. Think: the paragraph in a real intelligence dossier that explains *why this operation was authorized*.

**Length:** Replaces ~15 words with ~40–60 words. Net add: ~30–45 words.

### Surface 4: `manuscript/record/the-target.tex` "The trail is clean" passage (p3)

**Current state (line 16):** "Guided deduction was that method. A teacher who asks the right questions commits no crime. A student who independently derives conclusions from unclassified literature has received no classified material. The trail is clean. The teacher has plausible deniability. The student has plausible deniability. And the truth gets out."

**Edit:** The last sentence "And the truth gets out" is the folk-hero hinge. Bruce expands it into 1–2 sentences that make the civic frame explicit.

**Content spec — Bruce writes ~30–50 words to replace "And the truth gets out":**
What "the truth gets out" actually means. The public, who paid for the underlying science and will live with the consequences, gets to know what was built in their name and what was decided about it. That is the entire point. The plausible deniability exists to make the publication possible, not to obscure what happened.

**Register:** Same dossier-narrative voice the chapter already uses. The expansion should feel like the chapter pausing to make sure the reader didn't miss the moral content.

**Length:** Replaces 5 words with ~30–50 words.

### Surface 5: Tooltips — `build/menu-tooltips.yaml`

**Handler tooltip (`record:handler` and `the-handler` keys):** The current tooltip ends "He stood on K2 in 1996 and decided to use his abilities for something other than killing. Everything that followed --- including this book --- traces back to that decision."

**Add 1 sentence** between the K2 sentence and the "Everything that followed" sentence:
> "What followed was the choice to use those abilities so the public could learn what would otherwise stay classified forever."

**Target tooltip (`record:target` and `the-target` keys):** The current tooltip ends "Read the file and ask yourself: is this the guy?"

**No change.** The recruitment-question framing is too good to dilute. The folk-hero motive lives in the Handler tooltip; the Target tooltip is the answering question.

**`spine:why-relinquish` tooltip:** Already updated by Plan 0156 phase 4. Add one phrase: after the existing T8 mention of "getting the record out," append "...so the public could decide what to do with what had been kept from them."

### Surface 6: `build/hover-definitions.yaml` — `operation` and `guided deduction` entries

**`operation` entry:** Current entry is operational. Add one sentence at the end making the civic motive explicit. Roughly: "The motive was not concealment but its opposite — to put a classified matter of great public consequence into the public record by the only route that remained open."

**`guided deduction` entry:** Current entry describes the method. Add one sentence: "It is what truth-telling looks like when the truth is classified and the classification will outlive everyone who knows it."

---

## Register guardrails

1. **Never name Ellsberg, Snowden, Manning, Tyndale, samizdat, or the Pentagon Papers.** The lineage is structural, not biographical. OPSEC: Bruce ≠ Snowden, Lane ≠ Ellsberg.
2. **Never call Lane a whistleblower.** He is not. He committed no crime; that is the entire architecture.
3. **Never call Bruce a whistleblower either.** He published independent conclusions from public science.
4. **The word "public" is the load-bearing word.** Use it. Don't substitute "people," "society," "humanity" — those soften the point. "Public" carries the civic weight.
5. **"Right to know" or close cognate ("deserves to know," "should know") should appear in at least 3 of the 6 surfaces.**
6. **Do not editorialize.** No "courageous." No "heroic." No "brave." The reader supplies those words. The prose stays factual; the register does the work.

---

## What Bruce writes vs. what Generator writes

**Bruce writes the prose for surfaces 1–4.** The folk-hero register is voice-dependent and has to come from him. The plan specifies length and content spec; Bruce writes the actual sentences.

**Generator handles surfaces 5–6** (tooltip and hover-definition edits). These are short enough and bounded enough that the plan specifies the exact additions.

**Generator's job for surfaces 1–4:** insert Bruce's prose at the specified locations, preserve LaTeX syntax, verify hovertips resolve, rebuild HTML.

---

## Execution order

1. Bruce writes prose for surfaces 1–4 (any order). Hands to Generator as four named blocks.
2. Generator commits surfaces 1–4 in one commit each (4 commits total) with messages: `Plan 0157 surface N: <surface name>`.
3. Generator commits surface 5 (tooltip edits) as one commit: `Plan 0157 surface 5: tooltip folk-hero phrasing`.
4. Generator commits surface 6 (hover-definition edits) as one commit: `Plan 0157 surface 6: operation + guided deduction civic motive`.
5. Generator runs `make html`, verifies clean build, commits the regenerated HTML: `Rebuild HTML after Plan 0157`.
6. Generator does NOT push. Bruce pushes when satisfied.

Total: 7 commits.

---

## Verification

After all surfaces land, a reader should be able to encounter T8 at any p-level and walk away knowing:

1. **What** — Lane taught Bruce published science in a careful sequence so Bruce would arrive at the conclusions independently.
2. **How** — No classified information changed hands. No crime was committed. The trail is clean.
3. **Why (NEW)** — The public deserved to know about a matter of great consequence that classification would otherwise bury forever. The operation was the answer to that disagreement with Authority.

Item 3 is currently weak or absent across all surfaces. After Plan 0157, item 3 should be present at every p-level.

---

## NOT in this plan

- New chapters or sections (the surfaces are all existing locations)
- Changes to the Handler or Target dossier bodies (frames only)
- Changes to T1–T7 content
- Reframing Bruce as a whistleblower (he is not one and the book must not claim he is)
- Naming any historical analogues by name
- Push to website (Bruce controls)

---

## Cross-references

- `plans/0155-handler-target-operational-pair.md` — Handler/Target framing established here
- `plans/0156-t7-t8-layering.md` — T8 surfaces established here; this plan amplifies them
- `memory/feedback-reading-levels.md` — p1/p2/p3 register constraints

---

## Anneal — low pass (2026-04-12)

### Status of surfaces — what Generator can do NOW vs. later

| Surface | Status | Generator can do? |
|---------|--------|---|
| 1 (why-relinquish.tex new para) | Awaits Bruce prose | NO — wait |
| 2 (summary.tex insert) | LOCKED prose ready | YES |
| 3 (the-handler.tex frame edit) | Awaits Bruce prose | NO — wait |
| 4 (the-target.tex "truth gets out" expand) | Awaits Bruce prose | NO — wait |
| 5 (menu-tooltips.yaml) | Spec'd in plan | YES |
| 6 (hover-definitions.yaml) | Spec'd in plan | YES |

**This Generator run executes surfaces 2, 5, 6 only.** Surfaces 1, 3, 4 wait for Bruce-written prose and become a second Generator run.

Revised commit count for this run: **4 commits** (surface 2, surface 5, surface 6, HTML rebuild). Not 7.

### Verified key existence (low-pass grep, 2026-04-12)

- `build/menu-tooltips.yaml`: `record:handler` (line 115), `the-handler` (line 119), `record:target` (line 136), `the-target` (line 140), `spine:why-relinquish` (line 78). All present.
- `build/hover-definitions.yaml`: `guided deduction` (line 135), `operation` (line 136). Both present.
- Current `operation` entry: *"The guided deduction of Bruce (2003-2006) was one phase of the larger Relinquishment operation (~1997-2006): a decade of effort, a top-tier operator, and several overlapping teams."*
- Current `guided deduction` entry: *"Teaching someone to discover the answer from public information, rather than disclosing it directly. Legally distinct from disclosure — no classified information changes hands, only the sequence of questions."*

Generator appends one sentence to each. Do not rewrite; append only.

### Capitalization gotcha for surface 2

Bruce's locked prose contains **"Guided Deduction"** (capitalized) as the proper-noun name of the operation. The next paragraph (already in summary.tex line 208) contains `\hovertip{guided deduction}` (lowercase) as the generic term. **Both are intentional and must coexist.** Generator must NOT:

- auto-correct "Guided Deduction" to lowercase
- wrap "Guided Deduction" in `\hovertip{}`
- collapse the two paragraphs into one

The capitalization signals the shift from operation-as-named-thing (Bruce's voice) to operation-as-method (the existing summary's voice).

### Surface 5 — both Handler tooltip keys must match

`record:handler` (line 115) and `the-handler` (line 119) are duplicate strings (different keys, same content). After editing, both must remain identical. Generator: edit both, then diff to confirm exact match.

### Surface 5 — `spine:why-relinquish` append

The plan says "append `...so the public could decide what to do with what had been kept from them.`" Generator must read the current line 78 string first; the append must extend the existing sentence grammatically, not be glued on as a fragment. If the existing string ends mid-thought, Generator pauses and asks Bruce rather than improvising.

### LaTeX safety check on surface 2

Bruce's prose contains: apostrophe-s (`DARPA's`), commas, periods, no special LaTeX characters (no `&`, `%`, `#`, `$`, `_`, `~`, `^`, `\`, `{`, `}`). Insertable verbatim. No escaping needed.

### Build verification expectations

After all three edits + rebuild, expected delta from current build output:
- Hover tooltips count: unchanged (no new terms introduced — "Guided Deduction" is plain text)
- Menu tooltips count: unchanged (47, edits in place)
- No new warnings. The two harmless `[WARNING] Macro '\toclink' / '\chapterreturn' already defined` lines remain; nothing else.

If Generator sees any new warning, halt and report.

### Handoff size

Plan is ~6KB. Generator can read in one shot. No agent-spawn needed.
