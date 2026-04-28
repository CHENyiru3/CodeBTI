# Memento

## Pattern Intent

Capture and externalize an object's internal state without violating encapsulation, so that the object can be restored to this state later.

## TypeScript Shape

TypeScript mementos use typed interfaces for the snapshot and generic constraints to ensure type safety. The originator creates and restores mementos.

```typescript
interface Memento<T> {
  readonly state: T;
  readonly name: string;
  readonly date: Date;
}

interface EmployeeState {
  salary: number;
  monthlyExpensesLimit: number;
}

class EmployeeOriginator {
  private _name: string;
  private _salary: number;
  private _monthlyExpensesLimit: number;

  constructor(name: string, salary: number) {
    this._name = name;
    this._salary = salary;
    this._monthlyExpensesLimit = 0;
  }

  saveSnapshot(): Memento<EmployeeState> {
    return {
      state: { salary: this._salary, monthlyExpensesLimit: this._monthlyExpensesLimit },
      name: `salary=${this._salary}, limit=${this._monthlyExpensesLimit}`,
      date: new Date(),
    };
  }

  restore(memento: Memento<EmployeeState>): void {
    this._salary = memento.state.salary;
    this._monthlyExpensesLimit = memento.state.monthlyExpensesLimit;
  }
}

class EmployeeCaretaker {
  private _mementos: Memento<EmployeeState>[] = [];
  constructor(private employee: EmployeeOriginator) {}

  backup(): void { this._mementos.push(this.employee.saveSnapshot()); }
  undo(): void {
    const m = this._mementos.pop();
    if (m) this.employee.restore(m);
  }
}
```

## When This Style Fits

- A snapshot of an object's state must be saved and restored without breaking encapsulation.
- Undo/redo functionality is needed.
- Checkpointing long-running processes.

## When To Avoid

- No undo/redo or checkpointing is needed.
- The object exposes its state publicly anyway — a memento adds little value.
- State is complex and serialization is impractical.

## CodeBTI Signals

The user wants explicit state capture for undo, history, or checkpointing. This appears in editors, form builders, game engines, and workflow systems.

## Agent Guidance

Use Memento for undo/redo or checkpointing. Prefer TypeScript's `readonly` and immutable data structures to minimize what must be captured.

## Related Patterns

[Command](command.md) (uses Memento for undo), [Iterator](iterator.md) (Memento can store iterator state).

## Source Reference

- Examples: [Conceptual](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Memento/Conceptual/index.ts), [RealWorld](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Memento/RealWorld/index.ts)
- Catalog: https://refactoring.guru/design-patterns/memento
