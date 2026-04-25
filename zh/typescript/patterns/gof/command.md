# Command

## 模式意图

将请求封装为对象，从而让你可以用不同的请求对客户进行参数化、排队或记录请求，并支持可撤销的操作。

## TypeScript 形态

TypeScript 的命令使用 `interface` 定义命令合约，使用类型化的 `execute` 方法。接收者是独立的对象或服务。调用者持有命令引用并调用 `execute`。

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

要支持撤销，在 `Command` 接口中添加 `undo(): void` 并存储备忘录或反向命令。

## 何时适合此风格

- 用操作对对象进行参数化（例如按钮、菜单项、键盘快捷键）。
- 对操作进行排队、调度或记录。
- 支持撤销/重做功能。

## 何时避免

- 简单的不需要排队、记录或撤销的一次性操作。
- "命令"只是一个函数调用 — 回调或高阶函数更简单。
- 命令对象增加了复杂性而没有提供上述好处。

## CodeBTI 信号

用户偏好显式的工作流步骤、撤销能力或事件驱动的 UI。这出现在 CLI、编辑器插件、批处理程序和响应式系统中。

## Agent 指导

当项目需要显式工作流步骤、撤销/重做或操作排队时使用 Command。当不需要撤销时，优先使用函数类型的命令（`() => void` 或 `() => Promise<void>`）。

## 相关模式

[Chain of Responsibility](../chain-of-responsibility.md), [Memento](../memento.md), [Strategy](../strategy.md).

## 来源引用

- 示例: [Conceptual](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Command/Conceptual/index.ts), [RealWorld](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Command/RealWorld/index.ts)
- 目录: https://refactoring.guru/design-patterns/command