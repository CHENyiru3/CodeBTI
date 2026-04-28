# CodeStyle

Project:
TODO: project name or short identifier.

Generated from session record:
TODO: path to `Recording.md` or archived record.

Project CodeBTI profile:
TODO: project profile from `project/profiles/project-profile-taxonomy.md`.

TypeScript CodeBTI profile:
TODO: primary TypeScript profile plus any secondary traits.

Evidence rule:
Every rule below must be traceable to the session record. If evidence is missing, write it under `Open Assumptions` instead of inventing a rule.

## Project Intent

Purpose:
TODO: one paragraph describing the project and why this style guide exists.

Primary constraints:
TODO: user-facing constraints such as correctness, speed, maintainability, learning, or delivery pressure.

Success signal:
TODO: how future agents should know a TypeScript change fits the project.

## Evidence Summary

Project answers used:
TODO: summarize the P1-P6 decisions that control shared behavior.

TypeScript answers used:
TODO: summarize Q1-Q10 decisions that shape TypeScript style.

Adaptive answers used:
TODO: summarize adaptive answers that changed or clarified the guidance.

## Shared Project Rules

Output shape:
TODO: required final artifacts and whether this file is single-language or part of a multi-language guide.

Git and collaboration:
TODO: branching, review, commit, and handoff expectations from project answers.

Validation gate:
TODO: exact commands or manual checks required before a change is complete.

Dependency governance:
TODO: when TypeScript dependencies may be added, replaced, or avoided.

Recordkeeping:
TODO: what must be preserved in `Recording.md`, changelog, release notes, or review notes.

Language override policy:
TODO: state whether TypeScript follows shared defaults or explicitly overrides them.

## Default Code Shape

Preferred organization:
TODO: module/package structure and where new code should live.

Module and folder rules:
TODO: naming, boundary, and import rules.

When to add abstraction:
TODO: evidence-backed triggers for interfaces, classes, functions, services, factories, or helpers.

When to keep code direct:
TODO: cases where plain functions, local types, or direct composition are preferred.

## TypeScript Style Rules

Naming:
TODO: naming conventions and exceptions.

Typing:
TODO: strictness, boundary typing, runtime validation, or flexible style.

Interfaces vs type aliases:
TODO: when to use `interface`, `type`, classes, discriminated unions, or generics.

Data modeling:
TODO: schema libraries, DTOs, plain objects, domain classes, or inferred types.

Error handling:
TODO: exception, result, fallback, and logging policy.

Async patterns:
TODO: promises, cancellation, retries, concurrency, and failure handling.

State management:
TODO: rules for mutable state, stores, context, singletons, and configuration.

Dependency management:
TODO: dependency policy specific to TypeScript tools and packages.

Comments and docstrings:
TODO: where comments/JSDoc are required, optional, or discouraged.

## Pattern Guidance

Encouraged patterns:
TODO: local pattern pages to use and the concrete reason each applies.

Allowed with caution:
TODO: pattern pages that are acceptable only under stated constraints.

Avoid by default:
TODO: pattern pages to avoid and the project-specific reason.

Pattern references:
TODO: curated links to the relevant local pages in `typescript/patterns/gof/`.

## References

Design pattern references:

- Encouraged: TODO. Link to the relevant local page in `typescript/patterns/gof/` and state why it applies.
- Allowed with caution: TODO. Link to the relevant local page in `typescript/patterns/gof/` and state the constraint.
- Avoid by default: TODO. Link to the relevant local page in `typescript/patterns/gof/` and state why it should usually be avoided for this project.

Useful project resources:

- TODO: Link to relevant local templates, profile taxonomy entries, framework docs, or library docs used to justify the guidance.

Reference rules:

- Prefer local CodeBTI pattern pages for design-pattern guidance.
- Include only references that affected the generated recommendation.
- For each reference, explain the practical rule it supports in one sentence.
- Do not cite a pattern only because it was mentioned; cite it when it is encouraged, allowed with caution, or explicitly avoided.
- Keep references curated rather than exhaustive.

## Testing Policy

Required tests:
TODO: exact TypeScript test types or commands expected before handoff.

Optional tests:
TODO: tests that are useful when risk or scope increases.

Manual verification:
TODO: manual checks required when automated coverage is insufficient.

## Git and Collaboration

Branching:
TODO: branch or checkpoint policy for TypeScript changes.

Commit messages:
TODO: message style and required evidence.

Review checklist:
TODO: review questions future agents should apply to TypeScript changes.

## Agent Behavior

When writing code:
TODO: concrete instructions for future coding agents.

When reviewing code:
TODO: concrete review posture and common risks.

When uncertain:
TODO: when to ask the user, record an assumption, or choose the project default.

## Examples

Preferred code shape:

```typescript
// TODO: minimal example that demonstrates the preferred TypeScript style.
```

Avoided code shape:

```typescript
// TODO: minimal example that shows what future agents should avoid.
```

## Open Assumptions

- TODO: unresolved or weakly evidenced assumption.
