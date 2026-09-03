# Connecting to corpus

Corpus is reachable from claude.ai and from Claude Code. Both sign in the
same way: corpus is its own OAuth server, so connecting sends you to corpus
to sign in with your work Google account and approve a consent screen. No
token to copy.

## claude.ai (web, desktop, Cowork)

1. Install the **corpus** plugin from Customize → Plugins. On Team and
   Enterprise plans an owner publishes it from Organization settings →
   Plugins; it may already be installed for you.
2. Connect the corpus connector the plugin brings along: sign in with Google,
   then approve the consent screen.
3. If corpus says access is not enabled, ask someone with corpus admin access
   to grant it in the claude.ai column on the corpus Users page.

Without the plugin, the connector can still be added by hand under Settings →
Connectors → **Add custom connector**, using the corpus MCP endpoint — the
base URL plus `/mcp` (e.g. `https://corpus.example/mcp`), not the bare base
URL.

## Claude Code

1. `/plugin install corpus@atolye` from the Atölye plugin marketplace.
2. Run `/mcp`, pick **corpus** and authenticate — the browser opens the same
   Google sign-in and consent screen.
3. `/mcp` should now list **corpus** as connected.
