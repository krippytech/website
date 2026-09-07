# Flagship Asset: Share Permissions vs NTFS Permissions

## Search Control cluster
File Server / SMB / NTFS

## New route
`/everyday-it/share-permissions-vs-ntfs-permissions/`

## Purpose
Own the practical troubleshooting question that appears after a Windows file share is reachable but access still fails or differs by user, action, or folder.

This is a decision guide, not a permissions theory page.

## Locked principle
**Access Denied does not tell you which permission layer failed. Prove the path and identity first, then separate the share layer from NTFS.**

## Locked decision path
**Path → Identity → Share → NTFS → Effective Access → Verify**

## Intent separation
- `/everyday-it/groups-permissions/` remains the broad authorization authority page.
- `/everyday-it/mapped-drives-access/` remains the broad mapped-drive/resource-identification and file-access troubleshooting page.
- `/everyday-it/share-permissions-vs-ntfs-permissions/` owns the specific share-vs-NTFS diagnostic decision.
- `/everyday-it/restrict-inherited-folder-permissions/` remains the change-safety branch for modifying inherited NTFS ACLs.
- `/everyday-it/access-denied-after-group-change/` remains the token/group-change branch.

## Required substance
The page must teach that:
- a reachable UNC path is a prerequisite before blaming permissions
- the actual user identity must be known
- SMB share permissions and NTFS permissions are separate gates
- network access cannot be more permissive than either layer allows
- local-on-server vs UNC behavior can be a useful comparison
- group membership is not identical to effective access
- newly changed group membership may require token refresh
- inheritance, explicit entries, nested groups, and Deny can change the result
- verification must test the user’s actual required action, not just read the ACL dialog

## Safety boundary
Do not recommend:
- granting Full Control at both layers as a troubleshooting shortcut
- changing share and NTFS permissions simultaneously
- breaking inheritance as a discovery step
- broad Deny rules as a quick fix
- direct-user permission sprawl
- privileged groups for ordinary access

Escalate when:
- the data owner or intended business access is unclear
- nested groups or inheritance are complex
- service/application/backup identities depend on the path
- a broad ACL change could affect production workflows

## Existing related pages to connect
Inbound candidates:
- `/everyday-it/groups-permissions/`
- `/everyday-it/mapped-drives-access/`
- `/everyday-it/restrict-inherited-folder-permissions/`
- `/everyday-it/access-denied-after-group-change/`
- `/everyday-it/vpn-mapped-drive/` only if the post-connect path is already reachable and the remaining symptom is authorization-specific

Outbound links already present in the draft:
- Mapped Drives & File Access
- Access Denied After Group Change
- Restrict Inherited Folder Permissions Safely
- Known-Good Comparison

## Jazzy production integration
1. Place the new card near Groups & Permissions / Mapped Drives in Everyday IT so the cluster reads naturally.
2. Add the canonical route to `sitemap.xml` exactly once.
3. Add validator expectations for exact title, social description, canonical, and article type.
4. Add a prominent inbound link from `groups-permissions` in the NTFS/share section or Next Test area.
5. Add a restrained inbound link from `mapped-drives-access` for the case where the UNC path works but authorization still fails.
6. Add a restrained inbound link from `restrict-inherited-folder-permissions` if it improves the share-vs-NTFS explanation without turning the page into a link farm.
7. Preserve intent separation from the existing pages above.
8. Do not add a printable/downloadable derivative in this PR.
9. Run full static-site validation.

## Production goal
The final cluster should help a reader move cleanly from:

**What is the resource? → Can I reach it? → Which identity? → Share or NTFS? → What is effective? → Did the real workflow succeed?**

No filler, no generic permission tiles, no duplicated broad authority content.
