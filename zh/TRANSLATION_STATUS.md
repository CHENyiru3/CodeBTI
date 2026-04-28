# Translation Status

This file tracks which files in the `zh/` directory are translations of English source files and which files mirror the shared architecture.

## Shared vs Translated

### Shared translated mirrors

These files mirror the English `shared/` layer in Chinese. English `shared/` files remain the source of truth. When an English shared file changes, update the corresponding Chinese mirror in the same change:

- `zh/shared/questions/adaptive-question-guide.md`
- `zh/shared/questions/editorial-guide.md`
- `zh/shared/questions/question-format.md`
- `zh/shared/questions/shared-architecture.md`
- `zh/shared/records/session-record.template.md`
- `zh/shared/templates/SKILL.template.md`
- `zh/shared/templates/SPEC.template.md`

### Translated (independent Chinese content)

The project pack (`project/`) is intentionally English-only in this baseline. Chinese entry docs link to the English project questions, profiles, and templates until a dedicated `zh/project/` translation pass is added.

| File | Status | Notes |
|------|--------|-------|
| `zh/AGENT.md` | Translated | Full translation of `AGENT.md` |
| `zh/README.md` | Translated | Chinese entry point |
| `zh/SKILL.md` | Translated | Full translation of `SKILL.md` |
| `zh/shared/` | Translated mirror | Chinese mirror of the English shared layer |
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
| `zh/typescript/questions/fixed-typescript.md` | Translated | 10 fixed TypeScript questions in Chinese |
| `zh/typescript/questions/README.md` | Translated | Interview framework guide |
| `zh/typescript/patterns/README.md` | Translated | Pattern database index |
| `zh/typescript/patterns/gof/` | Translated | 22 GoF pattern pages in Chinese |
| `zh/typescript/profiles/README.md` | Translated | Profile inference guide |
| `zh/typescript/profiles/typescript-profile-taxonomy.md` | Translated | Profile taxonomy |
| `zh/typescript/records/README.md` | Translated | Session recording rules |
| `zh/typescript/templates/README.md` | Translated | Template guide |
| `zh/typescript/templates/CodeStyle.template.md` | Translated | CodeStyle output template |

## Maintenance Notes

When updating English source files, check the "Translated" list above and update the corresponding Chinese files. For `shared/`, update both the English source and the Chinese translated mirror. Release notes and operational docs such as `CHANGELOG.md` and `docs/golden-path.md` may remain English-only unless a Chinese version is explicitly added. Run `python3 scripts/validate_repo.py` and `python3 -m pytest` before submitting changes.

## Migration History

- 2026-04-25: Migrated from old structure (`zh/python/questions/adaptive-question-guide.md`, etc.) to mirrored shared + language pack structure. Pattern pages moved from `zh/python/patterns/python/` to `zh/python/patterns/gof/`. `zh/example/` renamed to `zh/examples/`.
- 2026-04-28: Stabilized the shared layer as translated mirrors of English shared files and added validation coverage for mirror presence.
- 2026-04-28: Added release-hardening docs and tightened shared/language output templates with matching Chinese mirrors where translated files already exist.
- 2026-04-28: Updated the opening workflow to a SPEC-style intake and mirrored shared record/SPEC template changes in Chinese.
- 2026-04-28: Added opening recovery and language override decision fields to English and Chinese session record templates.
