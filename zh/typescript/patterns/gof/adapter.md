# Adapter

## 模式意图

将一个类的接口转换为客户期望的另一个接口。Adapter 让原本因接口不兼容而无法合作的类可以一起工作。

## TypeScript 形态

TypeScript 中的适配器使用 `interface` 声明并显式实现它们。类或函数包装不兼容的原始对象并暴露期望的接口。

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

## 何时适合此风格

- 集成第三方库或遗留代码中接口不兼容的部分。
- 创建一个稳定的内部接口，使项目与外部 API 变化隔离。
- 在不同数据源或服务提供商之间迁移。

## 何时避免

- 不兼容性很小，可以通过直接使用加类型断言来解决。
- 适配器引入的新抽象层与现有类型重复。
- 一个更简单的工厂函数或包装器可以达到同样的目标。

## CodeBTI 信号

用户接受显式的边界包装，可能更重视可测试性而非便利性。这与 [Facade](facade.md) 结合使用非常适合复杂子系统集成。

## Agent 指导

在系统边界处默认使用显式接口。使用 Adapter 包装不兼容的外部依赖。不要为内部代码创建适配器，内部代码已经具有一致的接口。

## 相关模式

[Facade](facade.md), [Strategy](strategy.md), [Proxy](proxy.md).

## 来源引用

- 示例: [Conceptual](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Adapter/Conceptual/index.ts), [RealWorld](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Adapter/RealWorld/index.ts)
- 目录: https://refactoring.guru/design-patterns/adapter