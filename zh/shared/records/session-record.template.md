# CodeBTI 会话记录

Date:
TODO

Project slug:
TODO

Language targets:
TODO

Interview status:
TODO

Current step:
TODO

Next question:
TODO

## 项目摘要

TODO

来源：必选 SPEC 风格开场提示。

## 开场 SPEC Intake

使命：
TODO

目标：
TODO

目标受众：
TODO

约束：
TODO

可能的技术栈或语言目标：
TODO

路线图意图：
TODO

非目标：
TODO

开放问题：
TODO

缺失的开场字段：
TODO：列出用户未回答的 SPEC 字段。后续用适应性问题解决高风险缺口。

初始 SPEC 草稿：
TODO：`SPEC.md` 路径，或说明为什么没有生成草稿。

## 访谈轮次

记录计划和已完成的轮次。

| Round | Scope | Source | Status |
| --- | --- | --- | --- |
| Opening | Project | Required SPEC-style opening prompt | TODO |
| Project fixed questions | Project | `project/questions/fixed-project.md` | TODO |
| Language fixed questions | Language:TODO | `TODO/questions/fixed-TODO.md` | TODO |
| Adaptive questions | Project, Language, or Cross-language | Generated from `shared/questions/adaptive-question-guide.md` | TODO |

## 题目卡快照

提问前保存完整的用户面对题目。固定问题应包含来源路径；适应性问题应直接存储生成的问题文本。开场提示、所有固定项目问题、所有固定语言问题和 5 个适应性问题都必须有快照块。

每个计分问题使用此块形状：

```text
### QN. Question Title

Question kind:
Project fixed, Language fixed, or Adaptive

Question ID:
Stable identifier if available

Scope:
Project, Language:<name>, or Cross-language

Source:
Local source path for fixed questions, or "Generated adaptive question"

Dimension:
Primary dimension being tested

User-facing scenario:
Full scenario shown to the user

User-facing instruction:
Full instruction shown to the user

Code example:
Full code example shown to the user, or "None"

Choices:
- A. Full choice text
- B. Full choice text
- C. Full choice text if present
- D. Full choice text if present
- E. Full choice text if present
```

### Opening. Project Summary and SPEC Intake

Question kind:
Opening

Scope:
Project

Source:
Required SPEC-style opening prompt

Full question:
请用一份紧凑的 SPEC 风格 brief 描述这个项目。请包含使命、目标、目标受众、约束、可能的技术栈或语言目标、路线图意图、非目标和开放问题。保持在 what/why 层级；除非它们是硬约束，否则避免低层实现细节。

Required scored snapshot blocks:

- P1-P6. Project fixed questions
- Language fixed questions for each selected language pack
- A1-A5. Adaptive questions

## 答案日志

每次回答后、提出下一个问题前更新此表。备注保持简洁；不要粘贴私密或无关个人信息。完整题目文本属于 `Question Card Snapshots`。

| Step | Question kind | Scope | Question focus | User answer | User note | Feedback given | Hidden inference note | Changed from | Recorded at |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Opening | Project summary and SPEC intake | Project | Mission, goals, audience, constraints, stack, roadmap, non-goals, open questions | TODO | TODO | TODO | Not scored | None | TODO |
| P1 | Project fixed | Project | Project control model | TODO | TODO | TODO | TODO | None | TODO |
| P2 | Project fixed | Project | Output shape | TODO | TODO | TODO | TODO | None | TODO |
| P3 | Project fixed | Project | Validation gate | TODO | TODO | TODO | TODO | None | TODO |
| P4 | Project fixed | Project | Shared versus language-specific rules | TODO | TODO | TODO | TODO | None | TODO |
| P5 | Project fixed | Project | Dependency governance | TODO | TODO | TODO | TODO | None | TODO |
| P6 | Project fixed | Project | Change record policy | TODO | TODO | TODO | TODO | None | TODO |
| Language:TODO Q1 | Language fixed | Language:TODO | TODO | TODO | TODO | TODO | TODO | None | TODO |
| Language:TODO Q2 | Language fixed | Language:TODO | TODO | TODO | TODO | TODO | TODO | None | TODO |
| Language:TODO Q3 | Language fixed | Language:TODO | TODO | TODO | TODO | TODO | TODO | None | TODO |
| Language:TODO Q4 | Language fixed | Language:TODO | TODO | TODO | TODO | TODO | TODO | None | TODO |
| Language:TODO Q5 | Language fixed | Language:TODO | TODO | TODO | TODO | TODO | TODO | None | TODO |
| Language:TODO Q6 | Language fixed | Language:TODO | TODO | TODO | TODO | TODO | TODO | None | TODO |
| Language:TODO Q7 | Language fixed | Language:TODO | TODO | TODO | TODO | TODO | TODO | None | TODO |
| Language:TODO Q8 | Language fixed | Language:TODO | TODO | TODO | TODO | TODO | TODO | None | TODO |
| Language:TODO Q9 | Language fixed | Language:TODO | TODO | TODO | TODO | TODO | TODO | None | TODO |
| Language:TODO Q10 | Language fixed | Language:TODO | TODO | TODO | TODO | TODO | TODO | None | TODO |
| A1 | Adaptive | TODO | TODO | TODO | TODO | TODO | TODO | None | TODO |
| A2 | Adaptive | TODO | TODO | TODO | TODO | TODO | TODO | None | TODO |
| A3 | Adaptive | TODO | TODO | TODO | TODO | TODO | TODO | None | TODO |
| A4 | Adaptive | TODO | TODO | TODO | TODO | TODO | TODO | None | TODO |
| A5 | Adaptive | TODO | TODO | TODO | TODO | TODO | TODO | None | TODO |

## 项目问题答案

记录全部 6 个项目级答案。如果用户修改答案，保留最终答案并记录变更。

| Question | Final answer | User note | Changed from |
| --- | --- | --- | --- |
| P1 | TODO | TODO | TODO |
| P2 | TODO | TODO | TODO |
| P3 | TODO | TODO | TODO |
| P4 | TODO | TODO | TODO |
| P5 | TODO | TODO | TODO |
| P6 | TODO | TODO | TODO |

## 语言问题答案

每个所选语言创建一个小节。

对于多语言会话，为每个选定语言复制下面的小节，例如 `Language: Python` 和 `Language: TypeScript`。保持各语言答案分开。不要用一个语言的答案表覆盖另一个语言的答案表。

### Language: TODO

Source question file:
TODO

Profile taxonomy:
TODO

| Question | Final answer | User note | Changed from |
| --- | --- | --- | --- |
| Q1 | TODO | TODO | TODO |
| Q2 | TODO | TODO | TODO |
| Q3 | TODO | TODO | TODO |
| Q4 | TODO | TODO | TODO |
| Q5 | TODO | TODO | TODO |
| Q6 | TODO | TODO | TODO |
| Q7 | TODO | TODO | TODO |
| Q8 | TODO | TODO | TODO |
| Q9 | TODO | TODO | TODO |
| Q10 | TODO | TODO | TODO |

## 语言覆盖决策

记录任何覆盖共享项目规则的语言专属决策。语言遵循共享默认规则时写 `None`。

| Language | Shared project rule | Override | Reason | Validation required |
| --- | --- | --- | --- | --- |
| TODO | TODO | TODO | TODO | TODO |

## 适应性问题答案

记录恰好 5 个适应性答案。

| Question | Scope | Direction | Final answer | User note | Why asked |
| --- | --- | --- | --- | --- | --- |
| A1 | TODO | TODO | TODO | TODO | TODO |
| A2 | TODO | TODO | TODO | TODO | TODO |
| A3 | TODO | TODO | TODO | TODO | TODO |
| A4 | TODO | TODO | TODO | TODO | TODO |
| A5 | TODO | TODO | TODO | TODO | TODO |

## 反馈摘要

记录访谈中给出的用户可见反馈主题。这有助于未来 Agent 保持有用的访谈风格，而不暴露隐藏评分。

- TODO

## 隐藏评分笔记

项目级信号：

- TODO

语言级风格轴信号：

- TODO

模式信号：

- Encouraged: TODO
- Allowed with caution: TODO
- Avoid by default: TODO

模式和资源引用：

| Reference | Local path or URL | Why it matters |
| --- | --- | --- |
| TODO | TODO | TODO |

矛盾或弱信号：

- TODO

生成前审阅的证据：

- `Question Card Snapshots`
- `Answer Log`
- 项目和语言答案表
- 适应性答案表
- 模式和资源引用

## CodeBTI 结果

Project profile name:
TODO

Project profile taxonomy reference:
`project/profiles/project-profile-taxonomy.md`

Language profiles:

| Language | Profile name | Profile taxonomy reference |
| --- | --- | --- |
| TODO | TODO | TODO |

Short explanation:
TODO

## 生成输出

- `CodeStyle.md`: TODO. 使用相关语言的 `templates/CodeStyle.template.md` 和共享项目规则。
- `ProjectStyle.md`: TODO. 当单独生成项目级工作流指导时，使用 `project/templates/ProjectStyle.template.md`。
- `SKILL.md`: TODO. 使用 `shared/templates/SKILL.template.md`。
- `SPEC.md`: TODO. 开场 intake 后创建，并在 replanning 时更新。使用 `shared/templates/SPEC.template.md`。

## 验证

Target project validation command:
TODO

CodeBTI repository validation command, if this record is generated while maintaining CodeBTI itself:
`python3 scripts/validate_repo.py`

Validation result:
TODO

## 未解决假设

- TODO
