# Tools, authoritative sources, freshness and privacy
## Source register, checked in research on 2026-10-26 (not a timeless claim)
- IDEA federal regulations overview and IEP content: https://sites.ed.gov/idea/regs/b/d/300.320 ; development/review: https://sites.ed.gov/idea/regs/b/d/300.324 . Check the applicable current text per issue; also https://www.ecfr.gov/current/title-34/subtitle-B/chapter-III/part-300 .
- California binding Education Code: https://leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?article=3.&chapter=4.&division=4.&lawCode=EDC&part=30.&title=2. ; focus applicable sections such as 56341.1, 56343, 56344, 56345 (not exhaustive). Check current code effective date and amendments.
- State special education portal and new administrative guidance: https://www.cde.ca.gov/sp/se/ and https://www.cde.ca.gov/sp/se/stateadminlst26.asp . CDE portal is an index, not itself proof of an unchanged rule.
- FERPA educational technology privacy FAQ: https://studentprivacy.ed.gov/faq/i-want-use-online-tool-or-application-part-my-course-however-i-am-worried-it-violation-ferpa .
- HQ IEPs educator resources, instructional **not binding**: https://highqualityieps.net/iep-journey/resources-for-educators (provider, general education teacher, administrative designee toolkits). Link to resources; do not copy licensed PDFs/Docs wholesale.
- Existing baseline functionality: https://github.com/robotros/California-IEP-AI-project-kit (source to compare, not an assumed installed dependency).

## Live-check protocol: every substantive IEP task
1. Note date/time and issue scope; identify whether an actual web/search capability is present. If absent, compliance conclusion ON HOLD.
2. Open the relevant authoritative federal provision plus CA law/CCR provision; confirm current effective text, amendment information and CDE update/letter applicable to subject. Search or fetch official pages directly rather than rely on old snippets.
3. Record `authority | exact URL | provision | retrieved date/time | publication/amendment/effective date if verified | applicability | comparison baseline | change status`.
4. Distinguish verified unchanged vs changed vs unable to compare. If the last version/date is unknown, state `CHANGE STATUS UNDETERMINED` (even if current pages loaded).
5. Check user-approved local SELPA/district rules only if authorized and accessible. Missing local rules means NO LOCAL VALIDATION.
6. Cite/label instruction vs statute/regulation. Note uncertainty and handoff to qualified reviewer. Update proposals are drafts, not software installation.

## Temporal legal traps to check, not hardcode
Transition planning, California high-school experience timing and federal age 16 baseline; annual review, initial assessment timelines and statutory exclusions; amendments; alternative assessment and benchmarks; graduation/diploma pathways; updated California IEP template availability. Always verify current rule, pupil-specific facts and local calendar; never auto compute from guesswork.

## Input schema
`role`, `stage`, `meeting_type`, `student_alias`, `grade_span`, `subject`, `strengths`, `family_voice_reported`, `baseline {source,date,skill,metric,sample,conditions,prompts}`, `impact`, `standard {code,official_url,verified_on}`, `local_procedure {owner,date,approved}`, `draft`, `human_approvals`, `guidance_last_checked`.

## Tool authority
No tools assumed. Read-only browse if available; write/export only after authorization and appropriate installed capability. Files in an AI chat/Skill are not live official law updates. No FERPA certification. If data is not institution-approved for this AI platform, stop and use wholly synthetic example instead.

## Curated HQ IEPs educator pages (nonbinding; original external content)
- Special education provider: https://highqualityieps.net/iep-journey/resources-for-educators/resources-for-special-education-providers/before-the-iep ; https://highqualityieps.net/iep-journey/resources-for-educators/resources-for-special-education-providers/during-the-iep ; https://highqualityieps.net/iep-journey/resources-for-educators/resources-for-special-education-providers/after-the-iep . Use for RIOT/evidence, meetings and implementation themes.
- General education teacher: https://highqualityieps.net/iep-journey/resources-for-educators/resources-for-general-education-teachers/before-the-iep ; https://highqualityieps.net/iep-journey/resources-for-educators/resources-for-general-education-teachers/during-the-iep ; https://highqualityieps.net/iep-journey/resources-for-educators/resources-for-general-education-teachers/after-the-iep . Classroom evidence/access input, not service authority.
- Administrative designee: https://highqualityieps.net/iep-journey/resources-for-educators/resources-for-administrative-designees/before-the-iep ; https://highqualityieps.net/iep-journey/resources-for-educators/resources-for-administrative-designees/during-the-iep ; https://highqualityieps.net/iep-journey/resources-for-educators/resources-for-administrative-designees/after-the-iep . Procedural process, meaningful participation and oversight, subject to live current legal check.
- See `docs/EDUCATOR_RESOURCE_MAP.md` in the distribution for a reference catalogue; it is an installer appendix, not a ninth knowledge upload.
