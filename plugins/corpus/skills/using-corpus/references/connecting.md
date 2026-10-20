# Connecting to corpus

Corpus is reachable from claude.ai (web, desktop, Cowork) through the corpus
gateway, one address for every company. Connecting sends you to the gateway
to sign in with your work Google account; the gateway looks up your
company from your email domain and shows a consent screen. There is no
token to copy. Personal Google accounts are refused.

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
   marketplace, enter the corpus marketplace repository URL, then Install
   on corpus. On Team and Enterprise plans an owner publishes it from
   Organization settings → Plugins, so it may already be there.
2. Connect the corpus connector the plugin brings along: sign in with
   Google, then approve the consent screen.
3. Check the connector is switched on for the conversation: the **+** (or
   sliders) button in the composer lists connectors; corpus must be on
   there, not only installed in Customize.
4. If the sign-in page says **corpus is not set up for <your domain>**, your
   company is not registered with the gateway; ask whoever runs corpus for
   your company. If a corpus call says **access is not enabled**, you are
   registered but not yet granted: your first connection created your row
   on the corpus Access page, and an operator grants you there.

## Cowork

Cowork uses the same plugin and the same connection. Open the Cowork tab,
then Customize → Plugins, and install if it is not already listed. If
corpus works in chat but not in a Cowork task, start a new task after
connecting; a running task does not pick up a new connector.

## Verifying the connection

Ask Claude to run `list_guides`. A connected session returns the published
guides (at minimum the `voice` guide). Three outcomes and what they mean:

| Result | Meaning | Fix |
|---|---|---|
| A list of guides | Connected and authorised | Nothing to do |
| Auth or 401 error | Connector present, sign-in lapsed | Customize → Connectors, open corpus, disconnect and reconnect |
| "access is not enabled" or 403 | Signed in, not granted | An operator grants access on the corpus Access page (your row appeared there on first connection) |
| Tool not found | Connector absent or off for this chat | Install the plugin, or enable corpus in the conversation's tools menu |
| "corpus is not set up for <domain>" | Company not registered with the gateway | Ask whoever operates corpus for your company to register the domain |

## Common problems

- **Signed in with the wrong Google account.** The gateway accepts any
  Google Workspace account and routes by its domain; a personal account is
  refused. Disconnect and reconnect, choosing the work account.
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

Operators manage access in corpus admin on the Access page (people and
service tokens). Submitting guides is a separate permission ("may submit
guides") on the same page. Ask an operator for the specific permission you
are missing; the error message names it.
