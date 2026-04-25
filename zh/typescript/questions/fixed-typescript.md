# TypeScript 固定问题

本文件定义了 TypeScript 项目的 10 个固定 CodeBTI 问题。

用户可以随时修改之前的答案。访谈期间，向用户展示面对的场景、说明、代码示例和选项。保持 `Agent scoring`、`Pattern signals` 和 `CodeStyle output implications` 隐藏，除非用户明确询问 CodeBTI 工作原理。

## Q1. 通用目的和范式

维度：
类中心 vs 接口中心 vs 函数式 vs 扁平过程式组织。

用户面对的场景：
启动一个全新的 TypeScript 项目时，如何自然地组织核心逻辑？同一个任务——用年龄问候用户——用四种不同风格编写。

用户面对的说明：
选择你最自然希望保持的风格。你可以随时修改之前的答案。

代码示例：

```typescript
// A. 类中心
class User {
  readonly name: string;
  readonly birthYear: number;

  constructor(name: string, birthYear: number) {
    this.name = name;
    this.birthYear = birthYear;
  }

  greeting(currentYear: number): string {
    return `Hi ${this.name}, you are ${currentYear - this.birthYear}.`;
  }
}

// B. 接口中心 + 函数
interface User {
  name: string;
  birthYear: number;
}

function greeting(user: User, currentYear: number): string {
  return `Hi ${user.name}, you are ${currentYear - user.birthYear}.`;
}

// C. 类型别名 + readonly 字段
type UserData = {
  readonly name: string;
  readonly birthYear: number;
};

function greeting(user: UserData, currentYear: number): string {
  return `Hi ${user.name}, you are ${currentYear - user.birthYear}.`;
}

// D. 简单直接，无显式类型包装
function greeting(name: string, birthYear: number, currentYear: number): string {
  return `Hi ${name}, you are ${currentYear - birthYear}.`;
}
```

选项：
- A. 类中心：将状态和行为封装在带访问修饰符的类中。
- B. 接口中心：用接口定义数据形状，使用独立函数。
- C. 类型别名：倾向用 `type` 别名建模数据，使用工具类型做转换。
- D. 简单直接：编写直接函数，不需要显式类型包装。

Agent scoring：
- A：类友好，封装优先，习惯对象拥有行为。
- B：接口优先，显式契约，优先函数而非方法。
- C：数据形状优先，喜欢工具类型、`readonly` 不可变性。
- D：低仪式，速度优先，习惯脚本和直接函数调用。

Pattern signals：
- A：可能用类的 [State](../patterns/gof/state.md)、[Template Method](../patterns/gof/template-method.md)、[Strategy](../patterns/gof/strategy.md)。
- B：可能用可调用接口的 [Strategy](../patterns/gof/strategy.md)、[Adapter](../patterns/gof/adapter.md)。
- C：当类型化构造复杂度增长时，可能用 [Builder](../patterns/gof/builder.md) 或 [Factory Method](../patterns/gof/factory-method.md)。
- D：避免过早使用 GoF 模式；优先小型辅助函数和清晰的模块。

CodeStyle output implications：
用此答案设置默认项目形态：类中心、接口优先、类型别名数据模型，还是函数优先。未来指导应说明项目何时可能偏离该默认值。

## Q2. 防御性编程和类型边界

维度：
严格静态类型 vs 边界类型 vs 运行时验证 vs 灵活鸭子类型。

用户面对的场景：
TypeScript 让你控制类型的强制程度。对于一个更新用户年龄的函数，项目应有多严格？

用户面对的说明：
选择你最自然希望保持的风格。你可以随时修改之前的答案。

代码示例：

```typescript
// A. 严格类型收窄
function updateUserAge(userId: number, newAge: number): boolean {
  if (typeof newAge !== 'number' || !Number.isInteger(newAge)) {
    throw new TypeError('newAge must be an integer');
  }
  if (newAge <= 0) {
    throw new RangeError('newAge must be positive');
  }
  const user = dbGet(userId);
  user.age = newAge;
  dbSave(user);
  return true;
}

// B. 边界类型
function updateUserAge(userId: number, newAge: number): boolean {
  const user = dbGet(userId);
  if (newAge <= 0) return false;
  user.age = newAge;
  dbSave(user);
  return true;
}

// C. 使用 schema 库进行运行时验证
import { z } from 'zod';

const AgeUpdateSchema = z.object({
  userId: z.number().int().positive(),
  newAge: z.number().int().positive(),
});

function updateUserAge(rawInput: unknown): boolean {
  const payload = AgeUpdateSchema.parse(rawInput);
  const user = dbGet(payload.userId);
  user.age = payload.newAge;
  dbSave(user);
  return true;
}

// D. 灵活鸭子类型
function updateUserAge(userId: unknown, newAge: unknown): boolean {
  const id = Number(userId);
  const age = Number(newAge);
  if (!id || !age) return false;
  const user = dbGet(id);
  user.age = age;
  dbSave(user);
  return true;
}
```

选项：
- A. 严格类型收窄：在重要函数中使用 `typeof` 检查、类型守卫和显式错误抛出。
- B. 边界类型：公开函数签名类型严格，但内部代码保持灵活。
- C. 运行时验证：使用 Zod、Yup 或 class-validator 等 schema 库清理和检查输入数据。
- D. 灵活鸭子类型：接受宽泛输入类型并安全强制转换，保持类型检查轻量。

Agent scoring：
- A：高防御性编码，显式不变量，强静态分析姿态。
- B：边界优先纪律，内部实用灵活性。
- C：验证优先，接受运行时模型库和强制转换。
- D：灵活，低仪式，鸭子类型友好。

Pattern signals：
- A：支持显式接口、协议、严格 [Adapter](../patterns/gof/adapter.md)。
- B：支持在边界处使用 [Facade](../patterns/gof/facade.md) 和 [Adapter](../patterns/gof/adapter.md)，不在内部过度类型化。
- C：支持数据优先建模、验证边界、复杂载荷的 [Builder](../patterns/gof/builder.md)。
- D：除非项目风险需要，否则避免重型接口模式。

CodeStyle output implications：
设置类型策略、验证策略，以及 Agent 应在哪里添加检查。此答案应防止未来代码在严格类型风格和随意无类型风格之间随机混用。

## Q3. 错误处理和恢复

维度：
快速失败 vs 安全回退 vs 显式结果对象 vs 批量隔离。

用户面对的场景：
项目从 JSON API 接收交易载荷。有时 `amount` 缺失或是一个类似 `"N/A"` 的值。代码应如何处理这种错误输入？

用户面对的说明：
选择你最自然希望保持的风格。你可以随时修改之前的答案。

代码示例：

```typescript
// A. 快速失败
class MalformedTransactionError extends Error {
  constructor(message: string) {
    super(message);
    this.name = 'MalformedTransactionError';
  }
}

function calculateTotal(tx: Record<string, unknown>): number {
  if (!('amount' in tx)) {
    throw new MalformedTransactionError('Transaction is missing amount');
  }
  if (typeof tx.amount !== 'number') {
    throw new MalformedTransactionError('Transaction amount must be numeric');
  }
  return tx.amount * 1.2;
}

// B. 安全回退
function calculateTotal(tx: Record<string, unknown>): number {
  const amount = Number(tx.amount ?? 0);
  return isNaN(amount) ? 0 : amount * 1.2;
}

// C. 显式结果
type Result<T> =
  | { ok: true; value: T }
  | { ok: false; error: string };

function calculateTotal(tx: Record<string, unknown>): Result<number> {
  const amount = tx.amount;
  if (typeof amount !== 'number') {
    return { ok: false, error: 'Invalid amount' };
  }
  return { ok: true, value: amount * 1.2 };
}

// D. 记录并继续
import { Logger } from './logger';

function processBatch(transactions: Record<string, unknown>[]): number[] {
  const totals: number[] = [];
  for (const tx of transactions) {
    try {
      const amount = Number(tx.amount);
      if (!isNaN(amount)) {
        totals.push(amount * 1.2);
      } else {
        Logger.warn(`Skipped invalid transaction: ${JSON.stringify(tx)}`);
      }
    } catch (err) {
      Logger.warn(`Skipped transaction: ${err instanceof Error ? err.message : err}`);
    }
  }
  return totals;
}
```

选项：
- A. 快速失败：无效数据一出现就抛出清晰的类型化错误。
- B. 安全回退：返回默认值，保持主流程继续。
- C. 显式结果：对于可恢复的业务错误，返回结构化的成功或失败值而非抛出异常。
- D. 记录并继续：记录失败，跳过坏项，继续处理其余数据。

Agent scoring：
- A：契约优先，正确性优先于连续性，异常友好。
- B：连续性优先，宽容回退风格，有隐藏数据质量问题的风险。
- C：显式控制流，结果对象风格，适合可恢复业务错误。
- D：批量弹性，可观测性友好，适合数据管道。

Pattern signals：
- A：支持边界验证、严格 [Facade](../patterns/gof/facade.md)、自定义错误类层次结构。
- B：支持宽容的 [Adapter](../patterns/gof/adapter.md)/[Facade](../patterns/gof/facade.md) 行为，但需要明确的回退策略。
- C：支持函数式风格、[Command](../patterns/gof/command.md) 结果、显式工作流状态。
- D：支持流水线风格、[Chain of Responsibility](../patterns/gof/chain-of-responsibility.md)、隔离/死信工作流。

CodeStyle output implications：
定义项目级错误策略，使 Agent 不会随机混用静默默认值、异常、结果对象和隔离行为。

## Q4. 命名和可读性

维度：
显式命名 vs 简洁惯用语 vs 领域词汇 vs 注释支持的命名。

用户面对的场景：
命名塑造代码库的外观。变量、函数、接口和类应如何命名？

用户面对的说明：
选择你最自然希望保持的风格。你可以随时修改之前的答案。

代码示例：
无。选项是关于命名风格和审查期望，而非代码片段。

选项：
- A. 显式命名：偏好 `calculateTotalRevenueForActiveUsers` 这样即使更长也清晰的名称。
- B. 简洁惯用语：当上下文清晰时，允许 `id`、`req`、`cfg` 或 `idx` 等常见短名称。
- C. 领域语言：使用产品、业务、数学或科学领域的术语，而非 `Manager` 或 `Handler` 等通用名称。
- D. 短名称 + 解释：当 JSDoc 或注释解释原因和上下文时，允许较短的名称。

Agent scoring：
- A：通过显式命名实现可读性；容忍较长的行和较少的缩写。
- B：上下文heavy，惯用 TypeScript，舒适于紧凑的本地名称。
- C：领域驱动命名，避免通用 service/object 词汇。
- D：文档支持的命名，接受注释作为可读性的一部分。

Pattern signals：
- A：有助于显式 [Facade](../patterns/gof/facade.md) 和边界 API。
- B：支持函数优先和脚本式风格。
- C：支持领域模型、领域服务、清晰的通用语言。
- D：支持注释引导的 Agent 工作流和更冗长的生成文档。

CodeStyle output implications：
为函数、类、接口、类型、模块、变量和审查注释设置命名规则。生成的 `CodeStyle.md` 应包含允许的缩写和不应使用的通用名称。

## Q5. 架构和接线风格

维度：
类组合 vs 依赖注入 vs 工厂模式 vs 中央注册表 vs 直接模块导入。

用户面对的场景：
当项目有路由、设置/拆除、服务或多种实现时，如何偏好将各部分连接在一起？

用户面对的说明：
选择你最自然希望保持的风格。你可以随时修改之前的答案。

代码示例：
无。此问题比较架构偏好，而非一个本地代码片段。

选项：
- A. 带装饰符的类组合：使用 TypeScript 装饰符、类属性注入或框架提供的组合。
- B. 依赖注入：将服务、客户端和仓库显式传入构造函数或函数。
- C. 可交换实现：定义清晰接口，使不同后端或算法可以交换。
- D. 中央注册表或模块单例：将共享服务保存在一个配置的模块中，其他代码导入。
- E. 直接模块导入：保持模块自包含，使用直接导入，最小化间接。

Agent scoring：
- A：装饰符友好，框架对齐组合，当名称和测试清晰时接受隐藏设置。
- B：可测试性优先，显式依赖，低隐藏全局状态。
- C：接口优先，扩展友好，习惯类模式结构。
- D：便利性优先，集中配置，隐藏耦合的风险。
- E：简洁性优先，避免仪式，偏好扁平模块图。

Pattern signals：
- A：[Decorator](../patterns/gof/decorator.md)、[Proxy](../patterns/gof/proxy.md) 类包装器、框架特定组合。
- B：[Adapter](../patterns/gof/adapter.md)、[Facade](../patterns/gof/facade.md)、依赖注入、测试替身。
- C：[Strategy](../patterns/gof/strategy.md)、[Factory Method](../patterns/gof/factory-method.md)、[Abstract Factory](../patterns/gof/abstract-factory.md)、[Bridge](../patterns/gof/bridge.md)。
- D：[Singleton](../patterns/gof/singleton.md)/注册表注意。
- E：避免不必要的 GoF 结构；优先清晰的函数和数据结构。

CodeStyle output implications：
设置默认接线规则：装饰符、依赖注入、显式接口、中央注册表或直接模块导入。包括隐藏状态和过度抽象的警告规则。

## Q6. 文件夹结构

维度：
特性文件夹 vs 技术分层 vs 扁平源树 vs 框架/工具驱动布局。

用户面对的场景：
当代码库从单个文件增长到多个文件时，Agent 默认应使用什么结构？

用户面对的说明：
选择你最自然希望保持的风格。你可以随时修改之前的答案。

代码示例：

```text
# A. 特性文件夹
src/features/users/
src/features/billing/
src/features/reports/

# B. 技术分层
src/
  models/
  services/
  routes/
  controllers/

# C. 扁平到需要时
src/
  users.ts
  billing.ts
  reports.ts

# D. 工具或框架布局
src/
  <framework-convention>/
tests/
docs/
```

选项：
- A. 特性文件夹：按产品区域或领域分组文件，每个区域拥有自己的本地模型、服务和路由。
- B. 技术分层：按技术角色分组文件，如模型、服务、路由、数据和测试。
- C. 扁平到需要时：保持简单 `src/` 布局，直到嵌套真正有帮助时才添加。
- D. 工具或框架布局：遵循所选框架、包工具或模板预期的结构。

Agent scoring：
- A：领域/特性隔离，模块化所有权，适合增长的产品。
- B：分层架构，按技术角色传统分离。
- C：最小结构，低导入复杂度，痛苦出现时重构。
- D：约定优先，重视与工具和生态系统期望的兼容性。

Pattern signals：
- A：支持有界上下文，每个特性的 [Facade](../patterns/gof/facade.md)，本地 [Adapter](../patterns/gof/adapter.md)。
- B：支持服务层和类 MVC 组织。
- C：支持过程式/函数优先代码和低抽象。
- D：支持框架对齐设计和模板驱动结构。

CodeStyle output implications：
定义 Agent 应在哪里创建新模块以及何时可以引入子文件夹。相关时包括源 vs 本地数据分离。

## Q7. 测试理念

维度：
测试优先覆盖 vs 集成信心 vs 核心逻辑专注 vs 手动/日志驱动迭代。

用户面对的场景：
测试需要时间和维护。项目默认应有什么级别的测试？

用户面对的说明：
选择你最自然希望保持的风格。你可以随时修改之前的答案。

代码示例：
无。选项是关于测试范围和审查期望，而非代码片段。

选项：
- A. 测试优先且广泛覆盖：尽早编写测试，覆盖分支、边界情况和重要失败路径。
- B. 集成为主：聚焦端点、数据库边界、服务流程或完整工作流。
- C. 仅核心逻辑：测试自定义算法和业务规则，但避免测试框架样板。
- D. 手动和日志优先：快速移动，手动测试，依赖日志或用户反馈直到项目稳定。

Agent scoring：
- A：高测试纪律，回归预防，变更较慢但更安全。
- B：行为和边界信心，对单元测试每个辅助函数兴趣较低。
- C：ROI 导向测试，保护自定义逻辑同时避免低价值测试。
- D：原型速度，低自动化测试期望，较高回归风险。

Pattern signals：
- A：支持契约测试、[Adapter](../patterns/gof/adapter.md)、严格接口。
- B：支持 [Facade](../patterns/gof/facade.md)/API 测试和集成边界。
- C：支持算法优先和函数优先测试。
- D：避免需要大量测试脚手架的重型抽象。

CodeStyle output implications：
为生成的代码和未来 Agent 编辑设置最低测试要求。定义新功能是否需要单元测试、集成测试、冒烟测试或手动验证说明。

## Q8. 注释和文档字符串

维度：
自文档代码 vs 解释原因 vs 严格 JSDoc vs AI 面对上下文注释。

用户面对的场景：
AI Agent 可能过度解释代码。项目应强制执行什么注释和文档字符串风格？

用户面对的说明：
选择你最自然希望保持的风格。你可以随时修改之前的答案。

代码示例：
无。选项是关于注释策略和文档密度，而非代码片段。

选项：
- A. 最小注释：代码应足够清晰，注释罕见；JSDoc 主要用于公开 API 表面。
- B. 解释原因：避免重复代码的注释，但解释业务规则、约束和非显而易见决策。
- C. 完整 JSDoc：大多数类、方法和函数使用一致的 JSDoc 风格，包括所有参数和返回类型。
- D. AI 上下文注释：当注释减少未来 Agent 编辑的困惑时，允许注释作为计划标记或上下文。

Agent scoring：
- A：自文档偏好，低注释密度。
- B：上下文优先注释，适中 JSDoc，强审查价值。
- C：文档重型，API 参考友好，维护成本较高。
- D：Agent 协作友好，接受注释作为未来编辑指导。

Pattern signals：
- A：最适合清晰的名称、小型函数和命名良好的类型。
- B：支持领域驱动规则和边界文档。
- C：支持公共库/API 风格和严格接口。
- D：支持 Agent 工作流、计划/规格标记和引导重构。

CodeStyle output implications：
定义 Agent 何时应添加注释、JSDoc、计划注释和上下文标记。还定义清理期间应删除哪些注释类型。

## Q9. Git 历史和协作

维度：
快速主分支提交 vs 传统 PR 流程 vs 发布分支 vs 线性历史 vs 无 Git 偏好。

用户面对的场景：
当人类和 AI Agent 共同生成代码时，Git 历史和分支风格应是什么样？

用户面对的说明：
选择你最自然希望保持的风格。你可以随时修改之前的答案。

代码示例：
无。选项是关于协作工作流，而非 TypeScript 代码。

选项：
- A. 快速主分支：直接提交到 `main` 或一个共享的 `dev` 分支，带简短描述性消息。
- B. 传统分支：使用特性分支、pull request 和 `feat:`、`fix:`、`refactor:` 等消息。
- C. 发布分支：保持 `main` 聚焦生产，使用集成和发布分支，隔离热修复。
- D. 线性历史：压缩或变基，使历史读作无合并提交的干净序列。
- E. 无强烈 Git 偏好：保持 Git 要求轻量，不将工作流作为主要约束。

Agent scoring：
- A：速度优先协作，低流程开销。
- B：传统，审查友好，自动化友好。
- C：发布管理纪律，更强环境分离。
- D：历史清洁度，偏好精选提交。
- E：Git 轻量，可能需要最小的 Agent 假设。

Pattern signals：
- A：支持快速原型和直接编辑。
- B：支持审查清单、CI 和结构化 Agent 提交。
- C：支持发布管理规格和部署门控。
- D：支持精致的补丁集和仔细重构。
- E：避免在生成风格文件中过度指定 Git 行为。

CodeStyle output implications：
为未来 Agent 工作设置提交消息、分支、PR 和历史期望。如果选择 E，保持 Git 指导最小化。

## Q10. 依赖和环境

维度：
标准 npm vs pnpm/yarn vs 锁文件纪律 vs 新型快速工具。

用户面对的场景：
TypeScript/JavaScript 依赖管理塑造整个项目。应如何管理环境和第三方库？

用户面对的说明：
选择你最自然希望保持的风格。你可以随时修改之前的答案。

代码示例：

```text
A. package.json + node_modules + npm
B. package.json + pnpm-lock.yaml 或 yarn.lock
C. pnpm-workspace.yaml 或带严格锁文件的 monorepo
D. 最小依赖 + copybara 或 esm.sh CDN 风格导入
```

选项：
- A. 标准 npm：用 `package.json` 和内置 node_modules 保持设置简单。
- B. pnpm 或 yarn：需要时使用更快速、更高效的包管理器和 workspace 支持。
- C. 严格锁文件的 monorepo：使用 pnpm workspaces 或类似设置实现严格可重复性。
- D. 最小依赖：优先标准库、最少 npm 包，实用时使用 CDN 风格导入。

Agent scoring：
- A：最小工具，广泛的兼容性，简单设置。
- B：速度优先，现代工具偏好，workspace 支持。
- C：可重复性优先，结构化项目元数据，monorepo 纪律。
- D：依赖极简主义，避免供应链风险，优先内置 API。

Pattern signals：
- A：支持轻量脚本和简单包。
- B：支持现代 Agent 工作流和快速迭代。
- C：支持包/库风格和 CI 可重复性。
- D：支持算法优先项目和最小工具链。

CodeStyle output implications：
设置依赖策略、环境文件、安装命令，以及 Agent 是否可以添加新库。包括依赖的首选事实来源。