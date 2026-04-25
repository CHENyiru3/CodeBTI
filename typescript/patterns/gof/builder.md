# Builder

## Pattern Intent

Construct complex objects step by step. The pattern allows producing different types and representations of an object using the same construction code.

## TypeScript Shape

TypeScript builders use `interface` for the builder contract and a fluent class method chain (`return this`) for step chaining. The director (optional) defines construction sequences.

```typescript
interface Builder {
  reset(): void;
  producePartA(): Builder;
  producePartB(): Builder;
  producePartC(): Builder;
  getProduct(): Product1;
}

class ConcreteBuilder1 implements Builder {
  private product = new Product1();
  reset() { this.product = new Product1(); }
  producePartA() { this.product.parts.push('PartA1'); return this; }
  producePartB() { this.product.parts.push('PartB1'); return this; }
  producePartC() { this.product.parts.push('PartC1'); return this; }
  getProduct(): Product1 { const p = this.product; this.reset(); return p; }
}

// Client usage
const builder = new ConcreteBuilder1();
builder.producePartA().producePartC().getProduct();
```

TypeScript's `class` with fluent method chaining is idiomatic. Generic builders with `Partial<T>` and `Required<T>` are also common.

## When This Style Fits

- Object construction has many optional parameters or steps.
- The same construction process should produce different representations.
- Validation needs to happen during construction, not after.

## When To Avoid

- Constructor arguments are few and required — do not add a builder for simple objects.
- The builder only forwards arguments to a constructor — use the constructor directly.
- The constructed object is a plain value object with no behavior.

## CodeBTI Signals

The user prefers step-by-step construction and may have complex domain objects. This pairs with [Factory Method](../factory-method.md) when construction has multiple stages.

## Agent Guidance

Use Builder for objects with complex initialization. Prefer TypeScript's fluent method chaining. Avoid builders for simple data objects that can use `type` aliases or constructor defaults.

## Related Patterns

[Factory Method](../factory-method.md), [Abstract Factory](../abstract-factory.md), [Composite](../composite.md) (sometimes used together for recursive structures).

## Source Reference

- Examples: [Conceptual](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Builder/Conceptual/index.ts), [RealWorld](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Builder/RealWorld/index.ts)
- Catalog: https://refactoring.guru/design-patterns/builder
