# Mediator

## 模式意图

通过中介路由协作，减少组件之间的直接依赖。

## Python 形态

使用事件总线、协调器对象、工作流服务、控制器或编排层。中介应拥有交互策略，而非全部业务逻辑。

## 何时适用

- 否则许多组件直接相互依赖。
- 交互规则独立于组件变化。
- 工作流需要集中协调。

## 何时避免

- 中介变成上帝对象。
- 组件可以直接协作而没有耦合问题。
- 事件使控制流难以追踪。

## CodeBTI 信号

用户想要低耦合和集中编排，但需要限制抽象蔓延。

## Agent 指导

保持中介方法以用例为导向。当类型化方法调用或显式事件模型更清晰时，避免通用事件字符串。

## 相关模式

Observer, Facade, Command。

## 来源引用

- Catalog: https://refactoring.guru/design-patterns/python
- Upstream example: https://github.com/RefactoringGuru/design-patterns-python/blob/main/src/Mediator/Conceptual/main.py
