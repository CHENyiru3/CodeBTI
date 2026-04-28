# CodeBTI Project Questions

This folder defines the project-wide CodeBTI interview round. Ask these questions once for the whole project before any language-specific round.

## Interview Flow

1. Ask the required SPEC-style opening prompt from the root `SKILL.md`.
2. Create or update a live `Recording.md` using [../../shared/records/session-record.template.md](../../shared/records/session-record.template.md).
3. Create or update the initial `SPEC.md` draft using [../../shared/templates/SPEC.template.md](../../shared/templates/SPEC.template.md).
4. Record the opening answer as the project summary and SPEC intake.
5. Ask the project-wide questions from [fixed-project.md](fixed-project.md).
6. Record the full question card before asking each question, then record the answer and brief feedback.
7. Continue with one language-specific round for each selected language pack, such as Python or TypeScript.
8. Use [../../shared/questions/adaptive-question-guide.md](../../shared/questions/adaptive-question-guide.md) for exactly 5 adaptive follow-ups across the whole session.

The project-wide round controls cross-cutting decisions: collaboration, repository layout, test gates, dependency posture, output shape, and multi-language boundaries. Language packs should not duplicate those decisions unless a language has a specific override.

## Question Style

Project questions should avoid language-specific code unless the tradeoff is about a concrete toolchain. Every answer should change the generated `CodeStyle.md`, `SKILL.md`, `SPEC.md`, or agent workflow.

Use [../../shared/questions/question-format.md](../../shared/questions/question-format.md) for the card structure and [../../shared/questions/editorial-guide.md](../../shared/questions/editorial-guide.md) for wording rules.
