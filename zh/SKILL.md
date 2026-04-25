---
name: codebti
description: 运行 CodeBTI 访谈以推断编码风格偏好，并为 Python 项目生成项目专属的 CodeStyle.md、SKILL.md 或 SPEC.md。
---

# CodeBTI Skill

当用户想要为项目建立一致的编码风格、设计模式姿态、测试策略或协作流程时，使用此技能。触发条件包括："运行 CodeBTI 访谈"、"定义我们的编码风格"、"创建 CodeStyle.md"、"生成 SKILL.md"、"创建 SPEC.md"、"我们的项目风格是什么"，或任何明确要求使用 CodeBTI 的请求。

## 工作流程

1. 询问必选开场语："您想构建什么类型的项目？请简要描述。"
2. 使用 `python/records/session-record.template.md` 作为结构，在目标项目根目录创建或更新一份实时的 `Recording.md`。
3. 将开场回答记录为项目摘要。此开场提示不计入评分的固定问题。
4. 对 `python/questions/fixed-python.md` 中的 10 个固定 Python 问题，每个问题都先将完整用户面对的题目卡保存到 `Recording.md`，再提问，然后记录答案。
5. 用户每次回答后，更新 `Recording.md`，给出简短的项目反馈，再问下一个问题。
6. 使用 `python/questions/adaptive-question-guide.md` 提出恰好 5 个适应性后续追问；每个自适应问题在提问前也要将生成的完整题目卡保存。
7. 每个自适应回答后，更新 `Recording.md`，包含答案、反馈和隐藏推理笔记。
8. 回答完全部 15 个计分问题后，重新阅读 `Recording.md`，以此作为 Profile 推断的事实来源。
9. 从 `python/profiles/python-profile-taxonomy.md` 和 `python/patterns/gof/` 中的模式数据库推断 Python Profile。
10. 选择支撑最终建议的本地模式/资源引用。优先选择 `python/patterns/gof/` 下的具体文件，仅包含对指导有影响的引用。
11. 根据 `python/templates/CodeStyle.template.md` 生成 `CodeStyle.md`，包含引用说明——每个被引用模式都附上一句说明其相关性的注释。
12. 可选：保留或将 `Recording.md` 重命名为最终会话记录，可选地将结果提炼为 `SKILL.md` 或 `SPEC.md`（使用 `python/templates/` 中的模板）。

## 参考材料

| 文件 | 用途 |
|------|------|
| `python/questions/fixed-python.md` | 10 个固定访谈问题，含代码示例 |
| `python/questions/adaptive-question-guide.md` | 5 个后续追问的规则 |
| `python/questions/editorial-guide.md` | 问题的编辑规则 |
| `python/records/session-record.template.md` | 会话记录模板 |
| `python/profiles/python-profile-taxonomy.md` | Python Profile 推断规则 |
| `python/patterns/` | 22 个 Python 设计模式页面（GoF + 扩展） |
| `python/templates/CodeStyle.template.md` | CodeStyle.md 输出模板 |
| `python/templates/SKILL.template.md` | SKILL.md 输出模板 |
| `python/templates/SPEC.template.md` | SPEC.md 输出模板 |

## Agent 规则

- 每轮只问一个用户面对的访谈问题，包括开场语、固定问题和适应性追问。
- 展示用户面对的场景、说明、代码示例和选项；评分/信号笔记对用户隐藏，除非用户主动询问 CodeBTI 工作原理。
- 将每个题目卡保存到 `Recording.md`，而不仅仅是答案。可恢复的记录应包含：标题、维度、场景、说明、代码示例、选项、来源路径、用户答案、反馈和隐藏推理笔记。
- 收到每个回答后，在问下一个问题前，用一两句话给出项目反馈。好的反馈应指明含义，例如"这表明项目倾向于轻量对象，不需要严格的类型仪式。"不透露隐藏的评分表。
- 全程维护 `Recording.md`，使回答历史在上下文丢失后仍可恢复。每次回答后、下一个问题前更新。
- 生成 `CodeStyle.md`、`SKILL.md` 或 `SPEC.md` 前，重新阅读 `Recording.md`。
- 在最终报告中，用相关本地模式页面的引用来支撑，例如 `python/patterns/gof/facade.md`，当框架或库选择影响了指导时，加上有用的资源链接。
- 在最终报告中，每个被引用的模式都应说明：对该项目是鼓励使用、谨慎使用还是避免使用。
- 允许用户在任何时候修改之前的答案。
- 在生成的输出中，不要混用不同的类型风格、错误策略或命名约定。
- 保存会话记录作为生成建议的证据。
- 除非用户明确要求工具化，否则优先使用 markdown 输出而非脚本或工具。
