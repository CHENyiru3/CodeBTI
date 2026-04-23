# Chain of Responsibility

## 模式意图

将请求沿着处理者链传递，直到有一个处理者处理它。

## Python 形态

在 Python 中，Chain of Responsibility 通常是处理函数或方法的有序列表、匹配函数注册表，或使用生成器的链式流水线。

## 何时适用

- 有多个对象可以处理请求，且处理者不预先已知。
- 用户希望在不硬编码处理者的情况下添加新处理步骤。
- 请求应被链中至少一个处理者处理。

## 何时避免

- 只有一到两个固定处理者，直接条件分支更清晰。
- 请求应被所有处理者处理（广播）。
- 链变得比原始条件逻辑更复杂。

## CodeBTI 信号

用户偏好解耦处理步骤、可组合的验证或转换流水线，以及清晰的处理者顺序。

## Agent 指导

从有序函数列表或字典注册表开始。保持处理者简单且单一职责。记录链的顺序，因为顺序影响结果。

## 相关模式

Command, Mediator, Observer。

## 来源引用

- Catalog: https://refactoring.guru/design-patterns/python
- Upstream example: https://github.com/RefactoringGuru/design-patterns-python/blob/main/src/ChainOfResponsibility/Conceptual/main.py
