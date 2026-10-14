# Implementation workflow

This document expands the [root README](../README.md) with a practical sequence for using both AI projects. Use **synthetic examples** when testing, and follow school/LEA authorization before processing any real education records.

## 1. Establish governance

Complete [`local-configuration.md`](../templates/shared/local-configuration.md), specifying who may use the tools, approved AI vendors, allowed data types, storage/retention expectations, authorized reviewers, local goal formatting and the district/SELPA standards policy. Unset fields remain **unknown**, not implied permission. Keep filled student and local operational documents out of the shared Git repository.

## 2. Configure two independent assistants

- **Essential Standards AI:** copy [`projects/essential-standards/PROJECT_INSTRUCTIONS.md`](../projects/essential-standards/PROJECT_INSTRUCTIONS.md) into the project instructions. Provide the authoritative [source guide](../references/authoritative-sources-and-rules.md) and approved standards documents.
- **IEP Goal Generator 2.0:** copy [`projects/iep-goal-generator/PROJECT_INSTRUCTIONS.md`](../projects/iep-goal-generator/PROJECT_INSTRUCTIONS.md) into the project instructions. Provide the source guide and approved local configuration.

The handoff is manual unless your institution has approved integration and data protection controls. Do not assume one AI project can access the other project's information.

## 3. Identify and verify standards

With the Essential Standards AI, enter the grade, subject, curricular context and any official local priority-standard list into [`essential-standards-review.md`](../templates/standards/essential-standards-review.md).

- Validate every proposed standard's code, exact language, grade, and published source before declaring it official.
- Distinguish **California-adopted content standards** from **locally identified priority/essential standards**.
- Treat **Core Content Connectors** and **Essential Understandings** as alternate-assessment resources, not synonyms for local priorities.
- When current source access is unavailable, label source-specific claims **UNVERIFIED** instead of guessing.

Fill in [`standards-to-goal-crosswalk.md`](../templates/standards/standards-to-goal-crosswalk.md) and send the checked crosswalk to the Goal Generator project.

## 4. Supply goal-writing inputs

For each proposed goal, complete these templates within an **approved private workflow**:

1. [`student-profile-intake.md`](../templates/iep/student-profile-intake.md): enrolled grade, student strengths, access and disability-related educational needs; no personal identifiers needed for initial drafting.
2. [`present-levels-baseline.md`](../templates/iep/present-levels-baseline.md): task and conditions, prompts/supports, performance data, denominator, dates and number of observations.
3. [`goal-request.md`](../templates/iep/goal-request.md): write/rewrite/audit task, target domain, and any verified standards crosswalk.

### Baseline readiness rule

A ready-for-team-review academic goal needs a reproducible baseline and observable annual target using the same or comparable construct. **Do not invent a baseline, mastery criterion, probe frequency or standard**. If information is missing, mark `INCOMPLETE / REQUIRES VERIFICATION` with a specific missing-data list.

## 5. Generate and review the goal

Use [`goal-output.md`](../templates/iep/goal-output.md) as the output structure. The draft should separate baseline from criterion, articulate measurement and reporting methods, document the standards connection when appropriate, and avoid claiming requirements that are only local preferences.

Review with [`quality-review-and-approval.md`](../templates/shared/quality-review-and-approval.md). Do not mark the output adopted until the authorized IEP team follows its process.

## 6. Test without student records

Use [`fictional-worked-example.md`](../examples/fictional-worked-example.md) and [`ready-to-use-prompts.md`](../prompts/ready-to-use-prompts.md) to validate the assistant's behavior before a district-authorized rollout.

## 7. Refresh source information

The source reference file records a research date of **October 14, 2026**. Check current California Department of Education guidance, California Education Code, federal IDEA regulations and official standards at the time the goals will be used. Update project instructions and references through normal review/commit procedures.
