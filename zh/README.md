# CodeBTI

![CodeBTI 概览](https://i.imgur.com/annGWpK.jpeg)

CodeBTI 是 MBTI 的代码风格版本，为软件项目服务。它帮助人类开发者和 AI Agent 在实现之前，选择一套一致的编码风格、设计模式姿态、测试策略、依赖策略和协作流程。

CodeBTI 不是人格测试。它是一套实用的访谈与文档系统，用来生成项目专属的指导文件，如 `CodeStyle.md`、`SKILL.md` 或 `SPEC.md`。

## 安装为 Skill

本仓库可直接安装为 Codex skill。将本仓库复制或安装到 Codex skills 目录中，命名为 `codebti`。根目录的 `SKILL.md` 即为入口文件。

## 工作原理

1. 用户描述项目需求。
2. Agent 在目标项目中创建一份实时的 `Recording.md`，并记录项目摘要。
3. Agent 针对选定语言提出固定问题集。当前的 Python 问题集位于 [python/questions/fixed-python.md](python/questions/fixed-python.md)。
4. 每个问题之前，Agent 将完整的题目卡保存到 `Recording.md`；用户回答后，更新答案日志并给出简短的项目反馈，再问下一个问题。
5. Agent 使用该语言的适应性追问指南，提出恰好 5 个后续追问。当前的 Python 追问指南位于 [python/questions/adaptive-question-guide.md](python/questions/adaptive-question-guide.md)。
6. Agent 将 `Recording.md` 作为事实来源重新阅读。
7. Agent 根据相关语言专属的 Profile 分类体系推断风格 Profile。
8. Agent 为该语言和生态系统选择相关的本地模式/资源引用。
9. Agent 使用语言包中的模板生成项目指导，包括引用说明——解释每个被引用模式或资源的重要性。

## 示例

[example/](example/) 目录中包含一个完整的 CodeBTI 访谈记录，针对一个小型 Python GUI 计算器。

- [example/Recording.md](example/Recording.md)：完整访谈记录，包含项目摘要、10 个固定答案、5 个自适应答案、反馈、隐藏推理笔记和最终 Profile 推断。
- [example/CodeStyle.md](example/CodeStyle.md)：生成的项目风格指南。

推断出的 Profile 为 **算法优先极简主义者（Algorithm-First Minimalist），具有对象中心边界特征**。最终指导建议：

- 在轻量 GUI 处理器背后放置一个小型 `Calculator` 对象，
- 直接的表达式/求值逻辑配合轻量级操作注册表，
- 对无效用户输入返回显式结果对象，
- 保持扁平项目结构，直到代码真正需要文件夹时才拆分，
- 对解析、优先级、无效输入和状态转换进行核心逻辑测试，
- 最小化注释，保持轻量类型注解，
- 使用 `uv`、`pyproject.toml` 和 `uv.lock` 进行依赖管理。

## 仓库地图

- [SKILL.md](SKILL.md)：面向 AI Agent 的可安装技能入口。
- [AGENT.md](AGENT.md)：顶层 Agent 指南和工作流参考。
- [example/](example/)：Python GUI 计算器 CodeBTI 示例。
- [python/](python/)：第一个语言包，包含 Python 的问题集、模式库、Profile 体系、记录模板和输出模板。
- [python/questions/](python/questions/README.md)：Python 固定问题和适应性追问指南。
- [python/patterns/](python/patterns/README.md)：Python 设计模式数据库，引用 RefactoringGuru。
- [python/profiles/](python/profiles/README.md)：Profile 推断规则和 Python Profile 分类体系。
- [python/records/](python/records/README.md)：会话记录规则和记录模板。
- [python/templates/](python/templates/README.md)：生成项目指导的输出模板。

## 语言覆盖

初始语言包为 Python。欢迎为其他语言贡献内容。

每个语言包应保持相同的 CodeBTI 访谈约定，同时将内容适配到该生态系统：

- 针对该语言风格、架构、测试、依赖和协作规范的固定问题集，
- 针对项目特定追问的适应性追问指南，
- 将答案模式映射为实用编码指导的 Profile 分类体系，
- 适配该语言而非强行使用 Python 或 GoF 术语的模式/资源引用，
- `CodeStyle.md`、`SKILL.md`、`SPEC.md` 等生成式输出的模板。

未来的语言包应作为同级目录添加，例如 `javascript/`、`typescript/`、`go/`、`rust/`、`java/` 或 `r/`。

## 输出

主要输出是项目专属的 `CodeStyle.md`。需要时，同一结果可提炼为：

- `SKILL.md`：可复用的 Agent 行为定义，
- `SPEC.md`：项目需求文档，
- 更细分的专项规范，如 `API_SPEC.md`、`TESTING_SPEC.md` 或 `ARCHITECTURE_SPEC.md`。

访谈中的实时证据保存在会话期间的 `Recording.md` 中，包含完整题目卡、答案日志、反馈、隐藏推理笔记和最终证据审核。项目可保留原文件、按日期重命名存入语言包 `records/` 目录，或在输出生成后将文件归档。

## 贡献

欢迎贡献，尤其是新的语言包、更优质的问题集、更完善的 Profile 分类体系、更清晰的示例和文档改进。

好的贡献应保留核心工作流：

- 每次只问一个问题，
- 提问前将完整题目卡记录下来，
- 每次回答后更新 `Recording.md`，
- 问 10 个固定问题加上恰好 5 个适应性追问，
- 根据完整的会话记录推断最终 Profile，
- 仅引用对生成指导有实质影响的参考。

新增语言包时：

1. 创建顶层语言目录，如 `typescript/` 或 `rust/`。
2. 包含平行的子目录：`questions/`、`patterns/`、`profiles/`、`records/` 和 `templates/`，除非该语言有充分理由不这样做。
3. 问题卡要具体且基于示例。使用该语言的惯用法、依赖工具、测试框架和协作规范。
4. 避免将 Python 特有的假设照搬到其他语言。生成的风格应原生适配目标生态系统。
5. 当新语言包足够成熟时，添加或更新示例。
6. 更新本 README 和仓库地图，以便 Agent 能发现新语言包。

小型改动请提交聚焦的补丁，说明要修复的行为或文档问题。如果问题、Profile 或模式页面有改动，需说明新措辞如何改善未来生成的指导。
