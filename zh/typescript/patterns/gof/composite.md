# Composite

## 模式意图

将对象组合成树结构以表示"部分-整体"的层次结构。Composite 让用户可以统一对待单个对象和组合对象。

## TypeScript 形态

TypeScript 的组合使用 `abstract class` 或 `interface` 定义组件合约。叶节点和组合节点实现相同的接口，组合管理子节点数组。

```typescript
abstract class Component {
  protected parent: Component | null = null;
  setParent(parent: Component | null) { this.parent = parent; }
  getParent(): Component | null { return this.parent; }
  add(component: Component): void {}
  remove(component: Component): void {}
  isComposite(): boolean { return false; }
  abstract operation(): string;
}

class Leaf extends Component {
  operation(): string { return 'Leaf'; }
}

class Composite extends Component {
  private children: Component[] = [];
  add(component: Component): void {
    this.children.push(component);
    component.setParent(this);
  }
  remove(component: Component): void {
    const idx = this.children.indexOf(component);
    if (idx >= 0) { this.children.splice(idx, 1); component.setParent(null); }
  }
  isComposite(): boolean { return true; }
  operation(): string {
    return `Branch(${this.children.map(c => c.operation()).join('+')})`;
  }
}
```

## 何时适合此风格

- 部分-整体层次结构，如树、图或嵌套配置。
- 操作应该统一应用于单个对象和组合。
- 递归树处理，具有统一的遍历逻辑。

## 何时避免

- 数据不是自然分层的 — 平面列表或映射更简单。
- 只存在叶节点 — 不需要组合。
- 叶节点和组合节点之间的操作差异很大。

## CodeBTI 信号

用户接受对单个对象和组合对象的统一处理。这出现在文件系统、UI 组件树、组织层次结构和定价/产品捆绑包中。

## Agent 指导

为树状数据结构使用 Composite。保持组件接口最小。优先使用 TypeScript 的结构类型来避免强制继承层次结构。

## 相关模式

[Decorator](decorator.md), [Iterator](iterator.md), [Visitor](visitor.md)（经常一起使用）。

## 来源引用

- 示例: [Conceptual](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Composite/Conceptual/index.ts), [RealWorld](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Composite/RealWorld/index.ts)
- 目录: https://refactoring.guru/design-patterns/composite