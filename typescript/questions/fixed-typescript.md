# Fixed TypeScript Questions

This file defines the 10 fixed CodeBTI questions for TypeScript projects.

Users can revise earlier answers at any time. During an interview, show the user-facing scenario, instruction, code example, and choices. Keep `Agent scoring`, `Pattern signals`, and `CodeStyle output implications` hidden unless the user explicitly asks how CodeBTI works.

## Q1. General Purpose and Paradigm

Question ID:
typescript.default.shape

Scope:
Language:TypeScript

Dimension:
Class-based vs interface-based vs functional vs flat procedural organization.

User-facing scenario:
When starting a fresh TypeScript project, how do you naturally organize the core logic? Here is the same small task — greeting a user with their age — written in four different styles.

User-facing instruction:
Choose the style you would most naturally want to maintain. You can revise earlier answers at any time.

Code example:

```typescript
// A. Class-based
class User {
  readonly name: string;
  readonly birthYear: number;

  constructor(name: string, birthYear: number) {
    this.name = name;
    this.birthYear = birthYear;
  }

  greeting(currentYear: number): string {
    return `Hi ${this.name}, you are ${currentYear - this.birthYear}.`;
  }
}

// B. Interface-based with functions
interface User {
  name: string;
  birthYear: number;
}

function greeting(user: User, currentYear: number): string {
  return `Hi ${user.name}, you are ${currentYear - user.birthYear}.`;
}

// C. Type alias with readonly fields
type UserData = {
  readonly name: string;
  readonly birthYear: number;
};

function greeting(user: UserData, currentYear: number): string {
  return `Hi ${user.name}, you are ${currentYear - user.birthYear}.`;
}

// D. Simple object without explicit typing
function greeting(name: string, birthYear: number, currentYear: number): string {
  return `Hi ${name}, you are ${currentYear - birthYear}.`;
}
```

Choices:
- A. Class-based: keep state and behavior together in classes with access modifiers.
- B. Interface-based: define data shapes with interfaces and use standalone functions.
- C. Type alias: prefer `type` aliases for modeling data, with utility types for transformations.
- D. Simple and direct: write straightforward functions without explicit type wrappers.

Agent scoring:
- A: Class-friendly, encapsulation-first, comfortable with objects owning behavior.
- B: Interface-first, explicit contracts, prefers functions over methods.
- C: Data-shape-first, likes utility types, mapped types, and readonly immutability.
- D: Low ceremony, speed-first, comfortable with scripts and direct function calls.

Pattern signals:
- A: Possible [State](../patterns/gof/state.md), [Template Method](../patterns/gof/template-method.md), [Strategy](../patterns/gof/strategy.md) as classes.
- B: Possible [Strategy](../patterns/gof/strategy.md) as callable interfaces, [Adapter](../patterns/gof/adapter.md).
- C: Possible [Builder](../patterns/gof/builder.md) or [Factory Method](../patterns/gof/factory-method.md) when typed construction grows.
- D: Avoid premature GoF patterns; prefer small helpers and clear modules.

CodeStyle output implications:
Use this answer to set the default project shape: class-centered, interface-first, type-alias data-model, or function-first. Future guidance should explain when the project may deviate from that default.

## Q2. Defensive Coding and Type Boundaries

Question ID:
typescript.typing.boundaries

Scope:
Language:TypeScript

Dimension:
Strict static typing vs boundary typing vs runtime validation vs flexible duck typing.

User-facing scenario:
TypeScript gives you control over how strictly types are enforced. For a function that updates a user's age, how strict should the project be?

User-facing instruction:
Choose the style you would most naturally want to maintain. You can revise earlier answers at any time.

Code example:

```typescript
// A. Strict type narrowing
function updateUserAge(userId: number, newAge: number): boolean {
  if (typeof newAge !== 'number' || !Number.isInteger(newAge)) {
    throw new TypeError('newAge must be an integer');
  }
  if (newAge <= 0) {
    throw new RangeError('newAge must be positive');
  }
  const user = dbGet(userId);
  user.age = newAge;
  dbSave(user);
  return true;
}

// B. Boundary typing
function updateUserAge(userId: number, newAge: number): boolean {
  const user = dbGet(userId);
  if (newAge <= 0) return false;
  user.age = newAge;
  dbSave(user);
  return true;
}

// C. Runtime validation with a schema library
import { z } from 'zod';

const AgeUpdateSchema = z.object({
  userId: z.number().int().positive(),
  newAge: z.number().int().positive(),
});

function updateUserAge(rawInput: unknown): boolean {
  const payload = AgeUpdateSchema.parse(rawInput);
  const user = dbGet(payload.userId);
  user.age = payload.newAge;
  dbSave(user);
  return true;
}

// D. Flexible duck typing
function updateUserAge(userId: unknown, newAge: unknown): boolean {
  const id = Number(userId);
  const age = Number(newAge);
  if (!id || !age) return false;
  const user = dbGet(id);
  user.age = age;
  dbSave(user);
  return true;
}
```

Choices:
- A. Strict type narrowing: use `typeof` checks, type guards, and explicit error throwing in important functions.
- B. Boundary typing: type public function signatures strictly, but keep internal code flexible.
- C. Runtime validation: use a schema library like Zod, Yup, or class-validator to clean and check incoming data.
- D. Flexible duck typing: accept broad input types and coerce them safely, keeping type checks lightweight.

Agent scoring:
- A: High defensive coding, explicit invariants, stronger static-analysis posture.
- B: Boundary-first discipline, pragmatic internal flexibility.
- C: Validation-first, accepts runtime model libraries and coercion.
- D: Flexible, low ceremony, duck-typing friendly.

Pattern signals:
- A: Supports explicit interfaces, protocols, strict [Adapter](../patterns/gof/adapter.md).
- B: Supports [Facade](../patterns/gof/facade.md) and [Adapter](../patterns/gof/adapter.md) at boundaries without overtyping internals.
- C: Supports data-first modeling, validation boundaries, [Builder](../patterns/gof/builder.md) for complex payloads.
- D: Avoid heavy interface patterns unless project risk demands them.

CodeStyle output implications:
Set the typing policy, validation strategy, and where agents should add checks. This answer should prevent future code from mixing strict type-heavy style with casual untyped style without a clear boundary.

## Q3. Error Handling and Recovery

Question ID:
typescript.error.recovery

Scope:
Language:TypeScript

Dimension:
Fail-fast exceptions vs safe fallback vs explicit result objects vs batch quarantine.

User-facing scenario:
The project receives transaction payloads from a JSON API. Sometimes `amount` is missing or is a value like `"N/A"`. How should the code handle that kind of bad input?

User-facing instruction:
Choose the style you would most naturally want to maintain. You can revise earlier answers at any time.

Code example:

```typescript
// A. Fail fast
class MalformedTransactionError extends Error {
  constructor(message: string) {
    super(message);
    this.name = 'MalformedTransactionError';
  }
}

function calculateTotal(tx: Record<string, unknown>): number {
  if (!('amount' in tx)) {
    throw new MalformedTransactionError('Transaction is missing amount');
  }
  if (typeof tx.amount !== 'number') {
    throw new MalformedTransactionError('Transaction amount must be numeric');
  }
  return tx.amount * 1.2;
}

// B. Safe fallback
function calculateTotal(tx: Record<string, unknown>): number {
  const amount = Number(tx.amount ?? 0);
  return isNaN(amount) ? 0 : amount * 1.2;
}

// C. Explicit result
type Result<T> =
  | { ok: true; value: T }
  | { ok: false; error: string };

function calculateTotal(tx: Record<string, unknown>): Result<number> {
  const amount = tx.amount;
  if (typeof amount !== 'number') {
    return { ok: false, error: 'Invalid amount' };
  }
  return { ok: true, value: amount * 1.2 };
}

// D. Log and continue
import { Logger } from './logger';

function processBatch(transactions: Record<string, unknown>[]): number[] {
  const totals: number[] = [];
  for (const tx of transactions) {
    try {
      const amount = Number(tx.amount);
      if (!isNaN(amount)) {
        totals.push(amount * 1.2);
      } else {
        Logger.warn(`Skipped invalid transaction: ${JSON.stringify(tx)}`);
      }
    } catch (err) {
      Logger.warn(`Skipped transaction: ${err instanceof Error ? err.message : err}`);
    }
  }
  return totals;
}
```

Choices:
- A. Fail fast: throw a clear typed error as soon as invalid data appears.
- B. Safe fallback: return a default value and keep the main flow moving.
- C. Explicit result: return a structured success or failure value instead of raising for expected problems.
- D. Log and continue: record the failure, skip the bad item, and keep processing the rest.

Agent scoring:
- A: Contract-first, correctness over continuity, exception-friendly.
- B: Continuity-first, tolerant fallback style, risk of hiding data quality issues.
- C: Explicit control flow, result-object style, good for recoverable business errors.
- D: Batch-resilient, observability-friendly, good for data pipelines.

Pattern signals:
- A: Supports boundary validation, strict [Facade](../patterns/gof/facade.md), custom error class hierarchy.
- B: Supports tolerant [Adapter](../patterns/gof/adapter.md)/[Facade](../patterns/gof/facade.md) behavior but needs clear fallback policy.
- C: Supports functional style, [Command](../patterns/gof/command.md) outcomes, explicit workflow states.
- D: Supports pipeline style, [Chain of Responsibility](../patterns/gof/chain-of-responsibility.md), quarantine/dead-letter workflows.

CodeStyle output implications:
Define the project-wide error policy so agents do not mix silent defaults, exceptions, result objects, and quarantine behavior randomly.

## Q4. Naming and Readability

Question ID:
typescript.naming.readability

Scope:
Language:TypeScript

Dimension:
Explicit names vs concise idioms vs domain vocabulary vs comment-supported naming.

User-facing scenario:
Names shape how a codebase feels to read. How should variables, functions, interfaces, and classes be named in this project?

User-facing instruction:
Choose the style you would most naturally want to maintain. You can revise earlier answers at any time.

Code example:
None. The choice is about naming style and review expectations.

Choices:
- A. Explicit names: prefer names like `calculateTotalRevenueForActiveUsers`, even when they are longer.
- B. Concise idioms: allow short common names like `id`, `req`, `cfg`, or `idx` when context is clear.
- C. Domain language: use the terms from the product, business, math, or science domain instead of generic names like `Manager` or `Handler`.
- D. Short names with explanation: allow shorter names when JSDoc or comments explain the reason and context.

Agent scoring:
- A: Readability through explicit naming; tolerates longer lines and less abbreviation.
- B: Context-heavy, idiomatic TypeScript, comfortable with compact local names.
- C: Domain-driven naming, avoids generic service/object vocabulary.
- D: Documentation-supported naming, accepts comments as part of readability.

Pattern signals:
- A: Helps explicit [Facade](../patterns/gof/facade.md) and boundary APIs.
- B: Supports function-first and script-like styles.
- C: Supports domain model, domain services, clear ubiquitous language.
- D: Supports comment-guided agent workflows and more verbose generated docs.

CodeStyle output implications:
Set naming rules for functions, classes, interfaces, types, modules, variables, and review comments. The generated `CodeStyle.md` should include allowed abbreviations and discouraged generic names.

## Q5. Architecture and Wiring Style

Question ID:
typescript.architecture.wiring

Scope:
Language:TypeScript

Dimension:
Class composition vs dependency injection vs factory patterns vs central registry vs direct module imports.

User-facing scenario:
When a project has routing, setup/teardown, services, or multiple implementations, how do you prefer to wire the pieces together?

User-facing instruction:
Choose the style you would most naturally want to maintain. You can revise earlier answers at any time.

Code example:
None. This question compares architecture preferences rather than one local code snippet.

Choices:
- A. Class composition with decorators: use TypeScript decorators, class property injection, or framework-provided composition.
- B. Dependency injection: pass services, clients, and repositories explicitly into constructors or functions.
- C. Swappable implementations: define clear interfaces so different backends or algorithms can be exchanged.
- D. Central registry or module singleton: keep shared services in one configured module that other code imports.
- E. Direct module imports: keep modules self-contained with direct imports, minimal indirection.

Agent scoring:
- A: Decorator-friendly, framework-aligned composition, accepts hidden setup when names and tests are clear.
- B: Testability-first, explicit dependencies, low hidden global state.
- C: Interface-first, extension-friendly, comfortable with pattern-like structure.
- D: Convenience-first, centralized configuration, risk of hidden coupling.
- E: Simplicity-first, avoids ceremony, prefers flat module graphs.

Pattern signals:
- A: [Decorator](../patterns/gof/decorator.md), [Proxy](../patterns/gof/proxy.md)-like wrappers, framework-specific composition.
- B: [Adapter](../patterns/gof/adapter.md), [Facade](../patterns/gof/facade.md), dependency injection, test doubles.
- C: [Strategy](../patterns/gof/strategy.md), [Factory Method](../patterns/gof/factory-method.md), [Abstract Factory](../patterns/gof/abstract-factory.md), [Bridge](../patterns/gof/bridge.md).
- D: [Singleton](../patterns/gof/singleton.md)/Registry caution.
- E: Avoid unnecessary GoF structure; prefer clear functions and data structures.

CodeStyle output implications:
Set the default wiring rule: decorators, dependency injection, explicit interfaces, central registry, or direct module imports. Include caution rules for hidden state and over-abstraction.

## Q6. Folder Structure

Question ID:
typescript.folder.structure

Scope:
Language:TypeScript

Dimension:
Feature folders vs technical layers vs flat source tree vs framework/tool-driven layout.

User-facing scenario:
As the codebase grows from one file to many files, what structure should agents use by default?

User-facing instruction:
Choose the style you would most naturally want to maintain. You can revise earlier answers at any time.

Code example:

```text
# A. Feature folders
src/features/users/
src/features/billing/
src/features/reports/

# B. Technical layers
src/
  models/
  services/
  routes/
  controllers/

# C. Flat until needed
src/
  users.ts
  billing.ts
  reports.ts

# D. Tool or framework layout
src/
  <framework-convention>/
tests/
docs/
```

Choices:
- A. Feature folders: group files by product area or domain, with each area owning its local models, services, and routes.
- B. Technical layers: group files by role, such as models, services, routes, data, and tests.
- C. Flat until needed: keep files in a simple `src/` layout until nesting clearly helps.
- D. Tool or framework layout: follow the structure expected by the chosen framework, package tool, or template.

Agent scoring:
- A: Domain/feature isolation, modular ownership, good for growing products.
- B: Layered architecture, conventional separation by technical role.
- C: Minimal structure, low import complexity, refactor when pain appears.
- D: Convention-first, values compatibility with tools and ecosystem expectations.

Pattern signals:
- A: Supports bounded contexts, [Facade](../patterns/gof/facade.md) per feature, local [Adapter](../patterns/gof/adapter.md).
- B: Supports service-layer and MVC-like organization.
- C: Supports procedural/function-first code and low abstraction.
- D: Supports framework-aligned design and template-driven structure.

CodeStyle output implications:
Define where agents should create new modules and when they may introduce subfolders. Include source-vs-local-data separation when relevant.

## Q7. Testing Philosophy

Question ID:
typescript.testing.philosophy

Scope:
Language:TypeScript

Dimension:
Test-first coverage vs integration confidence vs core-logic focus vs manual/log-driven iteration.

User-facing scenario:
Tests take time to write and maintain. What level of testing should be the default for this project?

User-facing instruction:
Choose the style you would most naturally want to maintain. You can revise earlier answers at any time.

Code example:
None. The choice is about testing scope and review expectations.

Choices:
- A. Test-first and broad coverage: write tests early and cover branches, edge cases, and important failure paths.
- B. Integration-heavy: focus on endpoints, database boundaries, service flows, or full workflows.
- C. Core logic only: test custom algorithms and business rules, but avoid testing framework boilerplate.
- D. Manual and logs first: move fast, test manually, and rely on logs or user feedback until the project stabilizes.

Agent scoring:
- A: High test discipline, regression prevention, slower but safer changes.
- B: Behavior and boundary confidence, less interest in unit-testing every helper.
- C: ROI-focused testing, protects custom logic while avoiding low-value tests.
- D: Prototype speed, low automated-test expectation, higher regression risk.

Pattern signals:
- A: Supports contract tests, [Adapter](../patterns/gof/adapter.md), strict interfaces.
- B: Supports [Facade](../patterns/gof/facade.md)/API testing and integration boundaries.
- C: Supports algorithm-first and function-first testing.
- D: Avoid heavy abstractions that require extensive test scaffolding.

CodeStyle output implications:
Set minimum test requirements for generated code and future agent edits. Define whether new features need unit tests, integration tests, smoke tests, or manual verification notes.

## Q8. Comments and Docstrings

Question ID:
typescript.comments.docstrings

Scope:
Language:TypeScript

Dimension:
Self-documenting code vs why-focused comments vs strict JSDoc vs AI-facing context comments.

User-facing scenario:
AI agents can over-explain code. What comment and docstring style should this project enforce?

User-facing instruction:
Choose the style you would most naturally want to maintain. You can revise earlier answers at any time.

Code example:
None. The choice is about comment policy and documentation density.

Choices:
- A. Minimal comments: code should be clear enough that comments are rare; JSDoc is mainly for public API surfaces.
- B. Explain why: avoid comments that repeat the code, but explain business rules, constraints, and non-obvious decisions.
- C. Full JSDoc: use a consistent JSDoc style for most classes, methods, and functions, including all parameters and return types.
- D. AI context comments: allow comments as planning markers or context for future agent edits when they reduce confusion.

Agent scoring:
- A: Self-documenting preference, low comment density.
- B: Context-first comments, moderate JSDoc, strong review value.
- C: Documentation-heavy, API-reference friendly, higher maintenance cost.
- D: Agent-collaboration friendly, accepts comments as future-edit guidance.

Pattern signals:
- A: Works best with clear names, small functions, and well-named types.
- B: Supports domain-driven rules and boundary documentation.
- C: Supports public library/API style and strict interfaces.
- D: Supports agent workflows, planning/spec markers, and guided refactors.

CodeStyle output implications:
Define when agents should add comments, JSDoc, planning notes, and context markers. Also define what kinds of comments should be removed during cleanup.

## Q9. Git History and Collaboration

Question ID:
typescript.git.collaboration

Scope:
Language:TypeScript

Dimension:
Fast mainline commits vs conventional PR flow vs release branches vs linear history vs no Git preference.

User-facing scenario:
When humans and AI agents generate code together, what should the Git history and branching style look like?

User-facing instruction:
Choose the style you would most naturally want to maintain. You can revise earlier answers at any time.

Code example:
None. The choice is about collaboration workflow, not TypeScript code.

Choices:
- A. Fast mainline: commit directly to `main` or one shared `dev` branch with short descriptive messages.
- B. Conventional branches: use feature branches, pull requests, and messages like `feat:`, `fix:`, and `refactor:`.
- C. Release branches: keep `main` production-focused, use integration and release branches, and isolate hotfixes.
- D. Linear history: squash or rebase so history reads as a clean sequence without merge commits.
- E. No strong Git preference: keep Git requirements light and do not make workflow a major constraint.

Agent scoring:
- A: Speed-first collaboration, lower process overhead.
- B: Conventional, review-friendly, automation-friendly.
- C: Release-management discipline, stronger environment separation.
- D: History cleanliness, prefers curated commits.
- E: Git-light, likely needs minimal agent assumptions.

Pattern signals:
- A: Supports rapid prototyping and direct edits.
- B: Supports review checklists, CI, and structured agent commits.
- C: Supports release management specs and deployment gates.
- D: Supports polished patch sets and careful refactors.
- E: Avoid over-specifying Git behavior in generated style files.

CodeStyle output implications:
Set commit-message, branch, PR, and history expectations for future agent work. If E is chosen, keep Git guidance minimal.

## Q10. Dependencies and Environments

Question ID:
typescript.dependencies.environments

Scope:
Language:TypeScript

Dimension:
Standard npm vs pnpm/yarn vs lockfile discipline vs newer fast tooling.

User-facing scenario:
TypeScript/JavaScript dependency management shapes the whole project. How should environments and third-party libraries be managed?

User-facing instruction:
Choose the style you would most naturally want to maintain. You can revise earlier answers at any time.

Code example:

```text
A. package.json + node_modules + npm
B. package.json + pnpm-lock.yaml or yarn.lock
C. pnpm-workspace.yaml or monorepo with strict lockfile
D. Minimal dependencies + copybara or esm.sh CDN-style imports
```

Choices:
- A. Standard npm: keep setup simple with `package.json` and built-in node_modules.
- B. pnpm or yarn: use a faster, more efficient package manager with workspace support when needed.
- C. Strict lockfile with monorepo: use pnpm workspaces or a similar setup for strict reproducibility.
- D. Minimal dependencies: prefer standard library, minimal npm packages, and CDN-style imports where practical.

Agent scoring:
- A: Minimal tooling, broad compatibility, simple setup.
- B: Speed-first, modern tooling preference, workspace support.
- C: Reproducibility-first, structured project metadata, monorepo discipline.
- D: Dependency-minimalist, avoids supply-chain risk, prefers built-in APIs.

Pattern signals:
- A: Supports lightweight scripts and simple packages.
- B: Supports modern agent workflows and fast iteration.
- C: Supports package/library style and CI reproducibility.
- D: Supports algorithm-first projects and minimal toolchain.

CodeStyle output implications:
Set dependency policy, environment files, install commands, and whether agents may add new libraries. Include the preferred source of truth for dependencies.
