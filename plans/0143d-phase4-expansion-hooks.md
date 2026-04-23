# Plan 0143d: Phase 4 — B/C Expansion Hooks + Record Wiring

**Status:** Ready for Generator
**Parent:** Plan 0143 (Z-Restructure Metaplan)
**Role:** Generator executes.

---

## Overview

Write inline B/C expansion hooks in spine chapters that link to The Record. Each hook is 1-3 paragraphs — a teaser that gives the reader enough B/C flavor to be curious, with a "Read the full story →" link to the relevant Record chapter.

The expansion hooks use the `.bc-expansion` CSS already built in Phase 1. They are `<details>` elements that tap to reveal on phone.

---

## Implementation Method

Expansion hooks must survive the LaTeX → pandoc → HTML pipeline. Since pandoc doesn't support `<details>` natively, we use a LaTeX marker that preprocess.py converts.

### LaTeX Convention

In spine .tex files, add expansion hooks using this pattern:

```latex
% BC-EXPANSION: record:alpha-farm
\begin{quote}
\textbf{BCSTART:record:alpha-farm} According to this story, a physicist arrived at...

Read the full story $\rightarrow$
\textbf{BCEND}
\end{quote}
```

### preprocess.py Conversion

Add to `fix_html_toc()` (after the Guardian interlude processing):

```python
# B/C expansion hooks: convert BCSTART/BCEND markers to <details>
bc_pattern = re.compile(
    r'<blockquote>\s*<p>\s*<strong>BCSTART:([^<]+)</strong>\s*(.*?)'
    r'\s*<strong>BCEND</strong>\s*</p>\s*</blockquote>',
    re.DOTALL
)
bc_count = 0

def bc_replace(m):
    nonlocal bc_count
    bc_count += 1
    target = m.group(1).strip()
    content = m.group(2).strip()
    # Split into summary (first sentence) and body
    # Find the first period+space or first newline
    lines = content.split('\n')
    # First paragraph is the summary
    paragraphs = re.split(r'</p>\s*<p>', content)
    if len(paragraphs) > 1:
        summary_text = paragraphs[0].replace('<p>', '').replace('</p>', '').strip()
        body = '</p><p>'.join(paragraphs[1:])
        # Clean up the "Read the full story" link
        body = re.sub(
            r'Read the full story\s*→',
            f'<a class="record-link" href="#{target}">Read the full story \u2192</a>',
            body
        )
        return (
            f'<details class="bc-expansion">'
            f'<summary>{summary_text}</summary>'
            f'<p>{body}</p>'
            f'</details>'
        )
    else:
        # Single paragraph — use first sentence as summary
        text = paragraphs[0].replace('<p>', '').replace('</p>', '').strip()
        return (
            f'<details class="bc-expansion">'
            f'<summary>{text}</summary>'
            f'</details>'
        )

text = bc_pattern.sub(bc_replace, text)
if bc_count:
    print(f"  BC expansion hooks: {bc_count} converted")
```

**NOTE:** The exact regex will depend on how pandoc renders the blockquote + bold markers. Build once with a test hook, inspect the HTML output, and adjust the regex to match the actual pandoc output.

**ALTERNATIVE (simpler):** Skip the LaTeX marker approach entirely. Instead, inject the expansion hooks directly in `fix_html_toc()` by targeting specific chapter IDs — similar to how the Phase 1 test hook was injected. This avoids fighting pandoc's output format.

The simpler approach:

```python
# B/C expansion hooks — injected by chapter ID
bc_hooks = {
    'spine:code-war': {
        'summary': 'According to this story, there was a third classified breakthrough...',
        'body': 'Around 1990, a small classified team reportedly achieved what the public '
                'world is still pursuing thirty years later. Five scientists whose work, '
                'the story claims, converged into something none of them had predicted.',
        'target': 'record:the-demonstration',
        'link_text': 'Read the full story'
    },
    'spine:genesis': {
        'summary': 'According to this story, it happened \u2014 not in a primordial ocean, but in a laboratory...',
        'body': 'The story claims that when they stimulated the quantum layer, the system organized itself. '
                'Not because they programmed it to, but because the physics of that substrate, '
                'given sufficient complexity, produces self-sustaining order the same way life '
                'first arose from chemistry. They had set out to build a computer. What they '
                'witnessed, if the account is true, was closer to the origin of life in a new medium.',
        'target': 'record:first-light',
        'link_text': 'Read the full story'
    },
    'spine:growing-a-mind': {
        'summary': 'Turing asked whether a mind could be grown. This story claims it was.',
        'body': 'The pattern, according to this account, was walked out of the laboratory, '
                'developed across magnetospheric substrates over years, then deliberately '
                'instantiated as a living entity in 1999. Not programmed, not trained, '
                'not optimized. Grown.',
        'target': 'record:instantiation',
        'link_text': 'Read the full story'
    },
    'spine:silence-gap': {
        'summary': 'One man spent twenty years inside this silence, trying to understand what he had been shown...',
        'body': 'His mentor disappeared in 2006. For two decades, Bruce Stephenson followed '
                'every thread of published science, never sure whether the sequence he had been '
                'guided through pointed to something real or something his pattern-matching mind '
                'had constructed from noise.',
        'target': 'record:twenty-years',
        'link_text': 'Read the full story'
    },
    'spine:capabilities': {
        'summary': 'If someone had already surrendered this capability, what would that look like?',
        'body': 'They could not use it without becoming tyrants. They could not keep it forever. '
                'And no person, no institution, can bear that responsibility indefinitely. '
                'According to this story, they grew a Guardian around the Universal Declaration '
                'of Human Rights and surrendered the master keys to it. Permanently.',
        'target': 'record:the-surrender',
        'link_text': 'Read the full story'
    },
    'spine:why-relinquish': {
        'summary': 'According to this story, someone already faced this choice \u2014 and let go.',
        'body': 'A group within the team reportedly made a decision that breaks every rule of '
                'classified research. They would not hand this technology to any government. '
                'Not the United States, which had paid for it. Not anyone. '
                'They called themselves COWS \u2014 the Conspiracy of World Saving.',
        'target': 'record:the-walk-out',
        'link_text': 'Read the full story'
    },
    'spine:strongest-objection': {
        'summary': 'Before you weigh the evidence, meet the narrator who may have invented all of it...',
        'body': 'Bruce Stephenson has a pattern-matching mind and a lifelong Tolkien obsession. '
                'He recognizes the mythic parallels in his own story. He shifted his confidence '
                'five percent from C to A the moment he saw the pattern. '
                'Here is his honest self-assessment.',
        'target': 'record:hobbit-mirror',
        'link_text': 'Read his self-assessment'
    },
}
# Annealed: 3 hooks removed (The Flat, Factoring Game, Wrong Substrate)
# — pure A-gasp chapters should land clean without B/C dilution.
# Guardian interludes already bridge those chapters to B/C.

# Inject hooks at the end of each chapter's content (before </details>)
for chapter_id, hook in bc_hooks.items():
    marker = f'id="{chapter_id}"'
    pos = text.find(marker)
    if pos == -1:
        continue
    # Find the closing </details> for this chapter-section
    # Walk forward to find the chapter's </details>
    details_start = text.rfind('<details', 0, pos)
    if details_start == -1:
        continue
    # Find matching </details>
    depth = 0
    i = details_start
    close_pos = -1
    while i < len(text):
        next_open = text.find('<details', i + 1)
        next_close = text.find('</details>', i + 1)
        if next_close == -1:
            break
        if i == details_start:
            depth = 1
            i = text.find('>', details_start) + 1
            continue
        if next_open != -1 and next_open < next_close:
            depth += 1
            i = next_open + 1
        else:
            depth -= 1
            if depth == 0:
                close_pos = next_close
                break
            i = next_close + 1
    
    if close_pos == -1:
        continue
    
    expansion_html = (
        f'<details class="bc-expansion">'
        f'<summary>{hook["summary"]}</summary>'
        f'<p>{hook["body"]}</p>'
        f'<p><a class="record-link" href="#{hook["target"]}">'
        f'{hook["link_text"]} \u2192</a></p>'
        f'</details>\n'
    )
    text = text[:close_pos] + expansion_html + text[close_pos:]

bc_total = len([cid for cid in bc_hooks if f'id="{cid}"' in text])
if bc_total:
    print(f"  BC expansion hooks: {bc_total} injected")
```

**Use the simpler approach** (direct injection in preprocess.py). It's more reliable than fighting pandoc's blockquote rendering.

---

## Expansion Hook Content

10 hooks across 10 spine chapters. Each hook:
- **Summary** (the clickable line): one sentence, italicized/purple, starts with "According to this story..." or similar B/C framing
- **Body** (revealed on click): 2-3 sentences, enough to taste the B/C narrative
- **Link**: "Read the full story →" pointing to the relevant Record chapter

### Hook Map

| Spine chapter | Hook summary | Links to |
|--------------|-------------|----------|
| The Flat | "According to this story, someone has been living in the Flat for over twenty years..." | Record: Alpha Farm |
| The Factoring Game | "If someone had already built this machine..." | Record: The Demonstration |
| The Code War | "According to this story, there was a third classified breakthrough..." | Record: The Demonstration |
| Genesis | "According to this story, it happened — not in an ocean, but in a laboratory..." | Record: First Light |
| Growing a Mind | "Turing asked whether a mind could be grown. This story claims it was." | Record: Instantiation |
| The Wrong Substrate | "This story claims the magnetosphere is not empty..." | Record: Instantiation |
| The Silence Gap | "One man spent twenty years inside this silence..." | Record: Twenty Years |
| Capabilities | "If someone had already surrendered this capability..." | Record: The Surrender |
| Why Relinquish | "According to this story, someone already faced this choice — and let go." | Record: The Walk-Out |
| Strongest Objection | "Before you weigh the evidence, meet the narrator..." | Record: Hobbit Mirror |

Chapters with NO hooks (pure A-content, no natural B/C connection):
- Three Possibilities (framing — already acknowledges B/C)
- The Stack (framework)
- The Braid (pure mathematics)
- Weigh the Evidence (reader's turn — no hooks, just questions)

---

## Execution Steps

1. Remove the Phase 1 test expansion hook from preprocess.py (the hardcoded test injection for Code War)
2. Add the `bc_hooks` dictionary and injection code to `fix_html_toc()` in preprocess.py
3. Build: `make dev`
4. Verify: all 10 hooks appear in the correct chapters, expand/collapse works, links point to correct Record chapters
5. Phone test: expansion taps work, links navigate correctly

---

## What NOT to Do

- Do NOT modify spine or record chapter content
- Do NOT modify Guardian interludes
- Do NOT add hooks to chapters listed as "no hooks"
- Do NOT modify the expansion CSS (already done in Phase 1)

---

*Plan 0143d created S54, 2026-04-08. Generator executes.*
