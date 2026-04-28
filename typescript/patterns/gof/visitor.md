# Visitor

## Pattern Intent

Separate algorithms from the objects on which they operate.

## TypeScript Shape

TypeScript visitors use `interface` for both the component and visitor contracts. The component declares `accept(visitor: Visitor)`, and each concrete visitor implements `visitConcreteComponentX` for each component type.

```typescript
interface Component {
  accept(visitor: Visitor): void;
}

interface Visitor {
  visitConcreteComponentA(element: ConcreteComponentA): void;
  visitConcreteComponentB(element: ConcreteComponentB): void;
}

class ConcreteComponentA implements Component {
  accept(visitor: Visitor): void { visitor.visitConcreteComponentA(this); }
  exclusiveMethod(): string { return 'A'; }
}

class ConcreteComponentB implements Component {
  accept(visitor: Visitor): void { visitor.visitConcreteComponentB(this); }
  specialMethod(): string { return 'B'; }
}

class ConcreteVisitor1 implements Visitor {
  visitConcreteComponentA(element: ConcreteComponentA): void {
    console.log(`${element.exclusiveMethod()} + ConcreteVisitor1`);
  }
  visitConcreteComponentB(element: ConcreteComponentB): void {
    console.log(`${element.specialMethod()} + ConcreteVisitor1`);
  }
}

// Usage
const components: Component[] = [new ConcreteComponentA(), new ConcreteComponentB()];
const visitor = new ConcreteVisitor1();
for (const comp of components) comp.accept(visitor);
```

## When This Style Fits

- Operations need to be added to objects in a closed set without modifying their classes.
- Related operations on a complex object structure need to be grouped.
- Cross-cutting operations (serialization, validation, rendering) on a type hierarchy.

## When To Avoid

- The set of component types is open and changing — each new type requires a new `visit` method in every visitor.
- Components already expose all necessary data — a simple function is sufficient.
- The visitor pattern adds complexity that is not justified by the benefit.

## CodeBTI Signals

The user is comfortable with double dispatch and wants operations separated from data. This appears in AST processors, document object models, and compilers.

## Agent Guidance

Use Visitor for operations on closed type hierarchies. Prefer simple functions or methods on the components when the set of types is stable. Avoid Visitor when new component types are expected to be added frequently.

## Related Patterns

[Composite](composite.md) (often traversed by Visitor).

## Source Reference

- Examples: [Conceptual](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Visitor/Conceptual/index.ts), [RealWorld](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Visitor/RealWorld/index.ts)
- Catalog: https://refactoring.guru/design-patterns/visitor
