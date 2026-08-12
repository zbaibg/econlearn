# EconLearn Quartz site

This repository keeps the Markdown vault as the source of truth and builds a Quartz 5 site in GitHub Actions.

## What gets published

- `Home.md` becomes the site home page (`index.md`).
- `Concepts/` is published as-is.
- `Economics/` is published as-is.
- `README.md` and repository/configuration files are not copied into the Quartz content directory.

## Deployment

The workflow at `.github/workflows/deploy-quartz.yml` runs on every push to `main` and can also be started manually.

It checks out Quartz 5, starts from Quartz's default configuration, sets the site title to `EconLearn`, sets the GitHub Pages base URL to `zbaibg.github.io/econlearn`, copies the vault content, builds the static site, and deploys the output with GitHub Pages.

## One-time GitHub setting

After merging this setup, open **Settings → Pages** for this repository and set **Source** to **GitHub Actions**. The expected public URL is:

`https://zbaibg.github.io/econlearn/`

## Privacy note

This repository is private. Publishing with GitHub Pages can make the generated site publicly accessible depending on the GitHub account/organization plan and Pages visibility settings. Do not enable the deployment if these notes must remain private unless the Pages access controls on the account meet that requirement.
