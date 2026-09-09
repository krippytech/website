# KT-000023 | Intermittent Internet and RDP Drops Required Continuous Evidence

## Purpose

Proof-layer case for intermittent WAN, ISP, RDP, and cloud-path troubleshooting where point-in-time tests often appeared healthy and continuous evidence was required to prove changing fault domains.

## Locked lesson

**Intermittent network problems are not disproven by a clean five-minute test. Measure the path over time.**

## Supporting principle

**Continuous evidence turns “the Internet feels slow” into something a carrier can act on.**

## Investigation path

**User reports → Continuous monitoring → LAN/WAN comparison → Loss and latency evidence → Carrier escalation → Transport repair → Retest → Cloud-path comparison → Fault-domain reclassification**

## Status

**Carrier Fault Confirmed / Remaining Path Reclassified**

## Source evidence

The source supports that:

- users reported repeated remote-session drops and Internet instability
- many point-in-time tests looked normal
- continuous monitoring captured intermittent loss/outages
- packet loss, outages, latency spikes, and restoration periods were documented
- internal and Internet targets were compared to help distinguish LAN health from WAN instability
- the ISP was escalated with source/destination information
- the ISP/NOC confirmed a transport-path issue during part of the incident
- testing continued after carrier remediation
- later ping/traceroute evidence showed healthy ISP delivery into a cloud provider network for a tested destination
- traceroute timeouts alone were not treated as proof of failure when the final destination remained reachable
- the incident spanned recurring symptoms and changing network conditions

## Evidence boundaries

Do not claim:

- every remote-session drop came from the same carrier fault
- every Internet symptom shared one universal root cause
- traceroute timeouts alone prove a failed network path
- a healthy post-repair ISP path proves every upstream/cloud component is healthy
- the carrier repair permanently resolved every recurring symptom in the broader ticket
- a specific customer, ISP, cloud provider, public IP, internal IP, hostname, circuit identifier, or ticket number

## Intent separation

- `/cases/KT-000023/` is proof-layer content
- `/everyday-it/scope-the-problem/` remains symptom-boundary methodology
- `/everyday-it/known-good-comparison/` remains comparison methodology
- `/everyday-it/verify-before-close/` remains verification methodology

## Required outbound links

- `/everyday-it/scope-the-problem/`
- `/everyday-it/known-good-comparison/`
- `/everyday-it/verify-before-close/`

## Production integration requirements

- place KT-000023 immediately after KT-000022 on `/cases/`
- add `/cases/KT-000023/` to `sitemap.xml` exactly once
- normalize the page to current shared navigation/template conventions
- add restrained inbound proof from Scope the Problem and/or Known-Good Comparison if the graph remains clean
- preserve the continuous-monitoring and changing-fault-domain lesson
- preserve traceroute as path evidence, not a binary pass/fail test
- preserve carrier fault as confirmed only for part of the incident
- preserve later healthy ISP delivery to one tested cloud destination as a reclassification clue, not universal proof
- keep customer-identifying data removed
- no downloadable derivative

## Validator requirements

Add strictly additive validation for:

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
- placement after KT-000022
- sitemap uniqueness
- required outbound/inbound proof links
- continuous-monitoring requirement
- LAN/WAN comparison language
- carrier-confirmed transport issue boundary
- post-repair retest requirement
- traceroute non-binary boundary
- changing-fault-domain language
- no universal-root-cause claim
- proof-layer positioning
- full static-site validation, navigation, headings, fragments, favicons, metadata, accessibility, encoding, and final newlines
