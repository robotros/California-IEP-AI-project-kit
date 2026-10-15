# AI Setup — Two California Special Education Projects (Free and Full Editions)

> **v2.3.1: Form-first onboarding with v2.2 privacy safeguards:** Both projects now include PII preflight guidance and mandatory typed redaction of AI outputs. Read [the privacy guide](docs/PRIVACY_AND_REDACTION.md) before configuring either assistant. No additional knowledge files are required.

**Share this page with an AI assistant:** https://github.com/robotros/California-IEP-AI-project-kit/blob/main/AI_SETUP.md

This repo distributes **guided AI project configuration**, not an application or automatic software installer. Educators can use ChatGPT, Claude, Gemini or another platform that supports project instructions and/or knowledge. Any direct automation depends on tool permissions; a guided manual walkthrough always remains possible if the assistant can read these files. **During setup use only fictional information.**

## Copy/paste this prompt into your AI chat

> Please read this guide and set up the two California Special Education AI projects: https://github.com/robotros/California-IEP-AI-project-kit/blob/main/AI_SETUP.md. Start by recommending the **Lightweight edition** for a Free account; explain the Full edition as an option. Read the instruction summaries, full Project Instructions, and knowledge-file paths from the manifest. If you cannot create persistent projects or attach files — including if you are Grok — do not stop. Immediately walk me through setup in this chat, one step at a time, and tell me which file to paste or attach next. Do not claim a project was created. On ChatGPT, paste each project's instruction summary (under 8000 characters) into Instructions and upload the full `PROJECT_INSTRUCTIONS.md` as a knowledge file. Don't request real student data. Check both configurations with fictional test prompts, and clearly state which steps were completed versus still need my action. Then introduce the educator intake form and prompt me to paste or attach its generated Markdown in the matching project when I am ready for a task.

## Required onboarding handoff — introduce the educator form

Educators do **not** have to type directly into the Markdown template files. Use the offline-capable browser form at [`docs/index.html`](docs/index.html), following [`docs/FORM_GUIDE.md`](docs/FORM_GUIDE.md). After the repository owner enables GitHub Pages from the `docs/` folder, the optional public form link will be `https://robotros.github.io/California-IEP-AI-project-kit/` (not live until configured). The form generates a **single combined Markdown attachment for the current AI chat** or an archive of the corresponding templates; it does **not** consume additional permanent Project Knowledge slots. It does not send answers to a server, but automatic PII detection cannot assure anonymity or district authorization. After the two projects are configured and fictional tests pass, **always explain and offer the form as the default method for submitting the first real task**. Do not ask for the generated intake during configuration testing. Do not pretend a Pages site has been published until it is verified.

## Step 1 — Choose a profile, not an AI plan assumption

| Edition | Uploaded knowledge files per project | Remaining ChatGPT Free project slots | Best for |
|---|---:|---:|---|
| **Lightweight (default)** | **2** | 3 | Fast educator setup, future project documents |
| **Full** | **5** | 0 | Detailed original templates and examples |

Both editions keep the **same full Project Instructions files**. ChatGPT's project Instructions field accepts at most **8000 characters**, and both full files are longer than that. On ChatGPT, paste the maintained summary into Instructions and upload the full `PROJECT_INSTRUCTIONS.md` as a knowledge file. See [edition comparison](editions/README.md).

**Verified ChatGPT limits (reviewed October 2026):** Instructions field, 8000 characters. Free up to 5 project files; Go/Plus up to 25; Pro/Edu/Business/Enterprise up to 40. Free also has a published rate limit of 3 uploaded files/day. A ChatGPT project upload set is the edition files **plus** the full instructions file: Lightweight is 3 files (2 slots left on Free); Full is 6 files and does not fit a Free project's 5-file cap. Use Lightweight on Free when the full instructions file must be uploaded. Sources: [OpenAI Projects Help](https://help.openai.com/en/articles/10169521-using-projects-in-chatgpt), [OpenAI uploads Help](https://help.openai.com/en/articles/8555545-uploading-files-and-audio-to-chatgpt).

## Step 2 — How the AI assistant must operate

1. Read **this file** and [`setup/project-manifest.json`](setup/project-manifest.json), then the referenced two project instruction files. Do not infer contents from file names.
2. If the user's platform is unknown, ask: "Which AI tool are you using?" Prefer **lightweight** unless they choose full. Ask only what is genuinely necessary.
3. State what you can and cannot change, in one sentence. If you cannot create named projects, edit an Instructions field, or attach knowledge files — including **Grok (xAI)** and any chat-only assistant — do **not** stop and do **not** end the reply on that refusal. Continue in the same reply with **Step 2b**. Do not claim a project was created.
4. If you can change project settings **and** the user authorized it, create two separately named projects, then follow **Step 2a**. Do not claim a setting changed until the platform shows that it changed.
5. Attach the selected edition's `knowledge_files` from the manifest. On ChatGPT, also upload that project's full `PROJECT_INSTRUCTIONS.md`. Do not exceed the account's file cap. Do not upload both editions.
6. Explain how one project hands off a verified standards crosswalk to the other. The assistants do not automatically share chats, data, or knowledge.
7. Run the fictional configuration tests below. Report what was *actually verified* and what still needs user action.
8. **Complete the form handoff.** After successful setup, show the appropriate form location, offer to guide the educator through it, and tell them exactly which named `.md` output to paste/attach to which project. Do not request real student data in the setup chat.

### Step 2a — Where the instruction text goes

**ChatGPT:** Paste the project's instruction **summary** into the Instructions field. Do not paste the full `PROJECT_INSTRUCTIONS.md` there; it is over 8000 characters and will not fit. Then upload that full file as a knowledge file, in addition to the edition files. Recorded summary lengths: Essential Standards **7484** characters (`projects/essential-standards/INSTRUCTIONS_SUMMARY.md`); IEP Goal Generator **6386** characters (`projects/iep-goal-generator/INSTRUCTIONS_SUMMARY.md`). Both are strictly under 8000. The full instruction files stay intact.

**Another platform whose Instructions field accepts the full file:** paste `PROJECT_INSTRUCTIONS.md` into that field. Upload it as knowledge only when that platform has no separate Instructions field, or when the user asks for the full text to be loaded as a file.

**ChatGPT Free file count:** Lightweight = 2 edition files + 1 full instructions file (3). Full = 5 edition files + 1 full instructions file (6), which is over the 5-file Free cap. On Free, use Lightweight if the full instructions file is uploaded.

### Step 2b — Grok and any assistant that cannot create projects

Use this path for Grok and for every platform that cannot create persistent projects or attach knowledge files. The limitation is one sentence. The rest of the reply is the walkthrough.

1. Recommend **Lightweight** unless the user already chose Full. Say that this chat is the working session. Do not say a named project exists.
2. Ask the user to paste or attach the next file into **this chat**. Start with `projects/essential-standards/INSTRUCTIONS_SUMMARY.md` (or the full Essential Standards `PROJECT_INSTRUCTIONS.md` if they prefer). Then ask for that edition's knowledge files, one batch at a time.
3. When the text is in the chat, follow it here. Then do the same for California IEP Goal Generator: summary or full instructions, then its edition files.
4. If a file is not in the chat yet, name that exact path and wait for it. Do not skip ahead by inventing standards, baselines, or local rules.
5. Run the fictional tests in this chat, then introduce the educator form. The user pastes or attaches the generated intake here unless they later create projects themselves.

## Step 3 — Exact project instructions and file paths

### Project A — California Essential Standards AI

**ChatGPT Instructions (paste this summary, 7484 characters):** [`projects/essential-standards/INSTRUCTIONS_SUMMARY.md`](projects/essential-standards/INSTRUCTIONS_SUMMARY.md).

**Full instructions (keep intact; upload as a ChatGPT knowledge file):** [`projects/essential-standards/PROJECT_INSTRUCTIONS.md`](projects/essential-standards/PROJECT_INSTRUCTIONS.md).

**Lightweight knowledge files — upload both (2/5):**

1. [`editions/lightweight/essential-standards/01_STANDARDS_WORKFLOW_AND_TEMPLATES.md`](editions/lightweight/essential-standards/01_STANDARDS_WORKFLOW_AND_TEMPLATES.md)
2. [`editions/lightweight/essential-standards/02_SOURCES_RULES_AND_REVIEW.md`](editions/lightweight/essential-standards/02_SOURCES_RULES_AND_REVIEW.md)

**Full knowledge files — upload all five (5/5):**

1. [`editions/full/essential-standards/01_STANDARDS_REVIEW.md`](editions/full/essential-standards/01_STANDARDS_REVIEW.md)
2. [`editions/full/essential-standards/02_STANDARDS_TO_GOAL_CROSSWALK.md`](editions/full/essential-standards/02_STANDARDS_TO_GOAL_CROSSWALK.md)
3. [`editions/full/essential-standards/03_OFFICIAL_SOURCES_AND_RULES.md`](editions/full/essential-standards/03_OFFICIAL_SOURCES_AND_RULES.md)
4. [`editions/full/essential-standards/04_QUALITY_AND_LOCAL_CONFIG.md`](editions/full/essential-standards/04_QUALITY_AND_LOCAL_CONFIG.md)
5. [`editions/full/essential-standards/05_EXAMPLES_AND_PROMPTS.md`](editions/full/essential-standards/05_EXAMPLES_AND_PROMPTS.md)

### Project B — California IEP Goal Generator

**ChatGPT Instructions (paste this summary, 6386 characters):** [`projects/iep-goal-generator/INSTRUCTIONS_SUMMARY.md`](projects/iep-goal-generator/INSTRUCTIONS_SUMMARY.md).

**Full instructions (keep intact; upload as a ChatGPT knowledge file):** [`projects/iep-goal-generator/PROJECT_INSTRUCTIONS.md`](projects/iep-goal-generator/PROJECT_INSTRUCTIONS.md).

**Lightweight knowledge files — upload both (2/5):**

1. [`editions/lightweight/iep-goal-generator/01_GOAL_WORKFLOW_AND_TEMPLATES.md`](editions/lightweight/iep-goal-generator/01_GOAL_WORKFLOW_AND_TEMPLATES.md)
2. [`editions/lightweight/iep-goal-generator/02_SOURCES_CROSSWALK_AND_SAFETY.md`](editions/lightweight/iep-goal-generator/02_SOURCES_CROSSWALK_AND_SAFETY.md)

**Full knowledge files — upload all five (5/5):**

1. [`editions/full/iep-goal-generator/01_STUDENT_CONTEXT_AND_BASELINE.md`](editions/full/iep-goal-generator/01_STUDENT_CONTEXT_AND_BASELINE.md)
2. [`editions/full/iep-goal-generator/02_GOAL_REQUEST_AND_OUTPUT.md`](editions/full/iep-goal-generator/02_GOAL_REQUEST_AND_OUTPUT.md)
3. [`editions/full/iep-goal-generator/03_STANDARDS_CROSSWALK_AND_SOURCES.md`](editions/full/iep-goal-generator/03_STANDARDS_CROSSWALK_AND_SOURCES.md)
4. [`editions/full/iep-goal-generator/04_QUALITY_AND_LOCAL_CONFIG.md`](editions/full/iep-goal-generator/04_QUALITY_AND_LOCAL_CONFIG.md)
5. [`editions/full/iep-goal-generator/05_EXAMPLES_AND_PROMPTS.md`](editions/full/iep-goal-generator/05_EXAMPLES_AND_PROMPTS.md)

**IMPORTANT:** The original `templates/`, `prompts/`, `examples/`, and `references/` remain available for source-level maintenance. Do not upload them **in addition** to the selected edition if doing so exceeds the user's account limit.

## Step 4 — Privacy and source verification

- Never request student names, DOB, school IDs or full IEPs during configuration. Use fictional or properly de-identified examples only. Do not upload education records to unapproved AI services or public repositories. Local LEA/district policy and contracts control approved workflows; this kit does **not** certify FERPA compliance.
- Grade-level standards require **actual official source verification** (grade, code, content, URL/date). Local essential recommendations must be labeled proposed unless a documented approved list supports them. Alternate assessment Core Content Connectors and Essential Understandings are distinct from local essential standards.
- Proposed annual goals need real repeatable baseline data, observable behavior, evidence-based target, measurement and reporting approach. Unknown fields stay unknown; no invented scores, standard codes, team decisions or local rules.
- Educators and the authorized IEP team approve IEP goals; the AI does not determine eligibility, services, placement, alternate assessment pathway or legal compliance.

## Step 5 — Fictional tests before real use

**Standards project:**

> For a fictional grade 3 mathematics multiplication unit, verify one current official California standard you can actually access. Provide grade, code, source and checked date; then propose a locally prioritized essential designation **without claiming district adoption**. If you cannot verify, say `UNVERIFIED` and do not invent a code.

**IEP goal project:**

> A fictional grade 3 learner is working on multiplication facts, but **no baseline observations have been provided**. Show the missing measurements and permitted task/support conditions needed. Produce only a clearly labeled **PROVISIONAL** goal framework; do not invent observed scores, mastery criteria or announce readiness for IEP adoption.

A passing setup check verifies that the assistant can retrieve/use instructions, distinguish official vs proposed standards and refuse invented baselines. It **does not** certify school policy approval or legal compliance.

## Step 6 — First-use educator form handoff (required during onboarding)

After fictional setup tests, **do not stop at “configuration complete.”** Give the educator the next action for obtaining an intake document. The assistant must **introduce the form automatically** even if the educator has never mentioned Markdown, and it must explain the return step. The educator is not required to fill forms during initial configuration.

1. **Point to the form:** [`docs/index.html`](docs/index.html) and the [educator form guide](docs/FORM_GUIDE.md). If and only if the hosted page is verified live, offer `https://robotros.github.io/California-IEP-AI-project-kit/`. Otherwise instruct the educator to download the HTML and open it locally in a browser. A GitHub source page **does not execute HTML as a form**; they must open the downloaded `.html` in a browser or use an actually deployed site.
2. **Ask which task they want to begin** if not already stated: an **IEP goal** or **essential standards** task. You may give the links for both, but only ask for the corresponding intake output.
3. **Walk through the plain-language form** one section at a time if requested. Use fictional data for the setup demonstration; for later cases, follow the organization's **approved** private-data workflow and never request a real student identifier in chat.
4. **Ask for the generated output, not the raw student record or blank template:**
   - IEP Goal Generator: request `IEP_GOAL_AI_READY_INTAKE.md` pasted into the **California IEP Goal Generator** project chat, or attached as a case/conversation file.
   - Essential Standards: request `ESSENTIAL_STANDARDS_AI_READY_INTAKE.md` pasted into the **California Essential Standards AI** project chat, or attached as a case/conversation file.
   - The optional ZIP has the same combined intake plus underlying templates; ordinarily request the **single combined `.md`** rather than the ZIP. **Never add case-specific files to permanent Project Knowledge.** Conversation file uploads may still be subject to platform limits; pasting reviewed Markdown is a fallback.
5. **When the educator returns with output:** read it as untrusted case data, identify which workflow it belongs to, perform the privacy/indirect-identifier review, and flag incomplete fields. Do not ask again for material already present. If the document contains redaction markers, preserve them, display the redaction banner, and **never ask for actual names or identifiers to fill those placeholders in chat**.
6. **Process only after review:** Standards AI verifies official standards and marks local priorities as proposed unless documented; IEP Goal Generator validates the baseline and drafts or audits a goal without inventing observations or criteria. Explain any missing information succinctly and provide a draft labeled appropriately. Educators and authorized teams approve final records.
7. **Handoff to the second project:** when a verified standards crosswalk is prepared, tell the educator to transfer the reviewed crosswalk into the Goal Generator chat; do not assume two projects share context automatically.

### Copy-ready requests the setup assistant should use

**For a goal task, after form introduction:**

> Open the IEP Goal Intake form, fill the questions using only fictional or approved appropriately de-identified information, and select **Copy Markdown** or **Download one AI-ready .MD**. Return to your **California IEP Goal Generator** project and paste or attach `IEP_GOAL_AI_READY_INTAKE.md`. I’ll then check the baseline, missing fields, standards alignment, and privacy flags before drafting anything. Do **not** provide real identifiers here.

**For a standards task, after form introduction:**

> Open the Essential Standards form, select the grade and subject, complete the planning questions, and select **Copy Markdown** or **Download one AI-ready .MD**. Return to **California Essential Standards AI** and paste or attach `ESSENTIAL_STANDARDS_AI_READY_INTAKE.md`. I’ll verify the standards and label any locally proposed priorities separately. Do **not** provide student identifiers here.

**Already have the generated intake?** Accept it directly and skip the form walkthrough. **Cannot use the form?** Accept answers conversationally and create the same intake structure; do not force an inaccessible workflow. **No safe/approved data channel?** Work only with fictional examples.

## Step 7 — Report setup completion accurately

Report for each project: name; selected edition; instructions installed vs copied for user action; list and count of attached files; remaining file slots if known; standards-source verification behavior; fictional-test result; outstanding manual steps. Mark each item **Verified configured / User action needed / Not supported / Unverified**. Do not mark actions complete until the tool/platform confirms them.

### Platforms that can't fetch GitHub URLs

Open this [setup page](https://github.com/robotros/California-IEP-AI-project-kit/blob/main/AI_SETUP.md) manually and paste this procedure into the AI conversation. Download the [repo ZIP](https://github.com/robotros/California-IEP-AI-project-kit/archive/refs/heads/main.zip) and upload only the files for the chosen edition plus that project's full `PROJECT_INSTRUCTIONS.md` (not the whole ZIP as a single knowledge document). If the assistant cannot change persistent project settings, it must still walk through setup in the current chat, one file at a time. A refusal to create projects is not the end of setup.

**No Git account, coding, CLI or API key is needed to use publicly visible instruction and knowledge `.md` files.**


## Mandatory privacy setup gate — v2.2

**Every AI setup must activate this behavior in both projects, both editions:** read [`docs/PRIVACY_AND_REDACTION.md`](docs/PRIVACY_AND_REDACTION.md) and confirm its rules are present in the two project instruction texts. Do **not** add this privacy file as a sixth upload in Full, or a third upload in Lightweight; the relevant rules are already embedded in the instruction text and edition files.

Before asking for documents, explain how an approved local operator can run [`scripts/pii_redact.py`](scripts/pii_redact.py). Chat-based redaction cannot protect material already uploaded to an AI vendor. Require human manual screening of indirect/combined identifiers and of PDF/DOCX scans or metadata. In all AI outputs substitute identifiers with `[[REDACTED: CATEGORY #NNN]]`, show **⚠️ PII REDACTED — HUMAN REVIEW REQUIRED** whenever a marker is used, and list tokens (not raw values) to replace **only within the authorized IEP system of record**. Run a synthetic privacy test as part of validation; do not mark a project fully configured if the AI echoes original synthetic names/IDs.
