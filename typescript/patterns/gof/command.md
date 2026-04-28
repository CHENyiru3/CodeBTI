# Command

## Pattern Intent

Encapsulate a request as an object, thereby letting you parameterize clients with different requests, queue or log requests, and support undoable operations.

## TypeScript Shape

TypeScript commands use `interface` for the command contract and typed `execute` methods. Receivers are separate objects or services. Invokers hold command references and call `execute`.

```typescript
interface Command {
  execute(): void;
}

class PrintRandomFactCommand implements Command {
  constructor(private receiver: RandomFactDomainServiceReceiver) {}
  async execute(): Promise<void> {
    const fact = await this.receiver.getRandomFact();
    console.info(fact);
  }
}

class CommandInvoker {
  constructor(private command: Command, private seconds: number = 5) {}
  start(): void {
    setInterval(() => this.command.execute(), this.seconds * 1000);
  }
}
```

For undo support, add `undo(): void` to the `Command` interface and store mementos or inverse commands.

## When This Style Fits

- Parameterizing objects with actions (e.g., buttons, menu items, keyboard shortcuts).
- Queueing, scheduling, or logging operations.
- Supporting undo/redo functionality.

## When To Avoid

- Simple one-off operations that do not need to be queued, logged, or undone.
- The "command" is just a function call — a callback or higher-order function is simpler.
- The command objects add complexity without providing the listed benefits.

## CodeBTI Signals

The user prefers explicit workflow steps, undo capability, or event-driven UI. This appears in CLIs, editor plugins, batch processors, and reactive systems.

## Agent Guidance

Use Command when the project needs explicit workflow steps, undo/redo, or action queuing. Prefer function-typed commands (`() => void` or `() => Promise<void>`) when undo is not needed.

## Related Patterns

[Chain of Responsibility](chain-of-responsibility.md), [Memento](memento.md), [Strategy](strategy.md).

## Source Reference

- Examples: [Conceptual](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Command/Conceptual/index.ts), [RealWorld](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Command/RealWorld/index.ts)
- Catalog: https://refactoring.guru/design-patterns/command
