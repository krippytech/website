# KT-000031 Content Spec

## Case title
Microsoft 365 Admin Consent Required a Controlled Approval Path

## Source
EX-006-07, sanitized engineering extraction.

## Proof-layer purpose
Show that a failed or missing consent request should be handled as a controlled Microsoft 365 identity/security workflow, not as a reason to bypass review or grant broad access blindly.

## Locked lesson
**“Grant access to Microsoft 365” is not an approval decision. Verify the application, the requested permissions, and the tenant consent path before granting access.**

## Supporting principle
**Consent should follow evidence: app identity, requested scopes, tenant policy, administrator review, least necessary approval, then functional testing.**

## Investigation path
**Integration request → Pending-request check → Consent-policy review → Request-path correction → Publisher/app review → Scope review → Administrator approval → Connector login → Functional retest**

## Status
**Consent Workflow Established / Integration Verified**

## Evidence to preserve
- a user attempted to connect third-party SaaS/AI applications to Microsoft 365
- the expected consent request did not initially appear
- the tenant was checked for pending consent requests and none had arrived
- the administrative consent policy was reviewed
- the requesting user was added to the appropriate consent workflow
- the application integration was retried
- consent/login for required connectors completed
- the integration succeeded after the tenant consent workflow was configured and the request was retried
- verification includes confirming the app requires the requested permissions
- publisher/app identity and requested scopes are reviewed
- tenant consent policy is checked
- the request is verified as appearing for administrator review
- only necessary scopes are approved
- functional testing occurs after approval

## Boundaries
Do not claim:
- every third-party integration uses the same consent path
- every Microsoft 365 tenant should enable the same admin-consent configuration
- publisher verification alone proves an application is safe
- every requested permission should be approved
- no risk remains after admin consent
- the original integration failure was caused by application malfunction
- current Entra/Microsoft 365 consent UI or terminology is permanent

Current Microsoft Entra and Microsoft 365 admin-consent capabilities, terminology, and UI require revalidation before time-sensitive procedural publication.

Do not publish customer, tenant, user, application-registration, publisher, object, consent-request, token, connector, or other identifying details.

## Intent separation
- `/cases/KT-000031/` is the proof layer
- `/everyday-it/conditional-access-signin-failure/` remains Conditional Access methodology, not app-consent guidance
- `/everyday-it/scope-the-problem/` remains scoping methodology
- `/everyday-it/verify-before-close/` remains verification methodology
- `/consulting/` remains the consulting bridge

## Production handoff
Jazzy should:
- place KT-000031 immediately after KT-000030 on `/cases/`
- add `/cases/KT-000031/` to `sitemap.xml` exactly once
- normalize the route to current shared accessible case-template conventions
- preserve canonical, social metadata, authorship/date, nav, footer, favicons, headings, fragments, UTF-8, and final newline conventions
- preserve exact locked lesson, supporting principle, investigation path, and status
- add restrained inbound proof link(s) from the cleanest relevant identity/security/consulting methodology route
- preserve outbound links to Scope the Problem, Verify Before Close, Consulting, and only other genuinely relevant existing methodology routes
- add validator coverage for metadata, canonical/article behavior, authorship/date, placement, sitemap uniqueness, exact locked text, request-path correction, publisher/app review, requested-scope review, admin-review verification, least-necessary approval, post-consent functional testing, non-universal claims, revalidation requirement, proof-layer positioning, and sanitization
- add no downloadable derivative
- run full static-site validation
