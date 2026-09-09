---
name: brief
description: Use before drafting any heavy company-facing piece (article, keynote, deck, whitepaper, full proposal, case study, landing page) to agree on audience, key message, desired action, proof points and tone before a word of the draft is written. Triggered by the using-corpus skill's heavy tier, by an explicit /brief, or when the user says "let's plan this", "before you write", "what's the angle". Requires a corpus connection (MCP server or claude.ai connector).
---

# Brief

## Overview

A brief is the agreement about what a piece says, to whom, and why, before
anyone argues about how it is structured. This skill teases the brief out of
the user one question at a time, proposes answers from corpus wherever it
can, then shows the brief in sections short enough to approve or reject
individually. The approved brief is saved and travels with the outline and
draft.

Two gates: the user approves each section, then approves the whole. Nothing
is drafted here. The output is a brief, not content.

## Invocation

- From `using-corpus` heavy tier: the task, the deliverable type and any
  material already in the conversation come with the handoff.
- `/brief <task>`: the arguments are the task.
- No arguments: brief whatever drafting is underway.

Announce in one line: `Building the brief. One question at a time; say
"draft it" at any point and I will fill the rest with defaults and move to
the outline.`

## Preflight

- Corpus tools missing or failing with an auth error: do not proceed. Point
  to `using-corpus`'s `references/connecting.md` and stop.
- Ground before asking. Call `ask` with 1 to 3 questions about the topic:
  what the company has said about it before, which projects or case studies
  touch it, which people are associated with it. Call `list_guides` and
  `get_guide` the voice guide plus any guide matching the deliverable.
  Everything corpus answers here is proposed, not asked.

## Question loop

One question per turn. Each question offers 2 to 4 options with a
recommended default marked, plus "you decide", and ends with
`or say "draft it" and I will use the defaults`. The question shape and
the per-surface tool mapping are in
the using-corpus skill's `references/elicitation.md` (next to its SKILL.md); read it before the first
question.

Ask only what the task and corpus have not already answered. Skip a slot
silently when it is already known; say `You already told me the audience`
only if the user might wonder why it was not asked.

The slots, in order:

1. **Outcome.** What should the reader do or believe after this? Options
   come from the deliverable type (proposal: request a call, accept the
   scope; keynote: remember one idea, look the company up; article: share
   it, subscribe, contact).
2. **Audience.** Who exactly reads or hears it, and what do they already
   know? Propose from the task (a named client, a conference) and from
   corpus (past proposals to similar clients).
3. **Key message.** The one sentence the reader should be able to repeat.
   Propose two or three candidates grounded in what corpus says the company
   actually claims; never invent a positioning the archive does not
   support.
4. **Proof points.** Which case studies, projects, numbers or people back
   the message. Propose from `ask`, `list_case_studies`, `list_projects`,
   `find_people`. The user picks; you never ask them to name one from
   memory. Anything they want that corpus lacks is recorded as `[TBD]`.
5. **Shape constraints.** Length or duration, format, venue, deadline,
   anything that must or must not appear. Propose defaults from the
   deliverable type and from same-genre exemplars in corpus.
6. **Tone within the voice guide.** Only if the voice guide allows a range
   (a "plain" and a "formal" register, say). If the guide fixes the tone,
   skip this slot and state the tone in the brief as a given.

Stop early when the user says "draft it" or "you decide". Fill the
remaining slots with the recommended defaults and mark each as
`(default, not confirmed)` in the brief.

## Presenting the brief

After the loop, show the brief one section per turn, each ending with
`Yes to keep, or say what to change.` Move to the next section only after a
yes. The sections are the six slots above plus a seventh:

7. **Not in scope.** What this piece will deliberately not cover or claim.
   Derived from the answers; the user confirms.

Then show the whole brief once, using the block below, and ask for a single
final yes.

```
Brief (approved)

deliverable: <type, e.g. keynote, 20 minutes>
task: <the user's task in one line>

## Outcome
<one or two sentences>

## Audience
<one or two sentences>

## Key message
<one sentence, verbatim as approved>

## Proof points
- <case study or project title> (<corpus document title>)
- <person and role> (<corpus document title>)
- [TBD: <what corpus lacks and the user wants>]

## Shape
<length or duration, format, venue, deadline, must and must-not>

## Tone
<register named in the voice guide, or "as fixed by the voice guide">

## Not in scope
- <item>

Sources:
- <title linked to sourceUrl, one per corpus document consulted>
```

## Saving the brief

The approved block in the transcript is the brief. claude.ai does not keep
files between conversations, so also:

- Write the block to `/mnt/user-data/outputs/briefs/<deliverable-slug>-brief.md`
  and present the file, so the user can download it and paste it into a
  later conversation.
- If the Google Drive connector is connected, offer once: `Save the brief
  to Drive as well? It will then be findable by corpus.` Save only on yes,
  to the folder the user names; report the link.

A change to the brief later is an edit to that block, restated in full, not
a new round of questions.

## Handoff

End with: `Brief saved (file above). Next is the outline: sections, word
budgets, and which corpus documents feed each one. Say "outline" to
continue, or "draft it" to skip the outline and draft from the brief
directly.`

Then stop. The `outline` skill takes it from here.

## Rationalizations

| Thought | Reality |
|---|---|
| "I'll ask audience, message and proof in one message to be efficient" | One per turn. The loop is short because most slots are proposed, not asked. |
| "They didn't answer the key message, I'll write a good one" | Propose from corpus, mark it default, not confirmed. Never silently decide the message. |
| "This case study fits perfectly, corpus just hasn't indexed it" | If corpus has not got it, it is a `[TBD]`. The archive is the source of truth. |
| "The brief is obvious from the task, I'll skip to the outline" | Show the brief anyway; the user's yes is what makes it a brief. Showing an obvious brief takes one turn. |
| "Approved section by section, no need for the final yes" | Section approvals can conflict once seen together. The final yes catches that. |
| "I'll draft the opening paragraph so they can see the direction" | Nothing is drafted here. Direction is the key message sentence. |

## Red flags

- Two or more questions in a single turn.
- A question without the "draft it" escape hatch.
- A proof point with no corpus document beside it and no `[TBD]`.
- A key message the user never saw before it appeared in the outline.
- A brief presented all at once without the section-by-section pass.
- Any sentence of the actual piece written in this skill.
- A slot asked when the task or corpus already answered it.
