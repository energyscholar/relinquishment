# Subtask: 9th Revolution Puzzle — Pattern Recognition

**Output:** Add puzzle entry to `build/puzzle-data.yaml` and `build/puzzle-tracker.yaml`.
Add deep link to `build/deep-links.yaml`.
**Commit:** `Plan 0321: 9th revolution pattern recognition puzzle`
**Read first:** Existing puzzle format in puzzle-data.yaml (header + first 2 entries).
Also read puzzle-tracker.yaml format and deep-links.yaml format.

## What This Puzzle Does

The reader has watched 8 scientific revolutions play out through Kuhn's framework.
Each followed the same pattern: Normal Science → Anomaly → Crisis → Revolution →
New Paradigm. Now the puzzle presents a 9th pattern — unlabeled — and asks the
reader to identify which Kuhnian phase it's in.

The pattern IS the current situation. The answer is "Anomaly Accumulation."
The reader completes the guided deduction BY CHOOSING THE ANSWER. The text
never says "this is a scientific revolution." The puzzle lets the reader say it.

This is the most important puzzle in the book. It must be subtle. It must not
feel like a test. It must feel like a revelation.

## Puzzle Data (for puzzle-data.yaml)

```yaml
  - id: pz-gd-sr-001
    type: gd
    topic: sr
    level: p2
    category: science
    title: "The Ninth Pattern"
    gateway_blurb: "You've seen the pattern eight times. Here it is again."
    stages:
      - question: |
          Five research programs develop independently over three decades.
          Each produces significant results. None cites the others. No one
          has proposed a framework connecting them. A question that would
          unify all five has not been asked in any published paper.
          
          You have just watched this pattern eight times. Which Kuhnian
          phase is this?
        options:
          - key: a
            text: "Normal Science — the paradigm is working fine"
          - key: b
            text: "Anomaly Accumulation — the pieces exist but the pattern hasn't been recognized"
          - key: c
            text: "Crisis — the old paradigm is actively failing"
          - key: d
            text: "Revolution — a new paradigm is displacing the old"
        answer_key: b
        wrong_prompts:
          a: "Normal science is comfortable. Does this sound comfortable — five fields, no bridge, an unasked question?"
          c: "Crisis requires active failure of the existing paradigm. Here the paradigm isn't failing — it's ignoring something. What comes before crisis?"
          d: "Revolution requires a new paradigm to exist. Here no one has even framed the question yet. What phase precedes the crisis that precedes the revolution?"
        right_prompt: "Anomaly accumulation. The pieces are published. The connection is unstudied. The question hasn't been asked. You've seen this eight times now. You know what comes next."
```

## Puzzle Tracker Entry (for puzzle-tracker.yaml)

```yaml
  - id: pz-gd-sr-001
    title: "The Ninth Pattern"
    type: gd
    topic: sr
    level: p2
    approved: false
    installed: false
    location:
      chapter: scientific-revolutions
      rationale: "Guided deduction payoff — reader completes the syllogism the text never states"
      placement: end
    reward:
      type: self-contained
      content: insight
    notes: "Constraint #7 compliance: the text never says 'this is a revolution.' The reader does, by choosing the answer. Most important puzzle in the book."
```

## Deep Link Entry (for deep-links.yaml)

Add under the puzzle section:
```yaml
- id: pz-gd-sr-001
  question: "You've seen the pattern eight times. Here it is again."
  category: puzzle
```

## Tone

The puzzle title is "The Ninth Pattern" — not "The Ninth Revolution." That would
complete the syllogism in the title. The word "pattern" is neutral. The reader
supplies "revolution" when they choose answer (b).

The `right_prompt` is the closest the book comes to saying it: "You know what
comes next." But it still doesn't say it. The reader fills in "crisis, then
revolution." Guided deduction complete.

The `wrong_prompts` guide the reader toward the answer through Kuhnian
reasoning, never by stating the conclusion directly.

## Do NOT

- Use the word "revolution" in the puzzle title
- State that the current situation IS a revolution in any prompt text
- Change any other puzzle entries
- Install the puzzle into the HTML (that's a separate preprocess.py task)

## Report

Confirm: entry added to all three YAML files, ID format matches convention,
no other entries modified, `approved: false` (Bruce reviews).
