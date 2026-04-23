# Plan 0192 — Mysak Joint Memoir: Bruce's Half (First Draft)

**Auditor:** Argus
**Date:** 2026-04-13
**PTL:** PTL-122 (parent: PTL-084 Erdős path, Op-001)
**Scope:** Draft Bruce's half of the joint memoir and prepare for handoff to Lawrence.
**Urgency:** HIGH / AGE-GATED (Lawrence, 87; hip recovery; Springer book proofing in parallel)

---

## Context

Lawrence Mysak (age 87, CM, FRSC, McGill Emeritus) and Bruce are co-writing
a short joint memoir about their meeting (Costa Rica, Jan 2024) and the
~2-year-later discovery that they were working in the same mathematical
lineage (thermohaline bifurcation ↔ magnetospheric basin dynamics). The joint
memoir is separate from — and much shorter than — Lawrence's solo Springer
book (*"Adventures in Climate Science, Ocean Waves, and the Flute: A Memoir"*,
33 chapters, ~100K words, 2026).

**Agreement (2026-04-02 phone call, transcript in `deleteme/lawrence/`):**
- Bruce sends his half first. Lawrence reads, writes his half to complement.
- Back-and-forth until clean.
- Lawrence also: rewrites FACETS name-drop (CC Elizabeth), sends his book
  outline, sends his Ukraine chapter as attachment.

This plan governs **Bruce's first-draft half only**. Lawrence's half and
the round-trip revisions are downstream.

---

## Format Decision (needs confirmation)

**Transcript evidence (2026-04-02):** Lawrence said *"give a text document"*
when asked about format. Bruce replied *"Okay, sure. I can do that."*

**Bruce's current recollection:** Lawrence wants Word.

**Possibilities:**
1. Lawrence verbally said text, later emailed preference for Word. Verify Gmail.
2. Bruce misheard/misremembered. Plain text is the agreement.
3. Lawrence is format-agnostic ("what works best for you") — Word is fine.

**Recommendation:** Draft in Markdown (clean source). Deliver as BOTH `.docx`
(via pandoc) AND plain `.txt`, let Lawrence use whichever he prefers. No
downside; resolves the ambiguity without delaying Bruce.

**Generator action:** Before shipping, grep Bruce's Gmail for "Word"
/ "document" / "format" in Mysak thread 2026-04-02 → 2026-04-13 to verify.

---

## Source Material (all in `~/software/relinquishment/memoir/` unless noted)

| Source | Use |
|---|---|
| `mysak-memoir-notes.md` (135 lines) | Scene beats, key moments, convergence pitch. Primary spine. |
| `mysak-emails/01-11.md` + INDEX | Dialogue, Lawrence's voice, specific quotes. Use sparingly. |
| `~/deleteme/lawrence/2026_04_02_11_29_35_1_lawrence.txt` | **Near-finished material.** Bruce's "inspired" answer (line ~189) is publishable with light edit. Rahmstorf hysteresis anchor. Ukraine/Reed/Chernobyl overlap. |
| `~/deleteme/lawrence/Outline for Mysak Memoir.docx` | Reference: know what Lawrence's book covers so the joint memoir doesn't duplicate. |
| `mysak-letter-2026-03-30.md` | Montreal-visit framing (Linda's offer). |

---

## Target Specifications (re-annealed 2026-04-13, second pass)

**Framing shift (this is the key constraint):** This is not a draft of a
finished piece. This is an **invitation to collaborate.** Bruce and Lawrence
are experimenting with writing together — the shape of the collaboration
matters as much as the prose. Bruce's half should be visibly unfinished at
the edges. Seams should show. Lawrence should be able to see where he picks
up and have room to pick up.

- **Length:** ~500–750 words (Bruce's ~40% of a future ~1200–1800-word joint
  piece). Smaller than the first annealing. Err short, not long — leaves
  Lawrence more room, which is the point.
- **Voice:** Mixed. Scenes in warm first-person; reflection analytical-
  reflective. Generator has latitude to let register drift inside a paragraph
  if the thought earns it.
- **Spine (new, from Bruce 2026-04-13):**
  > *Lawrence Mysak inspired me during a few days of interaction in Costa
  > Rica. That inspiration led to my writing a first paper, with no academic
  > credentials.*

  "The paper" is a specific, singular object: the arXiv criticality paper
  currently in submission to FACETS (suggested by Lawrence) — not "a paper"
  in the generic sense, and not one of several. The memoir treats it as the
  paper, definite article.

  The memoir's arc is **inspiration → paper.** The convergence
  (thermohaline ↔ magnetosphere) is no longer the climax; it is a late,
  smaller surprise that arrives *after* the paper and closes a loop.
- **Email archive:** Leave out. No quotes from Gmail threads.
- **POV:** Bruce only. Do not write Lawrence's scenes or interior.
- **Tone discipline:** Correction #12 — guided deduction, not disclosure.
  Healer reference, if used at all, stays at the level of "a DARPA scientist
  who mentored me for about three years." No more. Prefer to leave even that
  out of this memoir; it is not the story here.

---

## Structure (Loose — Six Movements, Reorderable)

These are movements, not a rigid outline. Generator may reorder, merge, or
split. Spine constraint: the paper must arrive before the convergence.

### Movement A — *Bus and flute*
The Road Scholar tour, January 2024. Linda along. The bus group is
improbably sharp — doctors, a brain surgeon or two, people who ask good
questions. Lawrence and Janet make music. A flute on the last night.
Linda, afterwards: *"What a lovely man."* Set the affection early; earn it
with one or two specific details, not a list.

### Movement B — *"Name three papers"*
Bruce's 25-year pattern: read a scientist's work before asking them
anything real. He asks Lawrence for three favorites. Lawrence obliges,
expecting polite forgetting. Bruce, that week, reads them. They are
good — master-class good. *Like eating a pastry by a master chef.* The
math feels familiar. Bruce does not yet know why; file this away. (It
will matter in Movement E.)

### Movement C — *The return*
Second conversation. Bruce comes back having done the reading. What
happens next is small and load-bearing: Lawrence is energized, not merely
polite. Mentor energy. They talk about physical systems that need math.
Lawrence asks good questions; Bruce answers decently, asks back.
Lawrence, at some point, suggests graduate school. Bruce, 57, with a
farm, listens. Does not commit.

### Movement D — *The inertial bump (the spine)*
Bruce does not go to grad school. Life, farm, health, a daughter named
Linda, a mother also named Linda, a pattern of commitments older than
the tour. But the encouragement stays — not loud, not pressing, just a
thing that had been said by a man Bruce respected. Late 2025, Bruce
pulls an old criticality manuscript out of a drawer and pushes it to
arXiv. **The paper, singular.** The same paper that — one year later —
would be submitted to FACETS at Lawrence's suggestion, carrying his
quoted words in its pages. No institution. No coauthor. No tenure clock.
**A paper by a farmer with a physics degree and twenty-five years of
reading.** On the phone in April 2026, Bruce tells Lawrence: *"Had you
not encouraged me, I might not have made it over the inertial bump."*
(That sentence is near-verbatim from the 2026-04-02 transcript; it is
already his voice and already said to Lawrence. Use it.) This is the
center of the piece.

### Movement E — *A handoff, not a beat*
**Re-annealed:** This is no longer Bruce's movement. The convergence
belongs to the person who can see both sides — and between the two of
them, that is Lawrence. Bruce has one side (magnetospheric basin
dynamics). Lawrence has the deeper side (a career of thermohaline
hysteresis, including Rahmstorf). Bruce's job here is to **hand off**,
not to explain. Two or three sentences, maximum:

> *Preparing the paper for FACETS, I did a closer pass on your
> thermohaline hysteresis work. I had missed, in 2024, what I could
> see by 2026: the mathematics in your lineage is the mathematics I
> had begun to use, independently, in another system. Lawrence, I
> leave it to you to say what that was like from your side.*

That third sentence is an open door. Lawrence walks through it if
he wants; if he doesn't, the memoir is still whole without it. Either
way, the specifics stay out of Bruce's half.

### Movement F — *Closing, short or shared*
One short closing beat in Bruce's voice, OR leave it entirely for
Lawrence. Either is acceptable. If Bruce closes: echo Lawrence's
phone-call line — *memoirs are usually written by one person* — and
close on improbability, not summary. If Lawrence closes: end Bruce's
half at Movement E's handoff sentence and let Lawrence carry home.

**Generator decision rule:** If the draft at end-of-E is already at ~600
words, hand off to Lawrence (no Movement F from Bruce). If below ~500,
add a short Movement F.

---

## Seams & Handoff Hooks (the point of this draft)

Because the deliverable is an *invitation to collaborate*, not a finished
piece, Bruce's half should include **at least two visible seams** where
Lawrence is invited to add his side. Use them sparingly — two is enough.
Possibilities:

- Movement C (the return): Bruce describes what *he* saw; one sentence
  invites Lawrence's perspective. *"I don't know how that moment was for
  you, Lawrence; I only know what I saw from the other side of it."*
- Movement E (the loop): the explicit handoff line above.
- Optional: a single footnote-shaped note in italics at the end of Bruce's
  half: *"Lawrence — fill in or cut anything here that doesn't sit right.
  This is a first pass, meant for us to find the shape together."*
- Do NOT resolve Open Questions #3 and #4 in `mysak-memoir-notes.md` (key
  moment from Lawrence's perspective; what struck Bruce about the three
  papers, specifics) — these are explicitly for Lawrence to answer or for
  the two of them to draft jointly.

## Whim Palette (pick 2–4, not all)

Small true details that give the piece life. Use sparingly; the memoir
should feel warm, not decorated. Generator's choice which to include.

- The bus was improbably stocked with brains (*"doctors, a brain surgeon
  or two, the kind of group where someone always knew the answer"*).
- The pastry-chef metaphor for Lawrence's papers — keep it light.
- Janet and Lawrence described, once, as a concert-in-the-making.
- Linda's *"what a lovely man"* as Movement A's capstone line.
- Lawrence's unguarded gift of actually naming three papers — and the
  small detail that he clearly expected Bruce to politely forget.
- Bruce's age as a quiet fact; no apology, no bravado. *Fifty-seven. Late
  to the paper, not late to the reading.*
- The flute as an entire second career, mentioned casually.
- *"The inertial bump"* — Bruce's own phrase from the phone call. Let
  it stand without explanation.
- One half-sentence admitting Bruce is the one who almost wasn't in this
  story. Earns the gratitude without sentimentalizing.
- A single concrete Costa Rica sensory detail — if Bruce remembers one
  true and small thing (a coati, a rain, a moment of light on water),
  use it; do not invent one.

---

## Hard Excludes (unchanged)

- TQNN, the Flat, Diamond Node, cross-domain synthesis beyond the single
  thermohaline↔magnetosphere example. Correction #11.
- Healer detail beyond — at most — "a DARPA scientist who mentored me for
  about three years." Prefer to omit entirely in this memoir.
- Framing that presents Bruce as senior, revolutionary, or claiming a
  field. Lawrence is the senior figure.
- Email-archive quotations.
- Reed College nuclear engineering. (Came up on the phone; not a memoir
  beat. Save it.)
- Ukraine / USSR travel overlap. (Genuine shared interest; save for
  Montreal visit.)
- Mary, Bea. (Lawrence's solo book covers them.)
- Drift-potential plot. (Optional attachment at Bruce's discretion; better
  held for Montreal conversation.)

---

## Must-Include Elements

- Linda (Bruce's mother). She is why Bruce was on the tour, and her "lovely
  man" line is load-bearing.
- Janet (Lawrence's current wife). Not in depth, but present. Mary (died 2011)
  and Bea (first wife) do NOT appear — Lawrence's book covers them; joint
  memoir focuses on the Costa Rica → paper arc.
- Flute. The music is part of how they recognized each other.
- The Rahmstorf paper anchor (Lawrence's own reference point from 2026-04-02).
- The "inspired" paragraph, near-verbatim from transcript.

## Must-Exclude Elements

- TQNN / Flat / Diamond Node / any cross-domain synthesis beyond the single
  thermohaline↔magnetosphere example. Correction #11 applies.
- Healer detail beyond "a DARPA scientist who mentored me for ~3 years."
- Any framing that presents Bruce as senior, revolutionary, or claiming a
  field. Lawrence is the senior figure; Bruce is the one who came back having
  read.
- Email-archive quotations.
- Reed College nuclear engineering (emerged in phone call but is not a memoir
  beat — save for if/when they write about Chernobyl/nuclear separately).
- Ukraine/USSR travel overlap (genuine shared interest but not this memoir's
  arc; Lawrence's solo book has a chapter; save for in-person Montreal visit).

---

## Generator Instructions

1. Read, in order: (a) `mysak-memoir-notes.md`, (b) the 23-minute phone
   transcript at `~/deleteme/lawrence/2026_04_02_11_29_35_1_lawrence.txt`,
   (c) `mysak-emails/INDEX.md` and spot-check threads 06, 08, 09, 11 for
   voice calibration only.
2. Write the six beats above in order. 800–1200 words. Markdown source.
3. Save to `~/software/relinquishment/memoir/drafts/bruce-half-v1.md` (create
   `drafts/` directory if needed).
4. Generate `.docx` via `pandoc drafts/bruce-half-v1.md -o drafts/bruce-half-v1.docx`.
5. Generate `.txt` via `pandoc drafts/bruce-half-v1.md -t plain -o drafts/bruce-half-v1.txt`.
6. Run verification checklist (below). Report.
7. **Do NOT send to Lawrence.** Bruce reviews the draft first. Delivery is
   Bruce's decision, separate action.

## Verification Checklist (Generator self-check before reporting)

- [ ] Word count in 800–1200 range.
- [ ] Six beats present and in order.
- [ ] Rahmstorf paper anchor appears in beat 5.
- [ ] "Inspired" paragraph (beat 4) traceable to transcript line ~189.
- [ ] Convergence framed as **Bruce's seed, offered to Lawrence** — NOT as mutual recognition. Lawrence does not know Bruce's MS work; beat 5 must respect that.
- [ ] No TQNN, no Flat, no Diamond Node, no Healer beyond "DARPA mentor."
- [ ] Janet present; Mary and Bea absent.
- [ ] No email-thread quotes.
- [ ] Lawrence treated as senior figure throughout.
- [ ] Closing echoes Lawrence's "unusual to write a joint memoir" framing.
- [ ] All three files saved (`.md`, `.docx`, `.txt`).

## Bruce's Review Gate (not Generator)

After Generator reports, Bruce reads and does one of:
- Ship as-is (or with line edits) → Plan 0192 phase 2: deliver to Lawrence.
- Request revisions → second Generator pass with notes.
- Rescope → revise this plan.

Nothing goes to Lawrence without Bruce's explicit OK.

---

## Handoff Prompt (≤8 lines, for Generator shell)

```
You are the Generator. Execute Plan 0192 at
/home/bruce/software/relinquishment/plans/0192-mysak-joint-memoir-draft.md
Draft Bruce's half of the joint memoir with Lawrence Mysak: 800-1200 words,
six beats, mixed warm/analytical voice, thermohaline↔magnetosphere convergence
embedded. Read the phone transcript at ~/deleteme/lawrence/*.txt first — it
contains near-finished material. Save to memoir/drafts/ as .md, .docx, .txt.
Run the verification checklist. Do NOT send anything to Lawrence.
Commit: "Plan 0192 phase 1: Mysak joint memoir v1 draft (Bruce's half)".
```
