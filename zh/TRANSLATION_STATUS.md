# Translation Status

This file tracks which files in the `zh/` directory are translations of English source files, and which are structurally shared.

## Shared vs Translated

### Shared (same content as root/shared/, not independently translated)

These files are language-neutral architecture/flow documents. They are symlinked or copied from the English `shared/` layer and should not be independently maintained:

- `zh/shared/questions/adaptive-question-guide.md` — shared across all languages; not independently translated
- `zh/shared/questions/editorial-guide.md` — shared across all languages; not independently translated
- `zh/shared/questions/question-format.md` — shared across all languages; not independently translated
- `zh/shared/questions/shared-architecture.md` — **reference the English version**: `../shared/questions/shared-architecture.md`
- `zh/shared/records/session-record.template.md` — shared across all languages; not independently translated
- `zh/shared/templates/SKILL.template.md` — shared across all languages; not independently translated
- `zh/shared/templates/SPEC.template.md` — shared across all languages; not independently translated

### Translated (independent Chinese content)

| File | Status | Notes |
|------|--------|-------|
| `zh/AGENT.md` | Translated | Full translation of `AGENT.md` |
| `zh/README.md` | Translated | Chinese entry point |
| `zh/SKILL.md` | Translated | Full translation of `SKILL.md` |
| `zh/python/questions/fixed-python.md` | Translated | 10 fixed Python questions in Chinese |
| `zh/python/questions/README.md` | Translated | Interview framework guide |
| `zh/python/patterns/README.md` | Translated | Pattern database index |
| `zh/python/patterns/gof/` | Translated | 22 GoF pattern pages in Chinese |
| `zh/python/profiles/README.md` | Translated | Profile inference guide |
| `zh/python/profiles/python-profile-taxonomy.md` | Translated | Profile taxonomy |
| `zh/python/records/README.md` | Translated | Session recording rules |
| `zh/python/templates/README.md` | Translated | Template guide |
| `zh/python/templates/CodeStyle.template.md` | Translated | CodeStyle output template |
| `zh/examples/CodeStyle.md` | Translated | Example CodeStyle output |
| `zh/python/patterns/gof/README.md` | Translated | Pattern index |

## Maintenance Notes

When updating English source files, check the "Translated" list above and update the corresponding Chinese files. Do not edit `zh/shared/` files — they are mirrors of the English shared layer and should be updated by running the same migration commands.

## Migration History

- 2026-04-25: Migrated from old structure (`zh/python/questions/adaptive-question-guide.md`, etc.) to mirrored shared + language pack structure. Pattern pages moved from `zh/python/patterns/python/` to `zh/python/patterns/gof/`. `zh/example/` renamed to `zh/examples/`.