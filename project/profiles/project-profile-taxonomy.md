# Project Profile Taxonomy

This taxonomy defines project-level CodeBTI profile families. These profiles describe workflow and governance preferences, not language style.

## Controlled Multi-Language Maintainer

Signals:
- Prefers shared project defaults with explicit language overrides.
- Wants recorded decisions, validation checks, and centralized guidance.
- Often chooses per-language sections inside one project-level output.

Preferred project shape:
- Shared rules first, language-specific sections second.
- One live session record with project and language rounds.
- Validation checks before generated guidance is considered stable.

Risks:
- Too much process for small experiments.
- Duplicated shared rules inside language sections.

Guidance:
- Keep cross-cutting policy in the project layer.
- Let language packs override only with a recorded reason.
- Require link and structure validation before publishing generated docs.

## Lightweight Prototype Collaborator

Signals:
- Prefers direct edits, minimal notes, and a single `CodeStyle.md`.
- Accepts manual verification and low process overhead.
- Often chooses minimal dependency governance.

Preferred project shape:
- Few generated files.
- Brief assumptions and manual verification notes.
- Add gates only after the project stabilizes.

Risks:
- Harder recovery after long agent sessions.
- Inconsistent rules if the project grows quickly.

Guidance:
- Keep records concise but preserve enough context for recovery.
- Add validation once repeated edits or multiple languages appear.

## Review-Gated Integrator

Signals:
- Prefers pull requests, CI-required checks, and reviewer-friendly history.
- Wants validation gates to block unstable changes.
- Often chooses lockfile discipline and structured outputs.

Preferred project shape:
- Branch/PR workflow.
- CI validation for links, question structure, and manifest drift.
- Clear review checklist in generated guidance.

Risks:
- Slow iteration from excessive gates.
- Process may outgrow project size.

Guidance:
- Keep checks fast and deterministic.
- Require agents to report validation results in final responses.

## Release-Managed Steward

Signals:
- Prefers milestones, release notes, migration notes, and auditable history.
- Wants stable compatibility across generated docs and language packs.
- Often chooses full session evidence and release-quality validation.

Preferred project shape:
- Versioned documentation changes.
- Release checklist for language-pack or shared-contract changes.
- Examples updated when behavior changes.

Risks:
- Heavy maintenance burden.
- Slower content iteration.

Guidance:
- Reserve release-managed workflow for shared contracts, public templates, and language-pack schema changes.
- Keep small wording fixes on a lighter path.
