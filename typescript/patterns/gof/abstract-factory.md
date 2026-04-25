# Abstract Factory

## Pattern Intent

Produce families of related or dependent objects without specifying their concrete classes.

## TypeScript Shape

Abstract factories in TypeScript use `interface` or `abstract class` to declare product creation methods. Concrete factories implement those methods and return typed instances.

```typescript
// Abstract products
interface DB { connect(): void; }
interface FS { readFile(path: string): Promise<string>; }

// Abstract factory
interface EnvironmentFactory {
  getDB(): DB;
  getFS(): FS;
}

// Concrete factory
class ProdFactory implements EnvironmentFactory {
  getDB(): DB { return new MySQLDB(); }
  getFS(): FS { return new S3FS(); }
}
```

## When This Style Fits

- The project has families of related objects (e.g., database + cache + logger) that must be consistent.
- Environments or configuration tiers require different concrete implementations.
- Testing needs to swap entire infrastructure stacks.

## When To Avoid

- Only one concrete factory variant exists — an abstract factory adds indirection without benefit.
- Simple factory functions or dependency injection can solve the problem with less code.
- The "family" is really just one product — do not create fake families.

## CodeBTI Signals

The user prefers swappable infrastructure implementations and may be building multi-environment applications. This suggests a preference for [Strategy](../strategy.md)-like flexibility across the whole dependency graph.

## Agent Guidance

Default to dependency injection with explicit interfaces. Use Abstract Factory when the project explicitly needs to swap families of related dependencies across environments or configurations.

## Related Patterns

[Factory Method](../factory-method.md), [Strategy](../strategy.md), [Facade](../facade.md).

## Source Reference

- Examples: [Conceptual](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/AbstractFactory/Conceptual/index.ts), [RealWorld](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/AbstractFactory/RealWorld/index.ts)
- Catalog: https://refactoring.guru/design-patterns/abstract-factory
