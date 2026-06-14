# Overleaf Git Offline Reference

Use this file as the operational source of truth when the agent has no network access. Source links are kept at the end for traceability, but the workflow below should be sufficient for normal Overleaf Git use.

## Capability And Access Requirements

- Overleaf Git integration is a premium feature on Overleaf Cloud. It is also available on Overleaf Server Pro 4.0+ when Git Bridge is enabled.
- The project owner or collaborator must have permission to access the project through Git.
- The Overleaf project behaves like a Git remote, but it is not a full general-purpose Git hosting service.
- Normal workflow: clone or add the Overleaf remote, edit locally, commit locally, then push to Overleaf.
- Always pull before editing when collaborators may have changed the online Overleaf project.

## Getting The Git URL

From the Overleaf project:

1. Open the project.
2. Select **Integrations** in the left side panel. In older UI versions, open the project **Menu**.
3. Select **Git**.
4. Copy the Git URL or the full clone command shown by Overleaf.

For Overleaf Cloud, project URLs map like this:

```text
Project URL: https://www.overleaf.com/project/<PROJECT_ID>
Git URL:     https://git.overleaf.com/<PROJECT_ID>
Clone:       git clone https://git.overleaf.com/<PROJECT_ID>
```

For Overleaf Server Pro, the URL shape is usually:

```text
Project URL: https://<SHARELATEX_SITE_URL>/project/<PROJECT_ID>
Git URL:     https://git@<SHARELATEX_SITE_URL>/git/<PROJECT_ID>
Clone:       git clone git@<SHARELATEX_SITE_URL>/git/<PROJECT_ID>
```

Use the exact URL shown by Overleaf when available; do not guess if the project is hosted on Server Pro or a managed institutional deployment.

## Authentication Tokens

Overleaf Git uses token-based authentication.

- Username: `git`
- Password: the Overleaf Git authentication token
- Tokens are generated and deleted in Overleaf Account Settings.
- The same token can access all projects available to that user through Git.
- Tokens expire after one year.
- A user can have up to 10 active tokens.
- Store tokens only in the OS credential manager or in an environment variable outside the repository.
- Never write a token into a Git URL, prompt, README, manuscript repository, log, or committed file.

Recommended local environment variable for this skill:

```powershell
setx OVERLEAF_GIT_TOKEN "<your-overleaf-git-token>"
```

Restart the agent app after setting the variable.

Optional Git credential helper:

```bash
git config --global credential.helper store
```

Only use `store` if the user accepts that credentials are saved on disk. Prefer the platform credential manager when available.

## First-Time Clone Workflow

Use this when the Overleaf project already exists and should be cloned locally.

```bash
git clone <GIT-URL> my-paper
cd my-paper
git status --short --branch
```

On the first network operation, Git may ask for credentials:

```text
Username: git
Password: <Overleaf Git authentication token>
```

After cloning:

1. Identify the main `.tex` file.
2. Check for `.gitignore`; if missing, add one that excludes generated LaTeX files such as `.aux`, `.log`, `.out`, `.toc`, `.synctex.gz`, and temporary build files.
3. Build or lint locally before pushing changes.

## Add Overleaf As A Remote To An Existing Local Paper

Use this when a local Git repository already exists and an empty Overleaf project should become the Overleaf remote.

Prepare Overleaf first:

1. Create a new blank Overleaf project.
2. Delete the default `main.tex` in Overleaf if the local project already has its own main file.
3. Copy the Overleaf Git URL from Integrations -> Git.

Then run locally:

```bash
cd my-paper
git remote add overleaf <GIT-URL>
git checkout master
git pull overleaf master --allow-unrelated-histories --rebase=false
git push overleaf master --set-upstream
```

If the local branch has a different name, push it to Overleaf's `master` branch explicitly:

```bash
git push overleaf my-branch:master
```

After pushing, open Overleaf and verify the project files appear. If Overleaf selected the wrong main document, change the main document in the Overleaf project menu.

## Regular Sync Workflow

Before local edits:

```bash
git status --short --branch
git pull --ff-only
```

After local edits:

```bash
git status --short
git diff
git add <changed-files>
git commit -m "Revise manuscript"
git push
```

If the Overleaf remote is named `overleaf` rather than `origin`:

```bash
git pull overleaf master --ff-only
git push overleaf master
```

Use small, manuscript-focused commits. Avoid bundling large file reorganizations, generated artifacts, and text edits in the same commit.

## Updating Older Remote URLs

If a local repository still uses an old password-style URL, update it to the token-compatible Overleaf Cloud URL:

```bash
cd my-paper
git remote -v
git remote set-url origin https://git.overleaf.com/<PROJECT_ID>
git remote -v
```

For a remote named `overleaf`:

```bash
git remote set-url overleaf https://git.overleaf.com/<PROJECT_ID>
```

The next pull or push will require username `git` and the token as password unless a credential helper is configured.

## Branch And History Rules

- Overleaf Git supports one linear history per project.
- The Overleaf branch is hard-coded as `master`.
- Local branches can exist, but pushes to Overleaf must target `master`, for example `git push overleaf my-branch:master`.
- Avoid force-push unless the user explicitly requests it and accepts the risk.
- When pulling unrelated histories from a newly created blank Overleaf project, use `--allow-unrelated-histories --rebase=false` as shown above.

## Commits Created By Overleaf

- Overleaf converts its internal project history into Git commits when Git needs them.
- A pull or fetch can cause Overleaf to generate a commit for the current online project state.
- A push from local Git creates a commit that future clones can see.
- Online edits by collaborators may not appear as Git commits until a Git operation requests them.

## Remote Pairing With GitHub Or Another Host

A local repository may use both GitHub and Overleaf remotes:

```bash
git remote -v
git remote add overleaf <GIT-URL>
git pull overleaf master --ff-only
git push overleaf master
```

Recommended convention:

- `origin`: GitHub/GitLab/Bitbucket
- `overleaf`: Overleaf Git URL

When synchronizing between GitHub and Overleaf, inspect `git log --oneline --decorate --graph --all` and `git diff` before pushing to either remote.

## File And Metadata Risks

- Do not rely on Git LFS or symbolic links in Overleaf projects.
- Renaming a folder through Git may leave an empty folder with the old name in Overleaf.
- A file rename is interpreted by Overleaf as delete plus create.
- Moving or renaming files with Overleaf comments or tracked changes can lose or displace metadata.
- Do not mix active Git pushing with active Overleaf comments or track changes unless the user accepts the risk.
- Large commits or many changed files can cause timeouts; split large changes into smaller commits.

## Troubleshooting

Repository not found:

- Verify the Git URL from Integrations -> Git.
- Confirm the project owner has Overleaf Git access.
- Confirm the user is owner/collaborator.

Authentication failed:

- Use username `git`.
- Use the current token as password.
- Generate a new token if the old one expired or was deleted.
- Clear stale cached credentials if Git keeps using an old password.

Rate limiting:

- Disable automatic Git polling in GUI clients.
- Run manual pull/fetch/push operations instead of frequent background polling.

Push reference failure or timeout:

```bash
git config http.postBuffer
git config --global http.postBuffer 10485760
```

If this does not help, split the commit into smaller commits. To remove the setting later:

```bash
git config --global --unset http.postBuffer
```

## Agent Operating Checklist

Before editing:

- Confirm the local path and remote name.
- Run `git status --short --branch`.
- Pull from Overleaf.
- Check whether comments or track changes are active.

Before pushing:

- Run the LaTeX/JSS checks requested by the user.
- Run `git diff` and summarize changed files.
- Commit only intentional source files.
- Ask for approval unless the user explicitly requested push/sync.
- Push to `master` on the Overleaf remote.

## Sources

- https://docs.overleaf.com/integrations-and-add-ons/git-integration-and-github-synchronization/git-integration
- https://docs.overleaf.com/integrations-and-add-ons/git-integration-and-github-synchronization/git-integration/git-integration-authentication-tokens
- https://docs.overleaf.com/integrations-and-add-ons/git-integration-and-github-synchronization/git-integration/advanced-git-operations