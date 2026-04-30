# Agent 路径速查

清理知识库前，先用本文件查找常见记忆和项目指南位置。路径是约定，不是保证；不存在就记录为“不存在”，继续审查项目文档。

## Claude Code

| 范围 | 常见路径 | 检查内容 |
|------|----------|----------|
| 全局指令 | `~/.claude/CLAUDE.md` | 只放跨项目用户偏好。 |
| 项目记忆 | `~/.claude/projects/<project-id>/memory/` | `MEMORY.md` 及其引用的 markdown。 |
| 项目指令 | `<project-root>/CLAUDE.md` | 项目专属 agent 规则和注意事项。 |

## OpenAI Codex

| 范围 | 常见路径 | 检查内容 |
|------|----------|----------|
| 全局指令 | `~/.codex/AGENTS.md` | 只放跨项目用户偏好。 |
| 本地记忆 | `~/.codex/memories/` | 若存在，检查用户级记忆文件。 |
| 项目指令 | `<project-root>/AGENTS.md` | 项目专属 agent 规则和注意事项。 |
| 技能文件 | `~/.codex/skills/<skill-name>/SKILL.md` | 已安装的 assistant skill。 |

## OpenCode

| 范围 | 常见路径 | 检查内容 |
|------|----------|----------|
| 项目配置 | `<project-root>/.opencode/` | Agent 配置和项目本地指南。 |
| 项目指令 | `<project-root>/AGENTS.md` 或等价文件 | 项目专属 agent 规则。 |

## OpenClaw

| 范围 | 常见路径 | 检查内容 |
|------|----------|----------|
| 全局配置 | `~/.openclaw/` | 用户级偏好和记忆文件。 |
| 项目指令 | `<project-root>/AGENTS.md` 或等价文件 | 项目专属 agent 规则。 |

## 兜底发现

平台路径不存在时，检查项目自身：

```sh
find <project-root> -maxdepth 3 \
  \( -name "CLAUDE.md" -o -name "AGENTS.md" -o -name "README.md" -o -path "*/docs/*.md" \) \
  -not -path "*/node_modules/*" \
  -not -path "*/.git/*"
```

除非对话明确建立了跨项目规则，否则不要创建或更新全局记忆/配置。
