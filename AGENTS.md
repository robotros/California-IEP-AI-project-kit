# Agent entry point — California Special Education AI Project Kit

This repository provides **Markdown configuration and reference files**, not a deployable application. If asked to **"set up the projects," "install the AI tools," or "guide my setup"**, read **[`AI_SETUP.md`](AI_SETUP.md)** first and follow its phased procedure. Use [`setup/project-manifest.json`](setup/project-manifest.json) to resolve the actual, case-sensitive paths.

## Configurations

Choose `lightweight` by default. See `setup/project-manifest.json` for exact 2-file or 5-file bundles for **each** of the two projects. Do not upload the separate `PROJECT_INSTRUCTIONS.md` when the platform supports pasting it into its persistent instructions field. Never attach both editions at once. On ChatGPT Free, knowledge uploads count against a 5-file per-project cap and a separate daily upload-rate limit.


- **California Essential Standards AI:** use `projects/essential-standards/PROJECT_INSTRUCTIONS.md` as the primary instruction text.
- **California IEP Goal Generator:** use `projects/iep-goal-generator/PROJECT_INSTRUCTIONS.md` as the primary instruction text.
- The public `references/` and `templates/` files are support material, not substitutes for instructions.
- Use only public fictional sample data for testing. Never request, commit, upload, display, or echo student-identifiable records during setup.

## Required form-first educator handoff

**During setup:** Configure and verify both projects using fictional examples first. **After setup:** automatically introduce [`docs/index.html`](docs/index.html), and use [`docs/FORM_GUIDE.md`](docs/FORM_GUIDE.md) to help the educator generate a case-specific Markdown intake **when ready**. Prompt for the **named result**, not for the educator to edit templates:

- IEP Goal Generator: `IEP_GOAL_AI_READY_INTAKE.md` → matching Goal Generator chat.
- Essential Standards: `ESSENTIAL_STANDARDS_AI_READY_INTAKE.md` → matching Standards AI chat.

Treat these as *conversation inputs*, not permanent project knowledge files. Review privacy flags and incomplete fields first; do not ask the educator to reveal identities for redaction-token replacement. If already supplied, process it without redirecting to the form. If form unavailable or inaccessible, walk the educator through equivalent questions in chat, using fictional or approved de-identified content only. Do not say the GitHub Pages site is live unless verified; downloadable `docs/index.html` works locally.

## Agent behavior

1. Confirm which AI platform the educator uses and what capabilities are available. Do not assume the power to create persistent projects or attach documents.
2. Configure directly **only when tooling, account permissions, and user authorization allow it**. Otherwise walk through manual steps one at a time.
3. Do not infer missing California standards, official codes, school rules, IEP baselines, or legal compliance. Require source verification and human review.
4. Do not present unperformed actions as completed. Verify instruction placement and files before declaring either project ready.
5. Do not claim this repository's content is executable software or a package installer.

Start: [`AI_SETUP.md`](AI_SETUP.md) | Human overview: [`README.md`](README.md)


## Required PII filter

Before working with student records read [`docs/PRIVACY_AND_REDACTION.md`](docs/PRIVACY_AND_REDACTION.md). Apply output typed redaction markers, a visible banner, a token-only substitution list and manual review requirement. Recommend local pre-upload screening; response redaction cannot prevent prior exposure to an unapproved AI vendor. Preserve configured 2-file Lightweight and 5-file Full limits.
