#!/usr/bin/env python3
"""Structural validator for Factory 1.4.1 upgraded specialist kit; stdlib only."""
import json, sys, zipfile
from pathlib import Path
root=Path(__file__).resolve().parent.parent
m=json.loads((root/"setup/project-manifest.json").read_text())
errs=[]
names={"light":["01_CONTEXT.md","02_OPERATIONS_AND_PROMPTS.md","03_QA_AND_HANDOFFS.md"],"full":["01_CHARTER_AND_SCOPE.md","02_REQUIREMENTS.md","03_WORKFLOWS.md","04_ROLES_AND_INTERFACES.md","05_PROMPT_LIBRARY.md","06_TOOLS_AND_DATA.md","07_QA_AND_TESTS.md","08_DEPLOYMENT_AND_CHANGELOG.md"]}
for role,rd in m["roles"].items():
 for ed,entry in rd["editions"].items():
  docs=entry["knowledge_files"]; want=len(names[ed]); inst=root/entry["instructions"]
  if len(docs)!=want:errs.append(f"{role}/{ed} expected {want} references")
  if not inst.exists():errs.append(f"Missing {inst}");continue
  instr=inst.read_text(encoding="utf-8")
  if len(instr)>7500:errs.append(f"Instructions too long: {role}/{ed}")
  for s in ("[[REDACTED:","HUMAN REVIEW REQUIRED","UNVERIFIED","approval"):
   if s.lower() not in instr.lower():errs.append(f"Missing {s} in {role}/{ed} instructions")
  for p in docs:
   f=root/p
   if not f.is_file():errs.append(f"Missing {p}");continue
   txt=root/("adapters/microsoft-365-agent-builder/"+ed+"/"+role+"/"+Path(p).stem+".txt")
   if not txt.is_file() or txt.read_bytes()!=f.read_bytes():errs.append(f"Transport mismatch: {p}")
  zbase=f"distributions/{role}-{ed}"
  for suff,expected in (("root-skill.zip","SKILL.md"),("claude-skill.zip",None)):
   z=root/(zbase+"-"+suff)
   if not z.exists():errs.append(f"Missing {z}");continue
   with zipfile.ZipFile(z) as a:
    bad=a.testzip()
    if bad:errs.append(f"Bad ZIP {z}: {bad}")
    entries=a.namelist()
    if any(q.startswith("/") or ".." in Path(q).parts for q in entries):errs.append(f"Unsafe ZIP {z}")
    if expected and expected not in entries:errs.append(f"Bad ZIP root {z}")
    if not expected and not any(q.endswith("/SKILL.md") for q in entries):errs.append(f"Bad Claude ZIP {z}")
for r in ("README.md","AI_SETUP_PROMPT.md","VALIDATION_REPORT.md","setup/PLATFORM_SUPPORT_MATRIX.md","setup/INSTALL_CHECKLIST.md","docs/index.html"):
 if not (root/r).is_file():errs.append(f"Missing {r}")
# Public-source and license regression gates for post-publication maintenance.
canonical = "https://github.com/robotros/California-IEP-AI-project-kit"
source = m.get("source_resolution", {})
if source.get("default_public_repo") != canonical or source.get("default_branch") != "main":
 errs.append("Public GitHub fallback missing or not main")
if source.get("priority", [])[:2] != ["USER_SUPPLIED_ZIP","USER_SUPPLIED_REPOSITORY_URL"]:
 errs.append("User-supplied source precedence changed")
if source.get("access") != "READ_ONLY_UNTIL_EXPLICIT_APPROVAL":
 errs.append("Default repo source must remain read-only")
for rel in ("AI_SETUP_PROMPT.md","AGENTS.md","AI_SETUP.md","README.md","setup/PLATFORM_INSTALLATION.md"):
 content=(root/rel).read_text(encoding="utf-8")
 if canonical not in content or "ZIP" not in content:
  errs.append(f"Missing public-source fallback disclosure: {rel}")
license_text=(root/"LICENSE").read_text(encoding="utf-8") if (root/"LICENSE").is_file() else ""
for phrase in ("MIT License","Copyright (c) 2026 robotros","Permission is hereby granted","THE SOFTWARE IS PROVIDED"):
 if phrase not in license_text:
  errs.append("Missing or malformed MIT license text: "+phrase)
if "[MIT License](LICENSE)" not in (root/"README.md").read_text(encoding="utf-8"):
 errs.append("README does not link MIT license")
print("FAIL:\n" + "\n".join(errs) if errs else "PASS — Factory v1.4.1 specialist structural checks")
sys.exit(bool(errs))
