# CodeStyle

Project:
Python GUI calculator for math calculations

Generated from session record:
[Recording.md](Recording.md)

Primary CodeBTI profile:
Algorithm-First Minimalist

Secondary traits:
Object-centered low-ceremony GUI boundary, pragmatic script-builder structure

## Project Intent

Build a compact Python calculator with a GUI. The code should make calculation behavior easy to inspect, keep GUI event handlers thin, and avoid architecture that is larger than the project.

## Default Code Shape

Preferred organization:
Use a small `Calculator` object as the main behavior boundary. Keep expression parsing, operation dispatch, result creation, and calculator state close to that object. GUI code should pass display text into the calculator and render the returned result.

Module and folder rules:
Start flat until needed. A simple shape such as `src/calculator.py`, `src/gui.py`, and focused tests is enough. Add folders only when files become crowded or separate domains appear.

When to add abstraction:
Add structure only when it removes real complexity. A small operation registry is allowed for operators and scientific functions. Snapshot history is allowed when undo or recent-history behavior exists.

When to keep code direct:
Keep helper functions, direct data structures, and straightforward control flow when the logic is readable. Do not introduce command, controller, factory, service, or plugin layers by default.

## Python Style Rules

Naming:
Use calculator and math vocabulary: `expression`, `operator`, `operand`, `operation`, `result`, `display`, `memory`, `history`, and `snapshot`. Avoid vague names such as `manager`, `handler`, `processor`, and `service` unless they are clearly the best domain term.

Typing:
Keep type hints light. Public or important methods may be typed when it improves readability, but internal code can stay dynamic and duck-typing friendly.

Data modeling:
Avoid heavy validation models. Use simple objects or dictionaries for small internal records. If result data becomes repeated, prefer a tiny result object with fields like `ok`, `text`, `value`, and `error`.

Error handling:
Expected user-input failures should return explicit result values from `Calculator.evaluate()`. The GUI should display the result or a simple error state. Avoid silent defaults, broad exception systems, and duplicate validation in the UI.

State management:
Keep ordinary mutable state directly on `Calculator` while the project is small. Add snapshot history only when undo, restore, or recent-calculation behavior is implemented.

Dependency management:
Use `uv` as the preferred workflow. Prefer `pyproject.toml` and `uv.lock` as the dependency source of truth. Add dependencies only when they clearly improve GUI delivery, parsing correctness, or maintainability.

Comments and docstrings:
Use minimal comments. Clear names and short functions should carry most meaning. Add comments only for non-obvious math rules, parser decisions, GUI toolkit quirks, or public APIs that need explanation.

## Pattern Guidance

Encouraged patterns:
Use a lightweight Facade shape for `Calculator`: one clear entrypoint such as `evaluate(expression)` for the GUI. Use Strategy as a plain operation registry or callable mapping when operations grow beyond simple branching.

Allowed with caution:
Memento is allowed for undo/history snapshots once that feature exists. Keep snapshots bounded and explicit. Avoid applying it before there is a real restore/history workflow.

Avoid by default:
Avoid Command objects for basic button clicks or arithmetic operations. Avoid Singleton/global registries for mutable calculator state. Avoid factories and plugin systems until there are multiple concrete variants that need them.

Pattern references:
See References below for the local CodeBTI pattern pages that shaped this guidance.

## References

Design pattern references:

- Encouraged: [Facade](../python/patterns/gof/facade.md). Supports a small `Calculator.evaluate()` boundary between GUI code and calculation internals.
- Encouraged: [Strategy](../python/patterns/gof/strategy.md). Supports the operation registry as a simple callable mapping without requiring class-heavy strategy objects.
- Allowed with caution: [Memento](../python/patterns/gof/memento.md). Supports snapshot history for undo/recent calculations, but only after the feature is real.
- Avoid by default: [Command](../python/patterns/gof/command.md). Basic GUI button actions should stay direct unless actions need replay, queuing, or undo metadata.
- Avoid by default: [Singleton](../python/patterns/gof/singleton.md). Mutable calculator state should not be hidden behind process-global access.

Useful project resources:

- [Python profile taxonomy](../python/profiles/python-profile-taxonomy.md). The final profile combines Algorithm-First Minimalist with object-centered boundary traits.
- [CodeStyle template](../python/templates/CodeStyle.template.md). This file follows the required CodeBTI output structure.

## Testing Policy

Required tests:
Test custom calculation logic: expression parsing, operator precedence, invalid input, division by zero, operation registry behavior, result objects, and state transitions.

Optional tests:
Add GUI smoke tests only if the GUI layer becomes complex or fragile. Do not test framework boilerplate by default.

Manual verification:
Manually run the GUI and check core flows: entering expressions, pressing operators, clearing display, showing errors, and using memory/history features if present.

## Git and Collaboration

Branching:
Fast mainline is preferred. Direct edits to `main` or one shared `dev` branch are acceptable for this small project.

Commit messages:
Use short descriptive messages, such as `add calculator result object` or `fix division error display`. Conventional commit prefixes are optional.

Review checklist:
Before finishing a change, check that the calculator behavior remains direct, GUI handlers stay thin, core logic tests cover changed calculation behavior, and no unnecessary layers were added.

## Agent Behavior

When writing code:
Start with the smallest clear implementation. Prefer one `Calculator` object, small helpers, a simple operation registry, and explicit result values.

When reviewing code:
Look first for over-architecture, hidden mutable globals, duplicated validation between GUI and calculator, missing core-logic tests, and comments that repeat obvious code.

When uncertain:
Keep code direct and local. Add structure only after repetition, confusing flow, or real feature variation appears.

## Examples

Preferred code shape:

```python
class Calculator:
    def __init__(self):
        self.memory = None
        self.history = []

    def evaluate(self, expression):
        try:
            value = evaluate_expression(expression, OPERATIONS)
        except (ValueError, ZeroDivisionError) as exc:
            return {"ok": False, "text": "Error", "value": None, "error": str(exc)}

        return {"ok": True, "text": str(value), "value": value, "error": None}
```

Avoided code shape:

```python
class CalculatorCommandFactory:
    def create_command(self, button_name):
        ...


class CalculatorServiceRegistry:
    calculator_service = None
```

## Open Assumptions

- GUI toolkit is not chosen yet.
- Exact calculator scope is not known: basic arithmetic, scientific functions, memory, undo, and history may change the structure.
- Packaging commands should be finalized once a `pyproject.toml` exists.
