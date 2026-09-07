# KT-000013 Production Handoff

## Case

**KT-000013 | Event Logs Proved Unexpected Server Restarts**

Route:
`/cases/KT-000013/`

## Purpose

Add a public-safe Infrastructure / Server Triage proof case showing how a repeated startup or recovery symptom was verified against Windows event evidence before making power, hypervisor, UPS, or hardware conclusions.

## Locked lesson

**The user's pop-up is the symptom. Event logs are the evidence.**

## Supporting principle

**Prove the event before diagnosing the cause.**

## Investigation path

**Reported symptom → Event logs → Unexpected-shutdown proof → Time correlation → Maintenance comparison → Recurrence monitoring → Next infrastructure evidence**

## Evidence boundary

Supported by EX-009-07:

- a remote user repeatedly saw a startup or recovery notice
- Windows event logs were reviewed
- explicit power-failure or unexpected-shutdown records were found
- event timing was correlated with the user's repeated morning notices
- a one-time maintenance restart was separated from repeated unplanned shutdowns
- the incident could then be monitored and escalated based on recurrence
- verification should record exact event times and event IDs
- maintenance and update windows should be compared
- UPS, power, and hypervisor history should be checked when applicable
- recurrence should be monitored before replacing hardware without evidence

Do not claim:

- the final cause of the unexpected shutdowns was proven
- a UPS failure was proven
- a utility power problem was proven
- a hypervisor fault was proven
- a server hardware defect was proven
- hardware replacement was required or completed
- every reboot was unexpected
- a specific Windows Event ID unless the source record provides it

## Status

**Evidence Confirmed / Monitor Recurrence**

## Intent separation

- `/cases/KT-000013/` is the proof layer
- `/everyday-it/troubleshooting-first-10-minutes/` remains broad troubleshooting methodology
- `/everyday-it/escalate-with-evidence/` remains evidence-driven escalation guidance
- `/everyday-it/verify-before-close/` remains verification methodology
- `/everyday-it/workaround-vs-resolution/` remains outcome classification

## Production integration for Jazzy

- place KT-000013 immediately after KT-000012 on `/cases/`
- add `/cases/KT-000013/` to `sitemap.xml` exactly once
- add validator coverage for exact title, social description, canonical behavior, `article` type, approved author markup, and publication-date markup
- add restrained inbound proof links from Troubleshooting: The First 10 Minutes and Escalate With Evidence if the graph remains clean
- preserve outbound links to Troubleshooting: The First 10 Minutes, Escalate With Evidence, Verify Before Close, and Workaround vs Resolution
- keep this a server-triage proof case, not a generic Event Viewer tutorial
- do not add a downloadable derivative
- preserve public-safe sanitization
- run full static-site validation

## Production report requested

Report:

- exactly what changed
- Cases landing placement
- sitemap result
- validator coverage
- inbound and outbound proof links
- whether the case remains clearly a proof layer
- whether the distinction between proving an unexpected shutdown and proving its root cause remains intact
- whether maintenance restarts remain separated from unplanned recurrence
- validation results
- blockers
- whether the PR is ready to move from Draft to Ready for Review
