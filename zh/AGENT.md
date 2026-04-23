# CodeBTI Agent 指南

## 项目概述

CodeBTI 是 MBTI 的代码风格版本。MBTI 描述人格偏好；CodeBTI 描述一个项目或通用工程身份的编码和设计偏好。

目标不是制作一个玩具式的人格测验。目标是帮助 AI Agent 和人类开发者明确选择贯穿整个项目的编码风格、架构边界、设计模式和审查标准。最终结果应足够实用，可以成为 `SKILL.md`、项目 `SPEC.md` 或可复用的 `CodeStyle.md`。

当前版本专注于 Python。仓库的组织方式使后续添加其他语言时无需更改核心工作流。

## 目标受众

本仓库面向 Agent。AI 编码 Agent 应能直接阅读并理解：

- CodeBTI 是什么，
- 如何进行用户访谈，
- 如何记录答案，
- 如何推断编码风格 Profile，
- 如何生成项目专属的 `CodeStyle.md`，
- 如何用新语言或设计模式示例扩展系统。

所有主要内容包括纯 markdown。初始版本避免运行时依赖、Web 应用、二进制资源和工具专属格式。

## 仓库结构

```
CodeBTI/
  SKILL.md          # 可安装技能入口
  AGENT.md          # Agent 指南和工作流参考
  README.md         # 人类入口
  zh/               # 简体中文翻译包
    README.md
    SKILL.md
    AGENT.md
    example/
    python/
      questions/
      patterns/
      profiles/
      records/
      templates/
  python/
    questions/
    patterns/
    profiles/
    records/
    templates/
```

`zh/` 目录是简体中文翻译包，结构与根目录平行。所有文件名保持英文，以便内部路径引用保持一致。`zh/SKILL.md` 和 `zh/AGENT.md` 是中文 Agent 的主要入口。

## 核心工作流

1. 用户描述想构建的内容。
2. Agent 在目标项目中创建或更新实时的 `Recording.md`。
3. Agent 提出所选语言的 10 个固定问题（当前为 Python）。
4. 每个问题之前，Agent 将完整题目卡保存到 `Recording.md`；每次回答后，更新答案日志并给出简短项目反馈，再问下一个问题。
5. Agent 使用适应性追问指南提出恰好 5 个后续追问。
6. Agent 重新阅读 `Recording.md` 并将其作为事实来源。
7. Agent 使用相关语言 Profile 分类体系和模式数据库分析答案。
8. Agent 选择支撑建议的具体本地模式/资源引用。
9. Agent 从输出模板生成详细的项目 `CodeStyle.md`，包含引用和每句一句的相关性说明。
10. 如适用，Agent 将 `Recording.md` 保存为最终会话记录，并将风格指导提炼为 `SKILL.md` 或 `SPEC.md`。

## 当前状态

Python 优先的 CodeBTI 基础已实现：

- 人类入口：`README.md`，
- Agent 指南：`AGENT.md`，
- 可安装技能入口：`SKILL.md`，
- 固定问题集：`python/questions/fixed-python.md`，
- 适应性追问指南：`python/questions/adaptive-question-guide.md`，
- 问题编辑规则：`python/questions/editorial-guide.md`，
- 22 页 Python 设计模式数据库：`python/patterns/python/`，
- Python Profile 分类体系：`python/profiles/python-profile-taxonomy.md`，
- 会话记录模板：`python/records/session-record.template.md`，
- 输出模板：`python/templates/CodeStyle.template.md`、`python/templates/SKILL.template.md`、`python/templates/SPEC.template.md`，
- 简体中文翻译包：`zh/`。

当前版本无自动化脚本、CLI、Web 应用或 CI 系统。

## 文件类型职责

### 入口文件

入口文件给 Agent 提供继续所需的最小上下文。`SKILL.md` 是可安装技能入口。`AGENT.md` 提供额外的工作流指导。`README.md` 向人类解释 CodeBTI 并链接到主工作流。

入口文件应简洁、可操作且稳定。避免将重要说明埋在长篇论述中。

### 设计模式示例

模式文件描述真实的工程偏好。不应简单罗列抽象模式。每个文件应说明：

- 该风格选择，
- 何时有用，
- 何时变得有害，
- 在 Python 中的样子，
- 用户答案中哪些信号暗示这种偏好，
- 生成的代码或审查评论中应如何体现该偏好。

模式示例是通用参考资料。生成的 `CodeStyle.md` 应针对具体项目。当前的 Python 模式数据库采用经典 GoF 目录结构，并在每个模式页面引用 RefactoringGuru 来源。

### 问答表

固定的 Python 问答表包含 10 个基于示例的问题，涵盖：

- 通用目的和范式，
- 防御性编程和类型边界，
- 错误处理和恢复，
- 命名和可读性，
- 架构和接线风格，
- 文件夹结构，
- 测试理念，
- 注释和文档字符串，
- Git 历史和协作，
- 依赖和环境。

适应性追问指南指导 Agent 根据模糊、矛盾、项目风险、强烈信号和可能的模式误用提出恰好 5 个后续追问。

### 记录

每次访谈应在访谈进行时增量记录。默认实时文件名：

```text
Recording.md
```

实时记录应放在目标项目根目录，以便另一个 Agent 在上下文丢失时能恢复访谈状态。访谈结束后，可保留为 `Recording.md` 或复制到语言包的 `records/` 目录，使用带日期戳的文件名，例如：

```text
python/records/2026-04-22-my-python-cli.md
```

会话记录应包含：

- 项目摘要，
- 访谈进度，
- 完整题目卡快照，
- 按时间顺序的答案日志，
- 固定问题和答案，
- 适应性问题及答案，
- 每次回答后的简短反馈，
- Agent 观察，
- 推断的 CodeBTI Profile，
- 生成的输出文件，
- 未解决的假设。

不记录秘密、私人凭证或无关个人信息。

### 生成输出

主要生成产物是 `CodeStyle.md`。它应足够具体，使 Agent 在实现和审查时都能使用。

一份强有力的 `CodeStyle.md` 应定义：

- 项目意图，
- 首选架构，
- 模块边界，
- 命名约定，
- 类型策略，
- 错误处理策略，
- 依赖策略，
- 测试策略，
- 文档策略，
- 首选代码示例，
- 避免的代码示例，
- 审查清单，
- 未来 Agent 行为说明。
- 支撑建议的本地模式/资源页面引用。

需要时，相同指导可提炼为：

- `SKILL.md`（可复用的 Agent 行为），
- `SPEC.md`（项目需求），
- 或更窄的专项规范，如 `API_SPEC.md`、`TESTING_SPEC.md`、`ARCHITECTURE_SPEC.md`。

## CodeBTI Profile 概念

CodeBTI 应产生令人难忘的 Profile 名称，但 Profile 必须保持工程基础。Profile 是一组设计偏好的简写，而非详细指导的替代品。

初始 Python 版本在以下实用轴上定义 Profile：

- 抽象：本地具体 vs 分层泛化。
- 类型纪律：动态实用 vs 严格显式。
- 状态模型：可变工作流 vs 不可变转换。
- 错误模型：异常、结果对象、前置验证或快速失败。
- 依赖姿态：标准库优先 vs 生态友好。
- 测试风格：行为优先、单元优先、属性优先、集成优先或冒烟测试优先。

当前 Python 分类体系定义了实用的 Profile 系列：

- `对象中心边界守护者 (Object-Centered Boundary Keeper)`
- `函数优先流水线构建者 (Function-First Pipeline Builder)`
- `数据优先验证者 (Data-First Validator)`
- `务实的脚本构建者 (Pragmatic Script Builder)`
- `测试优先集成者 (Test-First Integrator)`
- `框架对齐构建者 (Framework-Aligned Builder)`
- `算法优先极简主义者 (Algorithm-First Minimalist)`

使用 `python/profiles/python-profile-taxonomy.md` 作为初始 Python 分类体系，并根据新的访谈数据不断完善。

## 初始 Python 范围

第一个版本应专注于 Python 项目，包括：

- 包，
- 命令行工具，
- 数据处理脚本，
- API，
- 转换为可维护模块的笔记本，
- Agent 编写的基础脚手架。

Python 指导应至少覆盖：

- 项目布局，
- 导入，
- 类型注解，
- dataclass 和 Pydantic 风格模型，
- 异常，
- 日志，
- 配置，
- 依赖管理，
- 测试，
- 脚本和 CLI，
- 文档字符串，
- 审查期望。

不要将系统过度适配单一框架。框架专属指导应作为可选扩展添加。

## 扩展模型

未来语言应通过创建平行的语言目录添加，而非重写核心工作流。

示例：

```text
python/
  questions/
    fixed-python.md
    fixed-typescript.md
  patterns/
    python/
    typescript/
  profiles/
    python-profile-taxonomy.md
    typescript-profile-taxonomy.md
```

通用工作流应保持语言中立。语言目录应持有语言专属的示例、问题和分类细节。

## Agent 行为规则

当 Agent 在本仓库工作时：

- 除非用户明确要求工具化，否则优先使用 markdown 文件而非代码。
- 保持源文件对人类和 Agent 都可读。
- 生成的模板应结构清晰、易于填充。
- 避免无法指导实现的模糊风格建议。
- 包含权衡，而非仅是规则。
- 保留会话记录作为生成建议的证据。
- 将 CodeBTI 结果视为项目指导，而非个人评判。
- 保持 Python 为第一实现目标，同时为其他语言留出空间。

## 当前完成定义

Python 优先的 markdown 基础在包含以下内容时即为就绪：

- 根 `SKILL.md` 作为可安装技能入口，
- `AGENT.md`，
- 面向人类的 `README.md`，
- `python/questions/` 中的固定 Python 问题集，
- `python/questions/` 中的适应性追问指南，
- `python/patterns/` 中的模式索引，
- `python/patterns/python/` 中的 22 个 Python GoF 模式页面，
- `python/profiles/` 中的 Profile 分类体系草案，
- `python/records/` 中的会话记录模板，
- `python/templates/` 中的 `CodeStyle.md` 模板，
- `python/templates/` 中 `SKILL.md` 和 `SPEC.md` 的输出模板，
- `python/records/` 文件夹中的记录指南，
- 所有本地 markdown 链接均可解析，
- `zh/` 简体中文翻译包。

具备这些文件后，用户可以请求 AI Agent 运行 CodeBTI 访谈，并收到实用的项目专属 `CodeStyle.md`。
