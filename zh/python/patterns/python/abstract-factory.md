# Abstract Factory

## 模式意图

创建一系列相关对象族，无需指定具体类。

## Python 形态

当需要多族相关对象且可能在运行时切换族时，使用抽象工厂注册表或工厂函数。在 Python 中，字典注册表或带类型的工厂函数通常是最佳选择。

## 何时适用

- 项目需要多族相关产品，且这些族必须一起使用。
- 用户希望在不暴露具体类的情况下切换产品实现。
- 用户愿意为清晰的对象边界增加一些结构。

## 何时避免

- 只有一族产品或对象创建简单。
- 工厂注册表变得比它创建的对象更复杂。
- 切换产品族不是真实需求。

## CodeBTI 信号

用户重视显式的对象族边界、类型化工厂接口，以及在不变动客户端代码的情况下切换实现族的能力。

## Agent 指导

从简单的字典注册表或类型化工厂函数开始。仅在族切换是真实项目需求时才升级到显式工厂类。保持工厂薄且易于发现。

## 相关模式

Factory Method, Prototype, Bridge。

## 来源引用

- Catalog: https://refactoring.guru/design-patterns/python
- Upstream example: https://github.com/RefactoringGuru/design-patterns-python/blob/main/src/AbstractFactory/Conceptual/main.py
