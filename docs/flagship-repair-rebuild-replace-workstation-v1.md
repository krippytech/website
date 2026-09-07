# Flagship: Repair, Rebuild, or Replace a Workstation

## Route

`/everyday-it/repair-rebuild-replace-workstation/`

## Search-control role

This page owns the workstation decision point where the technician has enough evidence to choose among a bounded repair, a clean rebuild, or replacement.

It must remain distinct from:

- `/everyday-it/when-to-replace-workstation/`, which owns replacement signals and when replacement belongs in the conversation.
- `/everyday-it/failing-disk-protect-data-first/`, which owns immediate storage/data-risk handling.
- `/everyday-it/new-pc-setup/`, which owns the controlled transition after rebuild/replacement is approved.
- `/everyday-it/workaround-vs-resolution/`, which owns outcome classification.

## Locked principle

**Do not ask only, “Can this be fixed?” Ask, “Which option restores trust with the least avoidable risk?”**

## Decision path

**Protect data → Classify fault → Read repair history → Choose durable option → Count downtime → Verify workflow**

## Core decision model

### Repair
Use when the fault is narrow, understood, the rest of the platform is healthy, and the repair is likely to be durable.

### Rebuild
Use when the hardware is trustworthy but Windows/software state is not. A rebuild requires known recovery inputs before wiping.

### Replace
Use when repeated failures, hardware concerns, performance limits, downtime cost, or loss of confidence make continued repair the weaker engineering choice.

## Safety boundaries

- Protect data before destructive work when storage, sync, profile, or encryption state is uncertain.
- Do not rebuild on unresolved hardware instability.
- Do not wipe before identifying BitLocker recovery, application licensing, local-only data, line-of-business software, special peripherals, mapped resources, certificates, and identity dependencies.
- Do not call a rebuild or replacement successful merely because Windows boots.
- Verify the user’s actual workflow.

## Production integration for Jazzy

- Add the route to Everyday IT in the Workstations area near `When to Replace a Workstation`.
- Add the canonical route to `sitemap.xml` exactly once.
- Add validator expectations for exact title, social description, canonical behavior, and article type.
- Add a prominent inbound link from `/everyday-it/when-to-replace-workstation/`.
- Add restrained inbound links from workstation/data-risk content when useful without clutter.
- Preserve the distinction between the decision guide and the existing replacement-signals page.
- Preserve the locked principle and six-stage decision path.
- Do not add a downloadable derivative in this PR.
- Run the full static-site validation suite.
