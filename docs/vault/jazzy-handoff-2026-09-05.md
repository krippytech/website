# Jazzy Handoff Log — September 5, 2026

**Purpose:** Canonical restart handoff for Codex/Jazzy when usage access resumes.

This file should be updated as work continues before September 5 so production review can resume without reconstructing chat history.

## Restart Order

1. Review this file first.
2. Review PR #44 and complete Expansion #6 production integration.
3. If green, Ready → Squash and merge → delete its branch.
4. Review PR #45 for Content Architecture v1 consistency/privacy boundaries.
5. If green, Ready → Squash and merge → delete its branch.
6. Review PR #46 for Strengthening Phase 1 production integration.
7. If green, Ready → Squash and merge → delete its branch.
8. Pull latest `main` before the next build.

Do not equate a merge with GitHub Pages deployment unless deployment is separately verified.

## PR #44 — Everyday IT Expansion #6

**Title:** `Expand Everyday IT identity and access troubleshooting`

**Branch:** `feature/everyday-it-expansion-6`

**Status:** Draft, awaiting Jazzy production integration/review.

### Approved content

- MFA Recovery Without Weakening Security
- Recurring Account Lockout Troubleshooting
- Shared Mailbox Not Showing in Outlook
- Access Denied After a Group Change

### Jazzy work

- add validator route/social-metadata policy for all four routes
- normalize complete desktop/mobile navigation
- normalize favicon declarations
- verify OG/Twitter metadata and canonicals
- verify sitemap entries
- add four landing-page cards in established Everyday IT format
- verify internal links, headings, fragments, accessibility basics, encoded characters, final newlines
- preserve approved content and intent
- run full static-site validation
- fix production/integration issues only
- report blockers before merge

## PR #45 — KrippyTech Content Architecture v1

**Title:** `Add KrippyTech content architecture v1`

**Branch:** `feature/content-architecture-v1`

**Status:** Draft, mergeable at last check.

### Purpose

Adds the operating system behind KrippyTech content development without changing public site content.

### Core additions

- ten stable primary content domains
- Raw → Sanitized Source → Extracted Lesson → Ledger → Asset → Published → Reuse pipeline
- batch intake/naming standard
- content ledger lifecycle and decision model
- two-level KER taxonomy: Primary Domain + Tags
- content-type decision rules
- cross-linking guidance
- published Everyday IT library map through Expansion #5
- public-route domain/tag mapping
- domain coverage/gap analysis
- private source-lineage register
- Expansion #6 lineage tracking
- high-value unpublished candidate tracking
- block on time-sensitive Microsoft/SMTP guidance until current vendor verification

### Important files

- `docs/content-architecture-v1.md`
- `docs/vault/batch-intake-standard.md`
- `docs/vault/content-ledger-standard.md`
- `docs/vault/ker-taxonomy.md`
- published library map/register files
- this handoff log

### Jazzy work

- review documentation consistency
- confirm no public exposure of source-lineage/private data
- confirm compatibility with `docs/vault/vault-standard.md` and `docs/publishing-standard.md`
- verify Markdown formatting/internal references/naming consistency
- preserve approved architecture intent
- report blockers before merge

## PR #46 — Everyday IT Strengthening Phase 1

**Title:** `Strengthen Everyday IT troubleshooting paths and safety workflows`

**Branch:** `feature/everyday-it-strengthening-1`

**Status:** Draft, mergeable at last check.

### Purpose

Turns Everyday IT from a collection of good articles into a connected troubleshooting system while filling major practical gaps exposed by Content Architecture v1.

### New routes

1. `/everyday-it/troubleshooting-paths/`
   - symptom-based routing hub across the existing Everyday IT library
   - routes users by failing layer rather than product name

2. `/everyday-it/scope-the-problem/`
   - scope-first troubleshooting method
   - one user, one device, one location, one resource, or everyone

3. `/everyday-it/known-good-comparison/`
   - changes one variable at a time
   - compares known-good user/device/client/network/resource paths
   - teaches that comparison means finding the meaningful difference, not making systems identical

4. `/everyday-it/change-safety-rollback/`
   - captures current state before remediation
   - identifies blast radius and shared dependencies
   - defines rollback before the change
   - protects the recovery path during the change
   - distinguishes rollback methods for permissions, profiles/clients, sync/data, and infrastructure
   - reinforces smallest justified change, checkpoint/stop conditions, regression testing, and post-change verification
   - core formula: `Current state + Blast radius + Rollback + Smallest justified action + Verification`

5. `/everyday-it/verify-before-close/`
   - separates change verification, technical verification, workflow verification, and user validation
   - distinguishes objective technical completion from situations where the user must confirm history, completeness, role-specific workflow, performance, or intermittent behavior
   - supports a clear `validation pending` state rather than inventing confirmation
   - closes with symptom, finding, action, verification, and pending validation evidence

6. `/everyday-it/escalate-with-evidence/`
   - teaches how to escalate without restarting the investigation
   - hand off symptom/scope, proven evidence, changes/results, risk boundaries, rollback state, and the exact unresolved next question
   - preserves useful failed tests and comparison results
   - emphasizes signal over a wall of ticket history

7. `/everyday-it/restrict-inherited-folder-permissions/`
   - full safe-change workflow for inherited NTFS permissions
   - approved-user confirmation
   - current ACL capture/rollback
   - preserve admin/SYSTEM/service identities
   - group-based access before restriction
   - Effective Access
   - disable inheritance by converting inherited entries before cleanup
   - avoid broad Deny shortcuts
   - share + NTFS interaction
   - token refresh after group changes
   - verify both approved and denied users
   - explicit stop/escalation boundaries

8. `/everyday-it/failing-disk-protect-data-first/`
   - data-protection-first response to suspected disk failure
   - identify data at risk
   - verify actual backup/sync state
   - avoid unnecessary write-heavy activity before protection state is known
   - collect storage/SMART/vendor evidence as appropriate
   - repair-tool caution when hardware failure is plausible
   - protect/recover → replace → rebuild → restore/validate
   - escalation when unique data or critical workloads are involved

### Strengthening methodology established

`Do not ask which product is broken first. Ask which layer failed.`

`Scope → Compare → Layer → Plan/Rollback → Change → Verify or Escalate.`

`Known-good comparison is not make them identical. It is find the meaningful difference.`

`Before you change it, know what it is, who depends on it, and how you will reverse it.`

`Make the smallest justified change.`

`Do not close because the change succeeded. Close because the required outcome was verified.`

`Escalate the investigation, not just the ticket.`

`Preserve a known-good access path before changing the permission model.`

`Data protection comes before repair when the storage itself may be failing.`

### Existing guide chains represented by the hub

- VPN Troubleshooting → VPN Works but the Drive Does Not → Mapped Drives & File Access
- Outlook vs Web → Outlook Profile Rebuild → Outlook Profile Creation Fails
- Shared Mailbox Permissions → shared-mailbox visibility/deeper tutorial path
- SharePoint & OneDrive → SharePoint Sync Troubleshooting → Free Up Space Safely
- Scanner Troubleshooting → Scan to Folder / Scan to Email
- Windows Temp Cleanup → When to Replace a Workstation → New PC Setup Checklist

### Jazzy work for #46

- add matching landing-page entries in established Everyday IT format
- add validator route/social-metadata policy for all eight routes
- verify complete desktop/mobile navigation and favicon declarations
- verify exact OG/Twitter metadata and canonicals
- verify all sitemap entries
- verify all internal links and cross-layer tutorial links
- verify headings, fragments, accessibility basics, encoded characters, final newlines
- add static Related Guides / Next Test sections to the highest-value existing pages where these routes identify a natural troubleshooting chain
- specifically consider linking `troubleshooting-escalation` to `scope-the-problem`, `known-good-comparison`, `change-safety-rollback`, `verify-before-close`, and `escalate-with-evidence`
- preserve approved content and symptom-first/layer-first intent
- run full static-site validation
- report blockers before merge

## Strategic Direction

This is the **KrippyTech strengthening phase**, not a reset.

Priorities:

1. Make Everyday IT behave like a knowledge graph rather than a flat article catalog.
2. Teach troubleshooting judgment, not only click-by-click fixes.
3. Keep Everyday IT as the approachable front door and advanced material as the authority layer.
4. Mine field-tested support material and preserve real diagnostic decisions, dead ends, warnings, and escalation boundaries.
5. Prefer enhancements when existing user intent is already served.
6. Add standalone pages only when the troubleshooting question is materially distinct and search-worthy.
7. Keep public material sanitized and client-independent.
8. Separate Everyday IT, KER/advanced, KT Cases, tutorials, downloads/checklists, course material, and future consulting references.

## Current High-Value Gaps / Future Candidates

- deeper file-access/permissions edge cases after inherited-folder safe-change guide
- remote-access dependency mapping as advanced/KER material
- stronger security/incident-response Everyday IT coverage
- server/infrastructure Everyday IT bridge material where safe for the audience
- advanced SPF/DMARC/direct-send only after current Microsoft verification
- SMTP AUTH identity guidance only after current Microsoft documentation verification

## Work Split

### Regular Chat / Ace

Use for strategy, source mining, sanitization, architecture, ledger work, page-vs-enhancement decisions, drafting, cross-link planning, and strengthening/content planning.

### Jazzy / Codex

Use for production integration, navigation normalization, validator/social metadata, landing-page integration, sitemap consistency, HTML/accessibility cleanup, repository-wide validation, and production-readiness review.

This split is intentional so Codex usage is reserved for work where it adds the most value.

## Living Log Rule

Append meaningful work completed before September 5 here or update the relevant PR section above. Record new branches/PRs, architecture decisions, source/ledger changes, pages, enhancements, cross-link plans, blockers, and vendor-verification dependencies.
