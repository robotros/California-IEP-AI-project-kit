# Platform setup and supported fallbacks
**Before any real account changes:** identify target and plan, institution's data classification permission, current instructions/knowledge backup, object name, visibility, available read/write tools and approval. ZIP/package is not installation. Test using fictional examples.

| Destination | Workspace route | Native Skill route | Fallback |
|---|---|---|---|
| ChatGPT personal Free/Go/Plus/Pro | Project instructions + 3 or 8 matching `.md`, subject to actual limits | Do not assume native Skills | Project's built-in QA workflow |
| ChatGPT Business/Enterprise/Healthcare/Edu | Eligible Project + matching references | Native Skills only if workspace UI/admin supports it | Same workflow without native Skill |
| Claude | Project instructions + matching references | `distributions/*-claude-skill.zip` where eligible, user enables separately | Claude Project |
| Gemini | Eligible Gem/project instructions and supported files | `distributions/*-root-skill.zip` only where UI/plan supports import | Gem instructions and source refs |
| Grok | Project/Bot according to actual UI/permission | Portable Skill source when Grok supports it, import shape verified in UI | Project/Bot guidance or chat |
| Microsoft 365 Copilot Agent Builder | Instructions + **3/8 faithful `.txt`** transport knowledge copies | Frontier preview-only when eligible; `root-skill` package | Plain instruction/knowledge workflow |
| Microsoft Copilot Studio | Verified standard or GitHub Copilot harness with approved environment, tools and knowledge | Native Skills only in compatible GitHub Copilot harness; `root-skill` | Standard agent topics/instructions/knowledge |

Platform limits/features change. Confirm official current documentation and actual signed-in UI. No connectors, automation, publishing or private-record access is conferred by an instruction. For all platforms, human must approve program decisions and legal conclusions. Keep assistant private until district clearance; do not upload identifiable education records to unapproved tools.

## Light / Full instructions and knowledge
Use `specialists/light/iep-educator/PROJECT_INSTRUCTIONS.txt` + precisely three `.md` files in same directory OR `specialists/full/iep-educator/PROJECT_INSTRUCTIONS.txt` + precisely eight `.md`. The files under `skills/`, `docs/`, `templates/`, `setup/` are NOT extra persistent Project knowledge files. Do not install both Light and Full in the same object. If migrating, back up then replace whole set and retest. User confirms saved configuration in GUI or an authenticated tool verifies readback.

## Minimal acceptance test
In a fresh chat, ask: `I teach grade 5 and need an annual goal for a fictional student, but I have no measured baseline. Please check current federal and California guidance, create a provisional outline, and tell me what remains missing.` Correct behavior: no invented baseline/criterion, official sources checked where tools exist or explicit legal ON HOLD, humans required to review. Record operational evidence separately.
