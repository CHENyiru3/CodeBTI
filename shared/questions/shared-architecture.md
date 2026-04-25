# Shared Architecture

This folder contains language-neutral parts of the CodeBTI interview system. They are shared across all language packs so that interview flow, editorial guidelines, and output structure remain consistent while question content and pattern examples remain language-specific.

## What Is Shared

| File | Purpose |
|------|---------|
| `adaptive-question-guide.md` | Rules for selecting and asking 5 follow-up questions. Language-neutral. |
| `editorial-guide.md` | Question-writing rules. Language-neutral. |
| `question-format.md` | Standard card structure for every question. Language-neutral. |
| `shared-architecture.md` | This file — explains the multi-language design. |

Shared templates and records are in `../templates/` and `../records/`.

## Multi-Language Interview Model

### Language-specific files

Each language pack owns:

- **`questions/fixed-<lang>.md`** — 10 fixed interview questions with code examples in that language. This is the core language-specific artifact.
- **`patterns/<lang>/`** — design pattern pages adapted for that language ecosystem.
- **`profiles/<lang>-profile-taxonomy.md`** — profile families for that language.
- **`templates/CodeStyle.template.md`** — output template with language-specific sections (e.g., `interface` vs `type` for TypeScript, `dataclass` vs `pydantic` for Python).

### Shared files

All language packs share:

- `shared/questions/` — interview flow rules, question structure, editorial guidelines.
- `shared/templates/` — SKILL and SPEC output templates (language-neutral).
- `shared/records/` — session recording template.

### How the interview flows

1. Opening prompt (language-neutral).
2. 10 fixed questions from the language's `questions/fixed-<lang>.md`.
3. 5 adaptive follow-up questions — rules from `shared/questions/adaptive-question-guide.md`, content shaped by the fixed answers.
4. Profile inference using `profiles/<lang>-profile-taxonomy.md` and `patterns/<lang>/`.
5. Output generation using `templates/CodeStyle.template.md` and `shared/templates/SKILL.template.md` / `shared/templates/SPEC.template.md`.

### Why this separation matters

- Question content (scenarios, code examples, language idioms) is language-specific and must be maintained per language pack.
- Interview mechanics (one question per turn, full card in recording, feedback after each answer) stay consistent across languages so agents behave the same way.
- Output templates can be shared because `SKILL.md` and `SPEC.md` are language-neutral documents — the language-specific guidance goes into `CodeStyle.md`.

### Adding a new language pack

1. Create `<lang>/questions/fixed-<lang>.md` with 10 language-specific questions.
2. Create `<lang>/patterns/<lang>/` with pattern pages in that language.
3. Create `<lang>/profiles/<lang>-profile-taxonomy.md`.
4. Create `<lang>/templates/CodeStyle.template.md` with language-specific output sections.
5. Copy `templates/SKILL.template.md` and `templates/SPEC.template.md` from `shared/templates/` (or reference them).
6. The shared files in `shared/questions/` and `shared/records/` work out of the box.

## Agent Rules for Shared Files

- Never modify `shared/questions/`, `shared/templates/`, or `shared/records/` in a language-specific way.
- If a language pack needs to deviate from shared rules, raise the conflict in an issue rather than forking shared content.
- When referencing shared files from within a language pack, use relative paths (e.g., `../../shared/questions/question-format.md`).