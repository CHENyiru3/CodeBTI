# CodeBTI Agent Guide

## Project Summary

CodeBTI is a code-style counterpart to MBTI. MBTI describes personality preferences; CodeBTI describes coding and design preferences for a project or a general engineering identity.

The goal is not to create a toy personality quiz. The goal is to help an AI agent and a human developer explicitly choose the coding style, architectural boundaries, design patterns, and review standards that should remain consistent throughout a project. The final result should be practical enough to become a `SKILL.md`, a project `SPEC.md`, or a reusable `CodeStyle.md`.

The current version focuses on Python. The repository is organized so that other languages can be added later without changing the core workflow.

## Audience

This repository is face-to-agent. AI coding agents should be able to read it directly and understand:

- what CodeBTI is,
- how to interview a user,
- how to record answers,
- how to infer a coding-style profile,
- how to generate a project-specific `CodeStyle.md`,
- and how to extend the system with new languages or design-pattern examples.

All primary content should be plain markdown. Avoid runtime dependencies, web apps, binary assets, and tool-specific formats in the initial version.

## Repository Shape

```
CodeBTI/
  SKILL.md              # installable skill entry point
  AGENT.md              # agent guide and workflow reference
  README.md             # human entry point
  MANIFEST.md           # file inventory
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
  python/
    questions/
      README.md
      fixed-python.md
    patterns/
      README.md
      gof/               # GoF pattern pages for Python
        README.md
        abstract-factory.md
        adapter.md
        bridge.md
        builder.md
        chain-of-responsibility.md
        command.md
        composite.md
        decorator.md
        facade.md
        factory-method.md
        flyweight.md
        iterator.md
        mediator.md
        memento.md
        observer.md
        prototype.md
        proxy.md
        singleton.md
        state.md
        strategy.md
        template-method.md
        visitor.md
    profiles/
      README.md
      python-profile-taxonomy.md
    records/
      README.md
    templates/
      README.md
      CodeStyle.template.md
  typescript/
    questions/
      README.md
      fixed-typescript.md
    patterns/
      README.md
      gof/               # GoF pattern pages for TypeScript
        README.md
        abstract-factory.md
        adapter.md
        bridge.md
        builder.md
        chain-of-responsibility.md
        command.md
        composite.md
        decorator.md
        facade.md
        factory-method.md
        flyweight.md
        iterator.md
        mediator.md
        memento.md
        observer.md
        prototype.md
        proxy.md
        singleton.md
        state.md
        strategy.md
        template-method.md
        visitor.md
    profiles/
      README.md
      typescript-profile-taxonomy.md
    records/
      README.md
    templates/
      README.md
      CodeStyle.template.md
  examples/              # completed CodeBTI run (Python GUI calculator)
  zh/                    # Simplified Chinese translation
```

The root `SKILL.md` is the installable skill entry point. `AGENT.md` and `README.md` provide additional context for humans and non-skill agents.

## Core Workflow

1. The user describes what they want to build.
2. The agent creates or updates a live `Recording.md` in the target project.
3. The agent asks the 10 fixed questions in the target language's `questions/fixed-<lang>.md`.
4. Before every question, the agent saves the full question card in `Recording.md`; after every answer, it updates the answer log and gives brief project-specific feedback before asking the next question.
5. The agent asks exactly 5 adaptive follow-up questions using `shared/questions/adaptive-question-guide.md`.
6. The agent rereads `Recording.md` and treats it as the source of truth for final inference.
7. The agent analyzes the answers using the language's `profiles/<lang>-profile-taxonomy.md` and pattern database in `patterns/gof/`.
8. The agent selects specific local pattern/resource references that ground the recommendation.
9. The agent generates a detailed project `CodeStyle.md` from `templates/CodeStyle.template.md`, including references and one-sentence relevance notes.
10. If appropriate, the agent preserves or renames `Recording.md` as the final session record and distills the style guidance into `SKILL.md` or `SPEC.md` using `shared/templates/SKILL.template.md` and `shared/templates/SPEC.template.md`.

## Current Status

The Python and TypeScript language packs are implemented with a shared layer.

- human entry point: `README.md`,
- agent guide: `AGENT.md`,
- installable skill entry point: `SKILL.md`,
- shared interview resources: `shared/questions/`, `shared/templates/`, `shared/records/`,
- Python fixed question sheet: `python/questions/fixed-python.md`,
- TypeScript fixed question sheet: `typescript/questions/fixed-typescript.md`,
- 22-page Python design-pattern database: `python/patterns/gof/`,
- 23-page TypeScript design-pattern database: `typescript/patterns/gof/`,
- Python profile taxonomy: `python/profiles/python-profile-taxonomy.md`,
- TypeScript profile taxonomy: `typescript/profiles/typescript-profile-taxonomy.md`,
- Python `CodeStyle.md` template: `python/templates/CodeStyle.template.md`,
- TypeScript `CodeStyle.md` template: `typescript/templates/CodeStyle.template.md`,
- shared SKILL and SPEC templates: `shared/templates/`,
- shared session recording template: `shared/records/session-record.template.md`,
- completed example: `examples/`.

No automation scripts, CLI, web app, or CI system are part of the current version.

## File Type Responsibilities

### Entry Files

Entry files give agents the minimum context needed to proceed. `SKILL.md` is the installable skill entry point. `AGENT.md` provides additional workflow guidance. `README.md` explains CodeBTI for humans and links to the main workflow.

Entry files should be concise, operational, and stable. Avoid burying important instructions in long essays.

### Design Pattern Examples

Pattern files describe real engineering preferences. They should not simply list abstract patterns. Each file should explain:

- the style choice,
- when it is useful,
- when it becomes harmful,
- what it looks like in Python,
- what signals in a user's answers suggest this preference,
- and how the preference should appear in generated code or review comments.

Pattern examples are general references. The generated `CodeStyle.md` should be project-specific. The current Python pattern database mirrors the classic GoF catalog structure and cites RefactoringGuru sources in each pattern page.

### QA Sheets

The fixed Python QA sheet contains 10 example-based questions covering:

- general purpose and paradigm,
- defensive coding and type boundaries,
- error handling and recovery,
- naming and readability,
- architecture and wiring style,
- folder structure,
- testing philosophy,
- comments and docstrings,
- Git history and collaboration,
- dependencies and environments.

The adaptive question guide instructs the agent to ask exactly 5 follow-up questions based on ambiguity, contradictions, project risk, strong signals, and likely pattern misuse.

### Records

Each session should be recorded incrementally while the interview is happening. The default live filename is:

```text
Recording.md
```

The live record should live in the target project root so another agent can recover the interview state if context is lost. After the session, the record may be kept as `Recording.md` or copied into `python/records/` with a date-stamped filename. The date-stamped filename should include the date and a short project slug, for example:

```text
python/records/2026-04-22-my-python-cli.md
```

A session record should include:

- project summary,
- interview progress,
- full question card snapshots,
- answer log in chronological order,
- fixed questions and answers,
- adaptive questions and answers,
- brief feedback given after each answer,
- agent observations,
- inferred CodeBTI profile,
- generated output files,
- and unresolved assumptions.

Do not record secrets, private credentials, or irrelevant personal information.

### Generated Output

The primary generated artifact is `CodeStyle.md`. It should be specific enough that an agent can use it during implementation and review.

A strong `CodeStyle.md` should define:

- project intent,
- preferred architecture,
- module boundaries,
- naming conventions,
- typing policy,
- error-handling policy,
- dependency policy,
- testing policy,
- documentation policy,
- examples of preferred code,
- examples of avoided code,
- review checklist,
- and instructions for future agent behavior.
- references to the local pattern/resource pages that ground the recommendations.

When useful, the same guidance can be distilled into:

- `SKILL.md` for reusable agent behavior,
- `SPEC.md` for project-specific requirements,
- or narrower spec files such as `API_SPEC.md`, `TESTING_SPEC.md`, or `ARCHITECTURE_SPEC.md`.

## CodeBTI Profile Concept

CodeBTI should produce memorable profile names, but the profiles must remain engineering-grounded. A profile is a shorthand for a set of design preferences, not a substitute for detailed guidance.

For the initial Python version, define profiles across practical axes such as:

- Abstraction: local and concrete vs. layered and generalized.
- Type discipline: dynamic and pragmatic vs. strict and explicit.
- State model: mutable workflow vs. immutable transformations.
- Error model: exceptions, result objects, validation upfront, or fail-fast.
- Dependency posture: standard-library first vs. ecosystem-friendly.
- Testing style: behavior-first, unit-first, property-based, integration-heavy, or smoke-test oriented.

The current Python taxonomy defines practical profile families such as:

- `Object-Centered Boundary Keeper`
- `Function-First Pipeline Builder`
- `Data-First Validator`
- `Pragmatic Script Builder`
- `Test-First Integrator`
- `Framework-Aligned Builder`
- `Algorithm-First Minimalist`

Use `python/profiles/python-profile-taxonomy.md` as the initial Python taxonomy and refine it as new interview data appears.

## Initial Python Scope

The first version should focus on Python projects, including:

- packages,
- command-line tools,
- data processing scripts,
- APIs,
- notebooks converted into maintainable modules,
- and agent-written project scaffolds.

The Python guidance should cover at least:

- project layout,
- imports,
- typing,
- dataclasses and Pydantic-style models,
- exceptions,
- logging,
- configuration,
- dependency management,
- tests,
- scripts and CLIs,
- docstrings,
- and review expectations.

Do not overfit the system to one framework. Framework-specific guidance should be added as optional extensions.

## Expansion Model

Future languages should be added as sibling directories. Each language pack owns its fixed questions, pattern pages, profile taxonomy, and `CodeStyle.md` template. Shared interview resources in `shared/` are used by all language packs without modification.

```
CodeBTI/
  shared/               # shared across all languages
  python/
  typescript/
  rust/                 # new language pack
    questions/fixed-rust.md
    patterns/gof/
    profiles/rust-profile-taxonomy.md
    templates/CodeStyle.template.md
```

The general workflow stays language-neutral. Language folders hold language-specific examples, questions, and taxonomy details.

## Agent Behavior Rules

When an agent works in this repository:

- Prefer markdown files over code unless the user explicitly asks for tooling.
- Keep source files readable by both humans and agents.
- Make generated templates structured and easy to fill.
- Avoid vague style advice that cannot guide implementation.
- Include tradeoffs, not just rules.
- Preserve session records as evidence for generated recommendations.
- Treat CodeBTI results as project guidance, not personal judgment.
- Keep Python as the first implementation target while leaving room for other languages.

## Current Definition of Done

A language pack is ready when it contains:

- the fixed question sheet in `questions/fixed-<lang>.md`,
- a pattern index in `patterns/README.md`,
- GoF pattern pages in `patterns/gof/`,
- a profile taxonomy draft in `profiles/<lang>-profile-taxonomy.md`,
- a `CodeStyle.md` template in `templates/CodeStyle.template.md`.

The shared layer (`shared/questions/`, `shared/templates/`, `shared/records/`) is shared — it does not need to be replicated per language.

With these files present, a user can ask an AI agent to run a CodeBTI interview and receive a useful project-specific `CodeStyle.md`.
