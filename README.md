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
- 提示词编写技巧
- 使用 skills 自动生成分析报告
- 数据可视化仪表盘
- 高质量报告生成

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
3. 应用到自己的实际工作场景

## 📁 项目结构

```
claude-code-101/
├── README.md                          # 项目总览（本文件）
├── claude-code-101-tutorial.md       # 主教程文档
├── CLAUDE.md                          # Claude Code 项目指导
├── case1-tiktok-analysis/             # Case 1：TikTok 数据分析
│   ├── README.md                      # Case 1 说明
│   ├── tiktok_data.csv                # 示例数据
│   └── generate_data.py               # 数据生成脚本
└── skills/                            # Skills 目录
    └── live-ops-analytics/            # 直播运营分析 skill
```

## 💡 使用建议

1. **快速上手**：教程聚焦于提示词编写，让你快速掌握核心技能
2. **动手实践**：不要只看教程，一定要亲自操作
3. **理解原理**：理解提示词的编写逻辑，而不是死记硬背
4. **举一反三**：尝试将学到的技能应用到自己的工作中

## 🎯 学习路径

### 快速入门（1-2 小时）
- 阅读教程第 1-4 章
- 了解 Claude Code 基础操作
- 学会编写基本提示词

### 实战应用（2-3 小时）
- 完成 Case 1 的完整分析
- 学会使用 skills 生成报告
- 掌握数据可视化技巧

### 进阶提升（持续）
- 将技能应用到实际工作中
- 探索更多 skills 和高级功能
- 优化和定制自己的分析流程

## 📝 常见问题

### Q: 我完全没有编程基础，能学会吗？
A: 可以！本教程专为非技术人员设计，不需要编程基础。Claude Code 会帮你生成和执行代码。

### Q: 需要安装 Python 吗？
A: 是的，Claude Code 需要 Python 环境。教程中有详细的安装说明。

### Q: 学完后能做什么？
A: 你将能够：
- 使用提示词让 Claude Code 自动完成数据分析
- 生成专业的数据可视化图表和仪表盘
- 撰写数据驱动的分析报告
- 提升工作效率和决策质量

### Q: 遇到问题怎么办？
A:
1. 查看教程的"常见问题"章节
2. 尝试用不同的方式描述你的需求
3. 参考教程中的提示词示例

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
