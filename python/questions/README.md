# CodeBTI Question Framework

This folder defines the Python-specific CodeBTI interview round. The language round helps an agent convert Python coding preferences into project-specific guidance after the project-wide round is complete.

## Interview Flow

1. Start with the project-wide round in [../../project/questions/fixed-project.md](../../project/questions/fixed-project.md).
2. Before asking each Python question, save the full question card in `Recording.md`.
3. Ask the 10 fixed Python questions from [fixed-python.md](fixed-python.md).
4. After each answer, record the answer under `Language:Python` and give brief project-specific feedback.
5. Ask exactly 5 adaptive follow-up questions total for the whole session using [../../shared/questions/adaptive-question-guide.md](../../shared/questions/adaptive-question-guide.md).
6. Reread `Recording.md`, infer Python style dimensions and pattern tendencies, then generate Python-specific guidance inside `CodeStyle.md`.

The opening project-description prompt and project-wide questions are outside this language round. Record Python answers separately from project-wide answers and other language answers.

Ask exactly one user-facing interview question per turn. This applies to the opening prompt, each fixed question, and each adaptive follow-up question.

Each asked question must be recoverable from the record. Do not rely on chat history or source files alone; copy the full question card into `Recording.md`.

## Question Style

Questions should use concrete examples instead of pattern terminology. A user should be able to answer by looking at a small scenario or code section and choosing the style they would rather maintain.

Good questions:

- present realistic Python tradeoffs,
- cover one primary dimension at a time,
- use short code snippets when code makes the choice clearer,
- avoid trick choices,
- keep design-pattern scoring hidden from the user.

Use [../../shared/questions/question-format.md](../../shared/questions/question-format.md) for the required card structure.
Use [../../shared/questions/editorial-guide.md](../../shared/questions/editorial-guide.md) when rewriting draft questions into final form.
Use [../records/README.md](../records/README.md) for recording guidance.

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
