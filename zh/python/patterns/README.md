# 设计模式数据库

本文件夹是 CodeBTI 设计模式数据库。Agent 应使用它将用户的风格偏好转化为具体的项目指导，而非当作通用教科书。

第一个数据库以 Python 为中心，映射了 RefactoringGuru 使用的经典 GoF 模式目录。CodeBTI 指导是原创的、面向 Agent 的：它解释模式偏好何时有用、何时变成过度工程，以及它对生成代码意味着什么。

## 来源引用

Python 目录结构和来源引用基于：

- RefactoringGuru Design Patterns in Python: https://github.com/RefactoringGuru/design-patterns-python
- RefactoringGuru Python catalog: https://refactoring.guru/design-patterns/python
- 许可证：Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International, https://github.com/RefactoringGuru/design-patterns-python/blob/main/LICENSE.txt
- 上游作者：Alexey Pyltsyn 和 Alexander Shvets。

不要将大型上游示例复制到 CodeBTI。链接到原始示例，用我们自己的话写 CodeBTI 专属指导。

## Python 模式索引

参见 [patterns/gof/README.md](../patterns/gof/README.md) 查看 Python 数据库。

## Agent 使用

在 CodeBTI 访谈期间，使用这些页面识别风格信号：

- 偏好显式相关组件族的用户可能倾向于 Abstract Factory。
- 想要灵活算法选择的用户可能倾向于 Strategy。
- 不喜欢隐藏全局状态的用户通常应避免 Singleton。
- 希望在复杂内部周围使用简单公共入口点的用户可能倾向于 Facade。

模式契合度是证据，不是身份。生成的 `CodeStyle.md` 应说明哪些模式被鼓励、哪些谨慎使用、哪些应避免。
