# CodeBTI Agent Guide

## Project Summary

CodeBTI is a code-style counterpart to MBTI. MBTI describes personality preferences; CodeBTI describes coding and design preferences for a project or a general engineering identity.

The goal is not to create a toy personality quiz. The goal is to help an AI agent and a human developer explicitly choose the coding style, architectural boundaries, design patterns, and review standards that should remain consistent throughout a project. The final result should be practical enough to become a `SKILL.md`, a project `SPEC.md`, or a reusable `CodeStyle.md`.

The initial version focuses on Python. The repository should be designed so that other languages can be added later without changing the core workflow.

## Audience

This repository is face-to-agent. AI coding agents should be able to read it directly and understand:

- what CodeBTI is,
- how to interview a user,
- how to record answers,
- how to infer a coding-style profile,
- how to generate a project-specific `CodeStyle.md`,
- and how to extend the system with new languages or design-pattern examples.

All primary content should be plain markdown. Avoid runtime dependencies, web apps, binary assets, and tool-specific formats in the initial version.

## Core Workflow

1. The user describes what they want to build.
2. The agent asks 10 fixed CodeBTI questions.
3. The agent asks 5 adaptive follow-up questions based on the user's previous answers and project description.
4. The agent records all answers in a session record file.
5. The agent analyzes the answers and assigns a CodeBTI style profile.
6. The agent generates a detailed `CodeStyle.md` for the project.
7. If appropriate, the agent distills the style guidance into a `SKILL.md` or one or more `SPEC.md` files.

## Repository Shape

Use this structure for the initial Python-focused version:

```text
CodeBTI/
  AGENT.md
  README.md
  questions/
    README.md
    fixed-python.md
    adaptive-question-guide.md
  patterns/
    README.md
    python/
      README.md
      error-handling.md
      typing.md
      data-modeling.md
      dependency-boundaries.md
      testing.md
      configuration.md
      cli-and-scripts.md
      documentation.md
  profiles/
    README.md
    python-profile-taxonomy.md
  records/
    README.md
    .gitkeep
  templates/
    CodeStyle.template.md
    session-record.template.md
    SKILL.template.md
    SPEC.template.md
```

The exact filenames can evolve, but the content types should remain clear:

- Entry files: orient the agent and define the workflow.
- Design pattern examples: explain style options and tradeoffs.
- QA sheets: define fixed and adaptive questions.
- Records: preserve each user's answers and inferred result.
- Templates: provide predictable generated outputs.

## File Type Responsibilities

### Entry Files

Entry files give agents the minimum context needed to proceed. `AGENT.md` is the top-level agent contract. `README.md` should explain CodeBTI for humans and link to the main workflow.

Entry files should be concise, operational, and stable. Avoid burying important instructions in long essays.

### Design Pattern Examples

Pattern files describe real engineering preferences. They should not simply list abstract patterns. Each file should explain:

- the style choice,
- when it is useful,
- when it becomes harmful,
- what it looks like in Python,
- what signals in a user's answers suggest this preference,
- and how the preference should appear in generated code or review comments.

Pattern examples are general references. The generated `CodeStyle.md` should be project-specific.

### QA Sheets

The fixed QA sheet should contain 10 carefully designed questions for Python projects. These questions should cover stable style axes such as:

- explicitness vs. concision,
- strict typing vs. lightweight typing,
- functional style vs. object-oriented style,
- framework-driven design vs. small local abstractions,
- exception strategy,
- data validation boundaries,
- test granularity,
- dependency tolerance,
- configuration style,
- and documentation expectations.

The adaptive question guide should instruct the agent to ask 5 follow-up questions based on ambiguity, contradictions, project risk, and domain-specific needs.

### Records

Each session should be recorded in `records/` using a markdown file. The filename should include the date and a short project slug, for example:

```text
records/2026-04-22-my-python-cli.md
```

A session record should include:

- project summary,
- fixed questions and answers,
- adaptive questions and answers,
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

Example profile naming styles:

- `Typed Minimalist`
- `Pragmatic Layerist`
- `Functional Pipeline Builder`
- `Framework-Aligned Builder`
- `Test-First Boundary Keeper`

These names are placeholders. The taxonomy should be refined in `profiles/python-profile-taxonomy.md`.

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

Future languages should be added by creating parallel language folders rather than rewriting the core workflow.

Example:

```text
questions/
  fixed-python.md
  fixed-typescript.md
patterns/
  python/
  typescript/
profiles/
  python-profile-taxonomy.md
  typescript-profile-taxonomy.md
```

The general workflow should stay language-neutral. Language folders should hold language-specific examples, questions, and taxonomy details.

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

## Definition of Done for the Initial Commit

The initial repository should be considered ready when it contains:

- this `AGENT.md`,
- a human-facing `README.md`,
- the fixed Python question sheet,
- the adaptive question guide,
- a pattern index,
- several Python pattern examples,
- a profile taxonomy draft,
- a session record template,
- a `CodeStyle.md` template,
- and an empty `records/` folder with a short README.

After those files exist, a user should be able to ask an AI agent to run a CodeBTI interview and receive a useful project-specific `CodeStyle.md`.
