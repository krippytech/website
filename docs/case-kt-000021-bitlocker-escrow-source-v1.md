# KT-000021 source handoff

## Case
**KT-000021 | BitLocker Recovery Key Was Missing from One Console but Present in Entra ID**

## Source
Sanitized engineering extraction: **EX-006-11 — BitLocker Recovery Key Missing from RMM but Present in Entra ID**.

## Category
Endpoint Security & Recovery

## Status
**Recovery Key Found / Boot Verified**

## Locked lesson
**An empty recovery-key field in one console does not prove the key is gone. Verify the device and check every approved escrow source.**

## Supporting principle
**Know the escrow hierarchy before a recovery event forces you to discover it under pressure.**

## Investigation path
**Recovery screen → Expected escrow source → Empty result → Device identity match → Alternate approved escrow → Key retrieval → Protected delivery → Successful boot → Escrow-gap review**

## Evidence supported by source
- A recently imaged endpoint entered BitLocker recovery.
- The expected recovery-key field in the management platform was empty.
- The endpoint was located in Microsoft Entra ID.
- The matching Entra device record contained the BitLocker recovery key.
- The key was retrieved from that approved source.
- The key was delivered through an approved protected channel.
- The user confirmed recovery succeeded.
- The secondary/expected escrow gap should be reviewed afterward.

## Evidence boundaries
Do not claim:
- Entra ID is always the authoritative BitLocker escrow source.
- Every missing key in one console will exist in another system.
- A key may be retrieved or disclosed without matching the correct device and confirming authorization.
- Any real recovery key, device identifier, user identity, or screenshot may be published.
- The case proves why the expected management platform lacked the key.

## Intent separation
- `/cases/KT-000021/` is the proof layer.
- `/everyday-it/known-good-comparison/` remains comparison methodology.
- `/everyday-it/change-safety-rollback/` remains change-safety methodology.
- `/everyday-it/verify-before-close/` remains verification methodology.
- Security first-response pages remain broader response guidance and should not be displaced by this case.

## Production integration targets
- Place KT-000021 immediately after KT-000020 on `/cases/`.
- Add `/cases/KT-000021/` to `sitemap.xml` exactly once.
- Add restrained inbound proof links only from existing relevant approved routes where the graph remains clean.
- Preserve privacy requirement: never expose real recovery keys, device IDs, user identities, or RAW screenshots.
- Add validator coverage for exact title, status, locked lesson, supporting principle, investigation path, placement, sitemap uniqueness, authorized-device match, approved escrow source, protected delivery, successful-boot verification, privacy boundary, and proof-layer positioning.
- No downloadable derivative.
