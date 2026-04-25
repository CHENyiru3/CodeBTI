# Memento

## 模式意图

在不暴露内部实现细节的情况下保存和恢复对象状态。

## Python 形态

使用快照、不可变状态对象、序列化记录、dataclass 副本或显式历史条目。避免捕获无法安全恢复的资源。

## 何时适用

- 需要撤销、回滚、检查点或审计历史。
- 状态恢复不得泄露内部信息。
- 状态模型是显式的且有界的。

## 何时避免

- 状态巨大或包含外部资源。
- 快照会隐藏事务边界。
- 数据库事务或事件日志更合适。

## CodeBTI 信号

用户重视可逆工作流、状态可追溯性和受控变更。

## Agent 指导

使快照边界显式。在中间变更和失败操作后测试恢复。

## 相关模式

Command, Prototype, State。

## 来源引用

- Catalog: https://refactoring.guru/design-patterns/python
- Upstream example: https://github.com/RefactoringGuru/design-patterns-python/blob/main/src/Memento/Conceptual/main.py
