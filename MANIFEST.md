# CodeBTI Repository Manifest

This file lists repository source files with one-line descriptions. High-volume translated GoF pattern catalogs may be represented by explicit directory entries.

## Root Files

| File | Description |
|------|-------------|
| `.gitignore` | Local generated artifact ignore rules. |
| `AGENT.md` | Agent guide and workflow reference. |
| `CHANGELOG.md` | Release notes and validation baseline. |
| `CONTRIBUTING.md` | Contribution rules and validation expectations. |
| `LICENSE` | MIT license. |
| `MANIFEST.md` | This file — repository file inventory. |
| `pyproject.toml` | Python test configuration and pytest optional dependency. |
| `README.md` | Human entry point and project overview. |
| `SKILL.md` | Installable Codex skill entry point. |

## Documentation (`docs/`)

Operational guides that explain how to run or review the workflow.

| File | Description |
|------|-------------|
| `docs/golden-path.md` | End-to-end CodeBTI session workflow from kickoff through validation and handoff. |

## Validation and Automation

Lightweight gates that keep the Markdown-first repository stable.

| File | Description |
|------|-------------|
| `.github/workflows/validate.yml` | GitHub Actions workflow that runs repository validation. |
| `scripts/validate_repo.py` | Standard-library validation script for links, pack structure, question quality, template sections, shared mirrors, and manifest drift. |
| `tests/test_validate_repo.py` | Pytest checks for validator behavior, release-hardening docs, templates, and fixtures. |
| `tests/fixtures/multilang/CodeStyle.md` | Multi-language generated guidance fixture. |
| `tests/fixtures/multilang/Recording.md` | Multi-language interview record fixture. |
| `tests/fixtures/multilang/SPEC.md` | Multi-language initial SPEC draft fixture. |

## Project Pack (`project/`)

Project-wide interview resources used before language-specific rounds.

| File | Description |
|------|-------------|
| `project/questions/README.md` | Project-wide interview flow guide. |
| `project/questions/fixed-project.md` | 6 fixed project questions for collaboration, validation, outputs, shared rules, dependencies, and records. |
| `project/profiles/README.md` | Project profile inference guide. |
| `project/profiles/project-profile-taxonomy.md` | Project-level workflow and governance profile families. |
| `project/templates/MultiLanguageCodeStyle.template.md` | Multi-language CodeStyle.md template with shared rules, language sections, and override policy. |
| `project/templates/ProjectStyle.template.md` | Project-level workflow and style output template. |

## Shared Layer (`shared/`)

Language-neutral interview resources used by all project and language packs.

| File | Description |
|------|-------------|
| `shared/questions/adaptive-question-guide.md` | Rules for selecting and phrasing 5 follow-up questions. |
| `shared/questions/editorial-guide.md` | Question-writing rules and topic sensitivity notes. |
| `shared/questions/question-format.md` | Standard card structure for every question. |
| `shared/questions/shared-architecture.md` | Multi-language design rationale and agent rules. |
| `shared/records/session-record.template.md` | Template for live and archived interview records. |
| `shared/templates/SKILL.template.md` | SKILL.md output template (language-neutral). |
| `shared/templates/SPEC.template.md` | SPEC.md output template (language-neutral). |

## Python Language Pack (`python/`)

### Questions

| File | Description |
|------|-------------|
| `python/questions/README.md` | Question framework guide and interview flow. |
| `python/questions/fixed-python.md` | 10 fixed Python interview questions with code examples. |

### Patterns — GoF Catalog (`python/patterns/gof/`)

| File | Description |
|------|-------------|
| `python/patterns/README.md` | Design pattern database index. |
| `python/patterns/gof/README.md` | Python GoF pattern index with RefactoringGuru citations. |
| `python/patterns/gof/abstract-factory.md` | Abstract Factory — families of related objects. |
| `python/patterns/gof/adapter.md` | Adapter — interface conversion. |
| `python/patterns/gof/bridge.md` | Bridge — separate abstraction from implementation. |
| `python/patterns/gof/builder.md` | Builder — step-by-step object construction. |
| `python/patterns/gof/chain-of-responsibility.md` | Chain of Responsibility — pass requests along a handler chain. |
| `python/patterns/gof/command.md` | Command — encapsulate requests as objects. |
| `python/patterns/gof/composite.md` | Composite — tree structures of parts and wholes. |
| `python/patterns/gof/decorator.md` | Decorator — attach behaviors dynamically. |
| `python/patterns/gof/facade.md` | Facade — simplified subsystem access. |
| `python/patterns/gof/factory-method.md` | Factory Method — defer instantiation to subclasses. |
| `python/patterns/gof/flyweight.md` | Flyweight — share fine-grained objects. |
| `python/patterns/gof/iterator.md` | Iterator — sequential access without exposure. |
| `python/patterns/gof/mediator.md` | Mediator — centralized component communication. |
| `python/patterns/gof/memento.md` | Memento — save and restore state snapshots. |
| `python/patterns/gof/observer.md` | Observer — one-to-many dependency notifications. |
| `python/patterns/gof/prototype.md` | Prototype — clone existing objects. |
| `python/patterns/gof/proxy.md` | Proxy — controlled access to objects. |
| `python/patterns/gof/singleton.md` | Singleton — one instance with global access. |
| `python/patterns/gof/state.md` | State — object behavior changes with internal state. |
| `python/patterns/gof/strategy.md` | Strategy — swappable algorithms. |
| `python/patterns/gof/template-method.md` | Template Method — algorithm skeleton with customizable steps. |
| `python/patterns/gof/visitor.md` | Visitor — separate operations from object structure. |

### Profiles

| File | Description |
|------|-------------|
| `python/profiles/README.md` | Profile inference rules and usage guide. |
| `python/profiles/python-profile-taxonomy.md` | 7 Python profile families (Object-Centered, Function-First, Data-First, etc.). |

### Records

| File | Description |
|------|-------------|
| `python/records/README.md` | Session recording rules and filename format. |

### Templates

| File | Description |
|------|-------------|
| `python/templates/README.md` | Output template inventory and usage guide. |
| `python/templates/CodeStyle.template.md` | CodeStyle.md output template with Python-specific sections. |

## TypeScript Language Pack (`typescript/`)

### Questions

| File | Description |
|------|-------------|
| `typescript/questions/README.md` | Question framework guide for TypeScript. |
| `typescript/questions/fixed-typescript.md` | 10 fixed TypeScript interview questions with code examples. |

### Patterns — GoF Catalog (`typescript/patterns/gof/`)

| File | Description |
|------|-------------|
| `typescript/patterns/README.md` | TypeScript design pattern database index. |
| `typescript/patterns/gof/README.md` | TypeScript GoF pattern index with RefactoringGuru citations. |
| `typescript/patterns/gof/abstract-factory.md` | Abstract Factory for TypeScript — interface factory + implements. |
| `typescript/patterns/gof/adapter.md` | Adapter for TypeScript — implements target + delegate to adaptee. |
| `typescript/patterns/gof/bridge.md` | Bridge for TypeScript — interface abstraction + interface implementation. |
| `typescript/patterns/gof/builder.md` | Builder for TypeScript — fluent method chaining. |
| `typescript/patterns/gof/chain-of-responsibility.md` | Chain of Responsibility for TypeScript — interface Handler + setNext(). |
| `typescript/patterns/gof/command.md` | Command for TypeScript — interface Command { execute(): void }. |
| `typescript/patterns/gof/composite.md` | Composite for TypeScript — abstract class with children array. |
| `typescript/patterns/gof/decorator.md` | Decorator for TypeScript — composition wrapper (prefer over @decorator). |
| `typescript/patterns/gof/facade.md` | Facade for TypeScript — plain class with typed methods. |
| `typescript/patterns/gof/factory-method.md` | Factory Method for TypeScript — abstract creator + implements product. |
| `typescript/patterns/gof/flyweight.md` | Flyweight for TypeScript — factory + intrinsic/extrinsic state split. |
| `typescript/patterns/gof/iterator.md` | Iterator for TypeScript — Symbol.iterator + Iterator<T>. |
| `typescript/patterns/gof/mediator.md` | Mediator for TypeScript — interface Mediator + typed notifications. |
| `typescript/patterns/gof/memento.md` | Memento for TypeScript — Memento<T> interface + caretaker. |
| `typescript/patterns/gof/observer.md` | Observer for TypeScript — Subject/Observer interfaces or EventEmitter. |
| `typescript/patterns/gof/prototype.md` | Prototype for TypeScript — clone(): T interface + spread operator. |
| `typescript/patterns/gof/proxy.md` | Proxy for TypeScript — same interface as real subject. |
| `typescript/patterns/gof/singleton.md` | Singleton for TypeScript — private static #instance + static getter. |
| `typescript/patterns/gof/state.md` | State for TypeScript — abstract class State + Context. |
| `typescript/patterns/gof/strategy.md` | Strategy for TypeScript — interface Strategy + Context. |
| `typescript/patterns/gof/template-method.md` | Template Method for TypeScript — abstract class + protected methods + hooks. |
| `typescript/patterns/gof/visitor.md` | Visitor for TypeScript — double dispatch with accept(visitor). |

### Profiles

| File | Description |
|------|-------------|
| `typescript/profiles/README.md` | TypeScript profile inference rules and usage guide. |
| `typescript/profiles/typescript-profile-taxonomy.md` | 7 TypeScript profile families (Interface-First, Class-Centered, Data-Model, etc.). |

### Records

| File | Description |
|------|-------------|
| `typescript/records/README.md` | TypeScript session recording rules. |

### Templates

| File | Description |
|------|-------------|
| `typescript/templates/README.md` | TypeScript output template inventory and usage guide. |
| `typescript/templates/CodeStyle.template.md` | CodeStyle.md output template with TypeScript-specific sections (interface vs type). |

## Examples (`examples/`)

| File | Description |
|------|-------------|
| `examples/CodeStyle.md` | Generated style guide for the Python GUI calculator example. |
| `examples/Recording.md` | Full interview record for the Python GUI calculator example. |

## Chinese Translation (`zh/`)

Simplified Chinese translation of the English documentation. Shared layer files are translated mirrors, and Python and TypeScript language packs are translated. The project pack remains English-only in this baseline.

### Root-level translated files

| File | Description |
|------|-------------|
| `zh/AGENT.md` | Chinese agent guide. |
| `zh/README.md` | Chinese entry point and overview. |
| `zh/SKILL.md` | Chinese skill entry point. |
| `zh/TRANSLATION_STATUS.md` | Translation maintenance guide for translated files and shared mirrors. |

### Shared layer (translated mirrors of `shared/`)

| File | Description |
|------|-------------|
| `zh/shared/questions/adaptive-question-guide.md` | Chinese mirror of `shared/questions/adaptive-question-guide.md`. |
| `zh/shared/questions/editorial-guide.md` | Chinese mirror of `shared/questions/editorial-guide.md`. |
| `zh/shared/questions/question-format.md` | Chinese mirror of `shared/questions/question-format.md`. |
| `zh/shared/questions/shared-architecture.md` | Chinese mirror of `shared/questions/shared-architecture.md`. |
| `zh/shared/records/session-record.template.md` | Chinese mirror of `shared/records/session-record.template.md`. |
| `zh/shared/templates/SKILL.template.md` | Chinese mirror of `shared/templates/SKILL.template.md`. |
| `zh/shared/templates/SPEC.template.md` | Chinese mirror of `shared/templates/SPEC.template.md`. |

### Chinese Python language pack (`zh/python/`)

| File | Description |
|------|-------------|
| `zh/python/questions/README.md` | Interview framework guide in Chinese. |
| `zh/python/questions/fixed-python.md` | 10 fixed Python questions in Chinese. |
| `zh/python/patterns/README.md` | Pattern database index in Chinese. |
| `zh/python/patterns/gof/` | 22 GoF pattern pages in Chinese. |
| `zh/python/profiles/README.md` | Profile inference guide in Chinese. |
| `zh/python/profiles/python-profile-taxonomy.md` | Chinese profile taxonomy. |
| `zh/python/records/README.md` | Session recording rules in Chinese. |
| `zh/python/templates/README.md` | Template guide in Chinese. |
| `zh/python/templates/CodeStyle.template.md` | Chinese CodeStyle output template. |

### Chinese TypeScript language pack (`zh/typescript/`)

| File | Description |
|------|-------------|
| `zh/typescript/questions/README.md` | Interview framework guide in Chinese. |
| `zh/typescript/questions/fixed-typescript.md` | 10 fixed TypeScript questions in Chinese. |
| `zh/typescript/patterns/README.md` | Pattern database index in Chinese. |
| `zh/typescript/patterns/gof/` | 22 GoF pattern pages in Chinese. |
| `zh/typescript/profiles/README.md` | Profile inference guide in Chinese. |
| `zh/typescript/profiles/typescript-profile-taxonomy.md` | Chinese TypeScript profile taxonomy. |
| `zh/typescript/records/README.md` | Session recording rules in Chinese. |
| `zh/typescript/templates/README.md` | Template guide in Chinese. |
| `zh/typescript/templates/CodeStyle.template.md` | Chinese TypeScript CodeStyle output template. |

### Chinese examples

| File | Description |
|------|-------------|
| `zh/examples/CodeStyle.md` | Chinese version of the example CodeStyle.md. |
