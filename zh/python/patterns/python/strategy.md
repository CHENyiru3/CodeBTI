# Strategy

## 模式意图

在共享接口背后定义可互换的算法。

## Python 形态

使用函数、可调用对象、协议或小型类。在 Python 中，传递函数通常是最直接的 Strategy 实现。

## 何时适用

- 算法选择因配置、数据或用户偏好而异。
- 调用者不应包含每个算法的分支。
- 测试应独立验证算法。

## 何时避免

- 只有一到两个小分支。
- Strategy 名称不如直接代码清晰。
- 共享接口要求是人为的。

## CodeBTI 信号

用户喜欢可组合行为、显式算法选择和可测试的变化点。

## Agent 指导

从类型化可调用对象开始。仅当策略需要状态、元数据、生命周期钩子或多种方法时才升级到类。

## 相关模式

State, Template Method, Bridge。

## 来源引用

- Catalog: https://refactoring.guru/design-patterns/python
- Upstream example: https://github.com/RefactoringGuru/design-patterns-python/blob/main/src/Strategy/Conceptual/main.py
