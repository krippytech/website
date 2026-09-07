# Flagship: VPN Connected, But Nothing Works

## Purpose

Add a distinct post-connect VPN troubleshooting asset without duplicating either the broad VPN connection guide or the existing mapped-drive-specific guide.

This route owns the search and support intent where the VPN tunnel is established but the user still cannot reach or use one or more internal resources.

## Canonical route

`/everyday-it/vpn-connected-but-nothing-works/`

## Locked principle

**A successful VPN connection proves the tunnel came up. It does not prove the user's required resource works.**

Supporting line:

**Treat connected as a checkpoint. Prove the path to the resource.**

## Decision path

**Resource → DNS → Route → Service → Identity → Permission**

The route should make each layer useful and testable:

1. Name the exact resource.
2. Test internal name resolution.
3. Test required routes and reachability.
4. Test the actual service or protocol.
5. Confirm which identity is being presented.
6. Confirm intended authorization and effective permissions.

## Distinct intent boundaries

### Existing broad authority

`/everyday-it/vpn-troubleshooting/`

Owns VPN connection establishment and pre-connect layers:

- client
- gateway/server address
- reachability to the VPN service
- credentials
- MFA
- backend authentication
- transition into post-connect testing

### Existing specific support route

`/everyday-it/vpn-mapped-drive/`

Owns the file-access branch after the tunnel connects:

- exact UNC path
- DNS/server reachability
- SMB/share path
- mapped drive state
- identity
- share and NTFS permissions

### New flagship

`/everyday-it/vpn-connected-but-nothing-works/`

Owns the broader post-connect problem before the technician knows whether the failed resource is a file share, internal web app, RDP host, database, printer, line-of-business application, or other internal endpoint.

Do not collapse these three intents into one page.

## Known-good comparison model

Preserve these comparisons:

- same user, different device
- same device, different network
- same VPN, different user
- same resource, several remote users

The point is to isolate endpoint, local network, user/identity, or shared infrastructure before making changes.

## Common traps

Do not encourage:

- reinstalling a VPN client that already establishes the tunnel without evidence of a client defect
- using an IP address as a permanent DNS workaround
- broad firewall changes based on one symptom
- granting broad permissions to solve access denied
- treating ping as proof that the required service is healthy

## Safety and escalation boundary

Escalate or move into infrastructure/change-control mode when the fix requires changes to:

- production routes
- VPN address pools
- split tunneling
- firewall policy
- NAT
- network segmentation
- shared DNS
- domain controllers
- identity services
- core application or server infrastructure

Shared-user failures should trigger shared-service triage instead of repeated endpoint changes.

## Internal link intent

The new page should link to:

- `/everyday-it/vpn-troubleshooting/`
- `/everyday-it/vpn-mapped-drive/`
- `/everyday-it/shared-service-outage-triage/`
- `/everyday-it/troubleshooting-first-10-minutes/`

Production integration should add restrained inbound links from the VPN authority page and other genuinely relevant routes. Do not scatter links across unrelated pages.

## Consulting boundary

A Consulting bridge is appropriate only when the work crosses into shared production routing, firewall/security policy, core identity/DNS, network architecture, undocumented dependencies, or another high-risk shared-system boundary.

Do not turn routine endpoint troubleshooting into a sales CTA.

## Production integration for Jazzy

- add the route to the Everyday IT landing page in a meaningful VPN/remote-access position
- add the route to `sitemap.xml` exactly once
- add validator expectations for canonical metadata and article social metadata
- add a prominent inbound link from `/everyday-it/vpn-troubleshooting/`
- add restrained relevant inbound links where they materially improve the decision graph
- preserve all existing useful VPN and mapped-drive content
- verify the new route does not cannibalize the mapped-drive page
- preserve accessibility, navigation, canonical, favicon, encoding, heading, fragment, and final-newline conventions
- run full static-site validation

Do not create a downloadable derivative in this PR. First lock the web asset and internal graph.