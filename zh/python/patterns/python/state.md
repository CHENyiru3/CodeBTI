# State

## 模式意图

让对象在其内部状态变化时改变行为。

## Python 形态

使用状态对象、带有转换表的枚举、dataclass 状态模型或显式工作流类。选择最简单的形式使转换可见。

## 何时适用

- 行为随生命周期状态实质性变化。
- 转换有值得测试的规则。
- 围绕状态的大型条件块在增长。

## 何时避免

- 只有两个简单状态。
- 状态类分散了少量逻辑。
- 转换模型未被很好理解。

## CodeBTI 信号

用户希望将生命周期规则编码在结构中，而非重复的条件判断。

## Agent 指导

记录允许的转换。优先使用枚举和表，除非每个状态的行为确实不同。

## 相关模式

Strategy, Memento, Template Method。

## 来源引用

- Catalog: https://refactoring.guru/design-patterns/python
- Upstream example: https://github.com/RefactoringGuru/design-patterns-python/blob/main/src/State/Conceptual/main.py
