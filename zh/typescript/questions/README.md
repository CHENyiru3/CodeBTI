# CodeBTI 访谈框架

本文件夹定义 CodeBTI 访谈系统。访谈帮助 Agent 将用户的项目目标和编码偏好转换为一个项目专属的 `CodeStyle.md`、`SKILL.md` 或 `SPEC.md`。

## 访谈流程

1. 询问必选开场语："您想构建什么类型的项目？请简要描述。"
2. 使用 [../../shared/records/session-record.template.md](../../shared/records/session-record.template.md) 创建或更新一份实时的 `Recording.md`。
3. 每个问题之前，将完整的题目卡保存到 `Recording.md`。
4. 从 [fixed-typescript.md](fixed-typescript.md) 提出 10 个固定 TypeScript 问题。
5. 每次回答后，记录答案并给出简短的项目反馈。
6. 使用 [../../shared/questions/adaptive-question-guide.md](../../shared/questions/adaptive-question-guide.md) 提出恰好 5 个适应性后续追问。
7. 重新阅读 `Recording.md`，推断风格维度和模式倾向，然后生成项目专属的 `CodeStyle.md`。

开场项目描述提示是访谈前的上下文。将其记录为会话的 `项目摘要`；不计入 10 个固定问题。

每轮只问一个用户面对的访谈问题。这适用于开场语、每个固定问题和每个适应性追问。

每个被问的问题必须可从记录中恢复。不要仅依赖聊天历史或源文件；将完整题目卡复制到 `Recording.md`。

## 问题风格

问题应使用具体示例而非模式术语。用户应该能够通过查看一个小场景或代码片段并选择他们最希望保持的风格来回答。

好的问题：

- 呈现真实的 TypeScript 权衡，
- 每次覆盖一个主要维度，
- 当代码使选择更清晰时使用短代码片段，
- 避免陷阱选项，
- 对用户隐藏设计模式评分。

使用 [../../shared/questions/question-format.md](../../shared/questions/question-format.md) 了解所需的卡片结构。
使用 [../../shared/questions/editorial-guide.md](../../shared/questions/editorial-guide.md) 将草稿问题改写为最终形式。
使用 [../../records/README.md](../../records/README.md) 了解记录指导。

## 评分原则

答案首先映射到 CodeBTI 风格维度，其次映射到设计模式信号。例如，一个选项可能主要信号"接口优先抽象"，仅在次要位置暗示 Strategy、Bridge 或 Abstract Factory。

访谈结果应指导编码一致性。不应评判用户的能力或人格。

## 组织通过

当用户提供草稿问题时，用中等改写组织它们：

1. 保留用户的维度和核心想法。
2. 重写场景和选项以达到平衡。
3. 简化措辞但不使主题不严肃。
4. 添加或修剪代码示例，使每个选项感觉同样真实。
5. 添加隐藏评分和 `CodeStyle.md` 影响。