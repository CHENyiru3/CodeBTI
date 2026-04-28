---
name: codebti
description: Run CodeBTI interviews to infer project and language coding-style preferences and generate project-specific CodeStyle.md, SKILL.md, or SPEC.md guidance.
---

# CodeBTI Skill

Use this skill when a user wants to establish consistent coding style, design-pattern posture, testing policy, dependency policy, or collaboration workflow for a project. Trigger on: "run a CodeBTI interview", "define our coding style", "create a CodeStyle.md", "generate a SKILL.md", "create a SPEC.md", "what's our project style", or any explicit request to use CodeBTI.

## Supported Packs

| Pack | Purpose |
|------|---------|
| `project/` | Project-wide decisions: collaboration, output shape, validation gates, shared-vs-language rules, dependency governance, and change records. |
| `python/` | Python-specific style, typing, error handling, folder structure, tests, comments, Git, and dependencies. |
| `typescript/` | TypeScript-specific style, typing, interfaces/types, error handling, folder structure, tests, comments, Git, and dependencies. |
| `shared/` | Language-neutral question format, adaptive question rules, templates, and session record structure. |

## Router Workflow

1. Ask the required opening prompt:
   "Please describe the project as a compact SPEC-style brief. Include mission, goals, target audience, constraints, likely tech stack or language targets, roadmap intent, non-goals, and open questions. Keep this at the what/why level; avoid low-level implementation details unless they are hard constraints."
2. Identify the target language pack or packs from the user's answer. If the language is unclear, ask one concise clarification before starting scored questions.
3. Create or update a live `Recording.md` in the target project root using `shared/records/session-record.template.md` as the structure.
4. Record the opening answer as the project summary and SPEC intake. This opening prompt is not scored.
5. Create or update an initial `SPEC.md` draft using `shared/templates/SPEC.template.md`. Preserve what and why; leave implementation details for later feature planning unless the user named them as constraints.
6. Ask the 6 fixed project questions from `project/questions/fixed-project.md`. Save the full user-facing question card in `Recording.md` before each question, then record the answer and feedback.
7. For each selected language pack, ask that language's fixed questions:
   - Python: `python/questions/fixed-python.md`
   - TypeScript: `typescript/questions/fixed-typescript.md`
8. Record each language answer set under its language target in `Recording.md`.
9. Ask exactly 5 adaptive follow-up questions total for the whole session using `shared/questions/adaptive-question-guide.md`. The adaptive questions may target project-level ambiguity, one language, or a cross-language conflict.
10. After all scored questions are answered, reread `Recording.md` and the current `SPEC.md` draft, then use them as the source of truth for profile inference.
11. Infer the project-level profile from `project/profiles/project-profile-taxonomy.md`.
12. Infer each language profile from its language taxonomy and pattern database:
    - Python: `python/profiles/python-profile-taxonomy.md`, `python/patterns/gof/`
    - TypeScript: `typescript/profiles/typescript-profile-taxonomy.md`, `typescript/patterns/gof/`
13. Select only local pattern/resource references that materially affect the final recommendation.
14. Generate the requested guidance:
    - single-language project: use that language's `templates/CodeStyle.template.md`;
    - multi-language project: use `project/templates/MultiLanguageCodeStyle.template.md` with shared project rules first, then language-specific sections;
    - project-level workflow summary: use `project/templates/ProjectStyle.template.md` when helpful;
    - optional `SKILL.md` or `SPEC.md`: use `shared/templates/SKILL.template.md` and `shared/templates/SPEC.template.md`.

## Reference Material

| File | Purpose |
|------|---------|
| `project/questions/fixed-project.md` | 6 project-wide interview questions |
| `project/profiles/project-profile-taxonomy.md` | Project-level workflow and governance profiles |
| `project/templates/ProjectStyle.template.md` | Project-level style and workflow output template |
| `project/templates/MultiLanguageCodeStyle.template.md` | Multi-language CodeStyle.md output template |
| `python/questions/fixed-python.md` | 10 fixed Python interview questions |
| `typescript/questions/fixed-typescript.md` | 10 fixed TypeScript interview questions |
| `shared/questions/adaptive-question-guide.md` | Rules for 5 adaptive follow-up questions |
| `shared/questions/editorial-guide.md` | Editorial rules for questions |
| `shared/questions/question-format.md` | Standard question card format |
| `shared/records/session-record.template.md` | Multi-round session recording template |
| `shared/templates/SKILL.template.md` | SKILL.md output template |
| `shared/templates/SPEC.template.md` | SPEC.md output template |

## Agent Rules

- Ask exactly one user-facing interview question per turn, including the opening prompt, project questions, language questions, and adaptive follow-ups.
- Treat the opening prompt as a single SPEC-style intake question. Do not split it into multiple turns unless the user asks to proceed section by section.
- If the opening answer omits requested SPEC fields, record missing fields under open questions instead of interrupting with multiple clarifications. Use adaptive questions later for the highest-risk gaps.
- Show user-facing scenarios, instructions, code examples, and choices; keep scoring/signal notes hidden unless the user asks.
- Save every question card in `Recording.md`, not just the answer.
- Create or update `SPEC.md` immediately after the opening answer, then revise it after later replanning or feature work.
- After receiving each answer, update `Recording.md`, give one or two sentences of project-specific feedback, then ask the next question.
- Keep project-wide answers separate from language-specific answers.
- For multi-language projects, shared project rules govern Git workflow, dependency governance, validation gates, output shape, and change records unless a language section explicitly overrides them.
- At the end, reread `Recording.md` and `SPEC.md` before generating `CodeStyle.md`, `ProjectStyle.md`, `SKILL.md`, or final SPEC updates.
- Ground final reports with relevant local pattern pages and profile references. Every cited pattern should explain whether it is encouraged, allowed with caution, or avoided for this project.
- Allow the user to revise earlier answers at any time and record answer changes.
- Do not mix typing styles, error policies, naming conventions, or validation expectations inconsistently in generated output.
- Preserve session records as evidence for generated recommendations.
- Prefer Markdown output over scripts or tooling unless the user explicitly requests tooling.
