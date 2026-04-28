# Builder

## 模式意图

逐步构建复杂对象。该模式允许使用相同的构建代码生成不同类型和表示的对象。

## TypeScript 形态

TypeScript 的 Builder 使用 `interface` 定义 Builder 合约，使用 fluent 类方法链（`return this`）进行步骤链接。Director（可选）定义构建序列。

```typescript
interface Builder {
  reset(): void;
  producePartA(): Builder;
  producePartB(): Builder;
  producePartC(): Builder;
  getProduct(): Product1;
}

class ConcreteBuilder1 implements Builder {
  private product = new Product1();
  reset() { this.product = new Product1(); }
  producePartA() { this.product.parts.push('PartA1'); return this; }
  producePartB() { this.product.parts.push('PartB1'); return this; }
  producePartC() { this.product.parts.push('PartC1'); return this; }
  getProduct(): Product1 { const p = this.product; this.reset(); return p; }
}

// Client usage
const builder = new ConcreteBuilder1();
builder.producePartA().producePartC().getProduct();
```

TypeScript 的 `class` 配合 fluent 方法链是惯用写法。使用 `Partial<T>` 和 `Required<T>` 的泛型 Builder 也很常见。

## 何时适合此风格

- 对象构建涉及多个可选参数或步骤。
- 相同的构建过程应该产生不同的表示。
- 需要在构建过程中进行验证，而不是在构建后。

## 何时避免

- 构造函数参数很少且必需 — 不要为简单对象添加 Builder。
- Builder 只是将参数转发给构造函数 — 直接使用构造函数。
- 构建的对象是具有无行为的简单值对象。

## CodeBTI 信号

用户偏好逐步构建，可能有复杂的领域对象。当构建有多个阶段时，这与 [Factory Method](factory-method.md) 配合使用效果良好。

## Agent 指导

为具有复杂初始化的对象使用 Builder。优先使用 TypeScript 的 fluent 方法链。避免将 Builder 用于可以使用 `type` 别名或构造函数默认值的简单数据对象。

## 相关模式

[Factory Method](factory-method.md), [Abstract Factory](abstract-factory.md), [Composite](composite.md)（有时一起用于递归结构）。

## 来源引用

- 示例: [Conceptual](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Builder/Conceptual/index.ts), [RealWorld](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Builder/RealWorld/index.ts)
- 目录: https://refactoring.guru/design-patterns/builder