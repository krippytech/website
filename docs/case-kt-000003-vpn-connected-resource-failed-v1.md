# KT-000003 - VPN Connected but Internal Resource Still Failed

## Purpose

Add the first proof-layer case for the VPN / Remote Access cluster.

This is a public-safe technical case based on a real troubleshooting record where the VPN session connected successfully but the user's mapped internal resource still failed. The public case removes customer identity, production server names, IP addresses, domains, share names, and authentication details.

## Route

`/cases/KT-000003/`

## Locked lesson

**A successful VPN connection proves the tunnel came up. It does not prove the user's required resource works.**

## Investigation path

**Tunnel -> Destination -> Identity -> Resource path -> Mapping -> Verify**

The case should reinforce, not replace, the newer flagship decision path:

**Resource -> DNS -> Route -> Service -> Identity -> Permission**

## Evidence boundary

Do not state a single definitive production root cause.

The source record supports these facts:

- VPN connection was restored successfully.
- The mapped internal resource still failed after reconnect/remap attempts.
- Server-address and identity/directory-synchronization changes occurred before successful access.
- A corrected internal path was mapped and verified in File Explorer.

The source record does not prove which individual downstream change was the sole root cause. Preserve that uncertainty in the public case.

## Intent separation

- `/everyday-it/vpn-troubleshooting/` remains broad tunnel-establishment authority.
- `/everyday-it/vpn-connected-but-nothing-works/` remains the broad post-connect diagnostic guide.
- `/everyday-it/vpn-mapped-drive/` remains the focused mapped-drive / SMB branch.
- `/cases/KT-000003/` is proof: it shows how the judgment played out in a real troubleshooting record.

## Production integration for Jazzy

- Add KT-000003 to `/cases/` after KT-000002.
- Add `/cases/KT-000003/` to `sitemap.xml` exactly once.
- Add validator coverage for exact title, social description, canonical, and article type.
- Add a restrained proof/case link from `/everyday-it/vpn-connected-but-nothing-works/`.
- Add a restrained case link from `/everyday-it/vpn-mapped-drive/` if the graph remains clean.
- Preserve all public-safe sanitization.
- Preserve the explicit uncertainty around root cause.
- Do not add a downloadable derivative.
- Run full static-site validation.

## Review rule

Do not convert the root-cause section into a stronger claim than the source record supports. The value of the case is that it demonstrates disciplined troubleshooting under uncertainty.
