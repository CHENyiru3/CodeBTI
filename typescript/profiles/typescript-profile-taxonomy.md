# TypeScript Profile Taxonomy

This taxonomy defines practical TypeScript CodeBTI profile families. Profiles can be combined when the user's answers are mixed, for example `Interface-First Boundary Keeper with Algorithm-First Minimalist traits`.

## Interface-First Boundary Keeper

Signals:
- Prefers `interface` declarations and explicit contracts over class hierarchies.
- Likes dependency injection, clear module boundaries, and typed public APIs.
- Comfortable with standalone functions and utility types.

Preferred code shape:
- Interfaces define what modules expose.
- Classes or factory functions implement the behavior behind those interfaces.
- External tools are wrapped behind typed adapters or facades.

Risks:
- Too many small interfaces before variation is real.
- Interfaces on internal code that never varies.

CodeStyle guidance:
- Use `interface` for public contracts that may have multiple implementations.
- Prefer `type` aliases for data shapes, unions, and mapped types.
- Keep interfaces focused on the boundary; avoid interface-only-for-namespacing.

## Class-Centered State Architect

Signals:
- Prefers classes with encapsulated state, access modifiers, and method composition.
- Likes inheritance hierarchies, abstract base classes, or mixins.
- Comfortable with `private`, `protected`, `readonly`, and constructor injection.

Preferred code shape:
- Domain objects own meaningful state and behavior.
- Subclasses or mixins provide variation.
- External tools are composed through class extension or decorator-like wrappers.

Risks:
- Deep inheritance trees become brittle.
- Testing class hierarchies requires careful mock setups.

CodeStyle guidance:
- Use classes for domain concepts with behavior that genuinely benefits from encapsulation.
- Prefer composition over inheritance for variation.
- Keep class public surfaces typed and tested.

## Data-Model Type Aliaser

Signals:
- Prefers `type` aliases, utility types, readonly modifiers, and discriminated unions.
- Likes Zod, Yup, or similar runtime validation at module boundaries.
- Comfortable with mapped types, conditional types, and template literal types.

Preferred code shape:
- Data shapes are defined as `type` or `interface` at the boundary.
- Business logic operates on those typed shapes.
- Validation happens at the entry point, not scattered through the domain.

Risks:
- Over-modeling internal data with types that never vary.
- Validation logic leaking across layer boundaries.

CodeStyle guidance:
- Define data models for important types crossing module or IO boundaries.
- Use utility types (`Partial`, `Required`, `Readonly`, `Pick`, `Omit`) for transformations.
- Prefer `readonly` on data that should not be mutated.

## Functional Pipeline Builder

Signals:
- Prefers standalone functions, pure transformations, and explicit data flow.
- Likes `async/await` pipelines, array method chaining, and result objects.
- Comfortable avoiding classes for primary logic.

Preferred code shape:
- Small, typed, composable functions.
- Data passed explicitly, not through `this`.
- Pipeline stages named clearly.

Risks:
- Passing too many loose objects or arrays without type safety.
- Long chains that are hard to debug.

CodeStyle guidance:
- Keep functions small and typed at boundaries.
- Name pipeline stages clearly.
- Use `Result<T, E>` or similar discriminated unions instead of throwing for recoverable errors.

## Framework-Aligned Builder

Signals:
- Prefers framework or tool conventions for folder layout, dependency management, and project structure.
- Values ecosystem compatibility over custom architecture.
- Comfortable with decorators, framework-specific patterns, and conventions.

Preferred code shape:
- Follow the selected framework's expected layout.
- Keep local abstractions thin unless framework boundaries are insufficient.
- Use framework-native configuration and testing patterns.

Risks:
- Fighting the framework with custom patterns.
- Lock-in without explicit reason.

CodeStyle guidance:
- Follow framework conventions first.
- Add adapters only where external services or project-specific rules need isolation.
- Document deviations from the framework.

## Test-First Integrator

Signals:
- Prefers broad test coverage, integration tests, strict boundaries, or CI-friendly workflows.
- Often chooses dependency injection, adapters, and conventional Git practices.
- Comfortable with `interface` mocking and test doubles.

Preferred code shape:
- Dependencies can be replaced in tests.
- External systems sit behind clear boundaries.
- New behavior includes tests alongside implementation.

Risks:
- Slow iteration from too much test scaffolding.
- Mock-heavy tests that do not protect real behavior.

CodeStyle guidance:
- Require tests for public behavior and important failure paths.
- Prefer integration tests at stable boundaries.
- Keep test doubles close to the adapter or interface they replace.

## Algorithm-First Minimalist

Signals:
- Prefers performance, direct APIs, data structures, and low dependency count.
- Often chooses algorithm-first architecture and tests around core logic.
- Comfortable with `any` where the type is genuinely unknown and `unknown` where the type is checked at runtime.

Preferred code shape:
- Functions are close to the data structures they operate on.
- Abstractions are added only when they remove real complexity.
- Dependencies are avoided unless they clearly improve correctness or speed.

Risks:
- Under-documenting non-obvious algorithms.
- Ignoring integration and user-facing failure modes.

CodeStyle guidance:
- Keep hot paths direct and measurable.
- Explain algorithm choices when they are not obvious.
- Add focused tests for edge cases and complexity-sensitive behavior.

## Pragmatic Script Builder

Signals:
- Prefers flat procedural flow and low ceremony.
- Values speed, readable helpers, and minimal structure.
- Often chooses simple dependency management and light testing.

Preferred code shape:
- Few files at first.
- Direct functions and module constants.
- Refactor only when repetition or confusion appears.

Risks:
- Hidden shared state.
- Hard-to-scale modules if project grows quickly.

CodeStyle guidance:
- Start simple, but set clear thresholds for extraction.
- Avoid global mutation unless the session record explicitly allows it.
- Add tests around core behavior before major refactors.
