# Decorator

## 模式意图

动态地给对象添加额外的职责。Decorator 为扩展功能提供了一种比子类化更灵活的替代方案。

## TypeScript 形态

TypeScript 的装饰器使用实验性的装饰器语法（`@decorator`）或基于组合的方法（组合包装类）。组合方法更具可移植性且更符合惯用法。

```typescript
interface Component {
  operation(): string;
}

class ConcreteComponent implements Component {
  operation(): string { return 'ConcreteComponent'; }
}

// Base decorator
class Decorator implements Component {
  constructor(protected component: Component) {}
  operation(): string { return this.component.operation(); }
}

// Concrete decorators
class ConcreteDecoratorA extends Decorator {
  operation(): string { return `ConcreteDecoratorA(${super.operation()})`; }
}

class ConcreteDecoratorB extends Decorator {
  operation(): string { return `ConcreteDecoratorB(${super.operation()})`; }
}

// Client usage
const component = new ConcreteDecoratorB(new ConcreteDecoratorA(new ConcreteComponent()));
```

注意：TypeScript 的装饰器语法是实验性的。请使用组合方法以获得可移植的、与框架无关的代码。

## 何时适合此风格

- 在不修改类的情况下向对象添加行为。
- 可以在运行时添加或移除的行为。
- 应该可堆叠和排序的行为组合。

## 何时避免

- 只需要一种装饰 — 直接修改类。
- 装饰逻辑很简单，该模式增加了不必要的仪式感。
- 简单的函数包装器可以达到同样的目标。

## CodeBTI 信号

用户偏好组合而非继承，且乐于包装行为。这出现在中间件栈、日志/遥测层和 UI 组件增强中。

## Agent 指导

优先使用函数组合（包装函数）或类组合，而非实验性装饰器。只有在项目已经使用需要装饰器的框架（如 Angular）时才使用装饰器。

## 相关模式

[Chain of Responsibility](../chain-of-responsibility.md)（结构相似，目的不同）, [Strategy](../strategy.md), [Proxy](../proxy.md).

## 来源引用

- 示例: [Conceptual](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Decorator/Conceptual/index.ts), [RealWorld](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Decorator/RealWorld/index.ts)
- 目录: https://refactoring.guru/design-patterns/decorator