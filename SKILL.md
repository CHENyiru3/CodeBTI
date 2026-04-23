---
name: codebti
description: Run CodeBTI interviews to infer coding style preferences and generate project-specific CodeStyle.md, SKILL.md, or SPEC.md for Python projects.
---

# CodeBTI Skill

Use this skill when a user wants to establish consistent coding style, design-pattern posture, testing policy, or collaboration workflow for a project. Trigger on: "run a CodeBTI interview", "define our coding style", "create a CodeStyle.md", "generate a SKILL.md", "create a SPEC.md", "what's our project style", or any explicit request to use CodeBTI.

## Workflow

1. Ask the required opening prompt: "What kind of project do you want to build? Please describe shortly."
2. Create or update a live `Recording.md` in the target project root using `python/records/session-record.template.md` as the structure.
3. Record the opening answer as the project summary. This opening prompt is not a scored fixed question.
4. For each of the 10 fixed Python questions in `python/questions/fixed-python.md`, save the full user-facing question card in `Recording.md`, ask the question, then record the answer.
5. After each user answer, update `Recording.md`, give a brief feedback response that reflects what the answer means for the project, then ask the next question.
6. Ask exactly 5 adaptive follow-up questions using `python/questions/adaptive-question-guide.md`; for each adaptive question, save the generated full question card before asking it.
7. After each adaptive answer, update `Recording.md` with the answer, feedback, and hidden inference notes.
8. After all 15 scored questions are answered, reread `Recording.md` and use it as the source of truth for profile inference.
9. Infer the Python profile from `python/profiles/python-profile-taxonomy.md` and the pattern database in `python/patterns/`.
10. Select the local pattern/resource references that ground the final recommendation. Prefer specific files under `python/patterns/python/` and include only references that affect the guidance.
11. Generate `CodeStyle.md` from `python/templates/CodeStyle.template.md`, including a References section with local pattern links and one-sentence relevance notes.
12. Optionally preserve or rename `Recording.md` as the final session record, and optionally distill the result into `SKILL.md` or `SPEC.md` using the templates in `python/templates/`.

## Reference Material

| File | Purpose |
|------|---------|
| `python/questions/fixed-python.md` | 10 fixed interview questions with code examples |
| `python/questions/adaptive-question-guide.md` | Rules for 5 follow-up questions |
| `python/questions/editorial-guide.md` | Editorial rules for questions |
| `python/records/session-record.template.md` | Session recording template |
| `python/profiles/python-profile-taxonomy.md` | Python profile inference rules |
| `python/patterns/` | 22 Python design-pattern pages (GoF + extras) |
| `python/templates/CodeStyle.template.md` | CodeStyle.md output template |
| `python/templates/SKILL.template.md` | SKILL.md output template |
| `python/templates/SPEC.template.md` | SPEC.md output template |

## Agent Rules

- Ask exactly one user-facing interview question per turn, including the opening prompt, fixed questions, and adaptive follow-up questions.
- Show user-facing scenarios, instructions, code examples, and choices; keep scoring/signal notes hidden unless the user asks.
- Save every question card in `Recording.md`, not just the answer. A recoverable record includes the title, dimension, scenario, instruction, code example, choices, source path, user answer, feedback, and hidden inference notes.
- After receiving each answer, respond with one or two sentences of project-specific feedback before the next question. Good feedback names the implication, such as "That points this project toward lightweight objects without strict type ceremony." Do not reveal hidden scoring tables.
- Maintain `Recording.md` throughout the interview so answer history survives context loss. Update it after every answer before asking the next question.
- At the end, reread `Recording.md` before generating `CodeStyle.md`, `SKILL.md`, or `SPEC.md`.
- Ground final reports with references to relevant local pattern pages, for example `python/patterns/python/facade.md`, plus useful resource links when a framework or library choice shaped the guidance.
- In final reports, every cited pattern should explain whether it is encouraged, allowed with caution, or avoided for this project.
- Allow the user to revise earlier answers at any time.
- Do not mix typing styles, error policies, or naming conventions inconsistently in generated output.
- Preserve session records as evidence for generated recommendations.
- Prefer markdown output over scripts or tooling unless the user explicitly requests it.
