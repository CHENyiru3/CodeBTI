# CodeBTI

![CodeBTI Overview](https://i.imgur.com/annGWpK.jpeg)

> **简体中文** | [Chinese translation available](zh/) — [中文版入口](zh/README.md)

CodeBTI is a code-style version of MBTI for software projects. It helps a human and an AI agent choose a consistent coding style, design-pattern posture, testing policy, dependency policy, and collaboration workflow before implementation starts.

CodeBTI is not a personality test. It is a practical interview and documentation system for generating project-specific guidance such as `CodeStyle.md`, `SKILL.md`, or `SPEC.md`.

## Install as a Skill

This repository can be installed directly as a Codex skill. Copy or install this repo into your Codex skills directory as `codebti`. The root `SKILL.md` is the entry point.

## How It Works — Single Language

For a project that uses one primary language:

1. The user describes the project and its language.
2. The agent starts a live `Recording.md` in the target project and records the project summary.
3. The agent asks the 10 fixed questions from the language's `questions/fixed-<lang>.md`.
4. Before each question, the agent saves the full question card in `Recording.md`; after each answer, it updates the answer log and gives a short project-specific feedback response before asking the next question.
5. The agent asks exactly 5 adaptive follow-up questions using `shared/questions/adaptive-question-guide.md`.
6. The agent rereads `Recording.md` as the source of truth.
7. The agent infers a style profile from the language's `profiles/<lang>-profile-taxonomy.md`.
8. The agent selects relevant pattern pages from `patterns/gof/` for that language.
9. The agent generates project guidance using `templates/CodeStyle.template.md` in the language pack.

## How It Works — Multi-Language

For a project that uses multiple languages (for example, a Python backend with a TypeScript frontend), the agent can run separate interview rounds per language:

1. **First round**: Select the primary or most complex language. Run the full 10 fixed + 5 adaptive question flow.
2. **Later rounds**: After the first `CodeStyle.md` is generated, run a shorter follow-up interview for the second language. Update `Recording.md` with the second language's answers. The agent can generate a second `CodeStyle.md` or merge the two into a single project `CodeStyle.md` that defines boundaries between languages.

For multi-language projects, the agent should:

- Record which language each answer set belongs to in `Recording.md`.
- Use the first language's `CodeStyle.md` as the default for cross-cutting concerns (Git workflow, dependency policy, test strategy).
- Use later rounds to add language-specific sections or override defaults.
- Reference the same `shared/` interview resources for both rounds — only the fixed question sheet and pattern pages are language-specific.

## Example

The [examples/](examples/) directory contains a completed CodeBTI run for a small Python GUI calculator.

- [examples/Recording.md](examples/Recording.md): full interview record with the project summary, 10 fixed answers, 5 adaptive answers, feedback, hidden inference notes, and final profile inference.
- [examples/CodeStyle.md](examples/CodeStyle.md): generated project style guide.

The inferred profile is **Algorithm-First Minimalist with Object-Centered Boundary traits**. The resulting guidance recommends:

- a small `Calculator` object behind thin GUI handlers,
- direct expression/evaluation logic with a lightweight operation registry,
- explicit result objects for invalid user input,
- flat project structure until the code genuinely needs folders,
- core-logic tests for parsing, precedence, invalid input, and state transitions,
- minimal comments and light typing,
- `uv`, `pyproject.toml`, and `uv.lock` for dependency management.

## Repository Structure

```
CodeBTI/
├── shared/                    # shared across all language packs
│   ├── questions/             # interview flow and editorial rules
│   ├── records/               # session recording template
│   └── templates/             # SKILL and SPEC output templates
│
├── python/                    # Python language pack
│   ├── questions/             # fixed-python.md + README
│   ├── patterns/gof/          # 22 GoF pattern pages for Python
│   ├── profiles/              # profile taxonomy
│   ├── records/               # README
│   └── templates/             # CodeStyle.template.md
│
├── typescript/                # TypeScript language pack
│   ├── questions/             # fixed-typescript.md + README
│   ├── patterns/gof/          # 22 GoF pattern pages for TypeScript
│   ├── profiles/              # profile taxonomy
│   ├── records/               # README
│   └── templates/             # CodeStyle.template.md
│
├── examples/                  # completed interview example
├── zh/                        # Simplified Chinese translation
├── AGENT.md                   # agent guide
├── MANIFEST.md                # file inventory
├── README.md                 # this file
└── SKILL.md                   # installable skill entry point
```

**Language-neutral vs language-specific:**

| Resource | Scope | Example |
|----------|-------|---------|
| Fixed questions | Per language | `python/questions/fixed-python.md`, `typescript/questions/fixed-typescript.md` |
| Pattern pages | Per language | `python/patterns/gof/facade.md`, `typescript/patterns/gof/facade.md` |
| Profile taxonomy | Per language | `python/profiles/python-profile-taxonomy.md` |
| CodeStyle template | Per language | `python/templates/CodeStyle.template.md` (has Python-specific sections) |
| Adaptive guide | **Shared** | `shared/questions/adaptive-question-guide.md` |
| Editorial guide | **Shared** | `shared/questions/editorial-guide.md` |
| Question format | **Shared** | `shared/questions/question-format.md` |
| Session record | **Shared** | `shared/records/session-record.template.md` |
| SKILL/SPEC templates | **Shared** | `shared/templates/SKILL.template.md`, `shared/templates/SPEC.template.md` |

## Language Coverage

Available language packs:

- **Python** — [python/](python/): full pack with 10 fixed questions, 22 GoF pattern pages, 7 profile families.
- **TypeScript** — [typescript/](typescript/): full pack with 10 fixed questions, 22 GoF pattern pages, 7 profile families.
- **Chinese** — [zh/](zh/): translated Python pack. `zh/shared/` mirrors the English shared layer.

Adding a new language pack:

1. Create a top-level directory, for example `rust/`.
2. Add `questions/fixed-rust.md` with 10 language-specific questions.
3. Add `patterns/gof/` with pattern pages in Rust idioms.
4. Add `profiles/rust-profile-taxonomy.md`.
5. Add `templates/CodeStyle.template.md` with Rust-specific sections.
6. Reference `shared/` for adaptive guide, editorial rules, session record, and SKILL/SPEC templates — do not copy them.
7. Update this README and `MANIFEST.md`.

## Output

The main output is a project-specific `CodeStyle.md`. When useful, the same result can be distilled into:

- `SKILL.md` for reusable agent behavior,
- `SPEC.md` for project requirements,
- narrower specs such as `API_SPEC.md`, `TESTING_SPEC.md`, or `ARCHITECTURE_SPEC.md`.

For multi-language projects, a single `CodeStyle.md` can contain language-specific sections. For example, Python section defines type discipline and exception policy; TypeScript section defines `interface` vs `type` usage and async patterns. Cross-cutting concerns (Git workflow, dependency policy, test strategy) apply to all languages unless overridden.

The live interview evidence is kept in `Recording.md` during the session. It includes the full question cards, answer log, feedback, hidden inference notes, and final evidence review. A project may keep that file as-is, copy it into the relevant language pack's `records/` directory, or rename it to a date-stamped session record after outputs are generated.

## Contributing

Contributions are welcome, especially new language packs, better interview questions, stronger profile taxonomies, clearer examples, and documentation improvements.

Good contributions should preserve the core workflow:

- ask one question at a time,
- record the full question card before asking it,
- update `Recording.md` after every answer,
- ask 10 fixed questions plus exactly 5 adaptive questions,
- infer the final profile from the completed session record,
- cite only references that materially affect the generated guidance.

For smaller changes, open a focused patch that explains the behavior or documentation problem being fixed. If a question, profile, or pattern page changes, include the reason the new wording improves future generated guidance.