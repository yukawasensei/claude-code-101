# Claude Code 101 教程

面向非技术背景用户的 Claude Code 入门项目。你可以用一份真实感较强的 TikTok 运营数据，完整体验：
- 提示词驱动的数据分析
- 自动生成管理层可读报告
- 自动生成可视化仪表盘网页

## 你将得到什么

- 主教程文档：从 0 到 1 的完整操作路径
- Case 1 实战：可直接复现的数据分析案例
- 示例产物：`analysis_report.md` + `dashboard.html`
- 常用附件：命令速查、提示词模板、进阶技巧

## 项目结构（当前）

```text
claude-code-101/
├── README.md
├── claude-code-101-tutorial.md
├── CLAUDE.md
├── img/
│   ├── warp.png
│   ├── cd-2-project.png
│   ├── cc-switch.png
│   ├── claude-dangerously-skip-permissions.png
│   ├── claude-code-start.png
│   └── dashboard.png
├── attachments/
│   ├── commands-cheatsheet.md
│   ├── prompt-templates.md
│   └── advanced-tips.md
├── case1-tiktok-analysis/
│   ├── README.md
│   ├── tiktok_data.csv
│   ├── analysis_report.md
│   └── dashboard.html
└── skills/
    └── live-ops-analytics/
```

## 快速开始

### 1) 安装 Claude Code

```bash
npm install -g @anthropic-ai/claude-code
claude --version
```

### 2) 打开主教程

先阅读主教程：[`claude-code-101-tutorial.md`](./claude-code-101-tutorial.md)

### 3) 运行 Case 1（推荐）

```bash
cd case1-tiktok-analysis
claude --dangerously-skip-permissions
```

进入 Claude Code 后，粘贴教程里 `5.3` 的完整提示词执行。

## 两种学习路径

### 路径 A：先看现成结果（最快）

```bash
cd case1-tiktok-analysis
cat analysis_report.md
open dashboard.html
```

适合先建立“结果感知”，再回头学习提示词结构。

### 路径 B：完整复现（推荐）

1. 按主教程完成环境准备与启动。
2. 使用 `5.3` 提示词生成报告和网页。
3. 对比 `case1-tiktok-analysis/` 中的示例产物，迭代你的提示词。

## 教程阅读顺序

1. [`claude-code-101-tutorial.md`](./claude-code-101-tutorial.md)
2. [`attachments/commands-cheatsheet.md`](./attachments/commands-cheatsheet.md)
3. [`attachments/prompt-templates.md`](./attachments/prompt-templates.md)
4. [`attachments/advanced-tips.md`](./attachments/advanced-tips.md)
5. [`case1-tiktok-analysis/README.md`](./case1-tiktok-analysis/README.md)

## 适用人群

- 运营
- 产品经理
- 数据分析师
- 非技术背景、但需要快速产出分析报告的人

## 常见问题

### 没有编程基础可以学吗？
可以。本项目重点是“会描述需求”，不是“会写代码”。

### 为什么推荐 `--dangerously-skip-permissions`？
这是高效率模式（YOLO）。教程里用它来减少反复权限确认，但请在可控目录中使用。

### 必须用 TikTok 这份数据吗？
不是。你可以替换为自己的 CSV，只要在提示词里明确字段含义和输出要求。

## 相关链接

- [Claude Code 官方文档](https://docs.claude.ai/code)
- [Anthropic 官网](https://www.anthropic.com)

---

从这里开始：[`claude-code-101-tutorial.md`](./claude-code-101-tutorial.md)
