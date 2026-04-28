# Fixed Project Questions

This file defines the 6 project-wide CodeBTI questions. Ask these once before language-specific questions. Keep `Agent scoring`, `Pattern signals`, and `CodeStyle output implications` hidden unless the user explicitly asks how CodeBTI works.

## P1. Project Control Model

Question ID:
project.control.model

Scope:
Project

Dimension:
Speed-first collaboration vs recorded checkpoints vs review-gated workflow vs release-managed workflow.

User-facing scenario:
When a human and an AI agent work on this project, how controlled should the change process be?

User-facing instruction:
Choose the workflow you would most naturally want to maintain. You can revise earlier answers at any time.

Code example:
None. This question is about collaboration control, not code.

Choices:
- A. Fast shared branch: keep the process light, with short notes and direct edits.
- B. Recorded checkpoints: keep a live record of decisions and require agents to update it before moving on.
- C. Review-gated changes: use branches, pull requests, validation checks, and review notes before merging.
- D. Release-managed changes: group work into planned milestones with versioned releases and migration notes.

Agent scoring:
- A: Speed-first, low ceremony, accepts higher recovery burden.
- B: Traceability-first, prefers recoverable agent state and explicit decision logs.
- C: Reliability-first, wants validation gates and reviewer-friendly patches.
- D: Release-discipline-first, expects staged delivery and compatibility notes.

Pattern signals:
- A: Avoid heavy process abstractions.
- B: Supports session-record and decision-log workflows.
- C: Supports CI gates, review checklists, and controlled agent execution.
- D: Supports release checklists and compatibility tracking.

CodeStyle output implications:
Set the default collaboration workflow, minimum recordkeeping, and required validation before future agent edits are considered complete.

## P2. Output Shape

Question ID:
project.output.shape

Scope:
Project

Dimension:
Single guidance file vs layered docs vs generated skill/spec split vs language-specific outputs.

User-facing scenario:
After the interview, what form should the project guidance take so future agents can follow it reliably?

User-facing instruction:
Choose the output shape you would most naturally maintain. You can revise earlier answers at any time.

Code example:
None. This question is about documentation structure.

Choices:
- A. One `CodeStyle.md`: keep the final guidance in one project-level file.
- B. Layered docs: keep a project overview plus focused files for architecture, testing, and dependencies.
- C. Skill and spec split: generate `SKILL.md` for agent behavior and `SPEC.md` for project requirements.
- D. Per-language sections: keep one project file with separate language-specific sections and shared rules first.

Agent scoring:
- A: Simplicity-first output, fewer files to maintain.
- B: Documentation-structure preference, expects focused references.
- C: Agent-operational preference, separates behavior rules from requirements.
- D: Multi-language coordination preference, centralizes cross-cutting rules.

Pattern signals:
- A: Avoid output fragmentation.
- B: Supports modular documentation.
- C: Supports reusable agent behavior.
- D: Supports facade-like project guidance with language-specific internals.

CodeStyle output implications:
Set the required generated files and how shared versus language-specific guidance should be organized.

## P3. Validation Gate

Question ID:
project.validation.gate

Scope:
Project

Dimension:
Manual verification vs lightweight checks vs CI-required validation vs release-quality test matrix.

User-facing scenario:
What should block future changes from being considered stable?

User-facing instruction:
Choose the validation level you would most naturally enforce. You can revise earlier answers at any time.

Code example:
None. This question is about project checks and acceptance criteria.

Choices:
- A. Manual review notes: agents explain what they checked, but no automated gate is required.
- B. Lightweight local checks: run fast validation for links, structure, and obvious consistency problems.
- C. CI-required checks: every pull request or shared branch update must pass automated validation.
- D. Release matrix: major changes require examples, compatibility checks, and release notes.

Agent scoring:
- A: Low automation, relies on human judgment.
- B: Stability-first with low tooling overhead.
- C: Gate-first, expects repeatable checks before integration.
- D: Release-quality discipline, accepts more process for lower regression risk.

Pattern signals:
- A: Avoid process machinery.
- B: Supports script-based structural validation.
- C: Supports CI and review workflows.
- D: Supports milestone/release checklists.

CodeStyle output implications:
Set required validation commands, CI expectations, and what must be reported in final agent responses.

## P4. Shared Versus Language-Specific Rules

Question ID:
project.shared-language.boundary

Scope:
Project

Dimension:
Shared defaults vs language overrides vs fully separate language guidance vs framework conventions.

User-facing scenario:
If this project uses multiple languages, how should shared decisions and language-specific decisions relate?

User-facing instruction:
Choose the boundary model you would most naturally maintain. You can revise earlier answers at any time.

Code example:
None. This question is about project boundaries.

Choices:
- A. Shared defaults first: one project policy controls Git, testing, dependencies, and agent behavior unless overridden.
- B. Language overrides: shared defaults exist, but each language section may override rules with a clear reason.
- C. Separate language guides: each language gets its own guidance file with only a short shared summary.
- D. Framework conventions first: each language follows its framework or ecosystem conventions, with minimal shared policy.

Agent scoring:
- A: Strong project-level consistency.
- B: Balanced multi-language coordination.
- C: Language autonomy preference, higher duplication risk.
- D: Ecosystem-aligned preference, avoids fighting frameworks.

Pattern signals:
- A: Supports centralized project facade.
- B: Supports explicit adapter-style language boundaries.
- C: Supports independent module ownership.
- D: Supports framework-aligned builder traits.

CodeStyle output implications:
Define how agents should handle cross-cutting rules and when language-specific guidance may override project defaults.

## P5. Dependency Governance

Question ID:
project.dependency.governance

Scope:
Project

Dimension:
Minimal dependencies vs approved dependency policy vs lockfile discipline vs ecosystem-friendly growth.

User-facing scenario:
When agents want to add packages, tools, or services, what policy should control that decision?

User-facing instruction:
Choose the dependency policy you would most naturally enforce. You can revise earlier answers at any time.

Code example:
None. This question is about dependency governance across the project.

Choices:
- A. Minimal dependencies: avoid new packages unless the standard toolchain is clearly insufficient.
- B. Justified additions: allow dependencies when the agent records why they are needed and how they will be maintained.
- C. Lockfile discipline: every dependency change must update the appropriate lockfile or environment source of truth.
- D. Ecosystem-friendly: prefer proven libraries and framework-native tools when they reduce custom code.

Agent scoring:
- A: Supply-chain cautious, low external dependency posture.
- B: Controlled dependency growth.
- C: Reproducibility-first.
- D: Ecosystem-aligned, accepts dependency cost for speed and correctness.

Pattern signals:
- A: Supports algorithm-first and lightweight project styles.
- B: Supports adapter/facade boundaries around external tools.
- C: Supports CI and release repeatability.
- D: Supports framework-aligned builder traits.

CodeStyle output implications:
Set the cross-language dependency approval rule and require generated guidance to identify each language's dependency source of truth.

## P6. Change Record Policy

Question ID:
project.change-record.policy

Scope:
Project

Dimension:
Minimal notes vs decision log vs session record as evidence vs auditable history.

User-facing scenario:
How much evidence should future agents preserve when they make or revise project guidance?

User-facing instruction:
Choose the recordkeeping style you would most naturally maintain. You can revise earlier answers at any time.

Code example:
None. This question is about project memory and recoverability.

Choices:
- A. Minimal notes: keep only final generated guidance and brief assumptions.
- B. Decision log: record important choices and why they changed.
- C. Full session evidence: keep the interview record, full question cards, answers, feedback, and hidden inference notes.
- D. Auditable history: keep session evidence plus release notes, validation results, and migration notes.

Agent scoring:
- A: Low record overhead.
- B: Decision traceability without full transcripts.
- C: Recoverability-first, treats the session record as evidence.
- D: Governance-first, supports stable releases and audits.

Pattern signals:
- A: Avoid documentation ceremony.
- B: Supports durable agent handoff.
- C: Supports evidence-grounded inference.
- D: Supports release-managed workflows.

CodeStyle output implications:
Set how much evidence agents must preserve and where future changes should record rationale.
