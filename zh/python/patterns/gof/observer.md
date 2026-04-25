# Observer

## 模式意图

当被观察对象变化时通知订阅者。

## Python 形态

使用回调、事件发射器、信号系统、异步队列或类型化事件分发。保持订阅生命周期可见，以避免泄漏和意外的副作用。

## 何时适用

- 多个独立消费者响应事件。
- 发布者不应知道订阅者。
- 事件是领域或集成边界的一部分。

## 何时避免

- 同步控制流更容易推理。
- 订阅者顺序重要但被隐藏。
- 副作用变得难以测试。

## CodeBTI 信号

用户偏好解耦的事件驱动扩展，并在有文档记录时接受间接流程。

## Agent 指导

使用类型化事件载荷和显式的 subscribe/unsubscribe API。在测试中，将发出的事件作为行为断言。

## 相关模式

Mediator, Command, Chain of Responsibility。

## 来源引用

- Catalog: https://refactoring.guru/design-patterns/python
- Upstream example: https://github.com/RefactoringGuru/design-patterns-python/blob/main/src/Observer/Conceptual/main.py
