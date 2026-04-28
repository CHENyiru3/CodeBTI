# CodeStyle

项目：
TODO：项目名称或简短标识。

来源会话记录：
TODO：`Recording.md` 或归档记录路径。

项目 CodeBTI Profile：
TODO：来自 `project/profiles/project-profile-taxonomy.md` 的项目 Profile。

TypeScript CodeBTI Profile：
TODO：主要 TypeScript Profile 和次要特征。

证据规则：
以下每条规则都必须能追溯到会话记录。证据不足时，写入 `开放假设`，不要编造规则。

## 项目意图

目的：
TODO：用一段话说明项目是什么，以及为什么需要这份风格指南。

主要约束：
TODO：正确性、速度、可维护性、学习目标、交付压力等用户可见约束。

成功信号：
TODO：未来 Agent 如何判断 TypeScript 变更符合项目需要。

## 证据摘要

使用的项目答案：
TODO：总结控制共享行为的 P1-P6 决策。

使用的 TypeScript 答案：
TODO：总结塑造 TypeScript 风格的 Q1-Q10 决策。

使用的适应性答案：
TODO：总结改变或澄清指导的适应性答案。

## 共享项目规则

输出形态：
TODO：必需的最终产物，以及本文件是单语言指南还是多语言指南的一部分。

Git 和协作：
TODO：来自项目答案的分支、审查、提交和交接要求。

验证门禁：
TODO：完成变更前必需的具体命令或手动检查。

依赖治理：
TODO：何时允许新增、替换或避免 TypeScript 依赖。

记录要求：
TODO：必须保存在 `Recording.md`、changelog、release note 或 review note 中的内容。

语言覆盖策略：
TODO：说明 TypeScript 是遵循共享默认规则，还是有明确记录的覆盖规则。

## 默认代码形态

首选组织方式：
TODO：模块/包结构以及新代码应该放在哪里。

模块和文件夹规则：
TODO：命名、边界和导入规则。

何时添加抽象：
TODO：有证据支持的接口、类、函数、服务、工厂或 helper 触发条件。

何时保持直接：
TODO：更适合普通函数、局部类型或直接组合的场景。

## TypeScript 风格规则

命名：
TODO：命名约定及例外。

类型：
TODO：严格类型、边界类型、运行时验证或灵活风格。

接口 vs 类型别名：
TODO：何时使用 `interface`、`type`、类、判别联合或泛型。

数据建模：
TODO：schema 库、DTO、普通对象、领域类或推导类型。

错误处理：
TODO：异常、结果对象、降级和日志策略。

异步模式：
TODO：Promise、取消、重试、并发和失败处理。

状态管理：
TODO：可变状态、store、context、singleton 和配置规则。

依赖管理：
TODO：TypeScript 工具和包的依赖策略。

注释和 JSDoc：
TODO：哪里必需、可选或不建议写注释/JSDoc。

## 模式指导

鼓励的模式：
TODO：要使用的本地模式页面，以及每个模式适用的具体原因。

谨慎使用的模式：
TODO：仅在特定约束下可接受的模式页面。

默认避免的模式：
TODO：应避免的模式页面，以及项目特定原因。

模式参考：
TODO：精选链接到 `typescript/patterns/gof/` 中的相关本地页面。

## 引用

设计模式参考：

- 鼓励：TODO。链接到 `typescript/patterns/gof/` 中的相关本地页面并说明原因。
- 谨慎使用：TODO。链接到 `typescript/patterns/gof/` 中的相关本地页面并说明约束。
- 默认避免：TODO。链接到 `typescript/patterns/gof/` 中的相关本地页面并说明为什么通常应该避免。

有用的项目资源：

- TODO：链接到用于证明指导合理性的相关本地模板、Profile 分类条目、框架文档或库文档。

引用规则：

- 优先使用本地 CodeBTI 模式页面进行设计模式指导。
- 仅包含影响生成推荐内容的参考。
- 每个参考都应用一句话解释它支持的实用规则。
- 不要仅仅因为提到了某个模式就引用它；当它被鼓励、谨慎使用或明确避免时才引用。
- 保持引用精选而非穷举。

## 测试策略

必需的测试：
TODO：交接前预期的 TypeScript 测试类型或具体命令。

可选的测试：
TODO：风险或范围增加时有用的测试。

手动验证：
TODO：自动化覆盖不足时必需的手动检查。

## Git 和协作

分支策略：
TODO：TypeScript 变更的分支或 checkpoint 策略。

提交信息：
TODO：提交信息风格和必需证据。

审查清单：
TODO：未来 Agent 审查 TypeScript 变更时应使用的问题。

## Agent 行为

编写代码时：
TODO：给未来编码 Agent 的具体指令。

审查代码时：
TODO：具体审查姿态和常见风险。

不确定时：
TODO：何时询问用户、记录假设或选择项目默认规则。

## 示例

首选代码形态：

```typescript
// TODO：展示首选 TypeScript 风格的最小示例。
```

避免的代码形态：

```typescript
// TODO：展示未来 Agent 应避免内容的最小示例。
```

## 开放假设

- TODO：未解决或证据较弱的假设。
