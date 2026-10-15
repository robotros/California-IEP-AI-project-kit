# Educator Guided Form — Markdown Builder v2.3

The form is a **standalone, client-side HTML file** at [`docs/index.html`](index.html). Educators do **not** need to edit the original Markdown templates or install Python, npm, Git, or a GitHub account.

## Launch

- **Offline (preferred for testing):** Download `docs/index.html` and open it in a current browser. No server or libraries are required. Test it with the built-in fictional example first.
- **Share via GitHub Pages (repository owner action):** GitHub repository **Settings → Pages → Build and deployment → Deploy from a branch → `main` → `/docs` → Save**, if that feature is available for the account/repository. Then share:
  `https://robotros.github.io/California-IEP-AI-project-kit/`
  The Pages URL is **not live until Pages is configured and deployed**. A Pages site is public; use only an institution-approved browser/workflow with education data.
- **No Pages access:** Users can download the repo ZIP and open `docs/index.html` locally; or continue to use Markdown templates manually.

## What to do when an AI assistant sends you here

Your setup assistant should have already configured and tested both projects with **fictional data**. Select the tab that matches your task, complete the form using only information allowed by your institution, and return the resulting **single combined Markdown** to the matching project chat. You can paste it directly instead of uploading another file.

- **IEP Goal Intake** → `IEP_GOAL_AI_READY_INTAKE.md` → **California IEP Goal Generator 2.0**.
- **Essential Standards** → `ESSENTIAL_STANDARDS_AI_READY_INTAKE.md` → **California Essential Standards AI**.

If you have already supplied the intake information to the AI, it should not make you fill the form again. If you cannot use the form, ask for a guided chat-based intake instead. Never provide real identifiers in an unapproved chat, and never replace `[[REDACTED: ...]]` placeholders in the AI conversation.

## Educator workflow

1. Choose **IEP Goal Intake** or **Essential Standards**.
2. Fill the plain-language fields. The form has built-in examples using fictional information only. A student alias such as `STUDENT-A` is sufficient; do not enter a real name.
3. Review the Markdown preview. Blank fields produce `[MISSING — educator must supply or verify]`. No benchmark, official standard, goal criterion, or student result is fabricated.
4. Acknowledge that the information is fictional or properly de-identified and that human review is required.
5. Choose **Copy Markdown** (paste into your AI chat, avoiding a file upload), download **one AI-ready `.md`** (easiest) or download **all generated `.md` files in a `.zip`**. The ZIP includes a privacy review checklist.
6. Open the relevant configured AI project and attach the **combined Markdown file to the chat/conversation**, not permanently to the project's knowledge section. Keep the project's 2-file Lightweight / 5-file Full uploaded knowledge files unchanged.
7. Review the output with qualified educational staff; if a redaction marker remains, substitute it only within the authorized system of record.

## Files produced

| Workflow | AI-ready combined file | ZIP detail files |
|---|---|---|
| IEP Goal Intake | `IEP_GOAL_AI_READY_INTAKE.md` | `student-profile-intake.md`, `present-levels-baseline.md`, `goal-request.md`, `privacy-review.md` |
| Essential Standards | `ESSENTIAL_STANDARDS_AI_READY_INTAKE.md` | `essential-standards-review.md`, `standards-to-goal-crosswalk.md`, `privacy-review.md` |

Each ZIP includes its corresponding combined file as well. The form deliberately generates **intake requests**, **not adopted IEP goals** or purportedly verified California standards.

## Privacy/security behavior and limitations

The HTML file is self-contained: it has **no backend, third-party libraries, analytics, fetch/XHR calls, cookies, or application-level local storage**. Fields are processed in browser memory; the site neither saves drafts nor sends inputs over a network. A restrictive Content Security Policy disables network requests from this app. The device/browser and browser extensions remain outside that guarantee.

Text values are screened for certain recognizable email addresses, phone numbers, street addresses, SSNs, **labeled** DOBs/student IDs, context-labeled names, and obvious full names typed into the alias field. Recognized instances are replaced using markers such as `[[REDACTED: STUDENT_NAME #001]]`. The generator always shows a review flag, includes a human checklist, and never stores a mapping of removed values. Pattern detection is incomplete: it can miss names, unusual identifiers, re-identifiable combinations, and sensitive context. **Zero hits is not proof of de-identification or legal compliance.** The more thorough local Python preflight utility in [`../scripts/pii_redact.py`](../scripts/pii_redact.py) remains a separate screening option.

No document produced by the form should be treated as ready for transmission to an unapproved AI service; district/LEA procedures and vendor approvals determine the permissible handling of education records. Actual identifiers belong only in an authorized IEP system of record. Browser downloads themselves are files on the educator's device and must be handled under local retention/security policies.

## Maintaining and testing the form

The UI is deliberately delivered as one `docs/index.html` file so it can run locally and on GitHub Pages with no build step. Run repository tests and the HTML regression script:

```bash
python scripts/validate_project_kit.py
python -m unittest discover -s scripts -p 'test_pii_redact.py' -v
python scripts/test_form_static.py
```

The last test checks source safety, form elements, JavaScript syntax where Node.js is available, and wiring. Manual/browser smoke tests should also cover downloads, both form tabs, marker substitution, and no network traffic. The form has been tested in Chromium against synthetic entries, with downloads inspected as valid ZIP files.
