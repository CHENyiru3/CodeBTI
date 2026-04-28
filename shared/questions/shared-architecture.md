# Shared Architecture

This folder contains language-neutral parts of the CodeBTI interview system. They are shared across all packs so interview mechanics, editorial guidelines, and output structure remain consistent while project and language packs own their content.

## What Is Shared

| File | Purpose |
|------|---------|
| `adaptive-question-guide.md` | Rules for selecting and asking 5 follow-up questions. Language-neutral. |
| `editorial-guide.md` | Question-writing rules. Language-neutral. |
| `question-format.md` | Standard card structure for every question. Language-neutral. |
| `shared-architecture.md` | This file explains the project/language pack design. |

Shared templates and records are in `../templates/` and `../records/`.

## Pack Model

### Project pack

The `project/` pack owns cross-cutting interview content:

- `project/questions/fixed-project.md` — project-wide questions.
- `project/profiles/project-profile-taxonomy.md` — workflow and governance profile families.
- `project/templates/ProjectStyle.template.md` — project-level output template.

Project-wide answers control collaboration, validation gates, output shape, dependency governance, change records, and shared-vs-language boundaries.

### Language packs

Each language pack owns:

- `questions/fixed-<lang>.md` — fixed interview questions with examples in that language.
- `patterns/gof/` — design pattern pages adapted for that language ecosystem.
- `profiles/<lang>-profile-taxonomy.md` — profile families for that language.
- `templates/CodeStyle.template.md` — output template with language-specific sections.

### Shared files

All packs share:

- `shared/questions/` — interview flow rules, question structure, editorial guidelines.
- `shared/templates/` — SKILL and SPEC output templates.
- `shared/records/` — session recording template.

## How the Interview Flows

1. SPEC-style opening prompt and initial `SPEC.md` draft.
2. Fixed project questions from `project/questions/fixed-project.md`.
3. Fixed language questions from each selected language pack.
4. Exactly 5 adaptive follow-up questions using `shared/questions/adaptive-question-guide.md`.
5. Project profile inference using `project/profiles/project-profile-taxonomy.md`.
6. Language profile inference using each language's profile taxonomy and `patterns/gof/` pages.
7. Output generation using the relevant language `CodeStyle.template.md`, optional `project/templates/ProjectStyle.template.md`, and optional shared SKILL/SPEC templates.

## Why This Separation Matters

- Project process decisions are asked once and reused across languages.
- Question content, code examples, and language idioms stay language-specific.
- Interview mechanics stay consistent, so agents behave the same way across packs.
- Shared templates avoid duplicated SKILL/SPEC structure while language packs keep their own CodeStyle details.

## Adding a New Language Pack

1. Create `<lang>/questions/fixed-<lang>.md` with fixed language-specific questions.
2. Create `<lang>/patterns/gof/` with pattern pages in that language.
3. Create `<lang>/profiles/<lang>-profile-taxonomy.md`.
4. Create `<lang>/templates/CodeStyle.template.md` with language-specific output sections.
5. Reference `shared/` for adaptive guide, editorial rules, session record, and SKILL/SPEC templates. Do not copy shared files into the language pack.
6. Update `README.md`, `AGENT.md`, and `MANIFEST.md`.
7. Run `python3 scripts/validate_repo.py`.

## Agent Rules for Shared Files

- Never modify `shared/questions/`, `shared/templates/`, or `shared/records/` in a project- or language-specific way.
- If a pack needs to deviate from shared rules, document the conflict in that pack rather than forking shared content.
- When referencing shared files from within a pack, use relative paths such as `../../shared/questions/question-format.md`.
