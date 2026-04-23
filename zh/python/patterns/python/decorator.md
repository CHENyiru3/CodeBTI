# Decorator

## 模式意图

动态地给对象附加额外职责，比继承更灵活。

## Python 形态

Python 的装饰器语法是 Decorator 模式的语言级实现。对于运行时行为组合，使用装饰器函数或带协议的包装类。

## 何时适用

- 需要在运行时为对象添加行为。
- 用户希望避免子类爆炸。
- 装饰行为可组合且顺序无关。

## 何时避免

- 装饰器链变得难以追踪或调试。
- 装饰顺序很重要但未记录。
- 行为变化最好是显式参数或策略模式。

## CodeBTI 信号

用户偏好行为组合、Pythonic 装饰器语法，以及在不修改类本身的情况下扩展功能。

## Agent 指导

使用 Python 装饰器语法时，确保装饰器的行为是透明的还是有副作用的。记录装饰顺序。避免深层装饰器链。

## 相关模式

Adapter, Facade, Strategy。

## 来源引用

- Catalog: https://refactoring.guru/design-patterns/python
- Upstream example: https://github.com/RefactoringGuru/design-patterns-python/blob/main/src/Decorator/Conceptual/main.py
