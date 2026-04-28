# Mediator

## Pattern Intent

Reduce chaotic dependencies between objects by forcing them to collaborate only via a mediator object.

## TypeScript Shape

TypeScript mediators use an `interface` for the mediator contract and typed notification methods. Components hold a mediator reference and use it to communicate.

```typescript
interface Mediator {
  notify(sender: object, event: string, payload?: string): void;
}

class ChatAppMediator implements Mediator {
  private users: User[] = [];

  notify(sender: object, event: string, payload?: string): void {
    if (event === 'subscribe') {
      const user = sender as User;
      this.users.push(user);
    }
    if (event === 'publish') {
      for (const user of this.users) {
        if (user !== sender) user.receiveMessage(payload);
      }
    }
  }
}

class User {
  constructor(
    public name: string,
    private mediator: Mediator
  ) {
    this.mediator.notify(this, 'subscribe');
  }
  receiveMessage(message: string) { console.log(`${this.name}: ${message}`); }
  publishMessage(message: string) { this.mediator.notify(this, 'publish', message); }
}
```

## When This Style Fits

- Communication between objects is complex and tightly coupled.
- A set of objects communicates in well-defined but complex ways.
- Adding a mediator simplifies and centralizes the communication protocol.

## When To Avoid

- Components communicate in simple, direct ways — a mediator adds unnecessary indirection.
- The mediator becomes a "god object" that knows about all components.
- Simple event emitters or direct calls solve the problem.

## CodeBTI Signals

The user prefers centralized communication and is building systems with many interconnected components (chat apps, UIs, distributed event systems).

## Agent Guidance

Use Mediator to centralize communication between tightly coupled components. Keep the mediator focused on coordination; it should not contain business logic.

## Related Patterns

[Facade](facade.md), [Observer](observer.md) (Observer can be used to implement Mediator), [Command](command.md).

## Source Reference

- Examples: [Conceptual](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Mediator/Conceptual/index.ts), [RealWorld](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Mediator/RealWorld/index.ts)
- Catalog: https://refactoring.guru/design-patterns/mediator
