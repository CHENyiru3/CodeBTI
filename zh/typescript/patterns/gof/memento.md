# Memento

## 模式意图

捕获并外化对象的内部状态而不违反封装约束，以便对象可以在以后恢复到该状态。

## TypeScript 形态

TypeScript 的 Memento 使用带类型的接口来定义快照，并使用泛型约束来确保类型安全。Originator 负责创建和恢复 Memento。

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

## 何时适合此风格

- 必须保存和恢复对象状态的快照，且不能破坏封装。
- 需要撤销/重做功能。
- 为长时间运行的进程设置检查点。

## 何时避免

- 不需要撤销/重做或检查点。
- 对象已经公开暴露其状态——Memento 增加的价值很小。
- 状态复杂，序列化不切实际。

## CodeBTI 信号

用户希望显式捕获状态，用于撤销、历史记录或检查点。这出现在编辑器、表单构建器、游戏引擎和工作流系统中。

## Agent 指导

将 Memento 用于撤销/重做或检查点。优先使用 TypeScript 的 `readonly` 和不可变数据结构，以减少需要捕获的内容。

## 相关模式

[Command](../command.md)（使用 Memento 实现撤销）、[Iterator](../iterator.md)（Memento 可用于保存迭代器状态）。

## 来源引用

- 示例：[Conceptual](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Memento/Conceptual/index.ts)、[RealWorld](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Memento/RealWorld/index.ts)
- 目录：https://refactoring.guru/design-patterns/memento