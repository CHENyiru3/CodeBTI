# Bridge

## Pattern Intent

Decouple an abstraction from its implementation so that the two can vary independently.

## TypeScript Shape

TypeScript bridges use `interface` for the abstraction and a separate hierarchy of implementations. The abstraction holds a typed reference to the implementation.

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

## When This Style Fits

- Two independent dimensions that should vary without creating a combinatorial explosion of subclasses.
- Runtime selection of implementations (e.g., rendering views across content types).
- Plugins or platform-specific behavior with a shared abstraction.

## When To Avoid

- Only one dimension of variation exists — a simple conditional or strategy is sufficient.
- The abstraction and implementation genuinely belong together in one class.
- The complexity of maintaining two hierarchies outweighs the benefit.

## CodeBTI Signals

The user prefers clean separation of concerns and is comfortable managing two hierarchies. This often appears in projects with multiple rendering targets, platform adapters, or multi-backend architectures.

## Agent Guidance

Use Bridge when the project has two genuine axes of variation. Prefer simpler composition when only one dimension varies.

## Related Patterns

[Abstract Factory](abstract-factory.md), [Adapter](adapter.md), [Strategy](strategy.md).

## Source Reference

- Examples: [Conceptual](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Bridge/Conceptual/index.ts), [RealWorld](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Bridge/RealWorld/index.ts)
- Catalog: https://refactoring.guru/design-patterns/bridge
