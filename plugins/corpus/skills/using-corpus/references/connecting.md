# Connecting to corpus

Corpus is reachable two ways. Which one applies depends on where this session
is running.

## claude.ai (web, desktop, mobile)

1. Settings → Connectors → **Add custom connector**, using the corpus base URL.
   On Team and Enterprise plans an owner adds it under Organization settings →
   Connectors, and members connect individually from there.
2. Click Connect. You will be sent to corpus to sign in with your work Google
   account, then shown a consent screen.
3. If corpus says access is not enabled, ask an operator to press **Grant** in
   the claude.ai column on the corpus Users page.

## Claude Code

1. `/plugin install corpus@atolye` from the Atölye plugin marketplace.
2. Ask an operator to issue a corpus token — it is shown once, in the corpus
   admin UI — and add `export CORPUS_MCP_TOKEN="<token>"` to your shell profile.
3. Restart Claude Code and confirm `/mcp` lists **corpus** as connected.
