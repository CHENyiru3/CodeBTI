# CodeBTI 问答框架

本文件夹定义了 Python 专属 CodeBTI 访谈轮次。该语言轮次在项目级轮次完成后，帮助 Agent 将 Python 编码偏好转化为项目专属指导。

## 访谈流程

1. 先完成 [../../../project/questions/fixed-project.md](../../../project/questions/fixed-project.md) 中的项目级轮次。
2. 每个 Python 问题之前，将完整题目卡保存到 `Recording.md`。
3. 从 [fixed-python.md](fixed-python.md) 询问 10 个固定 Python 问题。
4. 每个回答后，将答案记录在 `Language:Python` 下，并给出简短项目反馈。
5. 使用 [../../shared/questions/adaptive-question-guide.md](../../shared/questions/adaptive-question-guide.md) 在整个会话中总共提出恰好 5 个适应性后续追问。
6. 重新阅读 `Recording.md` 和 `SPEC.md`，推断 Python 风格维度和模式倾向，然后在 `CodeStyle.md` 中生成 Python 专属指导。

开场 SPEC 风格提示和项目级问题不属于此语言轮次。Python 答案应与项目级答案及其他语言答案分开记录。

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

使用 [question-format.md](../../shared/questions/question-format.md) 获取要求的卡片结构。
在将草稿问题改写为最终形式时使用 [editorial-guide.md](../../shared/questions/editorial-guide.md)。
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
