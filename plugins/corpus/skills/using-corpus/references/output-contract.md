# Output contract

What every corpus draft looks like when delivered. The SKILL.md lists the
parts; this file shows them and explains what each is for.

## Parts, in order

1. **The draft.** Nothing before it: no "Here is the draft", no summary
   of the questions asked. Standard tier prefixes one line restating the
   answers used, because the user may have said "you decide" and should
   see what was decided.
2. **`Needs your input:`** one bullet per `[TBD: …]` in the draft, in
   order of appearance, each saying what to fill in and, when useful,
   where it might be found. Omitted entirely when there are no `[TBD]`s.
3. **`Sources:`** a deduped list of every corpus document used, title
   linked to `sourceUrl`, title alone when `sourceUrl` is null. Built from
   `ask`'s `documents` array plus any `get_document`, `get_project`,
   `list_case_studies` or `find_people` result that contributed a fact.
   Guides are listed too (`voice guide`), since they shaped the wording.
   Ends with one line: `Delete this section before sending.`
4. **Light tier:** one line offering two or three one-word adjustments
   that fit the piece.
5. **Heavy tier:** the brief and outline files presented alongside the
   draft (claude.ai keeps no files between conversations, so the user
   downloads them or saves them to Drive).

## Why the parts are separate

- The draft is what gets copied. Anything above it gets copied by
  accident.
- `Needs your input` exists so gaps are a checklist, not something to
  hunt for in the text.
- `Sources` exists so the reader can verify a claim before it goes out,
  and so a colleague can find the case study the draft mentions. It is
  the reason the plugin can be trusted with client names.
- The adjustments line replaces questions at the light tier: the user
  reacts to a draft instead of answering a form.

## Example, light tier

```
Hi Lena,

Thursday works. I will send a calendar invite for 14:00 and include Tomas
from our delivery team, since he ran the Nordwind onboarding you asked
about.

Best,
Erdinc

Sources:
- [Nordwind Logistics onboarding case study](https://drive.google.com/...)
- voice guide
Delete this section before sending.

Say shorter, warmer or more formal and I will redo it.
```

## Example, standard tier with a gap

```
Angle: engineering leaders evaluating a partner. Proof point: Helix migration.

Zero-downtime migrations are not luck. When Helix Health moved their
platform to Kubernetes with us, the cutover ran during business hours
and nobody outside the team noticed. [TBD: number of services migrated]
went across over six weeks, with every rollback path rehearsed before
it was needed.

If your next migration cannot afford a maintenance window, that is the
kind of work we do.

Needs your input:
- [TBD: number of services migrated]: the case study mentions the
  migration but not the count; the project retro in Drive may have it.

Sources:
- [Helix Health platform migration case study](https://drive.google.com/...)
- voice guide
Delete this section before sending.
```

## Example, heavy tier tail

```
<draft>

Needs your input:
- …

Sources:
- …
Delete this section before sending.

[files presented: devopsdays-berlin-keynote-brief.md, devopsdays-berlin-keynote-outline.md]
```
