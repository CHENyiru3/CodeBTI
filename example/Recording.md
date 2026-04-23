# CodeBTI Session Record

Date:
2026-04-23

Project slug:
example

Language target:
Python

Interview status:
Complete

Current step:
CodeStyle.md generated

Next question:
None

## Project Summary

Python based calculator with GUI to deal with math calculation.

Source: required opening prompt, "What kind of project do you want to build? Please describe shortly."

## Question Card Snapshots

### Opening. Project Summary

Question kind:
Opening

Source:
Required opening prompt

Full question:
What kind of project do you want to build? Please describe shortly.

### Q1. General Purpose and Paradigm

Question kind:
Fixed

Source:
/Users/eric_yiru/.codex/skills/codebti/python/questions/fixed-python.md

Dimension:
Object-centered vs function-first vs data-first vs flat procedural organization.

User-facing scenario:
When starting a fresh Python project, how do you naturally organize the core logic? Here is the same small task, greeting a user with their age, written in four different styles.

User-facing instruction:
Choose the style you would most naturally want to maintain. You can revise earlier answers at any time.

Code example:
```python
# A. Object-centered
class User:
    def __init__(self, name: str, birth_year: int):
        self.name = name
        self.birth_year = birth_year

    def age(self, current_year: int) -> int:
        return current_year - self.birth_year

    def greeting(self, current_year: int) -> str:
        return f"Hi {self.name}, you are {self.age(current_year)}."


# B. Function-first
def calculate_age(birth_year: int, current_year: int) -> int:
    return current_year - birth_year


def greeting(name: str, age: int) -> str:
    return f"Hi {name}, you are {age}."


# C. Data-first
from dataclasses import dataclass


@dataclass(frozen=True)
class UserData:
    name: str
    birth_year: int


def greet_user(user: UserData, current_year: int) -> str:
    age = current_year - user.birth_year
    return f"Hi {user.name}, you are {age}."


# D. Flat procedural
CURRENT_YEAR = 2026


def greet(user_payload: dict) -> str:
    age = CURRENT_YEAR - user_payload["birth_year"]
    return f"Hi {user_payload['name']}, you are {age}."
```

Choices:
- A. Object-centered: keep state and behavior together in domain objects.
- B. Function-first: use small functions that transform explicit inputs into outputs.
- C. Data-first: define the data shape first, then write lightweight functions around it.
- D. Flat procedural: write a direct flow with simple helpers and module-level constants when useful.

Required scored snapshot blocks:

### Q2. Defensive Coding and Type Boundaries

Question kind:
Fixed

Source:
/Users/eric_yiru/.codex/skills/codebti/python/questions/fixed-python.md

Dimension:
Strict static typing vs boundary typing vs runtime validation vs dynamic duck typing.

User-facing scenario:
Python lets you choose how strongly the code checks its own assumptions. For a function that updates a user's age, how strict should the project be?

User-facing instruction:
Choose the style you would most naturally want to maintain. You can revise earlier answers at any time.

Code example:
```python
# A. Strict checks
def update_user_age(user_id: int, new_age: int) -> bool:
    if not isinstance(new_age, int):
        raise TypeError("new_age must be an integer")
    if new_age <= 0:
        raise ValueError("new_age must be positive")

    user: dict[str, object] = db_get(user_id)
    user["age"] = new_age
    db_save(user)
    return True


# B. Boundary typing
def update_user_age(user_id: int, new_age: int) -> bool:
    user = db_get(user_id)
    if new_age <= 0:
        return False

    user["age"] = new_age
    db_save(user)
    return True


# C. Runtime validation
from pydantic import BaseModel, Field


class AgeUpdate(BaseModel):
    user_id: int
    new_age: int = Field(gt=0)


def update_user_age(raw_input: dict) -> bool:
    payload = AgeUpdate(**raw_input)
    user = db_get(payload.user_id)
    user["age"] = payload.new_age
    db_save(user)
    return True


# D. Dynamic Python
def update_user_age(user_id, new_age):
    user = db_get(user_id)
    user["age"] = int(new_age)
    db_save(user)
    return True
```

Choices:
- A. Strict checks: use strong type hints and explicit validation in important functions.
- B. Boundary typing: type public functions and module boundaries, but keep internal code flexible.
- C. Runtime validation: use validation models to clean and check incoming data.
- D. Dynamic Python: keep type hints light and trust callers unless a bug proves otherwise.

Required scored snapshot blocks:

### Q3. Error Handling and Recovery

Question kind:
Fixed

Source:
/Users/eric_yiru/.codex/skills/codebti/python/questions/fixed-python.md

Dimension:
Fail-fast exceptions vs safe fallback vs explicit result objects vs batch quarantine.

User-facing scenario:
The project receives transaction payloads from a JSON API. Sometimes `amount` is missing or is a value like `"N/A"`. How should the code handle that kind of bad input?

User-facing instruction:
Choose the style you would most naturally want to maintain. You can revise earlier answers at any time.

Code example:
```python
# A. Fail fast
class MalformedTransactionError(ValueError):
    pass


def calculate_total(tx: dict) -> float:
    if "amount" not in tx:
        raise MalformedTransactionError("Transaction is missing amount")
    if not isinstance(tx["amount"], (int, float)):
        raise MalformedTransactionError("Transaction amount must be numeric")
    return tx["amount"] * 1.2


# B. Safe fallback
def calculate_total(tx: dict) -> float:
    try:
        return float(tx.get("amount", 0)) * 1.2
    except (TypeError, ValueError):
        return 0.0


# C. Explicit result
def calculate_total(tx: dict) -> dict:
    amount = tx.get("amount")
    if not isinstance(amount, (int, float)):
        return {"ok": False, "value": None, "error": "Invalid amount"}
    return {"ok": True, "value": amount * 1.2, "error": None}


# D. Log and continue
import logging


def process_batch(transactions: list[dict]) -> list[float]:
    totals = []
    for tx in transactions:
        try:
            totals.append(float(tx["amount"]) * 1.2)
        except (KeyError, TypeError, ValueError) as exc:
            logging.warning("Skipped transaction %s: %s", tx.get("id"), exc)
    return totals
```

Choices:
- A. Fail fast: raise a clear error as soon as invalid data appears.
- B. Safe fallback: return a default value and keep the main flow moving.
- C. Explicit result: return a structured success or failure value instead of raising for expected problems.
- D. Log and continue: record the failure, skip the bad item, and keep processing the rest.

Required scored snapshot blocks:

### Q4. Naming and Readability

Question kind:
Fixed

Source:
/Users/eric_yiru/.codex/skills/codebti/python/questions/fixed-python.md

Dimension:
Explicit names vs concise idioms vs domain vocabulary vs comment-supported naming.

User-facing scenario:
Names shape how a codebase feels to read. How should variables, functions, and classes be named in this project?

User-facing instruction:
Choose the style you would most naturally want to maintain. You can revise earlier answers at any time.

Code example:
None. The choice is about naming style and review expectations.

Choices:
- A. Explicit names: prefer names like `calculate_total_revenue_for_active_users`, even when they are longer.
- B. Concise idioms: allow short common names like `idx`, `req`, `df`, or `cfg` when context is clear.
- C. Domain language: use the terms from the product, business, math, or science domain instead of generic names like `manager` or `handler`.
- D. Short names with explanation: allow shorter names when docstrings or comments explain the reason and context.

Required scored snapshot blocks:

### Q5. Architecture and Wiring Style

Question kind:
Fixed

Source:
/Users/eric_yiru/.codex/skills/codebti/python/questions/fixed-python.md

Dimension:
Python language tools vs dependency injection vs swappable patterns vs central registry vs algorithm-first code.

User-facing scenario:
When a project has routing, setup/teardown, services, or multiple implementations, how do you prefer to wire the pieces together?

User-facing instruction:
Choose the style you would most naturally want to maintain. You can revise earlier answers at any time.

Code example:
None. This question compares architecture preferences rather than one local code snippet.

Choices:
- A. Python tools: use decorators, context managers, and small wrappers for repeated setup or cleanup.
- B. Passed-in dependencies: pass services, clients, and repositories directly into functions or classes.
- C. Swappable implementations: define clear interfaces so different backends or algorithms can be exchanged.
- D. Central registry: keep shared services in one configured module or object that other code imports.
- E. Algorithm-first: keep abstractions thin and focus on data structures, performance, and direct APIs.

Required scored snapshot blocks:

### Q6. Folder Structure

Question kind:
Fixed

Source:
/Users/eric_yiru/.codex/skills/codebti/python/questions/fixed-python.md

Dimension:
Feature folders vs technical layers vs flat source tree vs framework/tool-driven layout.

User-facing scenario:
As the codebase grows from one file to many files, what structure should agents use by default?

User-facing instruction:
Choose the style you would most naturally want to maintain. You can revise earlier answers at any time.

Code example:
```text
# A. Feature folders
src/users/
src/billing/
src/reports/

# B. Technical layers
src/models/
src/services/
src/routes/

# C. Flat until needed
src/
  users.py
  billing.py
  reports.py

# D. Tool or framework layout
src/<framework-or-template-convention>/
tests/
docs/
```

Choices:
- A. Feature folders: group files by product area or domain, with each area owning its local models, services, and routes.
- B. Technical layers: group files by role, such as models, services, routes, data, and tests.
- C. Flat until needed: keep files in a simple `src/` layout until nesting clearly helps.
- D. Tool or framework layout: follow the structure expected by the chosen framework, package tool, or template.

Required scored snapshot blocks:

### Q7. Testing Philosophy

Question kind:
Fixed

Source:
/Users/eric_yiru/.codex/skills/codebti/python/questions/fixed-python.md

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
- B. Integration-heavy: focus on endpoints, database boundaries, CLI flows, or full workflows.
- C. Core logic only: test custom algorithms and business rules, but avoid testing framework boilerplate.
- D. Manual and logs first: move fast, test manually, and rely on logs or user feedback until the project stabilizes.

Required scored snapshot blocks:

### Q8. Comments and Docstrings

Question kind:
Fixed

Source:
/Users/eric_yiru/.codex/skills/codebti/python/questions/fixed-python.md

Dimension:
Self-documenting code vs why-focused comments vs strict docstrings vs AI-facing context comments.

User-facing scenario:
AI agents can over-explain code. What comment and docstring style should this project enforce?

User-facing instruction:
Choose the style you would most naturally want to maintain. You can revise earlier answers at any time.

Code example:
None. The choice is about comment policy and documentation density.

Choices:
- A. Minimal comments: code should be clear enough that comments are rare; docstrings are mainly for public APIs.
- B. Explain why: avoid comments that repeat the code, but explain business rules, constraints, and non-obvious decisions.
- C. Full docstrings: use a consistent docstring style for most classes, methods, and functions.
- D. AI context comments: allow comments as planning markers or context for future agent edits when they reduce confusion.

Required scored snapshot blocks:

### Q9. Git History and Collaboration

Question kind:
Fixed

Source:
/Users/eric_yiru/.codex/skills/codebti/python/questions/fixed-python.md

Dimension:
Fast mainline commits vs conventional PR flow vs release branches vs linear history vs no Git preference.

User-facing scenario:
When humans and AI agents generate code together, what should the Git history and branching style look like?

User-facing instruction:
Choose the style you would most naturally want to maintain. You can revise earlier answers at any time.

Code example:
None. The choice is about collaboration workflow, not Python code.

Choices:
- A. Fast mainline: commit directly to `main` or one shared `dev` branch with short descriptive messages.
- B. Conventional branches: use feature branches, pull requests, and messages like `feat:`, `fix:`, and `refactor:`.
- C. Release branches: keep `main` production-focused, use integration and release branches, and isolate hotfixes.
- D. Linear history: squash or rebase so history reads as a clean sequence without merge commits.
- E. No strong Git preference: keep Git requirements light and do not make workflow a major constraint.

Required scored snapshot blocks:

### Q10. Dependencies and Environments

Question kind:
Fixed

Source:
/Users/eric_yiru/.codex/skills/codebti/python/questions/fixed-python.md

Dimension:
Standard pip/venv vs conda environments vs lockfile package managers vs newer Rust-based tooling.

User-facing scenario:
Python dependency management can shape the whole project. How should environments and third-party libraries be managed?

User-facing instruction:
Choose the style you would most naturally want to maintain. You can revise earlier answers at any time.

Code example:
```text
A. requirements.txt + venv
B. environment.yml + conda/miniconda
C. pyproject.toml + poetry.lock or Pipfile.lock
D. pyproject.toml / uv.lock / inline script metadata
```

Choices:
- A. Standard `pip` and `venv`: keep setup simple with `requirements.txt` and built-in virtual environments.
- B. Conda-style environment: use `conda` or `miniconda` when data science packages or native dependencies matter.
- C. Lockfile package manager: use Poetry or Pipenv for structured config and reproducible lock files.
- D. Newer fast tooling: use tools like `uv` or `rye` for fast resolution and modern Python project workflows.

Required scored snapshot blocks:

### A1. GUI Boundary and Calculator Logic

Question kind:
Adaptive

Source:
Generated adaptive question

Dimension:
Boundaries around outside tools and UI framework coupling.

User-facing scenario:
For a GUI calculator, the button click code can either directly perform calculations or call a small calculator object that keeps the math separate from the GUI toolkit. Which shape should future agents prefer?

User-facing instruction:
Choose the style you would most naturally want to maintain. You can revise earlier answers at any time.

Code example:
```python
# A. Direct GUI logic
def on_equals_clicked():
    display.setText(str(eval(display.text())))


# B. Small calculator object behind the UI
class Calculator:
    def evaluate(self, expression):
        return parse_and_calculate(expression)


def on_equals_clicked():
    result = calculator.evaluate(display.text())
    display.setText(result.text)


# C. UI adapter around the toolkit
class CalculatorView:
    def read_expression(self):
        return self.display.text()

    def show_result(self, result):
        self.display.setText(result.text)
```

Choices:
- A. Direct GUI logic: keep button handlers simple and calculate directly when the code stays readable.
- B. Small calculator object: keep math behavior in a calculator object, with GUI handlers only passing input and showing output.
- C. UI adapter: wrap GUI toolkit details behind a small view class so calculator code does not know toolkit methods.

### A2. Adding New Calculator Operations

Question kind:
Adaptive

Source:
Generated adaptive question

Dimension:
Growth and extension for new operations, algorithms, and rule types.

User-facing scenario:
If the calculator later adds operations like square root, power, percentage, memory buttons, or scientific functions, how should future agents extend the code?

User-facing instruction:
Choose the style you would most naturally want to maintain. You can revise earlier answers at any time.

Code example:
```python
# A. Simple branching
def apply_operator(operator, left, right):
    if operator == "+":
        return left + right
    if operator == "-":
        return left - right
    if operator == "^":
        return left ** right
    return None


# B. Named operation methods
class Calculator:
    def add(self, left, right):
        return left + right

    def subtract(self, left, right):
        return left - right

    def power(self, left, right):
        return left ** right


# C. Operation registry
OPERATIONS = {
    "+": lambda left, right: left + right,
    "-": lambda left, right: left - right,
    "^": lambda left, right: left ** right,
}
```

Choices:
- A. Simple branching: use direct `if`/`elif` logic until it becomes hard to read.
- B. Named operation methods: keep each operation as a clear method on the calculator object.
- C. Operation registry: keep operations in a mapping so new operators can be added in one place.

### A3. Invalid User Input

Question kind:
Adaptive

Source:
Generated adaptive question

Dimension:
Data trust, validation, and user-facing recovery.

User-facing scenario:
A GUI user can enter expressions such as `1 / 0`, `2 +`, `sqrt(-1)`, or pasted text like `hello`. Where should invalid input be handled?

User-facing instruction:
Choose the style you would most naturally want to maintain. You can revise earlier answers at any time.

Code example:
```python
# A. Validate before evaluation
def on_equals_clicked():
    expression = display.text()
    if not looks_valid(expression):
        display.setText("Error")
        return
    display.setText(calculator.evaluate(expression).text)


# B. Calculator returns explicit result
def on_equals_clicked():
    result = calculator.evaluate(display.text())
    display.setText(result.text if result.ok else "Error")


# C. Let exceptions surface inside calculator, then catch at UI
def on_equals_clicked():
    try:
        display.setText(calculator.evaluate(display.text()))
    except Exception:
        display.setText("Error")
```

Choices:
- A. Validate before evaluation: screen obvious bad input in the GUI handler before calling calculator logic.
- B. Calculator returns explicit result: let the calculator handle validity and return a success/failure result for the UI to display.
- C. Catch exceptions at UI: let calculator internals raise naturally, then convert failures to `Error` at the GUI boundary.

### A4. Calculator State and History

Question kind:
Adaptive

Source:
Generated adaptive question

Dimension:
State and history for display value, memory buttons, undo, and recent calculations.

User-facing scenario:
If the calculator grows beyond one-shot expression evaluation, it may need state for the display, memory value, last result, or recent history. How should future agents handle that state?

User-facing instruction:
Choose the style you would most naturally want to maintain. You can revise earlier answers at any time.

Code example:
```python
# A. Local mutable fields on Calculator
class Calculator:
    def __init__(self):
        self.display = ""
        self.memory = None


# B. Explicit state object
class CalculatorState:
    def __init__(self, display="", memory=None, history=None):
        self.display = display
        self.memory = memory
        self.history = history or []


class Calculator:
    def __init__(self, state):
        self.state = state


# C. Snapshot history
class Calculator:
    def __init__(self):
        self.snapshots = []

    def save_snapshot(self):
        self.snapshots.append({"display": self.display, "memory": self.memory})
```

Choices:
- A. Local mutable fields: keep display, memory, and recent values directly on the calculator object.
- B. Explicit state object: keep state in a separate object so it is easier to inspect, test, or replace.
- C. Snapshot history: record state changes as snapshots when undo/history becomes important.

### A5. Where To Stop Adding Structure

Question kind:
Adaptive

Source:
Generated adaptive question

Dimension:
Ceremony budget for a small object-centered, algorithm-first GUI calculator.

User-facing scenario:
Future agents may be tempted to add extra classes for commands, controllers, factories, validators, and services. For this project, where should they stop adding structure?

User-facing instruction:
Choose the style you would most naturally want to maintain. You can revise earlier answers at any time.

Code example:
```python
# A. Stop at small helpers
class Calculator:
    def evaluate(self, expression):
        tokens = tokenize(expression)
        return evaluate_tokens(tokens)


# B. Allow boundary objects only
class Calculator:
    def evaluate(self, expression):
        ...


class CalculatorWindow:
    def on_equals_clicked(self):
        result = self.calculator.evaluate(self.display.text())
        self.display.setText(result.text)


# C. Allow pattern-like structure for real variation
class OperationRegistry:
    def register(self, symbol, operation):
        self.operations[symbol] = operation
```

Choices:
- A. Stop at small helpers: keep one calculator class plus helper functions unless the file becomes hard to read.
- B. Allow boundary objects only: use a calculator object and a GUI/window object, but avoid extra layers by default.
- C. Allow pattern-like structure for real variation: add registries, command objects, or factories only when multiple real variants exist.

## Answer Log

| Step | Question kind | Question focus | User answer | User note | Feedback given | Hidden inference note | Changed from | Recorded at |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Opening | Project summary | Project intent | Python based calculator with GUI to deal with math calculation. | GUI calculator for math calculations. | Recorded as a Python GUI calculator project; future questions should distinguish UI wiring from calculator logic. | Not scored | None | 2026-04-23 |
| Q1 | Fixed | General purpose and paradigm | A. Object-centered | Prefers keeping state and behavior together in domain objects. | That points the calculator toward a small set of objects that own behavior, which fits a GUI app if the calculator state and UI wiring stay cleanly separated. | Class-friendly, encapsulation-first, comfortable with objects owning behavior; possible Strategy or State later if calculator operations or UI modes grow. | None | 2026-04-23 |
| Q2 | Fixed | Defensive coding and type boundaries | D. Dynamic Python | "Duck walk style"; prefers light type hints and trusting callers unless bugs prove otherwise. | That makes the style object-centered but low ceremony: useful for a small GUI calculator where readable behavior matters more than type-heavy infrastructure. | Dynamic, low ceremony, duck-typing friendly; avoid heavy interface patterns unless project risk demands them. | None | 2026-04-23 |
| Q3 | Fixed | Error handling and recovery | C. Explicit result | "Fail is fail"; wants simple explicit failure without overthinking for now. | That points to simple, visible failure handling: operations can return a clear success or failure value without turning expected calculator mistakes into a large exception system. | Explicit control flow, result-object style, good for recoverable user-input/business errors; avoid broad exception hierarchy unless failures become exceptional. | None | 2026-04-23 |
| Q4 | Fixed | Naming and readability | C. Domain language | "C is fine for now." | Domain naming fits a calculator well: names like expression, operand, operator, result, and display are more useful than vague controller names. | Domain-driven naming; avoid generic service/object vocabulary and prefer calculator/math vocabulary. | None | 2026-04-23 |
| Q5 | Fixed | Architecture and wiring style | E. Algorithm-first | Suitable for the project. | Algorithm-first reinforces that the calculator should keep abstractions thin and make the expression/evaluation logic easy to inspect. | Performance/directness first, avoids architecture ceremony; prefer direct APIs and clear data structures over patterns unless a real extension point appears. | None | 2026-04-23 |
| Q6 | Fixed | Folder structure | C. Flat until needed | Project is not heavy; simple layout is enough. | That keeps the calculator project intentionally compact: one simple source tree until there is real pressure to split modules. | Minimal structure, low import complexity; refactor into subfolders only when pain appears. | None | 2026-04-23 |
| Q7 | Fixed | Testing philosophy | C. Core logic only | Wants tests for custom algorithms and business rules, not GUI/framework boilerplate. | That matches the project shape: tests should protect expression parsing and calculation behavior, while GUI widget plumbing can mostly stay manual unless it becomes fragile. | ROI-focused testing; protect custom calculation logic and avoid low-value framework boilerplate tests. | None | 2026-04-23 |
| Q8 | Fixed | Comments and docstrings | A. Minimal comments | "Save my token"; wants low comment density. | Minimal comments fit the low-ceremony style: clear names and compact methods should carry most of the meaning, with comments only where the math or UI behavior is not obvious. | Self-documenting preference, low comment density; public APIs may get docstrings, but most code should avoid redundant comments. | None | 2026-04-23 |
| Q9 | Fixed | Git history and collaboration | A. Fast mainline | Prefers direct commits to main or shared dev with short descriptive messages. | Fast mainline keeps collaboration lightweight, which matches the project's small scope and low-process preference. | Speed-first collaboration, lower process overhead; supports rapid prototyping and direct edits. | None | 2026-04-23 |
| Q10 | Fixed | Dependencies and environments | D. Newer fast tooling | Loves `uv`; prefers modern fast dependency tooling. | That sets the project up for fast iteration with `uv`, which fits the lightweight calculator direction while still keeping dependencies reproducible. | Modern tooling preference, speed-first dependency management; use `pyproject.toml` and `uv.lock` or related uv workflow as dependency source of truth. | None | 2026-04-23 |
| A1 | Adaptive | GUI boundary and calculator logic | B. Small calculator object | Prefers math behavior in a calculator object, with GUI handlers only passing input and showing output. | That gives the project a practical boundary: the GUI stays thin, and the calculator object owns expression behavior without adding a full adapter layer. | Encourages a small Facade-like calculator boundary for GUI use, but avoid wrapping every GUI toolkit detail unless needed. | None | 2026-04-23 |
| A2 | Adaptive | Growth and extension for new operations | C. Operation registry | Likes a mapping for adding operators in one place. | A small operation registry fits the algorithm-first direction if it stays simple: one place to see available operators without building a plugin system too early. | Encourages a lightweight Strategy/registry for calculator operations; avoid full plugin or class hierarchy unless operation metadata grows. | None | 2026-04-23 |
| A3 | Adaptive | Invalid user input handling | B. Calculator returns explicit result | Calculator should handle validity and return success/failure for the UI to display. | That is consistent with your earlier explicit-result answer: the calculator object becomes the single place that decides whether an expression is valid, and the UI just displays the outcome. | Strong explicit-result signal; keep validation in calculator/evaluation boundary and return simple result objects for user-facing failures. | None | 2026-04-23 |
| A4 | Adaptive | Calculator state and history | C. Snapshot history, based on A when simple | Prefers snapshot history when needed, but ordinary state can live as local mutable fields on Calculator. | That gives a clear priority: keep ordinary calculator state simple on the object, but introduce snapshot history when undo or recent-calculation behavior matters. | Prefer local mutable calculator state by default; introduce snapshots for undo/history rather than a separate state object unless state complexity grows. | None | 2026-04-23 |
| A5 | Adaptive | Ceremony budget | A. Stop at small helpers | Keep one calculator class plus helper functions unless the file becomes hard to read. | That locks in the ceremony budget: keep the project compact, with one calculator object and small helpers unless the code genuinely becomes hard to read. | Strong low-ceremony signal; avoid command/controller/factory/service layers until there is real variation or readability pressure. | None | 2026-04-23 |

## Fixed Question Answers

| Question | Final answer | User note | Changed from |
| --- | --- | --- | --- |
| Q1 | A. Object-centered | Prefers keeping state and behavior together in domain objects. | None |
| Q2 | D. Dynamic Python | "Duck walk style"; prefers light type hints and trusting callers unless bugs prove otherwise. | None |
| Q3 | C. Explicit result | "Fail is fail"; wants simple explicit failure without overthinking for now. | None |
| Q4 | C. Domain language | "C is fine for now." | None |
| Q5 | E. Algorithm-first | Suitable for the project. | None |
| Q6 | C. Flat until needed | Project is not heavy; simple layout is enough. | None |
| Q7 | C. Core logic only | Wants tests for custom algorithms and business rules, not GUI/framework boilerplate. | None |
| Q8 | A. Minimal comments | "Save my token"; wants low comment density. | None |
| Q9 | A. Fast mainline | Prefers direct commits to main or shared dev with short descriptive messages. | None |
| Q10 | D. Newer fast tooling | Loves `uv`; prefers modern fast dependency tooling. | None |

## Adaptive Question Answers

Record exactly 5 adaptive answers.

| Question | Direction | Final answer | User note | Why asked |
| --- | --- | --- | --- | --- |
| A1 | GUI boundary and calculator logic | B. Small calculator object | Prefers math behavior in a calculator object, with GUI handlers only passing input and showing output. | Clarify how strongly to separate GUI toolkit event handlers from calculator behavior after object-centered + algorithm-first answers. |
| A2 | Growth and extension for new operations | C. Operation registry | Likes a mapping for adding operators in one place. | Clarify whether adding operations should use branching, calculator methods, or a registry after choosing object-centered plus algorithm-first. |
| A3 | Invalid user input handling | B. Calculator returns explicit result | Calculator should handle validity and return success/failure for the UI to display. | Clarify where invalid GUI/user input should be handled after choosing explicit results. |
| A4 | Calculator state and history | C. Snapshot history, based on A when simple | Prefers snapshot history when needed, but ordinary state can live as local mutable fields on Calculator. | Clarify state handling for display, memory, undo, and calculation history. |
| A5 | Ceremony budget | A. Stop at small helpers | Keep one calculator class plus helper functions unless the file becomes hard to read. | Resolve tension between object-centered style, operation registry interest, and algorithm-first/minimal-structure preferences. |

## Feedback Summary

- Opening feedback: Recorded as a Python GUI calculator project; future questions should distinguish UI wiring from calculator logic.
- Q1 feedback: That points the calculator toward a small set of objects that own behavior, which fits a GUI app if the calculator state and UI wiring stay cleanly separated.
- Q2 feedback: That makes the style object-centered but low ceremony: useful for a small GUI calculator where readable behavior matters more than type-heavy infrastructure.
- Q3 feedback: That points to simple, visible failure handling: operations can return a clear success or failure value without turning expected calculator mistakes into a large exception system.
- Q4 feedback: Domain naming fits a calculator well: names like expression, operand, operator, result, and display are more useful than vague controller names.
- Q5 feedback: Algorithm-first reinforces that the calculator should keep abstractions thin and make the expression/evaluation logic easy to inspect.
- Q6 feedback: That keeps the calculator project intentionally compact: one simple source tree until there is real pressure to split modules.
- Q7 feedback: That matches the project shape: tests should protect expression parsing and calculation behavior, while GUI widget plumbing can mostly stay manual unless it becomes fragile.
- Q8 feedback: Minimal comments fit the low-ceremony style: clear names and compact methods should carry most of the meaning, with comments only where the math or UI behavior is not obvious.
- Q9 feedback: Fast mainline keeps collaboration lightweight, which matches the project's small scope and low-process preference.
- Q10 feedback: That sets the project up for fast iteration with `uv`, which fits the lightweight calculator direction while still keeping dependencies reproducible.
- A1 feedback: That gives the project a practical boundary: the GUI stays thin, and the calculator object owns expression behavior without adding a full adapter layer.
- A2 feedback: A small operation registry fits the algorithm-first direction if it stays simple: one place to see available operators without building a plugin system too early.
- A3 feedback: That is consistent with your earlier explicit-result answer: the calculator object becomes the single place that decides whether an expression is valid, and the UI just displays the outcome.
- A4 feedback: That gives a clear priority: keep ordinary calculator state simple on the object, but introduce snapshot history when undo or recent-calculation behavior matters.
- A5 feedback: That locks in the ceremony budget: keep the project compact, with one calculator object and small helpers unless the code genuinely becomes hard to read.

## Hidden Scoring Notes

Style-axis signals:

- Project target: Python GUI calculator; likely needs a clean split between calculation engine and GUI event wiring, but this remains unscored until fixed/adaptive answers are collected.
- Q1: Object-centered; prefer classes owning calculator state/behavior, with care not to over-entangle GUI widgets with domain logic.
- Q2: Dynamic Python; prefer light type hints, duck-typing-friendly internals, and avoid broad runtime validation frameworks unless a boundary needs them.
- Q3: Explicit result; expected calculator/user-input failures should return clear outcome data rather than raise, silently default, or require a logging pipeline.
- Q4: Domain language; use math/calculator/UI terms instead of generic names such as manager, handler, processor, or service unless they are truly clearer.
- Q5: Algorithm-first; avoid architecture ceremony and prefer direct expression/evaluation APIs, clear data structures, and only minimal object structure.
- Q6: Flat until needed; start with a compact source tree and introduce folders only after module responsibilities become crowded.
- Q7: Core logic only; add tests for calculation algorithms, parsing, precedence, invalid input, and state transitions, but do not require GUI boilerplate tests by default.
- Q8: Minimal comments; prefer self-documenting names and short methods, only adding comments/docstrings for non-obvious public APIs, math decisions, or GUI quirks.
- Q9: Fast mainline; use direct edits or a shared dev branch with short descriptive commits, avoiding heavy PR/release workflow requirements by default.
- Q10: Newer fast tooling; prefer `uv`, `pyproject.toml`, and `uv.lock` as the dependency/environment workflow.
- A1: Small calculator object behind the UI; keep GUI handlers thin and place expression behavior in a calculator class.
- A2: Operation registry; allow a lightweight mapping for operations as a simple Strategy-like structure, but avoid a heavy plugin framework by default.
- A3: Invalid input handled by calculator result objects; GUI should not duplicate validation beyond simple display concerns.
- A4: State starts as local mutable fields on Calculator; add snapshot history when undo/recent-history behavior is implemented.
- A5: Stop at small helpers; do not add command/controller/factory/service layers unless there is real readability pressure or multiple concrete variants.

Pattern signals:

- Encouraged: Facade-like `Calculator.evaluate()` boundary; Strategy-like operation registry as a callable mapping.
- Allowed with caution: Memento-style snapshots for undo/history after that feature exists.
- Avoid by default: Command objects for simple button actions; Singleton/global registries for mutable calculator state; factories/plugin frameworks before real variation exists.

Pattern and resource references:

| Reference | Local path or URL | Why it matters |
| --- | --- | --- |
| Facade | /Users/eric_yiru/.codex/skills/codebti/python/patterns/python/facade.md | Encouraged as a thin `Calculator.evaluate()` boundary between GUI code and calculation internals. |
| Strategy | /Users/eric_yiru/.codex/skills/codebti/python/patterns/python/strategy.md | Encouraged as a lightweight operation registry or callable mapping for calculator operations. |
| Memento | /Users/eric_yiru/.codex/skills/codebti/python/patterns/python/memento.md | Allowed with caution for undo/history snapshots once that behavior exists. |
| Command | /Users/eric_yiru/.codex/skills/codebti/python/patterns/python/command.md | Avoid by default for basic GUI button actions unless replay, queueing, or undo metadata is needed. |
| Singleton | /Users/eric_yiru/.codex/skills/codebti/python/patterns/python/singleton.md | Avoid by default because mutable calculator state should not be hidden behind process-global access. |

Contradictions or weak signals:

- Object-centered and algorithm-first are balanced by using one small `Calculator` object while keeping helper functions and operation data direct.
- Operation registry is allowed, but A5 limits it to a simple mapping rather than a plugin framework.

Evidence reviewed before generation:

- `Question Card Snapshots`
- `Answer Log`
- Fixed and adaptive answer tables
- Pattern and resource references

## CodeBTI Result

Profile name:
Algorithm-First Minimalist with Object-Centered Boundary traits

Profile taxonomy reference:
[python-profile-taxonomy.md](/Users/eric_yiru/.codex/skills/codebti/python/profiles/python-profile-taxonomy.md)

Short explanation:
The strongest signal is algorithm-first, low-ceremony Python: keep abstractions thin, test core calculation behavior, use a flat layout, and avoid unnecessary layers. Object-centered answers add one practical boundary: a small `Calculator` object should own expression behavior while GUI handlers stay thin.

## Generated Outputs

- `CodeStyle.md`: Generated at [CodeStyle.md](/Users/eric_yiru/Desktop/Github/CodeBTI/example/CodeStyle.md). Used [CodeStyle.template.md](/Users/eric_yiru/.codex/skills/codebti/python/templates/CodeStyle.template.md).
- `SKILL.md`: Not generated; not requested.
- `SPEC.md`: Not generated; not requested.

## Unresolved Assumptions

- GUI framework, calculator complexity, packaging target, and testing scope are not known yet.
