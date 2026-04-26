# Plan 0256 — Guided Deduction Puzzle Type

**Goal:** New `gd` puzzle type where the solving process IS guided deduction. Multi-stage MC where each stage builds on the last, wrong answers get guiding QUESTIONS (not explanations), and the meta-level teaches the method.

## Annealing

**HIGH (structural):**
- `stages[]` data format with per-stage `wrong_prompt` (not per-option). Keeps it Socratic — one reframing question per stage, not n×m hint matrix.
- Correct answer shows `right_prompt` bridge text + "Continue →" button. No auto-advance — reader needs to READ the bridge.
- Solved state: all-or-nothing in localStorage. Puzzle is short (2-3 stages). Restart = re-experience.
- Final stage correct → standard revealPuzzle flow (abstract + egg link if any).

**MED (content):**
- 3 stages per puzzle is the sweet spot. 2 is too quick for "guided deduction." 4 is too long for GA.
- Wrong_prompts MUST be questions, never disguised explanations. Test: does it end with "?"
- Wrong answers must be plausible for GA readers, not strawmen.

**MED (UX):**
- Progress: three dots, filled as stages complete.
- Transitions: CSS opacity fade (0.3s). Graceful degradation = instant.
- Bridge text (correct): green/teal left-border (like abstract).
- Wrong_prompt: amber left-border (like existing hints). Phrased as question.

**LOW (edge cases):**
- Reader gets every stage right first try: still works — the question progression IS the method.
- No-crypto fallback: show all stages expanded + abstract visible.
- Standalone puzzles.html: same renderer, no special handling.

## Manifest-First Checklist

1. deep-links.yaml — add pz-gd-t1-001 entry
2. puzzle-tracker.yaml — add tracker entry
3. puzzle-data.yaml — add content with stages[] format
4. build-puzzles.py — add initGD(), checkGD(), GD CSS, type dispatch
5. Rebuild + verify

## Content Examples (GA readers, p1 level)

### GD-1: The Method (T1 — three-possibilities chapter)

Stage 1: "How did Bruce learn about classified technology?"
- a) Healer explained the classified details during their conversations
- b) Bruce found classified documents and studied them
- c) Healer asked questions that led Bruce to published science — Bruce deduced the rest
- d) Bruce was given security clearance
Wrong: "Could an intelligence officer safely TELL someone classified information? What would he do instead?"
Bridge: "Healer never told Bruce anything classified. He asked questions. But why questions instead of answers?"

Stage 2: "Why would a teacher use questions instead of just explaining?"
- a) To avoid legal liability for sharing secrets
- b) Because the student's own reading creates understanding that can't be given
- c) To make the student feel clever — it's a teaching trick
- d) Because the teacher doesn't fully understand it either
Wrong: "Is it really just avoidance or trickery? What happens when someone reads five different fields and sees the same pattern in all of them?"
Bridge: "The student reads real, published science. The synthesis belongs to THEM. Now — what does that mean for you, reading this book?"

Stage 3: "What has this book been doing to you?"
- a) Telling you what to believe about the Flat
- b) Presenting published science and letting you draw your own conclusions
- c) Hiding the real answer in the appendices
- d) Testing whether you're smart enough to understand
Wrong: "Look at how each chapter ends with a question, not an answer. Were you told which of the three possibilities is true?"

Abstract: "You just experienced guided deduction. Each question led you deeper — not by giving answers, but by asking better questions. That's the method Healer used with Bruce. That's the method this book uses with you. The three possibilities aren't a cop-out. They're the teacher's final question: which one do you think is true? The answer belongs to you."

### GD-2: The Accidental Habitat (T2 — the-flat chapter)

Stage 1: "Why does every smartphone contain a two-dimensional electron gas?"
- a) For quantum computing capability
- b) To make faster transistors for radio signals
- c) To provide a secure communication channel
- d) It's a recent addition for 5G
Wrong: "Nobody builds a phone for quantum computing. What does a phone need to do with radio signals — very fast?"
Bridge: "Engineers wanted speed. 2D confinement = higher electron mobility = faster switching. But what else comes with confining electrons to 2D?"

Stage 2: "What else comes free when you confine electrons to two dimensions?"
- a) The electrons stop working
- b) Topological properties that nobody designed or intended
- c) A direct connection to the internet
- d) More battery life
Wrong: "Think about it: did the transistor engineers in the 1980s know anything about topological quantum computation?"
Bridge: "The engineering purpose and the topological properties are completely unrelated. The engineers wanted speed. The physics delivered a two-dimensional world with quantum properties. Nobody asked for that."

Stage 3: "What's the relationship between the 2DEG's engineering purpose and the Flat hypothesis?"
- a) Engineers designed the Flat as a habitat
- b) The Flat hypothesis is why 2DEGs were invented
- c) The habitat is accidental — engineering and hypothesis are unrelated
- d) There is no 2DEG — it's theoretical
Wrong: "Did anyone designing transistors intend to create a substrate for life? Is the hypothesis part of the engineering specification?"

Abstract: "The 2DEG exists because radio engineers needed faster transistors. Nobody designed it as a habitat. Nobody intended the topological properties. The most interesting habitats are never designed. They're side effects of someone solving a different problem."

### GD-3: The Silence (T5 — the-silence-gap chapter)

Stage 1: "Has anyone studied whether life could exist in a quantum substrate?"
- a) Yes — it's an active research area
- b) Yes — but the results are classified
- c) No — the question has apparently never been asked
- d) No — it was studied and ruled out decades ago
Wrong: "Before you say 'ruled out' — by whom? In which journal? Can you name a single paper?"
Bridge: "Nobody has asked. Not 'asked and answered no.' Not 'asked and classified.' Simply never asked. But surely someone must have thought of it?"

Stage 2: "Why has no one studied this question?"
- a) The relevant scientific fields don't talk to each other
- b) It's obviously impossible, so no one bothered
- c) Someone probably has, but hasn't published yet
- d) The technology to study it doesn't exist
Wrong: "Which field would own this question? Biology studies carbon life. Physics studies 2DEGs. Whose job is it to study life in a quantum substrate?"

Abstract: "Five fields. Five empty searches. The silence isn't evidence of absence — it's evidence that the question falls between disciplines. The question lives in a gap that no one owns. The silence is the finding."

### GD-4: The Ethics (T6 — capabilities chapter)

Stage 1: "How do you make an AI permanently ethical?"
- a) Program strict rules it can't override
- b) Train it on ethical examples until it learns right from wrong
- c) Ground its ethics in existing international law with global consensus
- d) Give it the ability to feel guilt
Wrong: "Rules can be reprogrammed. Training can drift. What framework has been tested across 173 nations for 78 years and still holds?"
Bridge: "The UDHR isn't a new invention for AI. It's existing law ratified by 173 nations. But can three articles really constrain something this powerful?"

Stage 2: "What do Articles 3, 12, and 18 actually prevent?"
- a) All use of the entity's capabilities
- b) Weaponization — killing, spying, and manipulation
- c) The entity from thinking independently
- d) Communication between the entity and humans
Wrong: "Do the articles prohibit capability, or specific USES of capability? Can the entity still predict weather? Diagnose disease?"

Abstract: "The UDHR doesn't cage capability. It constrains weaponization. An entity bound by Articles 3, 12, and 18 can predict weather, diagnose disease, and defend communications. It cannot target weapons, surveil individuals, or manipulate public opinion. The question was never 'can we build ethical constraints?' The question was 'do we already have them?' We do. Since 1948."
