# KT-000015 Production Handoff

## Case
**KT-000015 | Forwarded Mail Failed After Authentication Changed Across Security Layers**

## Purpose
Create the proof-layer case for the Mail Flow & Security cluster. This is a real multi-hop forwarding case, not a generic SPF/DKIM/DMARC tutorial.

## Locked lesson
**A message can be legitimate at hop one and look spoofed at hop four. Troubleshoot the path, not just the sender.**

## Supporting principle
**Authentication results have to be evaluated at the hop that actually rejects the message.**

## Investigation path
**NDR → Rejecting hop → Original authentication → Forwarded authentication → Tracking identifiers → Matched policy → Scoped correction → End-to-end retest**

## Evidence boundary
Preserve these facts:
- a business workflow forwarded mail between organizations and repeatedly hit an administrative-policy rejection
- original delivery authentication could pass
- the forwarded or re-sent copy later showed SPF soft-fail and DKIM/DMARC failure
- the downstream email-security layer rejected the later message
- the full NDR and message headers were collected
- the exact rejecting mail-security service was identified from the SMTP error path
- original authentication results were compared with the forwarded copy
- message and security tracking identifiers were used to locate the policy decision
- anti-spoof, blocked-sender, and forwarding-related policies were reviewed
- the preferred engineering direction was a workflow correction or the narrowest justified exception rather than a global allow
- verification requires identifying the rejecting hop, comparing authentication before and after forwarding, reviewing every security layer, confirming the exact matched policy, and retesting the complete forward path

Do not claim:
- every forwarding failure has this root cause
- the original sender was malicious
- forwarding always breaks SPF, DKIM, or DMARC
- one named security product was universally at fault
- every attempted allow rule in the raw record was the final root fix
- a broad allow list was required
- a permanent final fix was proven if the raw record does not establish that

## Status
**Policy Path Identified / Scoped Correction Required**

## Intent separation
- `/cases/KT-000015/` is proof
- `/everyday-it/microsoft-365-email/` remains broad email authority
- `/everyday-it/message-trace-delivery/` remains delivery and transport evidence guidance
- `/everyday-it/quarantine-delivery-false-positive/` remains detection/action/delivery-state guidance
- `/everyday-it/escalate-with-evidence/` remains escalation methodology

## Production integration for Jazzy
- place KT-000015 immediately after KT-000014 on `/cases/`
- add `/cases/KT-000015/` to `sitemap.xml` exactly once
- add validator coverage for exact title, social description, canonical behavior, article type, approved author markup, and publication date
- add a restrained inbound proof link from `/everyday-it/message-trace-delivery/`
- add a restrained inbound proof link from `/everyday-it/microsoft-365-email/` or `/everyday-it/quarantine-delivery-false-positive/` if the graph remains clean
- preserve outbound links to Microsoft 365 Email, Message Trace and Delivery, Quarantine Delivery or False Positive, and Escalate With Evidence
- keep this as mail-flow/security proof, not a generic authentication standards tutorial
- preserve public-safe sanitization
- do not add a downloadable derivative
- run full static-site validation

## Production report requested
Report exactly what changed, Cases landing placement, sitemap result, validator coverage, inbound and outbound proof links, whether the case remains clearly proof-layer content, whether hop-by-hop authentication remains distinct from original-sender reputation, whether broad allow rules remain explicitly discouraged, validation results, blockers, and whether the PR is ready to move from Draft to Ready for Review.
