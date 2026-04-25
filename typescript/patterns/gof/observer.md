# Observer

## Pattern Intent

Define a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.

## TypeScript Shape

TypeScript observers can use `interface` contracts, Node.js `EventEmitter`, or custom typed event systems. Generics make the subscription type-safe.

```typescript
interface Subject {
  attach(observer: Observer): void;
  detach(observer: Observer): void;
  notify(): void;
}

class ConcreteSubject implements Subject {
  public state: number = 0;
  private observers: Observer[] = [];

  attach(observer: Observer): void {
    if (!this.observers.includes(observer)) this.observers.push(observer);
  }
  detach(observer: Observer): void {
    const idx = this.observers.indexOf(observer);
    if (idx >= 0) this.observers.splice(idx, 1);
  }
  notify(): void {
    for (const observer of this.observers) observer.update(this);
  }
  someBusinessLogic(): void {
    this.state = Math.floor(Math.random() * 10);
    this.notify();
  }
}

interface Observer {
  update(subject: Subject): void;
}

class ConcreteObserverA implements Observer {
  update(subject: Subject): void {
    if (subject instanceof ConcreteSubject && subject.state < 3) {
      console.log('ConcreteObserverA reacted');
    }
  }
}
```

Node.js `EventEmitter` and typed event libraries (e.g., `typed-emitter`) are common alternatives.

## When This Style Fits

- A change to one object requires changing others, and you do not know how many objects need to change.
-- An object should be able to notify other objects without assumptions about who those objects are.

## When To Avoid

- Simple synchronous updates can be handled with direct function calls.
- The observer list is dynamic and complex — consider an event bus or observable library.
- Memory leaks from dangling observer references are a risk.

## CodeBTI Signals

The user prefers event-driven or reactive architectures. This appears in UI systems, real-time dashboards, data-binding frameworks, and distributed systems.

## Agent Guidance

Default to explicit `Subject`/`Observer` interfaces or typed event emitters. Ensure `detach` is called to prevent memory leaks. Prefer unsubscription patterns over one-time observers.

## Related Patterns

[Mediator](../mediator.md) (can centralize Observer relationships), [Singleton](../singleton.md) (often used as a centralized event bus).

## Source Reference

- Examples: [Conceptual](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Observer/Conceptual/index.ts), [RealWorld](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Observer/RealWorld/index.ts)
- Catalog: https://refactoring.guru/design-patterns/observer
