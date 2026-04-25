# Singleton

## Pattern Intent

Ensure a class has only one instance and provide a global access point to it.

## TypeScript Shape

TypeScript singletons use `private` constructors and static accessors. Private class fields (`#instance`) or static properties with lazy initialization are both idiomatic.

```typescript
class Singleton {
  private static #instance: Singleton;

  private constructor() {}

  static get instance(): Singleton {
    if (!Singleton.#instance) {
      Singleton.#instance = new Singleton();
    }
    return Singleton.#instance;
  }

  someMethod(): void { /* ... */ }
}

// Usage
const s1 = Singleton.instance;
const s2 = Singleton.instance;
console.assert(s1 === s2); // true
```

Module-level singletons (a plain object exported from a file) are simpler and equally effective in TypeScript's ES module system.

## When This Style Fits

- Exactly one instance of a class is genuinely correct (e.g., a configuration manager, a connection pool, a logger).
- The instance is initialized once and never reconfigured.
- A global access point is acceptable for this specific resource.

## When To Avoid

- Multiple instances are needed in tests or different configurations.
- The singleton introduces hidden global state that complicates testing.
- Different parts of the application need different configurations of the same resource.

## CodeBTI Signals

The user accepts centralized infrastructure but may be trading testability for convenience. Prefer dependency injection over singleton when testability matters.

## Agent Guidance

Default to dependency injection or module-level constants. Use Singleton only when the generated `CodeStyle.md` explicitly allows process-global state. Document the singleton clearly and ensure it is thread-safe if used in async contexts.

## Related Patterns

[Abstract Factory](../abstract-factory.md), [Facade](../facade.md), [State](../state.md).

## Source Reference

- Examples: [Conceptual](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Singleton/Conceptual/index.ts), [RealWorld](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Singleton/RealWorld/index.ts)
- Catalog: https://refactoring.guru/design-patterns/singleton
