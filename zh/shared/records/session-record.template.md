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

来源：必选开场提示，"您想构建什么类型的项目？请简要描述。"

## 访谈轮次

记录计划和已完成的轮次。

| Round | Scope | Source | Status |
| --- | --- | --- | --- |
| Opening | Project | Required opening prompt | TODO |
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

### Opening. Project Summary

Question kind:
Opening

Scope:
Project

Source:
Required opening prompt

Full question:
What kind of project do you want to build? Please describe shortly.

Required scored snapshot blocks:

- P1-P6. Project fixed questions
- Language fixed questions for each selected language pack
- A1-A5. Adaptive questions

## 答案日志

每次回答后、提出下一个问题前更新此表。备注保持简洁；不要粘贴私密或无关个人信息。完整题目文本属于 `Question Card Snapshots`。

| Step | Question kind | Scope | Question focus | User answer | User note | Feedback given | Hidden inference note | Changed from | Recorded at |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Opening | Project summary | Project | Project intent | TODO | TODO | TODO | Not scored | None | TODO |
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
- `SPEC.md`: TODO. 使用 `shared/templates/SPEC.template.md`。

## 验证

Target project validation command:
TODO

CodeBTI repository validation command, if this record is generated while maintaining CodeBTI itself:
`python3 scripts/validate_repo.py`

Validation result:
TODO

## 未解决假设

- TODO
