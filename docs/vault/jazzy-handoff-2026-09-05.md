# Jazzy Handoff Log — September 5, 2026

**Purpose:** Canonical restart handoff for Codex/Jazzy now that production integration can resume.

## September 5 Live State

Verified before execution:

- PR #44: merged; feature branch deleted
- PR #45: open, draft, rebased onto the post-#44 `main`
- PR #46: open, draft, mergeable
- PR #47: open, draft, mergeable
- PR #48: open, draft, mergeable

PR #44 is merged. PRs #45–#48 are not merged yet. Do not assume GitHub Pages deployment merely because a PR is merged; deployment must be verified separately.

## Execution Order

1. Review this file first. **Completed for PR #45.**
2. Complete production integration for PR #44. **Completed.**
3. Run full static-site validation. If green, Ready → Squash and merge → delete branch. **Completed for PR #44.**
4. Pull latest `main`. **Completed after PR #44.**
5. Review PR #45 for Content Architecture v1 consistency and privacy boundaries. If green, Ready → Squash and merge → delete branch. **Review completed; awaiting Ready for Review.**
6. Pull latest `main`.
7. Update/rebase PR #46 against current `main` if needed, preserving all merged sitemap, landing, validator, and navigation work.
8. Complete PR #46 production integration and cross-link implementation. Run full static-site validation. If green, Ready → Squash and merge → delete branch.
9. Pull latest `main`.
10. Update/rebase PR #47 against current `main`, preserving the complete Phase 1 route set and integration surfaces.
11. Complete PR #47 production integration. Run full static-site validation. If green, Ready → Squash and merge → delete branch.
12. Pull latest `main`.
13. Update/rebase PR #48 against current `main` if needed.
14. Review and production-integrate the consulting repositioning without reintroducing MSP-style messaging. Run full validation. If green, Ready → Squash and merge → delete branch.
15. Pull latest `main` and verify the resulting site/deployment separately.

## Global Production Rules

- Preserve approved page intent and troubleshooting methodology. Fix integration and consistency issues without rewriting the strategy.
- Never overwrite a newer `sitemap.xml`, landing page, validator policy, navigation block, or shared metadata surface with an older branch version.
- Normalize every new public page to the current established desktop/mobile navigation and favicon pattern.
- Verify canonical, OG, Twitter, internal links, headings, fragments, encoded characters, accessibility basics, and final newlines.
- Add validator coverage for every new public route and social metadata requirement.
- Run the repository’s full static-site validation workflow before recommending merge.
- Report blockers rather than hiding uncertainty.
- Keep public material sanitized and client-independent.

## PR #44 — Everyday IT Expansion #6

**Title:** `Expand Everyday IT identity and access troubleshooting`

**Branch:** `feature/everyday-it-expansion-6`

**Status:** Merged on September 5; feature branch deleted.

### Approved content

- MFA Recovery Without Weakening Security
- Recurring Account Lockout Troubleshooting
- Shared Mailbox Not Showing in Outlook
- Access Denied After a Group Change

### Jazzy implementation work

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

**Status:** Open and draft; rebased onto the post-#44 `main` and production-readiness review completed on September 5.

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
- published Everyday IT library map through Expansion #6
- public-route domain/tag mapping
- domain coverage/gap analysis
- private source-lineage register
- published Expansion #6 lineage tracking
- high-value unpublished candidate tracking
- block on time-sensitive Microsoft/SMTP guidance until current vendor verification

### Important files

- `docs/content-architecture-v1.md`
- `docs/vault/batch-intake-standard.md`
- `docs/vault/content-ledger-standard.md`
- `docs/vault/ker-taxonomy.md`
- `docs/everyday-it-library-map.md`
- `docs/vault/source-lineage-register.md`
- this handoff log

### Jazzy implementation work

- review documentation consistency
- confirm no public exposure of source-lineage/private data
- confirm compatibility with `docs/vault/vault-standard.md` and `docs/publishing-standard.md`
- verify Markdown formatting/internal references/naming consistency
- preserve approved architecture intent
- report blockers before merge

## PR #46 — Everyday IT Strengthening Phase 1

**Title:** `Strengthen Everyday IT troubleshooting paths and safety workflows`

**Branch:** `feature/everyday-it-strengthening-1`

**Status:** Open, draft, mergeable as of September 5.

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
   - comparison means finding the meaningful difference, not making systems identical

4. `/everyday-it/change-safety-rollback/`
   - captures current state before remediation
   - identifies blast radius and shared dependencies
   - defines rollback before the change
   - protects the recovery path during the change
   - core formula: `Current state + Blast radius + Rollback + Smallest justified action + Verification`

5. `/everyday-it/verify-before-close/`
   - separates change verification, technical verification, workflow verification, and user validation
   - supports `validation pending` rather than inventing confirmation

6. `/everyday-it/escalate-with-evidence/`
   - hand off symptom/scope, proven evidence, changes/results, risk boundaries, rollback state, and the exact unresolved next question
   - preserves useful failed tests and comparison results

7. `/everyday-it/workaround-vs-resolution/`
   - distinguishes workaround, containment, validation pending, and true resolution
   - temporary paths require an exit plan, risk statement, and follow-up owner

8. `/everyday-it/prevent-recurrence/`
   - asks whether the incident was preventable, detectable sooner, easier to diagnose, or evidence of a needed permanent change
   - converts resolved incidents into documentation, monitoring, configuration, ownership, training, and reusable knowledge improvements

9. `/everyday-it/restrict-inherited-folder-permissions/`
   - safe inherited NTFS permission-change workflow
   - rollback, Effective Access, group-based access, token refresh, share + NTFS interaction, and verification

10. `/everyday-it/failing-disk-protect-data-first/`
   - data-protection-first response to suspected disk failure
   - protect/recover → replace → rebuild → restore/validate

### Strengthening methodology

`Do not ask which product is broken first. Ask which layer failed.`

`Scope → Compare → Layer → Plan/Rollback → Change → Verify → Workaround/Resolution → Prevent Recurrence.`

At any unsafe or unresolved point: `Escalate With Evidence.`

`Known-good comparison is not make them identical. It is find the meaningful difference.`

`Before you change it, know what it is, who depends on it, and how you will reverse it.`

`Make the smallest justified change.`

`Do not close because the change succeeded. Close because the required outcome was verified.`

`A workaround restores productivity. A resolution restores the intended design or safely controls the cause.`

`Escalate the investigation, not just the ticket.`

`A good fix restores service. A great support system also keeps the lesson.`

`Preserve a known-good access path before changing the permission model.`

`Data protection comes before repair when the storage itself may be failing.`

### Existing guide chains represented by the hub

- VPN Troubleshooting → VPN Works but the Drive Does Not → Mapped Drives & File Access
- Outlook vs Web → Outlook Profile Rebuild → Outlook Profile Creation Fails
- Shared Mailbox Permissions → shared-mailbox visibility/deeper tutorial path
- SharePoint & OneDrive → SharePoint Sync Troubleshooting → Free Up Space Safely
- Scanner Troubleshooting → Scan to Folder / Scan to Email
- Windows Temp Cleanup → When to Replace a Workstation → New PC Setup Checklist

### Jazzy implementation work

- update/rebase after prior merges as needed, preserving all current shared integration surfaces
- add matching landing-page entries in established Everyday IT format
- add validator route/social-metadata policy for all ten routes
- normalize complete desktop/mobile navigation and favicon declarations on drafted pages
- verify exact OG/Twitter metadata and canonicals
- verify all sitemap entries
- verify all internal links and cross-layer tutorial links
- verify headings, fragments, accessibility basics, encoded characters, final newlines
- implement static `Related Guides` / `Next Test` sections on the highest-value existing pages, based on actual troubleshooting outcomes rather than generic article dumping
- prioritize cross-links from `troubleshooting-escalation`, `groups-permissions`, `mapped-drives-access`, `outlook-vs-web`, `sharepoint-onedrive`, `scanner-troubleshooting`, `when-to-replace-workstation`, and `windows-temp-cleanup`
- specifically connect the lifecycle across `scope-the-problem`, `known-good-comparison`, `change-safety-rollback`, `verify-before-close`, `workaround-vs-resolution`, `prevent-recurrence`, and `escalate-with-evidence`
- wire `troubleshooting-paths` through the complete methodology, not just product paths
- preserve approved content and symptom-first/layer-first intent
- run full static-site validation
- report blockers before merge

## PR #47 — Everyday IT Strengthening Phase 2

**Title:** `Strengthen Everyday IT security and infrastructure triage`

**Branch:** `feature/everyday-it-strengthening-2`

**Status:** Open, draft, mergeable as of September 5. Still update/rebase after #44–#46 are merged because it shares integration surfaces with them.

### Purpose

Fills two thinner Everyday IT domains without turning approachable support guidance into deep incident-response or production-infrastructure runbooks.

### New routes

1. `/everyday-it/suspicious-signin-first-response/`
   - unexpected MFA prompts, unfamiliar sign-ins, suspicious mailbox/account behavior
   - core lesson: `Unexpected authentication activity changes the ticket from make login work to prove who is signing in.`

2. `/everyday-it/malware-alert-first-response/`
   - confirm endpoint/user/detection, preserve evidence, contain through approved tooling, verify mitigation, correlate related activity, escalate unresolved risk
   - core flow: `Confirm → Preserve → Contain → Verify → Correlate → Escalate.`

3. `/everyday-it/shared-service-outage-triage/`
   - moves first-line troubleshooting upstream when several users/devices share a symptom
   - core lesson: `One user can be an endpoint problem. Ten users with the same symptom are telling you to look upstream.`

4. `/everyday-it/server-restart-safety/`
   - treats a production restart as a controlled change rather than a diagnostic shortcut
   - core lesson: `Restarting is remediation. Treat it like a change, not a substitute for diagnosis.`

### Jazzy implementation work

- update/rebase the branch after #44–#46 merge so shared integration changes are preserved
- normalize complete established desktop/mobile navigation on all four drafted pages
- normalize favicon declarations and exact page metadata
- add validator route/social-metadata policy for all four routes
- verify sitemap against the merged route set rather than overwriting newer entries
- add landing-page entries in established Everyday IT format
- add `Related Guides` / `Next Test` links into the Phase 1 lifecycle
- strongly consider security links from Passwords/MFA and Troubleshooting & Escalation
- strongly consider infrastructure links from Troubleshooting & Escalation, VPN/file-access paths, and appropriate advanced tutorials
- preserve Everyday IT safety boundaries and do not expand the pages into deep security remediation or infrastructure redesign procedures
- verify headings, fragments, accessibility basics, encoded characters, final newlines, canonical/OG/Twitter metadata, and internal links
- run full static-site validation
- report blockers before merge

## PR #48 — Consulting Positioning v1

**Title:** `Reposition consulting around independent small-business IT guidance`

**Branch:** `feature/consulting-positioning-v1`

**Status:** Open, draft, mergeable as of September 5.

### Purpose

Repositions KrippyTech consulting away from managed-services/MSP language and toward independent small-business IT consulting.

### Approved positioning

- experienced technical help without the traditional MSP model
- `Teach it. Handle it. Partner on it.` depending on what the business actually needs
- do not create dependency for routine tasks that a business can safely handle internally
- bring KrippyTech in when work becomes complicated, risky, specialized, or time-consuming
- focus on troubleshooting, projects, modernization, planning, security improvement, simplification, second opinions, cost review, and documentation
- avoid unlimited helpdesk, endpoint bundles, monitoring packages, per-user MSP pricing, 24/7 promises, and outsourced-IT-department language
- speak as KrippyTech or `I` where a human voice is useful; do not imply a team or staff structure that does not exist

### Primary message

`I don’t need you to depend on me for every password reset. I’d rather help you understand the easy things and be there when the work becomes complicated, risky, or time-consuming.`

Supporting principles:

- learn what makes sense to learn
- hand off what should not be guessed at
- leave the environment easier to operate than it was before
- technology should support the business, not exist to sell another subscription
- independent recommendations should be based on need, risk, budget, and measurable value

### Jazzy implementation work

- update/rebase after prior merges if needed
- preserve the approved independent-consultant voice and remove any residual MSP/team-oriented phrasing
- normalize page HTML/navigation/metadata to the final current site standard
- verify canonical, OG, Twitter, favicon, internal links, accessibility basics, encoded characters, and final newline
- review CTA wording and contact path for clarity without adding unapproved availability/SLA promises
- preserve the connection between consulting and Everyday IT: public teaching demonstrates the consulting philosophy rather than competing with it
- do not add managed-service packages, unlimited helpdesk, endpoint pricing, monitoring bundles, or outsourced-IT-department language
- run full static-site validation
- report blockers before merge

## Strategic Direction

This is the KrippyTech strengthening phase, not a reset.

Priorities:

1. Make Everyday IT behave like a knowledge graph rather than a flat article catalog.
2. Teach troubleshooting judgment, not only click-by-click fixes.
3. Keep Everyday IT as the approachable front door and advanced material as the authority layer.
4. Mine field-tested support material and preserve real diagnostic decisions, dead ends, warnings, and escalation boundaries.
5. Prefer enhancements when existing user intent is already served.
6. Add standalone pages only when the troubleshooting question is materially distinct and search-worthy.
7. Keep public material sanitized and client-independent.
8. Keep consulting independent, practical, and anti-dependency rather than drifting into MSP positioning.

## Current High-Value Future Candidates

- deeper file-access/permissions edge cases after inherited-folder safe-change guide
- remote-access dependency mapping as advanced/KER material
- deeper security/incident-response content only where it can remain safely scoped for Everyday IT
- additional server/infrastructure bridge material only where it teaches observation, dependency mapping, verification, and escalation rather than casual production changes
- advanced SPF/DMARC/direct-send only after current Microsoft verification
- SMTP AUTH identity guidance only after current Microsoft documentation verification

## Work Split

### Regular Chat / Ace

Use for strategy, source mining, sanitization, architecture, ledger work, page-vs-enhancement decisions, drafting, cross-link planning, positioning, and strengthening/content planning.

### Jazzy / Codex

Use for production integration, branch update/rebase work, navigation normalization, validator/social metadata, landing-page integration, sitemap consistency, HTML/accessibility cleanup, repository-wide validation, and production-readiness review.

## Living Log Rule

Update this handoff with meaningful decisions or scope changes until the active PR queue is integrated. Record new branches/PRs, architecture decisions, source/ledger changes, pages, enhancements, cross-link plans, blockers, and vendor-verification dependencies.
