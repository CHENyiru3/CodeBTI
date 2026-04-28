# CodeBTI Agent Guide

## Project Summary

CodeBTI is a code-style counterpart to MBTI. MBTI describes personality preferences; CodeBTI describes coding and design preferences for a project or engineering context.

The goal is not to create a toy personality quiz. The goal is to help an AI agent and a human developer explicitly choose the project workflow, architectural boundaries, design patterns, review standards, testing policy, dependency policy, and language-specific coding style that should remain consistent throughout a project.

The repository is Markdown-first and agent-facing. AI coding agents should be able to read it directly and understand how to run an interview, record answers, infer profiles, and generate project guidance.

## Repository Shape

```text
CodeBTI/
  SKILL.md              # installable skill entry point and router
  AGENT.md              # agent guide and workflow reference
  README.md             # human entry point
  MANIFEST.md           # file inventory
  project/              # project-wide interview pack
    questions/fixed-project.md
    profiles/project-profile-taxonomy.md
    templates/ProjectStyle.template.md
  shared/               # language-neutral interview resources
    questions/
      adaptive-question-guide.md
      editorial-guide.md
      question-format.md
      shared-architecture.md
    templates/
      SKILL.template.md
      SPEC.template.md
    records/
      session-record.template.md
  python/               # Python language pack
  typescript/           # TypeScript language pack
  scripts/              # validation tooling
  .github/workflows/    # CI validation
  docs/                 # operational workflow guides
  examples/             # completed single-language example
  zh/                   # Simplified Chinese translation
```

The root `SKILL.md` is the installable skill entry point. It routes every CodeBTI session through the project pack first, then through one or more language packs.

## Core Workflow

1. The user describes what they want to build.
2. The agent identifies target language packs. If unclear, ask one concise clarification before scored questions.
3. The agent creates or updates a live `Recording.md` in the target project.
4. The agent asks the 6 fixed project questions in `project/questions/fixed-project.md`.
5. The agent asks fixed questions for each selected language pack, such as Python or TypeScript.
6. Before every scored question, the agent saves the full question card in `Recording.md`.
7. After every answer, the agent updates the answer log and gives brief project-specific feedback before asking the next question.
8. The agent asks exactly 5 adaptive follow-up questions total using `shared/questions/adaptive-question-guide.md`.
9. The agent rereads `Recording.md` and treats it as the source of truth.
10. The agent analyzes project answers using `project/profiles/project-profile-taxonomy.md`.
11. The agent analyzes language answers using each language's profile taxonomy and `patterns/gof/` database.
12. The agent selects specific local pattern/resource references that materially affect the recommendation.
13. The agent generates the requested guidance: `CodeStyle.md`, optional `ProjectStyle.md`, optional `SKILL.md`, optional `SPEC.md`, or narrower spec files.

Use `docs/golden-path.md` as the operational checklist when validating or teaching the workflow.

## Current Status

The project, Python, and TypeScript packs are implemented with a shared layer.

- human entry point: `README.md`,
- release notes: `CHANGELOG.md`,
- golden path guide: `docs/golden-path.md`,
- agent/router entry point: `SKILL.md`,
- agent guide: `AGENT.md`,
- project-wide questions: `project/questions/fixed-project.md`,
- project profile taxonomy: `project/profiles/project-profile-taxonomy.md`,
- shared interview resources: `shared/questions/`, `shared/templates/`, `shared/records/`,
- Python fixed question sheet: `python/questions/fixed-python.md`,
- TypeScript fixed question sheet: `typescript/questions/fixed-typescript.md`,
- 22-page Python design-pattern database: `python/patterns/gof/`,
- 22-page TypeScript design-pattern database: `typescript/patterns/gof/`,
- validation script: `scripts/validate_repo.py`,
- quality test harness: `tests/`,
- CI workflow: `.github/workflows/validate.yml`,
- Simplified Chinese translation: `zh/`.

No runtime interview app is part of the current version.

## File Type Responsibilities

### Entry Files

Entry files give agents the minimum context needed to proceed. `SKILL.md` is operational and should remain concise. `README.md` explains CodeBTI for humans. `AGENT.md` defines repository maintenance expectations.

### Project Pack

The project pack contains cross-cutting questions and profile guidance. It controls:

- collaboration workflow,
- output shape,
- validation gates,
- shared-vs-language rule boundaries,
- dependency governance,
- change record policy.

Language packs should not duplicate these decisions unless a language-specific override is necessary and recorded.

### Language Packs

Each language pack owns its fixed questions, pattern pages, profile taxonomy, records guide, and `CodeStyle.md` template. Language packs should use shared interview mechanics and shared output templates rather than copying them.

### Shared Layer

Shared files must remain project- and language-neutral. Use them for question format, adaptive question rules, editorial rules, session record structure, and language-neutral SKILL/SPEC templates.

If a pack needs to deviate from shared rules, document the conflict in that pack. Do not fork shared files into a language pack.

### Design Pattern Examples

Pattern files describe real engineering preferences. Each file should explain:

- the style choice,
- when it is useful,
- when it becomes harmful,
- what it looks like in the target language,
- what signals in a user's answers suggest this preference,
- and how the preference should appear in generated code or review comments.

Generated `CodeStyle.md` guidance should be project-specific. Cite only pattern pages that shaped the recommendation.

### Records

Each session should be recorded incrementally while the interview is happening. The default live filename is:

```text
Recording.md
```

The live record should live in the target project root so another agent can recover interview state if context is lost. Use `shared/records/session-record.template.md` as the starting point.

A session record should include:

- project summary,
- language targets,
- interview progress,
- full question card snapshots,
- chronological answer log,
- project fixed answers,
- language fixed answers,
- adaptive answers,
- feedback given after each answer,
- hidden inference notes,
- inferred project and language profiles,
- generated output files,
- validation result,
- unresolved assumptions.

Do not record secrets, private credentials, or irrelevant personal information.

### Generated Output

The primary generated artifact is `CodeStyle.md`. It should be specific enough that an agent can use it during implementation and review.

A strong `CodeStyle.md` should define:

- project intent,
- shared project rules,
- preferred architecture,
- module boundaries,
- language-specific style rules,
- typing policy,
- error-handling policy,
- dependency policy,
- testing policy,
- documentation policy,
- examples of preferred code,
- examples of avoided code,
- review checklist,
- instructions for future agent behavior,
- references to local pattern/resource pages.

When useful, generate:

- `ProjectStyle.md` for project workflow and governance,
- `SKILL.md` for reusable agent behavior,
- `SPEC.md` for project-specific requirements,
- narrower spec files such as `API_SPEC.md`, `TESTING_SPEC.md`, or `ARCHITECTURE_SPEC.md`.

## Profile Concept

CodeBTI profiles are engineering shorthand, not judgments of skill or personality.

Project profiles describe workflow and governance preferences, such as:

- `Controlled Multi-Language Maintainer`,
- `Lightweight Prototype Collaborator`,
- `Review-Gated Integrator`,
- `Release-Managed Steward`.

Language profiles describe coding-style preferences, such as:

- Python `Object-Centered Boundary Keeper`,
- Python `Data-First Validator`,
- TypeScript `Interface-First Boundary Keeper`,
- TypeScript `Functional Pipeline Builder`.

Mixed results should be expressed as combined profiles rather than forced into a single clean label.

## Expansion Model

Future languages should be added as sibling directories. Each language pack owns its fixed questions, pattern pages, profile taxonomy, records guide, and `CodeStyle.md` template. Shared interview resources in `shared/` are used by all packs without modification.

```text
CodeBTI/
  shared/
  project/
  python/
  typescript/
  rust/
    questions/fixed-rust.md
    patterns/gof/
    profiles/rust-profile-taxonomy.md
    records/README.md
    templates/CodeStyle.template.md
```

After adding or changing packs, update `README.md`, `AGENT.md`, and `MANIFEST.md`, then run:

```sh
python3 scripts/validate_repo.py
python3 -m pytest
```

## Validation Gate

The repository has a lightweight validation gate. It checks:

- local Markdown links,
- required pack files,
- fixed-question counts and required sections,
- fixed-question ID/scope quality,
- choice/scoring/pattern-signal label parity,
- required template sections,
- shared Chinese mirror coverage,
- manifest drift.

Run it before submitting changes:

```sh
python3 scripts/validate_repo.py
python3 -m pytest
```

GitHub Actions runs the same command on pull requests and pushes.

For release-hardening passes, also run:

```sh
git diff --check
PYTHONPYCACHEPREFIX=/tmp/codebti_pycache python3 -m py_compile scripts/validate_repo.py
```

## Agent Behavior Rules

When an agent works in this repository:

- Prefer Markdown files over code unless the user explicitly asks for tooling.
- Keep source files readable by both humans and agents.
- Keep `shared/` language-neutral.
- Keep project-wide workflow decisions in `project/`.
- Keep language-specific examples, patterns, and profile rules inside the language pack.
- Avoid vague style advice that cannot guide implementation.
- Include tradeoffs, not just rules.
- Preserve session records as evidence for generated recommendations.
- Treat CodeBTI results as project guidance, not personal judgment.
- Run `python3 scripts/validate_repo.py` after structural, link, question, template, or manifest changes.

## Definition of Done

A change is ready when:

- docs describe one consistent workflow,
- relevant question/profile/template files are updated together,
- translated mirror files are updated when shared files change,
- `MANIFEST.md` reflects new files or directories,
- `python3 scripts/validate_repo.py` passes,
- `python3 -m pytest` passes,
- release-hardening changes also pass `git diff --check` and `py_compile`.
