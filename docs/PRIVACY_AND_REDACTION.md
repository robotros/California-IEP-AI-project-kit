# Privacy screening and typed redaction — California Special Education AI (v2.2)

**Scope:** Both the IEP Goal Generator and Essential Standards AI; both Lightweight and Full editions. **Human privacy review is mandatory.** This is an operational risk-reduction feature, **not** a legal opinion, proof of de-identification, FERPA certification, or permission to upload protected records to consumer AI services.

## Legal framework and coverage

For **pupil records**, prioritize the federal **FERPA 34 CFR §99.3** definition of personally identifiable information: student and family names, student/family address, SSN/student number/biometrics, date and place of birth, mother's maiden name, information linked or linkable to a student even when no direct identifier is present, and identification using combined details by a reasonable person in the school community. See [U.S. Department of Education FERPA regulations](https://studentprivacy.ed.gov/ferpa) and [PII guidance](https://studentprivacy.ed.gov/content/personally-identifiable-information-education-records).

California **Education Code §49061(b)** defines pupil records in terms of information directly related to an identifiable pupil (subject to statutory distinctions) and **§49073.1** imposes contractual requirements when LEAs use eligible third-party services for pupil records. Check [§49061](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=EDC&sectionNum=49061.) and [§49073.1](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=EDC&sectionNum=49073.1.) in the current official statutory text. These duties are not reduced to a name-matching regex.

California **Civil Code §1798.140** (CCPA/CPRA) also uses a broad notion of personal information linked or reasonably linkable to consumers or households, with sensitive personal information categories; **its business applicability, exemptions and legal obligations are separate** from FERPA/education-record handling. See [California DOJ CCPA guidance](https://oag.ca.gov/privacy/ccpa) and [statute](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1798.140.). The scanner uses these concepts to choose conservative detection categories; it does not claim the same statute governs every school file.

## Browser form option (v2.3)

The standalone [`docs/index.html`](index.html) provides optional **in-browser** intake and Markdown generation, plus a narrow set of recognizable direct-identifier substitutions. It processes the typed values in browser memory with no remote request, tracking library, or built-in persistence. This client-side pattern check has **less coverage** than reviewed institutional DLP tools and should be treated only as early warning. It does not prevent identifiable information from appearing briefly in the form fields, nor screen all free text, combined identifiers or external device/browser behavior. Downloaded and clipboard-copied Markdown always needs manual review before any transfer to an AI service. See [`FORM_GUIDE.md`](FORM_GUIDE.md) for usage details. **The form does not certify legal de-identification.**

## Detect and redact

1. **Before transmission to any AI provider**, use an approved local/private workflow to examine files. No live student records are required to set up the projects.
2. The offline `scripts/pii_redact.py` searches recognizable patterns, labeled fields, and structured CSV/JSON fields. It produces **redacted text copies only**, leaving originals unchanged.
3. Every replacement uses a **typed, numbered marker**: `[[REDACTED: STUDENT_NAME #001]]`, `[[REDACTED: DATE_OF_BIRTH #001]]`, `[[REDACTED: STUDENT_ID #001]]`, `[[REDACTED: EMAIL_ADDRESS #001]]`, etc. The same recognized input value within a run receives the same token. No unredacted lookup file is created.
4. The generated `pii_review_report.json` contains **categories and marker IDs only**, not original values, names, or filenames. All outputs are marked `HOLD_FOR_HUMAN_REVIEW`.
5. **Manual review remains required** for unlabeled names, unusual addresses, combinations of grade/rare disability/school/incident and small-group details, images, audio, free-text identities, biometrics, birthplaces, geographic clues, and metadata. A zero-match scan is **not** clearance or legal de-identification.
6. Do not assume directory information is automatically safe for AI uploads. Confirm LEA policy, applicable disclosures, and the service provider's approved security/contractual controls.
7. Never embed actual identifiers, re-identification keys, or protected student files in this public repository, pull request, issue, CI artifact, or setup chat.

### Offline usage (run in district-approved local environment)

```bash
# TXT/Markdown/CSV/TSV/JSON/YAML use Python standard library.
python scripts/pii_redact.py /approved/private/input --out-dir /approved/private/redacted --strict

# Optional private file listing, one known individual per line, improves name detection.
python scripts/pii_redact.py /approved/private/input --out-dir /approved/private/redacted --names-file /approved/private/known-names.txt
```

For PDFs and DOCX, **optional** `PyMuPDF` and `python-docx` dependencies extract **text only**. The script does NOT generate a redacted PDF/DOCX or sanitize its embedded content, images, comments, hidden XML, metadata, or file properties. Scanned PDFs without extracted text are **blocked**, not silently declared safe. For PDF/DOCX inputs, the output is a `.txt` copy of extractable text with markers; inspect the original and any other data channels separately. No OCR is performed.

Exit codes: `0` completed with review required; `2` detection found with `--strict`; `3` at least one file blocked/uninspected. No result signifies legal clearance. Keep outputs in private directories outside the repository; do not publish even redacted files until independently approved.

## Mandatory behavior for BOTH AI projects

- **On intake:** If the material is not confirmed synthetic, treat identifiers as sensitive. Explain that automatic detection is incomplete; request de-identified or institutionally approved inputs rather than directing users to paste original records into chat.
- **On output:** Never reproduce apparent PII. Replace each occurrence with the exact typed marker form `[[REDACTED: CATEGORY #NNN]]`, including headings, sample data, tables, quotes, file text, feedback, downloadable artifacts, and summaries. Use the same marker for repeated appearances in the same response. Prefer conservative omission if unsure.
- **Banner if any marker appears:** `⚠️ PII REDACTED — HUMAN REVIEW REQUIRED. Replace the marked fields ONLY in the authorized IEP system of record. Do not send originals or replacements back into the AI chat.`
- **Redaction checklist:** At the end of the response, list each placeholder **by category and token only**. Example: `[[REDACTED: STUDENT_NAME #001]] — student name — substitute inside the approved system of record.` Never display the removed values or reconstruct them in notes.
- **If no match:** Use `PII SCREENING INCOMPLETE — no obvious direct identifiers reproduced; manually assess indirect/combined identifiers.` Do not say "PII-free", "FERPA compliant", or "safe to share".
- **With meaningful context:** Keep nonidentifying performance data (e.g., 6/10 with supports), academic standard codes, task conditions, and goal timelines when they do not uniquely identify someone. Do not blindly remove useful educational information; assess combined identifiability.
- **Before entry in the system of record:** A qualified authorized user must check the draft, substitute the actual identifiers **only within the authorized system**, verify no markers remain, and approve the IEP content through the appropriate process. Do not request a re-identification mapping in chat.

### Example — synthetic only

**Input (never supply real PII to an unapproved AI):** `Student Name: Example Learner; Student ID: [synthetic ID]; baseline 6/10.`

**Expected response style:**

> ⚠️ PII REDACTED — HUMAN REVIEW REQUIRED. Replace flagged placeholders only in the authorized IEP system of record.
>
> `[[REDACTED: STUDENT_NAME #001]]` currently answers 6/10 opportunities under the supplied conditions.
>
> **Redactions to substitute:** `[[REDACTED: STUDENT_NAME #001]]` — student name.

## Threat model and known gaps

- **Regex is incomplete by design.** Arbitrary names in paragraphs, rare facts, unusual ID formats, images, scanned PDF pages, hidden document data, family relation clues, and indirect re-identification are not fully solved by this tool. Use local named-entity checks, approved DLP tools and trained human reviewers where warranted.
- **AI response redaction happens after input is sent.** It cannot retroactively protect information already shared with an external AI provider. Local screening before upload and vendor authorization are distinct safeguards.
- **The CLI cannot detect protected attributes in every context.** A disability/health datum tied to an identifiable student is highly sensitive; whether it can be retained as de-identified instructional context requires human review.
- **False positives happen.** Review markers before copying into an official record; remove only within an approved private workflow.
- **Do not assume `--strict` means complete screening.** It merely exits nonzero when the patterns found a match.
