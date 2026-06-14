# Overleaf Paper

Overleaf Paper is a portable paper-writing skill/plugin for Codex and Claude. It helps AI agents work with academic manuscripts stored in Overleaf Git projects, edit LaTeX locally, and check Journal of Systems and Software (JSS) writing and formatting requirements.

It provides:

- Overleaf Git workflows for clone, pull, status, commit, push, and sync.
- A JSS writing and formatting checklist for manuscripts.
- A lightweight LaTeX checker for highlights, keywords, structure, figures, tables, and acknowledgements.
- A Codex Desktop marketplace plugin package.
- A Claude-compatible skill package.

## Install Or Update

Use the same commands for first install and update:

```text
/plugin marketplace add hhhwwwuuu/overleaf-paper-skill
/plugin install overleaf-paper
```

Claude reads the marketplace entry from:

```text
.claude-plugin/marketplace.json
```

The GitHub repository is:

```text
https://github.com/hhhwwwuuu/overleaf-paper-skill
```

After updating, start a new Codex or Claude chat so the latest skill instructions are loaded.

## Install In Codex Desktop

In Codex Desktop, install this repository as a custom plugin marketplace:

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

A token is required if you want the agent to pull from or push to Overleaf Git. Set it as an environment variable and restart Codex or Claude:

```powershell
setx OVERLEAF_GIT_TOKEN "<your-overleaf-git-token>"
```

Overleaf Git uses username `git`; the password is your Overleaf Git authentication token. Never commit the token to this repository.

## Use In Codex

Recommended direct invocation:

```text
Use $overleaf-paper to pull my Overleaf project and check it for JSS requirements.
```

Supported aliases:

| Alias | Purpose |
|---|---|
| `overleaf-pull` | Clone or pull an Overleaf Git project. |
| `overleaf-edit` | Edit local LaTeX manuscript files. |
| `overleaf-jss-check` | Check JSS writing and formatting requirements. |
| `overleaf-sync` | Inspect diff, commit, and prepare a safe push. |
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
| `/overleaf-pull` or `overleaf-pull` | Clone or pull an Overleaf Git project. |
| `/overleaf-edit` or `overleaf-edit` | Edit local LaTeX manuscript files. |
| `/overleaf-jss-check` or `overleaf-jss-check` | Check JSS writing and formatting requirements. |
| `/overleaf-sync` or `overleaf-sync` | Inspect diff, commit, and prepare a safe push. |
| `/overleaf-push` or `overleaf-push` | Push to Overleaf after explicit user approval. |

## Safety Notes

- Pull before editing.
- Inspect diffs before committing or pushing.
- Push only when the user explicitly asks or approves.
- Do not force-push unless the user understands the history rewrite.
- Do not store Overleaf tokens in Git URLs, files, logs, prompts, or manuscript repositories.
- Be careful with Overleaf comments, review mode, and track changes because Git sync may not preserve editor-only metadata as expected.