---
name: overleaf-paper
description: Use when an AI coding/writing agent such as Codex or Claude needs to work on academic papers in Overleaf via Git, including cloning, pulling, editing, validating, committing, and pushing Overleaf LaTeX projects; especially for Journal of Systems and Software manuscripts that must follow the JSS Guide for Authors writing and formatting requirements.
---

# Overleaf Paper

## Operating Rule

Treat Overleaf as the remote source of record and the local clone as the editable workspace. Pull before editing, inspect diffs before committing, and push only when the user explicitly asks for push/sync or clearly approves it.

## Agent Compatibility

This skill is written to be portable across Codex and Claude-style skill loaders:

- In Codex, use the plugin root and its `.codex-plugin/plugin.json`, `.mcp.json`, and MCP server.
- In Claude, package or copy the `claude/overleaf-paper` folder. Claude can use the same `SKILL.md`, references, and scripts, while Git commands may run through the user's shell or a configured MCP bridge.
- In any agent, never store credentials in the repository. Use `OVERLEAF_GIT_TOKEN` or an OS credential manager.

## Prompt Aliases

Recognize these aliases when they appear in a Codex or Claude prompt:

- `overleaf-pull` or `/overleaf-pull`: clone or pull an Overleaf Git project.
- `overleaf-edit` or `/overleaf-edit`: edit local LaTeX manuscript files.
- `overleaf-jss-check` or `/overleaf-jss-check`: check JSS writing and formatting requirements.
- `overleaf-sync` or `/overleaf-sync`: inspect diff, commit, and prepare a safe push.
- `overleaf-push` or `/overleaf-push`: push to Overleaf only after explicit approval.

Treat slash-prefixed aliases as plain-text intent when the client passes them through. If a client intercepts slash commands, tell the user to use the plain alias form.
## Resource Map

Read only the reference needed for the task. These reference files are offline operational manuals; use their local content first and treat source links as provenance only:

- `references/overleaf-git.md` for Overleaf Git URLs, token authentication, branch behavior, and sync cautions.
- `references/jss-writing-formatting.md` for Journal of Systems and Software writing and formatting checks.
- `scripts/jss_latex_check.py` for deterministic checks on highlights, keywords, manuscript structure, and common LaTeX submission risks.

## Overleaf Git Workflow

1. Identify either an Overleaf Git URL or an existing local clone path.
2. If MCP tools are available, prefer the `overleaf-git` MCP tools over ad hoc shell commands.
3. For first-time setup, clone into a user-approved local directory.
4. Before editing an existing clone, run status and pull.
5. Make scoped manuscript changes in `.tex`, `.bib`, figure, table, or supplementary files.
6. Build or lint when possible.
7. Run the JSS checker when working with a JSS LaTeX manuscript:
   `python scripts/jss_latex_check.py <path-to-main-tex>`
8. Inspect `git diff` and summarize manuscript-level changes.
9. Commit with an academic-writing message such as `Revise JSS manuscript structure`.
10. Push only after approval or an explicit user request.

Never write Overleaf authentication tokens into repository files, Git URLs, logs, or skill resources. Use `OVERLEAF_GIT_TOKEN` or the user's Git credential manager.

## JSS Manuscript Workflow

When drafting or revising for Journal of Systems and Software:

1. Read `references/jss-writing-formatting.md`.
2. Preserve the journal/template structure unless the user asks for migration.
3. Check title page, abstract, keywords, highlights, section structure, figures, tables, equations, references, data statement, acknowledgements, and declarations.
4. Keep all tables and equations editable.
5. Cite every table and figure in text.
6. Keep highlights to 3 to 5 bullet points, each at most 85 characters including spaces.
7. Keep keywords to 1 to 7 English keywords.
8. Do not number the abstract as a section.
9. Put acknowledgements before references.
10. Report unresolved issues instead of silently inventing missing ethics, funding, data, or author-contribution details.

## Validation Before Push

Before pushing to Overleaf, provide a short sync report:

- local path and remote URL host/project id when available;
- files changed;
- LaTeX build/check result;
- JSS checklist result;
- whether comments, track changes, or large files may be affected;
- commit hash if committed;
- push result if pushed.
