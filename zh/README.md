# CodeBTI

![CodeBTI 概览](https://i.imgur.com/annGWpK.jpeg)

CodeBTI 是 MBTI 的代码风格版本，为软件项目服务。它帮助人类开发者和 AI Agent 在实现之前，选择一套一致的编码风格、设计模式姿态、测试策略、依赖策略和协作流程。

CodeBTI 不是人格测试。它是一套实用的访谈与文档系统，用来生成项目专属的指导文件，如 `CodeStyle.md`、`SKILL.md` 或 `SPEC.md`。

## 安装为 Skill

本仓库可直接安装为 Codex skill。将本仓库复制或安装到 Codex skills 目录中，命名为 `codebti`。根目录的 `SKILL.md` 即为入口文件。

## 工作原理 — 单语言项目

适用于使用一种主要语言的项目：

1. 用户描述项目及其语言。
2. Agent 在目标项目中创建一份实时的 `Recording.md`，并记录项目摘要。
3. Agent 针对选定语言提出 `questions/fixed-<lang>.md` 中的 10 个固定问题。
4. 每个问题之前，Agent 将完整的题目卡保存到 `Recording.md`；用户回答后，更新答案日志并给出简短的项目反馈，再问下一个问题。
5. Agent 使用 `shared/questions/adaptive-question-guide.md` 提出恰好 5 个适应性后续追问。
6. Agent 将 `Recording.md` 作为事实来源重新阅读。
7. Agent 根据该语言的 `profiles/<lang>-profile-taxonomy.md` 推断风格 Profile。
8. Agent 为该语言从 `patterns/gof/` 中选择相关的模式页面。
9. Agent 使用语言包中的 `templates/CodeStyle.template.md` 生成项目指导。

## 工作原理 — 多语言项目

适用于使用多种语言的项目（例如，Python 后端 + TypeScript 前端）。Agent 可以分语言运行多轮访谈：

1. **第一轮**：选择主要或最复杂的语言，运行完整的 10 固定 + 5 自适应问题流程。
2. **后续轮次**：第一份 `CodeStyle.md` 生成后，为第二种语言运行较短的访谈。在 `Recording.md` 中记录第二种语言的答案。Agent 可以生成第二份 `CodeStyle.md`，或将两份合并为一份项目级 `CodeStyle.md`，在其中定义语言间的边界。

对于多语言项目，Agent 应：

- 在 `Recording.md` 中标注每组答案属于哪种语言。
- 以第一种语言的 `CodeStyle.md` 作为跨语言共同事项的默认值（Git 工作流、依赖策略、测试策略）。
- 用后续轮次补充语言专属章节或覆盖默认值。
- 两轮访谈都引用同一个 `shared/` 面试资源——只有固定问题表和模式页面是语言专属的。

## 示例

[examples/](examples/) 目录中包含一个完整的 CodeBTI 访谈记录，针对一个小型 Python GUI 计算器。

- [examples/Recording.md](examples/Recording.md)：完整访谈记录，包含项目摘要、10 个固定答案、5 个自适应答案、反馈、隐藏推理笔记和最终 Profile 推断。
- [examples/CodeStyle.md](examples/CodeStyle.md)：生成的项目风格指南。

推断出的 Profile 为 **算法优先极简主义者（Algorithm-First Minimalist），具有对象中心边界特征**。最终指导建议：

- 在轻量 GUI 处理器背后放置一个小型 `Calculator` 对象，
- 直接的表达式/求值逻辑配合轻量级操作注册表，
- 对无效用户输入返回显式结果对象，
- 保持扁平项目结构，直到代码真正需要文件夹时才拆分，
- 对解析、优先级、无效输入和状态转换进行核心逻辑测试，
- 最小化注释，保持轻量类型注解，
- 使用 `uv`、`pyproject.toml` 和 `uv.lock` 进行依赖管理。

## 仓库结构

```
CodeBTI/
├── shared/                    # 所有语言包共享
│   ├── questions/             # 访谈流程和编辑规则
│   ├── records/               # 会话记录模板
│   └── templates/             # SKILL 和 SPEC 输出模板
│
├── python/                    # Python 语言包
│   ├── questions/             # fixed-python.md + README
│   ├── patterns/gof/          # 22 个 Python GoF 模式页面
│   ├── profiles/              # Profile 分类体系
│   ├── records/               # README
│   └── templates/             # CodeStyle.template.md
│
├── typescript/                # TypeScript 语言包
│   ├── questions/             # fixed-typescript.md + README
│   ├── patterns/gof/          # 22 个 TypeScript GoF 模式页面
│   ├── profiles/              # Profile 分类体系
│   ├── records/               # README
│   └── templates/             # CodeStyle.template.md
│
├── examples/                  # 完成的访谈示例
├── zh/                        # 简体中文翻译（镜像结构）
├── AGENT.md                   # Agent 指南
├── MANIFEST.md                # 文件清单
├── README.md                 # 本文件
└── SKILL.md                   # 可安装技能入口
```

**语言中立 vs 语言专属：**

| 资源 | 范围 | 示例 |
|------|------|------|
| 固定问题 | 按语言 | `python/questions/fixed-python.md`、`typescript/questions/fixed-typescript.md` |
| 模式页面 | 按语言 | `python/patterns/gof/facade.md`、`typescript/patterns/gof/facade.md` |
| Profile 分类体系 | 按语言 | `python/profiles/python-profile-taxonomy.md` |
| CodeStyle 模板 | 按语言 | `python/templates/CodeStyle.template.md`（含 Python 专属章节） |
| 适应性追问指南 | **共享** | `shared/questions/adaptive-question-guide.md` |
| 编辑规则 | **共享** | `shared/questions/editorial-guide.md` |
| 问题格式 | **共享** | `shared/questions/question-format.md` |
| 会话记录模板 | **共享** | `shared/records/session-record.template.md` |
| SKILL/SPEC 模板 | **共享** | `shared/templates/SKILL.template.md`、`shared/templates/SPEC.template.md` |

## 语言覆盖

可用语言包：

- **Python** — [python/](python/)：完整包，包含 10 个固定问题、22 个 GoF 模式页面、7 个 Profile 家族。
- **TypeScript** — [typescript/](typescript/)：完整包，包含 10 个固定问题、22 个 GoF 模式页面、7 个 Profile 家族。
- **中文** — [zh/](zh/)：翻译版 Python 包。`zh/shared/` 镜像英文共享层。

新增语言包：

1. 创建顶层目录，例如 `rust/`。
2. 添加 `questions/fixed-rust.md`（10 个语言专属问题）。
3. 添加 `patterns/gof/`（Rust 惯用法的模式页面）。
4. 添加 `profiles/rust-profile-taxonomy.md`。
5. 添加 `templates/CodeStyle.template.md`（含 Rust 专属章节）。
6. 从 `shared/` 引用适应性指南、编辑规则、会话记录和 SKILL/SPEC 模板——不要复制它们。
7. 更新本 README 和 `MANIFEST.md`。

## 输出

主要输出是项目专属的 `CodeStyle.md`。需要时，同一结果可提炼为：

- `SKILL.md`：可复用的 Agent 行为定义，
- `SPEC.md`：项目需求文档，
- 更细分的专项规范，如 `API_SPEC.md`、`TESTING_SPEC.md` 或 `ARCHITECTURE_SPEC.md`。

对于多语言项目，单份 `CodeStyle.md` 可以包含语言专属章节。例如，Python 章节定义类型纪律和异常策略；TypeScript 章节定义 `interface` vs `type` 用法和异步模式。跨语言共同事项（Git 工作流、依赖策略、测试策略）适用于所有语言，除非被覆盖。

访谈中的实时证据保存在会话期间的 `Recording.md` 中，包含完整题目卡、答案日志、反馈、隐藏推理笔记和最终证据审核。项目可保留原文件、按日期重命名存入语言包 `records/` 目录，或在输出生成后将文件归档。

## 贡献

欢迎贡献，尤其是新的语言包、更优质的问题集、更完善的 Profile 分类体系、更清晰的示例和文档改进。

好的贡献应保留核心工作流：

- 每次只问一个问题，
- 提问前将完整题目卡记录下来，
- 每次回答后更新 `Recording.md`，
- 问 10 个固定问题加上恰好 5 个适应性追问，
- 根据完整的会话记录推断最终 Profile，
- 仅引用对生成指导有实质影响的参考。

小型改动请提交聚焦的补丁，说明要修复的行为或文档问题。如果问题、Profile 或模式页面有改动，需说明新措辞如何改善未来生成的指导。