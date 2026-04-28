# Session Records

This folder stores Python CodeBTI interview records or archived project records that include a Python language round. A record preserves the user's project description, full question cards, project answers, language answers, adaptive answers, feedback, agent observations, and final style inference.

During an interview, maintain a live `Recording.md` in the target project root. Update it after every answer before asking the next question. At the end, reread `Recording.md` before generating `CodeStyle.md`, `ProjectStyle.md`, `SKILL.md`, or `SPEC.md`.

After the interview, either keep `Recording.md` in the project or copy it into this folder with one markdown file per interview session.

Filename format:

```text
YYYY-MM-DD-project-slug.md
```

Example:

```text
2026-04-22-python-cli-tool.md
```

## Recording Rules

- Record the full user-facing question card for every fixed and adaptive question: title, dimension, scenario, instruction, code example if present, choices, and source path.
- Record the user's selected answer and any short explanation they gave.
- Record a concise chronological QA history as the interview proceeds.
- Record the brief feedback response given after each answer.
- Record answer changes when the user goes back and reselects.
- Keep hidden scoring separate from user-facing answers.
- Do not record secrets, credentials, private tokens, or unrelated personal details.
- Prefer concise notes over full conversation transcripts.
- Preserve enough evidence that another agent can understand why the final `CodeStyle.md` was generated.
- Treat the final `Recording.md` as the source of truth for generated markdown outputs.

## What To Record

Each session should include:

- project summary,
- interview date,
- language targets,
- interview progress,
- full question card snapshots,
- chronological QA history,
- project and language fixed question answers,
- adaptive question answers,
- brief feedback given to the user,
- answer changes,
- style-axis summary,
- pattern signals,
- unresolved assumptions,
- generated output files.

Use [../../shared/records/session-record.template.md](../../shared/records/session-record.template.md) as the starting point.
