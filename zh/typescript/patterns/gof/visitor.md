# Visitor

## 模式意图

将算法与操作其上的对象分离。

## TypeScript 形态

TypeScript 中的 Visitor 模式使用 `interface` 来定义组件和访问者两方的合约。组件声明 `accept(visitor: Visitor)`，每个具体访问者实现每个组件类型的 `visitConcreteComponentX` 方法。

```typescript
interface Component {
  accept(visitor: Visitor): void;
}

interface Visitor {
  visitConcreteComponentA(element: ConcreteComponentA): void;
  visitConcreteComponentB(element: ConcreteComponentB): void;
}

class ConcreteComponentA implements Component {
  accept(visitor: Visitor): void { visitor.visitConcreteComponentA(this); }
  exclusiveMethod(): string { return 'A'; }
}

class ConcreteComponentB implements Component {
  accept(visitor: Visitor): void { visitor.visitConcreteComponentB(this); }
  specialMethod(): string { return 'B'; }
}

class ConcreteVisitor1 implements Visitor {
  visitConcreteComponentA(element: ConcreteComponentA): void {
    console.log(`${element.exclusiveMethod()} + ConcreteVisitor1`);
  }
  visitConcreteComponentB(element: ConcreteComponentB): void {
    console.log(`${element.specialMethod()} + ConcreteVisitor1`);
  }
}

// Usage
const components: Component[] = [new ConcreteComponentA(), new ConcreteComponentB()];
const visitor = new ConcreteVisitor1();
for (const comp of components) comp.accept(visitor);
```

## 何时适合此风格

- 需要向一个封闭的对象集合添加操作而不修改它们的类。
- 需要将复杂对象结构上的相关操作分组。
- 在类型层次结构上执行横切操作（序列化、验证、渲染）。

## 何时避免

- 组件类型集合是开放的且不断变化——每种新类型都需要在每个访问者中添加新的 `visit` 方法。
- 组件已经暴露了所有必要的数据——简单的函数就足够了。
- Visitor 模式添加的复杂性没有得到相应的好处。

## CodeBTI 信号

用户熟悉双重分派，并希望将操作与数据分离。这出现在 AST 处理器、文档对象模型和编译器中。

## Agent 指导

将 Visitor 用于封闭类型层次结构上的操作。当类型集合稳定时，优先使用简单的函数或组件上的方法。当预期会频繁添加新组件类型时，避免使用 Visitor。

## 相关模式

[Composite](composite.md)（常被 Visitor 遍历）。

## 来源引用

- 示例：[Conceptual](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Visitor/Conceptual/index.ts)、[RealWorld](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Visitor/RealWorld/index.ts)
- 模式目录：https://refactoring.guru/design-patterns/visitor