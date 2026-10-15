#!/usr/bin/env python3
"""Static checks for standalone guided form; no third-party packages."""
from pathlib import Path
import re,sys,subprocess,shutil
ROOT=Path(__file__).resolve().parent.parent
p=ROOT/'docs/index.html'
s=p.read_text(encoding='utf8')
errors=[]
for id in ('iep-form','standards-form','tab-iep','tab-standards','mdPreview','fileSelect','oneBtn','zipBtn','copyBtn','ack'):
    if not re.search(r'id="'+re.escape(id)+'"',s): errors.append(f'Missing form control {id}')
for label in ('STUDENT_NAME','DATE_OF_BIRTH','STUDENT_ID','EMAIL_ADDRESS','PII SCREENING INCOMPLETE','HUMAN REVIEW REQUIRED','makeZip','privacyDoc'):
    if label not in s: errors.append(f'Missing privacy/export contract {label}')
for tag in ('<script src=', '<link rel="stylesheet"','fetch(', 'XMLHttpRequest','localStorage','sessionStorage','sendBeacon(', 'indexedDB'):
    if tag in s:errors.append(f'Unexpected external/storage feature: {tag}')
if not re.search("connect-src 'none'",s): errors.append('Missing CSP connect-src none')
if shutil.which('node'):
    js=s.split('<script>')[-1].split('</script>')[0]
    result=subprocess.run(['node','--check','-'],input=js,text=True,capture_output=True)
    if result.returncode:errors.append(f'JavaScript syntax: {result.stderr[:600]}')
if errors:
    for e in errors: print('FAIL',e)
    sys.exit(1)
print('PASS: form controls, privacy contracts, no external dependencies, valid JS syntax')
