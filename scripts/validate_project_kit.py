#!/usr/bin/env python3
"""Validate repository edition manifests and Markdown links. No external packages required."""
from pathlib import Path
import json, re, hashlib, os, sys
ROOT = Path(__file__).resolve().parent.parent
m = json.loads((ROOT / "setup/project-manifest.json").read_text(encoding="utf-8"))
errors = []
for project in m["projects"]:
    inst=ROOT / project["instructions"]
    if not inst.is_file(): errors.append(f"Missing project instructions: {inst}")
    for edition in ("lightweight","full"):
        paths=project["editions"][edition]["knowledge_files"]
        expected=2 if edition=="lightweight" else 5
        if len(paths)!=expected: errors.append(f"{project['id']}/{edition}: expected {expected} files, found {len(paths)}")
        if len(paths)!=len(set(paths)): errors.append(f"{project['id']}/{edition}: duplicate file paths")
        for path in paths:
            if not (ROOT/path).is_file(): errors.append(f"Missing knowledge file: {path}")
insts=[(ROOT/p["instructions"]).read_bytes() for p in m["projects"] if (ROOT/p["instructions"]).exists()]
if len(insts)==2 and hashlib.sha256(insts[0]).digest()==hashlib.sha256(insts[1]).digest():
    errors.append("Critical: both projects have identical instructions")
if len(insts)==2:
    for p in m["projects"]:
        data=(ROOT/p["instructions"]).read_text(encoding="utf-8")
        label="Essential Standards AI" if p["id"]=="essential-standards" else "IEP Goal Generator"
        if label.lower() not in data.lower():errors.append(f"Wrong project role: {p['id']}")
for file in ROOT.rglob("*.md"):
    text=file.read_text(encoding="utf-8")
    prose=re.sub(r"```[\s\S]*?```", "", text)
    for dest in re.findall(r"(?<!!)\]\(([^)]+)\)",prose):
        dest=dest.split("#")[0].split("?")[0]
        if not dest or "://" in dest or dest.startswith("mailto:"):continue
        path=(file.parent/dest).resolve()
        if not path.exists():errors.append(f"Broken Markdown link: {file.relative_to(ROOT)} -> {dest}")
    if re.search(r"`(?:03_STUDENT_PROFILE_INTAKE_TEMPLATE|04_PRESENT_LEVELS_BASELINE_TEMPLATE|07_ESSENTIAL_STANDARDS_REVIEW|08_STANDARDS_GOAL_CROSSWALK)\.md`",text):
        errors.append(f"Stale template filename: {file.relative_to(ROOT)}")
# Ensure the privacy rules are present in both instruction sets and every edition upload.
if not m.get('pii_redaction',{}).get('requires_human_review'):
    errors.append('PII privacy gate missing in manifest')
for project in m['projects']:
    candidates=[project['instructions']]
    for edition in ('lightweight','full'):
        candidates.extend(project['editions'][edition]['knowledge_files'])
    for rel in candidates:
        content=(ROOT/rel).read_text(encoding='utf8') if (ROOT/rel).exists() else ''
        if '[[REDACTED:' not in content or 'HUMAN REVIEW REQUIRED' not in content:
            errors.append(f'Missing typed redaction contract: {rel}')
if not (ROOT/'scripts/pii_redact.py').is_file() or not (ROOT/'docs/PRIVACY_AND_REDACTION.md').is_file():
    errors.append('Missing privacy scanner or documentation')
limit = m.get('file_limits', {}).get('chatgpt_project_instructions_character_limit')
if limit != 8000:
    errors.append('ChatGPT instruction character limit must stay 8000')
for project in m['projects']:
    summary_rel = project.get('instruction_summary')
    recorded = project.get('instruction_summary_character_count')
    if not summary_rel:
        errors.append(f"Missing instruction summary path: {project['id']}")
        continue
    summary_path = ROOT / summary_rel
    if not summary_path.is_file():
        errors.append(f'Missing instruction summary file: {summary_rel}')
        continue
    summary = summary_path.read_text(encoding='utf-8')
    count = len(summary)
    if count != recorded:
        errors.append(f'Summary character count mismatch for {summary_rel}: file {count}, manifest {recorded}')
    if count >= 8000:
        errors.append(f'Summary is not under 8000 characters: {summary_rel} has {count}')
    for gate in ('[[REDACTED:', 'HUMAN REVIEW REQUIRED', 'pii_redact.py'):
        if gate not in summary:
            errors.append(f'Summary missing required gate {gate}: {summary_rel}')
    if '2.0' in summary:
        errors.append(f'Summary still contains a 2.0 marker: {summary_rel}')
setup_text = (ROOT/'AI_SETUP.md').read_text(encoding='utf-8')
agents_text = (ROOT/'AGENTS.md').read_text(encoding='utf-8')
for phrase in ('Step 2b', 'do **not** stop', 'Do not claim a project was created', 'INSTRUCTIONS_SUMMARY.md'):
    if phrase not in setup_text:
        errors.append(f'AI_SETUP.md missing manual-walkthrough phrase: {phrase}')
if 'Grok' not in setup_text or 'Grok' not in agents_text:
    errors.append('Setup docs must name Grok so a capability refusal does not end the walkthrough')
# Browser-based guided intake form should be present and discoverable.
form=m.get('intake_form',{})
for key in ('entrypoint','guide'):
    if not (ROOT/form.get(key,'__missing__')).is_file(): errors.append(f'Missing browser form asset: {key}')
if not m.get('intake_form',{}).get('setup_handoff_required'):
    errors.append('Form handoff must be introduced after setup')
for project_id, filename in [('iep-goal-generator','IEP_GOAL_AI_READY_INTAKE.md'), ('essential-standards','ESSENTIAL_STANDARDS_AI_READY_INTAKE.md')]:
    instr=(ROOT/f'projects/{project_id}/PROJECT_INSTRUCTIONS.md').read_text(encoding='utf-8')
    if filename not in instr or filename not in (ROOT/'AI_SETUP.md').read_text(encoding='utf-8'):
        errors.append(f'Missing form output handoff for {project_id}')
if errors:
    for err in errors:print("FAIL:",err)
    print(f"FAILED: {len(errors)} issue(s)")
    sys.exit(1)
print("PASS: distinct instructions, correct manifest paths, exact edition counts, and Markdown links")

