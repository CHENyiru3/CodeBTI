# Template Method

## 模式意图

在一个操作中定义一个算法的骨架，将某些步骤推迟到子类中实现。Template Method 让子类可以重新定义算法的某些步骤而无需改变其结构。

## TypeScript 形态

TypeScript 使用 `abstract class` 和 `protected` 方法来实现模板方法，抽象方法用于需要子类实现的步骤。钩子（Hook）是带有默认实现的 `protected` 方法。

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

## 何时适合此风格

- 一个算法有不变的步骤和可定制的步骤。
- 通用行为应该定义一次并被共享。
- 钩子允许子类在特定点上扩展行为，而无需重写整个算法。

## 何时避免

- 算法没有不变的步骤——每个步骤都是可变的。
- 更简单的方法（如函数组合）就能达到同样的目的。
- 继承很别扭或不可能（优先使用组合而非继承）。

## CodeBTI 信号

用户偏好带有共享基础逻辑的类层次结构，并希望允许在特定点上定制。这出现在报告生成器、序列化器和格式转换器中。

## Agent 指导

将 Template Method 用于具有不变步骤和可定制步骤的算法。如果算法的步骤可以建模为独立函数，优先使用组合而非继承。

## 相关模式

[Strategy](strategy.md)（Strategy 重写整个算法，Template Method 只重写步骤）、[Factory Method](factory-method.md)（常从模板方法中调用）。

## 来源引用

- 示例：[Conceptual](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/TemplateMethod/Conceptual/index.ts)、[RealWorld](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/TemplateMethod/RealWorld/index.ts)
- 模式目录：https://refactoring.guru/design-patterns/template-method