# Atölye Claude plugins

Internal plugin marketplace for claude.ai and Claude Code. The same
`marketplace.json` serves both: claude.ai syncs it from this repository
(Organization settings → Plugins), Claude Code adds it as a marketplace.

## Install

### claude.ai

Customize → Plugins → **corpus**. On Team and Enterprise plans an owner
publishes it from Organization settings → Plugins, so it may already be
installed. Connect the bundled corpus connector: sign in with your work
Google account and approve the consent screen.

### Claude Code

```
/plugin marketplace add backpass-ai/claude-plugins
/plugin install corpus@atolye
```

Then run `/mcp`, select **corpus** and authenticate — it opens the same Google
sign-in and consent screen. `/mcp` should now list **corpus** as connected.
Enable auto-update for the marketplace under `/plugin` → Marketplaces so
plugin updates arrive on their own.

If corpus says access is not enabled, ask someone with corpus admin access to
grant it in the claude.ai column on the corpus Users page.

## Plugins

### corpus

- Connects the corpus knowledge service over MCP
  (`https://corpus-production-22c2.up.railway.app/mcp`), authenticated by
  OAuth against corpus itself.
- `/using-corpus <request>` — draft any company-facing content (emails, job
  postings, proposal sections, posts) grounded in the corpus archive instead
  of invented facts. Example:

  ```
  /using-corpus write me a draft job posting for our new system designer position
  ```

## Releasing

claude.ai re-syncs the marketplace when a pull request that bumps a plugin's
`version` (in `plugins/<name>/.claude-plugin/plugin.json`) is merged to
`main`. Bump the version in every PR that changes a plugin; without it the
change does not reach claude.ai.
