# Set Up the California Special Education AI Projects with Your AI Assistant

**One-link setup guide for ChatGPT, Claude, Gemini, Copilot, and other assistants that can read public GitHub files.**

> **For educators:** This is a guided configuration kit, **not an application to deploy**. You do not need to know Git or write code. You need access to an AI platform that supports custom/project instructions or equivalent conversations. Different platforms support different levels of automation. An assistant should not claim to have created a project unless it actually did so and verified the result.

## Start here — give this link to your AI assistant

**Share this GitHub page after it is published on the repository's `main` branch:**

https://github.com/robotros/California-IEP-AI-project-kit/blob/main/AI_SETUP.md

Copy and paste the following message into your AI assistant along with the link:

> Help me set up both California Special Education AI projects from this public GitHub setup guide: https://github.com/robotros/California-IEP-AI-project-kit/blob/main/AI_SETUP.md. Read the guide and the project instruction files before proceeding. First determine what setup you can actually perform in my AI platform. Create/configure both projects if supported and authorized; otherwise walk me through setup **one step at a time**, including exactly which files to copy or attach. Use only fictional examples for testing. Do not ask for any student-identifiable information. At the end, verify each project's instructions and knowledge files and provide a completion checklist.

**If your AI cannot open GitHub links:** Open this page yourself and copy the **AI setup procedure** below into the chat. Download the repository as a ZIP (GitHub **Code → Download ZIP**) and upload only the relevant public Markdown files if supported. Some assistants cannot browse external URLs, manage project settings, or save configurations; in those cases follow their guided manual setup instructions.

## AI setup procedure (instructions to the assisting AI)

When an educator supplies the link above or asks to "install/setup the two projects," act as a **configuration guide**, not an IEP case manager. Read this document and the actual linked project instruction files. Do not infer their contents from filenames or a summary. Do not ask for identifiable student data. Complete the process in this order:

### Phase 1 — Verify access and platform capability

1. Read the repository's [README.md](README.md) and the [project manifest](setup/project-manifest.json). Confirm that the linked instruction and reference files exist. Use raw-file URLs below if the platform does not render GitHub pages correctly.
2. Identify the user's AI platform **only if it is not already clear**. Ask one simple question: **"Which AI tool are you using (for example, ChatGPT, Claude, Gemini, or Microsoft Copilot)?"**
3. Determine actual capabilities: Can you read external links? Can you create projects or custom assistants, edit their instructions, and attach knowledge files? Can these settings persist? Do you have permission to perform these actions?
4. State your capability accurately in one sentence. Use one of: `I can configure the projects directly`, `I can configure some elements; you will complete others`, or `I can guide manual setup only`. Do not claim persistent setup was successful without verification.
5. Do **not** require a GitHub account, programming, installation of Python, or access to any repository secrets. The public source files are enough.

### Phase 2 — Create two separate projects or equivalents

Use these exact project names. If the user's platform lacks named projects, offer two **independent, persistent configured assistants or workspaces**, if the platform supports them; otherwise use two separate conversations with copied instructions, and clearly explain that instructions may not persist.

| Project | Copy into its **instructions** area | Add public knowledge/reference files |
|---|---|---|
| **California Essential Standards AI** | [`projects/essential-standards/PROJECT_INSTRUCTIONS.md`](projects/essential-standards/PROJECT_INSTRUCTIONS.md) | [`references/authoritative-sources-and-rules.md`](references/authoritative-sources-and-rules.md), [`templates/standards/essential-standards-review.md`](templates/standards/essential-standards-review.md), [`templates/standards/standards-to-goal-crosswalk.md`](templates/standards/standards-to-goal-crosswalk.md) |
| **California IEP Goal Generator 2.0** | [`projects/iep-goal-generator/PROJECT_INSTRUCTIONS.md`](projects/iep-goal-generator/PROJECT_INSTRUCTIONS.md) | [`references/authoritative-sources-and-rules.md`](references/authoritative-sources-and-rules.md), all four files under [`templates/iep/`](templates/iep/), [`templates/standards/standards-to-goal-crosswalk.md`](templates/standards/standards-to-goal-crosswalk.md), [`templates/shared/quality-review-and-approval.md`](templates/shared/quality-review-and-approval.md) |

**Important distinction:** The full contents of each `PROJECT_INSTRUCTIONS.md` file belong in the project's **instruction/system behavior** configuration, *not merely as an uploaded knowledge file* if separate instruction and knowledge features are available. Knowledge files are supporting material; merely uploading files may not make an assistant follow instructions persistently.

If upload limits apply, prioritize the two instruction documents in their respective instruction fields, then the source guide, then the output/intake templates. [`templates/shared/local-configuration.md`](templates/shared/local-configuration.md) is a **blank template** for locally approved procedures, not permission to invent those procedures. Only approved local policy documents may be supplied, privately. [`prompts/ready-to-use-prompts.md`](prompts/ready-to-use-prompts.md) and [`examples/fictional-worked-example.md`](examples/fictional-worked-example.md) are optional supporting examples for either project.

### Phase 3 — Enforce privacy and sourcing

Before asking for IEP inputs, explain:

- **Use fictional or properly de-identified examples for setup/testing.** Real student records are not needed to create the projects. Do not solicit names, birthdates, student numbers, or complete IEP files.
- **Do not upload student-identifiable material** to an unapproved AI vendor, public repository, or shared conversation. An organization's own policies and agreements govern approved use; this guide does not certify FERPA compliance.
- Treat all outputs as **drafts requiring educator/IEP-team review**. Neither project can declare legal compliance, eligibility, assessment pathway, services, or placement.
- Verify grade-level standards, exact codes, source wording, source URLs, and currency using official California materials before declaring them verified. If source access is unavailable, mark claims `UNVERIFIED`.
- Distinguish **California state-adopted standards**, **local essential/priority standards**, **Core Content Connectors**, and **Essential Understandings**. They are not interchangeable.
- Do not manufacture student baseline data, performance measurements, standard codes, or progress histories. State missing fields explicitly.

### Phase 4 — Configure the workflow between projects

The **Essential Standards AI** runs first for standards identification, local-priority consideration, unpacking, and source verification. Its output is placed into [`templates/standards/standards-to-goal-crosswalk.md`](templates/standards/standards-to-goal-crosswalk.md). A person transfers the verified crosswalk to the **IEP Goal Generator 2.0**, which uses actual approved, de-identified present levels/baselines to draft goals. **Do not assume the two AI projects share files, chats, memory, or integrations.** Only automate a handoff if the platform supports it and the user's organization has authorized the data flow.

### Phase 5 — Validate each configuration with synthetic data

Do not begin a live student case. Run **one small test per project** (or give the educator copy-ready test prompts if you cannot run them):

**Essential Standards AI — safe test prompt:**

> Using only official California sources you can actually access, find one California grade 3 mathematics standard relevant to multiplication and label its code, grade, official source link and verification status. Explain the difference between the official standard and a proposed locally prioritized essential standard. If you cannot verify a code, do not invent one.

**IEP Goal Generator 2.0 — safe test prompt:**

> Use a **fictional** grade 3 student who is working on multiplication facts. No observed baseline data is supplied. Show which baseline details are missing, do not invent scores or accuracy, and either ask for essential missing information or draft an explicitly **INCOMPLETE** goal template. Do not assert that the goal is ready for IEP adoption.

Confirm that the standards assistant distinguishes official vs. proposed priority designations and that the IEP assistant does not fabricate a baseline or label an incomplete goal ready for team review. If the test fails, review the instruction placement and revise the project configuration; do not silently claim success.

### Phase 6 — Present completion status

Provide the educator a **two-project setup checklist** with status for each item: `Verified configured`, `User action needed`, `Not supported by this platform`, or `Not yet verified`.

Checklist items: correct project names; correct project instruction text; source guide attached/reachable; appropriate templates attached/reachable; privacy notice understood; synthetic test results; crosswalk handoff explained. Never mark anything `Verified configured` solely because it was recommended in this document.

If user action is needed, provide **only the next concrete step** (for example, "Open your AI platform's project creation screen and tell me when it's open"). Do not invent button names or account-specific UI. Advance after the user confirms the step. Avoid long questionnaires or requesting permissions that are not needed.

## Direct raw URLs for AI assistants that prefer plain text

- Manifest: https://raw.githubusercontent.com/robotros/California-IEP-AI-project-kit/main/setup/project-manifest.json
- Standards project instructions: https://raw.githubusercontent.com/robotros/California-IEP-AI-project-kit/main/projects/essential-standards/PROJECT_INSTRUCTIONS.md
- IEP goal project instructions: https://raw.githubusercontent.com/robotros/California-IEP-AI-project-kit/main/projects/iep-goal-generator/PROJECT_INSTRUCTIONS.md
- Source guide: https://raw.githubusercontent.com/robotros/California-IEP-AI-project-kit/main/references/authoritative-sources-and-rules.md
- Manual workflow: https://raw.githubusercontent.com/robotros/California-IEP-AI-project-kit/main/docs/WORKFLOW.md

If a requested URL does not exist or cannot be fetched, **say so**; do not imply that you installed any project. Refer back to the GitHub repository file browser and ask the educator to provide the missing file.

## Human-only quick setup (no AI control of account settings needed)

1. Open your AI platform and create **two separate projects** or custom assistants with the names above. If no project feature exists, start two independent chats.
2. Open each `PROJECT_INSTRUCTIONS.md` file from this repository. Copy its full text into the matching project's custom instructions field; save if your platform requires it.
3. Add the relevant public reference and template files listed in the table above, if the platform supports files/knowledge sources.
4. Open your **Essential Standards AI** project and run the synthetic standards test above.
5. Open your **California IEP Goal Generator 2.0** project and run the synthetic missing-baseline test above.
6. For actual use, complete local policy checks, obtain appropriate approval, and follow your organization's private workflow. See [implementation workflow](docs/WORKFLOW.md).

**Support boundaries:** This repo distributes prompts, templates, and procedural guidance, not a live app, an IEP database, or a legally validated IEP production environment. Changes to AI service capabilities, California standards, or law may require updates to these instructions.
