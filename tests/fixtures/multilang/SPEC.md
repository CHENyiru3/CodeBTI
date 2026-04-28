# Task Tracker SPEC

Project:
Python + TypeScript task tracker fixture

Source CodeBTI session:
[Recording.md](Recording.md)

Project profile:
Controlled Multi-Language Maintainer with Review-Gated Integrator traits

Language profile(s):
Python Data-First Validator; TypeScript Interface-First Boundary Keeper

Evidence rule:
Every requirement below must be traceable to the session record or listed under `Open Questions`.

## Mission

Help a small team track tasks across a Python service layer and a TypeScript client without losing project intent between agent sessions.

## Goals

- Create a basic task workflow with reviewable API and client boundaries.
- Preserve project intent and validation expectations across future agent sessions.

## Target Audience

Primary users:
Developers and maintainers coordinating small project tasks.

Secondary users or stakeholders:
Future agents that need recoverable context before changing the project.

## Constraints

Hard constraints:
Use controlled agent changes, CI-required checks, and lockfile discipline.

Soft preferences:
Avoid selecting an API framework or UI framework until feature planning needs it.

## Non-Goals

- Real-time collaboration is out of scope for the first pass.
- Plugin marketplace behavior is out of scope for the first pass.

## Tech Stack

Known stack decisions:
Python service/API layer and TypeScript browser client.

Stack assumptions:
API and UI frameworks remain open questions.

## Roadmap

Phase 1:
Task CRUD and shared project guidance.

Phase 2:
Richer client flows and boundary validation.

Later:
External integrations after the core workflow stabilizes.

## Summary

Build a small task tracker whose initial architecture preserves project intent and keeps Python/TypeScript boundaries explicit.

## Requirements

- Record task behavior in a way that can be tested from both service and client boundaries.
- Keep generated guidance synchronized with `Recording.md`.

## Shared Project Rules

Output shape:
One shared `CodeStyle.md` with project rules first and language sections below.

Validation gate:
Repository validation plus language behavior tests before handoff.

Dependency governance:
Use lockfile discipline and avoid framework choices until needed.

Recordkeeping:
Keep `Recording.md` and this `SPEC.md` aligned during replanning.

## Architecture Rules

Default structure:
Python service/API layer and TypeScript browser client.

Allowed abstractions:
Facades and adapters when they stabilize external or cross-language boundaries.

Disallowed patterns or styles:
Mutable singleton state and unrecorded framework decisions.

## Interfaces and Data

Public APIs:
Task service operations and client-facing API calls.

Data models:
Task payloads with boundary validation.

Validation boundaries:
Validate at API/client boundaries, keep internal code lighter.

## Error Handling

Use explicit result values for recoverable user-facing failures.

## Testing

Required scenarios:
Language behavior tests plus repository validation for documentation and generated guidance changes.

Acceptance checks:
Generated guidance links back to local profile and pattern references.

## Agent Implementation Notes

- Re-read `Recording.md` and this `SPEC.md` before feature planning.
- Update roadmap or open questions before implementing a new phase.

## Open Questions

- Which Python API framework should be used?
- Which TypeScript UI framework should be used?
