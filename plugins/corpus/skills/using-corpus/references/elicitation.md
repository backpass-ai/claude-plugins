# Elicitation

How every corpus skill asks the user a question. `using-corpus` carries the
short version; this file is the full rule set with the reasoning, examples,
and the tool mapping. Read it when a skill is about to ask its first
question in a session.

## Why these rules exist

The plugin's promise is that the user controls the content. Control comes
from being asked the right thing at the right moment, not from being asked
a lot. A three-question form before an email reply is the fastest way to
make someone stop using the plugin. A single well-placed question with a
recommended default, and a way out, is what makes them feel the draft is
theirs.

## Rules

1. **One question per turn.** Never a numbered list of questions. If two
   things are unknown, ask the more consequential one first; the answer
   often settles the second.
2. **Options first, open text last.** Offer 2 to 4 options, mark one as
   recommended, and add "you decide". Open text only when any option
   would be a guess (a client's internal codename, a deadline).
3. **Propose, do not ask, whatever corpus can answer.** If `ask` surfaces
   the fitting case study, present it as the recommended option. If corpus
   has three candidate case studies, they are the options. The user never
   has to remember what the archive contains.
4. **Do not ask what the task already answers.** A pasted email gives the
   audience, register and usually the goal. A conference name gives the
   audience. Skip the slot; mention the skip only if the user might wonder.
5. **Every question carries the escape hatch in its own text**: `or say
   "draft it" and I will use the defaults`. Do not rely on the user
   knowing the phrase from an earlier turn.
6. **"You decide" or "draft it" ends the round.** Fill remaining slots with
   the recommended defaults and mark each `(default, not confirmed)`
   wherever the answers are recorded.
7. **Record every answer where the next step can see it.** Standard tier:
   one line restating the answers before the draft. Heavy tier: the
   answers are the brief.
8. **Never ask permission to do the thing that was asked.** "Shall I draft
   it now?" after the user said "write the post" is a wasted turn. Announce
   the tier and go.

## Question shape

```
<one sentence naming the decision and why it matters for this piece>

A) <option> (recommended)
B) <option>
C) <option>
D) You decide

Or say "draft it" and I will use A.
```

Example, standard tier, LinkedIn post about a completed project:

```
Who should feel this post is written for them? It sets how much I explain
versus assume.

A) Engineering leaders evaluating a partner like us (recommended)
B) Peers in the same field, for credibility
C) The client's own network, as a thank-you
D) You decide

Or say "draft it" and I will use A.
```

Example, heavy tier, proof points slot, proposed from corpus:

```
Which proof points should carry the argument? Corpus has three that fit
the audience.

A) Nordwind Logistics rollout: 40 percent faster onboarding (recommended)
B) Helix Health platform migration: zero downtime cutover
C) Both A and B
D) You decide

Or say "draft it" and I will use A.
```

## Tool mapping

Use the platform's structured-question tool when it exists; it renders as
tappable options and is easier than typing on mobile.

| Surface | Tool | Notes |
|---|---|---|
| claude.ai web, desktop, mobile | `ask_user_input_v0` (tappable options) | The primary surface. Single select for tier and angle questions; multi select for proof points. Your turn ends after the call; the answer arrives as the next user message. |
| Cowork | `AskUserQuestion` when present, else `ask_user_input_v0` | Same shape. |
| No options tool in the session | Lettered list in prose | Exactly as in the question shape above. |

Whichever tool is used, the escape hatch sentence goes in the question
text, not in an option, so it is visible even when the options render as
buttons.

## Anti-patterns

| Looks like | Why it fails |
|---|---|
| "Before I start, a few questions: 1) … 2) … 3) …" | A form. Users abandon forms. |
| "Which case study would you like to feature?" with no options | Asks the user to recall the archive. Corpus knows; propose. |
| "Do you want me to draft it now?" | The task already said yes. |
| An option list with no recommended default | Forces a decision the user came here to delegate. |
| Asking the audience of a reply to a pasted email | The email answers it. |
| The escape hatch stated once at the top of the session | Not visible on the third question. Repeat it every time. |
