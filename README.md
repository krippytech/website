# KrippyTech website

Static source for [krippytech.com](https://krippytech.com), a practical IT
knowledge and consulting site covering Microsoft 365, Azure, MSP operations,
PowerShell, technical cases, and downloadable resources.

## Architecture

- Plain HTML and CSS; no application server or client-side build step.
- `index.html` and feature directories are published as static pages.
- Shared styling lives in `styles.css`.
- Authoring standards live in `docs/`.
- Non-public authoring templates belong in `.github/templates/` so they are not
  included in the GitHub Pages output.

## Deployment

GitHub Pages deploys the root of the `main` branch. The `CNAME` file configures
the custom domain `krippytech.com`, and GitHub Pages enforces HTTPS.

Changes merged to `main` are production changes. Use a pull request and wait
for the static-site validation check before merging.

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
