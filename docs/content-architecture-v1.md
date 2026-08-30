# KrippyTech Content Architecture v1

**Version:** 1.0

## Purpose

This document defines how KrippyTech organizes, evaluates, develops, and reuses technical knowledge across Everyday IT, KER, tutorials, cases, downloads, MSP University, and future consulting material.

It does not replace the Vault Standard or Publishing Standard.

The Vault Standard defines privacy and engineering preservation.
The Publishing Standard defines how public technical material should read.
This architecture defines how material moves between them.

## Core Model

KrippyTech content follows one reusable knowledge pipeline:

`Raw case → Sanitized source → Extracted lesson → Content ledger → Content asset → Published → Reused`

The goal is to preserve the engineering value once, then reuse it many times without repeatedly mining the same ticket history.

## Working Registers

Content Architecture v1 is implemented through four working registers/standards:

- `docs/vault/batch-intake-standard.md` defines how source material enters the system.
- `docs/vault/content-ledger-standard.md` defines how extracted lessons are evaluated and tracked.
- `docs/everyday-it-library-map.md` maps the published Everyday IT library into domains, tags, relationships, and coverage gaps.
- `docs/vault/source-lineage-register.md` records where published and planned knowledge came from without exposing source clients.

These documents turn the architecture into an operating workflow rather than a conceptual model only.

## Content Domains

Every extracted lesson receives one primary domain.

### 01 Identity & Access

Active Directory, Entra ID, users, groups, permissions, authentication, passwords, MFA, lockouts, delegated access, identity lifecycle.

### 02 Microsoft 365 & Email

Exchange Online, Outlook, shared mailboxes, calendar, message trace, mail flow, licensing, distribution groups, email security interactions.

### 03 SharePoint & OneDrive

SharePoint sites, OneDrive, sync, Files On-Demand, sharing, storage, migration, shortcuts, document access.

### 04 Windows & Workstations

Windows troubleshooting, profiles, cleanup, application behavior, new PC setup, performance, device replacement, drivers.

### 05 Remote Access & VPN

VPN clients, gateways, MFA, remote access dependencies, DNS, reachability, mapped resources, remote-session troubleshooting.

### 06 Printers, Scanners & MFP

Printer deployment, drivers, scanners, scan to folder, scan to email, device communication, MFP workflows.

### 07 File Servers & SMB

Mapped drives, UNC paths, NTFS permissions, share permissions, inheritance, file access, storage workflows.

### 08 Servers & Infrastructure

Windows Server, Active Directory infrastructure, DNS, DHCP, Hyper-V, VMware, storage, patching, backup, replication, hardware.

### 09 Security & Incident Response

Endpoint security, Defender, SentinelOne, email security, quarantine, suspicious activity, containment, investigation, verification.

### 10 Advanced / KER

Deep engineering procedures, scripts, infrastructure references, architectural decisions, vendor-specific advanced troubleshooting, and material too specialized for Everyday IT.

A lesson may carry secondary tags, but only one primary domain. This keeps the library navigable as it grows.

## Content Layers

### Layer 1: Raw Intake

Original exports, ticket notes, field notes, screenshots, logs, and supporting material.

Rules:
- Preserve the original.
- Never publish directly.
- Treat as private.
- Do not spend time over-cleaning before extraction.

### Layer 2: Sanitized Source

A working source pack containing technically useful material with identifying information removed.

Preserve:
- symptom
- environment type
- diagnostic path
- evidence
- failed attempts when useful
- root cause
- resolution
- verification
- escalation boundary

Remove:
- customer and company identities
- domains and email addresses
- phone numbers
- credentials
- identifying device names
- ticket numbers
- confidential correspondence
- irrelevant chatter

### Layer 3: Extracted Lesson

The smallest reusable technical idea worth retaining.

Examples:
- Browser works but Outlook fails, isolate the client layer.
- A VPN connection proves the tunnel, not access to the resource.
- Group membership changes may require a refreshed Windows token.
- Message trace receive time separates copier delay from Microsoft 365 processing.

One source case may produce many extracted lessons.
Multiple source cases may support one lesson.

### Layer 4: Content Ledger

The ledger is the decision layer.

Every extracted lesson receives:
- ID
- primary domain
- title or working title
- source reference
- content type
- status
- priority
- related published material
- duplication notes
- next action

The ledger answers: Have we already covered this? Where does it belong? What should we build next?

### Layer 5: Content Assets

An extracted lesson may become one or more assets:
- Everyday IT guide
- Existing-page enhancement
- KER reference
- KT Case
- Tutorial
- PowerShell tool
- Checklist
- Download
- MSP University lesson
- Azure lab
- Consulting reference

Do not force every lesson into a standalone page.

### Layer 6: Published Knowledge

Published assets should link into the rest of the library whenever the connection is useful.

A page should not become an isolated dead end if another KrippyTech resource naturally continues the troubleshooting path.

### Layer 7: Reuse

Strong published material can later feed:
- learning paths
- downloadable checklists
- troubleshooting decision trees
- courses
- case collections
- consulting playbooks
- assessment frameworks

The public library is therefore not the end of the pipeline. It becomes structured source material for larger KrippyTech products.

## Content Type Decision Rules

### Everyday IT Standalone Guide

Use when:
- the symptom is common
- a junior or mid-level technician could act on it
- the diagnostic flow can be safely generalized
- the topic deserves its own search target

### Everyday IT Enhancement

Use when:
- the lesson strengthens an existing page
- creating another page would fragment the topic
- the reader should encounter the lesson in the existing workflow

### KER / Advanced Reference

Use when:
- the procedure is high-risk
- the environment is complex
- the material is vendor- or architecture-specific
- safe execution requires stronger prerequisite knowledge

### KT Case

Use when:
- the diagnostic story itself is valuable
- several layers were involved
- the investigation teaches engineering judgment beyond a simple procedure

### Checklist / Download

Use when:
- the value is repeatable execution
- a technician benefits from carrying the steps into live work

### MSP University / Course Material

Use when:
- several related lessons form a teachable progression
- the goal is understanding and judgment, not only problem resolution

### Consulting Reference

Use when:
- the lesson reveals a recurring business risk, cost issue, governance weakness, or architectural pattern
- the material can support assessment or advisory work without exposing source clients

## Standard Public Guide Pattern

Everyday IT guides should generally follow:

1. Quick answer
2. What the symptom tells you
3. Practical troubleshooting path
4. Common failure patterns
5. What not to do
6. Verification
7. When to escalate
8. Related guides

This complements the broader Publishing Standard rather than replacing it.

## Cross-Linking Rules

Add a related link when it answers the reader's likely next question.

Good examples:
- VPN Troubleshooting → VPN Works but Mapped Drive Does Not
- Shared Mailbox Permissions → Shared Mailbox Not Showing in Outlook
- Passwords, Lockouts & MFA → MFA Recovery Without Weakening Security
- Groups & Permissions → Access Denied After a Group Change
- SharePoint & OneDrive → SharePoint Sync Troubleshooting

Avoid linking pages merely because they share a product name.

Use `docs/everyday-it-library-map.md` as the current relationship register and update it whenever new Everyday IT routes are merged.

## Operating Principle

KrippyTech should increasingly behave like a knowledge graph, not a pile of articles.

A real incident creates lessons.
Lessons create multiple assets.
Assets connect to related assets.
Repeated patterns become learning paths and consulting frameworks.

The system should make every new batch easier to process than the previous one.
