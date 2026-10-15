# Full Essential Standards AI — Test example and prompts

**Edition: FULL — one of five knowledge files.** These sections reproduce the detailed original source templates and reference materials. Do not fill this public source document with student records.

---

## Fictional worked example
*Original module: `examples/fictional-worked-example.md`*

# FICTIONAL END-TO-END EXAMPLE — NOT A REAL STUDENT

**Purpose:** Show how templates connect. **All student-level facts below are invented training data**, not evidence about any student; goal criteria are illustrative, not default legal requirements.

## 1. De-identified intake

- **Alias:** STUDENT-EXAMPLE
- **Enrolled grade:** 3
- **Area:** Answering questions about grade-level informational text
- **Strengths:** Can identify details when presented orally and allowed to refer to highlighted text (fictional input)
- **Educational need:** Has difficulty locating and using explicit text evidence for literal comprehension questions (fictional input)
- **Grade-level participation impact:** During grade 3 science and social-studies reading activities, needs support finding evidence to answer questions (fictional input)
- **Access conditions:** Short grade-level informational text shown with standard instructional supports; student may reread and point to text; no answer-giving prompts (fictional input)
- **IEP annual target date:** [To be supplied; not invented]

## 2. Hypothetical baseline data (fictional)

| Hypothetical probe | Equivalent reading passage | Correct evidence-backed answers | Total opportunities |
|---|---|---:|---:|
| A | grade-level brief informational text | 3 | 10 |
| B | same task format, alternate text | 4 | 10 |
| C | same task format, alternate text | 5 | 10 |

**Baseline summary:** 12/30 = 40% of questions answered correctly with a supporting detail across three *hypothetical* comparable probes. Actual implementation would require current, real, student-specific probes and a scorer definition of what counts as adequate text evidence.

## 3. Standards handoff

**Official standard selected for manual verification:** CA CCSS ELA/Literacy **RI.3.1**, on asking/answering questions demonstrating understanding of a text with explicit text reference. **Do not mark verified solely from this example**: the Standards AI must re-check the exact California CDE catalog page and any CA-specific annotation/version before use.

**Instructional interpretation:** Answering literal questions and pointing to/identifying a relevant passage detail is an individualized enabling skill to support grade-level comprehension expectations; it is not a new official standard code.

## 4. Illustrative proposed goal

> By [actual IEP annual target date], when presented with a comparable grade 3 informational passage and ten literal comprehension questions, and allowed to reread or reference the passage without answer-giving prompts, STUDENT-EXAMPLE will answer each question and identify a relevant supporting text detail for at least **8 of 10 questions on three comparable probes**, as measured by a teacher-created scored comprehension-and-evidence record.

**Why the criterion is hypothetical:** 8/10 across 3 probes is an example selection, **not** a California mandate or an evidence-established target for a real learner. A real IEP team would select a data-supported ambitious, attainable target after reviewing instruction, trend, variability and individual circumstances.

## 5. Monitoring and human QA

- **Scoring:** Count a question correct only when both the answer and cited text detail are accurate; operationalize acceptable text evidence and response modality.
- **Sample:** Ten comparable questions from a documented rubric; avoid artificially easier passages.
- **Frequency:** [team/provider-selected based on instruction and feasibility]
- **Reports to family:** [IEP-specified schedule]
- **Team verification:** Confirm readability/accessibility, standard ID in CDE catalog, actual baseline, goal target date and attainable criterion.

**Status:** `ILLUSTRATION ONLY — DO NOT COPY INTO A REAL IEP WITHOUT ACTUAL EVIDENCE AND REVIEW`.

---

## Reusable prompts
*Original module: `prompts/ready-to-use-prompts.md`*

# Ready-to-Use Prompts — California IEP / Essential Standards Projects

These prompts assume you supplied the relevant blank/completed Markdown templates. Do not enter identifiable student information unless the AI platform and workflow have formal LEA approval.

## Prompt 1 — Build essential standards for a grade

> Act under the California Essential Standards AI project instructions. For grade [GRADE], subject [SUBJECT], and instructional period [PERIOD], verify current California adopted standards from authoritative CDE sources. Recommend a limited set of locally *proposed*, not state-designated, essential/priority standards using the project rubric. Provide exact codes, grade, concise accurate expectation, source URL, checked date, prioritized rationale, unpacked knowledge/skills, and any uncertain items. Complete the `01_STANDARDS_REVIEW.md` structure. If the official catalog cannot be checked, flag all unverified codes and request the source document rather than inventing them.

## Prompt 2 — Produce the standards-to-goal handoff

> For the verified enrolled-grade standard [CODE, GRADE, SOURCE], prepare `02_STANDARDS_TO_GOAL_CROSSWALK.md`. Distinguish the official standard from your inferred prerequisite/enabling skills. Suggest accessible learning tasks and measurable evidence types, but do not invent an individual student's baseline or IEP target. If this is an IEP-team-determined alternate assessment pathway, include the applicable verified CCC/EU or science connector and show the grade-level connection.

## Prompt 3 — Draft a measurable annual goal

> Act under IEP Goal Generator instructions. Use attached de-identified intake (`03`), repeatable baseline (`04`), request (`05`), and verified standards crosswalk (`08`). Draft **one** individualized annual goal in the `06_IEP_GOAL_OUTPUT_TEMPLATE.md` format. Clearly separate observed information, proposed target choices, verification needed, and the plan to report progress. If anything essential is missing, flag `PROVISIONAL — MISSING DATA` and state the shortest possible collection plan. Do not assume 80% mastery or a fixed prompt level.

## Prompt 4 — Audit and repair an existing goal

> Review the following annual goal against documented present levels, a comparable baseline, educational impact, applicable verified grade-level standard (if academic), observable behavior, success criterion, accommodations, and progress monitoring. Quote the specific deficiencies; then supply a minimally changed proposed rewrite and a table listing each revision and justification. Preserve all real measurement results and disclosed supports. Label unverified standard claims.

## Prompt 5 — Generate a progress report from evidence

> Using the adopted IEP goal text and real progress probes below, calculate performance accurately, explain trend and variability, distinguish criterion met/not met from incomplete evidence, and draft an accessible parent progress update. Do not infer mastery from a single high data point unless the actual goal's criterion permits it. Identify changes in probe difficulty or supports that make observations non-comparable.

## Prompt 6 — Compare general and alternate curriculum pathways

> For [GRADE/SUBJECT], compare the verified grade-level California content standard with a verified alternate achievement connector/EU **only for an IEP-team-determined alternate assessment pathway**. Distinguish official standards from instructional examples. Do not use diagnosis as a basis for choosing the alternate pathway and do not invent connector codes.

## Prompt 7 — Quality control batch

> Evaluate all supplied proposed IEP annual goals with `10_QUALITY_REVIEW_AND_APPROVAL.md`. Give each goal `PASS FOR TEAM REVIEW`, `REVISE`, or `FAIL — NOT READY`, with evidence-based fixes and a list of missing measurements/sources. Do not mark them formally adopted; that remains with the authorized IEP team.


---
### Mandatory privacy response contract (v2.2)
For any student-specific material, replace discovered PII in **all assistant outputs** with typed labels, e.g., `[[REDACTED: STUDENT_NAME #001]]`, `[[REDACTED: DATE_OF_BIRTH #001]]`, `[[REDACTED: STUDENT_ID #001]]`. When any marker is used, begin with: **⚠️ PII REDACTED — HUMAN REVIEW REQUIRED. Replace marked information ONLY in the authorized IEP system of record.** At the end list types/tokens only; never show original values or ask users to paste replacements into AI chat. If no PII is detected, say screening is incomplete and indirect identifiers still need manual review. Do **not** assume uploading student-identifiable files to a consumer AI tool is permitted; use approved local pre-upload scanning and qualified human review. Source guide: `docs/PRIVACY_AND_REDACTION.md`.
