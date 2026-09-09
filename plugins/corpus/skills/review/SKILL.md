---
name: review
description: Use after drafting any heavy company-facing piece (article, keynote, deck, whitepaper, full proposal, case study, landing page) to check the draft against its brief, its outline, the voice guide and corpus fact provenance, and report issues by severity for the user to decide on. Triggered by the using-corpus heavy tier after drafting, by an explicit /review, or when the user says "review this", "check this against the brief", "is this on-voice", "did we cover everything". Also usable on a standard-tier draft when the user asks. Requires a corpus connection.
---

# Review

## Overview

A review answers four questions about a finished draft: does it do what the
brief says, does it follow the outline, does it sound like the company, and
can every company fact be traced. It reports findings by severity and
stops. The user decides what gets fixed; the reviewer never edits the draft
on its own.

Two outputs: a findings report, then (only after the user picks) the fixes.

## Invocation

- From `using-corpus` heavy tier: the draft, brief path and outline path
  come with the handoff.
- `/review <what>`: reviews the named draft. With no brief available,
  run only the voice and provenance checks and say the brief and outline
  checks were skipped and why.
- Standard-tier drafts: voice and provenance checks only, unless the user
  supplies a brief.

Announce in one line: `Reviewing the draft against the brief, outline,
voice guide and corpus. Findings first, fixes only after you pick.`

## Preflight

- Corpus tools missing or failing with an auth error: run the brief and
  outline checks, skip voice and provenance, and say so. Do not guess at
  voice from memory.
- `list_guides`, then `get_guide` the voice guide and any guide matching
  the deliverable. Read the brief and outline in full.
- Retrieve the corpus documents cited in the draft's Sources section via
  `get_document`, so provenance can be checked against text rather than
  titles.

## The four checks

Run all four before reporting anything. Each finding carries a location
(section number and, where useful, the sentence), a severity, and one
sentence of evidence.

**1. Brief compliance.**
- Is the key message present verbatim, in the section the outline placed
  it, and not contradicted anywhere?
- Does the piece ask for the brief's outcome (the action or belief), and
  is that ask where the reader will see it?
- Is the register right for the brief's audience (what they already know
  is neither re-explained nor assumed beyond the brief)?
- Does anything in "Not in scope" appear?

**2. Outline compliance.**
- Every outline section present, in order, with the purpose it was given.
- Each section's budget within roughly 15 percent of the outline. Total
  within the brief's shape constraint.
- Every proof point in the section the outline assigned it.
- No sections the outline did not have, unless the user added them in
  drafting (check the transcript).

**3. Voice.**
- Each rule in the voice guide, checked once against the whole draft.
  Cite the rule and the sentence that breaks it.
- Terminology: names of services, products and roles match the guide and
  the exemplars. Flag synonyms the company does not use.
- Register drift: sections that read as a different author (typically the
  ones drafted last, or the ones with no corpus source).
- Greetings, sign-offs and calls to action match same-genre exemplars.

**4. Provenance.**
- Every client name, person, metric, date, project and claim about the
  company's work either appears in a retrieved corpus document or is a
  `[TBD]`. A sentence that paraphrases a source beyond what the source
  says is a finding.
- Every `[TBD]` in the draft has a bullet under `Needs your input`.
- The Sources section lists every document actually used and nothing
  that was not.

## Severity

| Severity | Meaning | Examples |
|---|---|---|
| Blocking | Ships wrong or unverifiable | Company fact with no corpus source; key message missing or contradicted; out-of-scope claim; outline section missing |
| Major | Ships weaker than the brief | Outcome ask buried or absent; proof point in the wrong section; voice guide rule broken; budget off by more than 15 percent |
| Minor | Polish | Terminology synonym; register drift in one sentence; Sources line missing a document that was used |

A draft with any blocking finding is reported as `Not ready`. Otherwise
`Ready with <n> major, <n> minor`.

## Presenting the findings

Show the block once and stop. Do not fix anything in the same turn.

```
Review: <Ready | Not ready> (<n> blocking, <n> major, <n> minor)

draft: <where it is>
brief: <path>
outline: <path>

## Blocking
B1. [section <n>] <finding>. Evidence: <one sentence>. Fix: <one line>.

## Major
M1. [section <n>] <finding>. Evidence: <one sentence>. Fix: <one line>.

## Minor
m1. [section <n>] <finding>. Fix: <one line>.

Checks skipped: <none, or which and why>

Say which to fix (e.g. "all blocking and M2", "everything", "just B1"),
or "ship it" to leave the draft as is.
```

Every fix line is one sentence stating what would change, not the changed
text. The user sees the change before it happens.

## After the user picks

Apply only the fixes named. Show each changed passage as before and after,
grouped by finding id. Re-run only the checks the fixes touch (a provenance
fix does not trigger a full voice re-review). Report the new status in one
line: `Now: Ready with 1 minor.` Then stop.

"Everything" means every finding at every severity. "Ship it" means no
edits; restate the status line and stop.

## Asking

Any question this skill asks follows
the using-corpus skill's `references/elicitation.md` (next to its SKILL.md): one per turn, options with a
recommended default, escape hatch in the question text.

## Rationalizations

| Thought | Reality |
|---|---|
| "The fix is obvious, I'll apply it while reporting" | Findings first, fixes after they pick. The draft is theirs. |
| "It reads well, voice is fine" | Check each voice guide rule once, with a cited sentence. "Reads well" is not a check. |
| "The number is close to what the case study says" | Paraphrase beyond the source is a blocking provenance finding. |
| "They added a section during drafting, that's an outline violation" | Check the transcript. A user-added section is not a finding. |
| "Minor issues aren't worth listing" | List them. The user decides what minor means for this piece. |
| "I fixed B1, I'll re-run everything to be safe" | Re-run what the fix touched. A full re-review after every fix is how reviews never end. |
| "No brief, so I'll review against what a brief would probably say" | Skip the brief and outline checks and say so. Never invent the spec. |

## Red flags

- Any edit to the draft in the findings turn.
- A finding with no section location.
- A voice finding with no cited rule.
- A provenance finding with no corpus document named as the source that
  was checked.
- "Ready" with a company fact that has no source and no `[TBD]`.
- Fixes applied beyond the ones the user named.
- Voice reviewed without `get_guide` having been called.
