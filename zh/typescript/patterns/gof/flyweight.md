# Flyweight

## 模式意图

通过共享来高效地支持大量细粒度对象。

## TypeScript 形态

TypeScript 的 Flyweight 将内在状态（可共享）与外在状态（每个对象独有）分开。一个工厂负责管理共享的 Flyweight 实例。

```typescript
class Flyweight {
  constructor(private sharedState: string) {}
  operation(uniqueState: string): void {
    console.log(`Flyweight: shared(${this.sharedState}), unique(${uniqueState})`);
  }
}

class FlyweightFactory {
  private flyweights: Map<string, Flyweight> = new Map();

  constructor(initialStates: string[]) {
    for (const state of initialStates) {
      this.flyweights.set(state, new Flyweight(state));
    }
  }

  getFlyweight(sharedState: string): Flyweight {
    if (!this.flyweights.has(sharedState)) {
      this.flyweights.set(sharedState, new Flyweight(sharedState));
    }
    return this.flyweights.get(sharedState)!;
  }
}

// Client usage
const factory = new FlyweightFactory(['Car', 'Truck']);
const car = factory.getFlyweight('Car');
car.operation('CL234IR'); // plate is extrinsic, 'Car' is intrinsic
```

## 何时适合此风格

- 应用程序使用大量存储成本高昂的对象。
- 大部分对象状态可以变为外在的而非内在的。
- 应用程序不依赖对象标识。

## 何时避免

- 对象共享增加了复杂性和困惑。
- 对象没有大量可共享的状态。
- 共享带来的性能提升微乎其微。

## CodeBTI 信号

用户熟悉共享优化，且正在构建包含大量相似对象的系统（渲染引擎、文档编辑器、游戏对象）。

## Agent 指导

在渲染、模拟或文档处理系统中，当存在大量相似对象时使用 Flyweight。优先通过工厂进行显式共享，而非隐式的全局缓存。

## 相关模式

[Composite](../composite.md)（可用于 Flyweight 管理子节点）、[State](../state.md)、[Strategy](../strategy.md)。

## 来源引用

- 示例：[Conceptual](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Flyweight/Conceptual/index.ts)、[RealWorld](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Flyweight/RealWorld/index.ts)
- 目录：https://refactoring.guru/design-patterns/flyweight