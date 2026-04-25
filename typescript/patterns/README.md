# TypeScript Design Pattern Database

This database covers the classic GoF pattern catalog for TypeScript and adapts it for CodeBTI style inference.

Use each page to answer three questions:

1. Does this pattern match the user's project problem?
2. Does this pattern match the user's preferred coding style?
3. Should generated code actively use it, permit it, or avoid it?

## Creational Patterns

- [Abstract Factory](gof/abstract-factory.md)
- [Builder](gof/builder.md)
- [Factory Method](gof/factory-method.md)
- [Prototype](gof/prototype.md)
- [Singleton](gof/singleton.md)

## Structural Patterns

- [Adapter](gof/adapter.md)
- [Bridge](gof/bridge.md)
- [Composite](gof/composite.md)
- [Decorator](gof/decorator.md)
- [Facade](gof/facade.md)
- [Flyweight](gof/flyweight.md)
- [Proxy](gof/proxy.md)

## Behavioral Patterns

- [Chain of Responsibility](gof/chain-of-responsibility.md)
- [Command](gof/command.md)
- [Iterator](gof/iterator.md)
- [Mediator](gof/mediator.md)
- [Memento](gof/memento.md)
- [Observer](gof/observer.md)
- [State](gof/state.md)
- [Strategy](gof/strategy.md)
- [Template Method](gof/template-method.md)
- [Visitor](gof/visitor.md)

## TypeScript Guidance

Modern TypeScript often has simpler alternatives to classic class-heavy patterns: interfaces, utility types, readonly fields, arrow functions, dependency injection containers, and ES modules. Prefer the simplest shape that preserves the user's desired boundaries.

TypeScript-specific alternatives worth considering:

- **GoF class patterns** often become simpler with `interface` + plain object + factory functions.
- **Decorator pattern** has an experimental TypeScript implementation; functional composition is often clearer.
- **Observer pattern** is built into Node.js `EventEmitter` and can be replaced by typed event systems.
- **Singleton** is often replaced by module-level singletons, dependency injection scoping, or a simple class factory.
- **Strategy** is naturally expressed with `interface` + function implementations in TypeScript.

When generating a `CodeStyle.md`, translate each preferred pattern into enforceable rules:

- naming and module boundaries,
- typing policy,
- allowed abstraction depth,
- test shape,
- and review checks for overuse.

## Source Reference

All examples are adapted from [RefactoringGuru/design-patterns-typescript](https://github.com/RefactoringGuru/design-patterns-typescript) under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0.
