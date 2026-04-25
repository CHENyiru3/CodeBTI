# Chain of Responsibility

## Pattern Intent

Pass requests along a chain of handlers. Upon receiving a request, each handler decides either to process the request or to pass it to the next handler in the chain.

## TypeScript Shape

TypeScript implementations use `interface` for the handler contract and `abstract class` or base implementations for chaining behavior. Generics can type the request and response.

```typescript
interface Handler<Request = string, Result = string> {
  setNext(handler: Handler<Request, Result>): Handler<Request, Result>;
  handle(request: Request): Result;
}

abstract class AbstractHandler implements Handler {
  private nextHandler: Handler;
  setNext(handler: Handler): Handler {
    this.nextHandler = handler;
    return handler; // enables chaining: monkey.setNext(squirrel).setNext(dog);
  }
  handle(request: string): string {
    if (this.nextHandler) return this.nextHandler.handle(request);
    return null;
  }
}

class MonkeyHandler extends AbstractHandler {
  handle(request: string): string {
    if (request === 'Banana') return `Monkey: I'll eat the ${request}.`;
    return super.handle(request);
  }
}
```

## When This Style Fits

- More than one object may handle a request, and the handler is not known in advance.
- You want to issue a request without specifying its receiver explicitly.
- The set of handlers should be determined at runtime.

## When To Avoid

- Only one handler is ever needed — use a direct call.
- The chain is static and known at compile time — simpler composition may suffice.
- Handlers need shared state that is awkward to thread through the chain.

## CodeBTI Signals

The user prefers pipeline-style processing, observability-friendly error handling, or batch processing with partial failure modes. This appears in authentication chains, middleware stacks, and data validation pipelines.

## Agent Guidance

Use Chain of Responsibility for processing pipelines where handlers may be added, removed, or reordered. Type the request and response with generics for compile-time safety.

## Related Patterns

[Command](../command.md), [Decorator](../decorator.md) (can build chains too), [Strategy](../strategy.md).

## Source Reference

- Examples: [Conceptual](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/ChainOfResponsibility/Conceptual/index.ts), [RealWorld](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/ChainOfResponsibility/RealWorld/index.ts)
- Catalog: https://refactoring.guru/design-patterns/chain-of-responsibility
