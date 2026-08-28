# Atölye Claude plugins

Internal plugin marketplace for Claude Code.

## Install

```
/plugin marketplace add <this-repo-git-url-or-local-path>
/plugin install corpus@atolye
```

Then get a corpus MCP token (ask an admin to issue one from the corpus admin UI
— it is shown once at issue time) and put it in your shell profile:

```sh
export CORPUS_MCP_TOKEN="<your token>"
```

Restart Claude Code. `/mcp` should now list **corpus** as connected.

## Plugins

### corpus

- Connects the corpus knowledge service over MCP
  (`https://corpus-production-22c2.up.railway.app/mcp`, bearer token via
  `CORPUS_MCP_TOKEN`).
- `/using-corpus <request>` — draft any company-facing content (emails, job
  postings, proposal sections, posts) grounded in the corpus archive instead
  of invented facts. Example:

  ```
  /using-corpus write me a draft job posting for our new system designer position
  ```
