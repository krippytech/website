# Aki Inu Tech website

Static source for [akiinutech.com](https://akiinutech.com), a practical IT
knowledge and consulting site covering Microsoft 365, Azure, MSP operations,
PowerShell, technical cases, and downloadable resources.

## Practical GitHub resources

- [First 10 Minutes IT Troubleshooting](resources/first-10-minutes-troubleshooting/README.md) — a compact, evidence-first field method with links to the full Aki Inu Tech guide and printable worksheet.

## Architecture

- Plain HTML and CSS; no application server or client-side build step.
- `index.html` and feature directories are published as static pages.
- Shared styling lives in `styles.css`.
- Authoring standards live in `docs/`.
- Non-public authoring templates belong in `.github/templates/` so they are not
  included in the GitHub Pages output.

## Deployment

GitHub Pages deploys the root of the `main` branch. The `CNAME` file configures
the custom domain `akiinutech.com`, and GitHub Pages enforces HTTPS.

Changes merged to `main` are production changes. Use a pull request and wait
for the static-site validation check before merging.

## Pre-launch TODOs (KrippyTech → Aki Inu Tech rebrand)

Left as-is on purpose during the rebrand; confirm before the new domain goes live:

- **Contact email** — still `hello@krippytech.com` (see `contact/index.html`).
  Switch to `hello@akiinutech.com` once that mailbox is live in Cloudflare.
- **GitHub link** — still `github.com/krippytech` (see `contact/index.html` and
  the JSON-LD `sameAs` in `index.html` / `.github/scripts/validate_site.py`).
  Only repoint if an `akiinutech` GitHub account/org actually exists; the repo
  itself does not need to move for the site's branding to change.
- **Root `LICENSE` copyright holder** — still `krippytech`. Do not change
  without explicit review; this may have legal/DBA implications.

## Local preview

From the repository root, run:

```powershell
python -m http.server 8000
```

Then open `http://localhost:8000`. A local server is preferred over opening the
HTML files directly because it matches root-relative links used in production.

## Validation

The repository validation checks HTML structure, internal links, page
fragments, and basic accessibility requirements. Run it locally with:

```powershell
python .github/scripts/validate_site.py
```

The validation files are introduced by PR #6 and will be available after that
PR is merged.
