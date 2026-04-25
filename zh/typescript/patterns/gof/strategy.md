# Strategy

## 模式意图

定义一系列算法，把它们一个个封装起来，并使它们可以相互替换。Strategy 让算法可以独立于使用它的客户端而变化。

## TypeScript 形态

TypeScript 中的策略模式使用 `interface` 来定义算法合约，具体策略实现该接口。Context 持有策略的引用并将操作委托给它。

```typescript
interface Strategy {
  doAlgorithm(data: string[]): string[];
}

class Context {
  constructor(private strategy: Strategy) {}
  setStrategy(strategy: Strategy) { this.strategy = strategy; }
  doSomeBusinessLogic(): void {
    const result = this.strategy.doAlgorithm(['a', 'b', 'c']);
    console.log(result.join(','));
  }
}

class ConcreteStrategyA implements Strategy {
  doAlgorithm(data: string[]): string[] { return data.sort(); }
}

class ConcreteStrategyB implements Strategy {
  doAlgorithm(data: string[]): string[] { return data.reverse(); }
}

// Usage
const ctx = new Context(new ConcreteStrategyA());
ctx.doSomeBusinessLogic();
ctx.setStrategy(new ConcreteStrategyB());
ctx.doSomeBusinessLogic();
```

在 TypeScript 中，策略接口经常是函数类型的：`type Strategy = (data: T[]) => T[]`。

## 何时适合此风格

- 多个相关类仅在行为上有所不同。
- 在运行时需要算法的不同变体。
- 算法使用了客户端不应该知道的数据。

## 何时避免

- 只有一种算法变体存在——策略只会增加间接层。
- 算法足够简单，可以直接作为函数传递。
- 策略之间需要共享状态——改用共享对象或闭包。

## CodeBTI 信号

用户偏好可交换的算法和"做什么"与"如何做"的清晰分离。这出现在排序、验证、支付处理和渲染引擎中。

## Agent 指导

将 Strategy 用于可交换的算法。当策略没有状态时，优先使用函数类型的策略（`(input: T) => U`）。当算法有内部状态时，使用基于类的策略。

## 相关模式

[Bridge](../bridge.md)（结构相似，意图不同）、[State](../state.md)、[Template Method](../template-method.md)。

## 来源引用

- 示例：[Conceptual](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Strategy/Conceptual/index.ts)、[RealWorld](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Strategy/RealWorld/index.ts)
- 模式目录：https://refactoring.guru/design-patterns/strategy