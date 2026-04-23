# Iterator

## 模式意图

遍历集合而不暴露其内部表示。

## Python 形态

使用 Python 的迭代器协议、生成器、可迭代对象和惰性流水线。简单遍历用生成器函数，需要有状态配置时用类。

## 何时适用

- 数据应惰性流动。
- 集合结构应保持私有。
- 需要多种遍历策略。

## 何时避免

- 普通列表更清晰且足够小。
- 惰性行为隐藏错误太晚。
- 迭代顺序不明确。

## CodeBTI 信号

用户喜欢数据流清晰、流动式处理和封装的遍历。

## Agent 指导

使用惯用的 `__iter__`、生成器和类型提示如 `Iterable[T]` 或 `Iterator[T]`。记录迭代是否可重复。

## 相关模式

Composite, Visitor, Generator Pipelines。

## 来源引用

- Catalog: https://refactoring.guru/design-patterns/python
- Upstream example: https://github.com/RefactoringGuru/design-patterns-python/blob/main/src/Iterator/Conceptual/main.py
