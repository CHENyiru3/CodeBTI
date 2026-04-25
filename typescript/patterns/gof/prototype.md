# Prototype

## Pattern Intent

Specify the kinds of objects to create using a prototypical instance, and create new objects by copying this prototype.

## TypeScript Shape

TypeScript prototypes use an interface with a `clone` method. TypeScript's spread operator (`{ ...obj }`) and `Object.assign` simplify shallow copying. Deep cloning requires careful handling of nested references.

```typescript
interface Cloneable<T> {
  clone(): T;
}

class Document implements Cloneable<Document> {
  components: ComponentPrototype[] = [];

  clone(): Document {
    const cloned = new Document();
    cloned.components = this.components.map(c => c.clone());
    return cloned;
  }
  add(component: ComponentPrototype) { this.components.push(component); }
}

class Title implements Cloneable<Title> {
  constructor(public text: string) {}
  clone(): Title { return new Title(this.text); }
}

// Usage
const doc = new Document();
doc.add(new Title('Original Title'));
const cloned = doc.clone();
```

## When This Style Fits

- Objects are created by copying an existing instance (cloning).
- Instances have a small number of state combinations.
- Avoiding subclassing for object creation is desirable.

## When To Avoid

- Constructor-based creation is simpler and more type-safe.
- Cloning produces unexpected shared references (shallow copy problem).
- The prototype hierarchy is used as a workaround for missing a factory.

## CodeBTI Signals

The user prefers copying existing objects over creating from scratch and may be building document editors, template systems, or game entity spawners.

## Agent Guidance

Use Prototype for cloning objects with complex initialization. Prefer `clone(): T` methods over class hierarchies for creating copies. Document whether deep or shallow cloning is expected.

## Related Patterns

[Abstract Factory](../abstract-factory.md) (can use Prototype for cloning), [Composite](../composite.md) (often cloned recursively), [Decorator](../decorator.md).

## Source Reference

- Examples: [Conceptual](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Prototype/Conceptual/index.ts), [RealWorld](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Prototype/RealWorld/index.ts)
- Catalog: https://refactoring.guru/design-patterns/prototype
