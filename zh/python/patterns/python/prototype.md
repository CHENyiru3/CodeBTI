# Prototype

## 模式意图

通过复制现有对象创建新对象，而不依赖其具体类。

## Python 形态

使用 `copy.copy`、`copy.deepcopy`、dataclass `replace`、模型复制方法或显式克隆方法。当对象包含可变字段、资源或标识符时，优先使用显式复制语义。

## 何时适用

- 从头构造对象代价高昂或冗长。
- 基础配置需要安全的变体。
- 测试需要对小fixture进行小幅修改。

## 何时避免

- 复制深度不明确。
- 对象包装文件、套接字、数据库会话或其他外部资源。
- 直接构造更好地传达意图。

## CodeBTI 信号

用户喜欢模板对象、fixture 重用和数据导向变化，但需要清晰的变更性规则。

## Agent 指导

记录浅拷贝与深拷贝行为。对于 dataclass，尽可能优先使用不可变对象和 `dataclasses.replace`。

## 相关模式

Builder, Memento, Flyweight。

## 来源引用

- Catalog: https://refactoring.guru/design-patterns/python
- Upstream example: https://github.com/RefactoringGuru/design-patterns-python/blob/main/src/Prototype/Conceptual/main.py
