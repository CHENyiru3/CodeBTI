# 共享架构

本目录包含 CodeBTI 访谈系统的语言中立部分。它们在所有语言包之间共享，使访谈流程、编辑指南和输出结构保持一致，同时问题内容和模式示例保持语言相关。

## 共享内容

| 文件 | 用途 |
|------|------|
| `adaptive-question-guide.md` | 选择和提出 5 个后续问题的规则。语言中立。 |
| `editorial-guide.md` | 问题编写规则。语言中立。 |
| `question-format.md` | 每个问题的标准卡片结构。语言中立。 |
| `shared-architecture.md` | 本文件——解释多语言设计。 |

共享模板和记录位于 `../templates/` 和 `../records/`。

## 多语言访谈模型

### 语言相关文件

每个语言包拥有：

- **`questions/fixed-<lang>.md`** — 10 个固定面试问题，包含该语言的代码示例。这是核心的语言相关产出。
- **`patterns/gof/`** — 针对该语言生态圈调整的设计模式页面。
- **`profiles/<lang>-profile-taxonomy.md`** — 该语言的 profile 族。
- **`templates/CodeStyle.template.md`** — 输出模板，包含语言相关部分（例如，TypeScript 的 `interface` vs `type`，Python 的 `dataclass` vs `pydantic`）。

### 共享文件

所有语言包共享：

- `shared/questions/` — 访谈流程规则、问题结构、编辑指南。
- `shared/templates/` — SKILL 和 SPEC 输出模板（语言中立）。
- `shared/records/` — 会议记录模板。

### 访谈流程

1. 开场提示（语言中立）。
2. 来自语言包 `questions/fixed-<lang>.md` 的 10 个固定问题。
3. 5 个自适应后续问题——规则来自 `shared/questions/adaptive-question-guide.md`，内容由固定答案决定。
4. 使用 `profiles/<lang>-profile-taxonomy.md` 和 `patterns/gof/` 推断 Profile。
5. 使用 `templates/CodeStyle.template.md` 和 `shared/templates/SKILL.template.md` / `shared/templates/SPEC.template.md` 生成输出。

### 为什么这种分离很重要

- 问题内容（场景、代码示例、语言惯用语）是语言相关的，必须按语言包维护。
- 访谈机制（每轮一个问题，完整卡片记入记录，每回答后反馈）在各语言间保持一致，使 Agent 行为相同。
- 输出模板可以共享，因为 `SKILL.md` 和 `SPEC.md` 是语言中立的文档——语言相关指导写入 `CodeStyle.md`。

### 添加新语言包

1. 创建 `<lang>/questions/fixed-<lang>.md`，包含 10 个语言相关问题。
2. 创建 `<lang>/patterns/gof/`，包含该语言的模式页面。
3. 创建 `<lang>/profiles/<lang>-profile-taxonomy.md`。
4. 创建 `<lang>/templates/CodeStyle.template.md`，包含语言相关输出部分。
5. 从 `shared/templates/` 复制或引用 `SKILL.template.md` 和 `SPEC.template.md`。
6. `shared/questions/` 和 `shared/records/` 中的共享文件开箱即用。

## Agent 共享文件规则

- 永远不要以语言相关方式修改 `shared/questions/`、`shared/templates/` 或 `shared/records/`。
- 如果语言包需要偏离共享规则，请在 issue 中提出，而不是 fork 共享内容。
- 从语言包内部引用共享文件时，使用相对路径（例如 `../../shared/questions/question-format.md`）。