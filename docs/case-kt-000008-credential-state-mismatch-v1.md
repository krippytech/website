# KT-000008 - Different Systems Accepted Different Password States

## Purpose

Add the proof-layer case for the Identity / Passwords / MFA cluster.

This is a public-safe technical case based on a real authentication incident where a hosted desktop and Microsoft 365/cloud applications accepted different password states after a service disruption. Accounts were not locked, MFA remained functional, and the identity path had to be tested system by system before credential state was normalized.

## Route

`/cases/KT-000008/`

## Locked lesson

**When credentials appear to diverge, map the actual identity path and prove where the old versus new credential is being accepted.**

## Investigation path

**Account state -> Identity boundary -> Accepted credential -> Sync state -> SSO/MFA reauth -> Controlled reset -> Cross-system verify**

The case should reinforce, not replace, the broad authority lesson from Passwords & MFA:

**Stop treating every sign-in problem like a password problem.**

## Evidence boundary

The source record supports these facts:

- Users experienced authentication failures across a hosted desktop and Microsoft 365/cloud applications.
- The hosted environment and cloud applications accepted different password states.
- Affected accounts were not locked.
- MFA remained functional.
- Hosted-desktop sign-in and cloud-application sign-in were tested separately.
- The affected identity state was re-synchronized.
- Applications relying on SSO/MFA were reauthenticated.
- Repeated sign-out/sign-in testing was performed.
- A controlled password reset was performed and the new credential was validated across required applications and the hosted session.
- A domain-connected laptop could require connection to the appropriate network before learning the changed password.
- Credential state was normalized successfully.

Do not claim a specific Microsoft service defect, hosted-provider defect, synchronization product defect, or exact backend root cause. The source explicitly says the mismatch and successful normalization are strongly documented, but the exact defect is not proven.

## Intent separation

- `/everyday-it/passwords-mfa/` remains the broad authentication authority.
- `/cases/KT-000008/` is proof: it shows a real cross-system credential mismatch and the testing sequence used to normalize it.
- `/everyday-it/known-good-comparison/` remains supporting troubleshooting methodology.
- `/everyday-it/verify-before-close/` remains verification methodology.
- `/everyday-it/escalate-with-evidence/` remains the escalation branch when identity boundaries still disagree.

## Production integration for Jazzy

- Add KT-000008 to `/cases/` immediately after KT-000007.
- Add `/cases/KT-000008/` to `sitemap.xml` exactly once.
- Add validator coverage for exact title, social description, canonical, `article` type, approved author markup, and publication-date markup.
- Add a restrained proof/case link from `/everyday-it/passwords-mfa/`.
- Add a restrained case link from `/everyday-it/known-good-comparison/` if the graph remains clean.
- Preserve Passwords & MFA as the broad authority.
- Preserve public-safe sanitization.
- Preserve the evidence boundary that credential mismatch and successful normalization are proven, while the exact backend defect is not.
- Do not add a downloadable derivative.
- Run full static-site validation.

## Review rule

Do not turn this into a generic password-reset tutorial or claim one vendor caused the mismatch. The proof value is that connected systems accepted different credential states, the boundaries were tested separately, and the identity state was normalized and verified across the required workflows.
