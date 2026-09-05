# Everyday IT Library Map

**Version:** 1.0

## Purpose

This register maps the existing Everyday IT library into KrippyTech Content Architecture v1.

It is the working inventory for published guides. It answers:

- What has already been published?
- Which primary domain owns each guide?
- Which tags describe it?
- What naturally links to it?
- Which parts of the library are dense, thin, or ready for deeper follow-up?

The public site does not need to expose this taxonomy. This is an internal operating map.

## Status Key

- **Published**: merged into the publishing branch and represented in the current route inventory.
- **Foundation**: broad entry-point or learning-path page rather than a single troubleshooting symptom.
- **Pending expansion**: approved or actively developed work not yet part of this published inventory.

## Current Everyday IT Inventory

| Route | Primary Domain | Tags | Role | Natural Relationships |
|---|---|---|---|---|
| `/everyday-it/` | Cross-domain | Everyday IT, Helpdesk, Troubleshooting | Foundation | Office IT Admin Survival Guide, all domain guides |
| `/everyday-it/office-it-admin-survival-guide/` | Cross-domain | Helpdesk, New Users, AD, Microsoft 365, Troubleshooting | Foundation | New User Setup, Active Directory, Groups & Permissions, Microsoft 365 & Email, Troubleshooting & Escalation |
| `/everyday-it/new-user-setup/` | 01 Identity & Access | Users, Onboarding, Active Directory, Microsoft 365, Access | Published | Active Directory, Groups & Permissions, New PC Setup |
| `/everyday-it/active-directory/` | 01 Identity & Access | Active Directory, Users, OUs, Groups | Published | Groups & Permissions, Passwords MFA, New User Setup |
| `/everyday-it/groups-permissions/` | 01 Identity & Access | Groups, Permissions, Effective Access, NTFS, Access Token | Published | Active Directory, Mapped Drives & File Access, Access Denied After Group Change |
| `/everyday-it/passwords-mfa/` | 01 Identity & Access | Passwords, MFA, Lockouts, Conditional Access, Authentication | Published | Mobile Exchange Sync, VPN Troubleshooting, MFA Recovery, Recurring Lockouts |
| `/everyday-it/access-denied-after-group-change/` | 01 Identity & Access | Active Directory, Groups, Effective Access, Access Token, NTFS, SMB | Published | Groups & Permissions, Mapped Drives & File Access |
| `/everyday-it/mfa-recovery/` | 01 Identity & Access | MFA, Identity Verification, Recovery, Temporary Access Pass, Escalation | Published | Passwords, Lockouts & MFA, Mobile Exchange Sync |
| `/everyday-it/recurring-account-lockout/` | 01 Identity & Access | Account Lockout, Stale Credentials, Services, Saved Sessions, Evidence | Published | Passwords, Lockouts & MFA, Active Directory |
| `/everyday-it/microsoft-365-email/` | 02 Microsoft 365 & Email | Microsoft 365, Exchange Online, Outlook, Licensing, Mail Flow | Published | Outlook vs Web, Shared Mailbox Permissions, Message Trace, Office Account Licensing |
| `/everyday-it/outlook-profile-rebuild/` | 02 Microsoft 365 & Email | Outlook, Profiles, Cache, Mailbox | Published | Outlook vs Web, Outlook Profile Creation Fails |
| `/everyday-it/outlook-vs-web/` | 02 Microsoft 365 & Email | Outlook, OWA, Isolation, Client Troubleshooting | Published | Outlook Profile Rebuild, Outlook Profile Creation Fails, Message Trace |
| `/everyday-it/office-account-licensing/` | 02 Microsoft 365 & Email | Office, Licensing, Identity, Activation | Published | Microsoft 365 & Email, Outlook vs Web |
| `/everyday-it/former-employee-mailbox/` | 02 Microsoft 365 & Email | Shared Mailbox, Offboarding, Mailbox Lifecycle, Delegation | Published | Shared Mailbox Permissions, Microsoft 365 & Email |
| `/everyday-it/shared-mailbox-permissions/` | 02 Microsoft 365 & Email | Shared Mailbox, Full Access, Send As, Send on Behalf | Published | Former Employee Mailbox, Shared Mailbox Not Showing in Outlook |
| `/everyday-it/shared-mailbox-not-showing/` | 02 Microsoft 365 & Email | Shared Mailbox, Delegation, Propagation, Auto-Mapping, Outlook | Published | Shared Mailbox Permissions, Outlook vs Web |
| `/everyday-it/message-trace-delivery/` | 02 Microsoft 365 & Email | Exchange Online, Message Trace, Delivery, Mail Flow | Published | Scan to Email, Microsoft 365 & Email |
| `/everyday-it/outlook-signature-troubleshooting/` | 02 Microsoft 365 & Email | Outlook, OWA, Signatures, HTML, Mail Flow | Published | Outlook vs Web, Microsoft 365 & Email |
| `/everyday-it/calendar-sharing-troubleshooting/` | 02 Microsoft 365 & Email | Calendar, Sharing Policy, Exchange, Tenants | Published | Microsoft 365 & Email, Shared Mailbox Permissions |
| `/everyday-it/mobile-exchange-sync/` | 02 Microsoft 365 & Email | Apple Mail, Exchange, OAuth, MFA, Tokens | Published | Passwords MFA, Outlook vs Web |
| `/everyday-it/outlook-profile-creation-fails/` | 02 Microsoft 365 & Email | Outlook, Profiles, Autodiscover, Credentials, Connectivity | Published | Outlook Profile Rebuild, Outlook vs Web, Office Account Licensing |
| `/everyday-it/sharepoint-onedrive/` | 03 SharePoint & OneDrive | SharePoint, OneDrive, Sync, Sharing, Files On-Demand | Published | OneDrive Free Up Space, SharePoint Sync Troubleshooting |
| `/everyday-it/onedrive-free-up-space/` | 03 SharePoint & OneDrive | OneDrive, Files On-Demand, Disk Space, Sync | Published | SharePoint & OneDrive, Windows Temp Cleanup |
| `/everyday-it/sharepoint-sync-troubleshooting/` | 03 SharePoint & OneDrive | SharePoint, OneDrive, Sync, Shortcuts, File Explorer | Published | SharePoint & OneDrive, OneDrive Free Up Space |
| `/everyday-it/windows-temp-cleanup/` | 04 Windows & Workstations | Windows, Disk Space, Temp Files, Cleanup | Published | OneDrive Free Up Space, When to Replace a Workstation |
| `/everyday-it/new-pc-setup/` | 04 Windows & Workstations | Windows, Onboarding, Applications, Peripherals, Identity | Published | New User Setup, Printers, SharePoint & OneDrive |
| `/everyday-it/when-to-replace-workstation/` | 04 Windows & Workstations | Performance, Hardware, Disk, Replacement | Published | Windows Temp Cleanup, Scanner Troubleshooting, New PC Setup |
| `/everyday-it/vpn-troubleshooting/` | 05 Remote Access & VPN | VPN, Gateway, Reachability, Credentials, MFA | Published | VPN Works but Drive Does Not, Passwords MFA |
| `/everyday-it/vpn-mapped-drive/` | 05 Remote Access & VPN | VPN, SMB, DNS, Mapped Drives, File Server | Published | VPN Troubleshooting, Mapped Drives & File Access |
| `/everyday-it/printers/` | 06 Printers, Scanners & MFP | Printers, Drivers, Ports, PCL, PostScript | Published | Scanner Troubleshooting, New PC Setup |
| `/everyday-it/scanner-troubleshooting/` | 06 Printers, Scanners & MFP | Scanner, USB, Drivers, Vendor Software, Hardware | Published | Scan to Folder, Scan to Email, When to Replace a Workstation |
| `/everyday-it/scan-to-email/` | 06 Printers, Scanners & MFP | Scan to Email, SMTP, Message Trace, Quarantine, MFP | Published | Message Trace, Scanner Troubleshooting |
| `/everyday-it/scan-to-folder/` | 06 Printers, Scanners & MFP | Scan to Folder, SMB, UNC, Permissions, MFP | Published | Scanner Troubleshooting, Mapped Drives & File Access |
| `/everyday-it/mapped-drives-access/` | 07 File Servers & SMB | Mapped Drives, UNC, SMB, NTFS, Permissions | Published | Groups & Permissions, VPN Works but Drive Does Not, Scan to Folder |
| `/everyday-it/troubleshooting-escalation/` | Cross-domain | Troubleshooting, Isolation, Escalation, Shared Failure Layer | Foundation | VPN, Scan to Email, Mapped Drives, Outlook vs Web |

## Domain Coverage Snapshot

### 01 Identity & Access

Current strength: **Strong foundation, moderate depth**.

Published coverage includes:
- users and onboarding
- Active Directory basics
- groups and permissions
- passwords, MFA, and lockout concepts
- safe MFA recovery
- recurring account lockout isolation
- access verification after group changes

High-value deeper follow-ups:
- inherited folder restriction workflow

### 02 Microsoft 365 & Email

Current strength: **Very strong and becoming a major library pillar**.

Published coverage includes:
- Outlook isolation and profile repair
- licensing and wrong-account problems
- shared mailbox lifecycle and permissions
- shared mailbox visibility after delegation
- message trace
- signatures
- calendar sharing
- mobile Exchange sync

Potential future depth:
- mailbox restore vs delegation vs forwarding
- mail forwarding and distribution-group audit patterns
- quarantine and email-security decision logic
- archive and retention troubleshooting

### 03 SharePoint & OneDrive

Current strength: **Good practical base, room for more access and data-management depth**.

Published coverage includes:
- OneDrive vs SharePoint concepts
- sync behavior
- Files On-Demand and disk recovery
- shortcut vs true sync relationships

Potential future depth:
- browser works but File Explorer fails
- duplicate sync relationships
- large-library migration and sync boundaries
- external sharing and access troubleshooting

### 04 Windows & Workstations

Current strength: **Useful but comparatively thin**.

Published coverage includes:
- safe temp cleanup
- new PC setup
- replacement decision-making

Potential future depth:
- failing disk: protect data before rebuilding
- profile corruption and local-account cleanup
- application-specific repair decision trees
- Windows credential and token cleanup patterns

### 05 Remote Access & VPN

Current strength: **Focused and coherent**.

Published coverage includes:
- layered VPN troubleshooting
- VPN connected but resource unavailable

Potential future depth:
- remote access is more than the tunnel
- DNS/routes after VPN connection
- RDP/session-host vs endpoint isolation

### 06 Printers, Scanners & MFP

Current strength: **Strong practical workflow coverage**.

Published coverage includes:
- printers
- local scanner detection
- scan to folder
- scan to email

Potential future depth:
- printer queue/port/driver isolation
- shared printer vs local printer troubleshooting
- modern SMTP/authentication architecture for MFPs after vendor verification

### 07 File Servers & SMB

Current strength: **Good entry point, high-value gap remains**.

Published coverage includes:
- mapped drives and finding the real resource
- SMB/UNC relationships through VPN and scan-to-folder workflows

Highest-priority gap:
- **Restrict an Inherited Network Folder Safely**

That topic already has strong source material and should become a flagship File Servers & SMB guide.

### 08 Servers & Infrastructure

Current Everyday IT strength: **Intentionally light**.

This domain is better represented in advanced tutorials, Cases, Windows & Hybrid, and KER.

Everyday IT should add only clearly safe, broadly useful infrastructure topics.

### 09 Security & Incident Response

Current Everyday IT strength: **Embedded across other workflows, not yet a dedicated pillar**.

Security lessons currently appear inside:
- MFA
- scan-to-email/quarantine
- mail delivery
- account and access troubleshooting

Potential future depth:
- first response to endpoint threat alert
- quarantine vs delivery vs false positive
- safe containment and escalation boundaries

### 10 Advanced / KER

Not intended to be a public Everyday IT shelf.

Use it to hold:
- advanced infrastructure procedures
- vendor-specific engineering
- high-risk changes
- PowerShell and automation
- deep mail-flow/authentication architecture
- recovery and migration procedures

## Cross-Link Priorities

As pages are next touched, prioritize these relationships:

1. `passwords-mfa` → MFA recovery and recurring lockout guides
2. `groups-permissions` → access denied after group change and inherited folder restriction
3. `shared-mailbox-permissions` → shared mailbox not showing in Outlook
4. `vpn-troubleshooting` → VPN mapped drive
5. `mapped-drives-access` → groups permissions and VPN mapped drive
6. `sharepoint-onedrive` → SharePoint sync troubleshooting and OneDrive free-up-space
7. `scan-to-email` → message trace delivery
8. `outlook-vs-web` → profile rebuild and profile creation failure

## Expansion Guidance

Do not choose future expansions only by whichever source was mined most recently.

Prefer work that does one or more of the following:
- closes a domain gap
- strengthens an existing cluster
- creates a natural next-step link from a high-traffic guide
- converts a strong KER lesson into a safe public guide
- adds a missing troubleshooting boundary

Based on the current map, the strongest near-term additions are:

1. Restrict an Inherited Network Folder Safely
2. Failing Disk: Protect Data Before Rebuilding

Expansion #6 is published and its four identity/access and shared-mailbox routes are included in the inventory above.

## Maintenance Rule

Whenever a new Everyday IT route is merged:

1. add it to this register
2. assign one primary domain
3. add only useful retrieval tags
4. record its natural parent/next-step relationships
5. check whether an older page should link to it
6. update the domain coverage snapshot when the balance materially changes

This keeps Everyday IT operating as a connected knowledge system instead of a flat route list.
