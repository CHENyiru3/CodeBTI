# Visitor

## 模式意图

在不改变化对象本身的情况下，向对象结构添加操作。

## Python 形态

对具有多种操作的稳定对象层次结构使用 Visitor 类。Python 替代方案包括 singledispatch、模式匹配、显式方法或普通递归。

## 何时适用

- 对象结构是稳定的。
- 新操作比新节点类型添加得更频繁。
- 遍历和操作逻辑应分离。

## 何时避免

- 新节点类型添加频繁。
- Visitor 接口变得嘈杂。
- 模式匹配或直接方法更清晰。

## CodeBTI 信号

用户重视数据结构与操作之间的分离，并为可扩展性接受仪式感。

## Agent 指导

在 Python 中谨慎使用 Visitor。考虑 `functools.singledispatch` 或 `match`，除非双重分派真正有用。

## 相关模式

Composite, Iterator, Command。

## 来源引用

- Catalog: https://refactoring.guru/design-patterns/python
- Upstream example: https://github.com/RefactoringGuru/design-patterns-python/blob/main/src/Visitor/Conceptual/main.py
