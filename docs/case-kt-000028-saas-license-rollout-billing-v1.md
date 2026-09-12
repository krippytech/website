# KT-000028 Case Handoff

## Public title
KT-000028 | SaaS License Rollout Required Recipient and Billing Control | Aki Inu Tech

## H1
SaaS License Rollout Required Recipient and Billing Control

## Category
Microsoft 365 / SaaS Licensing

## Status
Access Verified / Billing Reconciled

## Technologies
Microsoft 365 / Copilot / SaaS Licensing

## Locked lesson
**Assigning a license is not the end of a SaaS rollout. Prove who needs it, prove it works, then prove billing matches the final requirement.**

## Supporting principle
**License assignment and subscription quantity are separate controls.**

## Investigation path
**Request → Account classification → Approved recipients → License assignment → Service propagation → In-app verification → Seat reconciliation → Subscription-window check → Billing cleanup**

## Evidence boundary
- the original access request did not define the final recipient set
- the tenant contained account types that were not all appropriate license targets
- selected users were assigned licenses
- assigned users confirmed the feature appeared in supported Office applications
- purchased, assigned, and required seat counts were reconciled
- unneeded seats were removed during an available subscription adjustment window
- access verification and billing reconciliation are separate proof points
- removing a license assignment is not presented as proof that paid subscription quantity changed
- do not claim every SaaS vendor uses the same billing or cancellation model
- do not claim every Microsoft 365 subscription can always be reduced immediately
- current licensing and cancellation terms require revalidation before time-sensitive procedural publication
- do not publish customer, tenant, user, subscription, invoice, pricing, account, or billing identifiers

## Intent separation
- `/cases/KT-000028/` is the proof layer
- `/everyday-it/scope-the-problem/` remains symptom/scope methodology
- `/everyday-it/verify-before-close/` remains verification methodology
- `/consulting/` remains the consulting bridge

## Production integration request for Jazzy
- place KT-000028 immediately after KT-000027 on `/cases/`
- add `/cases/KT-000028/` to `sitemap.xml` exactly once
- normalize the page to current shared accessible nav/footer/favicon/social/authorship conventions
- add restrained inbound proof links from Verify Before Close and/or the consulting area if graph placement is clean
- preserve outbound links to Scope the Problem, Verify Before Close, and Consulting
- validator coverage should include exact metadata, canonical/article behavior, authorship/date, locked lesson, supporting principle, exact investigation path, exact status, Cases placement, sitemap uniqueness, recipient-classification evidence, in-app verification, seat reconciliation, assignment-versus-billing distinction, subscription-window qualification, non-universal billing claims, revalidation requirement, proof-layer positioning, and sanitization
- no downloadable derivative
- run full static validation
- keep PR Draft and do not merge
