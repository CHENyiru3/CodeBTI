# Flyweight

## 模式意图

在多个对象之间共享公共状态以减少内存使用。

## Python 形态

使用内部化、缓存、不可变值对象、共享查找表，或重用固有状态的工厂。带有 `frozen=True` 的 dataclass 可以使共享状态更安全。

## 何时适用

- 许多对象重复大量不可变数据。
- 内存压力是真实且可测量的。
- 对象标识不如值标识重要。

## 何时避免

- 内存不是已证明的约束。
- 共享可变状态会产生 bug。
- 缓存生命周期不清楚。

## CodeBTI 信号

用户有性能意识，当资源压力证明确保有时接受间接层。

## Agent 指导

使用 Flyweight 前要求有可测量的理由。优先使用不可变共享状态和显式缓存所有权。

## 相关模式

Factory Method, Prototype, Singleton。

## 来源引用

- Catalog: https://refactoring.guru/design-patterns/python
- Upstream example: https://github.com/RefactoringGuru/design-patterns-python/blob/main/src/Flyweight/Conceptual/main.py
