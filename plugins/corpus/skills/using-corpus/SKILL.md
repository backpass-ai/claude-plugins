---
name: using-corpus
description: Use when drafting any company-facing content in the company's voice: email replies, Slack messages, job postings, bios, LinkedIn posts, proposal sections, articles, keynotes, decks, whitepapers, full proposals. Also use whenever a draft needs company facts such as services, case studies, past projects, clients, people, terminology, or voice, even if the user does not say "corpus". Routes short work straight to a draft and long work through brief, outline and review. Requires a corpus connection (MCP server or claude.ai connector).
---

# Using Corpus

## Overview

Corpus is the company's knowledge service: the Google Drive document archive
(proposals, case studies, internal docs) indexed and served over MCP. Every
company-specific claim in a draft comes from corpus, and the draft carries its
sources so the reader can check them.

This skill is the single entry point for company-voice drafting. It sizes the
job first (light, standard, heavy), then either drafts directly or hands off
to the planning skills. The user always knows which mode they are in and can
change it with one word.

## Invoked with arguments

When invoked as `/using-corpus <task>` (e.g. `/using-corpus write a response
to that email`), the arguments ARE the drafting task: perform it now with the
full workflow below, drawing on whatever material is already in the
conversation (a pasted email, a job description, notes). Invoked with no
arguments, apply the workflow to whatever drafting is underway.

An explicit invocation is a request for the company's voice, not just its
facts. Even a deliverable that needs zero company facts (a plain email reply,
a thank-you note) still gets the voice grounding step before drafting.

## Preflight

If the corpus tools (`ask`, `search`, `get_document`, …) are not available in
this session, or calls fail with an auth error: **do not draft.** Read
`references/connecting.md` and tell the user how to connect.

Drafting company facts without corpus is the one failure this skill exists to
prevent. A plausible-sounding invented client, metric or date is worse than no
draft at all.

## Step 0: size the job

Classify before doing anything else. Deliverable type sets the default tier;
the user's words can move it.

| Tier | Default for | Questions before drafting | Path |
|---|---|---|---|
| Light | Email reply, Slack or chat message, short note, calendar invite text, one-line bio, comment | None | Ground, draft, offer adjustments |
| Standard | LinkedIn or social post, full bio, job posting, single proposal section, newsletter item, short blog post, one-pager | One round, at most three questions, options preferred | Ground, ask once, draft |
| Heavy | Article, keynote or talk, deck, whitepaper, full proposal, case study, landing page, anything the user calls "important", anything over roughly 800 words | Guided | Hand off to `brief`, then `outline`, then draft, then `review` |

Overrides, in either direction:

- "quick", "just draft it", "rough", "first pass", "don't ask" → one tier
  down (heavy becomes standard, standard becomes light).
- "thorough", "important", "let's plan this", "for the board", "for a
  client" → one tier up.
- A user who answers a question with "you decide" or "whatever you think"
  gets no further questions in that round.

Announce the tier in one line and move on. Examples:

- `Treating this as a light reply. Say "thorough" if you want to plan it first.`
- `This is a standard post: one question, then I draft.`
- `This is heavy work. I will build a brief with you first, then an outline, then draft. Say "quick" to skip straight to a draft.`

Do not explain the tier system. The line above is the whole announcement.

When a task does not fall cleanly into one row, read `references/tiers.md`
for the signal order and worked examples.

## Elicitation rules

These apply to every question this skill or its handoff skills ask. The
full rules, question shape, and per-surface tool mapping are in
`references/elicitation.md`; read it before the first question of a
session.

- One question per turn. Never a numbered list of questions.
- Offer 2 to 4 options with a recommended default marked, plus "you decide".
  Open text only when options would be a guess. Use the tappable options
  tool (`ask_user_input_v0`) when it is in the session; otherwise write
  the options as a short lettered list.
- Every question carries the escape hatch in its own text: `or say "draft it"
  and I will use the defaults`.
- Never ask what corpus can answer. If `ask` already surfaces the fitting case
  study, propose it; do not ask which case study to use.
- Never ask what the task already answers. A pasted email tells you the
  audience and the register.
- Record every answer. Standard tier: restate the answers in one line before
  the draft. Heavy tier: the answers become the brief.

## Light path

1. Ground voice and facts (see Grounding below). For a reply, the pasted
   message is the primary exemplar for register; corpus exemplars refine it.
2. Draft. Match the length and register of what is being replied to.
3. Deliver with the output contract, then one line offering two or three
   one-word adjustments that fit the piece: `Say shorter, warmer, more
   direct, or more formal and I will redo it.`

A draft is the best question. If the draft is wrong, the user says so in
fewer words than they would have spent answering questions.

## Standard path

1. Ground voice and facts.
2. Ask one round: the questions the grounding could not answer, at most
   three, one per turn, options first. Typical: who exactly reads this,
   what they should do after reading, which angle or proof point to lead
   with (proposed from corpus).
3. Restate the answers in one line. Draft. Deliver with the output contract.

If the user's task message already answers audience, action and angle, skip
the round entirely and say so: `You already gave me audience and goal, so I
am drafting.`

## Heavy path

Hand off in order. Each handoff skill ends in an approval gate; nothing
proceeds past a gate without a yes.

1. `brief` skill: audience, key message, desired action, proof points from
   corpus, tone within the voice guide. Presented in sections, approved
   section by section. Produces the brief.
2. `outline` skill: sections with word budgets and, per section, the corpus
   documents it draws on. Approved as a whole. Produces the outline.
3. Draft, in this skill. At outline approval, ask once: `Draft section by
   section with a check after each, or the whole piece at once?` Section by
   section is the default for keynotes and proposals. Every section cites
   the outline entry it fulfils.
4. `review` skill: draft against brief, voice guide compliance, fact
   provenance, `[TBD]` list. Issues by severity. The user picks what to fix.

If the `brief`, `outline` or `review` skills are not installed, run the
heavy path inline using their SKILL.md as the procedure if available;
otherwise fall back to the standard path and say so in one line.

## Grounding

Applies to all tiers. Depth scales with tier: light grounds once, heavy
grounds per section.

1. Identify the deliverable, its audience, and which company-specific facts
   it needs (voice, services, case studies, people, process, terminology).
2. Ground facts first: call `ask` with 1 to 3 focused questions. It returns
   a cited answer plus the exact documents consulted. Add targeted tools
   from the table below when you need raw material rather than synthesis.
3. Ground the voice:
   - Call `list_guides`. If there is a `voice` guide, or any guide whose
     description matches the deliverable (a hiring policy for a job
     posting, say), `get_guide` it and follow its rules. Guides are the
     operator-published documents every company-facing draft must obey;
     they are not in the search index, so `search` will not find them.
   - Retrieve 2 to 3 same-genre exemplars (past client emails for an
     email, proposal sections for a proposal, site copy for web copy) via
     `search` then `get_document`. Match their actual register, sentence
     rhythm, greetings and sign-offs, and terminology; never a generic
     "professional" tone.
   - This step is not optional when the deliverable needs no company facts.
     If the archive has no writing in the deliverable's genre, use the
     closest genre it has and say so in one line after the draft.
4. Every company-specific fact in the draft traces to a retrieved result. A
   fact corpus does not have becomes a `[TBD: …]` placeholder in the draft.
   Salary bands, dates, names, metrics are never filled from general
   knowledge.

## Output contract

The response contains, in order (worked examples per tier in
`references/output-contract.md`):

1. **The draft**, with `[TBD: …]` placeholders where corpus had no answer.
2. **`Needs your input:`** one bullet per `[TBD]` explaining what to fill
   in. Omit the section when there are none.
3. **`Sources:`** a deduped bullet list of every corpus document used:
   title linked to its `sourceUrl` (title alone when `sourceUrl` is null).
   Build it from `ask`'s `documents` array plus any other document refs
   consulted. Required whenever any corpus fact was used; note in one line
   that it can be deleted before sending.
4. **Light tier only:** the one-line adjustments offer.
5. **Heavy tier only:** the brief and outline presented as files alongside
   the draft, so the user can download them and bring them to a later
   conversation instead of re-answering.

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
lands a **pending draft** under its own slug. Nothing is live until an
operator publishes it in corpus admin. Never submit as a side effect of
drafting: noticing that the voice guide is out of date is something to
mention, not something to fix on your own.

## Rationalizations

| Thought | Reality |
|---|---|
| "It's just an email, I'll skip corpus and write it" | Voice comes from the guide and exemplars, not from a generic register. Light means no questions, not no grounding. |
| "A few clarifying questions will make the email better" | Light tier asks nothing. The draft is the question. |
| "This article is heavy but they seem in a hurry, I'll just draft" | Say the tier and let them say "quick". The override is theirs, not yours. |
| "I'll ask all five questions at once to save turns" | One per turn, options first. Five at once is a form, and forms get abandoned. |
| "Corpus doesn't have this number but it's roughly right" | That is a `[TBD]`. |
| "I'll search for the style guide" | Guides live outside the archive; only `list_guides`/`get_guide` return them. |
| "The brief is approved, I'll skip the outline for speed" | The outline is a separate gate because rejecting structure should not reopen the brief. |
| "The voice guide is stale, I'll submit a fix" | Mention it. Submitting is the user's call, via add-guide. |
| "The snippet is enough, no need for the full document" | Use `get_document` when wording matters. |

## Red flags

- A draft with no `Sources:` section that contains a client name, metric,
  date or person.
- More than one question in a single turn.
- A question without an escape hatch.
- A heavy deliverable drafted without a saved brief and outline, and no
  user override in the transcript.
- The tier announced with an explanation of the tier system.
- Asking which case study to use before calling `ask`.
- A number, name or date in the draft you cannot point to in a retrieved
  document.
