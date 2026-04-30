# 同步影响矩阵

开发阶段收尾时，用这张表判断哪些知识层需要更新。它用于帮助思考，不能替代实际阅读文件。

| 变更类型 | Agent 记忆 | 项目 agent 指南（`CLAUDE.md` / `AGENTS.md`） | 人类文档（`README.md`, `docs/`） |
|----------|------------|-----------------------------------------------|----------------------------------|
| 新 API 路由或 endpoint | 仅在影响未来 agent 决策时记录 | 增加路由清单、鉴权假设、本地测试命令 | 更新 integration guide、architecture routes、API reference、示例 |
| API contract 变化 | 修正过期假设 | 替换旧 contract 说明 | 更新 integration guide、API reference、迁移说明、changelog |
| 新环境变量 | 通常不记，除非是跨项目习惯 | 添加变量表、默认值、secret 处理 | 更新 runbook、setup guide、deployment docs、下游集成 |
| 环境变量改名或删除 | 删除旧记忆 | 替换或删除旧变量名 | 更新 setup、deployment、runbook、CI/deploy 说明 |
| 新数据库表或 collection | 只记录非显而易见的设计决策 | 添加 schema/data-model 说明和 migration 命令 | 更新 architecture data model、migrations、operations guide |
| 数据迁移 | 若可复用，记录运维决策 | 添加 migration 命令和 rollback 注意事项 | 更新 runbook、release notes、deployment checklist |
| 跨多文件新功能 | 捕捉持久设计决策 | 添加 feature map、涉及模块、不变量 | 更新 architecture、integration guide、runbook、handoff/changelog |
| 无行为变化的重构 | 若已有旧模块图则修正 | 更新模块归属和命令 | 只有公开结构变化时更新 architecture |
| 新 CLI 命令 | 若成为默认工作流则记录 | 添加命令和常用参数 | 更新 README、CLI reference、runbook 示例 |
| 新后台任务或 scheduler | 记录非显而易见的运行假设 | 添加 job 名称、触发方式、本地运行命令 | 更新 architecture、runbook、monitoring/troubleshooting |
| 新依赖或外部服务 | 若策略特殊则记录 | 添加依赖用途和 setup 注意事项 | 更新 README/setup、architecture、runbook、安全说明 |
| 鉴权或权限变化 | 修正旧安全假设 | 添加 auth flow 和 required roles | 更新 integration guide、architecture、runbook、API 示例 |
| 部署/runtime 变化 | 修正旧部署假设 | 添加命令、端口、服务、环境变量 | 更新 README、deployment docs、runbook、handoff |
| 测试策略变化 | 若是持久偏好则记录 | 添加 validation gates | 更新 contributor docs 和 runbook |
| 跨项目 contract 变化 | 记录持久项目关系 | 更新双方项目 agent 指南 | 更新上游和下游 integration docs |
| 临时计划完成 | 删除或压缩为持久事实 | 删除已完成 task list | 只把有意义的完成信息移到 changelog/handoff |
| 决策被推翻 | 替换旧决策 | 替换旧指导 | 更新 architecture decision notes 或删除 stale docs |

## 必查配对

- 新 API 路由：integration guide + architecture。
- 新环境变量：runbook + 项目 agent 指南。
- 新数据库表：architecture data model + 项目 agent 指南。
- 新外部集成：integration guide + runbook + architecture。
- 跨项目变化：上游 docs + 下游 docs。
- 公开行为变化：README 或用户面对文档 + changelog/handoff。

## 红旗

- 文档里出现“最近”“今天”“昨天”“上周”等相对时间，却没有绝对日期。
- `CLAUDE.md` / `AGENTS.md` 写了只有人类需要的信息，而 `docs/` 没写。
- `README.md` 的安装/运行命令与 package scripts、Make targets 或测试命令不一致。
- architecture 文档仍提旧模块名或已移除服务。
- 记忆说某任务待做，但代码显示已经完成。
- 下游 integration docs 仍展示旧 endpoint、环境变量、payload 或 auth flow。
