# Facade

## Pattern Intent

Provide a simplified interface to a library, framework, or any other complex set of classes.

## TypeScript Shape

A TypeScript facade is typically a plain class or object that holds references to subsystem components and exposes a simplified, typed API.

```typescript
// Complex subsystems
class Subsystem1 {
  operation1(): string { return 'Subsystem1: Ready!'; }
  operationN(): string { return 'Subsystem1: Go!'; }
}
class Subsystem2 {
  operation1(): string { return 'Subsystem2: Get ready!'; }
  operationZ(): string { return 'Subsystem2: Fire!'; }
}

// Facade
class Facade {
  constructor(
    private subsystem1: Subsystem1 = new Subsystem1(),
    private subsystem2: Subsystem2 = new Subsystem2()
  ) {}

  operation(): string {
    let result = 'Facade initializes subsystems:\n';
    result += this.subsystem1.operation1() + '\n' + this.subsystem2.operation1() + '\n';
    result += 'Facade orders subsystems to perform the action:\n';
    result += this.subsystem1.operationN() + '\n' + this.subsystem2.operationZ();
    return result;
  }
}
```

## When This Style Fits

- Providing a simple API over a complex or layered subsystem.
- Structuring a system into layers where each layer has a single facade.
- Reducing dependencies between clients and implementation details.

## When To Avoid

- The subsystem is already simple — a facade adds indirection without benefit.
- Clients need full access to subsystem internals — do not hide what is needed.
- The facade becomes a "god object" that knows too much.

## CodeBTI Signals

The user values convenience over fine-grained control for common operations. This appears in API wrappers, CLI tool internals, and service layer abstractions.

## Agent Guidance

Default to simple facades over complex subsystems. Each facade should have a focused responsibility. Expose typed methods; do not return raw subsystem types.

## Related Patterns

[Abstract Factory](../abstract-factory.md) (can create facades), [Adapter](../adapter.md), [Mediator](../mediator.md).

## Source Reference

- Examples: [Conceptual](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Facade/Conceptual/index.ts), [RealWorld](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Facade/RealWorld/index.ts)
- Catalog: https://refactoring.guru/design-patterns/facade
