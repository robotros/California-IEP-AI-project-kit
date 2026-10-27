# California High-Quality IEP Educator Assistant — v1.0.0

A **new, independent** educator-oriented, conversation-led IEP drafting and review kit for California. Informed by the [High Quality IEPs educator journey](https://highqualityieps.net/iep-journey/resources-for-educators) and functionally modeled on the [California IEP AI Project Kit](https://github.com/robotros/California-IEP-AI-project-kit). Neither project endorses, operates or certifies this package. Third-party instructional materials remain at their original URLs; this kit does not republish them.

**Scope:** special education providers, general education teachers and administrative designees, with BEFORE/DURING/AFTER workflow and standards / present levels / goal drafting / goal auditing / implementation / guidance updates. All case outputs are drafts requiring authorized human/IEP team review. No student-specific data in kit files.

**Most important safeguard:** Every substantive IEP task requires a **live state + federal Current Guidance Gate** when authoritative browsing exists. Without it, legal/compliance findings are ON HOLD and educational drafts are explicitly provisional. This source register cannot update itself or promise unattended monitoring. Human owner approves updates and installations.

## Quick start (no code or paid API needed)
1. Read [AI setup prompt](AI_SETUP_PROMPT.md) and [install sheet](setup/PLATFORM_INSTALLATION.md). Choose platform/plan and **either** Specialist Light or Specialist Full.
2. Create **one** private workspace/agent called `California HQ IEP Educator Assistant`. Paste the selected `specialists/<edition>/iep-educator/PROJECT_INSTRUCTIONS.txt` into its **Instructions** field. Upload **exactly 3 Light or 8 Full `.md`** canonical knowledge files from that same folder. Do not upload the instruction text as a knowledge file.
3. Verify saved files and instructions, test with **fictional** material in a **fresh conversation**, and record findings in [installation checklist](setup/INSTALL_CHECKLIST.md) and [receipt](setup/DEPLOYMENT_RECEIPT.md).
4. Optional: use the [offline educator intake form](docs/index.html) and [form guide](docs/FORM_GUIDE.md). Treat generated case text as conversation-specific input, not permanent knowledge. This form is not a FERPA certification or perfect PII scrubber.
5. Native Skills: see [Skill guide](skills/README.md). Skill ZIPs are separate from workspace installation. If the account cannot install Skills, use the Project's built-in audit workflow.

## Package navigation
- [Manifest](KIT_MANIFEST.md) — exact role and counts, assumptions, classification, Skill decision
- [Prompt starters](prompts/READY_TO_USE_PROMPTS.md) and [templates](templates/)
- [Workflow map](WORKFLOW_MAP.md) — evidence-to-goal and change-control flow
- [Primary-source update procedure](setup/GUIDANCE_UPDATE_PROTOCOL.md)
- [Microsoft installation](setup/MICROSOFT_INSTALLATION.md) — `.txt` transport copies for Agent Builder, native `.md` for supported Studio configuration
- [Validation report](VALIDATION_REPORT.md) and [change log](CHANGELOG.md)

**Caution:** Do not enter student names, DOB, student IDs, exact schools or student-identifiable records into a nonapproved AI system. A school/LEA must first approve the specific provider and educational data use under its privacy/security practices. AI-driven masking cannot reverse disclosure after submission. Use synthetic examples for testing. Final IEP determinations and record entry stay with the authorized IEP team and district system.

## Delivery state
`GENERATED_ONLY`: ZIP is a reusable package, **not** a GitHub publication, active ChatGPT Project, agent, account Skill, district-approved service or operationally tested IEP workflow. See [deployment receipt](setup/DEPLOYMENT_RECEIPT.md). There is no automation performing ongoing change monitoring until separately authorized and configured.

For curated official HQ IEPs pages by educator role and meeting phase, see [educator resource map](docs/EDUCATOR_RESOURCE_MAP.md).