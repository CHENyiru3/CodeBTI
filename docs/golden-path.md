# CodeBTI Golden Path

This guide describes the expected end-to-end workflow for a normal CodeBTI session. It is the operational version of the shorter router in [../SKILL.md](../SKILL.md).

## 1. Start the Session

Ask the required opening prompt:

```text
Please describe the project as a compact SPEC-style brief. Include mission, goals, target audience, constraints, likely tech stack or language targets, roadmap intent, non-goals, and open questions. Keep this at the what/why level; avoid low-level implementation details unless they are hard constraints.
```

Use the answer to identify the target language pack or packs. If the language is unclear, ask one concise clarification before scored questions begin.

Create or update `Recording.md` in the target project root using [../shared/records/session-record.template.md](../shared/records/session-record.template.md). Record the opening answer as the project summary and SPEC intake. The opening answer is not scored.

Create or update an initial `SPEC.md` draft using [../shared/templates/SPEC.template.md](../shared/templates/SPEC.template.md). Capture what and why: mission, goals, audience, constraints, non-goals, likely tech stack, roadmap intent, and open questions. Leave implementation details to later feature specs unless the user named them as hard constraints.

If the user answers casually and misses one or more SPEC fields, record the missing fields under `Open Questions`. Do not turn the opening into a long clarification interview; reserve the highest-risk gaps for adaptive follow-up questions.

## 2. Ask Project Questions

Ask the 6 fixed project questions from [../project/questions/fixed-project.md](../project/questions/fixed-project.md).

Before each question:

- copy the full user-facing question card into `Recording.md`,
- keep hidden scoring and pattern-signal notes out of the user-facing prompt,
- ask exactly one question.

After each answer:

- update the chronological answer log,
- record selected choice, free-form notes, overrides, and feedback,
- give one or two sentences of project-specific feedback,
- move to the next question.

Project answers establish the default rules for collaboration, output shape, validation gates, shared-vs-language boundaries, dependency governance, and change records.

## 3. Ask Language Questions

For each selected language, ask that pack's fixed questions:

- Python: [../python/questions/fixed-python.md](../python/questions/fixed-python.md)
- TypeScript: [../typescript/questions/fixed-typescript.md](../typescript/questions/fixed-typescript.md)

Record each language answer set under its language target in `Recording.md`. Language answers may override project defaults only when the override is explicit and recorded.

## 4. Ask Adaptive Questions

Ask exactly 5 adaptive follow-up questions total for the session using [../shared/questions/adaptive-question-guide.md](../shared/questions/adaptive-question-guide.md).

Adaptive questions may target:

- project-level ambiguity,
- a language-specific tension,
- a cross-language conflict,
- missing validation, dependency, output, or recordkeeping detail.

## 5. Infer Profiles

After all scored answers are recorded, reread `Recording.md` and the current `SPEC.md` draft before inferring anything.

Infer:

- one project profile from [../project/profiles/project-profile-taxonomy.md](../project/profiles/project-profile-taxonomy.md),
- one language profile for each selected language,
- mixed or secondary traits when answers do not fit a single profile cleanly.

Do not treat profiles as personal traits. They are shorthand for project guidance.

## 6. Generate Outputs

Generate only the outputs requested by the user or clearly useful for the project:

- `CodeStyle.md`: primary project style guide,
- `ProjectStyle.md`: project workflow and governance summary,
- `SKILL.md`: reusable agent behavior,
- `SPEC.md`: project requirements,
- narrower specs such as `API_SPEC.md`, `TESTING_SPEC.md`, or `ARCHITECTURE_SPEC.md`.

For single-language projects, use that language's `CodeStyle.template.md`. For multi-language projects, use [../project/templates/MultiLanguageCodeStyle.template.md](../project/templates/MultiLanguageCodeStyle.template.md), put shared project rules first, then language-specific sections, and cite only local pattern or profile pages that materially affected the guidance.

## 7. Validate and Handoff

If maintaining this CodeBTI repository, run:

```sh
python3 scripts/validate_repo.py
python3 -m pytest
git diff --check
PYTHONPYCACHEPREFIX=/tmp/codebti_pycache python3 -m py_compile scripts/validate_repo.py
```

If generating guidance for another project, record that project's own validation command in `Recording.md`.

Final handoff should state:

- generated files,
- inferred project and language profiles,
- validation commands run and results,
- unresolved assumptions.

Between feature implementations, replan by rereading `SPEC.md`, updating it with changed mission, stack, roadmap, or constraints, and recording the rationale in `Recording.md`.
