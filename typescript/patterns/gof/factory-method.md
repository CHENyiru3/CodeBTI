# Factory Method

## Pattern Intent

Define an interface for creating an object, but let subclasses decide which class to instantiate. Factory Method lets a class defer instantiation to subclasses.

## TypeScript Shape

TypeScript factory methods use `abstract class` or `interface` for the creator and typed return values. Subclasses implement the factory method to return concrete product types.

```typescript
interface Product {
  operation(): string;
}

abstract class Creator {
  abstract factoryMethod(): Product;
  someOperation(): string {
    const product = this.factoryMethod();
    return `Creator: worked with ${product.operation()}`;
  }
}

class ConcreteCreator1 extends Creator {
  factoryMethod(): Product { return new ConcreteProduct1(); }
}

class ConcreteProduct1 implements Product {
  operation(): string { return '{Result of the ConcreteProduct1}'; }
}
```

## When This Style Fits

- A class cannot anticipate the type of objects it must create.
- Subclasses should specify the objects they create.
- Delegating responsibility to helper subclasses localizes knowledge of which product is created.

## When To Avoid

- Only one concrete product exists — the factory adds indirection.
- The creation logic is simple enough for a constructor call.
- Factory Method is used as a fancy name for a plain function — prefer a named factory function.

## CodeBTI Signals

The user prefers explicit object creation with controlled overrides. This appears in plugin systems, database connectors, and multi-backend architectures.

## Agent Guidance

Use Factory Method for creation that genuinely needs to be overridden by subclasses. Prefer simple named factory functions (`function createProduct(): Product`) when subclassing is not needed.

## Related Patterns

[Abstract Factory](../abstract-factory.md), [Builder](../builder.md), [Prototype](../prototype.md).

## Source Reference

- Examples: [Conceptual](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/FactoryMethod/Conceptual/index.ts), [RealWorld](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/FactoryMethod/RealWorld/index.ts)
- Catalog: https://refactoring.guru/design-patterns/factory-method
