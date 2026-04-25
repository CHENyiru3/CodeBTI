# Observer

## 模式意图

定义对象之间的一对多依赖关系，当一个对象的状态改变时，所有依赖它的对象都会自动收到通知并更新。

## TypeScript 形态

TypeScript 的 Observer 可以使用 `interface` 契约、Node.js `EventEmitter` 或自定义带类型的事件系统。泛型使订阅具有类型安全保障。

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

Node.js `EventEmitter` 和带类型的事件库（如 `typed-emitter`）是常见的替代方案。

## 何时适合此风格

- 修改一个对象需要同时修改其他对象，而你不知道有多少对象需要改变。
- 一个对象应该能够在不知道其他对象是谁的情况下通知它们。

## 何时避免

- 简单的同步更新可以直接用函数调用来处理。
- 观察者列表动态且复杂——考虑使用事件总线或可观察对象库。
- 悬挂的观察者引用可能导致内存泄漏风险。

## CodeBTI 信号

用户偏好事件驱动或响应式架构。这出现在 UI 系统、实时仪表板、数据绑定框架和分布式系统中。

## Agent 指导

默认使用显式的 `Subject`/`Observer` 接口或带类型的事件发射器。确保调用 `detach` 以防止内存泄漏。优先使用取消订阅模式，而非一次性观察者。

## 相关模式

[Mediator](../mediator.md)（可集中化 Observer 关系）、[Singleton](../singleton.md)（常被用作集中式事件总线）。

## 来源引用

- 示例：[Conceptual](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Observer/Conceptual/index.ts)、[RealWorld](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Observer/RealWorld/index.ts)
- 目录：https://refactoring.guru/design-patterns/observer