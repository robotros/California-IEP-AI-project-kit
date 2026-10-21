# Kit manifest — California IEP v2.4.0 / Factory v1.4.1

**Status:** GENERATED_ONLY upgrade overlay; existing https://github.com/robotros/California-IEP-AI-project-kit repository remains at its observed v2.3.1 until owner authorizes publication. Original assets are preserved on merge. Each specialist gets independent instructions + exactly 3 or 8 canonical knowledge files. The Factory **host** installation edition is not the same as Specialist Light/Full.

| Role | Edition | Instructions field | Canonical knowledge (3/8) | Native Skill decision |
|---|---|---|---|---|
| essential-standards | Light | `specialists/light/essential-standards/PROJECT_INSTRUCTIONS.txt` (5248 chars) | 3 files under `specialists/light/essential-standards/` | focused procedure only if eligible; otherwise portable fallback |
| essential-standards | Full | `specialists/full/essential-standards/PROJECT_INSTRUCTIONS.txt` (5429 chars) | 8 files under `specialists/full/essential-standards/` | focused procedure only if eligible; otherwise portable fallback |
| iep-goal-generator | Light | `specialists/light/iep-goal-generator/PROJECT_INSTRUCTIONS.txt` (5165 chars) | 3 files under `specialists/light/iep-goal-generator/` | focused procedure only if eligible; otherwise portable fallback |
| iep-goal-generator | Full | `specialists/full/iep-goal-generator/PROJECT_INSTRUCTIONS.txt` (5346 chars) | 8 files under `specialists/full/iep-goal-generator/` | focused procedure only if eligible; otherwise portable fallback |

## Exact paths and transport rules
The machine-readable [setup/project-manifest.json](setup/project-manifest.json) lists each of the 22 canonical Markdown knowledge files (two roles × [3+8]), all four instructions, all Skill source/ZIP paths and Microsoft transport files. File names are case-sensitive. Instructions are **not** knowledge uploads. Separate Skills do not add to the 3/8 count. Agent Builder faithful `.txt` copies replace, not supplement, role `.md` in its embedded knowledge list. No full instructions `.md` upload in v2.4.0.

## Scope and authority
Two distinct roles are justified by independent curriculum verification vs individualized goal drafting/human IEP review. A crosswalk moves by authorized human handoff unless actual configured integration is approved. Synthetic setup only; no student PII in repository or account-wide Skill. School permission, real installation, Skills activation and operational evaluation require independent evidence.

## Skill triggers
- Standards: `verify-california-standards-light/full` for official standard verification and curriculum crosswalk, NOT student-specific annual goal adoption.
- Goals: `audit-iep-goal-measurement-light/full` for baseline/goal measurement audits, NOT standalone CDE curriculum discovery.

References included with each Skill are byte-identical subsets of safe project procedure content. No private project knowledge, credentials, executables, secret API keys or automatic tool access.
