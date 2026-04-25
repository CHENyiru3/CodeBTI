# Iterator

## 模式意图

提供一种顺序访问聚合对象元素的方法，而不暴露其底层表示。

## TypeScript 形态

TypeScript 的迭代器使用 `Symbol.iterator` 协议，可以实现 `Iterator<T>` 接口。泛型使迭代器具有类型安全保障。

```typescript
interface Iterator<T> {
  current(): T;
  next(): T;
  key(): number;
  valid(): boolean;
  rewind(): void;
}

class AlphabeticalOrderIterator implements Iterator<string> {
  private position = 0;
  constructor(
    private collection: WordsCollection,
    private reverse = false
  ) {
    if (reverse) this.position = collection.getCount() - 1;
  }

  current(): string { return this.collection.getItems()[this.position]; }
  next(): string {
    const item = this.collection.getItems()[this.position];
    this.position += this.reverse ? -1 : 1;
    return item;
  }
  key(): number { return this.position; }
  valid(): boolean {
    return this.reverse
      ? this.position >= 0
      : this.position < this.collection.getCount();
  }
  rewind(): void {
    this.position = this.reverse ? this.collection.getCount() - 1 : 0;
  }
}
```

TypeScript 原生支持 `Symbol.iterator` 和 `for...of` 循环，通常比实现完整的 Iterator 接口更简单。

## 何时适合此风格

- 访问集合内容但不暴露其内部结构。
- 支持对集合的多次同时遍历。
- 为遍历不同集合结构提供统一接口。

## 何时避免

- TypeScript 内置的 `for...of`、`Array.map`、`Array.filter` 或生成器函数已经能解决问题。
- 只需要一个遍历方向。
- "集合"其实只是一个数组或 `Map`/`Set`。

## CodeBTI 信号

用户偏好显式的遍历控制，或需要多个同时存在的迭代器。这出现在树遍历、数据库结果集和流数据处理器中。

## Agent 指导

优先使用内置的 TypeScript 迭代（`for...of`、生成器），而非实现完整的 Iterator 接口。只有当聚合对象具有非标准遍历逻辑时，才实现自定义迭代器。

## 相关模式

[Composite](../composite.md)（递归遍历）、[Factory Method](../factory-method.md)、[Memento](../memento.md)（可用于保存迭代器状态）。

## 来源引用

- 示例：[Conceptual](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Iterator/Conceptual/index.ts)、[RealWorld](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Iterator/RealWorld/index.ts)
- 目录：https://refactoring.guru/design-patterns/iterator