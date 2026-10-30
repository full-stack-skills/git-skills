# git-skills

九个可独立安装的项目 Git 规范技能。语言：中文；Apache-2.0；运行时 Python 3.11+ 与 Git 2.41+，无第三方依赖。

- `gitguard-awesome`：权威资料导航与比较
- `gitguard-workflow`：工作流识别、选择与定义
- `gitguard-init`：Git 状态发现与接入
- `gitguard-branch`：分支生命周期
- `gitguard-audit`：分支与规范审计
- `gitguard-commit`：提交前分支与消息门禁
- `gitguard-sync`：同步与集成
- `gitguard-release`：发布、修复与版本回灌
- `gitguard-recovery`：诊断与保留式恢复

以下名称属于本次本地候选，远端旧发布尚未提供新入口；发布后安装示例：`npx skills add full-stack-skills/git-skills --skill gitguard-workflow`。仓库：https://github.com/full-stack-skills/git-skills 。安装行为由使用者执行，本次没有安装到宿主。

技能可只读独立工作；GitFlow 插件提供确定性规则、Hook/MCP 与显式变更。不把分支治理通过当质量/CI/生产通过。当前 GitGuard 运行时仅以 `<git-common-dir>/gitflow.xml` 为规则权威；init 选择工作流并初始化 XML，install 管理 AGENTS.md 引导。旧 JSON/激活资料只用于显式兼容迁移，不得默认回退。

[来源](sources.json) 与 profiles/ 为模板事实源；技能内参考自包含，可粒度安装。首次空仓主线提交需要明确初始提交规则，模板不会自动免检。

验证：`python3 scripts/validate.py`；TRACE 在工作区工具中执行。

0.2.0：九技能补充 v2 规则级别、结构化检查、可信 PR 范围、固定组织基线与接线诊断契约；旧 v1 模板保持兼容。
