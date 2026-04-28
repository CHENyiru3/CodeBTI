# Prototype

## 模式意图

使用原型实例来指定要创建的对象的种类，并通过复制这个原型来创建新对象。

## TypeScript 形态

TypeScript 的 Prototype 使用带有 `clone` 方法的接口。TypeScript 的展开操作符（`{ ...obj }`）和 `Object.assign` 简化了浅拷贝。深拷贝需要对嵌套引用进行仔细处理。

```typescript
interface Cloneable<T> {
  clone(): T;
}

class Document implements Cloneable<Document> {
  components: ComponentPrototype[] = [];

  clone(): Document {
    const cloned = new Document();
    cloned.components = this.components.map(c => c.clone());
    return cloned;
  }
  add(component: ComponentPrototype) { this.components.push(component); }
}

class Title implements Cloneable<Title> {
  constructor(public text: string) {}
  clone(): Title { return new Title(this.text); }
}

// Usage
const doc = new Document();
doc.add(new Title('Original Title'));
const cloned = doc.clone();
```

## 何时适合此风格

- 对象通过复制现有实例（克隆）来创建。
- 实例具有少量可能的状态组合。
- 希望避免为对象创建使用子类化。

## 何时避免

- 基于构造函数的创建更简单且更有类型安全保障。
- 克隆产生意外的共享引用（浅拷贝问题）。
- 原型层次结构被用作缺少工厂时的变通方案。

## CodeBTI 信号

用户偏好复制现有对象而非从头创建，可能正在构建文档编辑器、模板系统或游戏实体生成器。

## Agent 指导

将 Prototype 用于克隆具有复杂初始化的对象。优先使用 `clone(): T` 方法而非类层次结构来创建副本。明确说明期望的是深拷贝还是浅拷贝。

## 相关模式

[Abstract Factory](abstract-factory.md)（可使用 Prototype 进行克隆）、[Composite](composite.md)（通常递归克隆）、[Decorator](decorator.md)。

## 来源引用

- 示例：[Conceptual](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Prototype/Conceptual/index.ts)、[RealWorld](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Prototype/RealWorld/index.ts)
- 目录：https://refactoring.guru/design-patterns/prototype