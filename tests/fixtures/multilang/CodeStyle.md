# CodeStyle

Project:
Python + TypeScript task tracker fixture

Generated from session record:
[Recording.md](Recording.md)

Primary CodeBTI profile:
Controlled Multi-Language Maintainer with Review-Gated Integrator traits

Secondary traits:
Python Data-First Validator; TypeScript Interface-First Boundary Keeper

## Project Intent

Build a task tracker with a Python service layer and a TypeScript client while keeping project rules explicit enough for future agent edits.

## Evidence Summary

Project answers used:
P1, P2, and P3 selected review-gated collaboration, one shared `CodeStyle.md`, and CI-required validation.

Language answers used:
Python answers prefer data-first boundary validation; TypeScript answers prefer interface-first client boundaries.

Adaptive answers used:
A1 and A3 clarified boundary validation and required repo/language checks before handoff.

## Shared Project Rules

Use one `CodeStyle.md` with shared rules first and language sections below. Shared rules control Git workflow, validation gates, dependency governance, and recordkeeping unless a language section explicitly overrides them.

Required gates:

- Run repository validation for documentation changes.
- Run language tests before behavior changes are considered complete.
- Keep session evidence in `Recording.md` or an archived dated record.

## Python Style Rules

Default shape:
Data-first API payloads with small service functions and explicit boundary typing.

Error handling:
Use explicit result values for recoverable user-facing failures. Raise exceptions for programmer errors and unexpected infrastructure failures.

Dependencies:
Use `uv`/lockfile discipline. Wrap external systems behind adapters when they affect tests or user-visible behavior.

## TypeScript Style Rules

Default shape:
Use interfaces for public client contracts and type aliases/discriminated unions for payloads and recoverable results.

Validation:
Validate API responses at the boundary before passing data into feature code.

Dependencies:
Use strict lockfile/workspace discipline. Prefer direct feature code until a boundary needs an adapter.

## Pattern Guidance

Encouraged patterns:

- Facade for stable project-facing service/client boundaries.
- Adapter for external API and storage dependencies.
- Strategy only when behavior has multiple real implementations.

Allowed with caution:

- Registry when plugin-like task behaviors appear.

Avoid by default:

- Singleton for mutable shared project state.

## References

- Project profile taxonomy: [../../../project/profiles/project-profile-taxonomy.md](../../../project/profiles/project-profile-taxonomy.md)
- Python profile taxonomy: [../../../python/profiles/python-profile-taxonomy.md](../../../python/profiles/python-profile-taxonomy.md)
- TypeScript profile taxonomy: [../../../typescript/profiles/typescript-profile-taxonomy.md](../../../typescript/profiles/typescript-profile-taxonomy.md)
- Python Facade guidance: [../../../python/patterns/gof/facade.md](../../../python/patterns/gof/facade.md)
- TypeScript Adapter guidance: [../../../typescript/patterns/gof/adapter.md](../../../typescript/patterns/gof/adapter.md)

## Testing Policy

Required tests:
Language behavior tests plus repository validation for documentation and generated guidance changes.

Optional tests:
End-to-end UI tests once the client workflow stabilizes.

Manual verification:
Record any manual UI checks in the final agent response.

## Git and Collaboration

Use conventional branches and review-gated changes. Commit messages should identify whether the change affects project rules, Python behavior, TypeScript behavior, or generated guidance.

## Agent Behavior

When writing code:
Respect shared project defaults first, then language-specific rules.

When reviewing code:
Check for hidden shared state, missing validation at external boundaries, dependency changes without lockfile updates, and generated docs that cite irrelevant pattern pages.

When uncertain:
Update the session record with the uncertainty and ask one focused question before changing policy.

## Open Assumptions

- API framework and UI framework are intentionally unspecified.
