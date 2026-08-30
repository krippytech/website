# KrippyTech Content Ledger Standard

**Version:** 1.0

## Purpose

The content ledger is the control plane for KrippyTech knowledge development.

It prevents duplicate work, shows what has already been captured, identifies the strongest next builds, and connects source material to published assets.

## Required Fields

Every retained content item should have:

- **ID**: permanent identifier such as `EIT-001`
- **Primary Domain**: one of the ten Content Architecture domains
- **Working Title**
- **Source File or Batch**
- **Source Strength**: Strong / Supporting / Weak
- **Candidate Type**
- **Status**
- **Priority**: High / Medium / Low
- **Published Route or Asset** when applicable
- **Related Content**
- **Notes / Next Action**

## Candidate Types

Use one primary candidate type:

- Everyday IT standalone
- Everyday IT enhancement
- KER / advanced reference
- KT Case
- Tutorial
- PowerShell
- Checklist
- Download
- MSP University
- Azure Lab
- Consulting reference
- Duplicate / supporting evidence
- Noise / archive only

## Status Model

Use these statuses consistently:

### Captured

The lesson exists in the ledger but has not been evaluated deeply.

### Qualified

The lesson has enough evidence and value to keep.

### Planned

A content type and likely destination have been chosen.

### Drafting

Content is actively being developed.

### Review

Content exists and is awaiting technical, production, or editorial review.

### Published

The public asset is live or merged into the publishing branch. Record the route or asset.

### Enhancement Needed

The topic is already published, but source material reveals a useful missing section.

### Supporting Evidence

The source reinforces another ledger item and should not create a duplicate page.

### Deferred

Valuable, but intentionally postponed.

### Blocked

Requires current vendor verification, missing technical evidence, or another dependency before publication.

### Retired

No longer appropriate to publish or maintain. Preserve history; do not reuse the ID.

### Noise

No reusable technical lesson.

## Priority Model

### High

Choose High when several are true:
- common support symptom
- strong search intent
- strong field evidence
- useful to a broad technician audience
- fits an existing learning path
- closes an obvious library gap
- can be safely generalized

### Medium

Useful content with narrower frequency, overlap with existing material, or lower urgency.

### Low

Niche, weakly supported, highly vendor-specific, or better held for a later advanced collection.

## Duplication Rule

Before adding a new candidate, compare it with:

1. existing Everyday IT routes
2. planned ledger items
3. KER references
4. tutorials and KT Cases

If the same user intent is already served, prefer:
- adding supporting source evidence
- enhancing the existing asset
- creating a deeper follow-up only when the troubleshooting question is materially different

## Relationship Fields

Where useful, track:

- **Parent**: broader guide this item belongs under
- **Next Step**: natural follow-up resource
- **Prerequisite**: material the reader should understand first
- **Source Siblings**: other lessons extracted from the same incident
- **Advanced Version**: corresponding KER/tutorial material
- **Consulting Signal**: recurring governance, risk, cost, or architecture pattern

These relationships make the library reusable as learning paths instead of a flat article catalog.

## Published Mapping

When an item is published, record:

- route or asset path
- PR number if useful
- publication type
- whether the original candidate became standalone content or an enhancement
- related guides added during publication

Do not delete the ledger row after publishing. The ledger is permanent knowledge history.

## Suggested Spreadsheet Columns

For the current spreadsheet workflow, use this order:

| Column | Purpose |
|---|---|
| ID | Permanent identifier |
| Domain | Primary content domain |
| Working Title | Human-readable topic |
| Source | Batch/file reference |
| Source Strength | Strong / Supporting / Weak |
| Candidate Type | Intended asset |
| Status | Lifecycle state |
| Priority | High / Medium / Low |
| Parent / Related | Existing or planned relationship |
| Published Route | Final destination |
| PR / Release | Implementation reference |
| Consulting Signal | Yes / No / Maybe |
| Notes / Next Action | Working decision |

## Operating Rules

1. Never reuse an ID.
2. Never delete a published item's history because the page later changes.
3. Do not create a page merely because a source exists.
4. Multiple sources may support one item.
5. One source may create multiple items.
6. Keep public-page decisions separate from raw-source privacy.
7. Use the ledger to pick expansion work rather than relying only on memory.
8. Periodically review Published items for cross-link and enhancement opportunities when new evidence arrives.

## Expansion Planning

A strong expansion batch should usually combine three or four High-priority items that:

- fit a coherent technical theme
- do not duplicate existing user intent
- have enough source evidence
- strengthen surrounding published material

A batch may include one enhancement alongside new pages when that creates better internal linking.

## Definition of Healthy

The ledger is healthy when a new source dump can be processed without asking:

- Have we already written this?
- Where should this go?
- What source supports it?
- Which topic is most important next?
- What published material should link to it?

Those answers should already be visible in the system.
