# California Special Education AI Project Kit — v2.4.0 (Factory v1.4.1)

Two independent, educator-reviewed AI specialists with **Light and Full workspace editions**, optional reusable **Skills**, and guided setup across supported AI platforms. **Canonical public source:** [robotros/California-IEP-AI-project-kit](https://github.com/robotros/California-IEP-AI-project-kit). The Factory v1.4.1 files have been published to `main`; actual installation and runtime tests must still be verified independently. No student data belongs in this public repository.

> **Educational draft assistance only.** No assistant is the IEP team, LEA, legal counsel, licensed evaluator or system of record. FERPA and district/SELPA authorization cannot be certified by this kit; use fictional information during setup, and approved private processes for any real student records. Human reviewers verify standards, baselines and outcomes. Typed redactions are assistance, not foolproof de-identification.

## Begin with the AI setup assistant

1. Open **[AI_SETUP_PROMPT.md](AI_SETUP_PROMPT.md)** and paste it into your chosen AI tool. **When you provide neither a ZIP nor a repository link, the assistant must use the default public GitHub source** [https://github.com/robotros/California-IEP-AI-project-kit](https://github.com/robotros/California-IEP-AI-project-kit) and retrieve the needed files in read-only mode. If it cannot access GitHub, it must say so and guide you to attach/download the files; it cannot claim retrieval.
2. It MUST first show a **Projects + Skills support report for all six destinations** using [the support matrix](setup/PLATFORM_SUPPORT_MATRIX.md), with account-specific `NEEDS_VERIFICATION` and fallbacks. It then asks which destination and edition you actually want.
3. Choose Specialist **Light (3 `.md` knowledge files)** or **Full (8 `.md`)** independently for each role. Paste matching `PROJECT_INSTRUCTIONS.txt` into Instructions; unlike v2.3.1 **do not upload a second oversized instructions document**.
4. Install one specialist at a time; test with fictional examples and capture a [deployment receipt](setup/DEPLOYMENT_RECEIPT.md). Native Skill installation, if eligible, is a separate action requiring authorization and fresh trigger/non-trigger tests.
5. At first actual task, offer the existing [offline educator form](docs/index.html) and [form guide](docs/FORM_GUIDE.md); treat its output as case-specific conversation input, not permanent Project knowledge.

## Two specialist roles

| Role | Produces | Human release gate | Specialist Light | Specialist Full |
|---|---|---|---|---|
| **California Essential Standards AI** | Date/source-checked official standard analysis, *proposed* local priorities, curriculum crosswalk | Curriculum/standards professional | [Instructions + 3 refs](specialists/light/essential-standards/) | [Instructions + 8 refs](specialists/full/essential-standards/) |
| **California IEP Goal Generator** | Baseline-based proposed annual goals, audit and progress-monitoring plan | Qualified IEP team/related professional | [Instructions + 3 refs](specialists/light/iep-goal-generator/) | [Instructions + 8 refs](specialists/full/iep-goal-generator/) |

## Package navigation

- [AI_SETUP_PROMPT.md](AI_SETUP_PROMPT.md): copy-paste AI onboarding across platforms, default Projects+Skills report.
- [KIT_MANIFEST.md](KIT_MANIFEST.md): exact per-edition paths, Skill decisions, versions and boundaries.
- [Platform installation](setup/PLATFORM_INSTALLATION.md), [installation checklist](setup/INSTALL_CHECKLIST.md) and [Microsoft-specific setup](setup/MICROSOFT_INSTALLATION.md).
- [Prompt starters](prompts/FACTORY_1_4_1_STARTERS.md) and [cross-project workflow map](WORKFLOW_MAP.md).
- [Edition QA reports](reports/), [overall validation](VALIDATION_REPORT.md), [migration and rollback](setup/MIGRATION_FROM_V2_3_1.md), and [change history](CHANGELOG.md).
- `skills/`: optional standalone Skill source; `distributions/`: ZIPs for **Claude folder-wrapped** and **root-SKILL import**. These are distinct from Project uploads and not yet installed.
- `adapters/microsoft-365-agent-builder/`: per-edition byte-faithful `.txt` transport copies of each `.md`, only for Agent Builder Knowledge list. Studio accepts canonical `.md` in supported upload surface.
- Existing `docs/`, `templates/`, `references/`, `examples/`, `scripts/` and browser form remain in the published repository. They are not extra Project knowledge uploads.
- [MIT License](LICENSE) — original repository code and documentation, subject to any applicable third-party rights; public standards and other third-party materials retain their own terms.

## Essential flow

**Official CDE source and approved local context → Essential Standards AI → human checks verified curriculum packet → IEP Goal Generator adds authorized de-identified baseline → human/IEP-team final review → record entry in authorized system only.** No shared state, automatic inter-agent messaging or autonomous student-record action.

## What changed since v2.3.1

Factory v1.4.1 now mandates 3/8 files per role, independent <=7,500-character instruction fields, explicit native Skill suitability, platform/plan readiness reports, transport adapters, evidence-tagged QA and rollback. The v2.3.1 2/5 archive and full-instructions upload remain as migration sources **only**, not the new installation route. Do not mix editions or claim that old tests validated these new files.

See [README deployment links](setup/PLATFORM_INSTALLATION.md), [validation](VALIDATION_REPORT.md), and [historical transition](setup/MIGRATION_FROM_V2_3_1.md). This GitHub repository is published, but publication alone is **not** proof of a configured/operationally tested AI workspace or institution-approved student data processing.
