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

## Phase 2 Prioritization Model

The twelve families are scored on six practical dimensions. Each dimension is scored from 1 to 5.

| Dimension | What a high score means |
|---|---|
| Existing depth | KrippyTech already has several useful, distinct supporting pages |
| Search-intent breadth | The family contains many legitimate symptom/task/decision searches |
| Differentiation | KrippyTech can say something more useful than generic vendor-summary content |
| Internal graph | Existing pages can reinforce each other naturally through links and next-step paths |
| Consulting fit | The family creates a legitimate path to paid help without forcing a sales pitch |
| Build efficiency | The cluster can become meaningfully stronger with relatively few new assets |

### Search Family Scores

| Rank | Search family | Depth | Intent | Differentiation | Internal graph | Consulting fit | Build efficiency | Total / 30 | Decision |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | Microsoft 365 and Outlook troubleshooting | 5 | 5 | 4 | 5 | 5 | 5 | **29** | Attack now |
| 2 | Identity, MFA, lockouts, groups, and access | 5 | 5 | 5 | 5 | 5 | 4 | **29** | Attack now |
| 3 | Practical IT troubleshooting methodology | 5 | 4 | 5 | 5 | 4 | 5 | **28** | Attack now |
| 4 | VPN, remote access, and mapped-drive failures | 4 | 5 | 4 | 5 | 5 | 4 | **27** | Next wave |
| 5 | SharePoint and OneDrive sync/access | 4 | 5 | 4 | 4 | 5 | 4 | **26** | Next wave |
| 6 | File server, SMB, NTFS, and permissions troubleshooting | 4 | 4 | 5 | 5 | 5 | 3 | **26** | Next wave |
| 7 | Small-business independent IT consulting | 3 | 4 | 5 | 4 | 5 | 4 | **25** | Strengthen alongside Tier 1 |
| 8 | Shared-service and server/infrastructure triage | 4 | 4 | 5 | 4 | 5 | 3 | **25** | Strengthen later |
| 9 | Security first response for small-business IT | 3 | 5 | 5 | 4 | 5 | 3 | **25** | Strengthen carefully |
| 10 | Windows workstation health and replacement decisions | 3 | 4 | 4 | 4 | 4 | 4 | **23** | Later |
| 11 | Azure and hybrid connectivity/infrastructure investigation | 3 | 4 | 5 | 3 | 5 | 2 | **22** | Build deeper authority first |
| 12 | Printer, scanner, scan-to-folder, and scan-to-email troubleshooting | 4 | 4 | 4 | 4 | 3 | 3 | **22** | Maintain, then expand selectively |

The first three topics are intentionally not chosen only by raw search breadth. They combine strong existing content, clear search intent, real troubleshooting judgment, internal linking potential, and realistic consulting relevance. That gives KrippyTech the best chance to look authoritative quickly rather than spreading effort across twelve clusters at once.

## Locked Initial Search-Control Targets

### Target 1 — Microsoft 365 and Outlook Troubleshooting

**Primary authority page:** `/everyday-it/microsoft-365-email/`

**Why this goes first:**

- already one of the deepest clusters on the site
- many distinct user searches already have dedicated routes
- naturally connects Outlook, Exchange Online, shared mailboxes, licensing, message trace, calendars, mobile sync, and profiles
- practical troubleshooting is stronger than broad Microsoft 365 marketing-style content
- strong consulting bridge for tenant cleanup, migrations, persistent mail-flow issues, and messy environments

**Initial attack queue:**

1. strengthen the authority page title/H1/meta around practical Microsoft 365 and Outlook troubleshooting without stuffing keywords
2. verify every narrow M365/Outlook guide links back to the authority page where natural
3. add a **Mailbox restore vs delegation vs forwarding** guide
4. add a **Quarantine, delivery, or false positive?** guide at safe triage level
5. add an **Archive and retention troubleshooting** guide when current Microsoft behavior is verified
6. create one sanitized Case showing a real M365 troubleshooting chain from symptom to evidence to resolution
7. create one GitHub utility/checklist that complements, rather than duplicates, a site article
8. create several concise LinkedIn field lessons that point back to the canonical guide only when useful

**Search intents to deliberately cover:**

- Microsoft 365 email troubleshooting
- Outlook works in browser but not desktop
- Outlook profile problems
- shared mailbox not showing
- Microsoft 365 wrong account or licensing issue
- email says delivered but user cannot find it
- calendar sharing not working
- Exchange sync on mobile not working
- mailbox archive or retention not behaving as expected

### Target 2 — Identity, MFA, Lockouts, Groups, and Access

**Primary authority pages:** `/everyday-it/passwords-mfa/` and `/everyday-it/groups-permissions/`

These remain a deliberate paired-authority cluster because authentication and authorization are distinct enough that forcing both into one broad page would weaken intent clarity.

**Why this goes second:**

- unusually strong overlap between AD, Entra, Microsoft 365, MFA, groups, tokens, permissions, and security
- several existing pages already answer narrow symptoms
- strong technical credibility because the cluster teaches verification and evidence rather than just password resets
- excellent bridge to real consulting work involving identity cleanup, Conditional Access, permissions review, and access-model redesign

**Initial attack queue:**

1. add a **Conditional Access failure decision tree** as the highest-priority new route
2. add a **Stale credentials and token cleanup** guide
3. add a practical **Entra ID vs Active Directory: where is this access actually coming from?** map/guide
4. add an **Offboarding access audit** checklist or guide
5. tighten cross-links among Passwords & MFA, Groups & Permissions, Active Directory, MFA Recovery, Recurring Lockout, Access Denied After Group Change, and Entra Sign-In Investigation
6. create one sanitized Case that demonstrates authentication vs authorization isolation
7. create GitHub/PowerShell support assets only where they safely help inspect or document identity state
8. use LinkedIn for short identity lessons, especially around stale sessions, group-token refresh, and proving the failing layer

**Search intents to deliberately cover:**

- MFA not working
- Microsoft 365 MFA recovery
- recurring account lockout
- access denied after group change
- group membership changed but access still denied
- Conditional Access blocking sign-in
- AD group permissions troubleshooting
- Entra ID vs Active Directory access troubleshooting
- stale credentials or stale tokens

### Target 3 — Practical IT Troubleshooting Methodology

**Primary authority page:** `/everyday-it/troubleshooting-paths/`

**Why this goes third:**

- this is the strongest KrippyTech differentiator
- competitors can reproduce click-by-click fixes more easily than a coherent diagnostic method
- the site already has the full lifecycle and enough supporting pages to behave like a true knowledge graph
- almost every future technical cluster can reinforce this one
- useful to junior admins, office IT generalists, helpdesk technicians, MSP technicians, and small-business technical owners without becoming vendor-specific

**Initial attack queue:**

1. strengthen the authority page around the full troubleshooting lifecycle
2. add a downloadable **Troubleshooting Worksheet / First 10 Minutes Checklist**
3. add symptom-to-layer examples across email, VPN, file access, printing, identity, and shared-service outages
4. create 2–3 sanitized Cases that explicitly show `Scope → Compare → Layer → Change → Verify`
5. ensure relevant technical guides link into the methodology at the correct stage instead of only linking laterally by product
6. create a compact GitHub troubleshooting checklist/template
7. use LinkedIn for short decision-framework posts rather than generic tips
8. treat this methodology as the connective tissue behind future course/training material

**Search intents to deliberately cover:**

- how to troubleshoot IT problems
- IT troubleshooting steps
- helpdesk troubleshooting process
- how to isolate an IT problem
- known-good comparison troubleshooting
- when to escalate an IT issue
- how to verify a technical fix
- workaround vs resolution
- troubleshooting checklist for IT support

## First Execution Sprint

Do not start by writing six unrelated new pages. Strengthen each winning cluster in a controlled sequence.

### Sprint A — Authority-page tune-up

Review only the three locked clusters for:

- title and H1 clarity
- meta description intent
- opening paragraph alignment
- visible route hierarchy
- internal links back from supporting guides
- Related Guides / Next Test paths
- consulting bridge placement

Do not change copy merely to insert keywords. Every edit must improve clarity for a human reader first.

### Sprint B — Three flagship new assets

Build one high-value addition for each locked family:

1. **M365:** `Mailbox restore vs delegation vs forwarding`
2. **Identity:** `Conditional Access failure decision tree`
3. **Methodology:** `Troubleshooting Worksheet / First 10 Minutes Checklist`

These three assets should be built before expanding to the rest of the gap queue because each fills a meaningful hole in one of the three priority clusters.

### Sprint C — Proof layer

Create one sanitized Case per locked family where strong source material exists:

- M365/Outlook troubleshooting chain
- authentication vs authorization / identity troubleshooting chain
- full troubleshooting lifecycle case

The Case should demonstrate decision quality, evidence, dead ends, validation, and why the final action made sense. It should not expose client information.

### Sprint D — External reinforcement

After the authority page and at least one supporting asset are strong:

- publish concise LinkedIn field lessons tied to the cluster
- add GitHub utilities/checklists only where there is genuine reusable value
- keep KrippyTech profile language consistent
- answer community questions when there is a real opportunity, linking only when the KrippyTech page materially expands the answer

Do not launch an external promotion push before the internal cluster is ready to receive traffic.

## Priority Ownership Tiers

### Tier 1: Attack now

1. Microsoft 365 and Outlook troubleshooting
2. Identity, MFA, groups, and permissions
3. Practical IT troubleshooting methodology

### Tier 1B: Strengthen immediately after the first three

1. VPN, remote access, mapped drives, and file access
2. SharePoint and OneDrive troubleshooting
3. File server / SMB / NTFS permissions
4. Small-business independent IT consulting

### Tier 2: Strengthen next

1. Security first response
2. Server and shared-service triage
3. Windows workstation health
4. Printers/scanners/MFP workflows
5. Azure and hybrid investigation

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

### Locked flagship additions

1. **Mailbox restore vs delegation vs forwarding**
   - strengthens Microsoft 365 / Outlook
   - answers a common admin decision rather than another generic mailbox guide
   - bridges naturally to consulting when mailbox lifecycle or migration state is messy

2. **Conditional Access failure decision tree**
   - strengthens Identity / MFA
   - connects Everyday IT to the existing Entra investigation tutorial
   - strong consulting bridge for risky tenant-wide policy changes

3. **Troubleshooting Worksheet / First 10 Minutes Checklist**
   - strengthens the methodology cluster
   - usable across every technical domain
   - ideal candidate for both a site download and a compact GitHub version

### High priority after the flagship three

4. **Browser works, OneDrive/File Explorer does not**
5. **Share permissions vs NTFS permissions**
6. **VPN connected, but DNS/routes/resources still fail**
7. **Quarantine, delivery, or false positive?**
8. **Workstation repair vs rebuild vs replace**

### Medium priority

- duplicate OneDrive/SharePoint sync relationships
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
4. Prioritize the flagship additions and immediate gap queue above.
5. Review title/H1/meta phrasing on the three locked Tier 1 authority clusters for clear search intent without keyword stuffing.
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
