# Proxy

## 模式意图

为另一个对象提供一个替代品或占位符，以控制对该对象的访问或为其添加额外职责。

## TypeScript 形态

TypeScript 中的 Proxy 模式使用一个 `interface` 来同时约束真实主题和代理对象。代理持有真实主题的引用，并在真实调用之前、之后或替代执行时添加行为。

```typescript
interface WeatherService {
  request(): Promise<WeatherForecast>;
}

class RealWeatherServiceSDK implements WeatherService {
  async request(): Promise<WeatherForecast> {
    return new Promise(resolve =>
      setTimeout(() => resolve({
        avgTemperature: Math.random() * 35,
        maxPrecipitationProbability: Math.random() * 100,
      }), 1000)
    );
  }
}

class ProxyWeatherService implements WeatherService {
  private cachedResponse: WeatherForecast | null = null;
  private cacheDate: Date | null = null;
  private readonly expiration = 24 * 60 * 60 * 1000;

  constructor(private real: WeatherService) {}

  async request(): Promise<WeatherForecast> {
    if (!this.isCacheValid()) {
      this.cachedResponse = await this.real.request();
      this.cacheDate = new Date();
    }
    return this.cachedResponse!;
  }

  private isCacheValid(): boolean {
    if (!this.cachedResponse || !this.cacheDate) return false;
    return Date.now() < this.cacheDate.getTime() + this.expiration;
  }
}
```

## 何时适合此风格

- 需要为现有对象添加缓存、日志、访问控制或延迟初始化，但不想修改其接口。
- 需要控制对昂贵或远程资源的访问。
- 需要在委托给真实对象之前有条件地添加行为。

## 何时避免

- 代理除了直接委托外不添加任何行为。
- 主题的接口已经存在——代理必须精确匹配它。
- 更简单的包装函数就能达到同样的目的。

## CodeBTI 信号

用户偏好中间件风格的分层架构，希望在不修改核心逻辑的情况下添加横切关注点（缓存、日志、认证）。

## Agent 指导

将 Proxy 用于缓存、延迟初始化和访问日志。让代理专注于单一职责。当更简单的组合就能满足需求时，不要链式叠加多个代理。

## 相关模式

[Decorator](../decorator.md)（结构相似，意图不同）、[Adapter](../adapter.md)（提供不同的接口，Proxy 则保留原接口）。

## 来源引用

- 示例：[Conceptual](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Proxy/Conceptual/index.ts)、[RealWorld](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Proxy/RealWorld/index.ts)
- 模式目录：https://refactoring.guru/design-patterns/proxy