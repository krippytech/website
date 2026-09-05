# KrippyTech Search Control Map v1

**Status:** Internal strategy document

**Purpose:** Define the search topics KrippyTech wants to own, identify the primary authority page for each topic, map the supporting content already published, expose content gaps, connect relevant consulting intent, and identify external footprints that can reinforce the same subject without creating duplicate or competing pages.

## Core Search Strategy

KrippyTech should not try to rank for every IT phrase. The goal is to build authority around a smaller set of practical problem families where the site already has real depth, troubleshooting judgment, and hands-on credibility.

Each search family should have:

1. one clear primary page that owns the broad topic
2. supporting guides that answer narrower symptom or task searches
3. advanced tutorials/cases that demonstrate deeper technical authority
4. a natural consulting bridge only where a reader may reasonably need experienced help
5. external reinforcement that points back to the same subject family instead of creating a separate competing content strategy

The preferred pattern is:

`Broad topic authority page → specific troubleshooting guides → advanced proof/content → consulting bridge`

Do not create a second broad page when an existing page can be strengthened into the authority page.

## Search Ownership Map

| Search family to own | Primary authority page | Existing support | High-value gaps | Consulting connection | External reinforcement candidates |
|---|---|---|---|---|---|
| Practical IT troubleshooting methodology | `/everyday-it/troubleshooting-paths/` | Scope the Problem, Known-Good Comparison, Change Safety & Rollback, Verify Before Close, Escalate With Evidence, Workaround vs Resolution, Prevent Recurrence, Troubleshooting & Escalation | Layer-identification examples by symptom, troubleshooting worksheet/checklist, real sanitized case examples showing the full lifecycle | Difficult recurring problems, second-look troubleshooting, technical assessment | LinkedIn troubleshooting posts, GitHub checklists/templates, short case writeups, practical forum/Q&A participation |
| Microsoft 365 and Outlook troubleshooting | `/everyday-it/microsoft-365-email/` | Outlook vs Web, Profile Rebuild, Profile Creation Fails, Office Account Licensing, Shared Mailbox Permissions, Shared Mailbox Not Showing, Message Trace, Calendar Sharing, Mobile Exchange Sync, Signatures | Archive/retention troubleshooting, forwarding/DL audit logic, quarantine decision tree, mailbox restore vs delegation vs forwarding | Microsoft 365 cleanup, migrations, tenant/admin troubleshooting, difficult mail-flow issues | LinkedIn M365 troubleshooting posts, GitHub utilities, Microsoft-focused community answers where appropriate |
| Identity, MFA, lockouts, groups, and access | `/everyday-it/passwords-mfa/` plus `/everyday-it/groups-permissions/` as paired authorities | Active Directory, New User Setup, MFA Recovery, Recurring Account Lockout, Access Denied After Group Change, Entra Sign-In & Conditional Access Investigation | Conditional Access failure decision tree, stale-token/credential cleanup, offboarding access audit, practical Entra vs AD identity map | Identity cleanup, permissions review, MFA/Conditional Access planning, access troubleshooting | LinkedIn identity/security notes, GitHub PowerShell tools, Entra/M365 community contributions |
| SharePoint and OneDrive sync/access | `/everyday-it/sharepoint-onedrive/` | SharePoint Sync Troubleshooting, OneDrive Free Up Space, OneDrive/SharePoint Sync Investigation tutorial | Browser works but File Explorer fails, duplicate sync relationships, external sharing/access troubleshooting, large-library boundaries | SharePoint/OneDrive cleanup, migrations, sync architecture, data-location simplification | LinkedIn file-management posts, GitHub diagnostic scripts, community answers around sync symptoms |
| VPN, remote access, and mapped-drive failures | `/everyday-it/vpn-troubleshooting/` | VPN & Mapped Drive Access, Mapped Drives & File Access, Shared Service Outage Triage, DNS/AD health tutorial, Azure VM connectivity tutorial | Remote access dependency map, DNS/routes-after-VPN guide, RDP/session-host vs endpoint isolation | Remote-access redesign, recurring VPN/file-access issues, network dependency review | LinkedIn troubleshooting diagrams/posts, GitHub network utilities, technical forum answers |
| File server, SMB, NTFS, and permissions troubleshooting | `/everyday-it/mapped-drives-access/` | Groups & Permissions, Access Denied After Group Change, Restrict Inherited Folder Permissions, Scan to Folder, VPN & Mapped Drive Access | Effective Access deep-dive, share-vs-NTFS decision guide, permissions cleanup/migration checklist | File-server cleanup, access-model redesign, migrations, permission reviews | GitHub permission-audit utilities/checklists, LinkedIn file-access lessons, sanitized Cases |
| Windows workstation health and replacement decisions | `/everyday-it/when-to-replace-workstation/` with `/everyday-it/windows-temp-cleanup/` supporting | New PC Setup, Windows Temp Cleanup, Failing Disk: Protect Data First | Profile corruption decision tree, credential/token cleanup, application repair vs rebuild, workstation health checklist | Workstation modernization, refresh planning, difficult endpoint troubleshooting | LinkedIn endpoint lifecycle posts, downloadable checklist, sanitized repair/replacement cases |
| Printer, scanner, scan-to-folder, and scan-to-email troubleshooting | `/everyday-it/printers/` | Scanner Troubleshooting, Scan to Folder, Scan to Email, Message Trace Delivery | Queue/port/driver isolation, shared-vs-local printer troubleshooting, modern scan-to-email authentication architecture after vendor verification | Office workflow troubleshooting, equipment replacement, scan workflow redesign | LinkedIn office-IT tips, vendor-neutral troubleshooting checklists, sanitized Cases |
| Security first response for small-business IT | `/everyday-it/suspicious-signin-first-response/` as initial authority with `/everyday-it/malware-alert-first-response/` paired | Passwords & MFA, MFA Recovery, Entra Sign-In & Conditional Access Investigation, Escalate With Evidence, Verify Before Close | Quarantine vs delivery vs false-positive guide, safe endpoint containment checklist, privileged-account first-response guide | Security assessment, identity hardening, incident triage/second opinion, remediation planning | LinkedIn first-response guidance, GitHub evidence/checklist templates, security community participation without publishing unsafe remediation detail |
| Shared-service and server/infrastructure triage | `/everyday-it/shared-service-outage-triage/` | Server Restart Safety, DNS/AD Domain Health, DHCP Scope Capacity, Windows Server Low Disk Space, Azure VM Connectivity, Troubleshooting Paths | Service dependency mapping, server-role identification, safe maintenance/restart planning checklist, RDP/session-host isolation | Infrastructure assessment, outage troubleshooting, modernization, server/cloud planning | LinkedIn infrastructure troubleshooting posts, GitHub diagnostic tools, technical case studies |
| Azure and hybrid connectivity/infrastructure investigation | `/azure-journey/` plus `/tutorials/azure-vm-connectivity-investigation/` | Azure VM Network Path lab, DNS/AD Domain Health, Entra Sign-In investigation, Windows & Hybrid hub | Azure network troubleshooting hub, hybrid identity troubleshooting map, VM access/RDP dependency guide, practical Azure cost/cleanup review | Azure/hybrid assessment, migrations, connectivity troubleshooting, architecture review | GitHub scripts/labs, LinkedIn Azure investigation posts, Microsoft/Azure community contributions |
| Small-business independent IT consulting | `/consulting/` | About, Contact, Everyday IT, Tutorials, Cases | Defined project examples, independent technology review, migration/project examples, technology planning examples, eventual local/service-intent pages only when substantively different | This is the commercial destination | LinkedIn profile/company presence, GitHub profile/repository, consistent KrippyTech entity/profile descriptions, selected local/business profiles if maintained accurately |

## Priority Ownership Tiers

### Tier 1: Build authority now

These are the strongest combinations of existing depth, real-world credibility, internal-link potential, and consulting relevance.

1. Practical IT troubleshooting methodology
2. Microsoft 365 and Outlook troubleshooting
3. Identity, MFA, groups, and permissions
4. VPN, remote access, mapped drives, and file access
5. SharePoint and OneDrive troubleshooting
6. Small-business independent IT consulting

### Tier 2: Strengthen next

These already have useful content but need one or two stronger authority/support pieces before they should be treated as major search-control targets.

1. File server / SMB / NTFS permissions
2. Security first response
3. Server and shared-service triage
4. Windows workstation health
5. Printers/scanners/MFP workflows
6. Azure and hybrid investigation

## Canonical Ownership Rules

A broad search topic should have one canonical authority page. Narrower guides should target the specific symptom, task, or decision rather than restating the broad topic.

Examples:

- `Microsoft 365 troubleshooting` belongs to `/everyday-it/microsoft-365-email/`.
- `Outlook works in web but not desktop` belongs to `/everyday-it/outlook-vs-web/`.
- `shared mailbox not showing in Outlook` belongs to `/everyday-it/shared-mailbox-not-showing/`.
- `VPN troubleshooting` belongs to `/everyday-it/vpn-troubleshooting/`.
- `VPN connects but mapped drive does not work` belongs to `/everyday-it/vpn-mapped-drive/`.
- `how to troubleshoot IT problems` belongs to `/everyday-it/troubleshooting-paths/`.
- `server restart safety` belongs to `/everyday-it/server-restart-safety/`.

Before publishing a new page, ask:

1. Is this a materially different search intent?
2. Does an existing authority page already own the broad topic?
3. Should this be a new support page, an enhancement, a tutorial, a Case, or just a section on an existing page?
4. Which primary page will link to it, and which page will it strengthen in return?

## Consulting Bridge Rules

Consulting links should appear where the reader has crossed from routine learning into work that is complicated, risky, specialized, or time-consuming.

Good consulting bridge situations:

- a recurring problem has resisted normal troubleshooting
- a change affects shared infrastructure or many users
- a migration or redesign is being considered
- the current environment is difficult to understand or poorly documented
- security, permissions, identity, or data-loss risk is material
- a business wants an independent second opinion before spending money
- the reader understands the task but does not want to perform the risky work internally

Avoid turning every guide into a sales page. The educational content should remain useful on its own.

Preferred message:

> Learn what makes sense to learn. Hand off what should not be guessed at. Bring KrippyTech in when the work becomes complicated, risky, specialized, or time-consuming.

## External Search Reinforcement

External activity should reinforce KrippyTech's topic clusters rather than become a separate content universe.

### GitHub

Use GitHub for technical proof and reusable tools:

- PowerShell utilities
- diagnostic scripts
- checklists/templates
- lab material
- small technical examples that naturally reference a deeper KrippyTech article

Do not duplicate entire site articles into repository READMEs.

### LinkedIn

Use LinkedIn for concise field lessons and recognizable problem statements:

- short troubleshooting observations
- before/after lessons from sanitized work
- common mistakes
- decision frameworks
- links to the canonical KrippyTech guide when readers need the complete workflow

### Community participation

When participating in legitimate technical communities, answer the question first. Link to KrippyTech only when the linked page materially expands the answer.

Do not create low-value backlinks, mass-post links, or duplicate keyword-stuffed profiles.

### Entity consistency

Keep the same basic KrippyTech description, website, service model, and topic language across maintained profiles. The public identity should consistently communicate:

- practical IT guidance
- independent consulting
- Microsoft 365 / identity / cloud / hybrid infrastructure experience
- troubleshooting and project work
- teaching where appropriate rather than forcing dependency

## Immediate Content Gap Queue

The next additions should be selected because they strengthen a target cluster, not merely because a new source became available.

### High priority

1. **Conditional Access failure decision tree**
   - strengthens Identity / MFA
   - connects Everyday IT to the existing Entra investigation tutorial
   - strong consulting bridge for risky tenant-wide policy changes

2. **Browser works, OneDrive/File Explorer does not**
   - strengthens SharePoint/OneDrive
   - clear user search intent
   - natural known-good comparison example

3. **Share permissions vs NTFS permissions**
   - strengthens File Servers & SMB
   - supports mapped drives, scan-to-folder, inherited permissions, and group-change troubleshooting

4. **VPN connected, but DNS/routes/resources still fail**
   - strengthens Remote Access & VPN
   - bridges basic VPN troubleshooting to infrastructure dependency mapping

5. **Quarantine, delivery, or false positive?**
   - strengthens Security + M365 mail flow
   - should stay at safe triage/decision level

6. **Workstation repair vs rebuild vs replace**
   - strengthens Windows/workstations
   - connects failing disk, temp cleanup, replacement, and new PC setup

### Medium priority

- duplicate OneDrive/SharePoint sync relationships
- mailbox restore vs delegation vs forwarding
- shared printer vs local printer troubleshooting
- server/service dependency mapping
- privileged-account suspicious-sign-in response
- RDP/session-host vs endpoint isolation
- Azure network troubleshooting hub

## Search-Control Scorecard

Each target family can be reviewed using five questions:

| Dimension | Question |
|---|---|
| Authority page | Is there one obvious page that owns the broad query family? |
| Support depth | Are there enough narrow guides to answer common follow-up searches? |
| Internal graph | Do authority, support, tutorials, and Cases link naturally to each other? |
| Proof | Is there deeper material showing real technical experience rather than generic summaries? |
| Commercial bridge | Is there a natural, non-pushy path to Consulting when the work exceeds DIY scope? |

A topic should not be considered controlled simply because KrippyTech has one article about it.

## Phase 1 Execution Plan

1. Lock the twelve search families above as the initial ownership set.
2. Confirm one primary authority page for each family.
3. Add the Search Control family name to new-content planning and ledger decisions.
4. Prioritize the six High Priority gaps above.
5. Review title/H1/meta phrasing on Tier 1 authority pages for clear search intent without keyword stuffing.
6. Strengthen internal links from narrow guides back to their authority page where missing.
7. Add Consulting bridges only at appropriate risk/complexity boundaries.
8. Establish consistent external KrippyTech descriptions before expanding external profiles.
9. Use future search-performance data to adjust priority, not to create duplicate pages for every keyword variation.

## Maintenance Rule

Whenever a new page, tutorial, Case, or consulting asset is proposed:

1. assign it to one Search Control family
2. identify the authority page it strengthens
3. define the distinct search intent before creating a new route
4. record supporting and return links
5. identify whether it creates a legitimate consulting bridge
6. identify any external reinforcement opportunity
7. update the gap queue and ownership map when the cluster materially changes

The objective is not more pages. The objective is a smaller number of subjects where KrippyTech becomes unusually useful, connected, and recognizable.
