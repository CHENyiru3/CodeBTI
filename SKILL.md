---
name: codebti
description: Run CodeBTI interviews to infer coding style preferences and generate project-specific CodeStyle.md, SKILL.md, or SPEC.md for Python projects.
---

# CodeBTI Skill

Use this skill when a user wants to establish consistent coding style, design-pattern posture, testing policy, or collaboration workflow for a project. Trigger on: "run a CodeBTI interview", "define our coding style", "create a CodeStyle.md", "generate a SKILL.md", "create a SPEC.md", "what's our project style", or any explicit request to use CodeBTI.

## Workflow

1. Ask the 10 fixed Python questions in `ref/questions/fixed-python.md`.
2. Ask exactly 5 adaptive follow-up questions using `ref/questions/adaptive-question-guide.md`.
3. Record the session with `ref/records/session-record.template.md`.
4. Infer the Python profile from `ref/profiles/python-profile-taxonomy.md` and the pattern database in `ref/patterns/`.
5. Generate `CodeStyle.md` from `ref/templates/CodeStyle.template.md`.
6. Optionally distill the result into `SKILL.md` or `SPEC.md` using the templates in `ref/templates/`.

## Reference Material

| File | Purpose |
|------|---------|
| `ref/questions/fixed-python.md` | 10 fixed interview questions with code examples |
| `ref/questions/adaptive-question-guide.md` | Rules for 5 follow-up questions |
| `ref/questions/editorial-guide.md` | Editorial rules for questions |
| `ref/records/session-record.template.md` | Session recording template |
| `ref/profiles/python-profile-taxonomy.md` | Python profile inference rules |
| `ref/patterns/` | 22 Python design-pattern pages (GoF + extras) |
| `ref/templates/CodeStyle.template.md` | CodeStyle.md output template |
| `ref/templates/SKILL.template.md` | SKILL.md output template |
| `ref/templates/SPEC.template.md` | SPEC.md output template |

## Agent Rules

- Show user-facing scenarios, instructions, code examples, and choices; keep scoring/signal notes hidden unless the user asks.
- Allow the user to revise earlier answers at any time.
- Do not mix typing styles, error policies, or naming conventions inconsistently in generated output.
- Preserve session records as evidence for generated recommendations.
- Prefer markdown output over scripts or tooling unless the user explicitly requests it.