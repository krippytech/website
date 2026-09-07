# KT-000010 Production Handoff

## Case

**KT-000010 | Printer Test Page Worked but Application Printing Failed**

Route:

`/cases/KT-000010/`

## Purpose

Add the proof-layer case for the Printer / MFP search family.

This case proves that a successful network response and Windows test page do not prove the user's real application workflow. It should remain a proof case, not expand into a generic printer tutorial.

## Locked lesson

**A Windows test page proves the printer path can work. It does not prove the user's actual application workflow works.**

Supporting principle:

**Printer validation is layered: network, spooler, queue, driver, application, document, and device options.**

## Investigation path

**Network → Test page → Simple application → Business application → Queue selection → Reopen/retest → Verify**

## Evidence boundary

The source supports all of the following:

- the printer responded on the network
- a Windows test page printed successfully
- a simple text application printed successfully
- the first PDF application test failed
- an alternate application could print the same content
- switching the active queue and reopening the PDF application restored printing
- the default queue was set for ordinary work
- the color-production queue was clearly named for intentional selection
- final verification included the actual PDF application workflow

Do not claim:

- a hardware defect was proven
- a universal printer failure was present
- a single global driver defect was proven
- the Windows test page proved end-to-end printing
- the PDF document itself was corrupt

## Intent separation

- `/everyday-it/printers/` remains the broad Printer Troubleshooting authority
- `/cases/KT-000010/` is the real-world proof layer
- `/everyday-it/known-good-comparison/` remains general comparison methodology
- `/everyday-it/verify-before-close/` remains verification methodology
- `/everyday-it/escalate-with-evidence/` remains evidence/escalation methodology

Do not create a derivative download from this case.

## Production integration requested from Jazzy

1. Place KT-000010 immediately after KT-000009 on `/cases/`.
2. Add `/cases/KT-000010/` to `sitemap.xml` exactly once.
3. Add validator expectations for:
   - exact title
   - social description
   - canonical behavior
   - article social type
   - approved author markup
   - publication-date markup
4. Add a restrained inbound proof link from `/everyday-it/printers/`.
5. Add a restrained inbound proof link from `/everyday-it/known-good-comparison/` if the graph remains clean.
6. Preserve the existing outbound proof links from the case.
7. Preserve navigation, favicons, accessibility, heading structure, valid fragments, encoding, and final newlines.
8. Run the full static-site validator.
9. Keep the PR Draft until the production pass and description cleanup are complete.
10. Do not merge.

## Source

Promoted from EX-018-08 in `engineering-extraction-batch-018.md`.

The source characterizes the case as High engineering value and explicitly notes that printer validation is layered and that a passing test page clears only part of the path.
