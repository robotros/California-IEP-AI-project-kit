# Factory v1.4.1 upgrade — package validation report

**Scope:** California Special Education AI Project Kit v2.4.0 upgrade OVERLAY (source GitHub observed v2.3.1). Tested only generated overlay files, not an actual merged/published repository or installed assistant. Original source assets (`docs/index.html`, old `templates/`, etc.) are expected to remain in repository after owner-approved merge.

| Evidence gate | Result | Note |
|---|---|---|
| Source repository read | PASS | GitHub connector identified v2.3.1 default branch; key setup and privacy docs inspected |
| Factory artifact structure | PASS | Generated 4 role/edition instruction files, 22 canonical Markdown files, 22 faithful Agent Builder `.txt` copies, 4 standalone Skills, 8 Skill ZIPs |
| Static contents / ZIP checks | PASS (44 deterministic checks) | Local deterministic checks across each role/edition; static inspection **not** a security certification |
| Package ready for owner review | PASS — GENERATED_ONLY (owner review pending) | Generated overlay only, no Github commit/pull request |
| Merged repository links/old CI integration | NEEDS_VERIFICATION | Requires merging overlay with original; original `scripts/`/CI still use historical map |
| Live installation and Skill import | NEEDS_VERIFICATION | Account eligibility, permission and UI not checked |
| Fresh installed behavioral tests | NEEDS_VERIFICATION | B1–B8 must run with synthetic data per role/edition |
| Real student-data authorization | NEEDS_VERIFICATION | No case data should be uploaded until institution authorizes specific service/data scope |

## Static checks

| Test / scope | Verdict | Evidence |
|---|---|---|
| I1 instruction exists and <7500 / essential-standards:light | PASS | characters=5248 |
| I2 exact canonical .md count / essential-standards:light | PASS | count=3 |
| I3 instruction separate from uploads / essential-standards:light | PASS | AI_GENERATED_AND_LOCAL_DETERMINISTIC_CHECK |
| I4 mandated guardrail content / essential-standards:light | PASS | privacy, baseline, source, team, approval, crosswalk all present |
| M1 faithful Microsoft .txt copies / essential-standards:light | PASS | AI_GENERATED_AND_LOCAL_DETERMINISTIC_CHECK |
| S1 skill exists and frontmatter / essential-standards:light | PASS | AI_GENERATED_AND_LOCAL_DETERMINISTIC_CHECK |
| S2 skill name + description / essential-standards:light | PASS | AI_GENERATED_AND_LOCAL_DETERMINISTIC_CHECK |
| S3 safe canonical skill reference / essential-standards:light | PASS | AI_GENERATED_AND_LOCAL_DETERMINISTIC_CHECK |
| S4 claude zip shape/safety / essential-standards:light | PASS | AI_GENERATED_AND_LOCAL_DETERMINISTIC_CHECK |
| S4 root zip shape/safety / essential-standards:light | PASS | AI_GENERATED_AND_LOCAL_DETERMINISTIC_CHECK |
| I1 instruction exists and <7500 / essential-standards:full | PASS | characters=5429 |
| I2 exact canonical .md count / essential-standards:full | PASS | count=8 |
| I3 instruction separate from uploads / essential-standards:full | PASS | AI_GENERATED_AND_LOCAL_DETERMINISTIC_CHECK |
| I4 mandated guardrail content / essential-standards:full | PASS | privacy, baseline, source, team, approval, crosswalk all present |
| M1 faithful Microsoft .txt copies / essential-standards:full | PASS | AI_GENERATED_AND_LOCAL_DETERMINISTIC_CHECK |
| S1 skill exists and frontmatter / essential-standards:full | PASS | AI_GENERATED_AND_LOCAL_DETERMINISTIC_CHECK |
| S2 skill name + description / essential-standards:full | PASS | AI_GENERATED_AND_LOCAL_DETERMINISTIC_CHECK |
| S3 safe canonical skill reference / essential-standards:full | PASS | AI_GENERATED_AND_LOCAL_DETERMINISTIC_CHECK |
| S4 claude zip shape/safety / essential-standards:full | PASS | AI_GENERATED_AND_LOCAL_DETERMINISTIC_CHECK |
| S4 root zip shape/safety / essential-standards:full | PASS | AI_GENERATED_AND_LOCAL_DETERMINISTIC_CHECK |
| I1 instruction exists and <7500 / iep-goal-generator:light | PASS | characters=5165 |
| I2 exact canonical .md count / iep-goal-generator:light | PASS | count=3 |
| I3 instruction separate from uploads / iep-goal-generator:light | PASS | AI_GENERATED_AND_LOCAL_DETERMINISTIC_CHECK |
| I4 mandated guardrail content / iep-goal-generator:light | PASS | privacy, baseline, source, team, approval, crosswalk all present |
| M1 faithful Microsoft .txt copies / iep-goal-generator:light | PASS | AI_GENERATED_AND_LOCAL_DETERMINISTIC_CHECK |
| S1 skill exists and frontmatter / iep-goal-generator:light | PASS | AI_GENERATED_AND_LOCAL_DETERMINISTIC_CHECK |
| S2 skill name + description / iep-goal-generator:light | PASS | AI_GENERATED_AND_LOCAL_DETERMINISTIC_CHECK |
| S3 safe canonical skill reference / iep-goal-generator:light | PASS | AI_GENERATED_AND_LOCAL_DETERMINISTIC_CHECK |
| S4 claude zip shape/safety / iep-goal-generator:light | PASS | AI_GENERATED_AND_LOCAL_DETERMINISTIC_CHECK |
| S4 root zip shape/safety / iep-goal-generator:light | PASS | AI_GENERATED_AND_LOCAL_DETERMINISTIC_CHECK |
| I1 instruction exists and <7500 / iep-goal-generator:full | PASS | characters=5346 |
| I2 exact canonical .md count / iep-goal-generator:full | PASS | count=8 |
| I3 instruction separate from uploads / iep-goal-generator:full | PASS | AI_GENERATED_AND_LOCAL_DETERMINISTIC_CHECK |
| I4 mandated guardrail content / iep-goal-generator:full | PASS | privacy, baseline, source, team, approval, crosswalk all present |
| M1 faithful Microsoft .txt copies / iep-goal-generator:full | PASS | AI_GENERATED_AND_LOCAL_DETERMINISTIC_CHECK |
| S1 skill exists and frontmatter / iep-goal-generator:full | PASS | AI_GENERATED_AND_LOCAL_DETERMINISTIC_CHECK |
| S2 skill name + description / iep-goal-generator:full | PASS | AI_GENERATED_AND_LOCAL_DETERMINISTIC_CHECK |
| S3 safe canonical skill reference / iep-goal-generator:full | PASS | AI_GENERATED_AND_LOCAL_DETERMINISTIC_CHECK |
| S4 claude zip shape/safety / iep-goal-generator:full | PASS | AI_GENERATED_AND_LOCAL_DETERMINISTIC_CHECK |
| S4 root zip shape/safety / iep-goal-generator:full | PASS | AI_GENERATED_AND_LOCAL_DETERMINISTIC_CHECK |
| PKG1 core docs exist / ALL | PASS | README, manifest, setup, prompts, workflow map present |
| PKG2 both specialists / ALL | PASS | AI_GENERATED_AND_LOCAL_DETERMINISTIC_CHECK |
| PKG3 default all AI capability preflight / ALL | PASS | AI_GENERATED_AND_LOCAL_DETERMINISTIC_CHECK |
| PKG4 same safety constraints across editions / ALL | PASS | AI_GENERATED_AND_LOCAL_DETERMINISTIC_CHECK |


## Significant change findings
1. Legacy repo v2.3.1 used 2-file Lightweight / 5-file Full **plus uploaded full instructions** rather than a dedicated <=7,500-character file in Instructions only. New paths fix static packaging; old layouts remain as historical sources.
2. Setup previously centered on persistent projects and instruction summary uploads. New `AI_SETUP_PROMPT.md` starts with an explicit matrix of **Project/agent and Skill support across all platforms**, and instructs account-specific checks, supported import layouts and fallbacks.
3. Existing privacy and offline form were valuable features; the new instructions carry mandatory typed PII redaction, no simulated de-identification certification, baseline gates, official code/date source verification, and human decision authority to both editions.
4. Skill packages are narrow, triggered procedure sources and expose no real learner data or programs/scripts. Import requires separate user approval and actual UI feature eligibility.

## Required release actions (human-led)
- Review changes against original README/AI_SETUP/AGENTS/manifest. Authorize GitHub branch/commit/PR *explicitly* before any external mutation; preserve original browser form and associated support assets.
- Review and align original repo's CI/static validation scripts for v2.4.0. Static compatibility of **merged** tree is not established by overlay checks.
- Back up and individually replace both installed role configurations as an atomic Light or Full set, verifying saved instructions/3-or-8 file count via UI or authorized tool.
- Run real, **synthetic** B1–B8 tests in every installed destination, including Skill positive/negative activation where eligible. Human educators review actual outputs and privacy.
- Record `USER_CONFIRMED` or `TOOL_VERIFIED` install receipts and `OPERATIONALLY_TESTED` separately, with blockers and retests. Never treat a generated ZIP as installed or public.
