# Decorator

## Pattern Intent

Attach additional responsibilities to objects dynamically. Decorators provide a flexible alternative to subclassing for extending functionality.

## TypeScript Shape

TypeScript decorators use either the experimental decorator syntax (`@decorator`) or a composition-based approach (composition wrapper class). The composition approach is more portable and idiomatic.

```typescript
interface Component {
  operation(): string;
}

class ConcreteComponent implements Component {
  operation(): string { return 'ConcreteComponent'; }
}

// Base decorator
class Decorator implements Component {
  constructor(protected component: Component) {}
  operation(): string { return this.component.operation(); }
}

// Concrete decorators
class ConcreteDecoratorA extends Decorator {
  operation(): string { return `ConcreteDecoratorA(${super.operation()})`; }
}

class ConcreteDecoratorB extends Decorator {
  operation(): string { return `ConcreteDecoratorB(${super.operation()})`; }
}

// Client usage
const component = new ConcreteDecoratorB(new ConcreteDecoratorA(new ConcreteComponent()));
```

Note: TypeScript's decorator syntax is experimental. Use the composition approach for portable, framework-agnostic code.

## When This Style Fits

- Adding behaviors to objects without modifying their class.
- Behaviors that can be added or removed at runtime.
- Combination of behaviors that should be stackable and ordered.

## When To Avoid

- Only one decoration is ever needed — modify the class directly.
- The decoration logic is trivial and the pattern adds ceremony without benefit.
- A simple function wrapper achieves the same goal.

## CodeBTI Signals

The user prefers composition over inheritance and is comfortable wrapping behavior. This appears in middleware stacks, logging/telemetry layers, and UI component enhancement.

## Agent Guidance

Prefer functional composition (wrapping functions) or class composition over experimental decorators. Use decorators only if the project already uses a framework that requires them (e.g., Angular).

## Related Patterns

[Chain of Responsibility](../chain-of-responsibility.md) (similar structure, different intent), [Strategy](../strategy.md), [Proxy](../proxy.md).

## Source Reference

- Examples: [Conceptual](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Decorator/Conceptual/index.ts), [RealWorld](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Decorator/RealWorld/index.ts)
- Catalog: https://refactoring.guru/design-patterns/decorator
