# KT-000014 Production Handoff

## Case

**KT-000014 | Legacy Application Upgrade Required Database Validation and Sequencing**

Route: `/cases/KT-000014/`

Category: **Line-of-Business Application Lifecycle**

Status: **Upgraded / Workflow Verified**

## Source

Sanitized engineering source: `engineering-extraction-batch-009.md`, EX-009-05.

## Locked lesson

**For database-backed line-of-business software, the installer completed is not verification.**

## Supporting principle

**Protect the data, follow the supported order, then prove the workflow.**

## Investigation path

**Application error → Vendor interpretation → Pre-change integrity → Backup → Server-side upgrade → Required version sequence → Client update → Post-change integrity → Business workflow verification**

## Evidence boundary

The source supports:

- a legacy line-of-business application produced an error tied to an outdated application version rather than Java alone
- vendor support was contacted to interpret application-specific errors
- data and integrity checks were run before the upgrade
- known or acceptable historical database errors were identified before proceeding
- a large manual backup of application data was completed
- the host or server installation was updated first
- workstation clients updated afterward
- a separate application instance required intermediate versions to be installed sequentially
- final data and integrity checks were run
- functional payment testing was performed
- the application was successfully upgraded
- users verified normal production workflows

Do not claim:

- every database-backed application requires this exact sequence
- Java was irrelevant in every similar incident
- every application must upgrade server-first
- every version can or cannot be skipped without vendor guidance
- the historical database errors were caused by the upgrade
- vendor support can be omitted
- a completed installer alone proves success
- any private application, customer, server, database, version, licensing, or error-code detail

## Intent separation

- `/cases/KT-000014/` is the proof layer
- `/everyday-it/change-safety-rollback/` remains change-safety methodology
- `/everyday-it/troubleshooting-first-10-minutes/` remains initial troubleshooting methodology
- `/everyday-it/verify-before-close/` remains verification methodology
- `/everyday-it/escalate-with-evidence/` remains evidence-driven escalation guidance

Do not turn KT-000014 into a generic application-upgrade tutorial or a vendor-specific installation guide.

## Production integration for Jazzy

- place KT-000014 immediately after KT-000013 on `/cases/`
- add `/cases/KT-000014/` to `sitemap.xml` exactly once
- add validator coverage for exact title, social description, canonical behavior, `article` type, approved author markup, and publication-date markup
- add restrained inbound proof links from Change Safety and Rollback and Verify Before Close if the graph remains clean
- preserve outbound links to Change Safety and Rollback, Troubleshooting: The First 10 Minutes, Verify Before Close, and Escalate With Evidence
- preserve public-safe sanitization
- preserve navigation, accessibility, favicons, headings, fragments, encoding, and final newlines
- add no downloadable derivative
- run full static-site validation

## Acceptance boundary

The case must remain a proof case about safe lifecycle sequencing and verification. Its core conclusion is not that one installer failed. Its core conclusion is that a database-backed application upgrade had to be treated as a controlled data and application lifecycle operation.
