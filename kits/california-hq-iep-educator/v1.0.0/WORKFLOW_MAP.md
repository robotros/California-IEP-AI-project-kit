# Workflow and approval map (one specialist, professional modes)

```mermaid
flowchart TD
A[Educator stage and approved deidentified inputs] --> B{Privacy and authority gate}
B -->|Unsafe| X[Stop and escalate to district privacy officer]
B -->|Safe| C{Live federal and California source check}
C -->|Unavailable or ambiguous| H[Compliance findings ON HOLD]
C -->|Verified for task| D[Assessment evidence and strengths]
H --> D
D --> E[Present levels with dated baseline]
E --> F[Identified need and curriculum impact]
F --> G[Verified standard or functional access rationale]
G --> I[Proposed measurable goal and monitoring]
I --> J[Proposed supports and services for team discussion]
J --> K[Five-component audit and open risks]
K --> L[Human professional and IEP team review]
L --> M[Authorized LEA record entry outside AI]
C --> N{Official change discovered}
N --> O[Draft delta and effective date]
O --> P[Owner and qualified reviewer approval]
P --> Q[Update both editions and adapters then test]
```

**Note:** `ON HOLD` legal findings cannot turn into compliance assurance merely because an instructional draft is useful. External transmissions, recording, changes to project instructions, cross-project handoffs and publishing require distinct approved actions. No diagram arrow implies an integration is configured.