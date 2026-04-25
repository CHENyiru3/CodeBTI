# Singleton

## 模式意图

确保存在一个实例，并提供对它的全局访问点。

## Python 形态

Python 模块、依赖注入容器、缓存工厂函数或进程级配置对象通常取代显式的 Singleton 类。如果线程安全重要，初始化必须经过深思熟虑并经过测试。

## 何时适用

- 对象代表真正进程级的基础设施。
- 重复构造是不正确或昂贵的。
- 生命周期简单，由应用程序启动控制。

## 何时避免

- 它从测试中隐藏了依赖。
- 它创建了可变全局状态。
- 不同调用者需要不同配置。

## CodeBTI 信号

用户接受集中式基础设施，但可能用可测试性换取便利性。

## Agent 指导

默认使用依赖注入或模块级常量。仅在生成的 `CodeStyle.md` 明确允许进程全局状态时才使用 Singleton。

## 相关模式

Facade, Factory Method, Proxy。

## 来源引用

- Catalog: https://refactoring.guru/design-patterns/python
- Upstream examples:
  - https://github.com/RefactoringGuru/design-patterns-python/blob/main/src/Singleton/Conceptual/NonThreadSafe/main.py
  - https://github.com/RefactoringGuru/design-patterns-python/blob/main/src/Singleton/Conceptual/ThreadSafe/main.py
