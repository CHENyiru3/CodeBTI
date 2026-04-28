# Flyweight

## Pattern Intent

Use sharing to support large numbers of fine-grained objects efficiently.

## TypeScript Shape

TypeScript flyweights separate intrinsic state (shared) from extrinsic state (unique per object). A factory manages the shared flyweight instances.

```typescript
class Flyweight {
  constructor(private sharedState: string) {}
  operation(uniqueState: string): void {
    console.log(`Flyweight: shared(${this.sharedState}), unique(${uniqueState})`);
  }
}

class FlyweightFactory {
  private flyweights: Map<string, Flyweight> = new Map();

  constructor(initialStates: string[]) {
    for (const state of initialStates) {
      this.flyweights.set(state, new Flyweight(state));
    }
  }

  getFlyweight(sharedState: string): Flyweight {
    if (!this.flyweights.has(sharedState)) {
      this.flyweights.set(sharedState, new Flyweight(sharedState));
    }
    return this.flyweights.get(sharedState)!;
  }
}

// Client usage
const factory = new FlyweightFactory(['Car', 'Truck']);
const car = factory.getFlyweight('Car');
car.operation('CL234IR'); // plate is extrinsic, 'Car' is intrinsic
```

## When This Style Fits

- An application uses a large number of objects with significant storage costs.
- Most object state can be made extrinsic rather than intrinsic.
- An application does not depend on object identity.

## When To Avoid

- Object sharing adds complexity and confusion.
- Objects do not have significant shared state.
- The performance gain from sharing is negligible.

## CodeBTI Signals

The user is comfortable with sharing optimization and is building systems with many similar objects (rendering engines, document editors, game objects).

## Agent Guidance

Use Flyweight for rendering, simulation, or document-processing systems with many similar objects. Prefer explicit sharing via a factory over implicit global caches.

## Related Patterns

[Composite](composite.md) (can use flyweight for child nodes), [State](state.md), [Strategy](strategy.md).

## Source Reference

- Examples: [Conceptual](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Flyweight/Conceptual/index.ts), [RealWorld](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Flyweight/RealWorld/index.ts)
- Catalog: https://refactoring.guru/design-patterns/flyweight
