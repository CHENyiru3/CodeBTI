# CodeBTI Question Framework

This folder defines the CodeBTI interview system. The interview helps an agent convert a user's project goals and coding preferences into a project-specific `CodeStyle.md`, `SKILL.md`, or `SPEC.md`.

## Interview Flow

1. Ask the required opening prompt: "What kind of project do you want to build? Please describe shortly."
2. Create or update a live `Recording.md` using [../../shared/records/session-record.template.md](../../shared/records/session-record.template.md).
3. Before asking each question, save the full question card in `Recording.md`.
4. Ask the 10 fixed TypeScript questions from [fixed-typescript.md](fixed-typescript.md).
5. After each answer, record the answer and give brief project-specific feedback.
6. Ask exactly 5 adaptive follow-up questions using [../../shared/questions/adaptive-question-guide.md](../../shared/questions/adaptive-question-guide.md).
7. Reread `Recording.md`, infer style dimensions and pattern tendencies, then generate a project-specific `CodeStyle.md`.

The opening project-description prompt is pre-interview context. Record it as the session `Project Summary`; do not count it as one of the 10 fixed questions.

Ask exactly one user-facing interview question per turn. This applies to the opening prompt, each fixed question, and each adaptive follow-up question.

Each asked question must be recoverable from the record. Do not rely on chat history or source files alone; copy the full question card into `Recording.md`.

## Question Style

Questions should use concrete examples instead of pattern terminology. A user should be able to answer by looking at a small scenario or code section and choosing the style they would rather maintain.

Good questions:

- present realistic TypeScript tradeoffs,
- cover one primary dimension at a time,
- use short code snippets when code makes the choice clearer,
- avoid trick choices,
- keep design-pattern scoring hidden from the user.

Use [../../shared/questions/question-format.md](../../shared/questions/question-format.md) for the required card structure.
Use [../../shared/questions/editorial-guide.md](../../shared/questions/editorial-guide.md) when rewriting draft questions into final form.
Use [../../records/README.md](../../records/README.md) for recording guidance.

## Scoring Principle

Answers map to CodeBTI style dimensions first and design-pattern signals second. For example, a choice may primarily signal "interface-first abstraction" and only secondarily suggest Strategy, Bridge, or Abstract Factory.

The interview result should guide coding consistency. It should not judge the user's ability or personality.

## Organization Pass

When the user provides draft questions, organize them with a medium rewrite:

1. Keep the user's dimension and core idea.
2. Rewrite the scenario and choices for balance.
3. Simplify wording without making the topic unserious.
4. Add or trim code examples so each option feels equally realistic.
5. Add hidden scoring and `CodeStyle.md` implications.