# CodeStyle

Project:
TODO: project name or short identifier.

Generated from session record:
TODO: path to `Recording.md` or archived record.

Generated from SPEC:
TODO: path to `SPEC.md` or archived SPEC.

Project CodeBTI profile:
TODO: project profile from `project/profiles/project-profile-taxonomy.md`.

Language CodeBTI profiles:
TODO: one profile per selected language.

Evidence rule:
Every rule below must be traceable to `Recording.md` or `SPEC.md`. If evidence is missing, write it under `Open Assumptions` instead of inventing a rule.

## Project Intent

Purpose:
TODO: one paragraph describing the project and why this shared style guide exists.

Primary constraints:
TODO: constraints from the opening SPEC intake and project answers.

Success signal:
TODO: how future agents should know a cross-language change fits the project.

## Evidence Summary

SPEC evidence used:
TODO: mission, goals, audience, constraints, roadmap, non-goals, and open questions that shaped this guidance.

Project answers used:
TODO: summarize P1-P6 decisions that control shared behavior.

Language answers used:
TODO: summarize the selected language rounds and any important differences.

Adaptive answers used:
TODO: summarize adaptive answers that changed cross-language guidance.

## Shared Project Rules

Output shape:
TODO: final artifacts and whether `ProjectStyle.md`, `SKILL.md`, or narrower specs are also generated.

Git and collaboration:
TODO: shared branching, review, commit, and handoff expectations.

Validation gate:
TODO: commands or manual checks required before cross-language changes are complete.

Dependency governance:
TODO: shared dependency rules plus language-specific package manager expectations.

Recordkeeping:
TODO: what must be preserved in `Recording.md`, `SPEC.md`, changelog, release notes, or review notes.

Language override policy:
TODO: when a language section may override a shared project rule.

## Cross-Language Contracts

Shared data contracts:
TODO: DTOs, schemas, API contracts, event shapes, generated types, or documents shared across languages.

Ownership:
TODO: which language, service, package, or document owns the canonical contract.

Validation boundaries:
TODO: where inputs are checked, normalized, rejected, or trusted across languages.

Failure and recovery:
TODO: shared policy for recoverable errors, partial success, retries, and user-facing warnings.

Privacy, security, and compliance:
TODO: cross-language rules for sensitive data, credentials, logging, audit, or external services.

## Language Sections

### Python

Profile:
TODO

Default code shape:
TODO

Typing and validation:
TODO

Error handling:
TODO

Testing:
TODO

Dependencies:
TODO

Overrides from shared rules:
TODO: list explicit overrides or write `None`.

### TypeScript

Profile:
TODO

Default code shape:
TODO

Typing and validation:
TODO

Error handling:
TODO

Testing:
TODO

Dependencies:
TODO

Overrides from shared rules:
TODO: list explicit overrides or write `None`.

### Other Languages

TODO: add one subsection per additional selected language. Do not add unused language sections.

## Conflict and Override Policy

Shared rule:
TODO

Language override:
TODO

Reason:
TODO

Affected files or packages:
TODO

Validation required:
TODO

## Pattern Guidance

Encouraged patterns:
TODO: local pattern pages to use and the concrete reason each applies.

Allowed with caution:
TODO: pattern pages that are acceptable only under stated constraints.

Avoid by default:
TODO: pattern pages to avoid and the project-specific reason.

Cross-language pattern notes:
TODO: where patterns differ by language or should stay hidden behind a shared contract.

## References

Project references:

- Project profile taxonomy: [../profiles/project-profile-taxonomy.md](../profiles/project-profile-taxonomy.md)
- ProjectStyle template: [ProjectStyle.template.md](ProjectStyle.template.md)
- SPEC template: [../../shared/templates/SPEC.template.md](../../shared/templates/SPEC.template.md)
- Session record template: [../../shared/records/session-record.template.md](../../shared/records/session-record.template.md)

Language references:

- TODO: link only to selected language profile taxonomies and pattern pages that materially affected the guidance.

Reference rules:

- Prefer local CodeBTI pattern pages for design-pattern guidance.
- Include only references that affected the generated recommendation.
- For each reference, explain the practical rule it supports in one sentence.
- Do not cite a pattern only because it was mentioned; cite it when it is encouraged, allowed with caution, or explicitly avoided.
- Keep references curated rather than exhaustive.

## Testing Policy

Required shared tests:
TODO: cross-language contract, integration, fixture, generated-type, or documentation checks.

Required language tests:
TODO: per-language checks or test commands.

Optional tests:
TODO: tests that become useful when risk or scope increases.

Manual verification:
TODO: manual checks required when automated coverage is insufficient.

## Git and Collaboration

Branching:
TODO: branch or checkpoint policy for multi-language changes.

Commit messages:
TODO: how commits should identify shared, Python, TypeScript, or generated-guidance changes.

Review checklist:
TODO: review questions future agents should apply to cross-language changes.

## Agent Behavior

When writing code:
TODO: concrete instructions for future coding agents.

When reviewing code:
TODO: concrete review posture and common cross-language risks.

When uncertain:
TODO: when to ask the user, record an assumption, or choose the shared project default.

## Examples

Preferred cross-language shape:

```text
TODO: minimal example of a shared contract and language-specific implementations.
```

Avoided cross-language shape:

```text
TODO: minimal example of duplicated or conflicting behavior to avoid.
```

## Open Assumptions

- TODO: unresolved or weakly evidenced assumption.
