# Tiers

How `using-corpus` sizes a job. The SKILL.md table is the rule; this file
is the reasoning and the edge cases. Read it when a task does not fall
cleanly into one row of the table.

## The principle

Effort should scale with how expensive a wrong draft is. A wrong email
reply costs the user thirty seconds and one word of correction; a wrong
keynote costs a week and possibly the talk. So the light tier optimises for
time to first draft, the heavy tier optimises for never drafting the wrong
thing, and standard sits between.

The tier decides only two things: how many questions come before the
draft, and whether the brief, outline and review gates run. Grounding in
corpus happens at every tier.

## Signals, in priority order

1. **Explicit override words** in the user's message beat everything.
   Down: quick, fast, rough, first pass, just draft, don't ask, no
   questions, one-liner. Up: thorough, important, careful, let's plan,
   before you write, for the board, for a client, for the CEO, this
   matters.
2. **Deliverable type** as named or clearly implied. See the table in
   SKILL.md.
3. **Length or duration** stated or implied. Over roughly 800 words, over
   roughly 10 slides, over roughly 10 minutes of talk: heavy.
4. **Audience stakes** when the type is ambiguous. External and named
   (a client, a conference, a publication): lean up. Internal and
   informal: lean down.
5. **Material already provided.** A user who pastes a full outline or
   detailed notes has done the brief; treat a heavy deliverable as
   standard, say so, and offer the outline gate anyway.

## Worked examples

| Task as written | Tier | Why |
|---|---|---|
| "reply to this and say we can do Thursday" (email pasted) | Light | Reply, register given, content given |
| "write back to Nordwind, they want a revised quote" | Light | Reply, but if corpus has the quote history propose it in the draft rather than asking |
| "draft a LinkedIn post about the Helix launch" | Standard | Social post, named subject, one question on audience or angle |
| "we need a job posting for a senior backend engineer" | Standard | Job posting; check for a hiring guide via `list_guides` |
| "write the case study for the Nordwind project" | Heavy | Case study is a heavy type; proof points and structure matter |
| "quick case study draft for Nordwind, rough is fine" | Standard | Override word moves heavy down one |
| "I have a 20 minute slot at DevOpsDays Berlin, help me with the talk" | Heavy | Keynote or talk, duration given, external audience |
| "just give me a rough title and three bullets for my DevOpsDays talk" | Light | Explicit scope: not the talk, a sketch of it |
| "write a proposal section on our delivery approach" | Standard | Single section |
| "write the proposal for Helix" | Heavy | Full proposal |
| "short bio for the conference site" | Light | Short and formulaic; corpus `find_people` has the facts |
| "full bio for the about page" | Standard | Longer, public, one question on emphasis |
| "here are my notes and structure for the whitepaper, write it up" (long paste) | Standard, offer outline gate | User did the brief; confirm structure once, then draft |
| "this reply is important, they are deciding between us and two others" | Standard | Reply moved up one by "important" |

## When the user disagrees

The announcement line always names the override word for the other
direction. If the user uses it, switch tiers and continue without comment
beyond `Switching to <tier>.` If the user disagrees with the tier a second
time in the same session, ask once which tier they want for the rest of
the session and keep it.

## What the tier does not change

- Grounding. Every tier calls `list_guides` and retrieves exemplars.
- The `[TBD]` rule. No tier fills a gap from general knowledge.
- The Sources section. Any tier that used a corpus fact lists it.
- The add-guide boundary. No tier submits guides as a side effect.
