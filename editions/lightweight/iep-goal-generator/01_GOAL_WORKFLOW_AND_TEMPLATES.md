# IEP Goal Generator — Lightweight Forms and Workflow

**Edition:** LIGHTWEIGHT. **Knowledge file 1 of 2.** Paste the separate `projects/iep-goal-generator/PROJECT_INSTRUCTIONS.md` into the AI project's **Instructions** field. This is a support file, not a substitute for the project instructions.

> For setup and testing, use only synthetic or appropriately de-identified information. Do not upload identifiable student records except within a formally authorized educational workflow. These are **drafting aids**; educators and the IEP team make final decisions.

## Step 1 — Student context (intake)

Copy and fill in only what is needed. Use `[NOT PROVIDED]` for unknown items; never fabricate data.

```markdown
### Student context — for drafting only
- Fictional or de-identified working label: [ ]
- Enrolled grade or program: [ ]
- Goal domain (academic, communication, behavior, etc.): [ ]
- Strengths, interests, and preferred learning methods: [ ]
- Instructional language/access considerations: [ ]
- Educational need and effect on curricular access/participation: [ ]
- Existing accommodations, AT/AAC and prompting supports: [ ]
- Previous goal and status, if relevant: [ ]
- Student/parent/teacher input, if provided: [ ]
- IEP annual target date or timeframe: [ ]
- Local district/SELPA rules provided and approved: [ ]
```

Do not request student's name, date of birth, school, IEP number, family contacts, address, or full IEP just to draft a goal. Functional/related-service goals should not be forced onto an irrelevant academic code.

## Step 2 — Present levels and repeatable baseline

```markdown
### Measured present level
- Target observable skill: [ ]
- Assessment/probe and recorded date(s): [ ]
- Materials/task or curriculum context: [ ]
- Task condition, accommodations and prompt level: [ ]
- Observed performance (numerator/denominator or valid units): [ ]
- Number of observations, variation, sample size: [ ]
- Data source / collector role: [ ]
- Educational impact (observed/verified, not inferred): [ ]
- Current instruction supports (document, do not infer): [ ]
- Limitations / missing evidence: [ ]
```

**Baseline gate:** If denominator, task, dates, observed level, or support conditions are missing such that progress cannot be interpreted, label the result `PROVISIONAL — MISSING BASELINE`. Do **not** invent a score or future mastery target.

## Step 3 — Goal request

```markdown
- Mode: [NEW_GOAL / REWRITE_GOAL / GOAL_AUDIT / PROGRESS_UPDATE]
- Domain and specific construct to measure: [ ]
- Related verified standard / crosswalk, if academic: [ ]
- Desired target date/timeframe: [ ]
- Constraints or approved local formatting: [ ]
- Special reporting, generalization or access considerations: [ ]
```

## Step 4 — Proposed annual goal and output

Use the sequence below when drafting. Keep the baseline and annual criterion comparable.

```markdown
## DRAFT — HUMAN IEP TEAM REVIEW REQUIRED
**Status:** [READY FOR TEAM REVIEW / PROVISIONAL — INCOMPLETE]
**Confirmed evidence:** [dated sources]
**Assumptions / needs verification:** [ ]
**Present levels:** [strengths + quantified baseline + educational impact]
**Grade-level standard:** [verified code, grade, official link, date] OR
  [functional access rationale / UNVERIFIED — official check required]
**Proposed annual goal:**
By [date], given [task, materials, access supports, permitted prompts],
student will [one observable skill] with [evidence-backed performance criterion],
as measured by [consistent metric, method, sampling and scoring rule].
**Baseline → proposed target:** [same units and comparable task conditions]
**Progress monitoring:** [probe, denominator, frequency, collector role, reporting timing]
**Access supports and scoring boundaries:** [ ]
**Short-term objectives:** [only when required for IEP-team-determined alternate-assessment pathway or specifically requested]
**Human review / QA flags:** [ ]
```

**Do not use 80%, 4/5 or three probes by default.** Select targets from available evidence and educator judgment. Distinguish access supports from prompting that changes what is being measured. Progress-reporting frequency is IEP/team/local-specific, not a universal number.

## Step 5 — Quality review checklist

- [ ] Baseline is dated, measured and reproducible with known support/conditions.
- [ ] Goal behavior is observable and scored consistently.
- [ ] Baseline and goal use comparable units and construct.
- [ ] Grade-level standard is verified when a standard is claimed.
- [ ] No nonofficial priority designation is presented as state-adopted.
- [ ] Criterion is justified; no automatic percentage inserted.
- [ ] Measurement/progress reporting are defined.
- [ ] Alternate-assessment objectives are included only where appropriate (and included when required).
- [ ] No student PII or invented local policy is included.
- [ ] Output is marked as a draft awaiting authorized human review.

When failing a gate, state exactly what information is missing, then propose a reasonable collection approach without fabricating observed values.

## Fictional setup test

> Fictional grade 3 learner, target multiplication facts, **no baseline provided**. Prepare an incomplete goal framework; specify which data to collect first, without inventing scores or claiming a finalized IEP goal.


---
### Mandatory privacy response contract (v2.2)
For any student-specific material, replace discovered PII in **all assistant outputs** with typed labels, e.g., `[[REDACTED: STUDENT_NAME #001]]`, `[[REDACTED: DATE_OF_BIRTH #001]]`, `[[REDACTED: STUDENT_ID #001]]`. When any marker is used, begin with: **⚠️ PII REDACTED — HUMAN REVIEW REQUIRED. Replace marked information ONLY in the authorized IEP system of record.** At the end list types/tokens only; never show original values or ask users to paste replacements into AI chat. If no PII is detected, say screening is incomplete and indirect identifiers still need manual review. Do **not** assume uploading student-identifiable files to a consumer AI tool is permitted; use approved local pre-upload scanning and qualified human review. Source guide: `docs/PRIVACY_AND_REDACTION.md`.
