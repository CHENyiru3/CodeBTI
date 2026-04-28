# CodeBTI

![CodeBTI 概览](https://i.imgur.com/annGWpK.jpeg)

CodeBTI 是 MBTI 的代码风格版本，为软件项目服务。它帮助人类开发者和 AI Agent 在实现之前，选择一套一致的项目工作流、编码风格、设计模式姿态、测试策略、依赖策略和协作流程。

CodeBTI 不是人格测试。它是一套实用的访谈与文档系统，用来生成项目专属的指导文件，如 `CodeStyle.md`、`ProjectStyle.md`、`SKILL.md` 或 `SPEC.md`。

## 安装为 Skill

本仓库可直接安装为 Codex skill。将本仓库复制或安装到 Codex skills 目录中，命名为 `codebti`。根目录的 `SKILL.md` 即为入口文件。

## 工作原理

CodeBTI 现在使用更可控的项目优先流程：

1. 用户描述项目及可能的语言目标。
2. Agent 在目标项目中创建一份实时的 `Recording.md`，并记录项目摘要。
3. Agent 先询问 [project/questions/fixed-project.md](../project/questions/fixed-project.md) 中的 6 个固定项目问题。
4. Agent 再对每个选定语言包询问固定语言问题，例如 [python/questions/fixed-python.md](../python/questions/fixed-python.md) 或 [typescript/questions/fixed-typescript.md](../typescript/questions/fixed-typescript.md)。
5. 每个计分问题之前，Agent 将完整题目卡保存到 `Recording.md`；用户回答后，更新答案日志并给出简短项目反馈。
6. Agent 使用 [shared/questions/adaptive-question-guide.md](../shared/questions/adaptive-question-guide.md) 在整个会话中总共提出恰好 5 个适应性后续追问。
7. Agent 将 `Recording.md` 作为事实来源重新阅读。
8. Agent 根据 [project/profiles/project-profile-taxonomy.md](../project/profiles/project-profile-taxonomy.md) 推断项目 Profile，并根据所选语言 taxonomy 推断语言 Profile。
9. Agent 只选择对最终指导有实质影响的模式/资源引用。
10. Agent 使用所选语言模板、可选 [project/templates/ProjectStyle.template.md](../project/templates/ProjectStyle.template.md) 和可选共享 SKILL/SPEC 模板生成项目指导。

可执行的逐步流程见英文 [golden path workflow](../docs/golden-path.md)。

## 多语言项目

对于多语言项目，CodeBTI 只询问一次项目级问题，然后对每个语言运行一个语言专属轮次。最终单份 `CodeStyle.md` 应先写共享项目规则，再写语言专属章节。

对于多语言项目，Agent 应：

- 在 `Recording.md` 中标注每组答案属于哪种语言。
- 以项目级答案作为 Git 工作流、验证门禁、依赖治理、输出形态和变更记录的默认规则。
- 只有在明确记录原因时，才允许语言专属章节覆盖项目级默认规则。
- 所有轮次都引用同一套 `shared/` 访谈资源。

## 验证

本仓库有轻量验证门禁：

```sh
python3 scripts/validate_repo.py
python3 -m pytest
```

这些检查会验证本地 Markdown 链接、必需包文件、固定问题数量和章节、中文共享镜像覆盖、`MANIFEST.md` 是否漂移、问题 ID/范围质量、模板章节，以及多语言 fixture。

当前发布加固基线见英文 [CHANGELOG.md](../CHANGELOG.md)。

## 示例

英文 [examples/](../examples/) 目录中包含一个完整的 CodeBTI 访谈记录，针对一个小型 Python GUI 计算器。

- [examples/Recording.md](../examples/Recording.md)：完整访谈记录，包含项目摘要、10 个固定答案、5 个自适应答案、反馈、隐藏推理笔记和最终 Profile 推断。
- [examples/CodeStyle.md](../examples/CodeStyle.md)：生成的英文项目风格指南。

中文翻译版 CodeStyle 示例位于 [zh/examples/CodeStyle.md](examples/CodeStyle.md)。

推断出的 Profile 为 **算法优先极简主义者（Algorithm-First Minimalist），具有对象中心边界特征**。最终指导建议：

该示例早于项目级问题轮次，但仍可作为单语言记录和输出示例参考。

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
├── project/                   # 项目级访谈包
│   ├── questions/             # fixed-project.md + README
│   ├── profiles/              # 项目 Profile taxonomy
│   └── templates/             # ProjectStyle.template.md
│
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
├── scripts/                   # 验证脚本
├── .github/workflows/         # CI 验证
├── docs/                      # 操作工作流指南
├── examples/                  # 完成的访谈示例
├── zh/                        # 简体中文翻译（镜像结构）
├── AGENT.md                   # Agent 指南
├── CHANGELOG.md               # 发布说明
├── MANIFEST.md                # 文件清单
├── README.md                 # 本文件
└── SKILL.md                   # 可安装技能入口
```

**项目级 vs 共享 vs 语言专属：**

| 资源 | 范围 | 示例 |
|------|------|------|
| 项目固定问题 | 项目级 | `project/questions/fixed-project.md` |
| 项目 Profile 分类体系 | 项目级 | `project/profiles/project-profile-taxonomy.md` |
| 语言固定问题 | 按语言 | `python/questions/fixed-python.md`、`typescript/questions/fixed-typescript.md` |
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

- **Project** — [project/](../project/)：项目级流程与治理包。
- **Python** — [python/](../python/)：完整包，包含 10 个固定问题、22 个 GoF 模式页面、7 个 Profile 家族。
- **TypeScript** — [typescript/](../typescript/)：完整包，包含 10 个固定问题、22 个 GoF 模式页面、7 个 Profile 家族。
- **中文** — [当前目录](.)：中文翻译包。`zh/shared/` 是英文共享层的翻译镜像。

新增语言包：

1. 创建顶层目录，例如 `rust/`。
2. 添加 `questions/fixed-rust.md`（10 个语言专属问题）。
3. 添加 `patterns/gof/`（Rust 惯用法的模式页面）。
4. 添加 `profiles/rust-profile-taxonomy.md`。
5. 添加 `templates/CodeStyle.template.md`（含 Rust 专属章节）。
6. 从 `shared/` 引用适应性指南、编辑规则、会话记录和 SKILL/SPEC 模板。不要把共享文件复制进语言包。
7. 更新根目录 `README.md`、`AGENT.md` 和 `MANIFEST.md`。
8. 运行 `python3 scripts/validate_repo.py` 和 `python3 -m pytest`。

## 输出

主要输出是项目专属的 `CodeStyle.md`。需要时，同一结果可提炼为：

- `SKILL.md`：可复用的 Agent 行为定义，
- `ProjectStyle.md`：项目级工作流和治理规则，
- `SPEC.md`：项目需求文档，
- 更细分的专项规范，如 `API_SPEC.md`、`TESTING_SPEC.md` 或 `ARCHITECTURE_SPEC.md`。

对于多语言项目，单份 `CodeStyle.md` 可以包含语言专属章节。跨语言共同事项适用于所有语言，除非某个语言章节明确覆盖。

访谈中的实时证据保存在目标项目根目录的 `Recording.md` 中，包含完整题目卡、答案日志、反馈、隐藏推理笔记和最终证据审核。项目可保留原文件，或在输出生成后将其按日期重命名归档。

## 贡献

欢迎贡献，尤其是新的语言包、更优质的问题集、更完善的 Profile 分类体系、更清晰的示例和文档改进。

好的贡献应保留核心工作流：

- 每次只问一个问题，
- 提问前将完整题目卡记录下来，
- 每次回答后更新 `Recording.md`，
- 问 6 个项目问题、语言固定问题，以及恰好 5 个适应性追问，
- 根据完整的会话记录推断最终 Profile，
- 仅引用对生成指导有实质影响的参考。
- 提交前运行 `python3 scripts/validate_repo.py` 和 `python3 -m pytest`。

小型改动请提交聚焦的补丁，说明要修复的行为或文档问题。如果问题、Profile 或模式页面有改动，需说明新措辞如何改善未来生成的指导。
