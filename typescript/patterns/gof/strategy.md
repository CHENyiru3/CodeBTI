# Strategy

## Pattern Intent

Define a family of algorithms, encapsulate each one, and make them interchangeable. Strategy lets the algorithm vary independently from clients that use it.

## TypeScript Shape

TypeScript strategies use `interface` for the algorithm contract and concrete strategy implementations. Contexts hold a strategy reference and delegate to it.

```typescript
interface Strategy {
  doAlgorithm(data: string[]): string[];
}

class Context {
  constructor(private strategy: Strategy) {}
  setStrategy(strategy: Strategy) { this.strategy = strategy; }
  doSomeBusinessLogic(): void {
    const result = this.strategy.doAlgorithm(['a', 'b', 'c']);
    console.log(result.join(','));
  }
}

class ConcreteStrategyA implements Strategy {
  doAlgorithm(data: string[]): string[] { return data.sort(); }
}

class ConcreteStrategyB implements Strategy {
  doAlgorithm(data: string[]): string[] { return data.reverse(); }
}

// Usage
const ctx = new Context(new ConcreteStrategyA());
ctx.doSomeBusinessLogic();
ctx.setStrategy(new ConcreteStrategyB());
ctx.doSomeBusinessLogic();
```

In TypeScript, strategy interfaces are often function-typed: `type Strategy = (data: T[]) => T[]`.

## When This Style Fits

- Many related classes differ only in their behavior.
- Different variants of an algorithm are needed at runtime.
- An algorithm uses data that clients should not know about.

## When To Avoid

- Only one algorithm variant exists — the strategy adds indirection.
- The algorithm is simple enough to be a function passed directly.
- Strategies need to share state — use a shared object or closure instead.

## CodeBTI Signals

The user prefers swappable algorithms and clear separation of "what to do" from "how to do it". This appears in sorting, validation, payment processing, and rendering engines.

## Agent Guidance

Use Strategy for swappable algorithms. Prefer function-typed strategies (`(input: T) => U`) when the strategy has no state. Use class-based strategies when the algorithm has internal state.

## Related Patterns

[Bridge](../bridge.md) (similar structure, different intent), [State](../state.md), [Template Method](../template-method.md).

## Source Reference

- Examples: [Conceptual](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Strategy/Conceptual/index.ts), [RealWorld](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Strategy/RealWorld/index.ts)
- Catalog: https://refactoring.guru/design-patterns/strategy
