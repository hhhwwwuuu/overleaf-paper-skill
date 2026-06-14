# Overleaf Paper

Overleaf Paper is a portable paper-writing skill/plugin for Codex and Claude. It helps AI agents work with academic manuscripts stored in Overleaf Git projects, edit LaTeX locally, and check Journal of Systems and Software (JSS) writing and formatting requirements.

This project is now a pure skill package. It does not auto-register an MCP server. Overleaf operations are performed with normal Git commands documented in the offline skill references.

It provides:

- Offline Overleaf Git workflows for clone, remote setup, pull, push, and sync.
- A JSS writing and formatting checklist for manuscripts.
- A lightweight LaTeX checker for highlights, keywords, structure, figures, tables, and acknowledgements.
- A Codex Desktop marketplace plugin package.
- A Claude-compatible skill package.

## Which Install Method Should I Use?

| Environment | Install method | Notes |
|---|---|---|
| Claude Code | `/plugin marketplace add` then `/plugin install` | Uses `.claude-plugin/marketplace.json`. |
| Codex CLI | `/plugin marketplace add` then `/plugin install` | Uses the Codex marketplace entry in `.agents/plugins/marketplace.json`. |
| Codex Desktop | Add a custom marketplace from the Plugins UI | Use the GitHub URL and choose plugin `overleaf-paper`. |

The plugin name is always:

```text
overleaf-paper
```

The repository is:

```text
https://github.com/hhhwwwuuu/overleaf-paper-skill
```

Current plugin version:

```text
0.2.0
```

## Install In Claude Code

Run these commands inside Claude Code:

```text
/plugin marketplace add hhhwwwuuu/overleaf-paper-skill
/plugin install overleaf-paper
```

Then open a new Claude chat.

Claude reads the marketplace entry from:

```text
.claude-plugin/marketplace.json
```

## Update In Claude Code

Run the install commands again:

```text
/plugin marketplace add hhhwwwuuu/overleaf-paper-skill
/plugin install overleaf-paper
```

If Claude still uses an older cached version:

```text
/plugin uninstall overleaf-paper
/plugin marketplace add hhhwwwuuu/overleaf-paper-skill
/plugin install overleaf-paper
```

Then restart Claude Code and open a new chat.

## Install In Codex CLI

Run these commands inside Codex CLI:

```text
/plugin marketplace add hhhwwwuuu/overleaf-paper-skill
/plugin install overleaf-paper
```

Then start a new Codex CLI session.

Codex CLI reads the marketplace entry from:

```text
.agents/plugins/marketplace.json
```

The installable Codex plugin package lives at:

```text
plugins/overleaf-paper
```

## Update In Codex CLI

Run the install commands again:

```text
/plugin marketplace add hhhwwwuuu/overleaf-paper-skill
/plugin install overleaf-paper
```

If Codex CLI still uses an older cached version, uninstall and reinstall:

```text
/plugin uninstall overleaf-paper
/plugin marketplace add hhhwwwuuu/overleaf-paper-skill
/plugin install overleaf-paper
```

Then start a new Codex CLI session.

## Install In Codex Desktop

In Codex Desktop, install this repository from the Plugins UI as a custom marketplace:

```text
Marketplace source: https://github.com/hhhwwwuuu/overleaf-paper-skill.git
Branch/ref: main
Plugin: overleaf-paper
```

The Codex marketplace entry is defined at:

```text
.agents/plugins/marketplace.json
```

The Codex plugin package is defined at:

```text
plugins/overleaf-paper/.codex-plugin/plugin.json
```

After installation, open a new Codex chat and check that `overleaf-paper` appears in the available skills/plugins.

## Update In Codex Desktop

1. Open Codex Desktop Plugins.
2. Refresh or re-add the custom marketplace:

```text
Marketplace source: https://github.com/hhhwwwuuu/overleaf-paper-skill.git
Branch/ref: main
Plugin: overleaf-paper
```

3. Reinstall or update `overleaf-paper` from the Plugins page.
4. Open a new Codex chat.

If the old behavior is still present, remove the old plugin installation, add the marketplace again, and reinstall `overleaf-paper`.

## Install Locally During Development

Local repository root:

```text
<path-to-this-repository>
```

Codex plugin package root:

```text
<path-to-this-repository>\plugins\overleaf-paper
```

Claude skill package root:

```text
<path-to-this-repository>\claude\overleaf-paper
```
## Overleaf Token

A token is not required for writing guidance or JSS checks.

A token is required only when the user performs real Overleaf Git network operations. The skill documents the commands and authentication flow, but it does not store or manage credentials.

Overleaf Git uses username `git`; the password is your Overleaf Git authentication token. Never commit the token to this repository.

## Use In Codex

Recommended direct invocation:

```text
Use $overleaf-paper to pull my Overleaf project and check it for JSS requirements.
```

Supported aliases:

| Alias | Purpose |
|---|---|
| `overleaf-pull` | Clone or pull an Overleaf Git project using normal Git commands. |
| `overleaf-edit` | Edit local LaTeX manuscript files. |
| `overleaf-jss-check` | Check JSS writing and formatting requirements. |
| `overleaf-sync` | Inspect diff, commit, and prepare a safe Git push. |
| `overleaf-push` | Push to Overleaf after explicit user approval. |

Examples:

```text
Use $overleaf-paper: overleaf-jss-check path/to/my-paper/main.tex
```

```text
Use $overleaf-paper: overleaf-sync my local Overleaf clone after checking the diff.
```

## Use In Claude

Recommended direct invocation:

```text
Use $overleaf-paper to revise my JSS manuscript and prepare a safe Overleaf sync.
```

Claude can use the same aliases. If slash commands are supported, use slash form; otherwise use plain text:

| Alias | Purpose |
|---|---|
| `/overleaf-pull` or `overleaf-pull` | Clone or pull an Overleaf Git project using normal Git commands. |
| `/overleaf-edit` or `overleaf-edit` | Edit local LaTeX manuscript files. |
| `/overleaf-jss-check` or `overleaf-jss-check` | Check JSS writing and formatting requirements. |
| `/overleaf-sync` or `overleaf-sync` | Inspect diff, commit, and prepare a safe Git push. |
| `/overleaf-push` or `overleaf-push` | Push to Overleaf after explicit user approval. |

## Safety Notes

- Pull before editing.
- Inspect diffs before committing or pushing.
- Push only when the user explicitly asks or approves.
- Do not force-push unless the user understands the history rewrite.
- Do not store Overleaf tokens in Git URLs, files, logs, prompts, or manuscript repositories.
- Be careful with Overleaf comments, review mode, and track changes because Git sync may not preserve editor-only metadata as expected.