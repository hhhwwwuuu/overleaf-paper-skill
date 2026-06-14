# Overleaf Git Reference

Sources:

- https://docs.overleaf.com/integrations-and-add-ons/git-integration-and-github-synchronization/git-integration
- https://docs.overleaf.com/integrations-and-add-ons/git-integration-and-github-synchronization/git-integration/git-integration-authentication-tokens
- https://docs.overleaf.com/integrations-and-add-ons/git-integration-and-github-synchronization/git-integration/advanced-git-operations

## Essentials

- Overleaf Git integration is a premium feature on Overleaf Cloud and is available on Overleaf Server Pro 4.0+ when Git bridge is enabled.
- The Overleaf project can be treated as a remote Git repository: clone locally, pull online changes, push local changes back.
- For Overleaf Cloud, a project URL like `https://www.overleaf.com/project/1234567` maps to `https://git.overleaf.com/1234567`.
- Clone format: `git clone https://git.overleaf.com/1234567`.
- Authentication uses Git authentication tokens. Username is `git`; password is the token.
- The same token can access all projects available to that user through Git. Store it securely.

## Safe Sync Practice

- Pull before editing.
- Check `git status` before and after edits.
- Keep commits small and manuscript-focused.
- Avoid committing generated build clutter such as `.aux`, `.log`, `.out`, `.synctex.gz`, and temporary files.
- Push only after validation and user approval.
- If collaborators are editing in Overleaf, pull frequently and resolve conflicts locally.

## Important Limitations

- Treat Overleaf Git as effectively single-branch for normal use; push to `master` unless a user-provided workflow says otherwise.
- Do not rely on Git LFS for Overleaf projects.
- Be cautious with Overleaf comments, review mode, and track changes. Git operations may not preserve editor-only review metadata in the way users expect.
- Do not force-push unless the user explicitly asks and understands that remote history may be rewritten.
