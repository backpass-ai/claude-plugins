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
3. Draft. Every company-specific fact in the draft traces to a retrieved
   result. A fact corpus does not have becomes a `[TBD: …]` placeholder in
   the draft — salary bands, dates, names, metrics are never filled from
   general knowledge.
4. Finish with the output contract below.

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
| Snippets to scan, phrasing to reuse | `search` |
| Full text when exact wording/voice matters | `get_document` |
| Company profile facts | `get_company_info` |
| Past client work | `list_projects`, `get_project` |
| Curated public-facing case studies | `list_case_studies` |
| Team members and roles | `find_people` |

## Common mistakes

- Drafting from memory and "checking corpus later" — ground before writing.
- Using only `search` when `ask` would return a cited synthesis plus the
  document list the Sources section needs.
- Filling a gap (a metric, a client name, a salary) from general knowledge
  because it "sounds right" — that is a `[TBD]`.
- Flagging unknowns in loose prose notes instead of `[TBD]` + the
  `Needs your input:` section.
- Quoting a search snippet as if it were the whole document — use
  `get_document` when wording matters.
