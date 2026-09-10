# KT-000029 Production Handoff

## Case
KT-000029 | Repeated Full-System Freezes Justified Hardware Escalation

## Source
Sanitized engineering source: `engineering-extraction-batch-018.md`, EX-018-01.

## Locked lesson
**A clean re-image followed by the same full-system failure is evidence that the fault domain may have moved beyond software.**

## Supporting principle
**Temporary improvement is not durable proof. Recurrence after a known-good software baseline should change the next test.**

## Investigation path
**Symptom scope → Cross-application comparison → Network comparison → Software remediation history → Clean re-image → Recurrence → Hardware escalation → Vendor repair → Rebuild → Stress and workflow verification**

## Status
**Hardware Repaired / Post-Repair Testing Passed**

## Evidence to preserve
- failure occurred in more than one meeting application
- full-system freezing, not only one application crash
- network performance from other devices remained normal during reported incidents
- issue persisted through operating-system and driver remediation
- factory re-image produced only temporary improvement
- failure was witnessed during a live meeting
- hardware vendor escalation followed
- returned device appeared to have received a system-board replacement and was factory-reset
- endpoint was rebuilt, patched, and equipped with required business applications
- post-repair GPU load testing completed without visual artifacts or instability
- video-call use was included in post-repair verification

## Boundaries
Do not claim:
- every Teams or Zoom freeze is hardware
- a clean re-image universally rules out software
- the exact failed component was independently proven beyond the vendor repair outcome
- the system-board replacement was documented with more certainty than the source supports
- permanent resolution or a long-duration recurrence-free period
- customer, user, vendor-ticket, serial-number, device, tenant, or other identifying details

## Intent separation
- `/cases/KT-000029/` is the proof layer
- `/everyday-it/scope-the-problem/` remains symptom-boundary methodology
- `/everyday-it/known-good-comparison/` remains comparison methodology
- `/everyday-it/repair-rebuild-replace-workstation/` remains workstation decision methodology
- `/everyday-it/verify-before-close/` remains verification methodology

## Production integration requested
- place immediately after KT-000028 on `/cases/`
- add route to sitemap exactly once
- normalize shared accessible navigation/template conventions
- add restrained inbound proof links from Repair/Rebuild/Replace Workstation, Known-Good Comparison, and/or Scope the Problem if graph remains clean
- preserve outbound links to Scope the Problem, Known-Good Comparison, Repair/Rebuild/Replace Workstation, and Verify Before Close
- add validator coverage for metadata, canonical/article behavior, authorship/date, exact lesson, exact principle, exact investigation path, exact status, placement, sitemap uniqueness, cross-application evidence, full-system symptom, network comparison, remediation history, clean-reimage recurrence, hardware escalation, vendor-repair qualification, post-repair stress/workflow verification, long-duration limitation, non-universal causation, proof-layer positioning, and sanitization
- no downloadable derivative
- run full static validation
