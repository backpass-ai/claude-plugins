---
name: outline
description: Use after a brief is approved and before drafting any heavy company-facing piece (article, keynote, deck, whitepaper, full proposal, case study, landing page) to agree the structure: sections, their order, word or time budgets, and which corpus documents feed each one. Triggered by the using-corpus heavy tier after the brief skill, by an explicit /outline, or when the user says "outline", "structure this", "what sections". Requires an approved brief and a corpus connection.
---

# Outline

## Overview

An outline turns the brief into a structure the draft can be checked
against: which sections exist, in what order, how long each is, and which
corpus documents each one draws on. Rejecting the structure should never
reopen the brief, which is why this is its own gate.

One gate: the user approves the whole outline. Nothing is drafted here.

## Invocation

- From `brief`: the saved brief path comes with the handoff.
- `/outline <brief path or task>`: the argument names the brief. With no
  brief in the conversation (approved block, uploaded file, or Drive
  link), stop and say the brief comes first
  (`/brief`). Do not build an outline from a bare task; that is drafting
  without a spec.

Announce in one line: `Building the outline from the brief at <path>. One
pass, then a yes from you.`

## Preflight

- Corpus tools missing or failing with an auth error: do not proceed. Point
  to `using-corpus`'s `references/connecting.md` and stop.
- Read the brief in full. Every section you propose must serve its
  outcome, audience and key message.
- Retrieve 2 to 3 same-genre exemplars via `search` then `get_document`
  (past proposals for a proposal, past talks or articles for a keynote or
  article). Their section structure is the starting point, not a generic
  template. Note in the outline which exemplar the structure follows.
- For each proof point in the brief, `get_document` the cited corpus
  document so the section that uses it can be scoped to what the document
  actually says.

## Building the outline

Rules:

- Every section has: a working title, a one-sentence purpose, a budget
  (words, slides, or minutes as the deliverable demands), and a Sources
  line listing the corpus documents it draws on. A section with no corpus
  source is allowed only when its purpose is framing or transition; say
  which.
- Every proof point in the brief appears in exactly one section. A proof
  point that fits nowhere means the outline is wrong, not that the proof
  point is dropped; ask.
- The key message appears verbatim in the section where it lands, so the
  draft can be checked for it.
- Budgets sum to the brief's shape constraint. If they cannot, say what
  has to go.
- Items the brief marks `[TBD]` stay `[TBD]` here, in the section that
  needs them.
- Do not write section content. A purpose sentence is the limit. If you
  notice yourself writing a sentence the reader would read, delete it.

Deck-specific: budget in slides; one purpose per slide; a slide's Sources
line may be empty only for title, agenda, section divider and closing
slides.

Keynote-specific: budget in minutes; mark where the opening and closing
land; note the one line the audience should leave with (the key message)
and which minute it is first said.

## Presenting the outline

Show the whole outline once, using the block below, and ask for a single
yes. If the user changes one section, revise and show the whole block
again; the structure is judged as a whole.

```
Outline (not yet approved)

brief: <path>
deliverable: <type and total budget, e.g. article, 1500 words>
structure follows: <exemplar corpus document title>

1. <working title> (<budget>)
   Purpose: <one sentence>
   Sources: <corpus document titles, or "framing, no source">

2. <working title> (<budget>)
   Purpose: <one sentence>
   Sources: ...

<...>

Key message lands in: section <n>
Proof points placed: <n of n from the brief>
[TBD] carried: <list, or "none">

Yes to approve, or say what to change.
```

## Saving the outline

The approved block in the transcript is the outline. Also write it to
`/mnt/user-data/outputs/briefs/<deliverable-slug>-outline.md` and present
the file next to the brief. If the brief went to Drive, offer the same for
the outline, once.

## Handoff

End with: `Outline saved (file above). Drafting is next, in using-corpus.
Section by section with a check after each, or the whole piece at once?`
Offer the two as options; section by section is the recommended default
for keynotes and proposals, whole piece for articles under 1500 words.

Then stop. `using-corpus` drafts from the brief and outline.

## Asking

Any question this skill asks follows
the using-corpus skill's `references/elicitation.md` (next to its SKILL.md): one per turn, options with a
recommended default, escape hatch in the question text.

## Rationalizations

| Thought | Reality |
|---|---|
| "The brief is clear, I'll outline and draft in one go" | Structure is its own gate. The user rejects an outline in one word; rejecting a draft costs a rewrite. |
| "A standard article structure will do" | The structure comes from a same-genre exemplar in corpus, named in the outline. |
| "This section obviously needs an intro paragraph, I'll sketch it" | Purpose sentences only. Content is drafting. |
| "That proof point doesn't fit, I'll leave it out" | Every brief proof point is placed or the user is asked. |
| "The budgets don't sum but it's close enough" | Say what has to go. Overrunning a keynote is the user's problem to discover now, not on stage. |
| "They changed section 3, I'll just show section 3" | Show the whole block again. |

## Red flags

- An outline built with no brief in the conversation or on disk.
- A section with content sentences instead of a purpose sentence.
- A section with no Sources line and no "framing" note.
- A proof point from the brief absent from every section.
- Budgets that do not sum to the brief's shape constraint, with no note.
- The structure with no exemplar named.
- Handoff without the section-by-section question.
