# Builder

## 模式意图

分步骤构造复杂对象，同时将构造过程与最终对象分离。

## Python 形态

当对象创建有意义的阶段、验证、默认值或替代表示时使用 Builder。在 Python 中，dataclass、Pydantic 模型、仅关键字构造函数或普通辅助函数通常就足够了。

## 何时适用

- 构造有许多可选部分，且各部分之间有规则。
- 同一构建过程可以产生不同表示。
- 用户希望在测试或流水线中获得可读的设置代码。

## 何时避免

- 对象简单，可以直接初始化。
- 链式调用隐藏了无效的中间状态。
- Builder 只是重复构造函数的参数。

## CodeBTI 信号

用户偏好显式构造阶段、可读设置，以及相对于大型构造函数受控的对象创建。

## Agent 指导

从 dataclass 和命名工厂函数开始。仅在分阶段构造或验证实质上提高清晰度时才使用 Builder 类。

## 相关模式

Abstract Factory, Factory Method, Template Method。

## 来源引用

- Catalog: https://refactoring.guru/design-patterns/python
- Upstream example: https://github.com/RefactoringGuru/design-patterns-python/blob/main/src/Builder/Conceptual/main.py
