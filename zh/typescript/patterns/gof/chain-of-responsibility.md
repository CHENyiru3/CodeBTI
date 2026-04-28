# Chain of Responsibility

## 模式意图

将请求沿着处理者链传递。收到请求时，每个处理者决定自己处理该请求还是将请求传递给链中的下一个处理者。

## TypeScript 形态

TypeScript 实现使用 `interface` 定义处理者合约，使用 `abstract class` 或基类实现链接行为。泛型可以为请求和响应定义类型。

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

## 何时适合此风格

- 多个对象可能处理请求，且处理者事先未知。
- 希望在不明确指定接收者的情况下发出请求。
- 处理者集合应该在运行时确定。

## 何时避免

- 永远只需要一个处理者 — 直接调用。
- 链是静态的且在编译时已知 — 更简单的组合可能就足够了。
- 处理者需要共享状态，而通过链传递这些状态很别扭。

## CodeBTI 信号

用户偏好管道式处理、可观察性友好的错误处理或具有部分失败模式的批处理。这出现在认证链、中间件栈和数据验证管道中。

## Agent 指导

为处理管道使用 Chain of Responsibility，处理者可以被添加、移除或重新排序。为请求和响应使用泛型以获得编译时安全性。

## 相关模式

[Command](command.md), [Decorator](decorator.md)（也可以构建链）, [Strategy](strategy.md).

## 来源引用

- 示例: [Conceptual](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/ChainOfResponsibility/Conceptual/index.ts), [RealWorld](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/ChainOfResponsibility/RealWorld/index.ts)
- 目录: https://refactoring.guru/design-patterns/chain-of-responsibility