#!/usr/bin/env python3
"""Screen public repo prose and configurations for obvious PII; no raw values logged."""
from pathlib import Path, PurePosixPath
import stat
import zipfile
from pii_redact import Redactor

ROOT=Path(__file__).resolve().parent.parent
INCLUDE={'.md','.json','.yaml','.yml','.txt','.csv','.tsv','.py'}
EXCLUDE={'scripts/test_pii_redact.py','examples/fictional-worked-example.md','docs/PRIVACY_AND_REDACTION.md'}
# Binary student documents should never silently pass text-only repository scans.
SENSITIVE_BINARY={'.pdf','.docx','.doc','.xlsx','.xls','.pptx','.jpg','.jpeg','.png','.webp','.tiff','.heic'}
# Repository maintainers may add already-reviewed public branding assets to this set.
REVIEWED_PUBLIC_ASSETS=set()

# An instruction-only Skill ZIP is not an opaque binary: inspect each contained
# text file as rigorously as ordinary source files. Keep failing closed for
# executable, nested, unreadable, oversized, or path-traversal archives.
def scan_text_only_zip(path):
    findings=[]
    try:
        with zipfile.ZipFile(path) as archive:
            entries=archive.infolist()
            if not entries or len(entries)>30:
                return ['unexpected entry count']
            seen=set()
            total=0
            for info in entries:
                name=info.filename
                pure=PurePosixPath(name)
                if (not name or name.startswith('/') or '\\' in name
                    or '..' in pure.parts or name in seen
                    or stat.S_ISLNK(info.external_attr >> 16)):
                    return ['unsafe archive path or symlink']
                seen.add(name)
                if info.is_dir():
                    continue
                if pure.suffix.lower() not in {'.md','.txt','.json','.yaml','.yml'}:
                    return ['contains non-text or executable content']
                total+=info.file_size
                if info.file_size>1048576 or total>5242880:
                    return ['archive text size limit exceeded']
                try:
                    text=archive.read(info).decode('utf-8')
                except (UnicodeError,OSError,RuntimeError,ValueError):
                    return ['unreadable ZIP entry']
                redactor=Redactor()
                redactor.text(text)
                if redactor.tokens:
                    categories=sorted({kind for kind,_ in redactor.tokens})
                    findings.append(name+' — '+', '.join(categories))
    except (OSError,zipfile.BadZipFile,zipfile.LargeZipFile):
        return ['unreadable or corrupt ZIP']
    return findings

issues=[]
for p in ROOT.rglob('*'):
    if not p.is_file() or p.relative_to(ROOT).as_posix() in EXCLUDE:
        continue
    if p.suffix.lower()=='.zip':
        for finding in scan_text_only_zip(p):
            issues.append(p.relative_to(ROOT).as_posix()+' — '+finding)
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
print('PASS: no recognizable direct identifiers in scanned public text and text-only ZIPs (not a de-identification guarantee; human review required before student-data use)')
