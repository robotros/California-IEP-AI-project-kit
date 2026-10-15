#!/usr/bin/env python3
"""Static checks for the required form-first onboarding contract."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parent.parent
m=json.loads((ROOT/'setup/project-manifest.json').read_text())
form=m['intake_form']
assert form.get('setup_handoff_required') is True
assert form.get('require_real_case_during_setup') is False
for name, filename, project in [
('iep-goal-generator', 'IEP_GOAL_AI_READY_INTAKE.md','California IEP Goal Generator 2.0'),
('essential-standards','ESSENTIAL_STANDARDS_AI_READY_INTAKE.md','California Essential Standards AI')]:
    item=form['request_on_first_task'][name]
    assert item['output']==filename and item['target_project']==project
    instructions=(ROOT/f'projects/{name}/PROJECT_INSTRUCTIONS.md').read_text()
    assert filename in instructions and 'skip the form' in instructions.lower()
    assert 'privacy' in instructions.lower()
    assert filename in (ROOT/'AI_SETUP.md').read_text()
setup=(ROOT/'AI_SETUP.md').read_text()
assert 'First-use educator form handoff' in setup
assert 'After fictional setup tests' in setup
assert 'Do not ask again for material already present' in setup
assert 'not permanent' in setup.lower() or 'never add' in setup.lower()
for f in ['README.md','AGENTS.md','docs/FORM_GUIDE.md','docs/WORKFLOW.md']:
    data=(ROOT/f).read_text()
    assert 'form' in data.lower() and 'intake' in data.lower(), f
page=(ROOT/'docs/index.html').read_text()
assert 'Return to your matching AI project' in page
print('PASS: guided form handoff, intake destinations, and privacy/fallback rules')
