# Contributing

CodeBTI is a Markdown-first skill repository. Contributions should keep the interview process recoverable, stable, and easy for agents to follow.

## Required Checks

Run this before submitting structural, question, template, translation, or manifest changes:

```sh
python3 scripts/validate_repo.py
python3 -m pytest
```

The same checks run in GitHub Actions.

For release-hardening changes, also run:

```sh
git diff --check
PYTHONPYCACHEPREFIX=/tmp/codebti_pycache python3 -m py_compile scripts/validate_repo.py
```

## Change Rules

- Update related files together. If a question changes, check the relevant profile taxonomy, template, records guide, and examples.
- Keep `shared/` project- and language-neutral. Put cross-cutting workflow decisions in `project/`; put language idioms in the language pack.
- Keep fixed question cards complete: `Question ID`, `Scope`, `Dimension`, scenario, instruction, code example, choices, scoring, pattern signals, and output implications.
- Keep generated guidance evidence-based. Cite only references that materially affect the recommendation.
- Keep the operational workflow in `docs/golden-path.md` aligned with `SKILL.md`, `README.md`, and `AGENT.md`.
- Preserve session records as the source of truth for generated output.
- Do not record secrets, private credentials, or unrelated personal information in examples or records.

## Quality Rubric

The pytest suite and repository validator enforce deterministic quality gates:

- English fixed question files must have unique `Question ID` values with the correct pack prefix.
- Fixed question scopes must match their pack: `Project`, `Language:Python`, or `Language:TypeScript`.
- Each question's choice labels must match its hidden scoring and pattern-signal labels.
- CodeStyle output implications must contain enough text to guide generation.
- Output templates must keep required sections.
- The multi-language fixture must include project, Python, TypeScript, adaptive answers, and generated shared/language guidance.
- Release-hardening docs must remain linked from the README and agent guide.

## Translation Rules

English root/shared files are the source of truth. Chinese files under `zh/` are translations or translated mirrors.

- When changing `shared/`, update the corresponding `zh/shared/` mirror in the same change.
- When changing root entry files, check whether `zh/README.md`, `zh/AGENT.md`, `zh/SKILL.md`, or `zh/TRANSLATION_STATUS.md` needs the same update.
- Run validation after translation updates to catch missing mirrors and broken links.

## Adding a Language Pack

1. Create `<lang>/questions/fixed-<lang>.md`.
2. Create `<lang>/patterns/gof/`.
3. Create `<lang>/profiles/<lang>-profile-taxonomy.md`.
4. Create `<lang>/records/README.md`.
5. Create `<lang>/templates/CodeStyle.template.md`.
6. Reference shared resources; do not copy them into the language pack.
7. Update `README.md`, `AGENT.md`, and `MANIFEST.md`.
8. Run `python3 scripts/validate_repo.py` and `python3 -m pytest`.
