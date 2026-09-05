# KrippyTech Batch Intake Standard

**Version:** 1.0

## Purpose

This standard defines how raw technical material is grouped, sanitized, mined, and handed into the content ledger.

The objective is simple: make large ticket exports useful without turning the source library into an unsearchable pile.

## Batch Philosophy

Batches should be grouped by technical theme, not by arbitrary page count.

Typical batch size may vary. A focused 100-page batch is better than a mixed 300-page batch when the smaller batch produces cleaner extraction.

Do not aggressively clean source notes before mining. Strange symptoms, failed attempts, partial fixes, and escalation decisions often contain the most useful lessons.

## Permanent Batch Domains

Use these prefixes for new sanitized source packs:

- `01 Identity & Access`
- `02 Microsoft 365 & Email`
- `03 SharePoint & OneDrive`
- `04 Windows & Workstations`
- `05 Remote Access & VPN`
- `06 Printers, Scanners & MFP`
- `07 File Servers & SMB`
- `08 Servers & Infrastructure`
- `09 Security & Incident Response`
- `10 Advanced / KER`

A source may contain material for several domains. Place it in the domain representing the primary engineering lesson and create secondary ledger entries where needed.

## Naming Convention

Use:

`Batch <domain>-<sequence> - <short theme>`

Examples:

- `Batch 02-001 - Outlook and Exchange`
- `Batch 03-001 - SharePoint and OneDrive`
- `Batch 05-002 - VPN and Remote Access`
- `Batch 07-001 - File Access and NTFS Permissions`

Legacy files such as `Batch 00022.docx` should remain unchanged as raw historical sources. Their extracted material can be assigned to the new domain model without renaming the original.

## Intake Stages

### Stage A: Raw

Store the original source unchanged.

Record:
- original filename
- rough date range if known
- likely domains
- whether the source contains screenshots/logs

### Stage B: Sanitization

Create a safe working copy.

Remove or replace identifying information while preserving the technical sequence.

Credentials must never survive into a sanitized source pack.

If a technical value is necessary to understand the lesson, generalize it.

Examples:
- `SERVER01` → `FILE-SERVER`
- `192.0.2.75` → `internal server IP`
- `user@client.example` → `user@company.example`

### Stage C: Extraction

For every useful technical pattern, capture:

- symptom
- environment
- evidence
- decision point
- action
- result
- lesson
- warning or escalation boundary

Do not require a full resolution before extracting value. A failed path may itself be a useful lesson.

### Stage D: Deduplication

Before creating a new content candidate, check whether the lesson is:

- already published
- already planned
- better as an enhancement
- a duplicate source supporting an existing lesson

Duplicate source evidence is valuable. Duplicate pages are usually not.

### Stage E: Ledger Entry

Every retained lesson receives a ledger record before public development begins.

## Extraction Template

Use this compact format when mining source material:

### Lesson

**Working title:**

**Primary domain:**

**Source:**

**Symptom:**

**What mattered:**

**Diagnostic path:**

**Resolution or decision:**

**Verification:**

**What not to do:**

**Escalation boundary:**

**Candidate type:** Everyday IT / Enhancement / KER / KT Case / Checklist / Download / Course / Consulting

**Priority:** High / Medium / Low

## Source Quality

### Strong source

Contains several of:
- exact symptom
- concrete diagnostic evidence
- meaningful decision point
- known root cause
- verified resolution
- useful failed attempts
- clear escalation boundary

### Supporting source

Confirms a pattern already seen elsewhere but does not justify a standalone lesson alone.

### Weak source

Contains mostly scheduling, client chatter, incomplete context, or a resolution with no technical explanation.

Weak sources may be ignored unless they support another item.

## Privacy Gate

Before material leaves the source layer, check for:

- passwords and secrets
- customer names
- company names
- email addresses
- domains
- phone numbers
- physical addresses
- ticket numbers
- identifying server/workstation names
- internal URLs
- confidential correspondence
- legal or regulated information

If privacy cannot be preserved without destroying the lesson, keep the material inside KER and do not publish it.

## Completion Definition

A batch is complete when:

1. useful lessons have been extracted
2. each retained lesson is represented in the ledger
3. duplicates are linked instead of recreated
4. privacy-sensitive material has not crossed into public drafts
5. high-value next actions are identifiable

The goal is not to publish every item in the batch. The goal is to preserve every worthwhile lesson and know what to do with it.
