# CodeStyle

项目：
Python GUI 计算器，用于数学计算

来源会话记录：
[Recording.md](../example/Recording.md)

主要 CodeBTI Profile：
算法优先极简主义者 (Algorithm-First Minimalist)

次要特征：
低仪式感对象中心 GUI 边界、务实的脚本构建者结构

## 项目意图

构建一个紧凑的 Python 计算器，带有 GUI。代码应使计算行为易于检查，保持 GUI 事件处理器薄，避免比项目本身更大的架构。

## 默认代码形态

首选组织方式：
使用一个小型 `Calculator` 对象作为主要行为边界。保持表达式解析、操作分发、结果创建和计算器状态靠近该对象。GUI 代码应将显示文本传入计算器并渲染返回的结果。

模块和文件夹规则：
保持扁平直到需要。简单的形状如 `src/calculator.py`、`src/gui.py` 和聚焦的测试就足够了。仅当文件拥挤或出现独立领域时才添加文件夹。

何时添加抽象：
仅在移除真实复杂度时才添加结构。小型操作注册表允许用于运算符和科学函数。当存在撤销或最近历史行为时，允许使用快照历史。

何时保持代码直接：
当逻辑可读时，保持辅助函数、直接数据结构和直接控制流。默认不引入 Command、Controller、Factory、Service 或 Plugin 层。

## Python 风格规则

命名：
使用计算器和数学词汇：`expression`、`operator`、`operand`、`operation`、`result`、`display`、`memory`、`history` 和 `snapshot`。避免 `manager`、`handler`、`processor`、`service` 等模糊名称，除非它们明显是最佳的领域术语。

类型注解：
保持类型提示轻量。公共或重要方法在提高可读性时可以加类型注解，但内部代码可以保持动态和鸭式类型友好。

数据建模：
避免重量级验证模型。对小型内部记录使用简单对象或字典。如果结果数据重复，偏好包含 `ok`、`text`、`value`、`error` 等字段的小型结果对象。

错误处理：
预期的用户输入失败应从 `Calculator.evaluate()` 返回显式结果值。GUI 应显示结果或简单错误状态。避免静默默认值、广泛的异常系统和 UI 中的重复验证。

状态管理：
项目较小时，在 `Calculator` 上直接保持普通可变状态。仅在实现撤销、恢复或最近计算行为时添加快照历史。

依赖管理：
使用 `uv` 作为首选工作流。优先使用 `pyproject.toml` 和 `uv.lock` 作为依赖的事实来源。仅在依赖明确改善 GUI 交付、解析正确性或可维护性时添加依赖。

注释和文档字符串：
使用最小注释。清晰的命名和短函数应承载大部分含义。仅对非显而易见的数学规则、解析器决策、GUI 工具包怪癖或需要解释的公共 API 添加注释。

## 模式指导

鼓励的模式：
使用轻量级 Facade 形态用于 `Calculator`：为 GUI 提供一个清晰的入口点如 `evaluate(expression)`。当操作增长超过简单分支时，使用 Strategy 作为简单的操作注册表或可调用映射。

谨慎使用的模式：
Memento 在该功能存在后允许用于撤销/历史快照。保持快照有界且显式。在存在真实的恢复/历史工作流之前避免应用它。

默认避免：
避免 Command 对象用于基本按钮点击或算术运算。避免 Singleton/全局注册表用于可变计算器状态。在存在需要它们的多个具体变体之前，避免工厂和插件系统。

模式参考：
有关塑造此指导的本地 CodeBTI 模式页面，参见下文引用部分。

## 引用

设计模式引用：

- 鼓励：[Facade](../python/patterns/python/facade.md)。支持 `Calculator.evaluate()` 在 GUI 代码和计算内部之间的小型边界。
- 鼓励：[Strategy](../python/patterns/python/strategy.md)。支持操作注册表作为简单的可调用映射，无需重量级策略类对象。
- 谨慎使用：[Memento](../python/patterns/python/memento.md)。支持撤销/最近计算的快照历史，但仅在该功能真实存在之后。
- 默认避免：[Command](../python/patterns/python/command.md)。基本 GUI 按钮操作应保持直接，除非操作需要重放、排队或撤销元数据。
- 默认避免：[Singleton](../python/patterns/python/singleton.md)。可变计算器状态不应隐藏在进程级全局访问之后。

有用的项目资源：

- [Python Profile 分类体系](../python/profiles/python-profile-taxonomy.md)。最终 Profile 将算法优先极简主义者与对象中心边界特征结合。
- [CodeStyle 模板](../python/templates/CodeStyle.template.md)。此文件遵循要求的 CodeBTI 输出结构。

## 测试策略

必须有的测试：
测试自定义计算逻辑：表达式解析、运算符优先级、无效输入、除零错误、操作注册表行为、结果对象和状态转换。

可选的测试：
仅在 GUI 层变得复杂或脆弱时添加 GUI 冒烟测试。默认不测试框架样板。

手动验证：
手动运行 GUI 并检查主流程：输入表达式、按下运算符、清除显示、显示错误，以及使用内存/历史功能（如果存在）。

## Git 与协作

分支：
首选快速主线。对于这个小型项目，直接编辑 `main` 或一个共享 `dev` 分支是可接受的。

提交消息：
使用简短的描述性消息，如 `add calculator result object` 或 `fix division error display`。常规提交前缀可选。

审查清单：
完成更改前，检查计算器行为是否保持直接、GUI 处理器是否保持薄、核心逻辑测试是否覆盖更改的计算行为，以及是否添加了不必要的层。

## Agent 行为

编写代码时：
从最小最清晰的实现开始。优先一个 `Calculator` 对象、小型辅助函数、简单的操作注册表和显式结果值。

审查代码时：
首先查找过度架构、隐藏的可变全局变量、GUI 和计算器之间的重复验证、缺失的核心逻辑测试，以及重复显而易见代码的注释。

不确定时：
保持代码直接和本地。仅在出现重复、令人困惑的流程或真实功能变化后才添加结构。

## 示例

首选代码形态：

```python
class Calculator:
    def __init__(self):
        self.memory = None
        self.history = []

    def evaluate(self, expression):
        try:
            value = evaluate_expression(expression, OPERATIONS)
        except (ValueError, ZeroDivisionError) as exc:
            return {"ok": False, "text": "Error", "value": None, "error": str(exc)}

        return {"ok": True, "text": str(value), "value": value, "error": None}
```

应避免的代码形态：

```python
class CalculatorCommandFactory:
    def create_command(self, button_name):
        ...


class CalculatorServiceRegistry:
    calculator_service = None
```

## 未解决的假设

- 尚未选定 GUI 工具包。
- 确切计算器范围未知：基本算术、科学函数、内存、撤销和历史可能会改变结构。
- 一旦存在 `pyproject.toml`，应最终确定打包命令。
