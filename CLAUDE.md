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
├── claude-code-101-tutorial.md    # 主教程文档（完整指南）
├── case1-tiktok-analysis/         # 案例：TikTok 直播+短视频运营分析
│   ├── tiktok_data.csv           # 50条直播和视频记录及完整数据
│   ├── generate_data.py          # 数据生成脚本
│   └── README.md                 # 案例说明
└── skills/                        # Skills 目录
    └── live-ops-analytics/        # 直播运营分析 skill
```

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

### 数据生成
案例包含 Python 脚本来重新生成示例数据：
```bash
cd case1-tiktok-analysis
python generate_data.py
```

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
