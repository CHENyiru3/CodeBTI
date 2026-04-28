# Mediator

## 模式意图

通过强制对象仅通过中介者对象协作，来减少对象之间混乱的依赖关系。

## TypeScript 形态

TypeScript 的中介者使用 `interface` 定义中介者契约和带类型的通知方法。组件持有对中介者的引用，并通过它进行通信。

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

## 何时适合此风格

- 对象之间的通信复杂且紧密耦合。
- 一组对象以明确但复杂的方式进行通信。
- 添加一个中介者可以简化并集中通信协议。

## 何时避免

- 组件以简单、直接的方式通信——中介者只是增加了不必要的间接层。
- 中介者变成一个"上帝对象"，了解所有组件。
- 简单的事件发射器或直接调用就能解决问题。

## CodeBTI 信号

用户偏好集中式通信，正在构建包含大量互连组件的系统（聊天应用、UI、分布式事件系统）。

## Agent 指导

使用 Mediator 将紧密耦合的组件之间的通信集中化。保持中介者专注于协调；它不应该包含业务逻辑。

## 相关模式

[Facade](facade.md)、[Observer](observer.md)（Observer 可用于实现 Mediator）、[Command](command.md)。

## 来源引用

- 示例：[Conceptual](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Mediator/Conceptual/index.ts)、[RealWorld](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Mediator/RealWorld/index.ts)
- 目录：https://refactoring.guru/design-patterns/mediator