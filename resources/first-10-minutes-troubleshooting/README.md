# First 10 Minutes IT Troubleshooting

> **The first 10 minutes should reduce uncertainty, not create more variables.**

This is the compact GitHub version of KrippyTech’s troubleshooting method for the opening minutes of an incident.

The goal is not to guess the final fix immediately. The goal is to narrow the problem safely, preserve useful evidence, and choose the next test that teaches you something.

## The sequence

1. **Symptom** — Write the failure in one sentence.
2. **Time** — Identify last known good and first known bad.
3. **Scope** — One user, one device, one location, one resource, or everyone?
4. **Known-good** — Change one dimension and compare the result.
5. **Layer** — Identity, client, network, service, policy, permissions, or data?
6. **Evidence** — Capture exact errors, times, IDs, logs, and observations before changing anything.
7. **Next test** — Choose the smallest test that reduces uncertainty.
8. **Safety / rollback** — Know the impact and how to get back before making a risky change.
9. **Verify** — Test the real business outcome, not just whether a button or service came back.
10. **Escalate** — Stop when risk or uncertainty exceeds the evidence.

## What not to do first

Avoid using broad changes as discovery tools. A blanket password or MFA reset, security exclusion, permission rewrite, shared-system restart, profile rebuild, or destructive repair can hide the original failure and create new variables.

A useful first action should answer a question.

## Fast known-good comparisons

A few comparisons can remove large parts of the troubleshooting tree quickly:

- same user on another device
- another user on the same device
- browser vs desktop client
- another network or location
- known-good path, group, resource, or workflow

Change one dimension at a time. If several things change at once, the result becomes harder to interpret.

## Safety boundary

Stop before changing a shared or high-risk system if you cannot explain the expected impact and rollback.

That includes shared infrastructure, privileged access, security controls, production data, backups, mail flow, identity architecture, and other changes where one troubleshooting step can affect many users or destroy evidence.

## Full KrippyTech resources

The GitHub version is intentionally compact. The canonical guides contain the deeper reasoning, examples, decision paths, and related troubleshooting links.

- **First 10 Minutes guide:** [Read the canonical guide](https://krippytech.com/everyday-it/troubleshooting-first-10-minutes/)
- **Full troubleshooting method:** [Follow the complete method](https://krippytech.com/everyday-it/troubleshooting-paths/)
- **Printable worksheet:** [Download the worksheet PDF](https://krippytech.com/downloads/guides/first-10-minutes/KrippyTech-First-10-Minutes-Troubleshooting-Worksheet.pdf)
- **KrippyTech Downloads:** [Browse practical guides and reviewed tools](https://krippytech.com/downloads/)

## One rule to keep

**Every early troubleshooting action should either reduce uncertainty, preserve evidence, or make the next decision safer.**
