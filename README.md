# git-skills

九个可独立安装的项目 Git 规范技能。语言：中文；Apache-2.0；运行时 Python 3.11+ 与 Git 2.41+，无第三方依赖。

- `git-awesome`：权威资料导航与比较
- `git-workflow`：工作流识别、选择与定义
- `git-init`：Git 状态发现与接入
- `git-branch`：分支生命周期
- `git-audit`：分支与规范审计
- `git-commit`：提交前分支与消息门禁
- `git-sync`：同步与集成
- `git-release`：发布、修复与版本回灌
- `git-recovery`：诊断与保留式恢复

安装示例：`npx skills add full-stack-skills/git-skills --skill git-workflow`。仓库：https://github.com/full-stack-skills/git-skills 。安装行为由使用者执行，本次没有安装到宿主。

技能可只读独立工作；GitFlow 插件提供确定性规则、Hook/MCP 与显式变更。不把分支治理通过当质量/CI/生产通过。共享规范推荐 .gitflow/workflow.json；Git 元数据保存激活与逐工作树日志。

[来源](sources.json) 与 profiles/ 为模板事实源；技能内参考自包含，可粒度安装。首次空仓主线提交需要明确初始提交规则，模板不会自动免检。

验证：`python3 scripts/validate.py`；TRACE 在工作区工具中执行。
