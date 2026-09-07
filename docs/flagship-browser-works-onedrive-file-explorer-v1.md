# Flagship: Browser Works, OneDrive/File Explorer Does Not

## Purpose

Create a distinct Search Control asset for the SharePoint / OneDrive cluster that owns the troubleshooting intent where the user can access the exact SharePoint or OneDrive content in the browser, but File Explorer or the OneDrive sync client does not present or update the same content correctly.

This page must not replace the broad SharePoint & OneDrive authority page or duplicate the existing sync-repair page.

## Intent separation

- `/everyday-it/sharepoint-onedrive/` remains the broad authority for SharePoint / OneDrive basics, access, sync concepts, and common complaints.
- `/everyday-it/browser-works-onedrive-file-explorer-does-not/` owns the comparison-driven diagnostic moment: browser is known-good, local File Explorer / OneDrive path is not.
- `/everyday-it/sharepoint-sync-troubleshooting/` remains the specific repair branch for shortcut vs Sync relationships, disconnected folders, re-sync, and duplicate relationship cleanup.

## Locked principle

**If the exact content works in the browser, do not restart with permissions. Use the browser as the known-good source and isolate the local sync path.**

## Locked decision path

**Browser → Account → Relationship → Client state → Local path → Next test**

## Required substance

The page should:

- prove the exact cloud resource works online, not merely that the user can reach SharePoint home
- compare the browser identity with the OneDrive client identity
- distinguish SharePoint library Sync, Add shortcut to OneDrive, stale disconnected folders, and local copies
- capture OneDrive state before changing it
- interpret missing, stale, duplicate, partial, or pending local content as evidence
- protect unsynced local work before unlink/reset/re-sync
- explain when a clean re-sync is justified
- verify the user's real File Explorer workflow after repair

## Safety boundary

Do not encourage:

- permission changes merely because File Explorer is broken when the same content works online
- unlinking OneDrive as the first diagnostic step
- deleting duplicate folders based on names alone
- broad tenant or OneDrive policy changes as endpoint troubleshooting
- reset/re-sync without first proving what exists in the cloud and what may still exist only locally

Escalate or move into experienced administration when the issue involves tenant-wide policy, privileged configuration, large library restructuring, unclear data preservation, or broad endpoint behavior.

## Production integration for Jazzy

- Add a meaningful card to the Everyday IT landing page near SharePoint / OneDrive content.
- Add the route to `sitemap.xml` exactly once.
- Add validator expectations for exact title, social description, canonical, and article type.
- Add a prominent inbound link from `/everyday-it/sharepoint-onedrive/`, ideally from the existing browser-vs-Explorer section or Next Test section.
- Add a restrained inbound link from `/everyday-it/sharepoint-sync-troubleshooting/` back to the diagnostic page when the technician has not yet proved the local relationship is the failing layer.
- Preserve `/everyday-it/sharepoint-sync-troubleshooting/` as the repair-specific branch.
- Add other inbound links only where they genuinely improve the troubleshooting graph.
- Preserve navigation, favicons, accessibility, heading structure, encoding, fragments, and final newline.
- Run full static-site validation.

## Do not add yet

- no printable/downloadable derivative
- no separate duplicate-sync flagship page in this PR
- no broad SharePoint authority rewrite unless a small integration edit is necessary
