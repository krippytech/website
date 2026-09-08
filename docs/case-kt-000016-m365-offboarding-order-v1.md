# KT-000016 Production Handoff

## Route
`/cases/KT-000016/`

## Case
**KT-000016 | Microsoft 365 Offboarding Required the Right Order**

## Category
**Microsoft 365 Identity & Offboarding**

## Status
**Access Blocked / Data Continuity Preserved**

## Locked lesson
**Offboarding is an ordered workflow. Doing the right steps in the wrong order can lose access or data.**

## Supporting principle
**Remove access without removing the business continuity the organization still needs.**

## Investigation / process path
**Authorization → Mailbox state → Block sign-in → Credential change → Mail continuity → Licensing → Endpoint handling → Verify security and continuity**

## Source evidence boundary
Supported by EX-009-09:
- same-day termination involved more than disabling a login
- termination timing and business-owner authorization were confirmed
- mailbox was converted to an appropriate retained/shared state
- interactive sign-in was blocked
- credentials were changed
- unneeded licensing was removed
- required mailbox access or forwarding was preserved for business continuity
- endpoint handling was coordinated separately
- verification includes blocked sign-in, retained mailbox availability to authorized users, approved forwarding/delegation, dependency-aware license removal, and separately controlled endpoint wipe/reassignment

Do not claim:
- every organization must follow one universal offboarding sequence
- every mailbox must become shared
- every termination requires forwarding
- license removal can occur before dependent data/services are accounted for
- endpoint wipe is part of the same identity action
- the source proves tenant-specific retention, legal-hold, OneDrive, device-management, or HR requirements beyond what is documented

## Production integration requested
- place KT-000016 immediately after KT-000015 on `/cases/`
- add sitemap route exactly once
- add validator coverage for exact title, social description, canonical behavior, article type, approved author markup, publication-date markup, locked lesson, supporting principle, path, status, Cases placement, sitemap uniqueness, and required links
- add restrained inbound proof link from `/everyday-it/mailbox-restore-delegation-forwarding/`
- add restrained inbound proof link from `/everyday-it/change-safety-rollback/` or `/everyday-it/verify-before-close/` if the graph remains clean
- preserve outbound links to Passwords & MFA, Mailbox Restore Delegation and Forwarding, Change Safety and Rollback, Verify Before Close
- keep as real offboarding proof, not a generic termination checklist or HR guide
- preserve distinction between access removal and data/mail continuity
- preserve distinction between identity/mailbox actions and endpoint handling
- no downloadable derivative
- run full static-site validation

## Report back
- exact changes
- Cases placement
- sitemap result
- validator coverage
- inbound/outbound links
- proof-layer integrity
- access-removal vs continuity boundary
- identity/mailbox vs endpoint boundary
- validation results
- blockers
- Ready-for-Review status

Keep Draft. Do not merge.
