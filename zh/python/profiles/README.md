# CodeBTI Profiles

Profile 将用户的 CodeBTI 答案总结为实用工程指导。Profile 是编码偏好的简写，而非技能或人格的评判。

在 10 个固定问题和 5 个适应性问题完成后使用 Profile。

## 推断输入

综合使用以下输入：

- 来自 [questions/fixed-python.md](../questions/fixed-python.md) 的固定问题答案，
- 来自 [questions/adaptive-question-guide.md](../questions/adaptive-question-guide.md) 的适应性问题答案，
- 项目上下文，
- 来自 [patterns/](../patterns/README.md) 的模式信号，
- 记录在 [records/session-record.template.md](../records/session-record.template.md) 中的矛盾或弱信号。

## 推断规则

- 优先最强烈的重复风格信号。
- 不要仅凭一个答案就分配 Profile。
- 记录矛盾而非强行给出干净标签。
- 使用模式名称作为支撑证据，而非主要结果。
- 从 Profile 生成具体的 `CodeStyle.md` 规则。

## Python 分类体系

使用 [python-profile-taxonomy.md](python-profile-taxonomy.md) 作为初始 Python Profile 家族。
