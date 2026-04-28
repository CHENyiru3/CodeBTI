# TypeScript 设计模式

所有 22 个 GoF 设计模式，针对 TypeScript 惯用法和 CodeBTI 风格推断系统进行了适配。

## 创建型模式

| 模式 | 意图 | TypeScript 关键思路 |
|------|------|-------------------|
| [Abstract Factory](abstract-factory.md) | 相关对象族 | `interface` 工厂 + `implements` |
| [Builder](builder.md) | 逐步构建 | 带 `return this` 的流式方法链 |
| [Factory Method](factory-method.md) | 延迟实例化到子类 | `abstract` creator + `implements` product |
| [Prototype](prototype.md) | 克隆现有对象 | `clone(): T` 接口 + 展开运算符 |
| [Singleton](singleton.md) | 单实例，全局访问 | `private static #instance` + static getter |

## 结构型模式

| 模式 | 意图 | TypeScript 关键思路 |
|------|------|-------------------|
| [Adapter](adapter.md) | 接口转换 | `implements` target + delegate to adaptee |
| [Bridge](bridge.md) | 将抽象与实现分离 | `interface` 抽象 + `interface` 实现 |
| [Composite](composite.md) | 树结构 | 带 children 数组的 `abstract class` |
| [Decorator](decorator.md) | 动态附加行为 | 组合包装类（优先于 `@decorator`） |
| [Facade](facade.md) | 简化子系统访问 | 带类型方法的普通类 |
| [Flyweight](flyweight.md) | 共享细粒度对象 | 工厂 + 内在/外在状态分离 |
| [Proxy](proxy.md) | 受控的对象访问 | 与真实主题相同的接口 |

## 行为型模式

| 模式 | 意图 | TypeScript 关键思路 |
|------|------|-------------------|
| [Chain of Responsibility](chain-of-responsibility.md) | 沿处理器链传递请求 | `interface Handler<T>` + `setNext()` |
| [Command](command.md) | 将请求封装为对象 | `interface Command { execute(): void }` |
| [Iterator](iterator.md) | 无暴露的顺序访问 | `Symbol.iterator` + `Iterator<T>` |
| [Mediator](mediator.md) | 集中组件通信 | `interface Mediator` + 类型化通知 |
| [Memento](memento.md) | 保存和恢复状态快照 | `Memento<T>` 接口 + caretaker |
| [Observer](observer.md) | 一对多依赖通知 | `Subject`/`Observer` 接口或 `EventEmitter` |
| [State](state.md) | 对象行为随状态变化 | `abstract class State` + `Context` |
| [Strategy](strategy.md) | 可交换算法 | `interface Strategy` + `Context` |
| [Template Method](template-method.md) | 带可自定义步骤的算法骨架 | `abstract class` + `protected` 方法 + hooks |
| [Visitor](visitor.md) | 将操作与对象结构分离 | 带 `accept(visitor)` 的双分派 |

## TypeScript 对 GoF 模式的替代方案

由于 TypeScript 的类型系统，许多 GoF 模式在 TypeScript 中更简单：

- **Singleton**：使用模块级导出对象或简单工厂函数
- **Strategy**：使用函数类型字段：`strategy: (data: T) => U`
- **Observer**：使用 Node.js 的 `EventEmitter` 或类型化事件库
- **Decorator**：使用组合包装类而非实验性 `@decorator` 语法
- **Iterator**：使用内置的 `Symbol.iterator` 和 `for...of` 循环
