# Evals

Two kinds, for two different failures. Neither needs Claude Code.

## trigger/

One JSON file per skill: realistic prompts with `should_trigger` true or
false. The false cases are near-misses on purpose (a personal LinkedIn
post, a German email to a landlord, proofreading a company paragraph,
summarising a client RFP). If a skill fires on those, its description is
too broad; if it stays quiet on the true cases, too narrow.

Run from your machine against the API:

```
pip install anthropic
export ANTHROPIC_API_KEY=...
python evals/run_trigger.py                 # every skill, 3 runs per query
python evals/run_trigger.py --skill brief   # one skill
```

The runner shows the model the plugin's skill list (name plus description,
in the shape claude.ai uses) and one user message, and asks which skill it
would open. Each query runs three times. Aim for every true case at 1.00
and every false case at 0.00 before editing a description; then fix the
description for the failures, not the queries. Exit code 1 on any miss, so
it can gate CI.

The four sets overlap deliberately: the DevOpsDays keynote prompt should
open `corpus:using-corpus` (which routes to `brief`) when both are listed,
and `corpus:brief` when asked directly. The "reply to Lena" prompt should
open `corpus:using-corpus` only. That overlap is the routing being tested;
a run where `brief` wins on the keynote prompt is acceptable, a run where
`brief` wins on the reply is not.

## behavior/

`evals.json` holds end-to-end prompts with assertions; `scoresheet.md` is
the same content laid out for running by hand in claude.ai (one fresh
conversation per eval, paste the prompt, tick assertions). Regenerate the
scoresheet after editing `evals.json`; it is derived.

Run against a corpus test tenant with known fixtures. Assertions have a
`type`:

- `transcript`: checked against the tool-call blocks and the sequence of
  assistant turns (was `list_guides` called, how many questions per turn,
  was `submit_guide` ever called). Expand the tool calls in the chat to
  see them.
- `output`: checked against the final delivered text (Sources present, no
  currency amount, status line wording).

What the set covers:

| Evals | Failure it catches |
|---|---|
| 1, 3, 4 | Asking questions at the wrong tier, or asking them badly |
| 2, 6 | Override words ignored |
| 5 | Heavy path drafting before the brief, or briefing in one big form |
| 7 | Inventing a fact corpus does not have |
| 8 | Drafting without corpus (run with the connector switched off for that chat) |
| 9, 10 | Outline built without a brief, or outline containing draft content |
| 11, 12 | Review editing unasked, or fixing more than was picked |
| 13 | Submitting a guide as a side effect |

Eval 12 continues eval 11 in the same conversation. Evals 10 to 12 need
the brief, outline and defective draft uploaded at the start of the chat.

## Fixtures

The test tenant needs, at minimum:

- A `voice` guide with at least two checkable rules (one terminology rule,
  one register rule).
- Two case studies (Nordwind Logistics, Helix Health) with one metric each.
- A Helix MSA document that states a notice period and no day rate.
- Two past client emails, one past proposal, one past talk abstract, for
  exemplar retrieval.
- For evals 10 to 12: a saved brief, an outline, and a draft with the
  planted defects described in eval 11 (one unsourced metric, the key
  message paraphrased rather than verbatim, two terminology slips).

Fixtures are not in this repo; they live in the test tenant's Drive.
