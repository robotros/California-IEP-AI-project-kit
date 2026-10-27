# Kit manifest | 2026-10-26 | v1.0.0 | generated from Factory v1.4.1 requirements
## Role and edition plan
| Role | Edition | Instructions | Canonical role knowledge | Skill decision |
|---|---|---|---|---|
| iep-educator | Light | `specialists/light/iep-educator/PROJECT_INSTRUCTIONS.txt` | `01_CONTEXT.md`, `02_OPERATIONS_AND_PROMPTS.md`, `03_QA_AND_HANDOFFS.md` (3) | `PORTABLE_FALLBACK`; native only where eligible |
| iep-educator | Full | `specialists/full/iep-educator/PROJECT_INSTRUCTIONS.txt` | `01_CHARTER_AND_SCOPE.md`, `02_REQUIREMENTS.md`, `03_WORKFLOWS.md`, `04_ROLES_AND_INTERFACES.md`, `05_PROMPT_LIBRARY.md`, `06_TOOLS_AND_DATA.md`, `07_QA_AND_TESTS.md`, `08_DEPLOYMENT_AND_CHANGELOG.md` (8) | `PORTABLE_FALLBACK`; native only where eligible |

One role is appropriate because the user requested an educator assistant covering coordinated phases; distinct professional modes do not justify additional AI identities. Standards verification, goal production and a final quality check are **ordered passes**, not independent human approvals. Any cross-app or cross-person handoff is manual unless separately authorized integration exists.

## Skill suitability
`audit-iep-evidence-and-goal-light` and `audit-iep-evidence-and-goal-full`: focused repeatable tasks with trigger **audit/check a de-identified IEP goal or its evidence-to-need linkage**. Non-trigger: unrelated education questions, generic math, legal representation, executing record changes. Each edition gets independent source `SKILL.md`, selected byte-identical safe workflow reference, Claude folder-wrapped ZIP and root-SKILL ZIP. Native capability, account state and activation all `NEEDS_VERIFICATION`. Global Skill contains only educator procedures, never student records or hidden private knowledge.

## Authority and classifications
Public source URLs are external read-only references, not ingested live databases. Rules and source links checked during research 2026-10-26; current texts must be rechecked per legal claim. All sample materials are synthetic placeholders. `INSTITUTIONAL_APPROVAL_REQUIRED` for identifiable student records; default use is no such data. No built-in write connectors; no authorization to send, publish or update stored policies. Human team controls real educational decisions.

## Distribution
`distributions/` ZIPs are optional Skills *not* extra Project files. `adapters/microsoft-365-agent-builder/{light,full}/iep-educator/` holds exact-text `.txt` copies of the 3/8 canonical `.md` for that destination only. `docs/index.html` is a standalone offline intake helper, not an IEP system of record. `PACKAGE_SHA256SUMS.txt` records sha256 digests for reproducibility. Outer shareable ZIP is independent from upload-only Skill ZIPs.

## Status
Artifact generation: **GENERATED_ONLY** pending static checks in `VALIDATION_REPORT.md`. Account setup, tenant clearance, legal compliance, live Skill activation and real-world effectiveness: **NEEDS_VERIFICATION**. No GitHub publication has been performed.

`docs/EDUCATOR_RESOURCE_MAP.md` is a noncanonical optional user guide, NOT an additional 3/8 Project knowledge upload.