# Full IEP Goal Generator — Student context and baseline

**Edition: FULL — one of five knowledge files.** These sections reproduce the detailed original source templates and reference materials. Do not fill this public source document with student records.

---

## Student profile intake
*Original module: `templates/iep/student-profile-intake.md`*

# TEMPLATE — De-identified Student / IEP Intake

**Handling:** Only use a district-approved AI/data workflow. Prefer fictional alias IDs. Do not include name, exact DOB, address, contact information, student ID or sensitive full-record uploads unless explicitly permitted and necessary.

## A. Essential identifiers (for task, not personal identity)

- **Student alias:** [STUDENT-A]
- **Enrolled grade / instructional program:** [REQUIRED]
- **School year / IEP period (year, not full DOB):** [REQUIRED]
- **Goal subject/domain(s):** [REQUIRED: reading / math / writing / communication / executive function / self-regulation / daily living / motor / other]
- **Request purpose:** [new annual goal / revise / goal audit / progress update]
- **Assessment pathway:** [general state assessment / IEP team-determined alternate assessment / preschool-TK / not specified]
- **Applicable language(s) and accessible response modality (if relevant):** [ ]

## B. Current learning and access context

- **Student strengths, interests, successful strategies:** [RECOMMENDED]
- **Need affecting participation/progress in age/grade curriculum:** [REQUIRED]
- **Specific observed skill difficulty:** [REQUIRED]
- **General education task(s) affected:** [REQUIRED for K–12 academic goals]
- **Assistive technology / AAC / accommodations used during baseline:** [REQUIRED when applicable]
- **Prompting/support level (types, frequency):** [REQUIRED when applicable]
- **Known instructional history / prior progress data:** [RECOMMENDED]
- **Family/student priorities or concerns, if voluntarily shared:** [RECOMMENDED]
- **English learner considerations / language of instruction (if relevant):** [CONDITIONAL]

## C. Supplied evidence inventory

| Evidence | Date or period | Source | Summary | Is it repeatable/scorable? |
|---|---|---|---|---|
| [probe] | [date] | [teacher] | [4/10] | [yes/no] |
| [work samples] | [date range] | [ ] | [ ] | [ ] |
| [evaluation] | [date] | [qualified assessor] | [ ] | [ ] |
| [prior goal progress] | [range] | [ ] | [ ] | [ ] |

## D. Goal development preferences

- **Annual goal target date:** [REQUIRED; may be based on proposed IEP annual cycle]
- **Instructional setting(s) where skill matters:** [ ]
- **Who will collect progress data:** [ ]
- **Feasible monitoring schedule / reporting timetable:** [ ]
- **Current services/related-service professionals to consult:** [optional, no unilateral change]
- **Current confirmed standard or standards crosswalk:** [code + URL/file, or `unknown`]
- **Local district/SELPA format to follow:** [ ]

## E. Safety and team review

- **Have records been appropriately de-identified / approved?** [yes/no]
- **Who will review the draft?** [role, not name]
- **Missing evidence requiring collection before team review:** [ ]

> Do not fill unknown fields with plausible details. Upload the present-levels/baseline section of this bundled file for each proposed goal area.

---

## Present levels and measurable baseline
*Original module: `templates/iep/present-levels-baseline.md`*

# TEMPLATE — Present Levels & Goal-Specific Baseline

**Complete one per distinct proposed goal construct.** Use de-identified records and observation dates.

## Instructional need and strengths

- **Student alias / enrolled grade:** [ ]
- **Goal domain and exact skill/construct:** [REQUIRED]
- **Strengths / what the student can do:** [REQUIRED]
- **Disability-related educational need:** [REQUIRED; describe functionally rather than inferring from label]
- **Impact on involvement/progress in grade-level curriculum or appropriate preschool activities:** [REQUIRED]
- **Grade-level task requiring this skill:** [REQUIRED for academic goals]
- **Relevant student or family input, if available:** [ ]

## Operational baseline — REPEATABLE

- **Date(s) and recency:** [REQUIRED]
- **Source / collector / measure name:** [REQUIRED]
- **Task and material complexity:** [REQUIRED: e.g. passage type, length, readability, math items]
- **Environment:** [REQUIRED when performance depends on setting]
- **Directions / opportunity definition:** [REQUIRED]
- **Access accommodations/assistive tech:** [REQUIRED if used; otherwise `none reported`]
- **Allowed prompts/supports:** [REQUIRED; e.g. verbal cue once, model, independent]
- **Observable student response that counts:** [REQUIRED]
- **Measure units:** [REQUIRED: 4 of 10; words correct per minute; duration; rubric score]
- **Total sample/opportunities and number of observations:** [REQUIRED]
- **Accuracy/scoring formula:** [REQUIRED: numerator / denominator or other explicit rubric]
- **Stability/variability across observations:** [RECOMMENDED]
- **Known access confounders (vision/hearing/language/response method/etc.):** [as applicable]

### Raw or summarized observation table

| Probe date | Task/material | Supports | Correct/total or measured units | Notes about comparability |
|---|---|---|---|---|
| [date] | [ ] | [ ] | [ ] | [ ] |
| [date] | [ ] | [ ] | [ ] | [ ] |
| [date] | [ ] | [ ] | [ ] | [ ] |

### Baseline statement — directly reproducible

> As of [date range], when given [defined task/materials] with [specific access supports and prompting], the student [observable behavior] at [n/N or defined units] across [number/period of observations] measured by [instrument/recording method]. This affects access to [specified curricular/participation activity].

## Target feasibility evidence

- **Previous related goal and progress:** [ ]
- **Recent learning/growth rate (if actually observed):** [ ]
- **Expected instructional supports (not necessarily service commitments):** [ ]
- **Potential target measure, same units/conditions as baseline:** [ ]
- **Constraints/uncertainties:** [ ]
- **Needed additional data:** [ ]

## Baseline readiness

- [ ] Evidence is dated and attributed
- [ ] Someone else could reproduce the probe and scoring
- [ ] Prompt level and accommodations are clear
- [ ] Denominator/metric is valid and matches the proposed goal skill
- [ ] Impact on educational access is explicit
- [ ] No measure or result has been estimated as though observed

**Readiness label:** [READY FOR DRAFT / NEED MORE BASELINE / INVALID MEASURE]


---
### Mandatory privacy response contract (v2.2)
For any student-specific material, replace discovered PII in **all assistant outputs** with typed labels, e.g., `[[REDACTED: STUDENT_NAME #001]]`, `[[REDACTED: DATE_OF_BIRTH #001]]`, `[[REDACTED: STUDENT_ID #001]]`. When any marker is used, begin with: **⚠️ PII REDACTED — HUMAN REVIEW REQUIRED. Replace marked information ONLY in the authorized IEP system of record.** At the end list types/tokens only; never show original values or ask users to paste replacements into AI chat. If no PII is detected, say screening is incomplete and indirect identifiers still need manual review. Do **not** assume uploading student-identifiable files to a consumer AI tool is permitted; use approved local pre-upload scanning and qualified human review. Source guide: `docs/PRIVACY_AND_REDACTION.md`.
