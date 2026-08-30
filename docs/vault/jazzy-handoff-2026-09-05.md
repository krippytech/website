# Jazzy Handoff Log — September 5, 2026

**Purpose:** Living handoff document for Codex/Jazzy when usage access resumes.

This file should be updated as work continues before September 5 so Jazzy can resume production review without reconstructing prior context.

## Current State

### PR #44 — Everyday IT Expansion #6

Title: `Expand Everyday IT identity and access troubleshooting`

Branch: `feature/everyday-it-expansion-6`

Status: Draft, awaiting Jazzy production integration/review.

Content already authored:
- MFA Recovery Without Weakening Security
- Recurring Account Lockout Troubleshooting
- Shared Mailbox Not Showing in Outlook
- Access Denied After a Group Change

Expected Jazzy work:
- add validator route/social-metadata policy for all four routes
- normalize the complete established desktop/mobile navigation
- normalize required favicon declarations
- verify exact OG/Twitter metadata and canonical URLs
- verify sitemap entries
- add four matching cards to the Everyday IT landing page using established formatting
- verify internal links, headings, fragments, accessibility basics, encoded characters, and final newlines
- preserve approved guide content and intent
- run the full static-site validation workflow
- fix production/integration issues only
- report blockers before merge

If production-ready with no blockers:
1. Mark Ready for review
2. Squash and merge
3. Delete `feature/everyday-it-expansion-6`

## PR #45 — KrippyTech Content Architecture v1

Title: `Add KrippyTech content architecture v1`

Branch: `feature/content-architecture-v1`

Status: Draft, mergeable at last check, awaiting documentation/production review.

Purpose: Adds the internal operating layer behind KrippyTech content development without changing public site content.

Core additions:
- ten stable primary content domains
- Raw → Sanitized Source → Extracted Lesson → Ledger → Asset → Published → Reuse pipeline
- batch intake and naming standard
- content ledger status and decision model
- two-level KER taxonomy using Primary Domain + Tags
- content-type decision rules
- cross-linking guidance
- published Everyday IT library map through Expansion #5
- public-route domain/tag mapping
- domain coverage and gap analysis
- cross-link priorities
- private source-lineage register
- active Expansion #6 lineage tracking
- strongest unpublished candidate tracking
- explicit block on time-sensitive Microsoft/SMTP guidance until current vendor verification

Files added/updated:
- `docs/content-architecture-v1.md`
- `docs/vault/batch-intake-standard.md`
- `docs/vault/content-ledger-standard.md`
- `docs/vault/ker-taxonomy.md`
- published library map/register files added during retrofit
- this handoff log

Expected Jazzy review for #45:
- review documentation consistency only
- confirm no public-site regression or accidental public exposure of private/source-lineage information
- confirm the architecture complements rather than conflicts with `docs/vault/vault-standard.md` and `docs/publishing-standard.md`
- verify Markdown formatting and internal references
- verify naming conventions are internally consistent
- preserve approved architecture intent
- report blockers before merge

If production-ready with no blockers:
1. Mark Ready for review
2. Squash and merge
3. Delete `feature/content-architecture-v1`

## Strategic Direction After #44 and #45

The next phase is not a reset. It is the **strengthening phase** for KrippyTech.

The objective is to improve and connect what already exists while continuing to add high-value practical content.

### Strengthening priorities

1. Retrofit all new Everyday IT content into Content Architecture v1 as it is created.
2. Add natural cross-links between related troubleshooting flows so the site behaves more like a knowledge graph than a pile of articles.
3. Keep Everyday IT as the approachable front door while advanced engineering remains the authority layer.
4. Continue mining field-tested source material instead of producing generic certification-style content.
5. Prefer enhancements when an existing page already serves the user intent.
6. Use standalone pages only when the troubleshooting question is materially distinct and search-worthy.
7. Keep client identity and credentials out of public content.
8. Continue separating Everyday IT, KER/advanced, KT Cases, tutorials, checklists/downloads, course material, and future consulting references.

## Strong Next Content Candidates

### Priority candidate: Restrict an Inherited Network Folder Safely

Primary domain: `07 File Servers & SMB`

Why it matters:
- high-value real-world permissions workflow
- teaches preservation of known-good access before changing ACL design
- covers Effective Access, inheritance, share + NTFS interaction, group-based access, token refresh, verification, rollback, and escalation
- fills a major file-permissions gap in Everyday IT

Key lesson:
`Preserve a known-good access path before changing the permission model, then prove both approved and denied access afterward.`

### Priority candidate: Failing Disk — Protect Data Before Rebuilding

Primary domain: `04 Windows & Workstations` or `08 Servers & Infrastructure` depending final scope.

Why it matters:
- teaches correct priority under hardware failure
- data protection before repair/rebuild
- backup-state verification
- evidence-driven disk health checks
- clear stop/escalation boundary

Key lesson:
`Do not begin repair or rebuild work until the data-protection state is understood.`

### Possible companion material

- stale credentials and lockout-source isolation if not fully covered by #44
- deeper file-access/permissions edge cases
- KER/advanced version of remote access dependency mapping
- advanced SPF/DMARC/direct-send material only after current Microsoft behavior is verified
- SMTP AUTH identity guidance only after current Microsoft documentation is verified

## Existing Everyday IT Build History

Confirmed merged prior to this handoff:
- PR #38 Everyday IT foundation
- PR #39 Expansion #1
- PR #40 Expansion #2
- PR #41 Expansion #3
- PR #42 Expansion #4
- PR #43 Expansion #5

Active at handoff creation:
- PR #44 Expansion #6
- PR #45 Content Architecture v1

Do not claim GitHub Pages deployment merely because a PR merged. Merge state and live deployment are separate.

## Work Split

### Regular Chat / Ace

Use for:
- strategy
- source mining
- sanitization decisions
- content architecture
- ledger work
- page-vs-enhancement decisions
- drafting approved content
- cross-link planning
- next-expansion planning

### Jazzy / Codex

Use for:
- production integration
- static navigation normalization
- validator/social metadata policy
- sitemap consistency
- landing-page integration
- HTML/accessibility cleanup
- repository-wide validation
- production-readiness review

This split is intentional to preserve Codex usage for work where it adds the most value.

## September 5 Restart Sequence

When Jazzy access returns:

1. Review this handoff log first.
2. Review PR #44 and complete production integration.
3. If green, merge #44 and delete its branch.
4. Review PR #45 for documentation/architecture consistency and privacy boundaries.
5. If green, merge #45 and delete its branch.
6. Pull latest `main` before creating the next content branch.
7. Begin the next strengthening/content expansion from the updated architecture, prioritizing high-value gaps rather than raw volume.

## Living Log Rule

Before September 5, append any important new work below this section.

Record:
- new branches/PRs
- new architecture decisions
- new source packs or ledger changes
- pages drafted
- existing pages enhanced
- cross-link plans
- blockers
- items requiring current vendor verification

Do not rely on memory alone. This file is the canonical restart handoff for Jazzy.

## Updates Before September 5

_Add new work here as it is completed._
