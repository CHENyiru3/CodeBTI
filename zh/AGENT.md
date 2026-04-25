# CodeBTI Agent 指南

## 项目概述

CodeBTI 是 MBTI 的代码风格版本。MBTI 描述人格偏好；CodeBTI 描述一个项目或通用工程身份的编码和设计偏好。

目标不是制作一个玩具式的人格测验。目标是帮助 AI Agent 和人类开发者明确选择贯穿整个项目的编码风格、架构边界、设计模式和审查标准。最终结果应足够实用，可以成为 `SKILL.md`、项目 `SPEC.md` 或可复用的 `CodeStyle.md`。

当前版本支持 Python 和 TypeScript。仓库的组织方式使后续添加其他语言时无需更改核心工作流。

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
├── SKILL.md              # 可安装技能入口
├── AGENT.md              # Agent 指南和工作流参考
├── README.md             # 人类入口
├── MANIFEST.md           # 文件清单
│
├── shared/               # 语言中立资源，所有语言包共享
│   ├── questions/
│   │   ├── adaptive-question-guide.md
│   │   ├── editorial-guide.md
│   │   ├── question-format.md
│   │   └── shared-architecture.md
│   ├── records/
│   │   └── session-record.template.md
│   └── templates/
│       ├── SKILL.template.md
│       └── SPEC.template.md
│
├── python/               # Python 语言包
│   ├── questions/
│   │   ├── README.md
│   │   └── fixed-python.md
│   ├── patterns/
│   │   ├── README.md
│   │   └── gof/          # 22 个 GoF 模式页面
│   │       ├── README.md
│   │       └── [22 pattern files]
│   ├── profiles/
│   │   ├── README.md
│   │   └── python-profile-taxonomy.md
│   ├── records/
│   │   └── README.md
│   └── templates/
│       ├── README.md
│       └── CodeStyle.template.md
│
├── typescript/           # TypeScript 语言包
│   ├── questions/
│   │   ├── README.md
│   │   └── fixed-typescript.md
│   ├── patterns/
│   │   ├── README.md
│   │   └── gof/          # 22 个 GoF 模式页面
│   │       ├── README.md
│   │       └── [22 pattern files]
│   ├── profiles/
│   │   ├── README.md
│   │   └── python-profile-taxonomy.md
│   ├── records/
│   │   └── README.md
│   └── templates/
│       ├── README.md
│       └── CodeStyle.template.md
│
├── examples/             # 已完成的 Python GUI 计算器示例
└── zh/                    # 简体中文翻译
    ├── AGENT.md
    ├── README.md
    ├── SKILL.md
    ├── TRANSLATION_STATUS.md
    ├── shared/           # 镜像英文 shared/ 层
    ├── python/            # 翻译版 Python 语言包
    └── examples/           # 翻译版示例
```

`zh/` 目录是简体中文翻译包，结构与根目录平行。所有文件名保持英文，以便内部路径引用保持一致。`zh/SKILL.md` 和 `zh/AGENT.md` 是中文 Agent 的主要入口。

## 核心工作流

1. 用户描述想构建的内容和主要语言。
2. Agent 在目标项目中创建或更新实时的 `Recording.md`。
3. Agent 提出目标语言 `questions/fixed-<lang>.md` 中的 10 个固定问题。
4. 每个问题之前，Agent 将完整题目卡保存到 `Recording.md`；每次回答后，更新答案日志并给出简短项目反馈，再问下一个问题。
5. Agent 使用 `shared/questions/adaptive-question-guide.md` 提出恰好 5 个适应性后续追问。
6. Agent 重新阅读 `Recording.md` 并将其作为事实来源。
7. Agent 使用该语言的 `profiles/<lang>-profile-taxonomy.md` 和 `patterns/gof/` 中的模式数据库分析答案。
8. Agent 选择支撑建议的具体本地模式/资源引用。
9. Agent 从语言包的 `templates/CodeStyle.template.md` 生成详细的项目 `CodeStyle.md`，包含引用和每句一句的相关性说明。
10. 如适用，Agent 将 `Recording.md` 保存为最终会话记录，并使用 `shared/templates/SKILL.template.md` 和 `shared/templates/SPEC.template.md` 将风格指导提炼为 `SKILL.md` 或 `SPEC.md`。

**多语言项目**：第一轮完成后，可以为其他语言运行较短的访谈。在 `Recording.md` 中分语言记录各组答案，合并为一份项目级 `CodeStyle.md`。

## 当前状态

Python 和 TypeScript 语言包已实现，带有共享层：

- 人类入口：`README.md`，
- Agent 指南：`AGENT.md`，
- 可安装技能入口：`SKILL.md`，
- 共享面试资源：`shared/questions/`、`shared/templates/`、`shared/records/`，
- Python 固定问题集：`python/questions/fixed-python.md`，
- TypeScript 固定问题集：`typescript/questions/fixed-typescript.md`，
- 22 页 Python 设计模式数据库：`python/patterns/gof/`，
- 22 页 TypeScript 设计模式数据库：`typescript/patterns/gof/`，
- Python Profile 分类体系：`python/profiles/python-profile-taxonomy.md`，
- TypeScript Profile 分类体系：`typescript/profiles/typescript-profile-taxonomy.md`，
- Python `CodeStyle.md` 模板：`python/templates/CodeStyle.template.md`，
- TypeScript `CodeStyle.md` 模板：`typescript/templates/CodeStyle.template.md`，
- 共享 SKILL 和 SPEC 模板：`shared/templates/`，
- 共享会话记录模板：`shared/records/session-record.template.md`，
- 已完成示例：`examples/`。

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

## Profile 概念

CodeBTI 应产生令人难忘的 Profile 名称，但 Profile 必须保持工程基础。Profile 是一组设计偏好的简写，而非详细指导的替代品。

每种语言包的分类体系在以下实用轴上定义 Profile：

- **抽象**：本地具体 vs 分层泛化。
- **类型纪律**：动态实用 vs 严格显式。
- **状态模型**：可变工作流 vs 不可变转换。
- **错误模型**：异常、结果对象、前置验证或快速失败。
- **依赖姿态**：标准库优先 vs 生态友好。
- **测试风格**：行为优先、单元优先、属性优先、集成优先或冒烟测试优先。

当前 Python 分类体系定义了 7 个实用的 Profile 系列：

- `对象中心边界守护者 (Object-Centered Boundary Keeper)`
- `函数优先流水线构建者 (Function-First Pipeline Builder)`
- `数据优先验证者 (Data-First Validator)`
- `务实的脚本构建者 (Pragmatic Script Builder)`
- `测试优先集成者 (Test-First Integrator)`
- `框架对齐构建者 (Framework-Aligned Builder)`
- `算法优先极简主义者 (Algorithm-First Minimalist)`

当前 TypeScript 分类体系定义了 7 个 TypeScript 专属的 Profile 系列：

- `接口优先边界守护者 (Interface-First Boundary Keeper)`
- `类中心状态架构师 (Class-Centered State Architect)`
- `数据模型类型别名者 (Data-Model Type Aliaser)`
- `函数式流水线构建者 (Functional Pipeline Builder)`
- `框架对齐构建者 (Framework-Aligned Builder)`
- `测试优先集成者 (Test-First Integrator)`
- `算法优先极简主义者 (Algorithm-First Minimalist)`

## 语言包范围

每种语言包的指导应至少覆盖：

- 项目布局，
- 导入和模块结构，
- 类型策略（Python：类型注解 vs 鸭子类型；TypeScript：`interface` vs `type` 别名），
- 数据模型（Python：dataclass、pydantic；TypeScript：interface、type、class），
- 错误处理和异常模型，
- 日志和配置，
- 依赖管理，
- 测试策略，
- 脚本和 CLI（Python：argparse、click；TypeScript：commander、yargs），
- 文档字符串和注释规范，
- 审查期望。

不要将系统过度适配单一框架。框架专属指导应作为可选扩展添加。

## 扩展模型

未来语言应作为同级目录添加。每种语言包拥有其固定问题、模式页面、Profile 分类体系和 `CodeStyle.md` 模板。`shared/` 中的共享面试资源供所有语言包使用，无需修改。

```
CodeBTI/
  shared/               # 所有语言包共享
  python/
  typescript/
  rust/                 # 新语言包
    questions/fixed-rust.md
    patterns/gof/
    profiles/rust-profile-taxonomy.md
    templates/CodeStyle.template.md
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
- 支持多语言项目——第一语言确立默认值，后续语言补充或覆盖。

## 完成定义

语言包在包含以下内容时即为就绪：

- `questions/fixed-<lang>.md` — 10 个固定问题，
- `patterns/README.md` — 模式索引，
- `patterns/gof/` — 22 个 GoF 模式页面，
- `profiles/<lang>-profile-taxonomy.md` — Profile 分类体系草案，
- `templates/CodeStyle.template.md` — `CodeStyle.md` 输出模板。

`shared/` 中的共享资源不需按语言复制——它是共享的，不需要每个语言包维护一份。

具备这些文件后，用户可以请求 AI Agent 运行 CodeBTI 访谈，并收到实用的项目专属 `CodeStyle.md`。
