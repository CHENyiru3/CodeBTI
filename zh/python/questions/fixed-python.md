# Python 固定问题

本文件定义了 Python 项目的 10 个固定 CodeBTI 问题。

用户可随时修改之前的答案。访谈期间，向用户展示面向用户的场景、说明、代码示例和选项。将 `Agent scoring`、`Pattern signals` 和 `CodeStyle output implications` 对用户隐藏，除非用户明确询问 CodeBTI 工作原理。

## Q1. 通用目的与范式

**维度：**
对象中心 vs 函数优先 vs 数据优先 vs 扁平过程式组织。

**用户面对的场景：**
开始一个新的 Python 项目时，您如何自然地组织核心逻辑？以下是同一个小型任务——问候用户并告知年龄——用四种不同风格编写的示例。

**用户面对的说明：**
选择您最自然愿意维护的风格。您可以随时修改之前的答案。

**代码示例：**

```python
# A. 对象中心
class User:
    def __init__(self, name: str, birth_year: int):
        self.name = name
        self.birth_year = birth_year

    def age(self, current_year: int) -> int:
        return current_year - self.birth_year

    def greeting(self, current_year: int) -> str:
        return f"Hi {self.name}, you are {self.age(current_year)}."


# B. 函数优先
def calculate_age(birth_year: int, current_year: int) -> int:
    return current_year - birth_year


def greeting(name: str, age: int) -> str:
    return f"Hi {name}, you are {age}."


# C. 数据优先
from dataclasses import dataclass


@dataclass(frozen=True)
class UserData:
    name: str
    birth_year: int


def greet_user(user: UserData, current_year: int) -> str:
    age = current_year - user.birth_year
    return f"Hi {user.name}, you are {age}."


# D. 扁平过程式
CURRENT_YEAR = 2026


def greet(user_payload: dict) -> str:
    age = CURRENT_YEAR - user_payload["birth_year"]
    return f"Hi {user_payload['name']}, you are {age}."
```

**选项：**
- A. 对象中心：将状态和行为保持在领域对象内部。
- B. 函数优先：使用小型函数，将显式输入转换为输出。
- C. 数据优先：先定义数据形状，然后围绕它编写轻量函数。
- D. 扁平过程式：用简单辅助函数编写直接流程，必要时使用模块级常量。

**代理评分：**
- A：类友好、封装优先、乐于让对象拥有行为。
- B：无状态、函数优先、显式数据流、偏好简单组合。
- C：数据形状优先、清晰的模型边界、喜欢不可变或已验证记录。
- D：低仪式、速度优先、乐于使用脚本和直接模块流程。

**模式信号：**
- A：可能使用 [State](../patterns/gof/state.md)、[Template Method](../patterns/gof/template-method.md)、[Strategy](../patterns/gof/strategy.md) 作为类。
- B：可能使用 [Strategy](../patterns/gof/strategy.md) 作为可调用对象、[Iterator](../patterns/gof/iterator.md)/生成器流水线。
- C：仅当数据构造复杂度增长时，才可能使用 [Builder](../patterns/gof/builder.md) 或 [Factory Method](../patterns/gof/factory-method.md)。
- D：避免过早使用 GoF 模式；偏好小型辅助函数和清晰的模块。

**CodeStyle 输出影响：**
用此答案设置默认项目形态：类中心、函数优先、数据模型中心还是脚本/过程优先。未来指导应说明项目何时可以偏离该默认形态。

---

## Q2. 防御性编程与类型边界

**维度：**
严格静态类型 vs 边界类型 vs 运行时验证 vs 动态鸭式类型。

**用户面对的场景：**
Python 让您可以选择代码检查自身假设的严格程度。对于更新用户年龄的函数，项目应有多严格？

**用户面对的说明：**
选择您最自然愿意维护的风格。您可以随时修改之前的答案。

**代码示例：**

```python
# A. 严格检查
def update_user_age(user_id: int, new_age: int) -> bool:
    if not isinstance(new_age, int):
        raise TypeError("new_age must be an integer")
    if new_age <= 0:
        raise ValueError("new_age must be positive")

    user: dict[str, object] = db_get(user_id)
    user["age"] = new_age
    db_save(user)
    return True


# B. 边界类型
def update_user_age(user_id: int, new_age: int) -> bool:
    user = db_get(user_id)
    if new_age <= 0:
        return False

    user["age"] = new_age
    db_save(user)
    return True


# C. 运行时验证
from pydantic import BaseModel, Field


class AgeUpdate(BaseModel):
    user_id: int
    new_age: int = Field(gt=0)


def update_user_age(raw_input: dict) -> bool:
    payload = AgeUpdate(**raw_input)
    user = db_get(payload.user_id)
    user["age"] = payload.new_age
    db_save(user)
    return True


# D. 动态 Python
def update_user_age(user_id, new_age):
    user = db_get(user_id)
    user["age"] = int(new_age)
    db_save(user)
    return True
```

**选项：**
- A. 严格检查：在重要函数中使用强类型提示和显式验证。
- B. 边界类型：公共函数和模块边界处类型化，内部代码保持灵活。
- C. 运行时验证：使用验证模型清理和检查传入数据。
- D. 动态 Python：保持类型提示轻量，除非有 bug 证明需要检查，否则信任调用者。

**代理评分：**
- A：高防御性编程、显式不变量、更强的静态分析姿态。
- B：边界优先纪律、实用的内部灵活性。
- C：验证优先、接受运行时模型库和类型强制。
- D：动态、低仪式、鸭式类型友好。

**模式信号：**
- A：支持显式接口、协议、严格适配器。
- B：支持在边界处使用 [Facade](../patterns/gof/facade.md) 和 [Adapter](../patterns/gof/adapter.md)，不在内部过度类型化。
- C：支持数据优先建模、验证边界、复杂载荷的 [Builder](../patterns/gof/builder.md)。
- D：除非项目风险要求，否则避免重量级接口模式。

**CodeStyle 输出影响：**
设置类型策略、验证策略，以及 Agent 应在何处添加检查。此答案应防止未来代码在严格类型风格与随意无类型风格之间随意混用。

---

## Q3. 错误处理与恢复

**维度：**
快速失败异常 vs 安全降级 vs 显式结果对象 vs 批量隔离。

**用户面对的场景：**
项目从 JSON API 接收交易载荷。有时 `amount` 缺失或是一个类似 `"N/A"` 的值。代码应如何处理这类坏数据？

**用户面对的说明：**
选择您最自然愿意维护的风格。您可以随时修改之前的答案。

**代码示例：**

```python
# A. 快速失败
class MalformedTransactionError(ValueError):
    pass


def calculate_total(tx: dict) -> float:
    if "amount" not in tx:
        raise MalformedTransactionError("Transaction is missing amount")
    if not isinstance(tx["amount"], (int, float)):
        raise MalformedTransactionError("Transaction amount must be numeric")
    return tx["amount"] * 1.2


# B. 安全降级
def calculate_total(tx: dict) -> float:
    try:
        return float(tx.get("amount", 0)) * 1.2
    except (TypeError, ValueError):
        return 0.0


# C. 显式结果
def calculate_total(tx: dict) -> dict:
    amount = tx.get("amount")
    if not isinstance(amount, (int, float)):
        return {"ok": False, "value": None, "error": "Invalid amount"}
    return {"ok": True, "value": amount * 1.2, "error": None}


# D. 记录并继续
import logging


def process_batch(transactions: list[dict]) -> list[float]:
    totals = []
    for tx in transactions:
        try:
            totals.append(float(tx["amount"]) * 1.2)
        except (KeyError, TypeError, ValueError) as exc:
            logging.warning("Skipped transaction %s: %s", tx.get("id"), exc)
    return totals
```

**选项：**
- A. 快速失败：无效数据一出现就抛出明确错误。
- B. 安全降级：返回默认值，保持主流程继续。
- C. 显式结果：返回结构化的成功或失败值，而非对预期问题抛异常。
- D. 记录并继续：记录失败、跳过坏项、继续处理其余部分。

**代理评分：**
- A：契约优先、正确性优先于连续性、异常友好。
- B：连续性优先、宽容降级风格、存在隐藏数据质量问题的风险。
- C：显式控制流、结果对象风格、适合可恢复的业务错误。
- D：批量弹性、可观测性友好、适合数据流水线。

**模式信号：**
- A：支持边界验证、严格 Facade、自定义异常层次结构。
- B：支持宽容 [Adapter](../patterns/gof/adapter.md)/[Facade](../patterns/gof/facade.md) 行为，但需要明确的降级策略。
- C：支持函数式风格、[Command](../patterns/gof/command.md) 结果、显式工作流状态。
- D：支持流水线风格、[Chain of Responsibility](../patterns/gof/chain-of-responsibility.md)、隔离/死信工作流。

**CodeStyle 输出影响：**
定义项目级错误策略，防止 Agent 随意混用静默默认值、异常、结果字典和隔离行为。

---

## Q4. 命名与可读性

**维度：**
显式命名 vs 简洁惯用语 vs 领域词汇 vs 注释支撑的命名。

**用户面对的场景：**
命名塑造代码库阅读体验。这个项目中，变量、函数和类应如何命名？

**用户面对的说明：**
选择您最自然愿意维护的风格。您可以随时修改之前的答案。

**代码示例：**
无。选项是关于命名风格和审查期望。

**选项：**
- A. 显式命名：即使更长，也偏好 `calculate_total_revenue_for_active_users` 这样的名称。
- B. 简洁惯用语：上下文清晰时允许 `idx`、`req`、`df`、`cfg` 等短名称。
- C. 领域语言：使用产品、业务、数学或科学领域的术语，而非 `manager` 或 `handler` 等通用名称。
- D. 简短名称加说明：文档字符串或注释解释了原因和上下文时，允许更短的名称。

**代理评分：**
- A：通过显式命名提高可读性；容忍更长的行和更少的缩写。
- B：上下文密集、惯用 Python、局部短名称舒适。
- C：领域驱动命名、避免通用服务/对象词汇。
- D：文档支撑命名、接受注释作为可读性的一部分。

**模式信号：**
- A：帮助显式 [Facade](../patterns/gof/facade.md) 和边界 API。
- B：支持函数优先和脚本式风格。
- C：支持领域模型、领域服务、清晰的通用语言。
- D：支持注释引导的 Agent 工作流和更详细的生成文档。

**CodeStyle 输出影响：**
为函数、类、模块、变量和审查注释设置命名规则。生成的 `CodeStyle.md` 应包含允许的缩写和反对的通用名称。

---

## Q5. 架构与接线风格

**维度：**
Python 工具 vs 依赖注入 vs 可替换模式 vs 中央注册表 vs 算法优先代码。

**用户面对的场景：**
当项目有路由、设置/清理、服务或多种实现时，您偏好如何将各部分连接在一起？

**用户面对的说明：**
选择您最自然愿意维护的风格。您可以随时修改之前的答案。

**代码示例：**
无。此问题比较架构偏好，而非一个局部代码片段。

**选项：**
- A. Python 工具：对重复设置或清理使用装饰器、上下文管理器和小型包装器。
- B. 传入依赖：将服务、客户端和仓储直接传入函数或类。
- C. 可替换实现：定义清晰接口，使不同后端或算法可交换。
- D. 中央注册表：将共享服务保存在一个配置模块或对象中，其他代码导入它。
- E. 算法优先：保持抽象薄，关注数据结构、性能和直接 API。

**代理评分：**
- A：Pythonic 组合、名称和测试清晰时接受隐藏设置。
- B：测试优先、显式依赖、低隐藏全局状态。
- C：接口优先、扩展友好、乐于使用模式式结构。
- D：便利优先、集中配置、存在隐藏耦合风险。
- E：性能和直接性优先、避免架构仪式。

**模式信号：**
- A：[Decorator](../patterns/gof/decorator.md)、上下文管理器模式、[Proxy](../patterns/gof/proxy.md) 式包装器。
- B：[Adapter](../patterns/gof/adapter.md)、[Facade](../patterns/gof/facade.md)、依赖注入、测试替身。
- C：[Strategy](../patterns/gof/strategy.md)、[Factory Method](../patterns/gof/factory-method.md)、[Abstract Factory](../patterns/gof/abstract-factory.md)、[Bridge](../patterns/gof/bridge.md)。
- D：[Singleton](../patterns/gof/singleton.md)/注册表、服务定位器注意。
- E：避免不必要的 GoF 结构；偏好清晰的函数和数据结构。

**CodeStyle 输出影响：**
设置默认接线规则：Python 包装器、依赖注入、显式接口、中央注册表还是算法优先的直接代码。包含隐藏状态和过度抽象的警示规则。

---

## Q6. 文件夹结构

**维度：**
特性文件夹 vs 技术分层 vs 扁平源码树 vs 框架/工具驱动布局。

**用户面对的场景：**
代码库从单文件增长到多个文件时，Agent 应默认使用什么结构？

**用户面对的说明：**
选择您最自然愿意维护的风格。您可以随时修改之前的答案。

**代码示例：**

```text
# A. 特性文件夹
src/users/
src/billing/
src/reports/

# B. 技术分层
src/models/
src/services/
src/routes/

# C. 扁平直到需要
src/
  users.py
  billing.py
  reports.py

# D. 工具或框架布局
src/<framework-or-template-convention>/
tests/
docs/
```

**选项：**
- A. 特性文件夹：按产品领域或领域对文件分组，每个区域拥有自己的本地模型、服务和路由。
- B. 技术分层：按角色分组，如模型、服务、路由、数据和测试。
- C. 扁平直到需要：保持 `src/` 布局简单，直到嵌套明显有帮助时才分层。
- D. 工具或框架布局：遵循所选框架、包工具或模板期望的结构。

**代理评分：**
- A：领域/特性隔离、模块化所有权，适合增长的产品。
- B：分层架构、按技术角色常规分离。
- C：最小结构、低导入复杂度，痛苦出现时才重构。
- D：约定优先、重视与工具和生态系统期望的兼容性。

**模式信号：**
- A：支持有界上下文、每个特性的 [Facade](../patterns/gof/facade.md)、本地适配器。
- B：支持服务层和 MVC 式组织。
- C：支持过程式/函数优先代码和低抽象。
- D：支持框架对齐设计和模板驱动结构。

**CodeStyle 输出影响：**
定义 Agent 应在何处创建新模块，以及何时可以引入子文件夹。在相关时包含源码与本地数据分离。

---

## Q7. 测试理念

**维度：**
测试优先覆盖 vs 集成置信 vs 核心逻辑聚焦 vs 手动/日志驱动迭代。

**用户面对的场景：**
测试需要时间编写和维护。这个项目的默认测试级别是什么？

**用户面对的说明：**
选择您最自然愿意维护的风格。您可以随时修改之前的答案。

**代码示例：**
无。选项是关于测试范围和审查期望。

**选项：**
- A. 测试优先且广泛覆盖：尽早编写测试，覆盖分支、边界情况和重要失败路径。
- B. 集成密集：聚焦端点、数据库边界、CLI 流程或完整工作流。
- C. 仅核心逻辑：测试自定义算法和业务规则，但不测试框架样板。
- D. 手动和日志优先：快速推进，手动测试，依靠日志或用户反馈，直到项目稳定。

**代理评分：**
- A：高测试纪律、回归预防、变更较慢但更安全。
- B：行为和边界置信，对单元测试每个辅助函数兴趣较低。
- C：ROI 聚焦测试、保护自定义逻辑同时避免低价值测试。
- D：原型速度、低自动化测试期望、较高回归风险。

**模式信号：**
- A：支持契约测试、适配器、严格接口。
- B：支持 [Facade](../patterns/gof/facade.md)/API 测试和集成边界。
- C：支持算法优先和函数优先测试。
- D：避免需要大量测试脚手架的重量级抽象。

**CodeStyle 输出影响：**
为生成的代码和未来 Agent 编辑设置最低测试要求。定义新功能是否需要单元测试、集成测试、冒烟测试或手动验证说明。

---

## Q8. 注释与文档字符串

**维度：**
自文档代码 vs 为什么导向注释 vs 严格文档字符串 vs AI 面向上下文注释。

**用户面对的场景：**
AI Agent 可能过度解释代码。这个项目应强制执行什么注释和文档字符串风格？

**用户面对的说明：**
选择您最自然愿意维护的风格。您可以随时修改之前的答案。

**代码示例：**
无。选项是关于注释策略和文档密度。

**选项：**
- A. 最小注释：代码应足够清晰，注释罕见；文档字符串主要用于公共 API。
- B. 解释为什么：避免重复代码的注释，但解释业务规则、约束和非显而易见的决策。
- C. 完整文档字符串：大多数类、方法和函数使用一致的文档字符串风格。
- D. AI 上下文注释：允许注释作为计划标记或未来 Agent 编辑的上下文，当它们减少困惑时。

**代理评分：**
- A：自文档偏好、低注释密度。
- B：上下文优先注释、中等文档字符串、高审查价值。
- C：文档密集、API 参考友好、较高维护成本。
- D：Agent 协作友好、接受注释作为未来编辑指导和引导重构。

**模式信号：**
- A：最适合清晰的命名和小型函数。
- B：支持领域驱动规则和边界文档。
- C：支持公共库/API 风格和严格接口。
- D：支持 Agent 工作流、计划/规范标记和引导重构。

**CodeStyle 输出影响：**
定义 Agent 应何时添加注释、文档字符串、计划笔记和上下文标记。也定义清理时应移除哪些类型的注释。

---

## Q9. Git 历史与协作

**维度：**
快速主线提交 vs 常规 PR 流程 vs 发布分支 vs 线性历史 vs 无 Git 偏好。

**用户面对的场景：**
当人类和 AI Agent 共同生成代码时，Git 历史和分支风格应是什么样的？

**用户面对的说明：**
选择您最自然愿意维护的风格。您可以随时修改之前的答案。

**代码示例：**
无。选项是关于协作工作流，而非 Python 代码。

**选项：**
- A. 快速主线：直接提交到 `main` 或一个共享 `dev` 分支，附以简短的描述性消息。
- B. 常规分支：使用特性分支、PR 和 `feat:`、`fix:`、`refactor:` 等消息格式。
- C. 发布分支：保持 `main` 聚焦生产，使用集成和发布分支，隔离热修复。
- D. 线性历史：压缩或变基，使历史读作干净序列，没有合并提交。
- E. 无强 Git 偏好：保持 Git 要求轻量，不将工作流作为主要约束。

**代理评分：**
- A：速度优先协作、低流程开销。
- B：常规、审查友好、自动化友好。
- C：发布管理纪律、更强的环境分离。
- D：历史清洁度、偏好策划提交。
- E：Git 轻量、最可能需要最少的 Agent 假设。

**模式信号：**
- A：支持快速原型和直接编辑。
- B：支持审查清单、CI 和结构化 Agent 提交。
- C：支持发布管理规范和部署门控。
- D：支持精心策划的补丁集和仔细的重构。
- E：避免在生成的风格文件中过度指定 Git 行为。

**CodeStyle 输出影响：**
为未来 Agent 工作设置提交消息、分支、PR 和历史期望。如果选择 E，保持 Git 指导最少。

---

## Q10. 依赖与环境

**维度：**
标准 pip/venv vs conda 环境 vs 锁文件包管理器 vs 新一代 Rust 工具。

**用户面对的场景：**
Python 依赖管理可以塑造整个项目。应如何管理环境和第三方库？

**用户面对的说明：**
选择您最自然愿意维护的风格。您可以随时修改之前的答案。

**代码示例：**

```text
A. requirements.txt + venv
B. environment.yml + conda/miniconda
C. pyproject.toml + poetry.lock 或 Pipfile.lock
D. pyproject.toml / uv.lock / 内联脚本元数据
```

**选项：**
- A. 标准 `pip` 和 `venv`：使用 `requirements.txt` 和内置虚拟环境保持设置简单。
- B. Conda 风格环境：当数据科学包或原生依赖重要时，使用 `conda` 或 `miniconda`。
- C. 锁文件包管理器：使用 Poetry 或 Pipenv 获得结构化配置和可复现的锁文件。
- D. 新一代快速工具：使用 `uv` 或 `rye` 等工具进行快速解析和现代 Python 项目工作流。

**代理评分：**
- A：最小工具、广泛兼容性、简单设置。
- B：数据科学友好、原生依赖感知、以环境文件为中心。
- C：可复现优先、结构化项目元数据、锁文件纪律。
- D：现代工具偏好、速度优先依赖管理。

**模式信号：**
- A：支持轻量脚本和简单包。
- B：支持研究/数据工作流和环境密集型项目。
- C：支持包/库风格和 CI 可复现性。
- D：支持现代 Agent 工作流和快速迭代。

**CodeStyle 输出影响：**
设置依赖策略、环境文件、安装命令，以及 Agent 是否可以添加新库。包括依赖的优先信任来源。
