# Connecting to corpus

Corpus is reachable from claude.ai (web, desktop, Cowork) and from Claude
Code. Both sign in the same way: corpus is its own OAuth server, so
connecting sends you to corpus to sign in with your work Google account and
approve a consent screen. There is no token to copy.

## When a skill sends you here

A corpus skill stops and points to this file in two situations:

- The corpus tools (`ask`, `search`, `get_document`, `list_guides`, …) are
  not in the session at all: the connector is not installed or not enabled
  for this conversation.
- A corpus call fails with an auth error: the connector is installed but
  the sign-in has lapsed or access was never granted.

Fix the connection, then re-run the skill. Skills do not draft company
content without corpus, so there is nothing to resume until it is back.

## claude.ai (web, desktop, mobile)

1. Install the **corpus** plugin: Customize → Plugins → **+** → Add
   marketplace, enter the Atölye marketplace repository URL, then Install
   on corpus. On Team and Enterprise plans an owner publishes it from
   Organization settings → Plugins, so it may already be there.
2. Connect the corpus connector the plugin brings along: sign in with
   Google, then approve the consent screen.
3. Check the connector is switched on for the conversation: the **+** (or
   sliders) button in the composer lists connectors; corpus must be on
   there, not only installed in Customize.
4. If corpus says access is not enabled, ask someone with corpus admin
   access to grant it in the claude.ai column on the corpus Users page.

Without the plugin, the connector can still be added by hand under
Customize → Connectors → **+** → Add custom connector, using the corpus MCP
endpoint: the base URL plus `/mcp` (for example `https://corpus.example/mcp`),
not the bare base URL. A manual connector brings the tools but not the
skills; install the plugin for those.

## Cowork

Cowork uses the same plugin and the same connection. Open the Cowork tab,
then Customize → Plugins, and install if it is not already listed. If
corpus works in chat but not in a Cowork task, start a new task after
connecting; a running task does not pick up a new connector.

## Claude Code

Only if someone uses corpus from the terminal as well; the connection is
separate from claude.ai.

1. `/plugin marketplace add <Atölye marketplace repository URL>`, then
   `/plugin install corpus@atolye`.
2. `/mcp`, pick **corpus**, authenticate in the browser.

## Verifying the connection

Ask Claude to run `list_guides`. A connected session returns the published
guides (at minimum the `voice` guide). Three outcomes and what they mean:

| Result | Meaning | Fix |
|---|---|---|
| A list of guides | Connected and authorised | Nothing to do |
| Auth or 401 error | Connector present, sign-in lapsed | Customize → Connectors, open corpus, disconnect and reconnect |
| "access is not enabled" or 403 | Signed in, not granted | An operator grants access on the corpus Users page (claude.ai column) |
| Tool not found | Connector absent or off for this chat | Install the plugin, or enable corpus in the conversation's tools menu |

## Common problems

- **Signed in with the wrong Google account.** The consent screen accepts
  any Google account; corpus only authorises work accounts. Disconnect and
  reconnect, choosing the work account.
- **Connected on the web, missing on mobile or desktop.** The connection
  is per account and should carry over; sign out and back in on the
  device that does not see it.
- **Cowork tasks started before connecting.** Start a new task; a running
  one does not pick up a new connector.
- **Skills present, tools absent.** The plugin installed but the connector
  step was skipped or declined. Re-run the connector setup from the plugin
  page.
- **Guides missing from search.** Not a connection problem. Guides are
  served by `list_guides` and `get_guide` only; `search` covers the
  document archive.

## Getting access granted

Operators manage access in corpus admin on the Users page (people) and the
Tokens page (service tokens). Submitting guides is a separate permission
("may submit guides") on the same pages. Ask an operator for the specific
permission you are missing; the error message names it.
