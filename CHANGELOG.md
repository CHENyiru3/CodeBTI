# Changelog

## 0.2.0 - 2026-04-28

Release-hardening baseline for the project-first CodeBTI workflow.

### Added

- Project-wide interview pack with fixed project questions, project profiles, and `ProjectStyle.md` template.
- Shared project mode: project answers govern Git workflow, validation gates, dependency governance, output shape, and recordkeeping unless a language section explicitly overrides them.
- Stable `Question ID` and `Scope` fields for English fixed project, Python, and TypeScript questions.
- Repository validator and pytest quality harness for links, pack structure, question quality, template sections, shared Chinese mirrors, manifest drift, and multi-language fixture coverage.
- GitHub Actions validation workflow.
- Multi-language fixture covering project, Python, TypeScript, adaptive answers, and generated shared/language guidance.
- Golden path workflow guide for agents and maintainers.

### Changed

- Root `SKILL.md` now routes every session through the project pack before language-specific rounds.
- Shared interview docs now stay language-neutral; project governance moved into `project/`.
- Language templates now expose shared project rules before language-specific guidance.
- Documentation now treats `Recording.md` as the recoverable source of truth for every session.

### Validation

The release baseline is expected to pass:

```sh
python3 scripts/validate_repo.py
python3 -m pytest
git diff --check
PYTHONPYCACHEPREFIX=/tmp/codebti_pycache python3 -m py_compile scripts/validate_repo.py
```

