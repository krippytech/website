# KrippyTech Search Control Sprint A

**Status:** Internal execution audit

## Goal

Strengthen the first three Search Control families before adding new flagship content.

Sprint A is an authority-page tune-up, not a page-count expansion. It focuses on titles, H1s, metadata, opening language, internal-link hierarchy, proof paths, and consulting bridges.

## Sprint A ownership targets

1. Microsoft 365 and Outlook troubleshooting
2. Identity, MFA, lockouts, groups, and access
3. Practical IT troubleshooting methodology

## 1. Microsoft 365 and Outlook troubleshooting

### Primary authority

`/everyday-it/microsoft-365-email/`

### Current strengths

- Strong practical coverage of licensing, mailbox type, shared-mailbox permissions, distribution lists, message trace, client-vs-cloud isolation, and mail-flow safety.
- Clear troubleshooting judgment: prove delivery before rebuilding the client, and avoid broad mail-flow changes for one-user symptoms.
- Existing support cluster is already deep enough to justify authority-page status.

### Sprint A changes recommended

**Title**

Current:

`Microsoft 365 & Email Basics | Everyday IT | KrippyTech`

Recommended:

`Microsoft 365 & Outlook Troubleshooting | Everyday IT | KrippyTech`

Reason: “Basics” undersells the actual page and does not clearly claim the broader troubleshooting family.

**H1**

Current:

`Start with the mailbox, then prove the mail flow.`

Recommended:

`Troubleshoot Microsoft 365 and Outlook by proving where the failure lives.`

Keep the existing field-language concept immediately below it: mailbox object, permissions, transport, then client.

**Meta description**

Recommended intent:

`Practical Microsoft 365 and Outlook troubleshooting for licensing, mailboxes, shared mailbox access, message trace, mail flow, Outlook symptoms, and safe escalation.`

**Opening hierarchy**

The first screen should explicitly establish four layers:

1. identity / licensing
2. mailbox / permissions
3. Microsoft 365 transport
4. Outlook / local client

This makes the page the broad routing authority rather than only an email-basics lesson.

**Internal-link priority**

Add a visible “Troubleshoot the symptom” section or equivalent that routes to the strongest narrow pages:

- Outlook vs Web
- Outlook Profile Rebuild
- Outlook Profile Creation Fails
- Shared Mailbox Permissions
- Shared Mailbox Not Showing
- Message Trace Delivery
- Office Account Licensing
- Calendar Sharing Troubleshooting
- Mobile Exchange Sync

The authority page should link down into these pages, and the narrow pages should return-link to the authority page where natural.

**Proof path**

Surface advanced proof from Tutorials without turning the Everyday IT page into a deep runbook:

- Shared Mailbox Not Showing in Outlook tutorial
- Exchange Online Archive Not Reducing Primary Mailbox tutorial

**Consulting bridge**

Add one restrained bridge near the end only after the user reaches organization-wide mail-flow, tenant design, migration, recurring delivery, or poorly understood configuration risk.

Suggested boundary message:

`If the issue has moved beyond one mailbox or one Outlook client into tenant-wide mail flow, migration, retention, or recurring configuration problems, that is where an independent Microsoft 365 review can save time and reduce risky trial-and-error.`

Do not add a sales CTA to routine password/profile/shared-mailbox tasks.

### Flagship content after Sprint A

**Mailbox restore vs delegation vs forwarding**

This should answer a materially different decision intent and strengthen the authority page without competing with it.

---

## 2. Identity, MFA, lockouts, groups, and access

### Paired authorities

`/everyday-it/passwords-mfa/`

`/everyday-it/groups-permissions/`

The search family is too broad to force into one page without making the page worse. Keep two paired authorities with a clear division:

- `passwords-mfa` owns authentication, lockouts, MFA, tokens, sign-in state, and policy-related access symptoms.
- `groups-permissions` owns authorization, group membership, effective access, NTFS/share permissions, role-based access, and post-membership-change verification.

### Passwords / MFA audit

**Current title**

`Passwords, Lockouts & MFA | Everyday IT | KrippyTech`

Recommended title:

`Password, Account Lockout & MFA Troubleshooting | Everyday IT | KrippyTech`

Reason: preserves the user-language topics while making the page’s troubleshooting intent explicit.

**H1**

Current field-language H1 is strong and should be preserved:

`Stop treating every sign-in problem like a password problem.`

Do not replace it with a keyword-stuffed H1. Instead strengthen the supporting hero copy so it explicitly names Microsoft 365 / Entra / Windows sign-in layers where natural.

**Internal-link priorities**

Make the narrow paths highly visible:

- MFA Recovery
- Recurring Account Lockout
- Entra Sign-In & Conditional Access Investigation
- Mobile Exchange Sync
- Suspicious Sign-In First Response

Add a return link from those narrow routes when natural.

### Groups / permissions audit

**Current title**

`Groups & Permissions | Everyday IT | KrippyTech`

Recommended title:

`Groups, NTFS & File Permission Troubleshooting | Everyday IT | KrippyTech`

This better communicates the practical access problem family while retaining group-based design.

**H1**

Current:

`Give access without creating a mess.`

Keep it. It is memorable and fits the KrippyTech voice.

Strengthen nearby copy to state that this page owns group-based access, NTFS/share permission layers, Effective Access, token refresh, and access-denied troubleshooting.

**Internal-link priorities**

- Access Denied After a Group Change
- Restrict Inherited Folder Permissions
- Mapped Drives & File Access
- Change Safety & Rollback
- Active Directory

### Cross-authority link

The two authority pages should explicitly link to one another at the authentication-vs-authorization boundary.

Suggested logic:

`If the user cannot prove identity, stay in Passwords, Lockouts & MFA. If the user can sign in but cannot reach the resource, move to Groups & Permissions.`

This distinction should become one of the defining KrippyTech identity/access concepts.

### Consulting bridge

Only bridge to Consulting when the problem involves:

- tenant-wide Conditional Access
- identity design or hybrid identity cleanup
- permission sprawl
- risky inheritance/ACL redesign
- privileged access
- repeated lockouts or access failures without a clear source

Suggested message:

`Routine access changes should be understandable and repeatable. When the environment has permission sprawl, unclear identity paths, risky Conditional Access, or inherited access nobody can explain, that is a good point for an independent review.`

### Flagship content after Sprint A

**Conditional Access failure decision tree**

This should bridge the Everyday IT authority page to the existing Entra investigation tutorial while keeping policy changes at a safe decision/verification level.

---

## 3. Practical IT troubleshooting methodology

### Primary authority

`/everyday-it/troubleshooting-paths/`

### Current strengths

- Already behaves like a real routing hub rather than a generic troubleshooting article.
- Strong core message: symptom first, failing layer second, product third.
- Existing lifecycle gives KrippyTech a distinct methodology:

`Scope → Compare → Layer → Plan/Rollback → Change → Verify → Workaround/Resolution → Prevent Recurrence`

At an unsafe or unresolved point:

`Escalate With Evidence`

### Sprint A changes recommended

**Title**

Current:

`Troubleshooting Paths | Everyday IT | KrippyTech`

Recommended:

`IT Troubleshooting Method & Decision Paths | Everyday IT | KrippyTech`

Reason: the current title is clean but vague. The recommended version claims the methodology/decision-intent family without turning it into keyword stuffing.

**H1**

Current:

`Start with the symptom. Find the failing layer.`

Keep exactly. This is one of the strongest KrippyTech lines on the site.

**Hero / opening**

Preserve:

`Scope first. Compare second. Then choose the path.`

Add one short line making the philosophy explicit:

`Do not ask which product is broken first. Ask which layer failed.`

**Hierarchy**

The lifecycle should be visually and structurally obvious near the top, not discovered only after routing through symptom cards.

Recommended order:

1. Scope
2. Known-good comparison
3. Identify the failing layer
4. Choose the symptom path
5. Plan / rollback before risky change
6. Verify the real outcome
7. classify workaround vs resolution
8. prevent recurrence
9. escalate with evidence when needed

**Internal-link priority**

Every lifecycle child should return naturally to Troubleshooting Paths as the parent methodology page.

High-value support pages:

- Scope the Problem
- Known-Good Comparison
- Change Safety & Rollback
- Verify Before Close
- Escalate With Evidence
- Workaround vs Resolution
- Prevent Recurrence
- Shared Service Outage Triage

**Proof layer**

Begin connecting sanitized Cases to specific lifecycle decisions as Cases grow.

The goal is not to say “KrippyTech uses a methodology.” The goal is to prove it through real examples where scope or comparison changed the investigation.

**Consulting bridge**

This authority page gets the strongest consulting bridge of the three because the natural boundary is clear: a problem has survived normal troubleshooting, impacts shared infrastructure, or requires a risky change.

Suggested message:

`If the problem keeps returning, affects several users or systems, or the next step is risky enough that rollback matters, stop guessing. That is a good point to bring in an experienced second set of eyes.`

Link to `/consulting/` from that boundary, not from every symptom card.

### Flagship content after Sprint A

**Troubleshooting Worksheet / First 10 Minutes Checklist**

Recommended format:

- printable/downloadable checklist
- optional GitHub Markdown version
- page on KrippyTech explaining how to use it
- prompts for scope, known-good comparison, recent change, business impact, risky next step, evidence captured, and verification target

This is the most reusable external-reinforcement asset in the first three families.

---

## Sprint A implementation order

1. Tune Microsoft 365 authority metadata/title/opening and add routing links.
2. Tune Passwords/MFA and Groups/Permissions as paired authorities and make authentication-vs-authorization explicit.
3. Tune Troubleshooting Paths title/opening/lifecycle hierarchy.
4. Add restrained consulting bridges only at the documented complexity/risk boundary.
5. Add or verify return links from narrow guides to the authority page.
6. Run validator, internal-link, sitemap-preservation, accessibility, metadata, and exact Git-tree validation.
7. Do not create the three flagship assets until the authority-page changes are merged or production-ready.

## Sprint A acceptance criteria

Sprint A is complete when:

- each of the three target families has an unmistakable authority page or paired authority
- title/meta language clearly matches the broad search intent
- distinctive KrippyTech H1/field language is preserved where already strong
- narrow guides link naturally into and back from the authority page
- advanced Tutorials/Cases provide a proof path where appropriate
- Consulting appears only at a credible risk/complexity boundary
- no duplicate broad-search page is introduced
- validator and site checks remain green

The objective is not to make these pages sound like SEO pages. The objective is to make it obvious to both people and search systems what each page owns.