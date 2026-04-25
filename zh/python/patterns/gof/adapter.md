# Adapter

## 模式意图

将不兼容接口适配为客户端期望的接口。

## Python 形态

在 Python 中，适配器通常是薄包装类或函数：包装外部 API、数据库驱动、CLI 工具或旧代码，使其符合项目的接口约定。

## 何时适用

- 项目需要与具有不兼容接口的外部系统交互。
- 用户希望将第三方依赖与内部代码隔离。
- 接口不一致是真实摩擦点，而非假设问题。

## 何时避免

- 接口实际上足够相似，可以直接使用。
- 适配器只是转发每个方法而不添加任何价值。
- 包装的成本大于收益。

## CodeBTI 信号

用户重视清晰的边界、接口一致性和隔离外部依赖的能力。

## Agent 指导

使适配器薄且专注。保持适配器靠近它包装的外部依赖。测试通过适配器与外部系统的交互，而非适配器本身。

## 相关模式

Facade, Bridge, Decorator。

## 来源引用

- Catalog: https://refactoring.guru/design-patterns/python
- Upstream example: https://github.com/RefactoringGuru/design-patterns-python/blob/main/src/Adapter/Conceptual/main.py
