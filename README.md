# CodeBTI

![CodeBTI Overview](https://i.imgur.com/annGWpK.jpeg)

CodeBTI is a code-style version of MBTI for software projects. It helps a human and an AI agent choose a consistent Python coding style, design-pattern posture, testing policy, dependency policy, and collaboration workflow before implementation starts.

CodeBTI is not a personality test. It is a practical interview and documentation system for generating project-specific guidance such as `CodeStyle.md`, `SKILL.md`, or `SPEC.md`.

## Install as a Skill

This repository can be installed directly as a Codex skill. Copy or install this repo into your Codex skills directory as `codebti`. The root `SKILL.md` is the entry point.

## How It Works

1. The user describes the project.
2. The agent starts a live `Recording.md` in the target project and records the project summary.
3. The agent asks the 10 fixed Python questions in [python/questions/fixed-python.md](python/questions/fixed-python.md).
4. Before each question, the agent saves the full question card in `Recording.md`; after each answer, it updates the answer log and gives a short project-specific feedback response before asking the next question.
5. The agent asks exactly 5 adaptive follow-up questions using [python/questions/adaptive-question-guide.md](python/questions/adaptive-question-guide.md).
6. The agent rereads `Recording.md` as the source of truth.
7. The agent infers a Python style profile from [python/profiles/python-profile-taxonomy.md](python/profiles/python-profile-taxonomy.md).
8. The agent selects relevant local pattern/resource references, especially pages in [python/patterns/python/](python/patterns/python/).
9. The agent generates project guidance using the templates in [python/templates/](python/templates/), including a references section that explains why each cited pattern or resource matters.

## Example

The [example/](example/) directory contains a completed CodeBTI run for a small Python GUI calculator.

- [example/Recording.md](example/Recording.md): full interview record with the project summary, 10 fixed answers, 5 adaptive answers, feedback, hidden inference notes, and final profile inference.
- [example/CodeStyle.md](example/CodeStyle.md): generated project style guide.

The inferred profile is **Algorithm-First Minimalist with Object-Centered Boundary traits**. The resulting guidance recommends:

- a small `Calculator` object behind thin GUI handlers,
- direct expression/evaluation logic with a lightweight operation registry,
- explicit result objects for invalid user input,
- flat project structure until the code genuinely needs folders,
- core-logic tests for parsing, precedence, invalid input, and state transitions,
- minimal comments and light typing,
- `uv`, `pyproject.toml`, and `uv.lock` for dependency management.

## Repository Map

- [SKILL.md](SKILL.md): installable skill entry point for AI agents.
- [AGENT.md](AGENT.md): top-level agent guide and workflow reference.
- [example/](example/): completed Python GUI calculator CodeBTI example.
- [python/questions/](python/questions/README.md): fixed and adaptive interview guidance.
- [python/patterns/](python/patterns/README.md): Python design-pattern database with RefactoringGuru citations.
- [python/profiles/](python/profiles/README.md): profile inference rules and Python profile taxonomy.
- [python/records/](python/records/README.md): session recording rules and record template.
- [python/templates/](python/templates/README.md): output templates for generated project guidance.

## Current Scope

The initial version is Python-first. Future languages should add parallel question sheets, pattern databases, and profile taxonomies without changing the core interview flow.

## Output

The main output is a project-specific `CodeStyle.md`. When useful, the same result can be distilled into:

- `SKILL.md` for reusable agent behavior,
- `SPEC.md` for project requirements,
- narrower specs such as `API_SPEC.md`, `TESTING_SPEC.md`, or `ARCHITECTURE_SPEC.md`.

The live interview evidence is kept in `Recording.md` during the session. It includes the full question cards, answer log, feedback, hidden inference notes, and final evidence review. A project may keep that file as-is, copy it into `python/records/`, or rename it to a date-stamped session record after outputs are generated.
