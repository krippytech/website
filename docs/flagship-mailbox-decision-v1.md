# Flagship Asset: Mailbox Restore vs Delegation vs Forwarding v1

**Status:** Draft content complete, production integration pending

## Search Control Family

Microsoft 365 and Outlook troubleshooting

## New Route

`/everyday-it/mailbox-restore-delegation-forwarding/`

## Search Intent

Primary intent:
- mailbox restore vs delegation vs forwarding
- former employee mailbox access
- should I convert a mailbox to shared
- Full Access vs Send As vs Send on Behalf
- mailbox forwarding vs shared mailbox

The page should own the decision layer, not duplicate detailed step-by-step recovery, archive, shared-mailbox, or Outlook troubleshooting pages.

## Locked Core Principle

**Do not start with the button. Start with what the business needs to happen next.**

Supporting decision model:

`Recover data → Delegate access → Redirect future mail → Choose sending identity → Preserve lifecycle/compliance`

## Required Distinctions

Keep these separate throughout the page:

1. **Recovery**: mailbox or historical data is missing.
2. **Delegation**: another approved user needs to open/manage content.
3. **Forwarding**: future messages must be delivered elsewhere.
4. **Sending identity**: someone needs Send As or Send on Behalf.
5. **Shared mailbox conversion**: the mailbox should remain as a shared business resource.
6. **Offboarding**: preserve the mailbox without preserving the former employee's sign-in access.
7. **Compliance/retention**: legal hold, retention, archive, and business continuity are not interchangeable.

## Current Microsoft Verification Notes

Verified against current Microsoft Learn guidance on 2026-09-06:

- Full Access allows mailbox access but does not itself grant Send As or Send on Behalf.
- Send As makes messages appear to come directly from the mailbox.
- Send on Behalf identifies the delegate as sending on behalf of the mailbox.
- Microsoft documents user-to-shared mailbox conversion as preserving existing email/calendar content.
- Microsoft currently documents unlicensed shared mailboxes as limited to 50 GB, with licensing required for larger capacity and certain archive/hold features.
- Microsoft states the user mailbox must be licensed before conversion to shared; license removal after conversion depends on mailbox size and feature requirements.
- Microsoft states the associated account remains required to anchor the shared mailbox.
- Hybrid Exchange can require different authoritative-object procedures.

Do not hard-code portal click paths into the Everyday IT page unless Jazzy decides they are stable and necessary. This is a decision guide, not a UI walkthrough.

## Safety Boundary

Do not turn this page into:

- a legal/compliance runbook
- instructions to bypass retention requirements
- a tenant-wide forwarding configuration guide
- a way to reuse former-employee credentials
- a shortcut for broad mailbox access
- an Exchange hybrid conversion runbook

Escalate or bridge to Consulting at:

- executive, legal, HR, finance, or otherwise sensitive mailboxes
- unclear retention/hold obligations
- hybrid Exchange authority questions
- broad forwarding or mail-flow redesign
- privileged/admin mailbox access
- irreversible or high-blast-radius lifecycle changes

## Existing Supporting Routes

Strong direct support:

- `/everyday-it/microsoft-365-email/`
- `/everyday-it/former-employee-mailbox/`
- `/everyday-it/shared-mailbox-permissions/`
- `/everyday-it/shared-mailbox-not-showing/`
- `/everyday-it/message-trace-delivery/`
- `/everyday-it/change-safety-rollback/`
- `/tutorials/exchange-online-archive-not-reducing-primary-mailbox/`
- `/tutorials/shared-mailbox-not-showing-outlook/`

## Production Integration Tasks for Jazzy

1. Rebase/update branch against current `main` if needed.
2. Normalize navigation/favicons/markup to current production conventions.
3. Add the route to the Everyday IT landing page.
4. Add the canonical route to `sitemap.xml` exactly once.
5. Add validator expectations for title, metadata, social metadata, article type, route, and internal links.
6. Add natural inbound links from:
   - Microsoft 365 & Email authority page
   - Former Employee Mailbox
   - Shared Mailbox Permissions
   - Shared Mailbox Not Showing
   - Troubleshooting Paths if appropriate
   - other M365/offboarding pages where the decision page is a genuine next step
7. Preserve outbound links already drafted.
8. Preserve the restrained Consulting bridge at sensitive/broad/risky mailbox-lifecycle boundaries.
9. Verify no duplicate broad search intent is introduced. Existing narrow pages remain canonical for their specific symptoms/tasks.
10. Run full static-site validation.

## Suggested Landing Card

**Mailbox Restore, Delegation or Forwarding?**

Decide whether the real need is historical recovery, mailbox access, future delivery, sending identity, or former-employee preservation before changing the mailbox.

## Canonical Ownership Rule

This route owns the **decision question**.

It does not replace:

- `former-employee-mailbox` for offboarding workflow
- `shared-mailbox-permissions` for delegation mechanics
- `shared-mailbox-not-showing` for Outlook visibility/propagation
- Exchange archive tutorial for archive/storage investigation

## Ready-for-Review Gate

Before moving PR to Ready for Review, confirm:

- landing page integration complete
- sitemap exactly once
- validator/social metadata complete
- inbound M365 cluster links added
- no broken links/fragments
- no duplicated canonical search intent
- Consulting bridge remains restrained
- static-site validation passes
- no blockers remain
