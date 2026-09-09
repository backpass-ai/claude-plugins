# corpus plugin

Drafts company-facing content in the company's voice, with every company
fact traced to a document in corpus.

## Skills

| Skill | Role | Ends with |
|---|---|---|
| `using-corpus` | Entry point. Sizes the job (light, standard, heavy), grounds in corpus, drafts. Holds the shared references. | A draft with `Needs your input` and `Sources` |
| `brief` | Heavy tier, step 1. Audience, key message, outcome, proof points, tone. One question at a time. | An approved brief, saved to `briefs/` |
| `outline` | Heavy tier, step 2. Sections, budgets, corpus documents per section. | An approved outline, saved next to the brief |
| `review` | Heavy tier, step 4 (after drafting). Draft vs brief, outline, voice guide, provenance. Findings by severity. | A findings report; fixes only for what the user picks |
| `add-guide` | Turns something from the conversation into a pending corpus guide. | A pending draft for an operator to publish |

Flow for heavy work: `using-corpus` → `brief` → `outline` → `using-corpus`
(draft) → `review`. Light and standard stay inside `using-corpus`.

## Layout

```
corpus/
├── .claude-plugin/plugin.json      plugin manifest
├── .mcp.json                       corpus MCP server (connector URL)
├── README.md
├── skills/
│   ├── using-corpus/
│   │   ├── SKILL.md
│   │   └── references/
│   │       ├── connecting.md       how to connect, verify, fix
│   │       ├── elicitation.md      how every skill asks questions
│   │       ├── tiers.md            sizing rules, signals, worked examples
│   │       └── output-contract.md  delivery format, examples per tier
│   ├── brief/SKILL.md
│   ├── outline/SKILL.md
│   ├── review/SKILL.md
│   └── add-guide/SKILL.md
└── evals/
    ├── README.md
    ├── trigger/                    should-trigger / should-not-trigger sets, one per skill
    └── behavior/evals.json         end-to-end prompts with assertions
```

Shared references live under `using-corpus/references/` because that skill
is the entry point and always installed. The other skills refer to them in
prose ("the using-corpus skill's references/elicitation.md, next to its
SKILL.md") rather than by absolute path, because claude.ai mounts skills
under a `plugin:skill` name and the mount root differs between surfaces.

## Setup (claude.ai)

1. Publish: Organization settings → Plugins (Team and Enterprise), or have
   members add the marketplace repository URL under Customize → Plugins →
   **+** → Add marketplace.
2. Connect: see `skills/using-corpus/references/connecting.md`.

This repository is a marketplace with one plugin. The marketplace catalog
is `.claude-plugin/marketplace.json` at the repo root; the plugin lives
under `plugins/corpus/`. Skills are namespaced as `corpus:<skill>` once
installed, so `/corpus:using-corpus`, `/corpus:brief` and so on.

## Persistence

claude.ai keeps no files between conversations. The brief and outline are
canonical as approved blocks in the transcript; the skills also present
them as downloadable files and offer to save them to Google Drive when
that connector is connected (which also makes them findable by corpus).

## Testing

See `evals/README.md`. Trigger evals run from your machine against the
API with `evals/run_trigger.py`. Behavior evals run by hand in claude.ai
with the scoresheet in `evals/behavior/scoresheet.md`.
