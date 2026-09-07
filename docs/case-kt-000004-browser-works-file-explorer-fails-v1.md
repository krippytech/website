# KT-000004 - SharePoint Worked in Browser but File Explorer Was Incomplete

## Purpose

Add the proof-layer case for the SharePoint / OneDrive cluster.

This is a public-safe technical case based on a real troubleshooting record where the intended SharePoint library worked in the browser but File Explorer showed incomplete contents because a pre-existing OneDrive shortcut conflicted with the intended library sync.

## Route

`/cases/KT-000004/`

## Locked lesson

**If the exact content works in the browser, use that as the known-good source and isolate the local sync relationship.**

## Investigation path

**Browser -> Relationship type -> Conflicting shortcut -> Correct sync -> Converge -> Verify**

The case should reinforce, not replace, the flagship decision path:

**Browser -> Account -> Relationship -> Client state -> Local path -> Next test**

## Evidence boundary

The source record supports these facts:

- The intended SharePoint library worked in the browser.
- File Explorer showed incomplete library contents.
- A pre-existing OneDrive shortcut conflicted with the intended SharePoint library sync.
- The stale relationship was removed.
- Sync was started from the correct SharePoint library.
- Large sync activity could temporarily create duplicate or incomplete-looking local folders while convergence was still in progress.
- The repaired relationship was allowed to complete before verification.

Do not broaden the root cause into a generic OneDrive client failure, permissions issue, or tenant-wide problem.

## Intent separation

- `/everyday-it/sharepoint-onedrive/` remains broad SharePoint / OneDrive authority.
- `/everyday-it/browser-works-onedrive-file-explorer-does-not/` remains the diagnostic flagship for browser-vs-local failures.
- `/everyday-it/sharepoint-sync-troubleshooting/` remains the repair-specific sync relationship guide.
- `/cases/KT-000004/` is proof: it shows how browser known-good evidence led to the actual local relationship failure.

## Production integration for Jazzy

- Add KT-000004 to `/cases/` immediately after KT-000003.
- Add `/cases/KT-000004/` to `sitemap.xml` exactly once.
- Add validator coverage for exact title, social description, canonical, `article` type, approved author markup, and publication-date markup.
- Add a restrained proof/case link from `/everyday-it/browser-works-onedrive-file-explorer-does-not/`.
- Add a restrained case link from `/everyday-it/sharepoint-sync-troubleshooting/` if the graph remains clean.
- Preserve all public-safe sanitization.
- Preserve the root-cause boundary around shortcut-vs-sync relationship conflict.
- Do not add a downloadable derivative.
- Run full static-site validation.

## Review rule

Do not rewrite this as a generic sync-reset story. The useful proof is the sequence: browser worked, local relationship type was identified, conflicting shortcut was removed, intended sync was established, and convergence was verified before closure.
