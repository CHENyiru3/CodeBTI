# Singleton

## 模式意图

确保一个类只有一个实例，并提供一个全局访问点来访问它。

## TypeScript 形态

TypeScript 中的 Singleton 模式使用 `private` 构造函数和静态访问器。私有类字段（`#instance`）或使用惰性初始化的静态属性都是惯用的写法。

```typescript
class Singleton {
  private static #instance: Singleton;

  private constructor() {}

  static get instance(): Singleton {
    if (!Singleton.#instance) {
      Singleton.#instance = new Singleton();
    }
    return Singleton.#instance;
  }

  someMethod(): void { /* ... */ }
}

// Usage
const s1 = Singleton.instance;
const s2 = Singleton.instance;
console.assert(s1 === s2); // true
```

模块级单例（从文件中导出的一个普通对象）在 TypeScript 的 ES 模块系统中更简单且同样有效。

## 何时适合此风格

- 一个类的实例恰好一个才是真正正确的（例如配置管理器、连接池、日志记录器）。
- 实例在初始化一次后永不重新配置。
- 为这个特定资源接受全局访问点是可接受的。

## 何时避免

- 测试或不同配置中需要多个实例。
- 单例引入了隐藏的全局状态，使测试变得复杂。
- 应用的不同部分需要同一资源的不同配置。

## CodeBTI 信号

用户接受集中的基础设施，但可能以可测试性换取便利。当可测试性重要时，优先选择依赖注入而非单例。

## Agent 指导

默认使用依赖注入或模块级常量。仅当生成的 `CodeStyle.md` 明确允许进程级全局状态时才使用 Singleton。清晰地记录单例，并在异步上下文中确保其线程安全。

## 相关模式

[Abstract Factory](abstract-factory.md)、[Facade](facade.md)、[State](state.md)。

## 来源引用

- 示例：[Conceptual](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Singleton/Conceptual/index.ts)、[RealWorld](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Singleton/RealWorld/index.ts)
- 模式目录：https://refactoring.guru/design-patterns/singleton