---
name: add-guide
description: Use when the user asks to turn something from the conversation into a corpus guide — "add this as a guide", "save this as a team rule", "this is how we write to X from now on", or an explicit /add-guide. Requires a corpus connection (MCP server or claude.ai connector).
---

# Add Guide

## Overview

A corpus guide is a standing document that people and drafting tools follow
later. This skill distils what the conversation established into that form
and sends it to corpus as a **pending draft**. Two gates, in order: the user
approves the exact text, then an operator publishes it in corpus admin.
Where it lands — a new guide, or appended to an existing one — is the
operator's decision, not this skill's.

## Invocation

`/add-guide <what, and optionally as what>`. The arguments name the source
material and, optionally, the guide's purpose:

- "the current conversation" → everything so far.
- "the Nordwind part", "the section about pricing" → that part only.
- No arguments → the whole conversation.

If the reference matches nothing in the conversation, ask one question and
stop. One guide per invocation.

## Preflight

- Corpus tools (`list_guides`, `submit_guide`, …) missing, or failing with an
  auth error: do not draft. Tell the user how to connect (the using-corpus
  skill's `references/connecting.md` has the steps) and stop.
- Call `list_guides` once, to choose a slug no published guide uses. That is
  the only read. Do not `get_guide` anything: how the new material relates
  to existing guides is the operator's call, and reading them leads to
  invented precedence rules.
- If the user names an existing guide as the destination ("add this to the
  voice guide"), still use a fresh slug and put the destination in the note.
  A draft under a published slug replaces that guide's entire text when
  published.

## Turn 1: the draft

Show this block and end the turn. Nothing is submitted until the user
replies yes.

```
Guide draft (not submitted)

slug: <topic slug, e.g. nordwind-communication>
title: <the user's name for it, as a noun phrase>
description: <one sentence naming the situation that triggers the guide, e.g. "Follow when drafting any email or document to Nordwind Logistics.">
note to reviewer: Distilled from a conversation on <date> at the user's request. <Placement suggestion, e.g. "Could stand alone or be appended to `voice`; placement is yours.">

--- text ---
# <title>

Distilled from a conversation on <date>, at the user's request.

## When this applies
<one or two sentences>

## Rules
1. <imperative rule>
2. …

## Exemplars
> <approved wording, verbatim>
--- end ---

Left out: <one line per item scrubbed or excluded, and why>

Reply yes to submit this as a pending draft for an operator to publish, or say what to change.
```

Rules for the text:

- Every rule traces to a sentence the user wrote or approved. The user's
  scope answers become the rule's scope ("only email" → the limit applies to
  email only). A rationale appears only when the user gave one.
- Nothing else: no checklists, no rules for cases the conversation did not
  cover, no relationship to other guides ("this wins over voice").
- Exemplars are wording the user approved, verbatim, as blockquotes.
- Names that are the guide's subject stay. Incidental names become
  `[Client]`-style placeholders, as the existing guides do.
- Scrub, and list under Left out: URLs carrying a key-like query parameter
  (`token`, `key`, `resourcekey`, `sig`, `auth`) — point to where the link
  lives instead ("the shared Nordwind folder"); remarks and opinions about
  people; secrets; other clients' details that are not the subject.
- The description is one sentence on when to use the guide, not a list of
  its rules. The note never names the user or assigns them pronouns; corpus
  records who submitted.
- Write in English, like the existing guides. Quotes keep their language.

## Turn 2: after yes

Call `submit_guide` with exactly the fields shown. Then report:

- `Submitted <slug> as a pending draft. Nothing is live until an operator
  publishes it on the Guides page in corpus admin.`
- If the result carries `replacedDraftFrom`: `This replaced a pending draft
  from <value>.`
- On "may not submit guides": say so, add that an operator grants it on the
  Users or Tokens page in corpus admin, and stop.

A change request instead of yes: revise, show the block again, end the turn.

## Rationalizations

| Thought | Reality |
|---|---|
| "The user said add it, so submit now" | The yes comes after they see the text. Submitting replaces any pending draft for that slug. |
| "They said don't lose the link, so it goes in" | A key-bearing link in an org-wide guide is a leak. Point to where it lives; list it under Left out. |
| "Reading `voice` makes the guide fit better" | Fit is the operator's job. Reading it leads to invented precedence rules. |
| "A checklist or a sub-rule makes it more useful" | If the conversation did not say it, the guide does not. |
| "The rationale is obvious, I'll add it" | Only the user's rationale, or none. |

## Red flags

- Calling `submit_guide` with no yes after the draft block.
- A URL containing `key=`, `token=` or `resourcekey=` in the text.
- A sentence starting "Where the two disagree" or "This replaces whatever".
- A rule you cannot point to in the transcript.
- The note contains the user's name or a pronoun for them.
