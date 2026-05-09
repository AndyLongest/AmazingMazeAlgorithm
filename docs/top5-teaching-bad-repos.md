# Top 5 教学型“坏仓库”报告（Python Web + SQLite）

本报告面向 Harness Engineer 实训场景，聚焦“人类工程师可运行，但 AI Agent 冷启动容易失败”的仓库。以下 5 个项目均为 Python Web 应用候选，适合用于补齐可见性、边界约束、验证门禁与交接协议。

## 1. VulpesCRM
- 仓库链接：https://github.com/pcanadas/VulpesCRM
- 选择原因：Flask CRM 业务流程完整（客户、线索、跟进等），具备真实表单与状态流转；常见问题是文档与自动化门禁不足，正适合训练 Agent 接手与验收闭环。

## 2. DjangoCRM / django-crm
- 仓库链接：https://github.com/DjangoCRM/django-crm
- 选择原因：Django 提供“可运行骨架”，但工程化工件往往不完整；可用于训练从“能跑”升级到“可约束、可验证、可交接”，尤其适合补任务边界与完成定义。

## 3. horilla-crm
- 仓库链接：https://github.com/horilla/horilla-crm
- 选择原因：模块较多、业务链路更复杂，能明显暴露 Agent 在跨模块改动时的上下文缺失问题；非常适合训练影响面分析、WIP=1 与分阶段验收。

## 4. koalixcrm
- 仓库链接：https://github.com/KoalixSwitzerland/koalixcrm
- 选择原因：偏 ERP/CRM 的真实业务场景（如单据与流程）适合做“可观测 + 可回归 + 可交接”训练；能系统演练决策记录、变更审计与验收门禁。

## 5. StudX
- 仓库链接：https://github.com/ghrimx/StudX
- 选择原因：学生管理系统具备典型后台信息系统特征（多表关系、增删改查、状态管理）；作为非 CRM 对照案例，便于同一 Harness 方法跨业务域迁移。

## 如何用于实训
建议将 15–30 人分为 5 组，每组负责一个仓库，统一补齐 AGENTS/架构说明/进度与决策记录/测试与 CI 门禁。每周以“可接手性、任务边界清晰度、自动验证通过率、交接质量”作为量化评分维度，最终形成可复用的工程化改造模板。
