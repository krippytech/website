# KrippyTech Source Lineage Register

**Version:** 1.0

## Purpose

This register records where published and planned KrippyTech knowledge came from without storing client-identifying material in public-facing content.

The goal is traceability, not exposure.

A public guide should be able to answer internally:

- Was this built from strategy/foundation material, field evidence, or both?
- Which sanitized source pack or historical batch supports it?
- Is the source strong enough to support a standalone guide?
- Are there sibling lessons from the same incidents that have not been published yet?

Do not place credentials, client names, domains, ticket numbers, phone numbers, or other identifying details in this register.

## Lineage Types

### Foundation

Built primarily from KrippyTech's approved teaching model and standard IT operating principles.

Use for broad orientation pages such as Active Directory basics, new-user setup, or the Office IT Admin Survival Guide.

### Field-Derived

Built from one or more real support incidents or operational source packs.

The public guide is sanitized and generalized, but its diagnostic path is grounded in production evidence.

### Mixed

Combines the approved KrippyTech teaching model with one or more field-derived patterns.

### Advanced / KER-Derived

Built from a deeper engineering reference that was simplified into a safe public workflow.

## Source Strength

- **Strong**: symptom + evidence + decision point + resolution/verification or meaningful escalation boundary.
- **Supporting**: reinforces an already-known pattern but is not sufficient alone.
- **Foundation**: intentionally conceptual and not dependent on one incident.

## Everyday IT Lineage Map

| Public Asset | Lineage | Sanitized / Historical Source | Strength | Notes |
|---|---|---|---|---|
| Everyday IT landing | Foundation | Everyday IT strategy and approved content hierarchy | Foundation | Front door and content-cluster index |
| Office IT Admin Survival Guide | Foundation | Approved Survival Guide modules and practical support philosophy | Foundation | Learning-path anchor |
| New User Setup | Foundation / Mixed | Approved onboarding model plus recurring field patterns | Foundation | Broad onboarding workflow |
| Active Directory | Foundation | Approved AD basics curriculum | Foundation | Safe conceptual entry point |
| Groups & Permissions | Mixed | Permissions source material and repeated access incidents | Strong | Later enhanced with Effective Access and token-refresh patterns |
| Passwords, Lockouts & MFA | Mixed | Identity troubleshooting patterns across field material | Strong | Parent for dedicated recovery/lockout follow-ups |
| Microsoft 365 & Email | Foundation / Mixed | Approved M365 support curriculum plus field patterns | Foundation | Domain anchor |
| Printers | Foundation / Mixed | Printer/scanner support material | Supporting | Broad printer workflow |
| SharePoint & OneDrive | Foundation / Mixed | SharePoint/OneDrive source packs and sync cases | Strong | Later enhanced with OneDrive icon and disk-use concepts |
| Troubleshooting & Escalation | Mixed | Repeated shared-layer troubleshooting patterns | Strong | Cross-domain decision framework |
| Outlook Profile Rebuild | Field-Derived | Outlook profile issue source material | Strong | Standalone practical rebuild workflow |
| Windows Temp Cleanup | Field-Derived | Workstation cleanup cases | Strong | Safe cleanup, not diagnosis |
| OneDrive Free Up Space | Field-Derived | OneDrive Files On-Demand disk-recovery source | Strong | Includes logical vs physical storage distinction |
| VPN Troubleshooting | Field-Derived | VPN issue source pack | Strong | Layered isolation model |
| Scanner Troubleshooting | Field-Derived | Scanner source pack | Strong | Hardware path, USB, driver, vendor software |
| Scan to Email | Field-Derived | Scanner/mail-flow source pack | Strong | Timestamp correlation and security/quarantine evidence |
| Mapped Drives & File Access | Mixed | File-access and permissions source material | Strong | Find real resource before mapping |
| VPN Works but Drive Does Not | Field-Derived | VPN issue source pack + file access lessons | Strong | Tunnel success does not prove resource access |
| Scan to Folder | Field-Derived | Scanner source pack and SMB workflow cases | Strong | Exact UNC, exact identity, exact copier test |
| Outlook vs Outlook on the Web | Field-Derived | Outlook support material | Strong | Browser success isolates the client layer |
| Office Account & Licensing Problems | Field-Derived | Office licensing / wrong-account cases | Strong | Activation as identity/ownership problem |
| New PC Setup Checklist | Mixed | Workstation setup cases plus approved onboarding model | Strong | Workflow-oriented setup |
| When to Replace a Workstation | Field-Derived | Aging workstation / scanner support case | Strong | Repair vs replace boundary |
| Former Employee Mailbox Handling | Field-Derived | Historical mailbox lifecycle and delegation cases | Strong | Preserve business data without preserving sign-in |
| Shared Mailbox Permissions | Field-Derived | Delegation and shared-mailbox access cases | Strong | Full Access vs Send As vs Send on Behalf |
| Message Trace: Prove Delivery | Field-Derived | Mail-delay and scanner-message trace cases | Strong | Evidence-first delivery isolation |
| Outlook Signature Troubleshooting | Field-Derived | Outlook/OWA signature cases | Strong | Clean test signature and internal/external comparison |
| SharePoint Sync Troubleshooting | Field-Derived | SharePoint/OneDrive sync cases | Strong | Shortcut vs true sync relationship |
| Calendar Sharing Troubleshooting | Field-Derived | Cross-tenant calendar sharing case | Strong | Identify exact tenant/policy before changing settings |
| Mobile Exchange Sync Troubleshooting | Field-Derived | Apple Mail / Exchange token-reset cases | Strong | Modern-auth re-add workflow |
| Outlook Profile Creation Fails | Field-Derived | Outlook connectivity / Autodiscover case | Strong | Step beyond normal profile rebuild |

## Active Expansion #6 Lineage

These guides are not yet counted as published in the current library map. They are included here so their source relationship is not lost during the review/merge cycle.

| Planned Asset | Primary Domain | Source Pattern | Strength |
|---|---|---|---|
| MFA Recovery Without Weakening Security | 01 Identity & Access | MFA, Conditional Access, sign-in, recovery patterns | Strong |
| Recurring Account Lockout Troubleshooting | 01 Identity & Access | repeated lockout / stale credential patterns | Strong |
| Shared Mailbox Not Showing in Outlook | 02 Microsoft 365 & Email | delegation, propagation, Outlook visibility patterns | Strong |
| Access Denied After a Group Change | 01 Identity & Access | Effective Access, group membership, token refresh, NTFS/SMB | Strong |

## Strong Unpublished Lineage

### Restrict an Inherited Network Folder Safely

Primary domain: `07 File Servers & SMB`

Lineage: Advanced / KER-Derived with strong field grounding.

Source strength: **Strong**.

Preserved lessons:
- confirm the approved-user list with the data owner
- record ACLs before changing them
- preserve administrative and service access
- add the approved security group before breaking inheritance
- convert inherited entries instead of deleting everything
- avoid broad explicit Deny entries
- verify both approved and unapproved users
- account for share + NTFS effective permissions
- refresh user access tokens after group changes
- define rollback and escalation boundaries

Recommended asset: Everyday IT standalone guide with a deeper KER companion.

### Failing Disk: Protect Data Before Rebuilding

Primary domain: `04 Windows & Workstations`

Lineage: Field-Derived / KER candidate.

Source strength: **Strong enough for development**, with final technical wording to be validated during drafting.

Preserved lessons:
- determine backup/data state first
- prioritize preservation over repeated repair attempts
- use disk-health evidence where appropriate
- avoid unnecessary heavy writes/reboots on a suspected failing disk
- do not begin an OS rebuild until data safety is known
- define the repair/replacement escalation boundary

Recommended asset: Everyday IT standalone guide plus optional KER recovery reference.

### SPF / DMARC / Direct Send Failure Pattern

Primary domain: `10 Advanced / KER` with secondary relationship to `02 Microsoft 365 & Email`.

Lineage: Scanner/mail-flow incidents.

Source strength: **Strong technically, but publication requires current vendor verification**.

Recommended asset: KER / advanced reference first.

### SMTP Authentication Identity for Devices

Primary domain: `10 Advanced / KER` with secondary relationship to `06 Printers Scanners & MFP`.

Lineage: Scanner authentication incidents.

Source strength: **Strong**, but exact Microsoft guidance is time-sensitive.

Status: **Blocked pending current Microsoft verification** before an exact public procedure is written.

## Source Sibling Rule

When several lessons come from one incident, keep them linked internally even when they become separate public pages.

Examples:

- scanner delay incident → Scan to Email + Message Trace + quarantine/security lesson + future SMTP identity guidance
- Outlook incident → Outlook vs Web + Profile Rebuild + Profile Creation Fails
- file access incident → Groups & Permissions + Mapped Drives + Access Denied After Group Change + inherited-folder restriction
- VPN incident → VPN Troubleshooting + VPN Works but Drive Does Not + advanced remote-access dependency reference

This allows one real incident to become a knowledge cluster without repeatedly mining the raw source.

## Maintenance Rule

Whenever a new asset is created from field material:

1. add or update its lineage record
2. identify the source type and source strength
3. record sibling lessons when useful
4. keep identifying material in the private raw layer only
5. mark time-sensitive vendor procedures as blocked until verified
6. never weaken the privacy standard for the sake of traceability

The lineage register should make it possible to improve a guide later without asking where the original engineering lesson came from.
