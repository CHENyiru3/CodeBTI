# State

## 模式意图

允许一个对象在其内部状态改变时改变其行为。对象看起来好像改变了它的类。

## TypeScript 形态

TypeScript 中的 State 模式使用 `abstract class` 或 `interface` 作为状态合约，具体状态实现各自的状态相关行为，由一个 Context 类管理状态转换。

```typescript
interface State {
  handle1(): void;
  handle2(): void;
}

class Context {
  private state: State;
  constructor(state: State) { this.transitionTo(state); }
  transitionTo(state: State): void {
    this.state = state;
  }
  request1(): void { this.state.handle1(); }
  request2(): void { this.state.handle2(); }
}

class ConcreteStateA implements State {
  constructor(private context: Context) {}
  handle1(): void {
    console.log('ConcreteStateA handles request1, transitioning to B');
    this.context.transitionTo(new ConcreteStateB(this.context));
  }
  handle2(): void { console.log('ConcreteStateA handles request2'); }
}

class ConcreteStateB implements State {
  constructor(private context: Context) {}
  handle1(): void { console.log('ConcreteStateB handles request1'); }
  handle2(): void {
    console.log('ConcreteStateB handles request2, transitioning to A');
    this.context.transitionTo(new ConcreteStateA(this.context));
  }
}
```

## 何时适合此风格

- 一个对象的行为取决于它的状态，并且状态需要在运行时改变。
- 操作有大量依赖于对象状态的条件语句。
- 状态之间的转换很复杂或涉及多个状态变量。

## 何时避免

- 基于状态的行为足够简单，可以用条件判断实现——不要过早引入状态。
- 状态数量少且固定，转换也很简单。
- 状态转换应该是确定性的和明确的，而不是委托的。

## CodeBTI 信号

用户偏好显式的状态机或工作流控制器。这出现在自动售货机、订单处理、认证流程和游戏引擎中。

## Agent 指导

将 State 用于复杂的状态相关行为。保持状态转换显式且类型安全。根据各状态之间是否存在共享行为，选择 `interface` 或 `abstract class`。

## 相关模式

[Flyweight](../flyweight.md)（共享内部状态）、[Singleton](../singleton.md)（常用于共享状态上下文）、[Strategy](../strategy.md)（结构相似，意图不同）。

## 来源引用

- 示例：[Conceptual](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/State/Conceptual/index.ts)、[RealWorld](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/State/RealWorld/index.ts)
- 模式目录：https://refactoring.guru/design-patterns/state