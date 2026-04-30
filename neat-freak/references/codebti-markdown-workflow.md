# CodeBTI / Markdown Skill Workflow Overlay

Use this overlay when neat-freak runs inside CodeBTI or a similar Markdown-first skill repository. The generic cleanup flow still applies; this file adds project-specific checks that prevent drift in repos where Markdown files are the product.

## Always Inventory These Files

For CodeBTI, the minimum cleanup inventory is:

- `SKILL.md`, `README.md`, `AGENT.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, `MANIFEST.md`
- `docs/*.md`
- `project/questions/*.md`, `project/profiles/*.md`, `project/templates/*.md`
- `shared/questions/*.md`, `shared/records/*.md`, `shared/templates/*.md`
- `python/**.md`, `typescript/**.md`
- `examples/*.md`
- `tests/fixtures/**/*.md`
- `zh/README.md`, `zh/AGENT.md`, `zh/SKILL.md`, `zh/TRANSLATION_STATUS.md`
- `zh/shared/**.md` and translated language-pack mirrors
- Any installed copy of the skill being edited, for example `~/.codex/skills/neat-freak/`

Ignore generated caches such as `.pytest_cache/`, build artifacts, egg-info, and editor metadata unless the user explicitly asks to clean them.

## CodeBTI Change Mapping

| Change | Required follow-up |
|--------|--------------------|
| Root `SKILL.md` workflow changes | Update `README.md`, `AGENT.md`, `docs/golden-path.md` if behavior changed. |
| `shared/` changes | Update the matching `zh/shared/` mirror in the same pass. |
| Python pack changes | Update matching `zh/python/` files when translated coverage exists. |
| TypeScript pack changes | Update matching `zh/typescript/` files when translated coverage exists. |
| New top-level file or directory | Update `MANIFEST.md`; update `README.md` repository structure if user-facing. |
| New validation rule | Update `scripts/validate_repo.py`, tests, `README.md` validation section, and `CHANGELOG.md`. |
| Template shape changes | Update examples or fixtures that demonstrate that template. |
| New skill package in this repo | Add it to `MANIFEST.md`; explain whether it is source, translation, or local overlay. |
| Installed skill copy changed | Copy the repo version into the installed skill directory and verify `diff -r`. |

## Translation Rules

- Treat `zh/TRANSLATION_STATUS.md` as the translation contract.
- `shared/` and `zh/shared/` must stay mirrored.
- The project pack is English-only in the current CodeBTI baseline unless a dedicated Chinese project-pack pass is added.
- When adding a Chinese-only local overlay under a nested skill, include both the root reference and the `zh/` reference if the skill exposes a Chinese entry point.

## Manifest Rules

`MANIFEST.md` is part of the validation gate. After adding or removing files, update it in the same pass. Do not list directories unless the validator explicitly allowlists them.

For nested skill packages, list every source file:

- `neat-freak/SKILL.md`
- `neat-freak/references/*.md`
- `neat-freak/zh/SKILL.md`
- `neat-freak/zh/references/*.md`

## Validation Gate

Before final summary, run the relevant subset. For CodeBTI repo maintenance, the expected full gate is:

```sh
python3 scripts/validate_repo.py
python3 -m pytest
git diff --check
PYTHONPYCACHEPREFIX=/tmp/codebti_pycache python3 -m py_compile scripts/validate_repo.py
```

If only a nested skill changed, still run `python3 scripts/validate_repo.py` because link and manifest drift are common.

## Summary Format Additions

For this repository, include these groups when they apply:

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
