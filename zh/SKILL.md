---
name: codebti
description: 运行 CodeBTI 访谈，推断项目级和语言级编码风格偏好，并生成项目专属的 CodeStyle.md、SKILL.md 或 SPEC.md 指导。
---

# CodeBTI Skill

当用户想为项目建立一致的编码风格、设计模式姿态、测试策略、依赖策略或协作工作流时使用本技能。触发语包括："运行 CodeBTI 访谈"、"定义我们的编码风格"、"创建 CodeStyle.md"、"生成 SKILL.md"、"创建 SPEC.md"、"我们的项目风格是什么"，或任何明确要求使用 CodeBTI 的请求。

## 支持的包

| 包 | 用途 |
|----|------|
| `project/` | 项目级决策：协作、输出形态、验证门禁、共享与语言规则边界、依赖治理和变更记录。 |
| `python/` | Python 专属风格、类型、错误处理、目录结构、测试、注释、Git 和依赖。 |
| `typescript/` | TypeScript 专属风格、类型、interface/type、错误处理、目录结构、测试、注释、Git 和依赖。 |
| `shared/` | 语言中立的问题格式、适应性追问规则、模板和会话记录结构。 |

## 路由工作流

1. 询问必选开场语："您想构建什么类型的项目？请简要描述。"
2. 从用户回答中识别目标语言包。如果语言不明确，在开始计分问题前提出一个简短澄清问题。
3. 使用 `shared/records/session-record.template.md` 作为结构，在目标项目根目录创建或更新实时 `Recording.md`。
4. 将开场回答记录为项目摘要。该开场提示不计分。
5. 询问 `project/questions/fixed-project.md` 中的 6 个固定项目问题。每个问题提问前，将完整用户面对题目卡保存到 `Recording.md`，然后记录答案和反馈。
6. 对每个所选语言包询问该语言的固定问题：
   - Python: `python/questions/fixed-python.md`
   - TypeScript: `typescript/questions/fixed-typescript.md`
7. 在 `Recording.md` 中按语言目标记录每组语言答案。
8. 使用 `shared/questions/adaptive-question-guide.md` 在整个会话中总共提出恰好 5 个适应性追问。适应性问题可以针对项目级模糊点、某个语言或跨语言冲突。
9. 回答完所有计分问题后，重新阅读 `Recording.md`，并将其作为 Profile 推断的事实来源。
10. 使用 `project/profiles/project-profile-taxonomy.md` 推断项目级 Profile。
11. 使用各语言 taxonomy 和模式数据库推断语言 Profile：
    - Python: `python/profiles/python-profile-taxonomy.md`, `python/patterns/gof/`
    - TypeScript: `typescript/profiles/typescript-profile-taxonomy.md`, `typescript/patterns/gof/`
12. 只选择真实影响最终建议的本地模式/资源引用。
13. 生成请求的指导：
    - 单语言项目：使用该语言的 `templates/CodeStyle.template.md`；
    - 多语言项目：先写共享项目规则，再写语言专属章节；
    - 项目级工作流摘要：需要时使用 `project/templates/ProjectStyle.template.md`；
    - 可选 `SKILL.md` 或 `SPEC.md`：使用 `shared/templates/SKILL.template.md` 和 `shared/templates/SPEC.template.md`。

## 参考资料

| 文件 | 用途 |
|------|------|
| `project/questions/fixed-project.md` | 6 个项目级访谈问题 |
| `project/profiles/project-profile-taxonomy.md` | 项目级工作流和治理 Profile |
| `project/templates/ProjectStyle.template.md` | 项目级风格和工作流输出模板 |
| `python/questions/fixed-python.md` | 10 个固定 Python 访谈问题 |
| `typescript/questions/fixed-typescript.md` | 10 个固定 TypeScript 访谈问题 |
| `shared/questions/adaptive-question-guide.md` | 5 个适应性追问的规则 |
| `shared/questions/editorial-guide.md` | 问题编辑规则 |
| `shared/questions/question-format.md` | 标准题目卡格式 |
| `shared/records/session-record.template.md` | 多轮会话记录模板 |
| `shared/templates/SKILL.template.md` | SKILL.md 输出模板 |
| `shared/templates/SPEC.template.md` | SPEC.md 输出模板 |

## Agent 规则

- 每轮只问一个用户面对的访谈问题，包括开场提示、项目问题、语言问题和适应性追问。
- 展示用户面对的场景、说明、代码示例和选项；除非用户询问，否则隐藏评分/信号笔记。
- 将每个题目卡保存到 `Recording.md`，而不仅仅是答案。
- 每次收到回答后，先更新 `Recording.md`，再给出一两句项目相关反馈，然后问下一个问题。
- 将项目级答案与语言特定答案分开保存。
- 对多语言项目，Git 工作流、依赖治理、验证门禁、输出形态和变更记录默认由项目级答案控制，除非语言章节明确覆盖。
- 生成 `CodeStyle.md`、`ProjectStyle.md`、`SKILL.md` 或 `SPEC.md` 前，重新阅读 `Recording.md`。
- 最终报告必须引用相关本地模式页面和 Profile 参考。每个被引用模式都应说明它在本项目中是鼓励、谨慎允许还是默认避免。
- 允许用户随时修改早先答案，并记录答案变更。
- 不要在生成输出中混用不一致的类型风格、错误策略、命名约定或验证期望。
- 保留会话记录，作为生成建议的证据。
- 除非用户明确要求工具，否则优先生成 Markdown 输出。
