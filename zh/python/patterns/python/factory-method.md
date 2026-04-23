# Factory Method

## 模式意图

让子类或专门创建者决定创建哪个具体对象。

## Python 形态

使用类方法、小型工厂函数、注册表或可覆盖方法，在共享接口背后返回对象。优先使用显式名称如 `from_config`、`for_backend`、`create_client`。

## 何时适用

- 创建逻辑因子类、配置或插件而异。
- 客户端代码应依赖稳定的产品接口。
- 项目需要受控的扩展点。

## 何时避免

- 直接构造函数更清晰。
- 动态选择会隐藏重要行为。
- 工厂变成一个万能服务定位器。

## CodeBTI 信号

用户想要扩展点，但仍然重视清晰的对象生命周期和命名构造路径。

## Agent 指导

将创建逻辑保持在它服务的抽象附近。除非插件行为是真实需求，否则避免全局注册表。

## 相关模式

Abstract Factory, Builder, Strategy。

## 来源引用

- Catalog: https://refactoring.guru/design-patterns/python
- Upstream example: https://github.com/RefactoringGuru/design-patterns-python/blob/main/src/FactoryMethod/Conceptual/main.py
