# CodeBTI

![CodeBTI Overview](https://i.imgur.com/annGWpK.jpeg)

> **简体中文** | [Chinese translation available](zh/) - [中文版入口](zh/README.md)

CodeBTI is a code-style version of MBTI for software projects. It helps a human and an AI agent choose consistent project workflow, coding style, design-pattern posture, testing policy, dependency policy, and collaboration rules before implementation starts.

CodeBTI is not a personality test. It is a practical interview and documentation system for generating project-specific guidance such as `CodeStyle.md`, `ProjectStyle.md`, `SKILL.md`, or `SPEC.md`.

## Install as a Skill

This repository can be installed directly as a Codex skill. Copy or install this repo into your Codex skills directory as `codebti`. The root [SKILL.md](SKILL.md) is the entry point.

## How It Works

For every project, CodeBTI now uses a controlled project-first flow:

1. The user answers one SPEC-style opening prompt covering mission, goals, audience, constraints, likely stack/languages, roadmap intent, non-goals, and open questions.
2. The agent starts a live `Recording.md` in the target project and records the opening answer as the project summary and SPEC intake.
3. The agent creates or updates an initial `SPEC.md` draft from [shared/templates/SPEC.template.md](shared/templates/SPEC.template.md), keeping it at the what/why level.
4. The agent asks the 6 fixed project questions from [project/questions/fixed-project.md](project/questions/fixed-project.md).
5. The agent asks the fixed questions for each selected language pack, such as [python/questions/fixed-python.md](python/questions/fixed-python.md) or [typescript/questions/fixed-typescript.md](typescript/questions/fixed-typescript.md).
6. Before each scored question, the agent saves the full user-facing question card in `Recording.md`; after each answer, it updates the answer log and gives short project-specific feedback.
7. The agent asks exactly 5 adaptive follow-up questions total using [shared/questions/adaptive-question-guide.md](shared/questions/adaptive-question-guide.md).
8. The agent rereads `Recording.md` and `SPEC.md` as the source of truth.
9. The agent infers a project profile from [project/profiles/project-profile-taxonomy.md](project/profiles/project-profile-taxonomy.md) and language profiles from the selected language taxonomies.
10. The agent selects only pattern/resource references that materially affect the guidance.
11. The agent generates project guidance using the selected language template for single-language projects, [project/templates/MultiLanguageCodeStyle.template.md](project/templates/MultiLanguageCodeStyle.template.md) for multi-language projects, optional [project/templates/ProjectStyle.template.md](project/templates/ProjectStyle.template.md), and optional shared SKILL/SPEC templates.

For an operational step-by-step version, use the [golden path workflow](docs/golden-path.md).

## Multi-Language Projects

For projects that use multiple languages, CodeBTI asks project-wide questions once and then asks one language-specific round per language. A single final `CodeStyle.md` should put shared rules first, then language-specific sections.

For multi-language projects, the agent should:

- Record which language each answer set belongs to in `Recording.md`.
- Use project-wide answers as the default for Git workflow, validation gates, dependency governance, output shape, and change records.
- Allow language-specific overrides only when the override is explicit and recorded.
- Reference the same `shared/` interview resources for all rounds.
- Use [project/templates/MultiLanguageCodeStyle.template.md](project/templates/MultiLanguageCodeStyle.template.md) only when more than one language pack is selected. Single-language projects keep using their language `CodeStyle.template.md`.

## Validation

This repository has a lightweight validation gate:

```sh
python3 scripts/validate_repo.py
python3 -m pytest
```

The checks validate local Markdown links, required pack files, fixed-question counts and sections, shared Chinese mirror coverage, `MANIFEST.md` drift, question ID/scope quality, template sections, and a multi-language fixture. GitHub Actions runs the same commands through [.github/workflows/validate.yml](.github/workflows/validate.yml).

See [CHANGELOG.md](CHANGELOG.md) for the current release-hardening baseline.

## Example

The [examples/](examples/) directory contains a completed CodeBTI run for a small Python GUI calculator.

- [examples/Recording.md](examples/Recording.md): full interview record with the project summary, 10 fixed answers, 5 adaptive answers, feedback, hidden inference notes, and final profile inference.
- [examples/CodeStyle.md](examples/CodeStyle.md): generated project style guide.

The example predates the project-wide round, but remains useful as a single-language record/output example.

## Repository Structure

```text
CodeBTI/
├── project/                   # project-wide interview pack
│   ├── questions/             # fixed-project.md + README
│   ├── profiles/              # project profile taxonomy
│   └── templates/             # ProjectStyle.template.md
│
├── shared/                    # shared across all packs
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
├── scripts/                   # validation scripts
├── .github/workflows/         # CI validation
├── docs/                      # operational workflow guides
├── examples/                  # completed interview example
├── zh/                        # Simplified Chinese translation
├── AGENT.md                   # agent guide
├── CHANGELOG.md               # release notes
├── MANIFEST.md                # file inventory
└── SKILL.md                   # installable skill entry point
```

**Project-wide vs shared vs language-specific:**

| Resource | Scope | Example |
|----------|-------|---------|
| Project fixed questions | Project-wide | `project/questions/fixed-project.md` |
| Project profile taxonomy | Project-wide | `project/profiles/project-profile-taxonomy.md` |
| Multi-language CodeStyle template | Project-wide | `project/templates/MultiLanguageCodeStyle.template.md` |
| Fixed language questions | Per language | `python/questions/fixed-python.md`, `typescript/questions/fixed-typescript.md` |
| Pattern pages | Per language | `python/patterns/gof/facade.md`, `typescript/patterns/gof/facade.md` |
| Language profile taxonomy | Per language | `python/profiles/python-profile-taxonomy.md` |
| CodeStyle template | Per language | `python/templates/CodeStyle.template.md` |
| Adaptive guide | Shared | `shared/questions/adaptive-question-guide.md` |
| Editorial guide | Shared | `shared/questions/editorial-guide.md` |
| Question format | Shared | `shared/questions/question-format.md` |
| Session record | Shared | `shared/records/session-record.template.md` |
| SKILL/SPEC templates | Shared | `shared/templates/SKILL.template.md`, `shared/templates/SPEC.template.md` |

## Language Coverage

Available packs:

- **Project** - [project/](project/): project-wide process and governance pack.
- **Python** - [python/](python/): full language pack with 10 fixed questions, 22 GoF pattern pages, and 7 profile families.
- **TypeScript** - [typescript/](typescript/): full language pack with 10 fixed questions, 22 GoF pattern pages, and 7 profile families.
- **Chinese** - [zh/](zh/): Simplified Chinese translation. `zh/shared/` is a translated mirror of the English shared layer.

Adding a new language pack:

1. Create a top-level directory, for example `rust/`.
2. Add `questions/fixed-rust.md` with fixed language-specific questions.
3. Add `patterns/gof/` with pattern pages in Rust idioms.
4. Add `profiles/rust-profile-taxonomy.md`.
5. Add `templates/CodeStyle.template.md` with Rust-specific sections.
6. Reference `shared/` for adaptive guide, editorial rules, session record, and SKILL/SPEC templates. Do not copy shared files into the language pack.
7. Update this README, [AGENT.md](AGENT.md), and [MANIFEST.md](MANIFEST.md).
8. Run `python3 scripts/validate_repo.py` and `python3 -m pytest`.

## Output

The main output is a project-specific `CodeStyle.md`. When useful, the same result can be distilled into:

- `ProjectStyle.md` for project-wide workflow and governance rules,
- `SKILL.md` for reusable agent behavior,
- `SPEC.md` for project requirements,
- narrower specs such as `API_SPEC.md`, `TESTING_SPEC.md`, or `ARCHITECTURE_SPEC.md`.

For multi-language projects, generate a single `CodeStyle.md` from [project/templates/MultiLanguageCodeStyle.template.md](project/templates/MultiLanguageCodeStyle.template.md). Cross-cutting concerns apply to all languages unless a language section explicitly overrides them.

The live interview evidence is kept in `Recording.md` during the session. It includes full question cards, answer log, feedback, hidden inference notes, and final evidence review.

For SPEC-driven work, treat `SPEC.md` as a living what/why document. Between feature implementations, reread it, update mission, constraints, stack, roadmap, or open questions when they change, and record the replanning rationale in `Recording.md`.

## Contributing

Good contributions should preserve the controlled workflow:

- ask one question at a time,
- record the full question card before asking it,
- update `Recording.md` after every answer,
- ask 6 project questions, language fixed questions, and exactly 5 adaptive questions,
- infer the final profile from the completed session record,
- cite only references that materially affect the generated guidance,
- run `python3 scripts/validate_repo.py` and `python3 -m pytest` before submitting changes.
