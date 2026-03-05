# CLAUDE.md

本文件为 Claude Code (claude.ai/code) 在此代码库中工作时提供指导。

## 语言要求

**重要：必须始终使用简体中文与用户交流**

- 所有回复、解释、分析都必须使用简体中文
- 代码注释使用简体中文
- 生成的报告使用简体中文
- 错误提示和指导使用简体中文
- 除非用户明确要求使用其他语言，否则一律使用简体中文

## 代码库概述

这是一个面向非技术人员（运营人员、产品经理、数据分析师）的 Claude Code 中文教程代码库，通过实战案例教授如何使用提示词让 Claude Code 自动生成高质量数据分析报告。

**目标用户**：需要数据分析能力的非技术专业人员
**主要语言**：简体中文
**教学重点**：提示词编写、skills 使用、自动化分析

## 代码库结构

```
claude-code-101/
├── README.md                      # 项目总览
├── CLAUDE.md                      # 本文件
├── claude-code-101-tutorial.md    # 主教程文档（完整指南）
├── img/                           # 教程配图
│   ├── warp.png
│   ├── cd-2-project.png
│   ├── cc-switch.png
│   ├── claude-dangerously-skip-permissions.png
│   ├── claude-code-start.png
│   └── dashboard.png
├── attachments/                   # 附件资料
│   ├── commands-cheatsheet.md    # 命令速查表
│   ├── prompt-templates.md       # 提示词模板
│   └── advanced-tips.md          # 进阶技巧
├── case1-tiktok-analysis/         # 案例：TikTok 直播+短视频运营分析
│   ├── README.md                 # 案例说明
│   ├── tiktok_data.csv           # 50条直播和视频记录
│   ├── analysis_report.md        # 示例输出：分析报告
│   └── dashboard.html            # 示例输出：可视化网页
└── skills/                        # Skills 目录
    └── live-ops-analytics/        # 直播运营分析 skill
        ├── SKILL.md              # Skill 定义
        └── references/           # 分析参考文档

## 快速开始

### 安装 Claude Code
```bash
npm install -g @anthropic-ai/claude-code
claude --version
```

### 启动项目
```bash
cd /Users/huangzhipeng/Coding/claude-code-101
claude --dangerously-skip-permissions  # YOLO 模式，减少权限确认
```

### 运行案例
```bash
cd case1-tiktok-analysis
claude --dangerously-skip-permissions
# 然后粘贴教程中的提示词执行
```

## 学习路径

### 路径 A：先看结果（最快）
适合快速建立"结果感知"，了解 Claude Code 能做什么。

```bash
cd case1-tiktok-analysis
cat analysis_report.md      # 查看分析报告
open dashboard.html         # 在浏览器中查看可视化网页
```

### 路径 B：完整复现（推荐）
适合系统学习提示词编写和 skills 使用。

1. 阅读主教程：`claude-code-101-tutorial.md`
2. 进入案例目录：`cd case1-tiktok-analysis`
3. 启动 Claude Code：`claude --dangerously-skip-permissions`
4. 使用教程中的提示词生成报告和网页
5. 对比示例产物，迭代优化提示词

## 教程文档

### 主教程
- `claude-code-101-tutorial.md`：从 0 到 1 的完整操作路径

### 附件资料
- `attachments/commands-cheatsheet.md`：常用命令速查表
- `attachments/prompt-templates.md`：提示词模板和示例
- `attachments/advanced-tips.md`：进阶技巧和最佳实践

### 案例文档
- `case1-tiktok-analysis/README.md`：案例详细说明

## 案例说明

### 案例：TikTok 直播+短视频运营分析
- **数据**：`case1-tiktok-analysis/tiktok_data.csv`（50条记录）
- **目标**：使用提示词让 Claude Code 自动生成深度分析报告和可视化网页
- **技能**：提示词编写、skills 调用、报告生成、数据可视化
- **关键字段**：
  - 基础数据：video_id、title、publish_date、publish_hour、views、likes、comments、shares、duration、video_type、conversions
  - 直播数据：live_uv、peak_online、avg_watch_time、gmv、order_conversion_rate
  - 投流数据：ad_cost、cpm、roi
  - 互动数据：danmu_count、gift_count、follow_conversion_rate

## 使用此代码库

### 分析工作流程
当用户请求数据分析时：
1. **理解需求**：明确用户想要什么样的分析和输出
2. **编写提示词**：清晰、具体、完整地描述需求
3. **调用 skills**：使用 `/live-ops-analytics` 生成分析报告
4. **生成可视化**：使用 `/frontend-design` 生成可视化网页
5. **交付结果**：确保输出符合用户预期

### Python 依赖
分析任务中常用的库：
- pandas（数据处理）
- matplotlib、seaborn、plotly（可视化）
- csv、datetime（数据处理）

## 交流方式

教程面向非技术用户设计，因此解释应该：
- 清晰易懂，避免专业术语
- 必要时提供分步说明
- 关注实际结果
- 强调提示词编写技巧

## 教学重点

### 提示词编写
- 如何清晰描述分析需求
- 如何调用 skills（`/live-ops-analytics`、`/frontend-design`）
- 如何在一个提示词中组合多个需求
- 提供完整的提示词模板和示例

### Skills 使用
- `/live-ops-analytics`：生成深度分析报告
- `/frontend-design`：生成现代化可视化网页
- 如何定制 skills 的输出
- 如何组合使用多个 skills

### 自动化分析
- 一个提示词完成所有分析
- 最小化学习曲线
- 快速上手，立即产出
- 重点展示结果，而不是过程

## 常见问题

### 没有编程基础可以学吗？
可以。本项目重点是"会描述需求"，不是"会写代码"。

### 为什么推荐 `--dangerously-skip-permissions`？
这是高效率模式（YOLO）。教程里用它来减少反复权限确认，但请在可控目录中使用。

### 必须用 TikTok 这份数据吗？
不是。你可以替换为自己的 CSV，只要在提示词里明确字段含义和输出要求。

### 如何定制分析报告？
在提示词中详细描述你想要的分析维度、报告风格、输出格式等，Claude Code 会根据你的要求生成。

## 相关链接

- [Claude Code 官方文档](https://docs.claude.ai/code)
- [Anthropic 官网](https://www.anthropic.com)
