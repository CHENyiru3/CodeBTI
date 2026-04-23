# CodeBTI 问答框架

本文件夹定义了 CodeBTI 访谈系统。访谈帮助 Agent 将用户的项目目标和编码偏好转化为项目专属的 `CodeStyle.md`、`SKILL.md` 或 `SPEC.md`。

第一版以 Python 为优先。未来语言应添加平行的固定问题集，而非修改共享访谈流程。

## 访谈流程

1. 询问必选开场语："您想构建什么类型的项目？请简要描述。"
2. 使用 [../records/session-record.template.md](../records/session-record.template.md) 创建或更新实时的 `Recording.md`。
3. 每个问题之前，将完整题目卡保存到 `Recording.md`。
4. 从 [fixed-python.md](fixed-python.md) 询问 10 个固定 Python 问题。
5. 每个回答后，记录答案并给出简短的项目反馈。
6. 使用 [adaptive-question-guide.md](adaptive-question-guide.md) 询问恰好 5 个适应性后续追问。
7. 重新阅读 `Recording.md`，推断风格维度和模式倾向，然后生成项目专属的 `CodeStyle.md`。

开场项目描述提示是访谈前的上下文。将其记录为会话的 `项目摘要`；不计入 10 个固定问题。

每轮只问一个用户面对的访谈问题。这适用于开场提示、每个固定问题和每个适应性后续追问。

每个被问到的问题必须能从记录中恢复。不要仅依赖聊天历史或源文件；将完整题目卡复制到 `Recording.md`。

## 问题风格

问题应使用具体示例而非模式术语。用户应能通过查看小型场景或代码段，选择他们更愿意维护的风格来回答。

好的问题：

- 展示现实的 Python 权衡，
- 每次覆盖一个主要维度，
- 当代码使选择更清晰时使用短代码片段，
- 避免陷阱选项，
- 对用户隐藏设计模式评分。

使用 [question-format.md](question-format.md) 获取要求的卡片结构。
在将草稿问题改写为最终形式时使用 [editorial-guide.md](editorial-guide.md)。
使用 [../records/README.md](../records/README.md) 获取记录指导。

## 评分原则

答案首先映射到 CodeBTI 风格维度，其次映射到设计模式信号。例如，一个选项可能主要信号"接口优先抽象"，仅次要地暗示 Strategy、Bridge 或 Abstract Factory。

访谈结果应指导编码一致性。不应评判用户的能力或人格。

## 组织整理

当用户提供草稿问题时，用中等改写整理：

1. 保留用户的维度和核心想法。
2. 重写场景和选项以达到平衡。
3. 简化措辞同时不使主题不严肃。
4. 添加或修剪代码示例，使每个选项感觉同样现实。
5. 添加隐藏评分和 `CodeStyle.md` 影响。
