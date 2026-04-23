# Plan 0127 — The IRA Sniper Story (Time of Troubles) — NOT EXECUTED

## Status: CANCELLED

Decision (2026-03-26): Do not include. Northern Ireland retribution risk persists 40+ years. The identifying details (conflict, year, unit, incident type) ARE the story — cannot de-anonymize without destroying narrative value. Toboggan story (Plan 0126) bridges childhood→SAS without operational specificity. Story remains on Substack where already public but not amplified. Leaving the corners of the field.

## Context

Bruce published this story on Substack (Dec 22, 2022) as "Time of Troubles." It's a Healer story about the 1985 IRA sniper incident in Northern Ireland that led to Healer's SAS recruitment. Insert it into the book between the kangaroo story and the toboggan story.

## Source Material

Bruce's Substack post (postquantum.substack.com/p/time-of-troubles), reproduced here:

> The year is 1985. British soldiers patrol Northern Ireland during the Time of Troubles.
>
> The shot rang out after the bullet struck David's patrol partner in the torso. It was fired by a distant sniper. Five meters to the nearest cover seemed very far. He grabbed his fallen comrade and began dragging him to cover. They dodged as best they could. Another bullet whizzed by. The crack of the shot sounded 1.5 seconds later. The direction of the shooter was clear.
>
> They reached cover but were pinned down. Unless there was another shooter they were safe for now. David quickly assessed John's wound. The bullet had passed clean through John's upper right torso and may have nicked a lung. He slapped on bandages and John, still conscious, applied pressure to minimize blood loss. John would probably die without surgery.
>
> David turned his attention to the shooter. He knew roughly where the sniper was. The sniper knew exactly where he was and was presumably watching his location through a rifle scope. David carried an FN-FAL battle rifle with iron sight. David peeked out and spotted the shooter's likely hiding place. He saw a muzzle flash and another bullet narrowly missed his head. The sniper was about 550 meters away and had partial cover.
>
> David quickly shifted location, exposing himself to enemy fire, and took careful aim. He could just barely see the distant gunman. The target was smaller than the rifle's sight. He took the shot. It had the sweet feel of a hit but it was impossible to be certain. He dropped back behind cover.
>
> They decided to make a break for it. He picked up his wounded comrade and ran. They moved from cover to cover, expecting to die. No more shots came. They made it to the nearest help. David reported what had occurred. John was rushed to surgery. A patrol-in-force was sent to check out the sniper's hiding place.
>
> The sniper died instantly from David's single rifle bullet to the head. He was later identified as Provisional IRA. He was armed with a scoped .303 Lee-Enfield bolt action rifle.
>
> John survived.
>
> David fired one bullet. This unusually accurate long range kill, while under fire, drew the attention of the elite Special Air Service. He was invited to try out for the SAS. David passed SAS tryouts and served in the SAS for the next 15 years.

## Placement

File: `manuscript/track-2-testament/pos05-the-stories.tex`

Insert AFTER the kangaroo story disclaimer (line 72: "Regardless of whether the stories were true.") and BEFORE the toboggan story (which was just inserted by Plan 0126).

Timeline order in the chapter:
1. Kangaroo ranch (1978, age 12) — already in book
2. **IRA sniper (1985) — THIS INSERTION**
3. Toboggan (post-SAS selection, pre-officer) — Plan 0126, just inserted
4. The Method (2003-2006, what Bruce observed directly)

## Task

Adapt the Substack prose into the chapter. Constraints:

1. **Voice:** The Substack version is already Bruce's voice, third-person retelling of Healer's story. Preserve it closely. This is Bruce's published writing — do not rewrite his prose. Adapt minimally for book format.
2. **Frame:** The kangaroo story is framed as "The year is 1978." This story opens "The year is 1985." Same pattern. Good — keep it.
3. **Adaptation needed:**
   - Convert to LaTeX (em-dashes as `---`, proper quoting)
   - Add a scene-break rule before the story: `\vspace{1cm}\noindent\rule{0.5\textwidth}{0.5pt}\vspace{0.5cm}`
   - The Substack version uses "David" throughout. Keep it — matches the chapter's convention (the kangaroo story also uses "David").
   - The Substack has a Keefe epigraph. Do NOT include it — the chapter already has epigraphs.
   - Do NOT include the Substack subscription prompts or metadata.
4. **Minimal changes only.** Bruce wrote this. Preserve his sentences. Fix only formatting (LaTeX conventions) and remove Substack-specific framing. Do not add commentary, footnotes, or editorial notes.
5. **The line 72 disclaimer** ("I never verified any of David's stories...") currently sits between the kangaroo story and The Method. After this insertion, it should sit between the kangaroo story and the IRA story — it covers all the Healer stories. Move the disclaimer if needed so it appears ONCE, after all three stories (kangaroo, IRA, toboggan) and before The Method. Or verify it already works in position.
6. **Scene break between IRA and toboggan.** The toboggan story (Plan 0126) should already have its own scene-break rule. If not, add one.

## Disclaimer Placement Decision

The current disclaimer on line 72 says: "I never verified any of David's stories about his childhood."

This needs a minor edit — "childhood" is too narrow now that we have three stories spanning childhood through SAS career. Change to something like: "I never verified any of David's stories about his past." Minimal edit, one word.

## What NOT to do

- Do not rewrite Bruce's prose. Adapt formatting only.
- Do not add LaTeX comments, srcnotes, or voice markers.
- Do not add footnotes or citations.
- Do not editorialize.
- Do not touch any other part of the file beyond the disclaimer word change and the insertion.

## Acceptance Criteria

- IRA sniper story inserted between kangaroo and toboggan stories.
- Bruce's Substack prose preserved with only LaTeX formatting changes.
- Scene breaks between all three stories.
- Disclaimer covers all three stories (word "childhood" → "past" or similar).
- `make html` succeeds.
