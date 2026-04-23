# Facade

## 模式意图

在复杂子系统之上提供一个简单接口。

## Python 形态

使用模块级 API、服务类、CLI 命令层或编排函数，隐藏内部顺序同时保持清晰的领域语言。

## 何时适用

- 用户需要一个清晰的入口点。
- 内部依赖复杂或不稳定。
- 项目受益于将编排与底层细节分离。

## 何时避免

- 门面变成一个巨大的上帝对象。
- 它隐藏了错误或重要配置。
- 它只是将每个方法不变地转发。

## CodeBTI 信号

用户重视平易近人的 API、稳定公共接口和可读的工作流。

## Agent 指导

使门面薄、以用户意图命名，且易于通过行为测试。将复杂逻辑保持在专门的协作者中。

## 相关模式

Adapter, Proxy, Mediator。

## 来源引用

- Catalog: https://refactoring.guru/design-patterns/python
- Upstream example: https://github.com/RefactoringGuru/design-patterns-python/blob/main/src/Facade/Conceptual/main.py
