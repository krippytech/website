# KT-000007 - Repeated Scanner Problems Exposed an Aging Workstation

## Purpose

Add the proof-layer case for the Workstation Decisions cluster.

This is a public-safe technical case based on a real workstation where scanner and browser symptoms briefly improved after cleanup, but the system remained at constant 100% CPU and the same workflow failed again within days. The scanner software then would not load or install normally, normal clicks could take 10 to 20 seconds, and the roughly seven-year-old workstation moved from another repair attempt toward replacement planning.

## Route

`/cases/KT-000007/`

## Locked lesson

**A temporary improvement is not a durable repair when the platform remains saturated and the same workflow fails again days later.**

## Investigation path

**Reported workflow -> Temporary cleanup -> Remaining saturation -> Recurrence -> Repair history -> Replacement decision -> Transition planning**

The case should reinforce, not replace, the flagship decision model:

**Protect data -> Classify fault -> Read repair history -> Choose durable option -> Count downtime -> Verify workflow**

## Evidence boundary

The source record supports these facts:

- The visible symptoms included scanner problems and severe browser/workstation slowness.
- Old profiles and temporary data were partially cleaned up.
- After restart, browser and scanner behavior temporarily improved.
- CPU utilization remained at 100%.
- The workstation was described as roughly seven years old.
- Within a few days, the symptoms returned.
- Scanner software would no longer load or install normally.
- Normal interaction could take roughly 10 to 20 seconds between clicks.
- Continuing to work on the system was consuming significant technician time without durable progress.
- Replacement was recommended.
- A replacement quote was requested.

Do not claim that a specific CPU, motherboard, disk, scanner, or Windows defect was proven as the root cause. Do not claim the replacement machine was purchased, deployed, or fully verified. The source proves the replacement decision and quote request, not the completed migration.

## Intent separation

- `/everyday-it/when-to-replace-workstation/` remains the broad replacement-signals authority.
- `/everyday-it/repair-rebuild-replace-workstation/` remains the diagnostic decision flagship.
- `/everyday-it/workaround-vs-resolution/` remains the outcome-classification guide.
- `/everyday-it/new-pc-setup/` remains the transition guide after replacement approval.
- `/cases/KT-000007/` is proof: it shows how recurrence and lifecycle evidence changed the engineering decision from another narrow repair toward replacement.

## Production integration for Jazzy

- Add KT-000007 to `/cases/` immediately after KT-000006.
- Add `/cases/KT-000007/` to `sitemap.xml` exactly once.
- Add validator coverage for exact title, social description, canonical, `article` type, approved author markup, and publication-date markup.
- Add a restrained proof/case link from `/everyday-it/repair-rebuild-replace-workstation/`.
- Add a restrained case link from `/everyday-it/when-to-replace-workstation/` if the graph remains clean.
- Preserve `/everyday-it/repair-rebuild-replace-workstation/` as the decision flagship.
- Preserve `/everyday-it/when-to-replace-workstation/` as the replacement-signals authority.
- Preserve public-safe sanitization.
- Preserve the evidence boundary that replacement was recommended and quoted, but deployment was not proven.
- Do not add a downloadable derivative.
- Run full static-site validation.

## Review rule

Do not convert this into a generic scanner tutorial or invent a single hardware root cause. The proof value is the decision shift: temporary cleanup worked briefly, the platform remained saturated, the same workflow failed again quickly, and continuing another repair cycle no longer restored confidence.
