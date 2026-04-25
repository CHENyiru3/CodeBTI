# CodeBTI Profiles

Profiles summarize the user's CodeBTI answers into practical engineering guidance. A profile is a shorthand for coding preferences, not a judgment of skill or personality.

Use profiles after the 10 fixed questions and 5 adaptive questions are complete.

## Inference Inputs

Use these inputs together:

- fixed question answers from [questions/fixed-typescript.md](../questions/fixed-typescript.md),
- adaptive answers from [../../shared/questions/adaptive-question-guide.md](../../shared/questions/adaptive-question-guide.md),
- project context,
- pattern signals from [patterns/](../patterns/README.md),
- contradictions or weak signals recorded in [../../shared/records/session-record.template.md](../../shared/records/session-record.template.md).

## Inference Rules

- Prefer the strongest repeated style signals.
- Do not assign a profile from one answer alone.
- Record contradictions instead of forcing a clean label.
- Use pattern names as supporting evidence, not the main result.
- Generate concrete `CodeStyle.md` rules from the profile.

## TypeScript Taxonomy

Use [typescript-profile-taxonomy.md](typescript-profile-taxonomy.md) for the TypeScript profile families.