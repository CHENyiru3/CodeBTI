# Adapter

## Pattern Intent

Convert the interface of a class into another interface clients expect. Adapter lets classes work together that could not otherwise because of incompatible interfaces.

## TypeScript Shape

TypeScript adapters use `interface` declarations and implement them explicitly. Classes or functions wrap the incompatible original and expose the expected interface.

```typescript
// Target interface (what the client expects)
interface TaxiCalculator {
  calculatePriceInEuros(km: number, isAirport: boolean): number;
}

// Adaptee (existing incompatible library)
class UKTaxiCalculatorLibrary {
  getPriceInPounds(miles: number, fare: Fares): number { /* ... */ }
}

// Adapter
class UKTaxiCalculatorLibraryAdapter implements TaxiCalculator {
  constructor(private adaptee: UKTaxiCalculatorLibrary) {}
  calculatePriceInEuros(km: number, isAirport: boolean): number {
    const miles = km * 1.609;
    const pounds = this.adaptee.getPriceInPounds(miles, isAirport ? Fares.Airport : Fares.Standard);
    return pounds * 1.15; // convert to euros
  }
}
```

## When This Style Fits

- Integrating third-party libraries or legacy code with incompatible interfaces.
- Creating a stable internal interface that shields the project from external API changes.
- Migrating between data sources or service providers.

## When To Avoid

- The incompatibility is minor and can be resolved by direct usage with type assertions.
- The adapter introduces a new abstraction layer that duplicates existing types.
- A simpler factory function or wrapper can achieve the same goal.

## CodeBTI Signals

The user accepts explicit boundary wrapping and likely values testability over convenience. This pairs well with [Facade](facade.md) for complex subsystem integration.

## Agent Guidance

Default to explicit interfaces at system boundaries. Use Adapter to wrap incompatible external dependencies. Do not create adapters for internal code that already has a consistent interface.

## Related Patterns

[Facade](facade.md), [Strategy](strategy.md), [Proxy](proxy.md).

## Source Reference

- Examples: [Conceptual](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Adapter/Conceptual/index.ts), [RealWorld](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Adapter/RealWorld/index.ts)
- Catalog: https://refactoring.guru/design-patterns/adapter
