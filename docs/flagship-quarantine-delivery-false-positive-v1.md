# Flagship: Quarantine, Delivery, or False Positive?

## Route
`/everyday-it/quarantine-delivery-false-positive/`

## Cluster
Security First Response

## Search/control purpose
Own the practical first-response question that appears after a security product raises an alert but the technician still needs to determine what actually happened to the item.

This route should answer:
- Was the item only detected, or actually blocked?
- Was it quarantined before or after delivery or execution?
- Did the user interact with it?
- What evidence is needed before calling it a false positive?
- When should the technician stop and escalate?

## Locked principle
**Do not confuse detection with outcome. First prove what happened. Then decide what it means.**

## Decision path
**Detection → Action taken → Delivery state → User impact → Evidence → False-positive decision**

## Intent separation
- `/everyday-it/malware-alert-first-response/` remains the endpoint malware/threat first-response route, including containment and related evidence.
- `/everyday-it/suspicious-signin-first-response/` remains the identity/sign-in first-response route.
- `/everyday-it/shared-service-outage-triage/` remains shared-service availability triage.
- this route owns the security-action-state question: detected vs blocked vs quarantined vs delivered, then evidence-based false-positive judgment.

## Safety boundary
This is first-response and decision support, not deep incident response.

Do not encourage:
- releasing quarantined content because the user requests it without review
- broad exclusions or allow rules
- disabling security controls
- deleting evidence before review
- reconnecting isolated systems casually
- treating a product's "resolved" badge as proof of safety

## Required branches
The published page should distinguish:
1. detection
2. action taken
3. delivery/execution availability
4. user interaction
5. evidence and correlation
6. false-positive decision
7. escalation boundary

## Internal links
Outbound should include:
- Malware Alert First Response
- Scope the Problem
- Verify Before Close
- Escalate With Evidence

Recommended inbound links during production integration:
- prominent from Malware Alert First Response
- restrained from any relevant broad security section or landing card

## Derivative strategy
No printable/downloadable derivative in this PR. Establish the canonical page and internal graph first.
