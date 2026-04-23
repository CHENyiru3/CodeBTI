# Command

## 模式意图

将请求封装为对象，从而允许参数化、排队、日志和撤销操作。

## Python 形态

在 Python 中，Command 可以是简单函数、可调用对象或带有 `execute()` 方法的类。当需要元数据、重放或复合命令时，类更合适。

## 何时适用

- 需要参数化操作、排队执行或带撤销的重放。
- 用户希望记录操作历史或支持批处理。
- 操作需要作为一等对象传递。

## 何时避免

- 操作简单且不需要撤销、重放或排队。
- 函数作为可调用对象已经足够。
- 命令对象只是包装一个函数调用，没有额外价值。

## CodeBTI 信号

用户偏好显式的操作边界、可组合的操作历史，以及将操作作为数据处理的能力。

## Agent 指导

从函数和可调用对象开始。Command 类仅在需要元数据（时间戳、用户、上下文）或多步骤复合命令时才有价值。保持命令小且专注。

## 相关模式

Composite, Memento, Prototype。

## 来源引用

- Catalog: https://refactoring.guru/design-patterns/python
- Upstream example: https://github.com/RefactoringGuru/design-patterns-python/blob/main/src/Command/Conceptual/main.py
