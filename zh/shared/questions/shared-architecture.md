# 共享架构

本文件夹包含 CodeBTI 访谈系统的语言中立部分。它们由所有包共享，使访谈机制、编辑指南和输出结构保持一致，同时由项目包和语言包拥有各自内容。

## 哪些内容共享

| 文件 | 用途 |
|------|------|
| `adaptive-question-guide.md` | 选择和提出 5 个后续追问的规则。语言中立。 |
| `editorial-guide.md` | 问题写作规则。语言中立。 |
| `question-format.md` | 每个问题的标准题目卡结构。语言中立。 |
| `shared-architecture.md` | 本文件，解释项目/语言包设计。 |

共享模板和记录位于 `../templates/` 和 `../records/`。

## 包模型

### 项目包

`project/` 包拥有跨项目访谈内容：

- `project/questions/fixed-project.md` — 项目级问题。
- `project/profiles/project-profile-taxonomy.md` — 工作流和治理 Profile 家族。
- `project/templates/ProjectStyle.template.md` — 项目级输出模板。

项目级答案控制协作、验证门禁、输出形态、依赖治理、变更记录，以及共享规则与语言规则的边界。

### 语言包

每个语言包拥有：

- `questions/fixed-<lang>.md` — 使用该语言示例的固定访谈问题。
- `patterns/gof/` — 适配该语言生态的设计模式页面。
- `profiles/<lang>-profile-taxonomy.md` — 该语言的 Profile 家族。
- `templates/CodeStyle.template.md` — 带语言特定章节的输出模板。

### 共享文件

所有包共享：

- `shared/questions/` — 访谈流程规则、题目结构、编辑指南。
- `shared/templates/` — SKILL 和 SPEC 输出模板。
- `shared/records/` — 会话记录模板。

## 访谈如何进行

1. 开场提示。
2. 来自 `project/questions/fixed-project.md` 的固定项目问题。
3. 来自每个所选语言包的固定语言问题。
4. 使用 `shared/questions/adaptive-question-guide.md` 提出恰好 5 个适应性后续追问。
5. 使用 `project/profiles/project-profile-taxonomy.md` 推断项目 Profile。
6. 使用每个语言的 Profile taxonomy 和 `patterns/gof/` 页面推断语言 Profile。
7. 使用相关语言 `CodeStyle.template.md`、可选的 `project/templates/ProjectStyle.template.md`，以及可选的共享 SKILL/SPEC 模板生成输出。

## 为什么这样分离

- 项目流程决策只问一次，并跨语言复用。
- 问题内容、代码示例和语言习惯用法保持语言特定。
- 访谈机制保持一致，使 Agent 在不同包中行为一致。
- 共享模板避免重复 SKILL/SPEC 结构，同时语言包保留各自 CodeStyle 细节。

## 添加新语言包

1. 创建 `<lang>/questions/fixed-<lang>.md`，包含固定语言问题。
2. 创建 `<lang>/patterns/gof/`，包含该语言的模式页面。
3. 创建 `<lang>/profiles/<lang>-profile-taxonomy.md`。
4. 创建 `<lang>/templates/CodeStyle.template.md`，包含语言特定输出章节。
5. 引用 `shared/` 中的适应性指南、编辑规则、会话记录和 SKILL/SPEC 模板。不要把共享文件复制进语言包。
6. 更新 `README.md`、`AGENT.md` 和 `MANIFEST.md`。
7. 运行 `python3 scripts/validate_repo.py`。

## 共享文件的 Agent 规则

- 永远不要以项目或语言特定方式修改 `shared/questions/`、`shared/templates/` 或 `shared/records/`。
- 如果某个包需要偏离共享规则，在该包中记录冲突，而不是 fork 共享内容。
- 从包内部引用共享文件时，使用类似 `../../shared/questions/question-format.md` 的相对路径。
