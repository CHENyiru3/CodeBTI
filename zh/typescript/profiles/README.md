# CodeBTI Profiles

Profile 将用户的 CodeBTI 答案总结为实用的工程指导。Profile 是编码偏好的简写，而非技能或人格的评判。

在项目级轮次、TypeScript 固定问题和 5 个适应性问题完成后使用 Profile。

## 推断输入

综合使用以下输入：

- 来自 [questions/fixed-typescript.md](../questions/fixed-typescript.md) 的固定问题答案，
- 来自 [../../../project/questions/fixed-project.md](../../../project/questions/fixed-project.md) 的项目级答案，
- 来自 [../../shared/questions/adaptive-question-guide.md](../../shared/questions/adaptive-question-guide.md) 的自适应答案，
- 项目背景，
- 来自 [patterns/](../patterns/README.md) 的模式信号，
- 记录在 [../../shared/records/session-record.template.md](../../shared/records/session-record.template.md) 中的矛盾或弱信号。

## 推断规则

- 优先使用最强的重复风格信号。
- 不要仅凭一个答案就分配 Profile。
- 记录矛盾而非强制给出清晰的标签。
- 使用模式名称作为支持证据，而非主要结果。
- 从 Profile 生成具体的 `CodeStyle.md` 规则。

## TypeScript 分类体系

使用 [typescript-profile-taxonomy.md](typescript-profile-taxonomy.md) 了解 TypeScript Profile 家族。
