# KT-000005 - Folder Access Was Wrong Because NTFS Inheritance

## Purpose

Add the proof-layer case for the File Server / SMB / NTFS cluster.

This is a public-safe technical case based on a real permissions change where a child folder beneath a broader SMB share inherited Modify access from its parent, leaving a broad group with more access than the business intended.

## Route

`/cases/KT-000005/`

## Locked lesson

**Do not change both share and NTFS permissions just because the symptom is access-related. Prove which layer actually controls the result.**

## Investigation path

**Exact folder -> Share layer -> NTFS layer -> Inheritance -> Effective Access -> Safe change -> Verify both sides**

The case should reinforce, not replace, the flagship decision path:

**Path -> Identity -> Share -> NTFS -> Effective Access -> Verify**

## Evidence boundary

The source record supports these facts:

- The target was a child folder beneath a broader SMB share.
- A broad group had Modify access through NTFS inheritance from the parent.
- The inherited entry could not be treated like an isolated explicit child-folder ACE.
- The SMB share itself was not identified as the faulty layer.
- Effective Access was checked for an approved and unapproved user.
- Administrative and SYSTEM access were preserved.
- A dedicated security group was used for approved users.
- The approved group was granted Modify before broad access was removed.
- Inherited permissions were converted to explicit entries before cleanup.
- Only the unwanted broad entry was removed.
- Child propagation was limited to approved scope.
- Verification included approved-user Modify behavior, unapproved-user denial, admin/SYSTEM retention, and dependent workflow checks.

Do not rewrite this as a generic Access Denied incident if the evidence does not support that symptom. The actual proof is that the permission model was wrong at the NTFS inheritance layer.

## Intent separation

- `/everyday-it/groups-permissions/` remains broad authorization authority.
- `/everyday-it/share-permissions-vs-ntfs-permissions/` remains the diagnostic flagship for separating permission layers.
- `/everyday-it/restrict-inherited-folder-permissions/` remains the safe inheritance-change guide.
- `/cases/KT-000005/` is proof: it shows how the layer was identified and the change was performed safely.

## Production integration for Jazzy

- Add KT-000005 to `/cases/` immediately after KT-000004.
- Add `/cases/KT-000005/` to `sitemap.xml` exactly once.
- Add validator coverage for exact title, social description, canonical, `article` type, approved author markup, and publication-date markup.
- Add a restrained proof/case link from `/everyday-it/share-permissions-vs-ntfs-permissions/`.
- Add a restrained case link from `/everyday-it/restrict-inherited-folder-permissions/` if the graph remains clean.
- Preserve all public-safe sanitization.
- Preserve the evidence boundary that NTFS inheritance, not the SMB share, was the identified layer.
- Do not add a downloadable derivative.
- Run full static-site validation.

## Review rule

Do not convert this into a generic permissions tutorial or invent an Access Denied root cause. The proof value is the real-world separation of share vs NTFS, identification of inheritance, preservation of known-good access, and verification of both allowed and denied users.
