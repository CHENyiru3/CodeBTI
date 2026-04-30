# CodeBTI / Markdown Skill 工作流 Overlay

当 neat-freak 在 CodeBTI 或类似 Markdown-first skill 仓库里运行时，使用本 overlay。通用清理流程仍然有效；本文件补充项目专属检查，避免“Markdown 本身就是产品”的仓库发生漂移。

## 必盘点文件

在 CodeBTI 中，最小盘点范围是：

- `SKILL.md`、`README.md`、`AGENT.md`、`CONTRIBUTING.md`、`CHANGELOG.md`、`MANIFEST.md`
- `docs/*.md`
- `project/questions/*.md`、`project/profiles/*.md`、`project/templates/*.md`
- `shared/questions/*.md`、`shared/records/*.md`、`shared/templates/*.md`
- `python/**.md`、`typescript/**.md`
- `examples/*.md`
- `tests/fixtures/**/*.md`
- `zh/README.md`、`zh/AGENT.md`、`zh/SKILL.md`、`zh/TRANSLATION_STATUS.md`
- `zh/shared/**.md` 和已翻译语言包镜像
- 正在编辑的 skill 的已安装副本，例如 `~/.codex/skills/neat-freak/`

忽略 `.pytest_cache/`、build artifacts、egg-info、编辑器元数据等生成缓存，除非用户明确要求清理。

## CodeBTI 变更映射

| 变更 | 必做后续 |
|------|----------|
| 根 `SKILL.md` 工作流变化 | 若行为变化，同步 `README.md`、`AGENT.md`、`docs/golden-path.md`。 |
| `shared/` 变化 | 同一轮更新匹配的 `zh/shared/` 镜像。 |
| Python pack 变化 | 若已有翻译覆盖，同步匹配的 `zh/python/` 文件。 |
| TypeScript pack 变化 | 若已有翻译覆盖，同步匹配的 `zh/typescript/` 文件。 |
| 新顶层文件或目录 | 更新 `MANIFEST.md`；若用户可见，同时更新 `README.md` 仓库结构。 |
| 新验证规则 | 更新 `scripts/validate_repo.py`、tests、`README.md` validation 章节和 `CHANGELOG.md`。 |
| 模板结构变化 | 更新展示该模板的 examples 或 fixtures。 |
| 本仓库新增 skill package | 加入 `MANIFEST.md`；说明它是 source、translation 还是 local overlay。 |
| 已安装 skill 副本变化 | 把仓库版本复制到安装目录，并用 `diff -r` 验证。 |

## 翻译规则

- 把 `zh/TRANSLATION_STATUS.md` 当成翻译契约。
- `shared/` 与 `zh/shared/` 必须保持镜像。
- 当前 CodeBTI baseline 中，project pack 仍是 English-only，除非专门做中文 project-pack 翻译。
- 如果在嵌套 skill 下添加中文本地 overlay，且该 skill 暴露中文入口，同时提供 root reference 和 `zh/` reference。

## Manifest 规则

`MANIFEST.md` 是验证门禁的一部分。新增或删除文件后，同一轮更新它。不要列目录，除非 validator 明确 allowlist。

嵌套 skill package 要逐文件列出：

- `neat-freak/SKILL.md`
- `neat-freak/references/*.md`
- `neat-freak/zh/SKILL.md`
- `neat-freak/zh/references/*.md`

## 验证门禁

最终汇报前运行相关子集。维护 CodeBTI 仓库时，完整门禁是：

```sh
python3 scripts/validate_repo.py
python3 -m pytest
git diff --check
PYTHONPYCACHEPREFIX=/tmp/codebti_pycache python3 -m py_compile scripts/validate_repo.py
```

即使只改了嵌套 skill，也至少运行 `python3 scripts/validate_repo.py`，因为链接和 manifest 漂移最常见。

## 汇报补充

在本仓库中，适用时按这些组汇报：

```markdown
### Skill package changes
- neat-freak/SKILL.md — ...

### CodeBTI repository docs
- MANIFEST.md — ...

### Installed skill copy
- ~/.codex/skills/neat-freak — refreshed and diff-checked

### Validation
- `python3 scripts/validate_repo.py` — passed
```
