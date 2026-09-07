# First 10 Minutes IT Troubleshooting Worksheet - Download Asset v1

Status: Draft integration handoff

## Asset

Canonical download file:

`/downloads/guides/first-10-minutes/KrippyTech-First-10-Minutes-Troubleshooting-Worksheet.pdf`

Format: one-page landscape Letter PDF, designed for printing and handwriting during live troubleshooting.

## Locked principle

**The first 10 minutes should reduce uncertainty, not create more variables.**

## Locked worksheet sequence

**Symptom -> Time -> Scope -> Known-good -> Layer -> Evidence -> Next test -> Safety/Rollback -> Verify -> Escalate**

## Worksheet purpose

The worksheet is the reusable field companion to:

- `/everyday-it/troubleshooting-first-10-minutes/`
- `/everyday-it/troubleshooting-paths/`

It should not replace either canonical web guide. The web pages own the explanatory search intent; the PDF is the practical reusable derivative.

## Safety boundary

Preserve the worksheet's evidence-first, change-light framing. Do not add language that encourages blanket password or MFA resets, broad security exclusions, blind permission copying, casual shared-infrastructure restarts, destructive repair, or simultaneous reset/rebuild actions as first-line discovery.

The STOP line at the bottom is intentional and should remain conceptually intact:

> STOP before changing a shared or high-risk system if you cannot explain the expected impact and rollback.

## Production integration for Jazzy

1. Add a clear PDF download CTA to `/everyday-it/troubleshooting-first-10-minutes/`.
2. Add the worksheet to `/downloads/` as a non-PowerShell practical guide/tool.
3. Update the Downloads page opening/meta copy so it no longer implies the section only contains PowerShell packages.
4. Keep the existing PowerShell package integrity language scoped to the PowerShell releases. Do not imply SHA-256/source-review requirements apply to the PDF worksheet.
5. Add natural cross-linking between the download listing and the First 10 Minutes guide.
6. Update validator coverage for the new download link/path and any changed Downloads metadata expectations.
7. Do not add the PDF to `sitemap.xml` as if it were a canonical HTML content route. The canonical search asset remains the First 10 Minutes guide page.
8. Preserve existing nav, favicons, accessibility, and page structure conventions.
9. Do not create a second HTML landing page solely for the worksheet in this PR.

## Reuse plan after merge

Potential derivatives, not part of this PR:

- GitHub README/checklist excerpt linking back to the canonical guide
- LinkedIn field-tip post built around the first 10 minutes principle
- optional DOCX/fillable version if there is real demand

Avoid duplicating the full canonical web article into external platforms.

## QA already performed on the PDF

The PDF was rendered to PNG at 180 DPI and visually inspected before repository upload.

Verified:

- one landscape Letter page
- no clipped text
- no overlapping cards
- checkboxes remain inside their sections
- footer and URLs remain printable
- all ten worksheet steps are present in the locked order
