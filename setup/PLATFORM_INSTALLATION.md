# Project/agent and Skill installation guide

Read the [all-platform Projects and Skills capability matrix](PLATFORM_SUPPORT_MATRIX.md) **first**, before recommending an edition or assuming access.

1. Record target app/product experience, plan/tenant/harness, project upload capacity, tool/read/write permissions, student data classification, human approver, and whether native Skills appear in actual UI. Unknown is NEEDS_VERIFICATION.
2. Obtain explicit permission before mutation; back up previous instructions, knowledge names and versions.
3. Install separate `specialists/<edition>/<role>/PROJECT_INSTRUCTIONS.txt` into the agent/project Instructions field. Upload only matching 3 or 8 canonical .md files. Never upload old long `PROJECT_INSTRUCTIONS.md` as an extra knowledge file.
4. For Microsoft 365 Agent Builder only, upload 3/8 faithful .txt transport copies from `adapters/microsoft-365-agent-builder/<edition>/<role>/` as knowledge, not ordinary .md. Studio depends on actual environment and harness.
5. Independently evaluate optional Skill eligibility; when supported select only the Skill-only ZIP under `distributions/` (Claude folder-wrapped, otherwise root-SKILL where documented), NOT the outer kit. Confirm UI installation/enabled state and triggers.
6. Run fresh-context fictional role/PII/source/permission/handoff cases, capture evidence and approval. A GitHub commit or ZIP is not an installed Project or Skill.

**ChatGPT:** Projects plus selected 3/8; personal Free/Go/Plus/Pro use portable workflow fallback rather than native ChatGPT Skill. Enterprise-capable skill UI eligibility must be checked. **Claude:** Project with refs, optional wrapped Skill in Customize > Skills when enabled. **Gemini:** Gem or eligible personal-account Skill with root-SKILL package; rollout and Keep Activity rules matter. **Grok:** verify Projects/Bots/Skills in account; use conversational fallback if no verified import. **Microsoft 365 Agent Builder:** declarative agent + .txt knowledge, Frontier preview only for native Skills. **Copilot Studio:** distinguish standard harness from GitHub Copilot harness; native Skill import is not universal, DLP/identity/licensing required.

If no authenticated create/edit UI is accessible, guide the user one manual step at a time without falsely claiming deployment. Student-specific material requires prior institution authorization; testing uses synthetic data only.
