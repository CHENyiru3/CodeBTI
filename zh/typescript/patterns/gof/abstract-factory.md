# Abstract Factory

## 模式意图

生成一系列相关或相互依赖的对象，而无需指定它们的具体类。

## TypeScript 形态

TypeScript 中的抽象工厂使用 `interface` 或 `abstract class` 来声明产品创建方法。具体工厂实现这些方法并返回类型化的实例。

```typescript
// Abstract products
interface DB { connect(): void; }
interface FS { readFile(path: string): Promise<string>; }

// Abstract factory
interface EnvironmentFactory {
  getDB(): DB;
  getFS(): FS;
}

// Concrete factory
class ProdFactory implements EnvironmentFactory {
  getDB(): DB { return new MySQLDB(); }
  getFS(): FS { return new S3FS(); }
}
```

## 何时适合此风格

- 项目包含一系列相关对象（如数据库 + 缓存 + 日志记录器），且必须保持一致。
- 不同环境或配置层需要不同的具体实现。
- 测试需要切换整个基础设施栈。

## 何时避免

- 只存在一个具体工厂变体 — 抽象工厂增加了间接性但没有收益。
- 简单的工厂函数或依赖注入可以用更少的代码解决问题。
- 这个"家族"实际上只有一个产品 — 不要创建虚假的家族。

## CodeBTI 信号

用户倾向于可切换的基础设施实现，可能正在构建多环境应用程序。这表明偏好在整个依赖图中使用类似 [Strategy](strategy.md) 的灵活性。

## Agent 指导

默认使用带有显式接口的依赖注入。当项目明确需要在环境或配置之间切换一系列相关依赖时，使用 Abstract Factory。

## 相关模式

[Factory Method](factory-method.md), [Strategy](strategy.md), [Facade](facade.md).

## 来源引用

- 示例: [Conceptual](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/AbstractFactory/Conceptual/index.ts), [RealWorld](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/AbstractFactory/RealWorld/index.ts)
- 目录: https://refactoring.guru/design-patterns/abstract-factory