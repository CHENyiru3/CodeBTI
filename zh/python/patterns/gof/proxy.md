# Proxy

## 模式意图

通过站在另一个对象前面来控制对它的访问。

## Python 形态

使用代理进行惰性加载、授权、缓存、限流、远程客户端或检测。Python 中，包装类和描述符都可以充当代理。

## 何时适用

- 访问需要检查或副作用。
- 昂贵资源应惰性初始化。
- 真实对象是远程的、慢的或受保护的。

## 何时避免

- 代理隐藏了网络或 IO 成本。
- 它以令人惊讶的方式改变行为。
- 直接依赖注入更清晰。

## CodeBTI 信号

用户想要受控边界，并在代理保护正确性或资源时接受包装器。

## Agent 指导

使代理行为在命名、文档和测试中可见。不要让代理静默改变领域语义。

## 相关模式

Adapter, Decorator, Facade。

## 来源引用

- Catalog: https://refactoring.guru/design-patterns/python
- Upstream example: https://github.com/RefactoringGuru/design-patterns-python/blob/main/src/Proxy/Conceptual/main.py
