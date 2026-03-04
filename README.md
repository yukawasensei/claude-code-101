# Claude Code 101 教程

欢迎来到 Claude Code 101 教程！这是一个面向非技术背景人员的 Claude Code 入门教程，通过两个实战案例帮助你快速掌握 Claude Code 的核心功能。

## 📚 教程简介

本教程专为以下人群设计：
- 运营人员
- 产品经理
- 数据分析师
- 项目经理
- 其他非技术背景但需要数据分析能力的人员

**学习目标**：
- 掌握 Claude Code 的基本操作
- 学会使用 Claude Code 进行数据分析
- 学会生成可视化图表和报告
- 提升数据驱动决策能力

## 📖 教程结构

### 主教程文档
- **[claude-code-101-tutorial.md](./claude-code-101-tutorial.md)** - 完整的教程文档，包含：
  - Claude Code 基础知识
  - 数据分析工作流程
  - 提示词编写技巧
  - 两个完整的实战案例
  - 常见问题解答

### 实战案例

#### Case 1: TikTok 数据分析
**目录**: `case1-tiktok-analysis/`

分析 TikTok 视频数据，找出高转化视频的特征。

**包含内容**：
- 50 条 TikTok 视频数据（CSV 格式）
- 数据生成脚本
- 详细的案例说明

**学习重点**：
- 数据探索和清洗
- 数据可视化
- 相关性分析
- 生成分析报告

#### Case 2: 项目健康度评估
**目录**: `case2-project-health/`

分析软件项目的健康状况，识别潜在风险。

**包含内容**：
- 项目文档（PRD、技术决策记录）
- 8 周会议纪要
- 用户反馈数据（100 条）
- 项目进度数据
- 数据生成脚本

**学习重点**：
- 多源数据整合
- 趋势分析
- 风险识别
- 综合报告生成

### 提示词模板库
**目录**: `templates/`

包含常用的提示词模板，帮助你快速上手：
- 数据分析模板
- 可视化模板
- 报告生成模板

## 🚀 快速开始

### 1. 安装 Claude Code

```bash
# macOS/Linux
curl -fsSL https://claude.ai/install.sh | sh

# 或使用 npm
npm install -g @anthropic-ai/claude-code
```

### 2. 启动 Claude Code

```bash
cd claude-code-101
claude
```

### 3. 开始学习

1. 阅读主教程文档：`claude-code-101-tutorial.md`
2. 完成 Case 1：TikTok 数据分析
3. 完成 Case 2：项目健康度评估
4. 参考提示词模板库进行实践

## 📁 项目结构

```
claude-code-101/
├── README.md                          # 项目总览（本文件）
├── claude-code-101-tutorial.md       # 主教程文档
├── case1-tiktok-analysis/             # Case 1：TikTok 数据分析
│   ├── README.md                      # Case 1 说明
│   ├── tiktok_data.csv                # 示例数据
│   └── generate_data.py               # 数据生成脚本
├── case2-project-health/              # Case 2：项目健康度分析
│   ├── README.md                      # Case 2 说明
│   ├── docs/                          # 项目文档
│   │   ├── PRD.md                     # 产品需求文档
│   │   ├── decisions.md               # 技术决策记录
│   │   └── meeting-notes/             # 会议纪要（8周）
│   ├── data/                          # 项目数据
│   │   ├── user-feedback.csv          # 用户反馈
│   │   └── progress.csv               # 项目进度
│   └── scripts/                       # 脚本文件
│       ├── generate_files.py          # 文件生成脚本
│       └── analyze.py                 # 分析脚本示例
└── templates/                         # 提示词模板库
    ├── data-analysis-templates.md     # 数据分析模板
    ├── visualization-templates.md     # 可视化模板
    └── report-templates.md            # 报告生成模板
```

## 💡 使用建议

1. **循序渐进**：先完成 Case 1，再挑战 Case 2
2. **动手实践**：不要只看教程，一定要亲自操作
3. **理解原理**：理解提示词的编写逻辑，而不是死记硬背
4. **举一反三**：尝试将学到的技能应用到自己的工作中
5. **参考模板**：遇到问题时查看提示词模板库

## 🎯 学习路径

### 初级（1-2 小时）
- 阅读教程第 1-3 章
- 完成 Case 1 的基础分析
- 学会生成简单的可视化图表

### 中级（3-5 小时）
- 阅读教程第 4-5 章
- 完成 Case 1 的完整分析
- 开始 Case 2 的数据探索

### 高级（6-8 小时）
- 完成 Case 2 的完整分析
- 尝试自定义分析维度
- 将技能应用到实际工作中

## 📝 常见问题

### Q: 我完全没有编程基础，能学会吗？
A: 可以！本教程专为非技术人员设计，不需要编程基础。Claude Code 会帮你生成和执行代码。

### Q: 需要安装 Python 吗？
A: 是的，Claude Code 需要 Python 环境。教程中有详细的安装说明。

### Q: 学完后能做什么？
A: 你将能够：
- 独立完成数据分析任务
- 生成专业的数据可视化图表
- 撰写数据驱动的分析报告
- 提升工作效率和决策质量

### Q: 遇到问题怎么办？
A:
1. 查看教程的"常见问题"章节
2. 参考提示词模板库
3. 尝试用不同的方式描述你的需求

## 🔗 相关资源

- [Claude Code 官方文档](https://docs.claude.ai/code)
- [Claude Code GitHub](https://github.com/anthropics/claude-code)
- [Anthropic 官网](https://www.anthropic.com)

## 📄 许可证

本教程采用 MIT 许可证。你可以自由使用、修改和分享本教程内容。

## 🙏 致谢

感谢所有为本教程提供反馈和建议的朋友们！

---

**开始学习**: 打开 [claude-code-101-tutorial.md](./claude-code-101-tutorial.md) 开始你的 Claude Code 之旅！
