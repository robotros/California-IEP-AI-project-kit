#!/usr/bin/env python3
"""Conservative offline PII screening + typed redaction for school AI workflows.

NOT a complete FERPA/California legal de-identification determination. Never upload
original student files to an unapproved model or public Git repository.
"""
from __future__ import annotations

import argparse
import csv
import io
import ipaddress
import json
import re
import sys
from collections import Counter
from pathlib import Path

TEXT_SUFFIXES = {'.md', '.txt', '.csv', '.tsv', '.json', '.yaml', '.yml'}
EXTRACT_SUFFIXES = {'.pdf', '.docx'}
ALLOWED_SUFFIXES = TEXT_SUFFIXES | EXTRACT_SUFFIXES

# Use narrowly targeted patterns so the report never becomes a stream of
# invented PII findings (especially annual IEP goal dates/grade-level codes).
PATTERNS = [
    ('EMAIL_ADDRESS', r'\b[A-Z0-9._%+\-]+@[A-Z0-9.\-]+\.[A-Z]{2,}\b', re.I),
    ('SSN', r'(?<!\w)\d{3}-\d{2}-\d{4}(?!\w)', 0),
    ('SSN', r'(?im)\b(?:SSN|social\s+security\s+(?:number|#))\s*[:=#]\s*(?P<value>\d{9})\b', 0),
    ('PHONE_NUMBER', r'(?<!\w)(?:\+1[\s.\-]?)?\(?[2-9]\d{2}\)?[\s.\-]?[2-9]\d{2}[\s.\-]?\d{4}(?!\w)', 0),
    ('IP_ADDRESS', r'(?<![A-Fa-f0-9:.])(?:\d{1,3}\.){3}\d{1,3}(?!\d)', 0),
    ('STUDENT_NAME', r'(?im)^\s*(?:student(?:\s+(?:full\s+)?name)?|pupil\s+name|learner\s+name)\s*[:=]\s*(?P<value>[A-ZÀ-ÖØ-Þ][\w\'’\-.]*(?:\s+[A-ZÀ-ÖØ-Þ][\w\'’\-.]*){0,4})(?=\s*(?:$|[,;|]))', 0),
    ('FAMILY_NAME', r'(?im)^\s*(?:parent|guardian|mother|father|family\s+member)(?:\s+(?:full\s+)?name)?\s*[:=]\s*(?P<value>[A-ZÀ-ÖØ-Þ][\w\'’\-.]*(?:\s+[A-ZÀ-ÖØ-Þ][\w\'’\-.]*){0,4})(?=\s*(?:$|[,;|]))', 0),
    ('STAFF_NAME', r'(?im)^\s*(?:teacher|case\s+manager|service\s+provider|staff)(?:\s+(?:full\s+)?name)?\s*[:=]\s*(?P<value>[A-ZÀ-ÖØ-Þ][\w\'’\-.]*(?:\s+[A-ZÀ-ÖØ-Þ][\w\'’\-.]*){0,4})(?=\s*(?:$|[,;|]))', 0),
    ('DATE_OF_BIRTH', r'(?im)\b(?:DOB|date\s+of\s+birth|birthdate|birth\s+date)\s*[:=]\s*(?P<value>\d{1,2}[/\-]\d{1,2}[/\-]\d{2,4}|\d{4}-\d{2}-\d{2}|[A-Z][a-z]+\s+\d{1,2},?\s+\d{4})', 0),
    ('STUDENT_ID', r'(?im)\b(?:(?:student|pupil|statewide\s+student|local\s+student)\s*(?:ID|number|#)|SSID)\b\s*(?::|=|#|-(?=\s*\d)|(?=\d))\s*(?P<value>[A-Z0-9][A-Z0-9\-]{4,19})\b', 0),
    ('GOVERNMENT_ID', r'(?im)\b(?:driver.?s\s+licen[sc]e|passport|state\s+ID|medi.cal\s+ID|medical\s+record\s+number|MRN)\s*(?:number|no\.?|#)?\s*[:=#]\s*(?P<value>[A-Z0-9\-]{5,22})\b', 0),
    ('STREET_ADDRESS', r'(?im)^\s*(?:home|street|mailing|residential|family|student)\s+address\s*[:=]\s*(?P<value>[^\r\n|]{6,130})', 0),
    ('STREET_ADDRESS', r"(?im)\b\d{1,5}\s+(?:[NSEW]\.?(?:\s+)?|North\s+|South\s+|East\s+|West\s+)?(?:[A-Za-z0-9'.\-]+\s+){1,5}(?:St(?:reet)?|Ave(?:nue)?|Rd|Road|Blvd|Boulevard|Dr(?:ive)?|Ln|Lane|Way|Ct|Court|Pl|Place)\b\.?", 0),
    ('PLACE_OF_BIRTH', r'(?im)\b(?:place|city|country)\s+of\s+birth\s*[:=]\s*(?P<value>[^\r\n,;|]{2,65})', 0),
    ('MOTHERS_MAIDEN_NAME', r'(?im)\bmother.?s\s+maiden\s+name\s*[:=]\s*(?P<value>[^\r\n,;|]{2,65})', 0),
    ('GEOLOCATION', r'(?im)\b(?:GPS|coordinates|latitude\s*/\s*longitude|precise\s+location)\s*[:=]\s*(?P<value>-?\d{1,3}\.\d{4,}\s*[,/]\s*-?\d{1,3}\.\d{4,})', 0),
    ('CREDENTIAL', r'(?im)\b(?:password|api[_ -]?key|access[_ -]?token|secret)\s*[:=]\s*(?P<value>[^\r\n,;|\s]{5,120})', 0),
]
COMPILED = [(kind, re.compile(regex, flags)) for kind, regex, flags in PATTERNS]

FIELD_CATEGORIES = [
    (re.compile(r'(?:^|_)(?:student|pupil|learner)(?:_full)?_?name$'), 'STUDENT_NAME'),
    (re.compile(r'(?:^|_)(?:parent|mother|father|guardian|family)(?:_full)?_?name$'), 'FAMILY_NAME'),
    (re.compile(r'(?:^|_)(?:teacher|case_manager|provider|staff)(?:_full)?_?name$'), 'STAFF_NAME'),
    (re.compile(r'^(?:name|full_name)$'), 'PERSON_NAME'),
    (re.compile(r'(?:^|_)(?:dob|date_of_birth|birthdate|birth_date)$'), 'DATE_OF_BIRTH'),
    (re.compile(r'(?:student|pupil|ssid|statewide_student).*(?:id|number)|^(?:ssid|studentid)$'), 'STUDENT_ID'),
    (re.compile(r'(?:address|street_address|residential_address)$'), 'STREET_ADDRESS'),
    (re.compile(r'(?:phone|telephone|mobile|cell)$'), 'PHONE_NUMBER'),
    (re.compile(r'(?:email|e_mail)$'), 'EMAIL_ADDRESS'),
    (re.compile(r'(?:ssn|social_security_number)$'), 'SSN'),
    (re.compile(r'(?:passport|drivers_license|license_number|medical_record_number)$'), 'GOVERNMENT_ID'),
    (re.compile(r'(?:password|api_key|secret|access_token)$'), 'CREDENTIAL'),
    (re.compile(r'(?:birth_place|place_of_birth|birth_city)$'), 'PLACE_OF_BIRTH'),
    (re.compile(r'(?:maiden_name)$'), 'MOTHERS_MAIDEN_NAME'),
    (re.compile(r'(?:latitude_longitude|gps|coordinates)$'), 'GEOLOCATION'),
    (re.compile(r'(?:ip_address)$'), 'IP_ADDRESS'),
]


def type_for_field(field: str) -> str | None:
    key = re.sub(r'[^a-z0-9]+', '_', field.strip().lower()).strip('_')
    for rx, category in FIELD_CATEGORIES:
        if rx.search(key):
            return category
    return None


class Redactor:
    def __init__(self, extra_names: list[str] | None = None):
        self.tokens: dict[tuple[str, str], str] = {}
        self.counts: Counter[str] = Counter()
        self.extra_names = []
        for name in extra_names or []:
            if name.strip() and len(name.strip()) >= 3:
                self.extra_names.append(re.compile(r'(?<!\w)' + re.escape(name.strip()) + r'(?!\w)', re.I))

    def token(self, kind: str, original: str) -> str:
        key = (kind, original.casefold().strip())
        if key not in self.tokens:
            self.counts[kind] += 1
            self.tokens[key] = f'[[REDACTED: {kind} #{self.counts[kind]:03d}]]'
        return self.tokens[key]

    def direct(self, category: str, value: object) -> object:
        if value is None or (isinstance(value, str) and not value.strip()):
            return value
        if isinstance(value, (dict, list)):
            return self.recursive(value)
        return self.token(category, str(value))

    def recursive(self, value: object) -> object:
        if isinstance(value, dict):
            return {k: self.direct(cat, v) if (cat := type_for_field(k)) else self.recursive(v)
                    for k, v in value.items()}
        if isinstance(value, list):
            return [self.recursive(v) for v in value]
        if isinstance(value, str):
            return self.text(value)
        return value

    def text(self, data: str) -> str:
        matches = []
        for kind, rx in COMPILED:
            for m in rx.finditer(data):
                if kind == 'IP_ADDRESS':
                    try:
                        ipaddress.ip_address(m.group(0))
                    except ValueError:
                        continue
                a,b = m.span('value') if 'value' in rx.groupindex else m.span()
                if b>a and not data[a:b].startswith('[[REDACTED:'):
                    matches.append((a,b,kind))
        for rx in self.extra_names:
            matches.extend((m.start(),m.end(),'PERSON_NAME') for m in rx.finditer(data))
        # Prefer the longest overlapping match; then keep replacements ordered.
        chosen=[]
        for a,b,k in sorted(matches,key=lambda x:(x[0],0 if x[2] in {'STUDENT_ID','SSN','DATE_OF_BIRTH','GOVERNMENT_ID','CREDENTIAL'} else 1,-(x[1]-x[0]))):
            if not any(a<x[1] and b>x[0] for x in chosen):
                chosen.append((a,b,k))
        for a,b,k in sorted(chosen, key=lambda x:x[0],reverse=True):
            data=data[:a]+self.token(k,data[a:b])+data[b:]
        return data

    def sanitized(self, text: str, suffix: str) -> str:
        if suffix == '.json':
            return json.dumps(self.recursive(json.loads(text)),ensure_ascii=False,indent=2)+'\n'
        if suffix in ('.csv','.tsv'):
            dialect='excel-tab' if suffix=='.tsv' else 'excel'
            reader=csv.reader(io.StringIO(text),dialect=dialect)
            rows=list(reader)
            if not rows:return text
            categories=[type_for_field(k) for k in rows[0]]
            output=io.StringIO()
            writer=csv.writer(output,dialect=dialect,lineterminator='\n')
            writer.writerow(rows[0])
            for row in rows[1:]:
                writer.writerow([self.direct(categories[i],v) if i<len(categories) and categories[i] else self.text(v)
                                 for i,v in enumerate(row)])
            return output.getvalue()
        return self.text(text)


def extract_source(path: Path) -> tuple[str,str,list[str]]:
    warnings=[]
    if path.suffix.lower() in TEXT_SUFFIXES:
        return path.read_text(encoding='utf-8-sig'),path.suffix.lower(),warnings
    if path.suffix.lower()=='.docx':
        try:
            from docx import Document
        except ImportError as exc:
            raise ValueError('DOCX requires python-docx; install only in an approved local environment') from exc
        doc=Document(str(path))
        segments=[p.text for p in doc.paragraphs]
        for table in doc.tables:
            for row in table.rows:
                segments.append(' | '.join(cell.text for cell in row.cells))
        for section in doc.sections:
            segments.extend(p.text for p in section.header.paragraphs)
            segments.extend(p.text for p in section.footer.paragraphs)
        warnings.append('DOCX drawings, embedded images, tracked changes, comments, properties, and other parts may not be extracted; manually review the ORIGINAL. Only redacted text is exported.')
        return '\n'.join(segments),'.txt',warnings
    if path.suffix.lower()=='.pdf':
        try:
            import fitz
        except ImportError as exc:
            raise ValueError('PDF requires PyMuPDF; install only in an approved local environment') from exc
        pdf=fitz.open(str(path))
        pages=[p.get_text('text') for p in pdf]
        if not any(t.strip() for t in pages):
            raise ValueError('Scanned/image-only PDF: cannot safely inspect; OCR locally in approved environment and manually validate before use')
        warnings.append('PDF image/text overlays, embedded objects, metadata, handwriting, and scanned portions may be missed. This is NOT a true-redacted PDF; only extracted redacted text is exported.')
        if any(not t.strip() for t in pages):
            raise ValueError('PDF includes at least one image-only/unextractable page; blocked pending local OCR and review')
        return '\n\n'.join(pages),'.txt',warnings
    raise ValueError('Unsupported format; only '+', '.join(sorted(ALLOWED_SUFFIXES)))


def main(argv=None):
    cli=argparse.ArgumentParser(description='Offline IEP PII redaction; all outputs require manual privacy review.')
    cli.add_argument('source', type=Path,help='Local file or directory to inspect (never a web URL)')
    cli.add_argument('--out-dir', type=Path,required=True,help='Private output folder, NOT inside public repository')
    cli.add_argument('--names-file', type=Path,help='Optional local list of known names; one per line; NEVER committed or uploaded')
    cli.add_argument('--strict',action='store_true', help='Exit 2 when PII is detected (redacted files still written)')
    args=cli.parse_args(argv)
    out=args.out_dir.resolve()
    if args.source.is_dir():
        paths=sorted(p for p in args.source.rglob('*') if p.is_file() and p.suffix.lower() in ALLOWED_SUFFIXES)
    else:
        paths=[args.source]
    if not paths:cli.error('No supported input files found')
    if args.source.resolve().is_dir() and (out==args.source.resolve() or args.source.resolve() in out.parents):
        cli.error('--out-dir must be OUTSIDE the input directory to prevent reprocessing output')
    repo_root=Path(__file__).resolve().parent.parent
    if out==repo_root or repo_root in out.parents:
        cli.error('--out-dir may not be inside the project repository (risk of committing sensitive output)')
    out.mkdir(parents=True,exist_ok=True)
    names=[] if not args.names_file else [x.strip() for x in args.names_file.read_text(encoding='utf-8').splitlines() if x.strip() and not x.lstrip().startswith('#')]
    redactor=Redactor(extra_names=names)
    report={'status':'HOLD_FOR_HUMAN_REVIEW','requires_manual_review':True,'automatic_deidentification_certified':False,'files':[], 'limitations':['Rules can miss unlabeled names, images/handwriting, indirect and combined identifiers, and hidden metadata.','Never send originals to unapproved AI services; replacing placeholders only inside authorized system of record.']}
    any_found=False
    for i, path in enumerate(paths,1):
        entry={'file_id':f'FILE_{i:03d}','detected_categories':{},'status':'REVIEW_REQUIRED','warnings':[]}
        before=Counter(redactor.counts)
        try:
            data,suffix,warnings=extract_source(path)
            sanitized=redactor.sanitized(data,suffix)
            entry['warnings'].extend(warnings)
            entry['redacted_filename']=f'redacted_{i:03d}.txt'
            payload=(
                'PII SCREENING NOTICE: [[PII_REVIEW_REQUIRED]] — automated redaction is incomplete and human review is required.\n'
                'RECORD-ENTRY FLAG: Replace all [[REDACTED: TYPE #NNN]] markers only in the authorized system of record.\n'
                'Do not reconstruct names/identifiers in the AI chat.\n\n'+sanitized
            )
            (out/entry['redacted_filename']).write_text(payload,encoding='utf-8')
            for kind in set(re.findall(r'\[\[REDACTED: ([A-Z_]+) #\d+\]\]', sanitized)):
                entry['detected_categories'][kind] = len(set(re.findall(r'\[\[REDACTED: '+kind+r' #\d+\]\]', sanitized)))
            any_found |=bool(entry['detected_categories'])
        except Exception as exc:
            # Error messages must never include original file names or content.
            entry['status']='BLOCKED_UNINSPECTED'
            entry['warnings'].append('Extraction failed, unsupported, or uninspectable content (including image-only documents); do not share without manual review')
        report['files'].append(entry)
    report['replacement_tokens']=[{'token':t,'category':kind} for (kind,_),t in redactor.tokens.items()]
    report['redaction_count']=len(redactor.tokens)
    (out/'pii_review_report.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(f'Privacy screening: {len(paths)} file(s), {len(redactor.tokens)} unique redaction marker(s). ALL OUTPUTS REQUIRE HUMAN REVIEW.')
    print('Sanitized files and category-only review report are in the PRIVATE output directory. No original values are in the report.')
    if any(x['status']=='BLOCKED_UNINSPECTED' for x in report['files']):return 3
    return 2 if args.strict and any_found else 0

if __name__=='__main__':sys.exit(main())
