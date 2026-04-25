# Iterator

## Pattern Intent

Provide a way to access the elements of an aggregate object sequentially without exposing its underlying representation.

## TypeScript Shape

TypeScript iterators use the `Symbol.iterator` protocol and can implement `Iterator<T>` interface. Generics make the iterator type-safe.

```typescript
interface Iterator<T> {
  current(): T;
  next(): T;
  key(): number;
  valid(): boolean;
  rewind(): void;
}

class AlphabeticalOrderIterator implements Iterator<string> {
  private position = 0;
  constructor(
    private collection: WordsCollection,
    private reverse = false
  ) {
    if (reverse) this.position = collection.getCount() - 1;
  }

  current(): string { return this.collection.getItems()[this.position]; }
  next(): string {
    const item = this.collection.getItems()[this.position];
    this.position += this.reverse ? -1 : 1;
    return item;
  }
  key(): number { return this.position; }
  valid(): boolean {
    return this.reverse
      ? this.position >= 0
      : this.position < this.collection.getCount();
  }
  rewind(): void {
    this.position = this.reverse ? this.collection.getCount() - 1 : 0;
  }
}
```

TypeScript natively supports `Symbol.iterator` and `for...of` loops, which is usually simpler than implementing the full Iterator interface.

## When This Style Fits

- Accessing a collection's contents without exposing its internal structure.
- Supporting multiple simultaneous traversals of a collection.
- Providing a uniform interface for traversing different collection structures.

## When To Avoid

- TypeScript's built-in `for...of`, `Array.map`, `Array.filter`, or generator functions solve the problem.
- Only one traversal direction is ever needed.
- The "collection" is really just an array or `Map`/`Set`.

## CodeBTI Signals

The user prefers explicit traversal control or needs multiple simultaneous iterators. This appears in tree traversals, database result sets, and streaming data processors.

## Agent Guidance

Prefer built-in TypeScript iteration (`for...of`, generators) over implementing the full Iterator interface. Implement custom iterators only when the aggregate has non-standard traversal logic.

## Related Patterns

[Composite](../composite.md) (traversed recursively), [Factory Method](../factory-method.md), [Memento](../memento.md) (used with iterator state).

## Source Reference

- Examples: [Conceptual](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Iterator/Conceptual/index.ts), [RealWorld](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Iterator/RealWorld/index.ts)
- Catalog: https://refactoring.guru/design-patterns/iterator
