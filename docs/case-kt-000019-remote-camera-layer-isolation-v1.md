# KT-000019 — Remote Camera Failure Was Isolated Layer by Layer

## Purpose

Public-safe proof case showing why camera and audio failures in remote-session workflows must be isolated across physical hardware, local Windows, redirection, the remote Windows session, and the conferencing application.

## Source

Primary sanitized source: `engineering-extraction-batch-004-rich.md`, EX-004-06, supported by EX-004-08 only for the multi-installation/VDI normalization boundary.

## Locked lesson

**"Zoom issue" is only the symptom. Prove the camera path before blaming the application.**

## Supporting principle

**The same symptom can exist at different layers. Test the layers in order.**

## Investigation path

**Physical hardware → Local Windows detection → Local app test → Remote-session redirection → Remote Windows detection → Conferencing app → Real workflow verification**

## Status

**Layers Isolated / Working Path Verified**

## Evidence preserved

- Multiple users experienced recurring Zoom camera/audio failures involving physical endpoints and remote Windows sessions.
- Camera behavior was compared locally and inside remote sessions.
- Some cases showed the camera missing in both the Windows Camera application and Zoom.
- Windows updates and remote-session reboots were used where appropriate.
- Local hardware drivers, BIOS/firmware, chipset, audio, and video components were updated where evidence pointed to those layers.
- Webcam firmware was updated in at least one case.
- External camera hardware was replaced or tested where necessary.
- Zoom was retested after changes.
- In one documented instance, updating Windows in the remote session and rebooting restored camera detection and Zoom operation.
- The broader batch contains multiple incidents and does not prove one universal root cause.

## Evidence boundaries

Do not claim:

- every camera/audio failure in a remote session is caused by Zoom
- every case was caused by Windows updates
- every case was caused by camera firmware, BIOS, chipset, drivers, or physical hardware
- every case was caused by redirection
- one universal root cause existed across the batch
- the incomplete EX-004-08 incident had a fully proven root cause
- reinstalling or cleaning Zoom/VDI components is always the first step

Keep the case centered on fault-domain isolation and ordered testing.

## Verification

1. Verify the camera locally in the Windows Camera application.
2. Verify microphone/audio locally.
3. Verify the device is presented inside the remote session.
4. Verify Windows and remote-session updates.
5. Test Zoom using its test workflow.
6. Reboot after driver/firmware/update changes.
7. Validate with a real meeting when business impact is high.

## Intent separation

- `/cases/KT-000019/` is proof-layer content.
- `/everyday-it/known-good-comparison/` owns the local-vs-remote comparison methodology.
- `/everyday-it/repair-rebuild-replace-workstation/` remains workstation decision guidance.
- `/everyday-it/verify-before-close/` remains verification methodology.

## Integration target

- Add KT-000019 immediately after KT-000018 on `/cases/`.
- Add `/cases/KT-000019/` to `sitemap.xml` exactly once.
- Add a restrained inbound proof link from Known-Good Comparison and, if the graph remains clean, Repair/Rebuild/Replace a Workstation.
- Preserve outbound links to Known-Good Comparison, Repair/Rebuild/Replace a Workstation, and Verify Before Close.
- Add validator coverage for exact title/social description, canonical, article type, approved author, publication date, locked lesson, supporting principle, exact investigation path, exact status, Cases placement, sitemap uniqueness, inbound/outbound links, multi-layer boundary, non-universal-root-cause boundary, and proof-layer positioning.
- No downloadable derivative.
