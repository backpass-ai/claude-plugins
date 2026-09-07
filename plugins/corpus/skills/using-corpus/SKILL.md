---
name: using-corpus
description: Use when drafting company-facing content — emails, job postings, proposal sections, bios, social posts, deck or site copy — or whenever a draft needs company facts such as services, case studies, past projects, clients, people, terminology, or voice. Requires a corpus connection (MCP server or claude.ai connector).
---

# Using Corpus

## Overview

Corpus is the company's knowledge service: the Google Drive document archive
(proposals, case studies, internal docs) indexed and served over MCP. Every
company-specific claim in a draft comes from corpus, and the draft carries its
sources so the reader can check them.

## Invoked with arguments

When invoked as `/using-corpus <task>` (e.g. `/using-corpus write a response
to that email`), the arguments ARE the drafting task: perform it now with the
full workflow below, drawing on whatever material is already in the
conversation (a pasted email, a job description, notes). Invoked with no
arguments, apply the workflow to whatever drafting is underway.

An explicit invocation is a request for the company's voice, not just its
facts. Even a deliverable that needs zero company facts — a plain email
reply, a thank-you note — still gets the voice grounding step before
drafting.

## Preflight

If the corpus tools (`ask`, `search`, `get_document`, …) are not available in
this session, or calls fail with an auth error: **do not draft.** Read
`references/connecting.md` and tell the user how to connect.

Drafting company facts without corpus is the one failure this skill exists to
prevent — a plausible-sounding invented client, metric or date is worse than no
draft at all.

## Workflow

1. Identify the deliverable, its audience, and which company-specific facts it
   needs (voice, services, case studies, people, process, terminology).
2. Ground first: call `ask` with 1–3 focused questions — it returns a cited
   answer plus the exact documents consulted. Add targeted tools from the
   table below when you need raw material rather than synthesis.
3. Ground the voice:
   - Call `list_guides`. If there is a `voice` guide — or any guide whose
     description matches the deliverable (a hiring policy for a job
     posting, say) — `get_guide` it and follow its rules. Guides are the
     operator-published documents every company-facing draft must obey;
     they are not in the search index, so `search` will not find them.
   - Retrieve 2–3 same-genre exemplars — past client emails for an email,
     proposal sections for a proposal, site copy for web copy — via `search`
     then `get_document`. Match their actual register, sentence rhythm,
     greetings and sign-offs, and terminology; never a generic
     "professional" tone.
   - This step is not optional when the deliverable needs no company facts:
     an email reply with nothing to cite still gets exemplars. If the
     archive has no writing in the deliverable's genre, use the closest
     genre it has and say so in one line after the draft.
4. Draft. Every company-specific fact in the draft traces to a retrieved
   result. A fact corpus does not have becomes a `[TBD: …]` placeholder in
   the draft — salary bands, dates, names, metrics are never filled from
   general knowledge.
5. Finish with the output contract below.

## Output contract

The response contains, in order:

1. **The draft**, with `[TBD: …]` placeholders where corpus had no answer.
2. **`Needs your input:`** — one bullet per `[TBD]` explaining what to fill
   in. Omit the section when there are none.
3. **`Sources:`** — a deduped bullet list of every corpus document used:
   title linked to its `sourceUrl` (title alone when `sourceUrl` is null).
   Build it from `ask`'s `documents` array plus any other document refs
   consulted. This section is REQUIRED whenever any corpus fact was used;
   note in one line that it can be deleted before sending.

## Tool quick reference

| Need | Tool |
|---|---|
| Synthesized answer with citations (start here) | `ask` |
| Voice guide, policies, standing rules (published by operators) | `list_guides`, `get_guide` |
| Snippets to scan, phrasing to reuse | `search` |
| Full text when exact wording/voice matters | `get_document` |
| Company profile facts | `get_company_info` |
| Past client work | `list_projects`, `get_project` |
| Curated public-facing case studies | `list_case_studies` |
| Team members and roles | `find_people` |

## Proposing a guide

When the user asks to turn something into a guide, or to revise one
("submit this as the new voice guide"), use the add-guide skill: it shows
the distilled draft for approval and only then calls `submit_guide`, which
lands a **pending draft** under its own slug — nothing is live until an
operator publishes it in corpus admin, and the operator decides whether it
becomes a new guide or joins an existing one. Never submit as a side effect
of drafting: noticing that the voice guide is out of date is something to
mention, not something to fix on your own.

## Common mistakes

- Drafting from memory and "checking corpus later" — ground before writing.
- Skipping voice grounding because the deliverable needs no company facts —
  an explicit `/using-corpus` invocation asks for the company's voice, and
  that comes from the published voice guide and exemplars, not from a
  generic register.
- `search`ing for a style guide — guides live outside the archive; only
  `list_guides`/`get_guide` return them.
- Calling `submit_guide` because a draft revealed a gap in a guide — that
  is the user's call, not the skill's.
- Calling `submit_guide` directly instead of through add-guide — the user
  never saw the text that was sent.
- Using only `search` when `ask` would return a cited synthesis plus the
  document list the Sources section needs.
- Filling a gap (a metric, a client name, a salary) from general knowledge
  because it "sounds right" — that is a `[TBD]`.
- Flagging unknowns in loose prose notes instead of `[TBD]` + the
  `Needs your input:` section.
- Quoting a search snippet as if it were the whole document — use
  `get_document` when wording matters.
