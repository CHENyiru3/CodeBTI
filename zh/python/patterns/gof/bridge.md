# Bridge

## 模式意图

将抽象部分与实现部分分离，使两者可以独立变化。

## Python 形态

在 Python 中，Bridge 通常体现为：协议定义行为接口，具体实现作为可注入依赖，或通过组合分离关注点。

## 何时适用

- 两个维度独立变化（如平台和形状、抽象和实现）。
- 切换实现不应影响调用代码。
- 用户希望在不同平台或配置之间灵活切换。

## 何时避免

- 抽象和实现总是耦合在一起。
- 只有一到两种变化组合，不值得额外的间接层。
- 协议/接口的额外间接层增加了不必要的复杂度。

## CodeBTI 信号

用户重视关注点分离、接口稳定性以及在不同实现之间切换而不影响客户端代码的能力。

## Agent 指导

从简单协议和可注入依赖开始。添加 Bridge 结构仅在两个维度确实独立变化时。保持接口稳定——接口变化代价高昂。

## 相关模式

Abstract Factory, Adapter, Strategy。

## 来源引用

- Catalog: https://refactoring.guru/design-patterns/python
- Upstream example: https://github.com/RefactoringGuru/design-patterns-python/blob/main/src/Bridge/Conceptual/main.py
