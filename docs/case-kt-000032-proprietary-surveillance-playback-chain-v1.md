# KT-000032 | Proprietary Surveillance Export Failed in Its Playback Chain

## Source
EX-006-08 from `engineering-extraction-batch-006.md`.

## Category
Evidence Handling / Application Dependencies

## Status
Playback Chain Isolated / Safer Re-Export Path Recommended

## Locked lesson
A proprietary file that will not play is not automatically corrupt. Prove the format, viewer, dependencies, package completeness, and endpoint behavior before changing the evidence.

## Supporting principle
Preserve the source first. Troubleshoot the playback chain around it before modifying, converting, or replacing the original evidence.

## Investigation path
Preserve source → Identify proprietary format → Test standard players → Test bundled viewer → Capture dependency errors → Test another endpoint → Isolate playback chain → Recommend standard re-export or complete supported player package

## Evidence boundary
- A proprietary surveillance-video export could not be played with normal media players.
- The included viewer launched but produced runtime/dependency errors and blank video.
- The proprietary format was identified.
- Standard media players could not decode it.
- The bundled viewer was tested from multiple locations.
- A missing/incompatible runtime dependency error was captured.
- The package was tested on another endpoint.
- The vendor playback chain was isolated as the relevant fault domain.
- The strongest supported recommendation was a fresh export in a standard format or a complete current standalone-player package.
- The record does not prove the original export itself was corrupt.
- Preserve the complete export folder before troubleshooting.
- Do not install random codec packs for proprietary evidence formats.
- Do not claim all proprietary playback failures share the same root cause.
- Do not claim the exact failed dependency is proven unless the evidence supports it.
- Do not claim a standard-format re-export is always possible.
- Do not publish customer, case, camera, location, filename, timestamp, chain-of-custody, or other identifying/evidentiary details.

## Intent separation
- `/cases/KT-000032/` is the proof layer.
- `/everyday-it/scope-the-problem/` remains scoping methodology.
- `/everyday-it/known-good-comparison/` remains comparison methodology.
- `/everyday-it/verify-before-close/` remains verification methodology.
- `/consulting/` remains the consulting bridge.

## Production handoff
- Place KT-000032 immediately after KT-000031 on `/cases/`.
- Add `/cases/KT-000032/` to `sitemap.xml` exactly once.
- Normalize the page to current shared accessible navigation, footer, favicon, authorship, canonical, article/social metadata conventions.
- Add one restrained inbound proof link from the cleanest relevant troubleshooting, evidence-handling, or consulting route if the graph remains clean.
- Preserve the outbound methodology links listed above.
- Add validator coverage for exact metadata, canonical/article behavior, authorship/date, locked lesson, supporting principle, investigation path, status, placement, sitemap uniqueness, source-preservation framing, proprietary-format identification, standard-player failure, bundled-viewer testing, runtime/dependency evidence, alternate-endpoint testing, playback-chain isolation, re-export/player-package recommendation, corruption non-claim, codec-pack caution, proof-layer positioning, and sanitization.
- Add no downloadable derivative.
- Run full static validation.
