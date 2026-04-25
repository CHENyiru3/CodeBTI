# Python 设计模式数据库

本数据库覆盖 Python 的经典 GoF 模式目录，并针对 CodeBTI 风格推断进行了适配。

使用每个页面回答三个问题：

1. 此模式是否匹配用户的项目问题？
2. 此模式是否匹配用户偏好的编码风格？
3. 生成的代码是否应积极使用它、允许它还是避免它？

## 创建型模式

- [Abstract Factory](abstract-factory.md)
- [Builder](builder.md)
- [Factory Method](factory-method.md)
- [Prototype](prototype.md)
- [Singleton](singleton.md)

## 结构型模式

- [Adapter](adapter.md)
- [Bridge](bridge.md)
- [Composite](composite.md)
- [Decorator](decorator.md)
- [Facade](facade.md)
- [Flyweight](flyweight.md)
- [Proxy](proxy.md)

## 行为型模式

- [Chain of Responsibility](chain-of-responsibility.md)
- [Command](command.md)
- [Iterator](iterator.md)
- [Mediator](mediator.md)
- [Memento](memento.md)
- [Observer](observer.md)
- [State](state.md)
- [Strategy](strategy.md)
- [Template Method](template-method.md)
- [Visitor](visitor.md)

## Python 指导

现代 Python 通常有更简单的替代方案来替代经典重量级类模式：函数、协议、dataclass、上下文管理器、生成器、装饰器、依赖注入和小型模块。优先选择保留用户期望边界的最简单形态。

生成 `CodeStyle.md` 时，将每个首选模式转化为可执行规则：

- 命名和模块边界，
- 类型注解策略，
- 允许的抽象深度，
- 测试形态，
- 以及过度使用的审查检查。
