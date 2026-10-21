# Default platform capability report — Projects AND Skills

**Required first output of AI_SETUP_PROMPT.md.** This table describes documented general features as of 2026-10-20; **no entry confirms eligibility, installation, source indexing or successful execution in a specific account**. Before any setup, show this matrix (or a concise version listing every destination), then identify the selected user platform, plan/tenant, product surface, whether direct write tools actually exist, approval owner, data category and cost. Values must be changed from `DOCUMENTED / ACCOUNT NEEDS_VERIFICATION` only on real evidence.

| AI destination | Persistent workspace / Project / Agent | Native Skill support | Fallback when unavailable | Required verification |
|---|---|---|---|---|
| ChatGPT Projects | YES — persistent Project | Eligible Business/Enterprise/Healthcare/Edu only; personal accounts: no native Skills per current help | Use Project with 3/8 refs + workflow inside refs; standalone Skill portable | Verify account workspace, attachment capacity, Skills toggle; fresh chat |
| Claude Projects | YES — Projects | YES where Customize > Skills enabled/allowed; name-wrapped ZIP | Project or standalone portable procedure | Verify plan, code/file settings and actual upload/enablement |
| Gemini Apps | Gem / conversational persistent configuration; not identical to Projects | Skills on eligible personal accounts; rollout/Keep Activity conditions; work/school may lack | Gem or chat with full reference content | Verify current Gems vs Skills UI, geography, account type and plan |
| Grok | Project / Bot options depend on current product surface | Skill support may exist but import/trigger needs account verification | Grok Project/Bot instructions or portable Skill conversational procedure | Verify actual Grok Project/Bot/Skill tools and separate credentials |
| Microsoft 365 Copilot Agent Builder | YES — declarative agent, not ChatGPT/Claude Project | Custom Skills **Frontier preview** eligible tenant only; ZIP root SKILL.md | Agent with 3/8 faithful .txt embedded knowledge files | Verify M365 license, tenant, embedded file policy, private/share state |
| Microsoft Copilot Studio | YES — maker-created agent, environment/harness dependent | Native SKILL.md import in **GitHub Copilot harness** only; standard harness uses tools/topics | Standard-harness agent with native 3/8 .md knowledge when accepted | Verify environment, maker rights, harness, data loss prevention, billing and publish rights |

## Source references for documenting capability, not account status
- OpenAI ChatGPT Skills: https://help.openai.com/en/articles/20001066-skills-in-chatgpt
- OpenAI ChatGPT Projects: https://help.openai.com/en/articles/10169521-using-projects-in-chatgpt
- Anthropic Claude Skills: https://support.claude.com/en/articles/12512180-use-skills-in-claude
- Google Gemini Skills: https://support.google.com/gemini/answer/17094296
- Google Gemini Gems: https://support.google.com/gemini/answer/15146780
- M365 Agent Builder embedded knowledge: https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-add-knowledge
- M365 Agent Builder Skills preview: https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-add-skills
- Copilot Studio file knowledge: https://learn.microsoft.com/en-us/microsoft-copilot-studio/knowledge-add-file-upload
- Copilot Studio Skills, GitHub Copilot harness: https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/skills-add-existing
- Grok: verify the currently available project/skill/bot product experience in the user's own UI; **do not claim unverified ZIP support**.

## Capability report fields (complete before any mutation)
`platform | product_surface | account_plan_or_tenant | workspace_or_agent_supported | native_skill_supported | actual_UI_or_tool_seen | scope_and_permissions | source_data_classification | installation_method | backup_status | skill_package_layout | feature_costs | verified_status | tests_pending`.

Status vocabulary: `DOCUMENTED`, `NEEDS_VERIFICATION`, `GENERATED_ONLY`, `USER_CONFIRMED`, `TOOL_VERIFIED`, `OPERATIONALLY_TESTED`, `UNAVAILABLE`, `NOT_APPLICABLE`. **Documented does not mean account verified.** Do not reduce project upload-count contracts because an account has fewer slots: instead use a portable chat fallback explicitly not claimed as a project installation.
