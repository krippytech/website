# KT-000011 Source Boundary

## Case

**KT-000011 | Office APPCRASH Survived Repair and Reinstall**

## Source

Engineering extraction: **EX-009-03 — Outlook APPCRASH Persisted Through Repair/Reinstall Because a Component File Was Bad**

## Locked lesson

**If a failure survives repair and reinstall, stop repeating the same broad fix. Identify what is actually faulting and prove the next layer.**

Supporting principle:

**A reinstall is evidence, not magic.**

## Investigation path

**Crash evidence → Time correlation → Broad repair → Reproduce → Reinstall → Reproduce → Exact component → Known-good replacement → Workflow verification**

## Evidence supported by source

- Outlook produced repeated Microsoft Office component crash dialogs while remaining partially usable.
- APPCRASH details identified the faulting Office executable.
- The beginning of the issue was correlated with a prior server/update event.
- Office repair, update rollback, and a new Outlook profile were attempted.
- The affected Office component/application was reinstalled.
- The error persisted after those broader remediation attempts.
- The identified executable was replaced with a known-good copy from another matching Office installation.
- Repeated Outlook send/reply testing followed the replacement.
- The repeated crash stopped after replacement of the bad Office component.

## Do not overclaim

Do not claim:

- a universal Microsoft Office defect,
- a Microsoft 365 service incident,
- that the earlier server/update event was the proven root cause,
- that every APPCRASH surviving reinstall should be fixed by copying binaries,
- that any arbitrary Office executable can safely be replaced from another system,
- that version compatibility can be ignored.

The public case must preserve the source requirement to validate file/version compatibility before any component replacement.

## Intent separation

- `/cases/KT-000011/` is the real-world proof layer.
- `/everyday-it/known-good-comparison/` remains the comparison methodology.
- `/everyday-it/workaround-vs-resolution/` remains outcome classification guidance.
- `/everyday-it/verify-before-close/` remains verification methodology.
- `/everyday-it/escalate-with-evidence/` remains evidence-driven escalation guidance.

Do not convert KT-000011 into a generic Office reinstall tutorial or a binary-replacement how-to.

## Publication safety

Use only public-safe, generalized environment details. Do not expose customer names, user identities, workstation/server names, private file paths, tenant details, or ticket identifiers.
