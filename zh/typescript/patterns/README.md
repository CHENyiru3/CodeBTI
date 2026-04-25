# TypeScript 设计模式数据库

本数据库涵盖经典 GoF 模式目录的 TypeScript 版本，并适配 CodeBTI 风格推断系统。

使用每个页面回答三个问题：

1. 此模式是否匹配用户的项目问题？
2. 此模式是否匹配用户首选的编码风格？
3. 生成的代码是否应积极使用它、允许它或避免它？

## 创建型模式

- [Abstract Factory](gof/abstract-factory.md)
- [Builder](gof/builder.md)
- [Factory Method](gof/factory-method.md)
- [Prototype](gof/prototype.md)
- [Singleton](gof/singleton.md)

## 结构型模式

- [Adapter](gof/adapter.md)
- [Bridge](gof/bridge.md)
- [Composite](gof/composite.md)
- [Decorator](gof/decorator.md)
- [Facade](gof/facade.md)
- [Flyweight](gof/flyweight.md)
- [Proxy](gof/proxy.md)

## 行为型模式

- [Chain of Responsibility](gof/chain-of-responsibility.md)
- [Command](gof/command.md)
- [Iterator](gof/iterator.md)
- [Mediator](gof/mediator.md)
- [Memento](gof/memento.md)
- [Observer](gof/observer.md)
- [State](gof/state.md)
- [Strategy](gof/strategy.md)
- [Template Method](gof/template-method.md)
- [Visitor](gof/visitor.md)

## TypeScript 指导

现代 TypeScript 由于其类型系统，往往有比经典类-heavy 模式更简单的替代方案：接口、工具类型、`readonly` 字段、箭头函数、依赖注入容器和 ES 模块。优先使用保持用户所需边界的最简单形态。

值得考虑的 TypeScript 特定替代方案：

- **GoF 类模式** 通常可以通过 `interface` + 纯对象 + 工厂函数变得更简单。
- **Decorator 模式** 有实验性 TypeScript 实现；函数式组合通常更清晰。
- **Observer 模式** 内置于 Node.js `EventEmitter`，可被类型化事件系统替换。
- **Singleton** 通常被模块级单例、依赖注入作用域或简单类工厂替换。
- **Strategy** 在 TypeScript 中自然表达为 `interface` + 函数实现。

生成 `CodeStyle.md` 时，将每个首选模式转换为可执行规则：

- 命名和模块边界，
- 类型策略，
- 允许的抽象深度，
- 测试形态，
- 以及过度使用的审查检查。

## 来源引用

所有示例改编自 [RefactoringGuru/design-patterns-typescript](https://github.com/RefactoringGuru/design-patterns-typescript)，采用 Creative Commons Attribution-NonCommercial-NoDerivatives 4.0。