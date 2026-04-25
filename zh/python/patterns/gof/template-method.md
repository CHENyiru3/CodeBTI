# Template Method

## 模式意图

定义算法骨架，同时允许选定的步骤变化。

## Python 形态

当子类共享稳定工作流时，使用带有钩子方法的基类。对于更简单的情况，使用高阶函数或带注入步骤的组合。

## 何时适用

- 工作流顺序固定且重要。
- 子类仅自定义特定步骤。
- 共享的设置、清理或验证应保持集中。

## 何时避免

- 子类覆盖了太多步骤。
- 继承使工作流难以追踪。
- 组合会使变化更清晰。

## CodeBTI 信号

用户在接受继承时，当它保护标准生命周期或算法顺序时。

## Agent 指导

保持钩子窄且按意图命名。优先使用调用可覆盖受保护步骤的最终公共方法。

## 相关模式

Strategy, State, Builder。

## 来源引用

- Catalog: https://refactoring.guru/design-patterns/python
- Upstream example: https://github.com/RefactoringGuru/design-patterns-python/blob/main/src/TemplateMethod/Conceptual/main.py
