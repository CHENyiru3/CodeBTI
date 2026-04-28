# Template Method

## Pattern Intent

Define the skeleton of an algorithm in an operation, deferring some steps to subclasses. Template Method lets subclasses redefine certain steps of an algorithm without changing its structure.

## TypeScript Shape

TypeScript uses `abstract class` with protected methods for the template method and abstract methods for steps to be implemented. Hooks are protected methods with default implementations.

```typescript
abstract class InvoiceFormatter {
  constructor(protected readonly invoice: Invoice) {}

  format(): string {
    return `${this.formatHeader()}${this.hookFormatSubHeader()}` +
      `${this.formatCustomer()}${this.formatInvoiceLines()}` +
      `${this.formatTaxes()}${this.formatTotal()}` +
      `${this.formatFooter()}${this.hookFormatSubFooter()}`;
  }

  protected abstract formatHeader(): string;
  protected abstract formatCustomer(): string;
  protected abstract formatInvoiceLines(): string;
  protected abstract formatTaxes(): string;
  protected abstract formatFooter(): string;
  protected hookFormatSubHeader(): string { return ''; }
  protected formatTotal(): string { return `Total: ${this.invoice.total}€`; }
  protected hookFormatSubFooter(): string { return ''; }
}

class HtmlInvoiceFormatter extends InvoiceFormatter {
  protected formatHeader(): string { return '<h1>ACME S.L. Invoice</h1>'; }
  protected hookFormatSubHeader(): string { return '<hr/>'; }
  protected formatCustomer(): string { return `<div>${this.invoice.customer}</div>`; }
  protected formatInvoiceLines(): string { return '<ul>...</ul>'; }
  protected formatTaxes(): string { return `<div>Taxes: ${this.invoice.taxes}€</div>`; }
  protected formatFooter(): string { return '<footer>Center Avenue, 42</footer>'; }
}
```

## When This Style Fits

- An algorithm has invariant steps and customizable steps.
- Common behavior should be defined once and shared.
- Hooks allow subclasses to extend behavior at specific points without overriding the entire algorithm.

## When To Avoid

- The algorithm has no invariant steps — every step varies.
- A simpler approach like function composition achieves the same goal.
- Inheritance is awkward or impossible (composition over inheritance).

## CodeBTI Signals

The user prefers class hierarchies with shared base logic and wants to allow customization at specific points. This appears in report generators, serializers, and format converters.

## Agent Guidance

Use Template Method for algorithms with invariant steps and customizable steps. Prefer composition over inheritance if the algorithm's steps can be modeled as separate functions.

## Related Patterns

[Strategy](strategy.md) (Strategy overrides the algorithm itself, Template Method overrides steps), [Factory Method](factory-method.md) (often called from template methods).

## Source Reference

- Examples: [Conceptual](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/TemplateMethod/Conceptual/index.ts), [RealWorld](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/TemplateMethod/RealWorld/index.ts)
- Catalog: https://refactoring.guru/design-patterns/template-method
