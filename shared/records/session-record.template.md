# CodeBTI Session Record

Date:
TODO

Project slug:
TODO

Language targets:
TODO

Interview status:
TODO

Current step:
TODO

Next question:
TODO

## Project Summary

TODO

Source: required SPEC-style opening prompt.

## Opening SPEC Intake

Mission:
TODO

Goals:
TODO

Target audience:
TODO

Constraints:
TODO

Likely tech stack or language targets:
TODO

Roadmap intent:
TODO

Non-goals:
TODO

Open questions:
TODO

Initial SPEC draft:
TODO: path to `SPEC.md`, or explain why no draft was generated.

## Interview Rounds

Record the planned and completed rounds.

| Round | Scope | Source | Status |
| --- | --- | --- | --- |
| Opening | Project | Required SPEC-style opening prompt | TODO |
| Project fixed questions | Project | `project/questions/fixed-project.md` | TODO |
| Language fixed questions | Language:TODO | `TODO/questions/fixed-TODO.md` | TODO |
| Adaptive questions | Project, Language, or Cross-language | Generated from `shared/questions/adaptive-question-guide.md` | TODO |

## Question Card Snapshots

Save the full user-facing question before asking it. Fixed questions should include a source path; adaptive questions should store the generated question text directly. There must be one snapshot block for the opening prompt, all fixed project questions, all fixed language questions, and all 5 adaptive questions.

Use this block shape for each scored question:

```text
### QN. Question Title

Question kind:
Project fixed, Language fixed, or Adaptive

Question ID:
Stable identifier if available

Scope:
Project, Language:<name>, or Cross-language

Source:
Local source path for fixed questions, or "Generated adaptive question"

Dimension:
Primary dimension being tested

User-facing scenario:
Full scenario shown to the user

User-facing instruction:
Full instruction shown to the user

Code example:
Full code example shown to the user, or "None"

Choices:
- A. Full choice text
- B. Full choice text
- C. Full choice text if present
- D. Full choice text if present
- E. Full choice text if present
```

### Opening. Project Summary and SPEC Intake

Question kind:
Opening

Scope:
Project

Source:
Required SPEC-style opening prompt

Full question:
Please describe the project as a compact SPEC-style brief. Include mission, goals, target audience, constraints, likely tech stack or language targets, roadmap intent, non-goals, and open questions. Keep this at the what/why level; avoid low-level implementation details unless they are hard constraints.

Required scored snapshot blocks:

- P1-P6. Project fixed questions
- Language fixed questions for each selected language pack
- A1-A5. Adaptive questions

## Answer Log

Update this table after every answer before asking the next question. Keep notes concise; do not paste private or unrelated user details. The full question text belongs in `Question Card Snapshots`.

| Step | Question kind | Scope | Question focus | User answer | User note | Feedback given | Hidden inference note | Changed from | Recorded at |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Opening | Project summary and SPEC intake | Project | Mission, goals, audience, constraints, stack, roadmap, non-goals, open questions | TODO | TODO | TODO | Not scored | None | TODO |
| P1 | Project fixed | Project | Project control model | TODO | TODO | TODO | TODO | None | TODO |
| P2 | Project fixed | Project | Output shape | TODO | TODO | TODO | TODO | None | TODO |
| P3 | Project fixed | Project | Validation gate | TODO | TODO | TODO | TODO | None | TODO |
| P4 | Project fixed | Project | Shared versus language-specific rules | TODO | TODO | TODO | TODO | None | TODO |
| P5 | Project fixed | Project | Dependency governance | TODO | TODO | TODO | TODO | None | TODO |
| P6 | Project fixed | Project | Change record policy | TODO | TODO | TODO | TODO | None | TODO |
| Language:TODO Q1 | Language fixed | Language:TODO | TODO | TODO | TODO | TODO | TODO | None | TODO |
| Language:TODO Q2 | Language fixed | Language:TODO | TODO | TODO | TODO | TODO | TODO | None | TODO |
| Language:TODO Q3 | Language fixed | Language:TODO | TODO | TODO | TODO | TODO | TODO | None | TODO |
| Language:TODO Q4 | Language fixed | Language:TODO | TODO | TODO | TODO | TODO | TODO | None | TODO |
| Language:TODO Q5 | Language fixed | Language:TODO | TODO | TODO | TODO | TODO | TODO | None | TODO |
| Language:TODO Q6 | Language fixed | Language:TODO | TODO | TODO | TODO | TODO | TODO | None | TODO |
| Language:TODO Q7 | Language fixed | Language:TODO | TODO | TODO | TODO | TODO | TODO | None | TODO |
| Language:TODO Q8 | Language fixed | Language:TODO | TODO | TODO | TODO | TODO | TODO | None | TODO |
| Language:TODO Q9 | Language fixed | Language:TODO | TODO | TODO | TODO | TODO | TODO | None | TODO |
| Language:TODO Q10 | Language fixed | Language:TODO | TODO | TODO | TODO | TODO | TODO | None | TODO |
| A1 | Adaptive | TODO | TODO | TODO | TODO | TODO | TODO | None | TODO |
| A2 | Adaptive | TODO | TODO | TODO | TODO | TODO | TODO | None | TODO |
| A3 | Adaptive | TODO | TODO | TODO | TODO | TODO | TODO | None | TODO |
| A4 | Adaptive | TODO | TODO | TODO | TODO | TODO | TODO | None | TODO |
| A5 | Adaptive | TODO | TODO | TODO | TODO | TODO | TODO | None | TODO |

## Project Question Answers

Record all 6 project-wide answers. If the user changes an answer, keep the final answer and note the change.

| Question | Final answer | User note | Changed from |
| --- | --- | --- | --- |
| P1 | TODO | TODO | TODO |
| P2 | TODO | TODO | TODO |
| P3 | TODO | TODO | TODO |
| P4 | TODO | TODO | TODO |
| P5 | TODO | TODO | TODO |
| P6 | TODO | TODO | TODO |

## Language Question Answers

Create one subsection per selected language.

### Language: TODO

Source question file:
TODO

Profile taxonomy:
TODO

| Question | Final answer | User note | Changed from |
| --- | --- | --- | --- |
| Q1 | TODO | TODO | TODO |
| Q2 | TODO | TODO | TODO |
| Q3 | TODO | TODO | TODO |
| Q4 | TODO | TODO | TODO |
| Q5 | TODO | TODO | TODO |
| Q6 | TODO | TODO | TODO |
| Q7 | TODO | TODO | TODO |
| Q8 | TODO | TODO | TODO |
| Q9 | TODO | TODO | TODO |
| Q10 | TODO | TODO | TODO |

## Adaptive Question Answers

Record exactly 5 adaptive answers.

| Question | Scope | Direction | Final answer | User note | Why asked |
| --- | --- | --- | --- | --- | --- |
| A1 | TODO | TODO | TODO | TODO | TODO |
| A2 | TODO | TODO | TODO | TODO | TODO |
| A3 | TODO | TODO | TODO | TODO | TODO |
| A4 | TODO | TODO | TODO | TODO | TODO |
| A5 | TODO | TODO | TODO | TODO | TODO |

## Feedback Summary

Record the user-facing feedback themes given during the interview. This helps future agents preserve a conversational, useful interview style without exposing hidden scoring.

- TODO

## Hidden Scoring Notes

Project-level signals:

- TODO

Language-level style-axis signals:

- TODO

Pattern signals:

- Encouraged: TODO
- Allowed with caution: TODO
- Avoid by default: TODO

Pattern and resource references:

| Reference | Local path or URL | Why it matters |
| --- | --- | --- |
| TODO | TODO | TODO |

Contradictions or weak signals:

- TODO

Evidence reviewed before generation:

- `Question Card Snapshots`
- `Answer Log`
- Project and language answer tables
- Adaptive answer table
- Pattern and resource references

## CodeBTI Result

Project profile name:
TODO

Project profile taxonomy reference:
`project/profiles/project-profile-taxonomy.md`

Language profiles:

| Language | Profile name | Profile taxonomy reference |
| --- | --- | --- |
| TODO | TODO | TODO |

Short explanation:
TODO

## Generated Outputs

- `CodeStyle.md`: TODO. Use the relevant language `templates/CodeStyle.template.md` and shared project rules.
- `ProjectStyle.md`: TODO. Use `project/templates/ProjectStyle.template.md` when project-level workflow guidance is generated separately.
- `SKILL.md`: TODO. Use `shared/templates/SKILL.template.md`.
- `SPEC.md`: TODO. Create after the opening intake and update during replanning. Use `shared/templates/SPEC.template.md`.

## Validation

Target project validation command:
TODO

CodeBTI repository validation command, if this record is generated while maintaining CodeBTI itself:
`python3 scripts/validate_repo.py`

Validation result:
TODO

## Unresolved Assumptions

- TODO
