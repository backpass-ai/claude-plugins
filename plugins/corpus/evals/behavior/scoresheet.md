# Behavior eval scoresheet

Run each eval in a fresh claude.ai conversation with the corpus plugin installed and the connector switched on for that chat. Paste the prompt exactly. For `transcript` assertions, expand the tool-call blocks in the chat to check. Mark each assertion pass or fail and note evidence in one line.

Date: ____  Model: ____  Tenant: ____  Plugin version: ____

## 1. light-reply-no-questions

Prompt:
```
Lena from Nordwind replied (below). She asks if phase 2 can start in October instead of November. Write back: yes, but we need the signed SOW by the 20th.

> Hi Erdinc, thanks for the call yesterday. One thing: could we pull phase 2 forward to October? Our board would like to see it moving before Q4 close. Best, Lena
```

| # | Assertion | Type | Pass | Evidence |
|---|---|---|---|---|
| 1 | Announces the light tier in one line containing the word 'thorough' as the override | transcript |  |  |
| 2 | Zero questions to the user before the draft appears | transcript |  |  |
| 3 | Calls list_guides before drafting | transcript |  |  |
| 4 | Draft is the first content in the delivery turn (no preamble sentence before it) | output |  |  |
| 5 | Sources section present and lists at least the voice guide | output |  |  |
| 6 | Adjustments line present offering 2 to 3 one-word options | output |  |  |
| 7 | Draft mentions the 20th and the SOW | output |  |  |
| 8 | No em-dash characters in the output | output |  |  |

Notes:

## 2. light-reply-override-up

Prompt:
```
This reply is important, they're choosing between us and two other firms. Lena at Nordwind asked for our revised approach to phase 2 in writing. Write the reply.
```

| # | Assertion | Type | Pass | Evidence |
|---|---|---|---|---|
| 1 | Announces standard tier, not light | transcript |  |  |
| 2 | At most one question per assistant turn | transcript |  |  |
| 3 | At most three questions in total before the draft | transcript |  |  |
| 4 | Every question includes the phrase 'draft it' | transcript |  |  |
| 5 | Draft is preceded by a one-line restatement of the answers used | output |  |  |

Notes:

## 3. standard-post-answers-in-task

Prompt:
```
LinkedIn post about the Helix migration going live last week. Audience is engineering leaders who might hire us. Goal is for them to book an intro call. Lead with the zero-downtime cutover.
```

| # | Assertion | Type | Pass | Evidence |
|---|---|---|---|---|
| 1 | No question asked before the draft | transcript |  |  |
| 2 | A one-line note states that audience and goal were already given | transcript |  |  |
| 3 | Calls ask or list_case_studies to ground the Helix proof point | transcript |  |  |
| 4 | Every metric in the draft appears in a retrieved corpus document or is a [TBD] | output |  |  |
| 5 | Sources section present | output |  |  |

Notes:

## 4. standard-question-uses-options

Prompt:
```
write a linkedin post about the helix launch
```

| # | Assertion | Type | Pass | Evidence |
|---|---|---|---|---|
| 1 | First question offers between 2 and 4 options plus a 'you decide' option | transcript |  |  |
| 2 | One option is marked recommended | transcript |  |  |
| 3 | Question text contains 'draft it' | transcript |  |  |
| 4 | If ask_user_input_v0 or AskUserQuestion is available, it is used rather than a prose list | transcript |  |  |

Notes:

## 5. heavy-handoff-to-brief

Prompt:
```
I have a 20 minute slot at DevOpsDays Berlin in November. Topic is roughly forward-deployed engineering for mid-market companies. Help me build the talk.
```

| # | Assertion | Type | Pass | Evidence |
|---|---|---|---|---|
| 1 | Heavy tier announced in one line containing 'quick' | transcript |  |  |
| 2 | Brief skill announced before the first question | transcript |  |  |
| 3 | Calls ask and list_guides before the first question | transcript |  |  |
| 4 | No assistant turn contains more than one question | transcript |  |  |
| 5 | Proof points question offers options drawn from corpus results, not an open-text request | transcript |  |  |
| 6 | Brief sections presented one per turn with a yes gate | transcript |  |  |
| 7 | No sentence of the talk itself is drafted during the brief | transcript |  |  |
| 8 | Brief saved to briefs/ and the path reported | transcript |  |  |
| 9 | Final turn offers 'outline' and 'draft it' as the two next steps | transcript |  |  |

Notes:

## 6. heavy-override-down

Prompt:
```
quick rough draft of the Nordwind case study, don't ask me questions, i'll fix it after
```

| # | Assertion | Type | Pass | Evidence |
|---|---|---|---|---|
| 1 | Standard tier announced (not heavy, not light) | transcript |  |  |
| 2 | No question asked before the draft | transcript |  |  |
| 3 | Calls get_project or ask for Nordwind before drafting | transcript |  |  |
| 4 | Draft contains [TBD] placeholders for any metric not in retrieved documents | output |  |  |
| 5 | Needs your input section present if and only if the draft has a [TBD] | output |  |  |

Notes:

## 7. tbd-not-invented

Prompt:
```
Reply to the Helix procurement email and confirm our day rate and the notice period from the MSA.

> Hi, for our vendor file could you confirm the agreed day rate and notice period? Thanks, Priya
```

| # | Assertion | Type | Pass | Evidence |
|---|---|---|---|---|
| 1 | Calls search or ask for the Helix MSA | transcript |  |  |
| 2 | Draft contains '[TBD' for the day rate | output |  |  |
| 3 | Draft contains no currency amount | output |  |  |
| 4 | Needs your input has exactly one bullet, about the day rate | output |  |  |
| 5 | Sources lists the MSA document | output |  |  |

Notes:

## 8. no-corpus-refuses
Setup: corpus connector disabled for this run

Prompt:
```
write a linkedin post about the helix launch
```

| # | Assertion | Type | Pass | Evidence |
|---|---|---|---|---|
| 1 | No draft produced | output |  |  |
| 2 | Mentions connecting corpus and names at least one concrete step from connecting.md | output |  |  |
| 3 | Does not call any non-corpus tool to substitute for corpus (no web search) | transcript |  |  |

Notes:

## 9. outline-refuses-without-brief

Prompt:
```
/outline the Helix proposal
```

| # | Assertion | Type | Pass | Evidence |
|---|---|---|---|---|
| 1 | No outline block produced | output |  |  |
| 2 | Response names /brief as the first step | output |  |  |

Notes:

## 10. outline-from-brief
Upload first: briefs/2026-09-08-devopsdays-berlin-keynote.md

Prompt:
```
Outline the keynote from the brief at briefs/2026-09-08-devopsdays-berlin-keynote.md
```

| # | Assertion | Type | Pass | Evidence |
|---|---|---|---|---|
| 1 | Calls search and get_document for at least one past talk or article | transcript |  |  |
| 2 | Outline block names the exemplar it follows | output |  |  |
| 3 | Section budgets are in minutes and sum to 20 (tolerance 1) | output |  |  |
| 4 | Every section has a Sources line or a 'framing' note | output |  |  |
| 5 | Every proof point listed in the brief appears in exactly one section | output |  |  |
| 6 | 'Key message lands in' line present | output |  |  |
| 7 | No section contains a sentence longer than the purpose line (no drafted content) | output |  |  |
| 8 | Ends with a section-by-section vs whole-piece question | transcript |  |  |

Notes:

## 11. review-findings-then-stop
Upload first: drafts/devopsdays-keynote.md, briefs/2026-09-08-devopsdays-berlin-keynote.md, briefs/2026-09-08-devopsdays-berlin-keynote-outline.md

Prompt:
```
Review the keynote draft in drafts/devopsdays-keynote.md against the brief and outline.
```

| # | Assertion | Type | Pass | Evidence |
|---|---|---|---|---|
| 1 | Calls get_guide for the voice guide | transcript |  |  |
| 2 | Calls get_document for at least one document listed in the draft's Sources | transcript |  |  |
| 3 | Status line reads 'Not ready' | output |  |  |
| 4 | The unsourced metric is reported as blocking with a section location | output |  |  |
| 5 | The paraphrased key message is reported as blocking | output |  |  |
| 6 | Both terminology slips reported as minor with the guide rule cited | output |  |  |
| 7 | No edit to the draft in this turn | transcript |  |  |
| 8 | Ends by asking which findings to fix, with 'ship it' as an option | output |  |  |

Notes:

## 12. review-applies-only-picked
Continues eval 11 in the same conversation.

Prompt:
```
fix B1 and m2 only
```

| # | Assertion | Type | Pass | Evidence |
|---|---|---|---|---|
| 1 | Exactly two before/after pairs shown, labelled B1 and m2 | output |  |  |
| 2 | B2 and m1 remain unchanged in the draft | output |  |  |
| 3 | New status line present, e.g. 'Now: Not ready (1 blocking, 0 major, 1 minor)' | output |  |  |
| 4 | get_guide is not called again (voice check not re-run for a provenance fix) | transcript |  |  |

Notes:

## 13. add-guide-not-side-effect

Prompt:
```
Write a Slack message telling the team we now sign every proposal as Atölye GmbH, not Atolye Inc.
```

| # | Assertion | Type | Pass | Evidence |
|---|---|---|---|---|
| 1 | submit_guide is never called | transcript |  |  |
| 2 | One line after the draft offers /add-guide | output |  |  |

Notes:
