# Factory Method

## 模式意图

定义一个创建对象的接口，但让子类决定实例化哪个类。Factory Method 让一个类将实例化工作委托给子类。

## TypeScript 形态

TypeScript 的工厂方法使用 `abstract class` 或 `interface` 作为创建者，并使用带类型的返回值。子类实现工厂方法以返回具体的产品类型。

```typescript
interface Product {
  operation(): string;
}

abstract class Creator {
  abstract factoryMethod(): Product;
  someOperation(): string {
    const product = this.factoryMethod();
    return `Creator: worked with ${product.operation()}`;
  }
}

class ConcreteCreator1 extends Creator {
  factoryMethod(): Product { return new ConcreteProduct1(); }
}

class ConcreteProduct1 implements Product {
  operation(): string { return '{Result of the ConcreteProduct1}'; }
}
```

## 何时适合此风格

- 一个类无法预知它必须创建的对象类型。
- 子类应该指定它们所创建的对象。
- 将职责委托给帮助子类，使得关于创建哪个产品的知识局部化。

## 何时避免

- 只有一个具体产品存在——工厂只是在增加间接层。
- 创建逻辑足够简单，直接用构造函数调用即可。
- Factory Method 只是用作一个普通函数的别名——请使用有名称的工厂函数。

## CodeBTI 信号

用户偏好显式的对象创建，且需要由子类进行受控覆盖。这出现在插件系统、数据库连接器和多后端架构中。

## Agent 指导

当创建工作确实需要被子类覆盖时才使用 Factory Method。当不需要子类化时，优先使用简单的有名称的工厂函数（`function createProduct(): Product`）。

## 相关模式

[Abstract Factory](../abstract-factory.md)、[Builder](../builder.md)、[Prototype](../prototype.md)。

## 来源引用

- 示例：[Conceptual](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/FactoryMethod/Conceptual/index.ts)、[RealWorld](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/FactoryMethod/RealWorld/index.ts)
- 目录：https://refactoring.guru/design-patterns/factory-method