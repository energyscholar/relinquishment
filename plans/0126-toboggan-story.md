# Plan 0126 — The Toboggan Story

## Context

Bruce provided a complete Healer story from memory. Insert it into `manuscript/track-2-testament/pos05-the-stories.tex`.

## Source Material

Bruce's verbatim account (recorded 2026-03-26):

> So Healer told this story at Alpha Farm, after we'd been there a few weeks. He talked about how he was working the SAS sorting training, where most recruits got cut. He was working the Mountain Climbing part. I think he was not yet an officer in SAS but not sure. (Was promoted in the field during Gulf War 1 during Operations Desert Shield.) So a recruit had died on the mountain. Healer and another SAS soldier were sent to recover the body. They hiked up the mountain and found him way up high altitude. The corpse was a big guy, and he'd frozen solid by the time they got to him. They had brought an XXL body bag or two so they were able to wrap him up in the body bag. That left them looking at each other, looking at this large bodybag holding a corpse they needed to bring home, and down this steep snowy mountain. They resented the guy for dying and forcing them to climb up and recover his corpse. So, how do they get the body down. "You didn't!" said one of the listeners. "We sure did" said Healer. "We rode it like a toboggan down the mountain and got home in record time."

## Placement

File: `manuscript/track-2-testament/pos05-the-stories.tex`

Insert AFTER line 72 ("Regardless of whether the stories were true.") and BEFORE line 74 (`\section*{The Method}`).

Timeline logic: kangaroo story = childhood (~1978). Toboggan = young-adult SAS, pre-officer (early-mid 1980s). The Method = what Bruce observed directly (2003-2006). Chronological order preserved.

## Task

Write the toboggan story as a new section in Bruce's first-person voice, matching the chapter's existing register. Constraints:

1. **Voice:** First person, Bruce narrating. Match the tone of the surrounding text — personal, direct, no literary flourish. Bruce is recounting what Healer told the room.
2. **Frame:** Healer told this at Alpha Farm, after they'd been there a few weeks. The audience was the farm commune. Include the listener's reaction ("You didn't!") and Healer's deadpan punchline.
3. **Details to include:** SAS selection training, mountain climbing portion, recruit died, frozen solid, big guy, XXL body bag, steep snowy mountain, two soldiers looking at each other with a logistics problem, the toboggan solution, "got home in record time."
4. **Details Bruce is uncertain about:** Whether Healer was an officer yet at this point. He was promoted in the field during Gulf War 1 (Desert Shield). Note the uncertainty naturally, as Bruce does elsewhere (see line 70: "Officer Kevin (or Ken --- the name is uncertain after decades)").
5. **Audience reaction:** The hippies went green. This is the punchline of the frame — SAS dark humor delivered deadpan to pacifist organic farmers. Don't explain why it's funny. Let the reader see it.
6. **Length:** 150-250 words. This is a short anecdote, not a set piece like the kangaroo story. It should feel like a quick story told between longer sections.
7. **Closing:** Brief transition connecting to the disclaimer pattern — Bruce couldn't verify this either, but like the childhood stories, it arrived complete. Do NOT repeat the full disclaimer from line 72; a single sentence referencing it is enough. Or omit if the existing line 72 disclaimer naturally covers both stories.
8. **No `\section*` heading.** This is a continuation of the same narrative block as the kangaroo story, separated by a `\vspace` rule like the scene breaks in pos02 (see lines 57, 77, 93 of pos02 for the pattern: `\vspace{1cm}\noindent\rule{0.5\textwidth}{0.5pt}\vspace{0.5cm}`).

## What NOT to do

- Do not add LaTeX comments, srcnotes, or voice markers.
- Do not editorialize about what the story reveals about Healer's character. The reader gets it.
- Do not touch any other part of the file.
- Do not add footnotes or citations.

## Acceptance Criteria

- Story reads naturally as Bruce's voice, indistinguishable from surrounding text.
- Timeline: clearly pre-officer SAS career.
- Hippie audience reaction visible without being explained.
- 150-250 words of new content.
- Existing disclaimer on line 72 still works as a cover for both stories (if not, adjust minimally).
