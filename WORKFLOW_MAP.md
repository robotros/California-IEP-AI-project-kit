# Two-role workflow map — v2.4.0-factory-1.4.1

```text
Official California source / approved local priority policy (nonstudent)
                         |
                         v
        California Essential Standards AI [Light 3 | Full 8]
        - Verify official code, grade, URL, version and date
        - Distinguish LOCAL PROPOSED vs LOCAL APPROVED
        - Build CURRICULUM ONLY or verified crosswalk
                         |
                 Human standards review
                         |
             MANUAL approved handoff packet
                         |
                         v
        California IEP Goal Generator [Light 3 | Full 8]
        - Receive only approved minimum-necessary de-identified context
        - Verify repeatable baseline, scoring, supports, conditions
        - Draft candidate annual goal and progress-monitoring plan
                         |
                    Human QA
                         |
               Qualified IEP team decision
                         |
       Authorized system-of-record entry by approved staff
```

No automatic data movement between workspaces, no implicit Skill state, no sharing of private Project knowledge with account-level Skills. Transfer packet fields: `handoff_id, kit_version, source_role, target_role, request, inputs, source_refs, verified_facts, assumptions, deliverable_links, QA_result, approval_state, open_risks, next_action`. A crosswalk with no learner baseline is curriculum-only. See each specialist's `03_QA_AND_HANDOFFS.md` or Full `04_ROLES_AND_INTERFACES.md`.
