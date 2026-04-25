# Composite

## Pattern Intent

Compose objects into tree structures and then work with these structures as if they were individual objects.

## TypeScript Shape

TypeScript composites use `abstract class` or `interface` for the component contract. Leaf and composite nodes implement the same interface, with composites managing children arrays.

```typescript
abstract class Component {
  protected parent: Component | null = null;
  setParent(parent: Component | null) { this.parent = parent; }
  getParent(): Component | null { return this.parent; }
  add(component: Component): void {}
  remove(component: Component): void {}
  isComposite(): boolean { return false; }
  abstract operation(): string;
}

class Leaf extends Component {
  operation(): string { return 'Leaf'; }
}

class Composite extends Component {
  private children: Component[] = [];
  add(component: Component): void {
    this.children.push(component);
    component.setParent(this);
  }
  remove(component: Component): void {
    const idx = this.children.indexOf(component);
    if (idx >= 0) { this.children.splice(idx, 1); component.setParent(null); }
  }
  isComposite(): boolean { return true; }
  operation(): string {
    return `Branch(${this.children.map(c => c.operation()).join('+')})`;
  }
}
```

## When This Style Fits

- Part-whole hierarchies such as trees, graphs, or nested configurations.
- Operations that should apply uniformly to both individual objects and compositions.
- Recursive tree processing with uniform traversal logic.

## When To Avoid

- The data is not naturally hierarchical — a flat list or map is simpler.
- Only leaf nodes exist — no composition is needed.
- Operations differ significantly between leaf and composite nodes.

## CodeBTI Signals

The user accepts uniform treatment of individual and composite objects. This appears in file systems, UI component trees, organizational hierarchies, and pricing/product bundles.

## Agent Guidance

Use Composite for tree-like data structures. Keep the component interface minimal. Prefer TypeScript's structural typing to avoid forcing inheritance hierarchies.

## Related Patterns

[Decorator](../decorator.md), [Iterator](../iterator.md), [Visitor](../visitor.md) (often used together).

## Source Reference

- Examples: [Conceptual](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Composite/Conceptual/index.ts), [RealWorld](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Composite/RealWorld/index.ts)
- Catalog: https://refactoring.guru/design-patterns/composite
