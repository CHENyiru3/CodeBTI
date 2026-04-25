# State

## Pattern Intent

Allow an object to alter its behavior when its internal state changes. The object will appear to change its class.

## TypeScript Shape

TypeScript state uses `abstract class` or `interface` for the state contract, with concrete states implementing state-specific behavior and a context class managing state transitions.

```typescript
interface State {
  handle1(): void;
  handle2(): void;
}

class Context {
  private state: State;
  constructor(state: State) { this.transitionTo(state); }
  transitionTo(state: State): void {
    this.state = state;
  }
  request1(): void { this.state.handle1(); }
  request2(): void { this.state.handle2(); }
}

class ConcreteStateA implements State {
  constructor(private context: Context) {}
  handle1(): void {
    console.log('ConcreteStateA handles request1, transitioning to B');
    this.context.transitionTo(new ConcreteStateB(this.context));
  }
  handle2(): void { console.log('ConcreteStateA handles request2'); }
}

class ConcreteStateB implements State {
  constructor(private context: Context) {}
  handle1(): void { console.log('ConcreteStateB handles request1'); }
  handle2(): void {
    console.log('ConcreteStateB handles request2, transitioning to A');
    this.context.transitionTo(new ConcreteStateA(this.context));
  }
}
```

## When This Style Fits

- An object's behavior depends on its state, and it must change at runtime.
- Operations have large conditional statements that depend on the object's state.
- Transitions between states are complex or involve multiple state variables.

## When To Avoid

- State-based behavior is simple enough for a conditional — do not introduce states prematurely.
- The number of states is small and fixed, and transitions are simple.
- State transitions should be deterministic and explicit rather than delegated.

## CodeBTI Signals

The user prefers explicit state machines or workflow controllers. This appears in vending machines, order processing, authentication flows, and game engines.

## Agent Guidance

Use State for complex state-dependent behavior. Keep state transitions explicit and type-safe. Prefer `interface` or `abstract class` based on whether shared behavior exists between states.

## Related Patterns

[Flyweight](../flyweight.md) (shared intrinsic state), [Singleton](../singleton.md) (often used for shared state contexts), [Strategy](../strategy.md) (similar structure, different intent).

## Source Reference

- Examples: [Conceptual](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/State/Conceptual/index.ts), [RealWorld](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/State/RealWorld/index.ts)
- Catalog: https://refactoring.guru/design-patterns/state
