# Bridge

## 模式意图

将抽象部分与它的实现部分分离，使两者可以独立变化。

## TypeScript 形态

TypeScript 中的桥接使用 `interface` 来定义抽象，用一个单独的实现层次结构。抽象持有对实现类的类型化引用。

```typescript
// Implementation interface
interface ContentTypeImplementation {
  renderTitle(): string;
  renderCaption(): string;
  renderThumbnail(): string;
  renderLink(): string;
}

// Abstraction
abstract class ListItemViewAbstraction {
  constructor(protected contentType: ContentTypeImplementation) {}
  abstract getRenderedItem(): string;
}

// Refined abstraction
class VisualListItemView extends ListItemViewAbstraction {
  getRenderedItem(): string {
    return `<li>${this.contentType.renderThumbnail()}${this.contentType.renderLink()}</li>`;
  }
}

// Concrete implementation
class PostContentType implements ContentTypeImplementation {
  constructor(
    private title: string,
    private caption: string,
    private imageUrl: string,
    private url: string
  ) {}
  renderTitle() { return `<h2>${this.title}</h2>`; }
  renderCaption() { return `<p>${this.caption}</p>`; }
  renderThumbnail() { return `<img alt="${this.title}" src="${this.imageUrl}"/>`; }
  renderLink() { return `<a href="${this.url}">${this.title}</a>`; }
}
```

## 何时适合此风格

- 存在两个独立维度，且不应该通过创建子类组合爆炸来变化。
- 需要在运行时选择实现（例如，跨内容类型的渲染视图）。
- 具有共享抽象的插件或平台特定行为。

## 何时避免

- 只存在一个变化维度 — 简单的条件或策略就足够了。
- 抽象和实现确实属于同一个类。
- 维护两个层次结构的复杂性超过其收益。

## CodeBTI 信号

用户偏好清晰的关注点分离，且能够舒适地管理两个层次结构。这通常出现在多渲染目标、多平台适配器或多后端架构的项目中。

## Agent 指导

当项目有两个真正的变化轴时使用 Bridge。当只有一个维度变化时，优先使用更简单的组合。

## 相关模式

[Abstract Factory](abstract-factory.md), [Adapter](adapter.md), [Strategy](strategy.md).

## 来源引用

- 示例: [Conceptual](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Bridge/Conceptual/index.ts), [RealWorld](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Bridge/RealWorld/index.ts)
- 目录: https://refactoring.guru/design-patterns/bridge