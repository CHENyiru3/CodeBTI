# TypeScript Design Patterns

All 22 GoF design patterns adapted for TypeScript idioms and the CodeBTI style inference system.

## Creational Patterns

| Pattern | Intent | TypeScript Key Idea |
|---------|--------|--------------------|
| [Abstract Factory](abstract-factory.md) | Families of related objects | `interface` factory + `implements` |
| [Builder](builder.md) | Step-by-step construction | Fluent method chaining with `return this` |
| [Factory Method](factory-method.md) | Defer instantiation to subclasses | `abstract` creator + `implements` product |
| [Prototype](prototype.md) | Clone existing objects | `clone(): T` interface + spread operator |
| [Singleton](singleton.md) | One instance, global access | `private static #instance` + static getter |

## Structural Patterns

| Pattern | Intent | TypeScript Key Idea |
|---------|--------|--------------------|
| [Adapter](adapter.md) | Interface conversion | `implements` target + delegate to adaptee |
| [Bridge](bridge.md) | Separate abstraction from implementation | `interface` abstraction + `interface` implementation |
| [Composite](composite.md) | Tree structures | `abstract class` with children array |
| [Decorator](decorator.md) | Attach behaviors dynamically | Composition wrapper class (prefer over `@decorator`) |
| [Facade](facade.md) | Simplified subsystem access | Plain class with typed methods |
| [Flyweight](flyweight.md) | Share fine-grained objects | Factory + intrinsic/extrinsic state split |
| [Proxy](proxy.md) | Controlled access to objects | Same interface as real subject |

## Behavioral Patterns

| Pattern | Intent | TypeScript Key Idea |
|---------|--------|--------------------|
| [Chain of Responsibility](chain-of-responsibility.md) | Pass requests along a handler chain | `interface Handler<T>` + `setNext()` |
| [Command](command.md) | Encapsulate requests as objects | `interface Command { execute(): void }` |
| [Iterator](iterator.md) | Sequential access without exposure | `Symbol.iterator` + `Iterator<T>` |
| [Mediator](mediator.md) | Centralized component communication | `interface Mediator` + typed notifications |
| [Memento](memento.md) | Save and restore state snapshots | `Memento<T>` interface + caretaker |
| [Observer](observer.md) | One-to-many dependency notifications | `Subject`/`Observer` interfaces or `EventEmitter` |
| [State](state.md) | Object behavior changes with state | `abstract class State` + `Context` |
| [Strategy](strategy.md) | Swappable algorithms | `interface Strategy` + `Context` |
| [Template Method](template-method.md) | Algorithm skeleton with customizable steps | `abstract class` + `protected` methods + hooks |
| [Visitor](visitor.md) | Separate operations from object structure | Double dispatch with `accept(visitor)` |

## TypeScript Alternatives to GoF Patterns

Many GoF patterns are simpler in TypeScript due to its type system:

- **Singleton**: use a module-level exported object or a simple factory function
- **Strategy**: use function-typed fields: `strategy: (data: T) => U`
- **Observer**: use `EventEmitter` from Node.js or a typed event library
- **Decorator**: use composition wrappers instead of experimental `@decorator` syntax
- **Iterator**: use built-in `Symbol.iterator` and `for...of` loops
