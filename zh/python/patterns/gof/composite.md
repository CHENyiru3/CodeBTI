# Composite

## 模式意图

将对象组合成树形结构以表示部分-整体层次。Composite 让客户端统一处理单个对象和组合对象。

## Python 形态

在 Python 中，Composite 通常使用协议定义统一接口、dataclass 表示叶节点，以及包含子组件的类表示组合节点。

## 何时适用

- 项目自然形成树形或层次结构（文件系统、UI 组件、AST）。
- 用户希望对单个对象和组合对象使用相同的代码路径。
- 操作应递归应用于整个结构。

## 何时避免

- 层次结构是扁平的或浅的。
- 用户只想对不同类型使用同一接口，但不需要递归操作。
- 层次结构是临时的，不值得专门的模式结构。

## CodeBTI 信号

用户偏好层次结构思维、统一接口处理不同规模的对象，以及递归组合操作。

## Agent 指导

从简单协议和 dataclass 开始。保持接口最小且一致。确保叶节点和组合节点都满足相同的接口契约。

## 相关模式

Chain of Responsibility, Decorator, Flyweight, Iterator。

## 来源引用

- Catalog: https://refactoring.guru/design-patterns/python
- Upstream example: https://github.com/RefactoringGuru/design-patterns-python/blob/main/src/Composite/Conceptual/main.py
