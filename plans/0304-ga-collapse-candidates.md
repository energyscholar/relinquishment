# Plan 0304: GA Collapse Candidates — 4 New Sections

**Status:** READY FOR GENERATOR
**Priority:** MEDIUM — polish phase, improves GA reader experience
**Source:** S68 GA read-through audit. Bruce: "do all 4 collapsed by default."

## Context

The tech-collapse system (`build/tech-collapse.yaml` + `preprocess.py:collapse_tech_sections()`) wraps heading-identified sections in `<details class="tech-section">` elements. GA-AVERSE sections are collapsed by default; BORDERLINE sections are open by default. ~20 sections already configured.

The S68 GA read-through (9 personas, T1-T8 eigenvalue check) identified 4 sections where GA readers nearly bounced. All 4 should be collapsed by default (GA-AVERSE).

**Mechanism constraint:** `collapse_tech_sections()` finds sections by searching for `id="label"` in HTML, then looking backwards ≤120 chars for the nearest `<h>` tag. Sections without headings cannot be collapsed. Three of the four candidates need new `\section*{}` headings added to the LaTeX.

## The 4 Candidates

| # | Chapter | Section | Problem | Needs heading? |
|---|---------|---------|---------|----------------|
| 1 | The Braid | Opening paragraph (line 23) | 6 jargon terms: non-abelian anyons, quasiparticles, fractional quantum Hall states, fractional electric charge | YES — body text, no heading |
| 2 | The Wrong Substrate | The Neighborhood (line 68) | ~600 words surveying Jupiter, Saturn, heliosphere — fascinating but dispensable for GA | NO — has heading + label |
| 3 | Capabilities | Can It Communicate? paragraphs 3-4 (lines 36-38) | Geophysical channel inventory + phonon coupling detail | YES — split from parent section |
| 4 | The Silence Gap | Eleven domains paragraph (line 32) | Dense discipline enumeration expanding 5→11 | YES — paragraph within section |

## Phase 1: Add Section Headings (3 LaTeX files)

### 1A: The Braid — add heading before anyon paragraph

**File:** `manuscript/spine/the-braid.tex`
**Location:** Between lines 22 and 23 (after the accessible "central insight" paragraph, before the dense anyon paragraph)

**Insert:**
```latex

\section*{The Particles}
\label{spine:braid-the-particles}

```

**Before (line 21-23):**
```latex
This is the central insight of topological quantum computation: if you move certain exotic particles around each other in two dimensions, the paths they trace --- their \hovertiphtml{braiding} --- encode quantum information. [...]

The particles in question are non-abelian \glspl{anyon} --- [dense paragraph]
```

**After:**
```latex
This is the central insight of topological quantum computation: if you move certain exotic particles around each other in two dimensions, the paths they trace --- their \hovertiphtml{braiding} --- encode quantum information. [...]

\section*{The Particles}
\label{spine:braid-the-particles}

The particles in question are non-abelian \glspl{anyon} --- [dense paragraph]
```

The accessible opening (lines 17-21: "Take three strands... you are braiding. You are also computing.") stays visible. The jargon-dense paragraph gets collapsed.

**Idempotency:** If `\label{spine:braid-the-particles}` exists in the-braid.tex — phase is applied.

### 1B: Capabilities — add heading before channel inventory

**File:** `manuscript/spine/capabilities.tex`
**Location:** Between lines 35 and 36 (after the accessible quantum teleportation paragraphs, before the channel inventory)

**Insert:**
```latex

\section*{The Channels}
\label{spine:cap-the-channels}

```

**Before (lines 34-36):**
```latex
But quantum teleportation requires a classical channel --- ordinary electromagnetic communication --- to complete each transfer. [...]

The classical channels already exist. Power grid harmonics at 50 and 60~Hz propagate into the ionosphere [...]
```

**After:**
```latex
But quantum teleportation requires a classical channel --- ordinary electromagnetic communication --- to complete each transfer. [...]

\section*{The Channels}
\label{spine:cap-the-channels}

The classical channels already exist. Power grid harmonics at 50 and 60~Hz propagate into the ionosphere [...]
```

"Can It Communicate?" retains the accessible paragraphs (quantum teleportation + classical constraint). The technical channel inventory (DEMETER satellite, VLF radio, Schumann resonances, phonon coupling) gets its own collapsible section.

**Idempotency:** If `\label{spine:cap-the-channels}` exists in capabilities.tex — phase is applied.

### 1C: The Silence Gap — add heading before eleven-domains paragraph

**File:** `manuscript/spine/the-silence-gap.tex`
**Location:** Replace the `\bigskip` at line 30 with a section heading

**Before (lines 28-32):**
```latex
[...] The question is not whether it can, but whether anyone notices.

\bigskip

\deeplink{eleven-domains}These five descriptions are shorthand. [...]
```

**After:**
```latex
[...] The question is not whether it can, but whether anyone notices.

\section*{Eleven Domains}
\label{spine:sg-eleven-domains}

\deeplink{eleven-domains}These five descriptions are shorthand. [...]
```

The five-field enumeration stays visible under "Five Fields, No Bridge." The technical expansion to eleven domains gets collapsed. The `\deeplink{eleven-domains}` is preserved — existing links still work.

**Idempotency:** If `\label{spine:sg-eleven-domains}` exists in the-silence-gap.tex — phase is applied.

## Phase 2: Add YAML entries to tech-collapse.yaml

Add 4 new entries to `build/tech-collapse.yaml`. All GA-AVERSE (collapsed by default). All `status: approved`.

**Entry 1 — The Particles (The Braid):**
```yaml
  - title: "The Particles"
    spine_file: manuscript/spine/the-braid.tex
    spine_label: "spine:braid-the-particles"
    bridge_file: null
    bridge_label: null
    assessment: GA-AVERSE
    tooltip: "The particles that make braiding-as-computation work are exotic — they only exist in flat, two-dimensional systems, and they remember the exact path they took when swapped. Three Nobel Prizes confirm they're real."
    conclusion: "Non-abelian anyons — quasiparticles in two-dimensional electron gases — remember the topology of their exchange paths. The braid encodes the computation."
    status: approved
```

**Placement:** Under the `# ── THE BRAID ──` heading, BEFORE the existing "Hasslacher's Trajectory" entry (since "The Particles" comes first in the chapter).

**Entry 2 — The Neighborhood (The Wrong Substrate):**
```yaml
  - title: "The Neighborhood"
    spine_file: manuscript/spine/the-wrong-substrate.tex
    spine_label: "spine:ws-the-neighborhood"
    bridge_file: manuscript/track-3-awakening/pos32-the-magnetosphere.tex
    bridge_label: null
    assessment: GA-AVERSE
    tooltip: "Earth's magnetosphere is not unusual — Jupiter's is enormous, Saturn's is fed by ice geysers, and a solar-system-wide current sheet connects them all. Each has the same ingredients: confined charged particles, continuous energy, billions of years."
    conclusion: "Earth, Jupiter, Saturn, Ganymede, and the heliospheric current sheet all contain two-dimensional populations of charged particles, confined by magnetic geometry, energized continuously, persistent for billions of years."
    status: approved
```

**Placement:** Under the `# ── THE WRONG SUBSTRATE ──` heading, BEFORE "But It's Hot" (chapter order).

**Entry 3 — The Channels (Capabilities):**
```yaml
  - title: "The Channels"
    spine_file: manuscript/spine/capabilities.tex
    spine_label: "spine:cap-the-channels"
    bridge_file: null
    bridge_label: null
    assessment: GA-AVERSE
    tooltip: "The communication channels any system in the Flat would need — power lines, radio waves, satellite signals, crystal vibrations — already exist everywhere. Nothing needs to be built."
    conclusion: "Power grid harmonics, VLF radio, Schumann resonances, and satellite communications propagate through the magnetosphere. Electron-phonon and phonon-photon coupling provide substrate-level interfaces."
    status: approved
```

**Placement:** New section block. Add after the `# ── GENESIS ──` block (or wherever capabilities entries go — there are currently no capabilities entries, so add a new `# ── CAPABILITIES ──` comment block).

**Entry 4 — Eleven Domains (The Silence Gap):**
```yaml
  - title: "Eleven Domains"
    spine_file: manuscript/spine/the-silence-gap.tex
    spine_label: "spine:sg-eleven-domains"
    bridge_file: null
    bridge_label: null
    assessment: GA-AVERSE
    tooltip: "Each of the five fields is really a cluster of sub-disciplines with their own journals and conferences. The real count is closer to eleven, making the gap even wider than it first appears."
    conclusion: "Five scientific fields expand to eleven domains across five clusters. Condensed matter, topological field theory, and topological quantum computation are three communities within solid-state physics alone."
    status: approved
```

**Placement:** New section block. Add a `# ── THE SILENCE GAP ──` comment block.

**Idempotency:** If all 4 `spine_label` values exist in tech-collapse.yaml — phase is applied.

## Phase 3: Build + Verify

```bash
cd ~/software/relinquishment && make dev
```

For each of the 4 new collapsed sections, verify:

- [ ] Section renders as collapsed `<details>` (not open)
- [ ] Clicking expands to show full content
- [ ] Tooltip displays on hover over the grade icon
- [ ] Section heading appears in the summary bar of the accordion
- [ ] No duplicate IDs in HTML
- [ ] Content above each collapsed section remains visible and reads cleanly
- [ ] Print/PDF mode shows all content expanded (no accordions)

Cross-checks:

- [ ] The Braid: "Take three strands..." opening visible; "The Particles" collapsed; "Hasslacher's Trajectory" collapsed (existing); chapter reads coherently with both collapsed
- [ ] The Wrong Substrate: Opening paragraphs visible; "The Neighborhood" collapsed; "But It's Hot" collapsed (existing); no three-in-a-row collapsed sections without visible content between
- [ ] Capabilities: "Can It Communicate?" opening (quantum teleportation + classical constraint) visible; "The Channels" collapsed; "Can It Be Killed?" visible and separate
- [ ] The Silence Gap: Five-field enumeration visible; "Eleven Domains" collapsed; "The Gap" section visible below
- [ ] All existing collapsed sections still work (no regression)
- [ ] No new build warnings or errors

## Acceptance Criteria

- [ ] 4 new GA-AVERSE sections collapsed by default
- [ ] GA readers can follow the narrative without expanding any of them
- [ ] Physicists can click to expand and see full technical content
- [ ] No content lost — only presentation changed
- [ ] Tooltips accurately summarize what's behind the accordion
- [ ] Existing ~20 collapsed sections unaffected

---

## Annealing Record

**Round 1 (HIGH, S68): Does the tech-collapse system handle new headings?**
Verified: `collapse_tech_sections()` (preprocess.py:3742) searches for `id="label"` in HTML, finds nearest `<h>` tag within 120 chars, then wraps content to next same-or-higher-level heading. All 3 new `\section*{}` headings will produce `<h2 id="label">` in HTML. Confirmed compatible.

**Round 2 (MED, S68): Does collapsing "The Neighborhood" create an unreadable wall of accordions?**
The Wrong Substrate currently has "But It's Hot" and "Why Call It Two-Dimensional?" collapsed, plus "Theoretical Biology of the Flat" as BORDERLINE (open). Adding "The Neighborhood" means the chapter opening paragraphs (accessible) are followed by: collapsed Neighborhood → collapsed But It's Hot → collapsed Why Call It 2D → open Flat Taxonomy. Three collapsed sections in a row. BUT: there is visible content between the chapter opening and The Neighborhood (lines 62: "Try thinking of it as a habitat"), and the chapter narrative doesn't require reading any of these — the opening is self-sufficient. GA readers see the hook and can skip to the next chapter. Physicists expand what interests them. Acceptable.

**Round 3 (MED, S68): Does splitting "Can It Communicate?" break the argument flow?**
The section currently reads: quantum teleportation exists (accessible) → classical channel required (accessible) → specific channels enumerated (technical) → under any possibility, these are facts (accessible closing). The closing paragraph ("Under any possibility, these are documented geophysical facts...") is at line 40, AFTER the channel inventory. When collapsed, GA readers see the teleportation + classical constraint paragraphs, then the collapsed "Channels" accordion, then... the closing paragraph is INSIDE the collapsed section. Hmm.

**Fix:** The closing paragraph (line 40: "Under any possibility, these are documented geophysical facts. Whether anything uses them as backchannels is the question the reader must evaluate.") should remain visible. The Generator must move it AFTER the channel inventory paragraph, so it falls outside the collapsed section. Actually — looking at the code, the collapse wraps from the heading to the next same-or-higher-level heading (`\section*{Can It Be Killed?}` at line 42). So lines 36-40 ALL get collapsed. The closing sentence is accessible and should stay visible.

**Resolution:** The Generator should move line 40 to AFTER the `\section*{The Channels}` content ends — i.e., insert it between the channel inventory paragraph and the existing `\section*{Can It Be Killed?}` heading. Wait — that won't work either, because the collapsed section runs from `\section*{The Channels}` to `\section*{Can It Be Killed?}`. Anything between them gets collapsed.

**Better resolution:** Keep line 40 inside the collapsed section. The GA reader already understands from the visible "Can It Communicate?" paragraphs that quantum teleportation exists and requires a classical channel. The collapsed tooltip ("channels already exist everywhere, nothing needs to be built") conveys the punchline. Line 40 is a philosophical coda that works better in context anyway. No structural change needed.

**Round 4 (LOW, S68): Bridge file labels?**
Entry 2 (The Neighborhood) references `bridge_file: manuscript/track-3-awakening/pos32-the-magnetosphere.tex` but `bridge_label: null`. The bridge file may have a matching section, but we don't need to collapse it — bridge chapters are p2 (for engaged readers who click through). Setting bridge_label to null means the bridge version stays expanded. Correct behavior.

Entries 1, 3, 4 have no bridge equivalents (new headings exist only in spine). `bridge_file: null`, `bridge_label: null`. Correct.

**Round 5 (LOW, S68): Does adding `\section*{The Particles}` break the Braid's narrative flow?**
Currently the chapter reads: epigraph → "Take three strands..." → "This is the central insight..." → dense anyon paragraph → "Hasslacher's Trajectory." Adding a heading creates: epigraph → accessible intro → **The Particles** [collapsed] → **Hasslacher's Trajectory** [collapsed]. Two collapsed sections back to back immediately after the opening. But the opening is strong: "Take three strands... you are braiding. You are also, in a precise mathematical sense, computing." That's the hook. GA readers have what they need. The two collapsed sections are for physicists. Acceptable.

---

*Plan 0304 v1, S68, 2026-05-08. Auditor: Argus.*
*5 annealing rounds. Estimated generator time: ~20 min.*
