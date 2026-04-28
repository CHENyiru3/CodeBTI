# Proxy

## Pattern Intent

Provide a surrogate or placeholder for another object to control access to the original object or to add other responsibilities.

## TypeScript Shape

TypeScript proxies use an `interface` shared between the real subject and proxy. The proxy holds a reference to the real subject and adds behavior before, after, or instead of the real call.

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

## When This Style Fits

- Adding caching, logging, access control, or lazy initialization to an existing object without changing its interface.
- Controlling access to expensive or remote resources.
- Adding behavior conditionally before delegating to the real object.

## When To Avoid

- The proxy adds no behavior beyond direct delegation.
- The subject's interface already exists — a proxy must match it exactly.
- A simpler wrapper function achieves the same goal.

## CodeBTI Signals

The user prefers middleware-style layers and wants to add cross-cutting concerns (caching, logging, authentication) without modifying core logic.

## Agent Guidance

Use Proxy for caching, lazy initialization, and access logging. Keep the proxy focused on one responsibility. Do not chain multiple proxies when a simpler composition suffices.

## Related Patterns

[Decorator](decorator.md) (similar structure, different intent), [Adapter](adapter.md) (provides a different interface, Proxy preserves it).

## Source Reference

- Examples: [Conceptual](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Proxy/Conceptual/index.ts), [RealWorld](https://github.com/RefactoringGuru/design-patterns-typescript/blob/main/src/Proxy/RealWorld/index.ts)
- Catalog: https://refactoring.guru/design-patterns/proxy
