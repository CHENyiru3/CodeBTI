# CodeBTI Agent 指南

## 项目摘要

CodeBTI 是 MBTI 的代码风格对应物。MBTI 描述人格偏好；CodeBTI 描述一个项目或工程上下文中的编码与设计偏好。

目标不是创建玩具人格测试，而是帮助 AI Agent 和人类开发者明确选择项目工作流、架构边界、设计模式、审查标准、测试策略、依赖策略和语言特定编码风格，使这些规则在整个项目中保持一致。

本仓库是 Markdown-first 且面向 Agent 的。AI 编码 Agent 应能直接阅读它，理解如何运行访谈、记录答案、推断 Profile，并生成项目指导。

## 仓库形态

```text
CodeBTI/
  SKILL.md              # 可安装 skill 入口和路由器
  AGENT.md              # Agent 指南和工作流参考
  README.md             # 人类入口
  MANIFEST.md           # 文件清单
  project/              # 项目级访谈包
    questions/fixed-project.md
    profiles/project-profile-taxonomy.md
    templates/ProjectStyle.template.md
  shared/               # 语言中立访谈资源
    questions/
      adaptive-question-guide.md
      editorial-guide.md
      question-format.md
      shared-architecture.md
    templates/
      SKILL.template.md
      SPEC.template.md
    records/
      session-record.template.md
  python/               # Python 语言包
  typescript/           # TypeScript 语言包
  scripts/              # 验证工具
  .github/workflows/    # CI 验证
  docs/                 # 操作工作流指南
  examples/             # 已完成的单语言示例
  zh/                   # 简体中文翻译
```

根目录 `SKILL.md` 是可安装 skill 入口。它将每个 CodeBTI 会话先路由到项目包，然后进入一个或多个语言包。

## 核心工作流

1. 用户回答一个 SPEC 风格开场提示，说明使命、目标、受众、约束、可能的技术栈/语言、路线图意图、非目标和开放问题。
2. Agent 识别目标语言包。如果不明确，在计分问题前提出一个简短澄清问题。
3. Agent 在目标项目中创建或更新实时 `Recording.md`。
4. Agent 在 what/why 层级创建或更新初始 `SPEC.md` 草稿。
5. Agent 询问 `project/questions/fixed-project.md` 中的 6 个固定项目问题。
6. Agent 对每个所选语言包询问固定问题，例如 Python 或 TypeScript。
7. 每个计分问题之前，Agent 将完整题目卡保存到 `Recording.md`。
8. 每次回答后，Agent 更新答案日志，并在下一个问题前给出简短项目反馈。
9. Agent 使用 `shared/questions/adaptive-question-guide.md` 在整个会话中总共提出恰好 5 个适应性后续追问。
10. Agent 重新阅读 `Recording.md` 和 `SPEC.md`，并将它们作为事实来源。
11. Agent 使用 `project/profiles/project-profile-taxonomy.md` 分析项目级答案。
12. Agent 使用每个语言的 Profile taxonomy 和 `patterns/gof/` 数据库分析语言答案。
13. Agent 只选择对建议有实质影响的本地模式/资源引用。
14. Agent 生成请求的指导：`CodeStyle.md`、可选 `ProjectStyle.md`、可选 `SKILL.md`、可选 `SPEC.md` 或更细的规范文件。

验证或讲解工作流时，使用英文 `docs/golden-path.md` 作为操作清单。

## 当前状态

项目包、Python 包和 TypeScript 包已经实现，并共享同一层共享资源。

- 人类入口：`README.md`
- 发布说明：`CHANGELOG.md`
- golden path 指南：`docs/golden-path.md`
- Agent/路由入口：`SKILL.md`
- Agent 指南：`AGENT.md`
- 项目级问题：`project/questions/fixed-project.md`
- 项目 Profile taxonomy：`project/profiles/project-profile-taxonomy.md`
- 共享访谈资源：`shared/questions/`、`shared/templates/`、`shared/records/`
- Python 固定问题表：`python/questions/fixed-python.md`
- TypeScript 固定问题表：`typescript/questions/fixed-typescript.md`
- Python 22 页设计模式数据库：`python/patterns/gof/`
- TypeScript 22 页设计模式数据库：`typescript/patterns/gof/`
- 验证脚本：`scripts/validate_repo.py`
- 质量测试：`tests/`
- CI 工作流：`.github/workflows/validate.yml`
- 简体中文翻译：`zh/`

当前版本不包含运行时访谈应用。

## 文件职责

### 入口文件

入口文件给 Agent 提供继续工作的最小上下文。`SKILL.md` 应保持可执行且简洁。`README.md` 面向人类解释 CodeBTI。`AGENT.md` 定义仓库维护预期。

### 项目包

项目包包含跨项目问题和 Profile 指导，控制：

- 协作工作流，
- 输出形态，
- 验证门禁，
- 共享规则与语言规则边界，
- 依赖治理，
- 变更记录政策。

语言包不应重复这些决策，除非语言特定覆盖是必要的并已记录。

### 语言包

每个语言包拥有自己的固定问题、模式页面、Profile taxonomy、记录指南和 `CodeStyle.md` 模板。语言包应使用共享访谈机制和共享输出模板，而不是复制它们。

### 共享层

共享文件必须保持项目和语言中立。它们用于问题格式、适应性追问规则、编辑规则、会话记录结构，以及语言中立的 SKILL/SPEC 模板。

如果某个包需要偏离共享规则，在该包中记录冲突。不要把共享文件 fork 到语言包中。

### 设计模式示例

模式文件描述真实工程偏好。每个文件应解释：

- 风格选择，
- 何时有用，
- 何时有害，
- 在目标语言中是什么样子，
- 用户答案中的哪些信号暗示该偏好，
- 以及该偏好应如何出现在生成代码或审查意见中。

生成的 `CodeStyle.md` 应是项目特定的。只引用真实影响建议的模式页面。

### 记录

每个会话都应在访谈进行时增量记录。默认实时文件名是：

```text
Recording.md
```

实时记录应放在目标项目根目录，以便另一个 Agent 在上下文丢失时恢复访谈状态。使用 `shared/records/session-record.template.md` 作为起点。

会话记录应包含：

- 项目摘要和 SPEC intake，
- 初始 `SPEC.md` 草稿引用，
- 语言目标，
- 访谈进度，
- 完整题目卡快照，
- 按时间顺序的答案日志，
- 项目固定答案，
- 语言固定答案，
- 适应性答案，
- 每次回答后的反馈，
- 隐藏推理笔记，
- 推断出的项目和语言 Profile，
- 生成的输出文件，
- 验证结果，
- 未解决假设。

不要记录秘密、私有凭证或无关个人信息。

## 生成输出

主要生成物是 `CodeStyle.md`。它应足够具体，使 Agent 能在实现和审查时直接使用。

强 `CodeStyle.md` 应定义：

- 项目意图，
- 共享项目规则，
- 首选架构，
- 模块边界，
- 语言特定风格规则，
- 类型策略，
- 错误处理策略，
- 依赖策略，
- 测试策略，
- 文档策略，
- 推荐代码示例，
- 避免代码示例，
- 审查清单，
- 未来 Agent 行为说明，
- 本地模式/资源页面引用。

需要时生成：

- `ProjectStyle.md`：项目工作流和治理，
- `SKILL.md`：可复用 Agent 行为，
- `SPEC.md`：项目专属需求，
- `API_SPEC.md`、`TESTING_SPEC.md` 或 `ARCHITECTURE_SPEC.md` 等更细规范。

对于 SPEC 驱动开发，`SPEC.md` 是持续演进的 what/why 文档。每次 feature 实现之间，如果使命、约束、技术栈、路线图或开放问题变化，重新阅读并更新它，然后在 `Recording.md` 中记录 replanning 理由。

## Profile 概念

CodeBTI Profile 是工程简写，不是能力或人格评判。

项目 Profile 描述工作流和治理偏好，例如：

- `Controlled Multi-Language Maintainer`
- `Lightweight Prototype Collaborator`
- `Review-Gated Integrator`
- `Release-Managed Steward`

语言 Profile 描述编码风格偏好，例如：

- Python `Object-Centered Boundary Keeper`
- Python `Data-First Validator`
- TypeScript `Interface-First Boundary Keeper`
- TypeScript `Functional Pipeline Builder`

混合结果应表达为组合 Profile，而不是强行归入单一干净标签。

## 扩展模型

未来语言应作为同级目录添加。每个语言包拥有自己的固定问题、模式页面、Profile taxonomy、记录指南和 `CodeStyle.md` 模板。`shared/` 中的共享访谈资源由所有包使用，不做修改。

```text
CodeBTI/
  shared/
  project/
  python/
  typescript/
  rust/
    questions/fixed-rust.md
    patterns/gof/
    profiles/rust-profile-taxonomy.md
    records/README.md
    templates/CodeStyle.template.md
```

添加或修改包后，更新 `README.md`、`AGENT.md` 和 `MANIFEST.md`，然后运行：

```sh
python3 scripts/validate_repo.py
python3 -m pytest
```

## 验证门禁

仓库有轻量验证门禁，检查：

- 本地 Markdown 链接，
- 必需包文件，
- 固定问题数量和必需章节，
- 固定问题 ID/范围质量，
- 选项、评分和模式信号标签是否一致，
- 必需模板章节，
- 中文共享镜像覆盖，
- manifest 漂移。

提交前运行：

```sh
python3 scripts/validate_repo.py
python3 -m pytest
```

GitHub Actions 会在 pull request 和 push 上运行同一命令。

发布加固类变更还应运行：

```sh
git diff --check
PYTHONPYCACHEPREFIX=/tmp/codebti_pycache python3 -m py_compile scripts/validate_repo.py
```

## Agent 行为规则

当 Agent 在本仓库工作时：

- 除非用户明确要求工具，否则优先修改 Markdown。
- 保持源文件同时适合人类和 Agent 阅读。
- 保持 `shared/` 语言中立。
- 将项目级工作流决策放在 `project/`。
- 将语言特定示例、模式和 Profile 规则放在语言包内。
- 避免无法指导实现的模糊风格建议。
- 包含权衡，而不仅是规则。
- 保留会话记录作为生成建议的证据。
- 将 CodeBTI 结果视为项目指导，而非个人评判。
- 在结构、链接、问题、模板或 manifest 变更后运行 `python3 scripts/validate_repo.py`。

## 完成定义

一次变更准备就绪时应满足：

- 文档描述同一个一致工作流，
- 相关问题/Profile/模板文件一起更新，
- 共享文件变化时同步更新中文镜像，
- `MANIFEST.md` 反映新增文件或目录，
- `python3 scripts/validate_repo.py` 通过，
- `python3 -m pytest` 通过，
- 发布加固类变更还通过 `git diff --check` 和 `py_compile`。
