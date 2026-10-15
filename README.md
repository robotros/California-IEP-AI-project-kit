# California Special Education AI Project Kit (v2.3.1)

**Markdown-first, Git-ready toolkit** for two coordinated projects:

1. **California IEP Goal Generator** — drafts and reviews individualized, measurable annual IEP goals from documented present levels, baseline evidence, and relevant standards.
2. **California Essential Standards AI** — verifies California standards, supports transparent local priority/essential-standard selection, and prepares a standards-to-goal handoff.

> [!IMPORTANT]
> **Educational drafting aid only.** This repository is not an IEP system of record, legal advice, a compliance certification, or a replacement for the IEP team. AI output must be reviewed by qualified staff against current law, official standards, and district/SELPA policies before use. Never upload identifiable student records to an unapproved AI service or a public Git repository.

**Instruction content version:** 2.0 · **Setup editions:** 2.1 · **Source notes last researched:** 2026-10-14 · **Audience:** California educators, case managers, related-service providers, curriculum teams and reviewers.

## Educator-friendly form — no Markdown editing

**Updated in v2.3.1:** Fill out a private, browser-based guided form instead of manually editing `.md` templates:

- **[Open the offline-capable form source](docs/index.html)** — save the HTML file and open it in a browser.
- **[Read the short form guide](docs/FORM_GUIDE.md)** — includes offline use and optional GitHub Pages hosting.
- **Future hosted form URL (only after GitHub Pages is enabled):** `https://robotros.github.io/California-IEP-AI-project-kit/`

After the AI has configured and tested both projects, **it should automatically introduce the form and ask for its generated `.md` output when an educator starts a task**. Goal tasks return `IEP_GOAL_AI_READY_INTAKE.md` to Goal Generator; standards tasks return `ESSENTIAL_STANDARDS_AI_READY_INTAKE.md` to Essential Standards AI. **Do not send real identifiers into an unapproved AI conversation.**

The form covers **IEP Goal Intake** and **Essential Standards**, shows missing fields and PII review flags, then lets educators copy Markdown into chat, download one combined AI-ready Markdown file, or download individual templates as a ZIP. There is **no backend or data upload by the form itself**. Use fictional inputs for setup; real student information requires district-approved controls. Attach generated `.md` to a **conversation**, not permanent project knowledge, so both **Lightweight (2 files)** and **Full (5 files)** bundles remain unchanged.

## Set up with your AI assistant — one shareable link

**No Git or coding required for educators.** Copy this link into an AI assistant that can read public GitHub files:

**[Open the guided AI setup instructions](AI_SETUP.md)**

`https://github.com/robotros/California-IEP-AI-project-kit/blob/main/AI_SETUP.md`

> **Copy into your AI chat:** Set up both California Special Education AI projects using the guide at https://github.com/robotros/California-IEP-AI-project-kit/blob/main/AI_SETUP.md. Read the files first. Configure whatever your platform actually supports; otherwise guide me through each action one step at a time. Start with fictional test data, never real student records, and verify each configuration before saying it is complete. Then direct me to the educator form and ask me to return its generated Markdown to the matching project when I am ready to use it.

The guide creates two **separate configured AI projects or platform equivalents**. It is not a software installer, and no AI service can guarantee automatic setup across every provider. If your assistant cannot open GitHub links, open [AI_SETUP.md](AI_SETUP.md) yourself and paste the instructions, or upload the public Markdown files. Agent-capable tools may also read [AGENTS.md](AGENTS.md) and the [machine-readable project manifest](setup/project-manifest.json).

## One-link AI setup — choose Lightweight or Full

Give your AI assistant **[`AI_SETUP.md`](AI_SETUP.md)**. It will guide creation of **two projects**. Select one edition per project:

| Edition | Goal Generator attachments | Essential Standards attachments | Free slots left per project |
|---|---:|---:|---:|
| **Lightweight (recommended for Free)** | 2 | 2 | 3 |
| **Full (detailed templates and examples)** | 5 | 5 | 0 |

Copy each project's `PROJECT_INSTRUCTIONS.md` into the platform's dedicated **Project Instructions field**, which avoids consuming an attachment slot. [See exact file lists and limitations](editions/README.md). OpenAI documents Free = 5 project files with a separate daily file upload limit; these may affect whether both projects can be finished in one day. This repo does **not** automatically install into external AI services.

## Quick start

1. **Clone/unzip the repository.** No installation or dependencies are required; these are Markdown instructions and templates.
2. **Select an edition**, using the [guided setup page](AI_SETUP.md) (Lightweight = 2 supporting files per project; Full = 5). **Create two separate AI projects** (or equivalent configured assistants):
   - Paste [`projects/iep-goal-generator/PROJECT_INSTRUCTIONS.md`](projects/iep-goal-generator/PROJECT_INSTRUCTIONS.md) into the **IEP Goal Generator 2.0** project's instruction area.
   - Paste [`projects/essential-standards/PROJECT_INSTRUCTIONS.md`](projects/essential-standards/PROJECT_INSTRUCTIONS.md) into the **Essential Standards AI** project's instruction area.
3. **Configure local rules** using [`templates/shared/local-configuration.md`](templates/shared/local-configuration.md). Keep local configuration and student-specific data in an approved private environment, **outside this public/shared repository**.
4. **Attach only the knowledge files listed for that edition** in [`AI_SETUP.md`](AI_SETUP.md). The original source guide is also preserved at [`references/authoritative-sources-and-rules.md`](references/authoritative-sources-and-rules.md); recheck official standards and legal sources before use.
5. **Run the standards workflow** with [`templates/standards/essential-standards-review.md`](templates/standards/essential-standards-review.md), then complete [`templates/standards/standards-to-goal-crosswalk.md`](templates/standards/standards-to-goal-crosswalk.md).
6. **Run the IEP goal workflow** using the student intake, baseline and goal-request templates. Use the goal-output template, then complete the human quality review.

**Start with fictional information:** [`examples/fictional-worked-example.md`](examples/fictional-worked-example.md) and [`prompts/ready-to-use-prompts.md`](prompts/ready-to-use-prompts.md).

## Repository structure

```text
california-special-education-ai/
├── README.md
├── AI_SETUP.md                 # Shareable setup link and guided AI procedure
├── AGENTS.md                   # Entry point for repository-aware AI agents
├── setup/
│   └── project-manifest.json   # Edition-aware file map
├── editions/
│   ├── README.md                 # File counts and comparison
│   ├── lightweight/             # 2 knowledge files per project
│   └── full/                    # 5 knowledge files per project
├── .gitignore
├── .gitattributes
├── projects/
│   ├── iep-goal-generator/
│   │   └── PROJECT_INSTRUCTIONS.md
│   └── essential-standards/
│       └── PROJECT_INSTRUCTIONS.md
├── templates/
│   ├── iep/
│   │   ├── student-profile-intake.md
│   │   ├── present-levels-baseline.md
│   │   ├── goal-request.md
│   │   └── goal-output.md
│   ├── standards/
│   │   ├── essential-standards-review.md
│   │   └── standards-to-goal-crosswalk.md
│   └── shared/
│       ├── local-configuration.md
│       └── quality-review-and-approval.md
├── references/
│   └── authoritative-sources-and-rules.md
├── prompts/
│   └── ready-to-use-prompts.md
├── examples/
│   └── fictional-worked-example.md
└── docs/
    ├── index.html              # Standalone browser-based form
    ├── FORM_GUIDE.md           # Educator instructions and hosting
    └── WORKFLOW.md
```

## Use the two projects together

```text
Official California standards + approved local curriculum
                         │
                         ▼
             Essential Standards AI
             ├── Verify code, grade, subject, source
             ├── Propose or document local priorities
             └── Produce standards-to-goal crosswalk
                         │
              human/source verification
                         │
                         ▼
            IEP Goal Generator 2.0
             ├── De-identified student context
             ├── Present levels and measurable baseline
             ├── Draft individualized annual goals
             └── Define measurement/reporting approach
                         │
                         ▼
                Human quality review
                         │
                         ▼
              Authorized IEP team process
```

The standards project **does not set a student's IEP goal on its own**. The goal project **must not fabricate missing baselines**, standard codes, achievement levels, team decisions or local requirements. When essential information is missing, use a clearly labeled incomplete draft and request verification.

## Template index

| Task | File |
|---|---|
| Configure local policies/permissions | [`templates/shared/local-configuration.md`](templates/shared/local-configuration.md) |
| Record de-identified student context | [`templates/iep/student-profile-intake.md`](templates/iep/student-profile-intake.md) |
| Document present levels and baseline | [`templates/iep/present-levels-baseline.md`](templates/iep/present-levels-baseline.md) |
| Request goal creation, revision or audit | [`templates/iep/goal-request.md`](templates/iep/goal-request.md) |
| Format goal drafts and progress monitoring | [`templates/iep/goal-output.md`](templates/iep/goal-output.md) |
| Evaluate/verify standards | [`templates/standards/essential-standards-review.md`](templates/standards/essential-standards-review.md) |
| Handoff standards and prerequisite-skill pathway | [`templates/standards/standards-to-goal-crosswalk.md`](templates/standards/standards-to-goal-crosswalk.md) |
| Complete educator review/approval checklist | [`templates/shared/quality-review-and-approval.md`](templates/shared/quality-review-and-approval.md) |
| Follow source/verification rules | [`references/authoritative-sources-and-rules.md`](references/authoritative-sources-and-rules.md) |
| Test with fictional data | [`examples/fictional-worked-example.md`](examples/fictional-worked-example.md) |
| Use copy-ready requests | [`prompts/ready-to-use-prompts.md`](prompts/ready-to-use-prompts.md) |

For a longer walkthrough, see [`docs/WORKFLOW.md`](docs/WORKFLOW.md).

## Safeguards and scope

- **Do not commit protected student data.** Use invented IDs and synthetic/de-identified examples; direct and indirect identifiers together can identify a student. The `.gitignore` blocks common local working folders, but **Git ignore rules are not a privacy/security control** and do not protect files already committed.
- **Verification is mandatory.** Check grade, code, wording, edition, and official URL before labeling a standard `VERIFIED OFFICIAL`. Distinguish approved local essential standards from an AI-proposed selection.
- **Individualization is mandatory.** Use actual baseline conditions, metric/denominator, task, support level, sampling information, and observed dates, or mark the goal `INCOMPLETE / REQUIRES VERIFICATION`.
- **Do not equate categories.** State academic content standards, locally prioritized essential standards, Core Content Connectors, and Essential Understandings are distinct resources.
- **Human approval is mandatory.** Educators and the authorized IEP team make eligibility, alternate-assessment, placement, services and final goal decisions. The assistant does not.
- **Review current sources.** The included source notes carry an October 14, 2026 review date; recheck legal/standards changes before adoption.

## Git usage

```bash
git init
git add README.md AI_SETUP.md AGENTS.md setup .gitignore .gitattributes projects templates references prompts examples docs
git commit -m "Add California special education AI project kit v2.0"
```

For a new GitHub repository, create an **empty repository**, add the chosen remote, and push your initial commit. Keep actual student inputs, outputs, and unapproved local policy documents outside the repository. If sensitive information has already been committed, removing it from a later commit is **not sufficient**: follow your organization's incident and history-remediation process.

## License and attribution

**No software/content license is included.** Choose and add a license deliberately before treating this as an open-source project. External laws, standards and linked reference materials remain subject to their original terms and should be linked/attributed rather than copied without review.


## Privacy preflight and response redaction (v2.2)

**Before sharing student-specific data with AI:** use the offline [PII redaction guide](docs/PRIVACY_AND_REDACTION.md), the [scanner](scripts/pii_redact.py) in an approved local environment and a human privacy reviewer. This is not a compliance certification. Both editions now **redact PII in generated responses** using typed `[[REDACTED: TYPE #001]]` markers and a conspicuous record-entry substitution warning. No additional Project knowledge files are needed; this behavior is embedded in both projects' instruction texts and 2-/5-file bundles. [Review checklist](templates/shared/pii-redaction-review.md).
