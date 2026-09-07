# Flagship Asset: Troubleshooting First 10 Minutes Checklist v1

Status: Draft content handoff for production integration.

## Search-control role

This is the flagship support asset for the Practical IT Troubleshooting Methodology cluster.

Primary authority page:
- `/everyday-it/troubleshooting-paths/`

New flagship route:
- `/everyday-it/troubleshooting-first-10-minutes/`

Search intent to own:
- IT troubleshooting checklist
- first 10 minutes troubleshooting
- IT troubleshooting worksheet
- how to start troubleshooting an IT problem
- troubleshooting steps before making changes

Do not create another broad troubleshooting authority page. This route is the reusable field asset beneath Troubleshooting Paths.

## Locked principle

**The first 10 minutes should reduce uncertainty, not create more variables.**

Supporting sequence:

**Symptom → Time → Scope → Known-good → Layer → Evidence → Next test → Safety/Rollback → Verify → Escalate**

The page should feel usable during a live incident, not like a conceptual essay.

## Content purpose

The worksheet is designed to make the technician leave the first ten minutes with:
1. a precise, testable symptom;
2. a last-known-good / first-known-bad boundary where possible;
3. a defined scope;
4. at least one meaningful known-good comparison;
5. a working hypothesis about the failing layer;
6. preserved evidence;
7. one safe next test that separates plausible causes;
8. an explicit risk/rollback boundary before change;
9. a real business-workflow verification target;
10. a clear escalation trigger and evidence package.

The ten-minute framing is a discipline, not a promise to resolve the incident within ten minutes.

## Safety boundary

Keep the asset evidence-first and change-light.

It must not encourage:
- blanket password/MFA resets before evidence points there;
- broad Conditional Access or security exclusions;
- blind copying of groups, ACLs, policies, routes, or permissions from a working user;
- casual restarts of shared servers, firewalls, hypervisors, network infrastructure, or other production systems;
- destructive disk/filesystem repair before protecting data;
- profile rebuilds, reinstallations, tenant changes, or multiple simultaneous resets as first-line discovery;
- bypasses being described as permanent resolutions.

When the next useful step can affect shared infrastructure, privileged access, security controls, production data, backups, mail flow, identity architecture, or multiple users, move to risk assessment, rollback, approval, evidence preservation, and escalation.

## Relationship to existing methodology pages

This route should link naturally to:
- `/everyday-it/troubleshooting-paths/`
- `/everyday-it/scope-the-problem/`
- `/everyday-it/known-good-comparison/`
- `/everyday-it/change-safety-rollback/`
- `/everyday-it/verify-before-close/`
- `/everyday-it/workaround-vs-resolution/`
- `/everyday-it/escalate-with-evidence/`
- `/everyday-it/prevent-recurrence/` where natural

The authority page should return-link to this asset prominently near the beginning/lifecycle section. Scope, known-good, change-safety, verify-before-close, and escalate-with-evidence are strong candidates for restrained inbound links where the worksheet genuinely helps.

## Search and hierarchy rules

Authority relationship:

`Troubleshooting Paths` → `First 10 Minutes Checklist` → narrow methodology guides → symptom/product-specific guides

This page should not compete with Troubleshooting Paths for broad ownership. It should own the actionable worksheet/checklist intent.

Recommended production title:
`IT Troubleshooting First 10 Minutes Checklist | Everyday IT | KrippyTech`

Recommended H1:
`The first 10 minutes should reduce uncertainty, not create more variables.`

Recommended meta description:
`A practical first-10-minutes IT troubleshooting worksheet for reducing uncertainty, scoping impact, comparing known-good states, identifying the failing layer, preserving evidence, and choosing a safe next test.`

## Reuse plan

After the web asset is merged and stable, it can be reused as:
- a printable one-page or two-page worksheet/download;
- a GitHub Markdown checklist or field template that points back to the canonical KrippyTech guide;
- a LinkedIn field lesson built around the locked principle;
- an internal KER/ticket triage worksheet.

Do not duplicate the full article into external footprints. External versions should be compact derivative assets that reinforce the canonical web page.

## Jazzy production integration

Preserve the locked principle and checklist order.

Complete:
1. add the route to the Everyday IT landing page;
2. add the canonical route to `sitemap.xml` exactly once;
3. add validator expectations for title, OG/Twitter description, article type, and any route-specific invariants used by current validation;
4. add a strong inbound link from `/everyday-it/troubleshooting-paths/`, preferably near the top or lifecycle/start section;
5. add natural inbound links from Scope the Problem, Known-Good Comparison, Change Safety & Rollback, Verify Before Close, and Escalate With Evidence where useful without link stuffing;
6. preserve the current outbound methodology links;
7. keep the Consulting bridge restrained to the risk boundary, not routine first-line troubleshooting;
8. normalize navigation, active state, favicons, canonical/OG/Twitter metadata, accessibility, headings, fragments, encoding, and final newline to current production conventions;
9. run full static-site validation;
10. report exact files changed, inbound/outbound links, landing/sitemap/validator integration, validation result, blockers, and whether the PR is ready to leave Draft.

Do not create the downloadable PDF/printable asset in this PR unless explicitly requested. First lock the canonical web asset and its internal search graph.
