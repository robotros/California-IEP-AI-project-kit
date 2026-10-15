# Choose an edition — ChatGPT Free–compatible AI project bundles

**Start at [`AI_SETUP.md`](../AI_SETUP.md)** to have an AI assistant walk an educator through installation. Two separate projects are created only when the assistant can actually create them. On ChatGPT, paste the instruction summary into **Instructions** (8000-character limit) and also upload the full `PROJECT_INSTRUCTIONS.md` as a knowledge file. If the assistant cannot create projects, including Grok, it starts the manual walkthrough in the current chat and does not stop after the refusal.

| Item | Lightweight | Full |
|---|---:|---:|
| IEP Goal Generator knowledge uploads | **2** | **5** |
| Essential Standards AI knowledge uploads | **2** | **5** |
| Free slots left after edition files only | 3 | 0 |
| ChatGPT uploads, edition files plus full instructions | 3 | 6, over the 5-file cap |
| Purpose | Quick routine drafting / validation | Full original templates, examples and configuration |
| ChatGPT Instructions field | Summary, under 8000 characters | Summary, under 8000 characters |
| Full instructions file on ChatGPT | Upload as a knowledge file | Upload as a knowledge file |

### Important Free-tier upload limits

OpenAI documents **5 files per Free project** and a separate **3 file uploads per day** limit for Free accounts. On ChatGPT, also upload each project's full instructions file. One Lightweight project is then 3 uploads, which meets the daily limit and leaves 2 project slots. Both Lightweight projects are 6 uploads and may take more than one day. Full plus the instructions file is 6 files in one project and does not fit the 5-file cap. Plan and platform constraints may change; verify official help pages.

References: [OpenAI Projects](https://help.openai.com/en/articles/10169521-using-projects-in-chatgpt), [OpenAI file upload limits](https://help.openai.com/en/articles/8555545-uploading-files-and-audio-to-chatgpt).

### What differs between editions?

**Lightweight:** 2 concise, curated knowledge files per project. They preserve the key safeguards, source hierarchy, intake/output schema, measurable baseline gate, standards verification, priority-label distinctions and standards-to-goal handoff, plus small test prompts. Detailed optional template variations are not all present.

**Full:** 5 bundled files per project. Together, the five documents reproduce the original detailed source modules in the repository: student intake, baseline, request, output, standards review, crosswalk, local configuration, QA, source rules, fictional example and ready-to-use prompts. Bundling changes file count, not the human verification requirements. Full consumes every ChatGPT Free file slot, so additional student/context files cannot be added as permanent project uploads until a slot is freed or the plan changes.

**Both:** full instruction texts remain at `projects/iep-goal-generator/PROJECT_INSTRUCTIONS.md` and `projects/essential-standards/PROJECT_INSTRUCTIONS.md`. ChatGPT summaries are `projects/iep-goal-generator/INSTRUCTIONS_SUMMARY.md` (6386 characters) and `projects/essential-standards/INSTRUCTIONS_SUMMARY.md` (7849 characters). Paste the summary into Instructions and upload the full file as knowledge. Attaching the full file does not by itself fill the Instructions field. On ChatGPT Free, Lightweight plus that extra file is 3 uploads; Full plus that file is 6 and does not fit the 5-file cap.

### Quick paths

#### Lightweight — 2 knowledge files per project

- [Goal Generator: Form & workflow](lightweight/iep-goal-generator/01_GOAL_WORKFLOW_AND_TEMPLATES.md)
- [Goal Generator: Sources & safety](lightweight/iep-goal-generator/02_SOURCES_CROSSWALK_AND_SAFETY.md)
- [Essential Standards: Forms & workflow](lightweight/essential-standards/01_STANDARDS_WORKFLOW_AND_TEMPLATES.md)
- [Essential Standards: Sources & review](lightweight/essential-standards/02_SOURCES_RULES_AND_REVIEW.md)

#### Full — 5 knowledge files per project

- [Full Goal Generator bundle](full/iep-goal-generator/)
- [Full Essential Standards bundle](full/essential-standards/)

See the [machine-readable project manifest](../setup/project-manifest.json) for exact paths and counts. Do not upload the entire repository ZIP as one knowledge file and assume the assistant will read every member. Attach the **individual `.md` files** for the selected project/edition, or use platform-supported text knowledge entries as appropriate.


### v2.2 privacy note

Both Lightweight and Full include the **same mandatory typed output-redaction rules in their project instruction text and knowledge bundles**, without adding uploads. Scan files locally using [PII scanner](../scripts/pii_redact.py) and follow [privacy guidance](../docs/PRIVACY_AND_REDACTION.md). Generated `[[REDACTED: CATEGORY #NNN]]` markers are **not** substitutes for human review; replace real identifiers only within the authorized IEP system of record.
