# TikTok 数据分析 HTML 报告生成器

## 概述

这个脚本将 TikTok 数据分析的 Markdown 报告和 Plotly 可视化图表整合成一个完整的、交互式的 HTML 报告。

## 功能特点

- ✅ **单个文件**：所有内容整合在一个 HTML 文件中（约 100KB）
- ✅ **交互式图表**：5 个 Plotly 交互式图表，支持鼠标悬停、缩放、筛选
- ✅ **完整报告**：包含综合分析和行动指南两个完整的 Markdown 报告
- ✅ **核心指标**：4 个关键指标卡片（总转化量、平均转化率、最佳类型、黄金时段）
- ✅ **简约设计**：专业的蓝色主题，响应式布局
- ✅ **文件优化**：从 23MB（5 个独立 HTML）减少到 100KB（99.6% 减少）

## 使用方法

### 1. 激活虚拟环境

```bash
cd /Users/huangzhipeng/Coding/claude-code-101/case1-tiktok-analysis
source venv/bin/activate
```

### 2. 运行生成脚本

```bash
python scripts/generate_html_report.py
```

### 3. 在浏览器中打开报告

```bash
open tiktok_analysis_report.html
```

或者直接双击 `tiktok_analysis_report.html` 文件。

## 输出文件

生成的 HTML 报告包含以下部分：

1. **导航栏**：快速跳转到概览、报告、图表区域
2. **英雄区**：报告标题和数据概览
3. **核心指标卡片**：4 个关键指标的可视化展示
4. **Tab 切换区**：
   - 📊 综合分析（analysis_report.md）
   - 💡 行动指南（insights.md）
5. **交互式图表区**：5 个 Plotly 图表
   - 各视频类型转化量对比
   - 播放量与转化量关系
   - 发布时间与转化量
   - 视频时长分布与转化率
   - 时间-类型转化率热力图
6. **页脚**：生成时间和数据来源

## 技术实现

### 依赖库

- **Python 标准库**：os, re, json, pathlib, datetime
- **pandas**：数据处理和指标计算
- **CDN 加载**：
  - Plotly.js 2.27.0（图表渲染）
  - Marked.js 11.0.0（Markdown 渲染）

### 文件结构

```
case1-tiktok-analysis/
├── scripts/
│   ├── generate_html_report.py  # 生成脚本
│   └── README_HTML_REPORT.md    # 本文件
├── reports/
│   ├── analysis_report.md       # 综合分析报告
│   └── insights.md              # 行动指南
├── visualizations/
│   ├── conversion_by_type.html  # 原始图表 1
│   ├── views_vs_conversions.html # 原始图表 2
│   ├── conversion_by_hour.html  # 原始图表 3
│   ├── duration_distribution.html # 原始图表 4
│   └── heatmap_hour_conversion.html # 原始图表 5
├── tiktok_data.csv              # 原始数据
└── tiktok_analysis_report.html  # 生成的报告（输出）
```

## 工作原理

1. **提取图表配置**：从 5 个现有的 Plotly HTML 文件中提取图表配置（data、layout、config）
2. **读取 Markdown 报告**：加载两个 Markdown 报告文件
3. **计算核心指标**：从 CSV 数据计算总转化量、平均转化率、最佳类型、黄金时段
4. **生成 HTML**：将所有内容整合到一个 HTML 文件中，使用 CDN 加载外部库

## 性能优化

- **文件体积**：使用 CDN 加载 Plotly.js 和 Marked.js，避免重复嵌入库代码
- **加载速度**：首屏快速加载，图表按需渲染
- **响应式设计**：支持桌面、平板、移动端

## 自定义

### 修改颜色主题

编辑 `_get_css_styles()` 方法中的 CSS 变量：

```css
:root {
    --primary-color: #2563eb;  /* 主色调 */
    --secondary-color: #10b981; /* 辅助色 */
    --accent-color: #f59e0b;   /* 强调色 */
}
```

### 修改图表样式

编辑 `_get_javascript_code()` 方法中的图表配置：

```javascript
layout.autosize = true;
layout.margin = { l: 60, r: 40, t: 60, b: 60 };
layout.font = { family: 'Arial, sans-serif', size: 12 };
```

## 故障排除

### 问题：pandas 模块未找到

**解决方案**：确保在虚拟环境中运行脚本

```bash
source venv/bin/activate
pip install pandas
```

### 问题：图表无法显示

**解决方案**：检查网络连接，确保可以访问 CDN

- Plotly.js CDN: https://cdn.jsdelivr.net/npm/plotly.js@2.27.0/dist/plotly.min.js
- Marked.js CDN: https://cdn.jsdelivr.net/npm/marked@11.0.0/marked.min.js

### 问题：Markdown 渲染异常

**解决方案**：检查 Markdown 文件编码是否为 UTF-8

```bash
file -I reports/analysis_report.md
file -I reports/insights.md
```

## 版本历史

- **v1.0.0** (2026-03-04)
  - 初始版本
  - 支持 5 个 Plotly 图表
  - 支持 2 个 Markdown 报告
  - 核心指标卡片
  - Tab 切换功能
  - 响应式设计

## 许可证

MIT License

## 作者

Claude Code 101 教程项目
