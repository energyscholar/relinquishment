# Plan 0096: Execution — Annealed Prompts & Process

**Status:** COMPLETE (verified S63 audit)
**Auditor:** Argus, Session 43
**References:** Plans 0088-0095 (detailed specs), staging/interview-content-prepared.md (S43 puzzle pieces)

---

## Annealing Record

Each phase was perturbed with 4-5 large variations and red-teamed for failure modes. Key changes from initial design:

**Phase 1:** Space chapter moved to Wave 1 (earlier) — it must extract habitat fragments before Monopoly merge. First Light + Demo combined into single Generator task (both Part II, adjacent, total output ~4K words). Hobbit stays in Wave 1 for quick feedback.

**Phase 2:** Dossier relocation expanded to include footnotes at first character mentions. Interlude trim tightened from ~800w to ~500w. Build test after EVERY file move, not just at end. Endnote LaTeX infrastructure verified/added.

**Phase 3:** Expanded from 3 to 5 verification tasks. Added: voice sweep, citation sweep, join quality sweep. Gen contingency: if her feedback hasn't arrived, tag and proceed; structural changes from Gen go into new plan (0097+), not retrofit.

---

## Investigative Threads (20% — run before/during Phase 1)

These de-risk the hardest operations. Research agents, not Generators.

**Thread A: Twenty Years skeleton.** Read pos29, pos31, pos34, pos23. Map chronological events onto timeline 2006-2026. Identify emotional thread from The Weight that should be woven throughout. Output: skeleton document at staging/twenty-years-skeleton.md.

**Thread B: Space chapter research.** Web search: Jupiter vs Earth magnetosphere quantitative comparison (field strength, volume, plasma density, energy budget). Ganymede magnetosphere. Heliospheric current sheet structure. Has anyone searched for emergent patterns in magnetospheric plasma? Output: staging/space-chapter-research.md.

**Thread C: Build system map.** Read main.tex and all \include/\input commands. Map current chapter ordering. Document exactly what must change for three-part structure. Identify endnote package status. Output: staging/build-system-map.md.

**Thread D: Citation verification.** Web search for 15 DOIs/URLs needed for Timeline (Plan 0095). Verify each link is live. Output: staging/timeline-citations.md.

---

## Phase 1: Write

### Lint Sweep (before any changes)

```
You are the Generator. Run a LaTeX lint sweep on the manuscript at
~/software/relinquishment/manuscript/. Check: compilation warnings,
orphaned \label/\ref, duplicate labels, remaining \aidraft markers,
QQQ/TODO markers. Output report to staging/lint-baseline.md.
```

### Wave 1 (parallel — no dependencies between tasks)

**1a. Merge: First Light + Demo (combined task)**
```
You are the Generator. Read plans/0092-part2-investigation.md.
Execute Merge 4 (First Light+Thermal Ladder+Capability → "First Light")
AND Merge 3 (Experiment+Threshold → "The Demo"). Source files in
manuscript/track-1-confession/ and manuscript/bridge/. Maintain
Track 1 voice for First Light, Bridge voice for Demo. Verify
Question Anchor + Concrete→Abstract→Stakes rhythm in both.
```

**1b. Merge: The Network**
```
You are the Generator. Read plans/0092-part2-investigation.md.
Execute Merge 5 (Network+Convergence Revisited → "The Network").
Source files: manuscript/track-1-confession/pos20-the-network.tex and
pos21-convergence-revisited.tex. Track 1 voice. This is the capstone
of the science sequence — the synthesis must feel earned, not stitched.
```

**1c. Write: The Hobbit in the Mirror**
```
You are the Generator. Read plans/0089-hobbit-mirror-early.md and
manuscript/convergence/pos36-steelman-a.tex (section "The Hobbit in
the Mirror" starting line 21). Write ~250-300 words, Bruce's DIRECT
talking voice — rougher than Steel-Man A, not literary. Place as
chapter 2 of Part I. Repetition with Steel-Man A is deliberate.
```

**1d. Write: The Wrong Substrate (Space chapter)**
```
You are the Generator. Read plans/0088-habitat-chapter.md,
staging/space-chapter-research.md (from Thread B),
staging/interview-content-prepared.md (Healer quote section), and
manuscript/track-3-awakening/pos32-the-magnetosphere.tex.
Write ~2,500 words replacing The Magnetosphere. Three acts:
Earth's magnetosphere as habitat → solar system survey → "What
might live here?" Nature documentary tone. Extract habitat
fragments from pos27-extension.tex and pos25-ethical-framework.tex,
marking what you extracted for the Monopoly merge. Use Healer's
magnetosphere confirmation (ancient pattern found, left in place)
as the bridge to Act 3. Do NOT mention Custodian by name. End
with the question, not the answer.
```

### Wave 2 (after Wave 1 starts; Twenty Years uses Thread A output)

**2a. Merge: The Stories + Patrick Ball + "The Method"**
```
You are the Generator. Read plans/0091-part1-story.md and
staging/interview-content-prepared.md (V6: "The Method" section).
Execute Merge 1 (Stories+Patrick Ball → "The Stories"). Source:
manuscript/track-2-testament/pos05-the-stories.tex and
pos19-patrick-ball.tex. Track 2 voice (Bruce, first person).
Patrick Ball/cDc/Srebrenica integrates as one story. ALSO add
~200-300 words naming and describing the Dunning-Kruger
pedagogical pattern ("The Method") — how David taught through
provocation not lecture. This is the ENGINE of the mentorship
and appears nowhere in the book as a named pattern.
```

**2b. Merge: Why Relinquish?**
```
You are the Generator. Read plans/0091-part1-story.md. Execute
Merge 2 (The Secret+Why Give It Up → "Why Relinquish?"). Source:
manuscript/bridge/pos06-the-secret.tex and manuscript/track-1-confession/
pos22-why-give-it-up.tex. Unified voice: expository with narrative
anchoring. The question (pos06) becomes the opening; the argument
(pos22) becomes the answer.
```

**2c. Merge: Twenty Years**
```
You are the Generator. Read plans/0093-part3-interpretation.md,
staging/twenty-years-skeleton.md (from Thread A), and
staging/interview-content-prepared.md (V10 + V11 sections).
Execute Merge 7 (Silence+Wolfram+Research+Weight → "Twenty Years").
Sources: pos29-the-silence.tex, pos31-wolfram.tex,
pos34-the-research.tex, pos23-the-weight.tex. Track 2 voice.
STRICTLY chronological: 2006→2008→2011→2012→2025. ALSO integrate
V10 (Research Years gap: Bannon, interlibrary loans, 2-3 hrs/day
research) and V11 (Mark at Oregon Country Fair, Joy article
discovery, electric shock, 50-mile bike ride). The Weight's
emotional content is WOVEN throughout, not appended. Wolfram
meeting + Joy article are the two structural turning points.
Target ~6,000 words.
```

**2d. Timeline Improvements**
```
You are the Generator. Read plans/0095-timeline-improvements.md
and staging/timeline-citations.md (from Thread D). Source:
manuscript/appendix/timeline.tex. Add 11 new entries, add
citations/links, add era subheadings, add chapter cross-references
(use consolidated chapter names), tighten wordy entries, apply
S43 corrections. Target ~5,000-5,500 words.
```

### Enrichment Tasks (parallel with Wave 2, small independent tasks)

**E1. Alpha Farm: V3 vulnerability insert**
```
You are the Generator. Read staging/interview-content-prepared.md
(V3 section) and manuscript/track-2-testament/pos02-alpha-farm.tex.
Insert ~150 words of Bruce's psychological context near the
opening: nervous breakdown, bipolar wife, caregiver burnout,
retired at 35, "spirit was broken." Track 2 voice. Shows WHY
he was receptive to mentorship. Do NOT add more than ~150 words.
```

**E2. The Departure: V9 spatial grounding**
```
You are the Generator. Read staging/interview-content-prepared.md
(V9 section) and manuscript/track-2-testament/pos07-the-departure.tex.
Enrich the "We already did it, mate" scene with ~200 words of
spatial/emotional grounding: 15th and Grant living room, mid-morning,
girlfriend away, kids at school. Track 2 voice. Add the 8-year
deferred understanding arc if not already present.
```

### Wave 3 (after Space chapter completes — Monopoly needs post-donation files)

**3a. Merge: The Monopoly**
```
You are the Generator. Read plans/0093-part3-interpretation.md.
Execute Merge 6 (Extension+Unipolar Condition → "The Monopoly").
Source: POST-DONATION versions of pos27-extension.tex (after Space
chapter extracted habitat fragments) and pos30-unipolar-condition.tex.
Track 3 voice. Structure: HOW it spread → WHY it's stable → WHAT
that means. Forest canopy metaphor is the anchor image.
```

**3b. Merge: The Question**
```
You are the Generator. Read plans/0093-part3-interpretation.md.
Execute Merge 8 (Digital Doppelgänger+The Question+Evidence Interlude
→ "The Question"). Source: pos33-digital-doppelganger.tex,
pos35-the-question.tex, interlude/evidence-interlude.tex. Mixed
voice (Track 2 for Doppelgänger, convergence for Question). This
is the penultimate chapter — must sustain attention before Steel-Man A.
```

---

## Phase 2: Reorganize

**Single combined prompt for most tasks:**
```
You are the Generator. Read plans/0094-peripheral.md and
staging/build-system-map.md (from Thread C). Execute ALL of:
(1) Relocate dossier-interlude.tex → appendix/dossier.tex, add
"See Appendix: Dossiers" footnotes at first character mentions
in narrative chapters. (2) Relocate pos34b-the-engine.tex →
99-back/afterword.tex. (3) Trim three-possibilities-interlude.tex
from 2,136w to ~500w — brief A/B/C checkpoint only. (4) Merge
authors-note.tex + preface.tex + not-claimed.tex → single front
matter piece (~400w). (5) Move summary.tex to appendix. (6) Delete
appendix/rlhf-bias.tex. (7) Update main.tex build order for
three-part structure with \part{} commands. (8) Verify endnote
package (\usepackage{endnotes}) is configured. Build test after
each structural change.
```

---

## Phase 3: Verify

**5 verification sweeps, one combined prompt:**
```
You are the Generator (in verification mode). Read plans/0090-master-restructure.md.
Execute these 5 sweeps across the restructured manuscript:

(1) LINT SWEEP: Repeat baseline lint check. Compare to
staging/lint-baseline.md. All new issues must be zero.

(2) BLOCKER-DEBLOCKER INTEGRITY: Verify in the new three-part
ordering: Braid before Genesis, Code War before Departure,
Genesis before Instantiation, Threshold before Network,
Question Anchor + C→A→S rhythm present in merged chapters.

(3) VOICE SWEEP: Track 2 chapters use first person ("I").
Bridge chapters have NO first person. Track 1 uses reconstructed
third person. Track 3 uses mixed. Flag any voice violations
in merged chapters. Pay special attention to Why Relinquish?
(merged Bridge+Track 1) and The Question (merged Track 2+Convergence).

(4) CITATION SWEEP: Check for duplicate citations across merged
chapters (same source cited in both halves). Check for needed
citations at new connections. Check Timeline links are live.
Remove citations to content that was cut (RLHF bias).

(5) JOIN QUALITY SWEEP: Read every merged chapter. At each point
where content from different source chapters meets, check:
smooth transition? voice shift? redundant material? abrupt topic
change? Each seam should be invisible.

Output: staging/phase3-verification-report.md with pass/fail
for each sweep + specific issues found.
```

**Metrics verification (separate, quick):**
```
Run word counts on all chapter files. Verify: ~25 narrative
chapters, ~64K narrative words, ~7,500 front matter words,
total ~90K. Compare to Plan 0090 targets. Report discrepancies.
```

**Gen feedback incorporation:**
```
If Gen has responded to issue #5 with structural feedback by this
point, create Plan 0097 for any adjustments. If not, tag current
state as v3.0-post-restructure and note that Gen's review is
pending. Do NOT retrofit Phase 2 work — forward-only changes.
```

---

## Join Protocol (How to Merge Cleanly)

Every merge Generator must follow this process:

1. **Read both sources completely** before writing anything
2. **List key content** from each source (bullet points, not prose)
3. **Identify overlaps** — both sources may say similar things differently. Pick the stronger version.
4. **Design transitions** — where source A ends and source B begins, write a bridging sentence that makes the shift feel inevitable
5. **Match voice to target track** — if sources are different tracks, the merged chapter must be ONE voice
6. **Apply Gen's constraints** — Question Anchor opening, Concrete→Abstract→Stakes rhythm
7. **Read the merged result** — does it flow? Any bumps? Any content lost from the source checklist?

---

## Voice Rules (What Goes Where)

| Voice | Track | Pronoun | Where Used |
|-------|-------|---------|------------|
| Bruce's testament | Track 2 | "I" | Alpha Farm, Stories, Departure, Twenty Years, Hobbit |
| Reconstructed history | Track 1 | "they"/"the team" | First Light, Walk-Out, Network, Why Relinquish? |
| Bridge/pedagogy | Bridge | no pronoun | Code War, Factoring Game, Braid, Demo, Genesis, Growing a Mind, Dual-Use |
| Custodian/speculation | Track 3 | "she"/"it" | Instantiation, Ethical Framework, Monopoly, Wrong Substrate |
| Convergence | Mixed | varies | Surrender, Question, Steel-Man A |

**Danger zones in merges:**
- **Why Relinquish?** (Bridge + Track 1) → Target: expository voice. No "I."
- **The Question** (Track 2 + Convergence + interlude) → Target: convergence voice. "I" only in Doppelgänger section.
- **Twenty Years** (all Track 2) → Safe. All first person.

---

## Dependency Map (verified)

```
Thread A (Twenty Years skeleton) ──→ Wave 2c (Twenty Years merge)
Thread B (Space research) ──────→ Wave 1d (Space chapter)
Thread C (Build system map) ────→ Phase 2 (Reorganize)
Thread D (Citation verification) → Wave 2d (Timeline)

Wave 1d (Space chapter) ────────→ Wave 3a (Monopoly — needs post-donation files)

All Phase 1 ──→ Phase 2 ──→ Phase 3

No circular dependencies. ✓
No orphaned tasks. ✓
```

---

## Gen Compatibility Check

| Gen's Contribution | How Plans Support It |
|-------------------|---------------------|
| Three-part structure (Story/Investigation/Interpretation) | Adopted as organizing principle (Plans 0091-0093) |
| Question Anchor (open with puzzle) | Specified as constraint in every merge prompt |
| Concrete → Abstract → Stakes | Specified as constraint in every merge prompt |
| Endnotes for technical density | Phase 2 verifies/adds \usepackage{endnotes} |
| Footnotes/endnotes separation | Preserved as design constraint throughout |
| Joy close-reading points | Phase 3 verifies Joy material lands in correct chapters. Gen reviewing on issue #9. If her assessment changes point count, Phase 3 incorporates. |
| UQs (from PTL-062) | Pending Gen's review. No conflict with restructure. |

---

## Risk Register

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Twenty Years merge too unwieldy | Medium | High | Thread A skeleton + fallback split option |
| Space chapter lacks quantitative rigor | Low | Medium | Thread B research pre-gathered |
| Build system breaks after restructure | Medium | Medium | Thread C map + test after every move |
| Gen feedback requires re-work | Low | High | Forward-only changes (Plan 0097+) |
| Voice contamination in merged chapters | Medium | Medium | Phase 3 voice sweep + voice rules table |
| Seams visible in merged chapters | Medium | Medium | Join protocol + Phase 3 join quality sweep |
| Citations duplicated or orphaned | Low | Low | Phase 3 citation sweep |
| Hobbit chapter too literary (matches Steel-Man A) | Low | Medium | Prompt specifies "rougher, talking voice" |
