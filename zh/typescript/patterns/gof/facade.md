# Facade

## 模式意图

为库、框架或任何其他复杂的类集合提供一个简化的接口。

## TypeScript 形态

TypeScript 中的 Facade 通常是一个普通的类或对象，它持有对子系统组件的引用，并暴露一个简化、有类型保障的 API。

```typescript
// Complex subsystems
class Subsystem1 {
  operation1(): string { return 'Subsystem1: Ready!'; }
  operationN(): string { return 'Subsystem1: Go!'; }
}
class Subsystem2 {
  operation1(): string { return 'Subsystem2: Get ready!'; }
  operationZ(): string { return 'Subsystem2: Fire!'; }
}

// Facade
class Facade {
  constructor(
    private subsystem1: Subsystem1 = new Subsystem1(),
    private subsystem2: Subsystem2 = new Subsystem2()
  ) {}

  operation(): string {
    let result = 'Facade initializes subsystems:\n';
    result += this.subsystem1.operation1() + '\n' + this.subsystem2.operation1() + '\n';
    result += 'Facade orders subsystems to perform the action:\n';
    result += this.subsystem1.operationN() + '\n' + this.subsystem2.operationZ();
    return result;
  }
}
```

## 何时适合此风格

- 需要为一个复杂或分层的子系统提供一个简单的 API。
- 将系统分层，每层都有一个单一的 Facade。
- 减少客户端与实现细节之间的依赖。

## 何时避免

- 子系统本身已经很简单——Facade 只是在增加不必要的间接层。
- 客户端需要完全访问子系统内部——不要隐藏真正需要暴露的内容。
- Facade 变成一个"上帝对象"，知道太多东西。

## CodeBTI 信号

用户重视便利性超过对常见操作的细粒度控制。这出现在 API 封装器、CLI 工具内部和服务层抽象中。

## Agent 指导

优先选择简单的 Facade 而不是复杂的子系统。每个 Facade 应该有单一的、专注的职责。暴露有类型的方法；不要返回原始的子系统类型。

## 相关模式

[Abstract Factory](../abstract-factory.md)（可用于创建 Facade）、[Adapter](../adapter.md)、[Mediator](../mediator.md)。

## 来源引用

- 示例：[Conceptual](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Facade/Conceptual/index.ts)、[RealWorld](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Facade/RealWorld/index.ts)
- 目录：https://refactoring.guru/design-patterns/facade