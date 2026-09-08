# KT-000020 Production Handoff

## Route
`/cases/KT-000020/`

## Case
**KT-000020 | Public Website Failed Internally Because DNS Owned the Name**

## Source
Sanitized engineering source: `engineering-extraction-batch-008.md`, EX-008-02.

## Locked lesson
**If a website works everywhere except inside the company, check split-brain or split-horizon DNS before blaming filtering.**

## Supporting principle
**Works outside but not inside is a location boundary. Compare name resolution before changing more security controls.**

## Investigation path
**External test → Internal test → Filtering visibility → Whitelist result → Internal DNS → Public resolver comparison → DNS correction → Internal retest**

## Status
**DNS Corrected / Internal Access Verified**

## Evidence boundary
The source supports:
- the public website worked from outside networks
- systems inside the company network could not reach it
- internal failure occurred before traffic appeared in the expected web-filtering platform
- whitelisting did not change the result
- firewall redirection and DNS were considered
- local DNS name resolution was identified as the failure domain
- the public domain overlapped with the organization's internal DNS namespace
- internal DNS behavior was corrected
- internal users could reach the public website afterward

Do not claim:
- every inside-only website failure is caused by split DNS
- the web filter or firewall can never cause this symptom
- every overlapping internal/public namespace is necessarily broken
- a single universal DNS correction applies to every environment
- a public web outage was proven
- exact customer DNS zone names, IP addresses, hostnames, or infrastructure identifiers

## Intent separation
- `/cases/KT-000020/` is the proof layer
- `/tutorials/dns-active-directory-domain-health/` remains the reusable DNS/AD investigation tutorial
- `/everyday-it/known-good-comparison/` remains comparison methodology
- `/everyday-it/scope-the-problem/` remains symptom-boundary methodology
- `/everyday-it/verify-before-close/` remains verification methodology

## Required outbound links
- `/tutorials/dns-active-directory-domain-health/`
- `/everyday-it/known-good-comparison/`
- `/everyday-it/scope-the-problem/`
- `/everyday-it/verify-before-close/`

## Production integration requirements
- place KT-000020 immediately after KT-000019 on `/cases/`
- add `/cases/KT-000020/` to `sitemap.xml` exactly once
- normalize case page to current shared navigation/template conventions
- add restrained inbound proof from `/tutorials/dns-active-directory-domain-health/`
- add restrained inbound proof from `/everyday-it/known-good-comparison/` or `/everyday-it/scope-the-problem/` if the graph remains clean
- preserve the inside-versus-outside comparison as the core diagnostic boundary
- preserve filtering/whitelisting as failed tests that redirected the investigation, not as universally irrelevant layers
- preserve split-DNS wording as a supported case finding, not a universal diagnosis
- keep customer-identifying data removed
- do not add a downloadable derivative

## Validator requirements
Enforce:
- exact browser/social title
- exact social description
- canonical behavior
- article type
- approved author markup
- publication date
- locked lesson
- supporting principle
- exact investigation path
- exact status
- placement immediately after KT-000019
- sitemap uniqueness
- required outbound links
- required inbound proof links
- inside-versus-outside comparison boundary
- internal DNS failure-domain wording
- no universal split-DNS claim
- proof-layer positioning

## Validation
Run full static-site validation, navigation, headings, fragments, favicons, metadata, accessibility, encoding, final newlines, and release-integrity checks.

Keep the PR Draft until integration is complete. Do not merge automatically.
