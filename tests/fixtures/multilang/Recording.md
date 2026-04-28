# CodeBTI Session Record

Date:
2026-04-28

Project slug:
python-typescript-task-tracker

Language targets:
Python, TypeScript

Interview status:
Complete fixture

Current step:
Generated outputs complete

Next question:
None

## Project Summary

A small task tracker with a Python API/service layer and a TypeScript browser client. The project values controlled agent changes, clear shared defaults, and enough validation to keep documentation and generated guidance stable.

## Opening SPEC Intake

Mission:
Help a small team track tasks across a Python service layer and a TypeScript client without losing project intent between agent sessions.

Goals:
Create a usable task workflow, keep API/client boundaries explicit, and preserve enough validation to make future changes reviewable.

Target audience:
Developers and maintainers using the tracker for small project coordination.

Constraints:
Prefer controlled agent changes, CI-required checks, and lockfile discipline. Avoid framework decisions until the feature scope needs them.

Likely tech stack or language targets:
Python service/API layer and TypeScript browser client.

Roadmap intent:
Phase 1 creates task CRUD and shared guidance; Phase 2 adds richer client flows; later phases can add integrations.

Non-goals:
No real-time collaboration or plugin marketplace in the first pass.

Open questions:
API framework and UI framework are intentionally unspecified until feature planning.

Initial SPEC draft:
[SPEC.md](SPEC.md)

## Interview Rounds

| Round | Scope | Source | Status |
| --- | --- | --- | --- |
| Opening | Project | Required SPEC-style opening prompt | Complete |
| Project fixed questions | Project | `../../../project/questions/fixed-project.md` | Complete |
| Python fixed questions | Language:Python | `../../../python/questions/fixed-python.md` | Complete |
| TypeScript fixed questions | Language:TypeScript | `../../../typescript/questions/fixed-typescript.md` | Complete |
| Adaptive questions | Project, Language, Cross-language | `../../../shared/questions/adaptive-question-guide.md` | Complete |

## Question Card Snapshot Inventory

| Step | Question ID | Scope | Source |
| --- | --- | --- | --- |
| Opening | opening.spec-intake | Project | Required SPEC-style opening prompt |
| P1 | project.control.model | Project | `../../../project/questions/fixed-project.md` |
| P2 | project.output.shape | Project | `../../../project/questions/fixed-project.md` |
| P3 | project.validation.gate | Project | `../../../project/questions/fixed-project.md` |
| P4 | project.shared-language.boundary | Project | `../../../project/questions/fixed-project.md` |
| P5 | project.dependency.governance | Project | `../../../project/questions/fixed-project.md` |
| P6 | project.change-record.policy | Project | `../../../project/questions/fixed-project.md` |
| Python Q1 | python.default.shape | Language:Python | `../../../python/questions/fixed-python.md` |
| Python Q2 | python.typing.boundaries | Language:Python | `../../../python/questions/fixed-python.md` |
| Python Q3 | python.error.recovery | Language:Python | `../../../python/questions/fixed-python.md` |
| Python Q4 | python.naming.readability | Language:Python | `../../../python/questions/fixed-python.md` |
| Python Q5 | python.architecture.wiring | Language:Python | `../../../python/questions/fixed-python.md` |
| Python Q6 | python.folder.structure | Language:Python | `../../../python/questions/fixed-python.md` |
| Python Q7 | python.testing.philosophy | Language:Python | `../../../python/questions/fixed-python.md` |
| Python Q8 | python.comments.docstrings | Language:Python | `../../../python/questions/fixed-python.md` |
| Python Q9 | python.git.collaboration | Language:Python | `../../../python/questions/fixed-python.md` |
| Python Q10 | python.dependencies.environments | Language:Python | `../../../python/questions/fixed-python.md` |
| TypeScript Q1 | typescript.default.shape | Language:TypeScript | `../../../typescript/questions/fixed-typescript.md` |
| TypeScript Q2 | typescript.typing.boundaries | Language:TypeScript | `../../../typescript/questions/fixed-typescript.md` |
| TypeScript Q3 | typescript.error.recovery | Language:TypeScript | `../../../typescript/questions/fixed-typescript.md` |
| TypeScript Q4 | typescript.naming.readability | Language:TypeScript | `../../../typescript/questions/fixed-typescript.md` |
| TypeScript Q5 | typescript.architecture.wiring | Language:TypeScript | `../../../typescript/questions/fixed-typescript.md` |
| TypeScript Q6 | typescript.folder.structure | Language:TypeScript | `../../../typescript/questions/fixed-typescript.md` |
| TypeScript Q7 | typescript.testing.philosophy | Language:TypeScript | `../../../typescript/questions/fixed-typescript.md` |
| TypeScript Q8 | typescript.comments.docstrings | Language:TypeScript | `../../../typescript/questions/fixed-typescript.md` |
| TypeScript Q9 | typescript.git.collaboration | Language:TypeScript | `../../../typescript/questions/fixed-typescript.md` |
| TypeScript Q10 | typescript.dependencies.environments | Language:TypeScript | `../../../typescript/questions/fixed-typescript.md` |
| A1 | adaptive.boundary.validation | Cross-language | Generated adaptive question |
| A2 | adaptive.error.recovery | Cross-language | Generated adaptive question |
| A3 | adaptive.test.gate | Project | Generated adaptive question |
| A4 | adaptive.dependency.boundary | Project | Generated adaptive question |
| A5 | adaptive.debuggability | Cross-language | Generated adaptive question |

## Project Question Answers

| Question | Final answer | User note | Changed from |
| --- | --- | --- | --- |
| P1 | C | Review-gated changes with CI checks. | None |
| P2 | D | One `CodeStyle.md` with per-language sections. | None |
| P3 | C | CI-required validation. | None |
| P4 | B | Shared defaults with recorded language overrides. | None |
| P5 | C | Lockfile discipline per language. | None |
| P6 | C | Preserve full session evidence. | None |

## Language Question Answers

### Language: Python

Source question file:
../../../python/questions/fixed-python.md

Profile taxonomy:
../../../python/profiles/python-profile-taxonomy.md

| Question | Final answer | User note | Changed from |
| --- | --- | --- | --- |
| Q1 | C | Data-first API payloads. | None |
| Q2 | B | Type public boundaries. | None |
| Q3 | C | Explicit result values for recoverable API errors. | None |
| Q4 | C | Domain language for tasks and projects. | None |
| Q5 | B | Pass dependencies for testability. | None |
| Q6 | A | Feature folders for API domains. | None |
| Q7 | B | Integration-heavy API tests. | None |
| Q8 | B | Explain why, not what. | None |
| Q9 | B | Conventional branches. | None |
| Q10 | D | Use `uv` and lockfiles. | None |

### Language: TypeScript

Source question file:
../../../typescript/questions/fixed-typescript.md

Profile taxonomy:
../../../typescript/profiles/typescript-profile-taxonomy.md

| Question | Final answer | User note | Changed from |
| --- | --- | --- | --- |
| Q1 | B | Interfaces for public client contracts. | None |
| Q2 | C | Runtime validation at API boundaries. | None |
| Q3 | C | Use discriminated result unions. | None |
| Q4 | C | Product/domain vocabulary. | None |
| Q5 | B | Constructor/function dependency injection. | None |
| Q6 | A | Feature folders under client features. | None |
| Q7 | B | Integration tests for user flows. | None |
| Q8 | B | Comments explain constraints. | None |
| Q9 | B | Conventional branches. | None |
| Q10 | C | Strict lockfile/workspace discipline. | None |

## Adaptive Question Answers

| Question | Scope | Direction | Final answer | User note | Why asked |
| --- | --- | --- | --- | --- | --- |
| A1 | Cross-language | Data trust and validation | Validate at API/client boundaries. | Keep internal code lighter. | Python B and TypeScript C needed reconciliation. |
| A2 | Cross-language | Error and recovery style | Use explicit result objects for user-facing recoverable errors. | Exceptions remain for programmer errors. | Both languages selected result-like errors. |
| A3 | Project | Test and review strictness | CI must run repo validation plus language tests. | Manual notes for UI-only changes. | Project gate selected CI-required checks. |
| A4 | Project | Boundaries around outside tools | Wrap external APIs behind adapters. | Direct calls allowed in prototypes only. | Dependency governance selected lockfile discipline. |
| A5 | Cross-language | Debuggability | Prefer named pipeline stages over event flow. | Avoid opaque callback chains. | Both language rounds selected testable dependencies. |

## CodeBTI Result

Project profile name:
Controlled Multi-Language Maintainer with Review-Gated Integrator traits

Language profiles:

| Language | Profile name | Profile taxonomy reference |
| --- | --- | --- |
| Python | Data-First Validator with Test-First Integrator traits | `../../../python/profiles/python-profile-taxonomy.md` |
| TypeScript | Interface-First Boundary Keeper with Data-Model Type Aliaser traits | `../../../typescript/profiles/typescript-profile-taxonomy.md` |

## Generated Outputs

- `CodeStyle.md`: Generated at [CodeStyle.md](CodeStyle.md).
- `ProjectStyle.md`: Not generated separately; project rules are embedded in `CodeStyle.md`.
- `SKILL.md`: Not generated.
- `SPEC.md`: Initial draft generated at [SPEC.md](SPEC.md).

## Validation

Target project validation command:
`python -m pytest`

CodeBTI repository validation command, if this record is generated while maintaining CodeBTI itself:
`python3 scripts/validate_repo.py`

Validation result:
Fixture passes CodeBTI quality tests.

## Unresolved Assumptions

- API framework and UI framework are intentionally unspecified.
