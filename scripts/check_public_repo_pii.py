#!/usr/bin/env python3
"""Screen public repo prose and configurations for obvious PII; no raw values logged."""
from pathlib import Path
from pii_redact import Redactor

ROOT=Path(__file__).resolve().parent.parent
INCLUDE={'.md','.json','.yaml','.yml','.txt','.csv','.tsv','.py'}
EXCLUDE={'scripts/test_pii_redact.py','examples/fictional-worked-example.md','docs/PRIVACY_AND_REDACTION.md'}
# Binary student documents should never silently pass text-only repository scans.
SENSITIVE_BINARY={'.pdf','.docx','.doc','.xlsx','.xls','.pptx','.zip','.jpg','.jpeg','.png','.webp','.tiff','.heic'}
# Repository maintainers may add already-reviewed public branding assets to this set.
REVIEWED_PUBLIC_ASSETS=set()
issues=[]
for p in ROOT.rglob('*'):
    if not p.is_file() or p.relative_to(ROOT).as_posix() in EXCLUDE:
        continue
    if p.suffix.lower() in SENSITIVE_BINARY and p.relative_to(ROOT).as_posix() not in REVIEWED_PUBLIC_ASSETS:
        issues.append(p.relative_to(ROOT).as_posix()+' — binary requires explicit human privacy review')
        continue
    if p.suffix.lower() not in INCLUDE:continue
    try:
        original=p.read_text(encoding='utf-8')
        r=Redactor()
        r.text(original)
    except (OSError,UnicodeError):
        issues.append(str(p.relative_to(ROOT))+' (unreadable)')
        continue
    if r.tokens:
        categories=sorted({kind for kind,_ in r.tokens})
        issues.append(p.relative_to(ROOT).as_posix()+' — '+', '.join(categories))
if issues:
    for item in issues:print('PII REVIEW REQUIRED:',item)
    raise SystemExit(1)
print('PASS: no recognizable direct identifiers in scanned public repository files (not a de-identification guarantee)')
