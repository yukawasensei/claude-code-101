#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TikTok 数据分析 HTML 可视化报告生成器

功能：
1. 从现有的 5 个 Plotly HTML 文件中提取图表配置
2. 读取两个 Markdown 报告（analysis_report.md 和 insights.md）
3. 从 CSV 计算核心指标
4. 生成单个完整的 HTML 可视化报告

输出：
- tiktok_analysis_report.html（约 300KB）
"""

import os
import re
import json
import pandas as pd
from pathlib import Path
from datetime import datetime


class HTMLReportGenerator:
    """HTML 报告生成器"""

    def __init__(self, base_dir):
        """
        初始化生成器

        Args:
            base_dir: case1-tiktok-analysis 目录的路径
        """
        self.base_dir = Path(base_dir)
        self.viz_dir = self.base_dir / 'visualizations'
        self.reports_dir = self.base_dir / 'reports'
        self.data_file = self.base_dir / 'tiktok_data.csv'

        # 图表文件映射
        self.chart_files = {
            'conversion_by_type': 'conversion_by_type.html',
            'views_vs_conversions': 'views_vs_conversions.html',
            'conversion_by_hour': 'conversion_by_hour.html',
            'duration_distribution': 'duration_distribution.html',
            'heatmap_hour_conversion': 'heatmap_hour_conversion.html'
        }

        # 存储提取的图表配置
        self.chart_configs = {}

        # 存储 Markdown 报告内容
        self.analysis_report = ""
        self.insights_report = ""

        # 存储核心指标
        self.metrics = {}

    def extract_plotly_config(self, html_file):
        """
        从 HTML 文件中提取 Plotly 图表配置

        Args:
            html_file: HTML 文件路径

        Returns:
            dict: 包含 data、layout、config 的字典
        """
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # 查找 Plotly.newPlot() 调用
        # 格式: Plotly.newPlot("id", [data], {layout}, {config})
        pattern = r'Plotly\.newPlot\(\s*"[^"]+",\s*(\[.*?\]),\s*(\{.*?\}),\s*(\{.*?\})\s*\)'

        # 使用非贪婪匹配，但需要处理嵌套的括号
        # 更安全的方法：找到 Plotly.newPlot 的位置，然后手动解析
        match = re.search(r'Plotly\.newPlot\(\s*"([^"]+)",', content)
        if not match:
            raise ValueError(f"无法在 {html_file} 中找到 Plotly.newPlot 调用")

        # 找到起始位置
        start_pos = match.end()

        # 手动解析三个参数（data, layout, config）
        data_str, layout_str, config_str = self._parse_plotly_args(content[start_pos:])

        return {
            'data': data_str,
            'layout': layout_str,
            'config': config_str
        }

    def _parse_plotly_args(self, content):
        """
        手动解析 Plotly.newPlot 的三个参数

        Args:
            content: 从第一个参数开始的字符串

        Returns:
            tuple: (data_str, layout_str, config_str)
        """
        # 跳过空白字符
        content = content.lstrip()

        # 解析第一个参数（data，应该是数组）
        data_str, remaining = self._extract_json_value(content)

        # 跳过逗号和空白
        remaining = remaining.lstrip().lstrip(',').lstrip()

        # 解析第二个参数（layout，应该是对象）
        layout_str, remaining = self._extract_json_value(remaining)

        # 跳过逗号和空白
        remaining = remaining.lstrip().lstrip(',').lstrip()

        # 解析第三个参数（config，应该是对象）
        config_str, _ = self._extract_json_value(remaining)

        return data_str, layout_str, config_str

    def _extract_json_value(self, content):
        """
        从字符串中提取一个完整的 JSON 值（对象或数组）

        Args:
            content: 字符串内容

        Returns:
            tuple: (json_str, remaining_content)
        """
        # 确定是对象还是数组
        if content.startswith('['):
            open_char, close_char = '[', ']'
        elif content.startswith('{'):
            open_char, close_char = '{', '}'
        else:
            raise ValueError(f"期望 JSON 对象或数组，但得到: {content[:50]}")

        # 计数括号深度
        depth = 0
        in_string = False
        escape_next = False
        end_pos = 0

        for i, char in enumerate(content):
            if escape_next:
                escape_next = False
                continue

            if char == '\\':
                escape_next = True
                continue

            if char == '"' and not escape_next:
                in_string = not in_string
                continue

            if not in_string:
                if char == open_char:
                    depth += 1
                elif char == close_char:
                    depth -= 1
                    if depth == 0:
                        end_pos = i + 1
                        break

        if depth != 0:
            raise ValueError("JSON 括号不匹配")

        json_str = content[:end_pos]
        remaining = content[end_pos:]

        return json_str, remaining

    def load_chart_configs(self):
        """加载所有图表配置"""
        print("正在提取图表配置...")
        for chart_id, filename in self.chart_files.items():
            filepath = self.viz_dir / filename
            print(f"  - 提取 {filename}")
            try:
                config = self.extract_plotly_config(filepath)
                self.chart_configs[chart_id] = config
            except Exception as e:
                print(f"    警告: 提取失败 - {e}")
                self.chart_configs[chart_id] = None

    def load_markdown_reports(self):
        """加载 Markdown 报告"""
        print("正在加载 Markdown 报告...")

        # 加载综合分析报告
        analysis_file = self.reports_dir / 'analysis_report.md'
        with open(analysis_file, 'r', encoding='utf-8') as f:
            self.analysis_report = f.read()
        print(f"  - 已加载 analysis_report.md")

        # 加载行动指南
        insights_file = self.reports_dir / 'insights.md'
        with open(insights_file, 'r', encoding='utf-8') as f:
            self.insights_report = f.read()
        print(f"  - 已加载 insights.md")

    def calculate_metrics(self):
        """从 CSV 计算核心指标"""
        print("正在计算核心指标...")

        # 加载数据
        df = pd.read_csv(self.data_file)

        # 计算总转化量
        total_conversions = df['conversions'].sum()

        # 计算平均转化率
        df['conversion_rate'] = (df['conversions'] / df['views'] * 100).round(2)
        avg_conversion_rate = df['conversion_rate'].mean()

        # 找出最佳视频类型（按平均转化率）
        type_stats = df.groupby('video_type').agg({
            'conversions': 'sum',
            'views': 'sum'
        })
        type_stats['conversion_rate'] = (type_stats['conversions'] / type_stats['views'] * 100).round(2)
        best_type = type_stats['conversion_rate'].idxmax()
        best_type_rate = type_stats['conversion_rate'].max()

        # 找出黄金发布时段（按平均转化率）
        hour_stats = df.groupby('publish_hour').agg({
            'conversions': 'sum',
            'views': 'sum'
        })
        hour_stats['conversion_rate'] = (hour_stats['conversions'] / hour_stats['views'] * 100).round(2)
        best_hour = hour_stats['conversion_rate'].idxmax()
        best_hour_rate = hour_stats['conversion_rate'].max()

        # 存储指标
        self.metrics = {
            'total_conversions': int(total_conversions),
            'avg_conversion_rate': round(avg_conversion_rate, 2),
            'best_type': best_type,
            'best_type_rate': round(best_type_rate, 2),
            'best_hour': int(best_hour),
            'best_hour_rate': round(best_hour_rate, 2),
            'total_videos': len(df),
            'date_range': f"{df['publish_date'].min()} 至 {df['publish_date'].max()}"
        }

        print(f"  - 总转化量: {self.metrics['total_conversions']}")
        print(f"  - 平均转化率: {self.metrics['avg_conversion_rate']}%")
        print(f"  - 最佳类型: {self.metrics['best_type']} ({self.metrics['best_type_rate']}%)")
        print(f"  - 黄金时段: {self.metrics['best_hour']}:00 ({self.metrics['best_hour_rate']}%)")

    def generate_html(self, output_file):
        """
        生成完整的 HTML 报告

        Args:
            output_file: 输出文件路径
        """
        print("正在生成 HTML 报告...")

        # 生成 HTML 内容
        html_content = self._build_html_template()

        # 写入文件
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)

        # 检查文件大小
        file_size = os.path.getsize(output_file)
        file_size_kb = file_size / 1024
        print(f"  - HTML 报告已生成: {output_file}")
        print(f"  - 文件大小: {file_size_kb:.1f} KB")

    def _build_html_template(self):
        """构建完整的 HTML 模板"""
        # 准备数据
        metrics_json = json.dumps(self.metrics, ensure_ascii=False)
        charts_json = json.dumps(self.chart_configs, ensure_ascii=False)

        # 转义 Markdown 内容中的特殊字符
        analysis_escaped = self.analysis_report.replace('`', '\\`').replace('${', '\\${')
        insights_escaped = self.insights_report.replace('`', '\\`').replace('${', '\\${')

        # 生成时间
        generation_time = datetime.now().strftime('%Y年%m月%d日 %H:%M')

        # HTML 模板
        html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TikTok 视频运营数据分析报告</title>

    <!-- 外部库 CDN -->
    <script src="https://cdn.jsdelivr.net/npm/plotly.js@2.27.0/dist/plotly.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/marked@11.0.0/marked.min.js"></script>

    <style>
{self._get_css_styles()}
    </style>
</head>
<body>
    <!-- 导航栏 -->
    <nav class="navbar">
        <div class="nav-container">
            <div class="nav-logo">📊 TikTok 数据分析</div>
            <div class="nav-links">
                <a href="#overview" class="nav-link">概览</a>
                <a href="#reports" class="nav-link">报告</a>
                <a href="#charts" class="nav-link">图表</a>
            </div>
        </div>
    </nav>

    <!-- 英雄区 -->
    <section class="hero">
        <div class="container">
            <h1 class="hero-title">TikTok 视频运营数据分析报告</h1>
            <p class="hero-subtitle">{self.metrics['date_range']} | {self.metrics['total_videos']} 条视频 | {self.metrics['total_conversions']} 次转化</p>
        </div>
    </section>

    <!-- 核心指标卡片 -->
    <section id="overview" class="metrics-section">
        <div class="container">
            <div class="metrics-grid">
                <div class="metric-card">
                    <div class="metric-icon">🎯</div>
                    <div class="metric-value">{self.metrics['total_conversions']}</div>
                    <div class="metric-label">总转化量</div>
                </div>
                <div class="metric-card">
                    <div class="metric-icon">📈</div>
                    <div class="metric-value">{self.metrics['avg_conversion_rate']}%</div>
                    <div class="metric-label">平均转化率</div>
                </div>
                <div class="metric-card">
                    <div class="metric-icon">🏆</div>
                    <div class="metric-value">{self.metrics['best_type']}</div>
                    <div class="metric-label">最佳视频类型</div>
                    <div class="metric-detail">{self.metrics['best_type_rate']}% 转化率</div>
                </div>
                <div class="metric-card">
                    <div class="metric-icon">⏰</div>
                    <div class="metric-value">{self.metrics['best_hour']}:00</div>
                    <div class="metric-label">黄金发布时段</div>
                    <div class="metric-detail">{self.metrics['best_hour_rate']}% 转化率</div>
                </div>
            </div>
        </div>
    </section>

    <!-- Tab 切换区 -->
    <section id="reports" class="reports-section">
        <div class="container">
            <div class="tabs">
                <button class="tab-button active" data-tab="analysis">📊 综合分析</button>
                <button class="tab-button" data-tab="insights">💡 行动指南</button>
            </div>

            <div class="tab-content active" id="analysis-content">
                <div class="markdown-content"></div>
            </div>

            <div class="tab-content" id="insights-content">
                <div class="markdown-content"></div>
            </div>
        </div>
    </section>

    <!-- 交互式图表区 -->
    <section id="charts" class="charts-section">
        <div class="container">
            <h2 class="section-title">交互式数据可视化</h2>
            <p class="section-subtitle">鼠标悬停查看详细数据，点击图例筛选数据，双击重置视图</p>

            <div class="charts-grid">
                <div class="chart-container">
                    <div id="chart-conversion-by-type" class="chart"></div>
                </div>
                <div class="chart-container">
                    <div id="chart-views-vs-conversions" class="chart"></div>
                </div>
                <div class="chart-container">
                    <div id="chart-conversion-by-hour" class="chart"></div>
                </div>
                <div class="chart-container">
                    <div id="chart-duration-distribution" class="chart"></div>
                </div>
                <div class="chart-container full-width">
                    <div id="chart-heatmap-hour-conversion" class="chart"></div>
                </div>
            </div>
        </div>
    </section>

    <!-- 页脚 -->
    <footer class="footer">
        <div class="container">
            <p>生成时间: {generation_time} | 数据来源: TikTok 视频运营数据</p>
        </div>
    </footer>

    <script>
{self._get_javascript_code(analysis_escaped, insights_escaped, metrics_json, charts_json)}
    </script>
</body>
</html>'''

        return html

    def _get_css_styles(self):
        """获取 CSS 样式"""
        return '''
/* CSS 变量 */
:root {
    --primary-color: #2563eb;
    --secondary-color: #10b981;
    --accent-color: #f59e0b;
    --text-primary: #111827;
    --text-secondary: #6b7280;
    --bg-primary: #ffffff;
    --bg-secondary: #f9fafb;
    --border-color: #e5e7eb;
    --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
    --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    --radius-sm: 0.375rem;
    --radius-md: 0.5rem;
    --radius-lg: 0.75rem;
}

/* 全局样式 */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
    color: var(--text-primary);
    background-color: var(--bg-secondary);
    line-height: 1.6;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 1.5rem;
}

/* 导航栏 */
.navbar {
    background-color: var(--bg-primary);
    border-bottom: 1px solid var(--border-color);
    position: sticky;
    top: 0;
    z-index: 1000;
    box-shadow: var(--shadow-sm);
}

.nav-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 1rem 1.5rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.nav-logo {
    font-size: 1.25rem;
    font-weight: 700;
    color: var(--primary-color);
}

.nav-links {
    display: flex;
    gap: 2rem;
}

.nav-link {
    color: var(--text-secondary);
    text-decoration: none;
    font-weight: 500;
    transition: color 0.2s;
}

.nav-link:hover {
    color: var(--primary-color);
}

/* 英雄区 */
.hero {
    background: linear-gradient(135deg, var(--primary-color) 0%, #1e40af 100%);
    color: white;
    padding: 4rem 0;
    text-align: center;
}

.hero-title {
    font-size: 2.5rem;
    font-weight: 700;
    margin-bottom: 1rem;
}

.hero-subtitle {
    font-size: 1.125rem;
    opacity: 0.9;
}

/* 核心指标卡片 */
.metrics-section {
    padding: 3rem 0;
    background-color: var(--bg-primary);
}

.metrics-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
}

.metric-card {
    background-color: var(--bg-primary);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-lg);
    padding: 1.5rem;
    text-align: center;
    transition: transform 0.2s, box-shadow 0.2s;
}

.metric-card:hover {
    transform: translateY(-4px);
    box-shadow: var(--shadow-lg);
}

.metric-icon {
    font-size: 2.5rem;
    margin-bottom: 0.5rem;
}

.metric-value {
    font-size: 2rem;
    font-weight: 700;
    color: var(--primary-color);
    margin-bottom: 0.25rem;
}

.metric-label {
    font-size: 0.875rem;
    color: var(--text-secondary);
    font-weight: 500;
}

.metric-detail {
    font-size: 0.75rem;
    color: var(--text-secondary);
    margin-top: 0.25rem;
}

/* Tab 切换区 */
.reports-section {
    padding: 3rem 0;
}

.tabs {
    display: flex;
    gap: 0.5rem;
    margin-bottom: 2rem;
    border-bottom: 2px solid var(--border-color);
}

.tab-button {
    background: none;
    border: none;
    padding: 1rem 1.5rem;
    font-size: 1rem;
    font-weight: 600;
    color: var(--text-secondary);
    cursor: pointer;
    border-bottom: 3px solid transparent;
    transition: all 0.2s;
}

.tab-button:hover {
    color: var(--primary-color);
}

.tab-button.active {
    color: var(--primary-color);
    border-bottom-color: var(--primary-color);
}

.tab-content {
    display: none;
    animation: fadeIn 0.3s;
}

.tab-content.active {
    display: block;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}

/* Markdown 内容样式 */
.markdown-content {
    background-color: var(--bg-primary);
    border-radius: var(--radius-lg);
    padding: 2rem;
    box-shadow: var(--shadow-sm);
}

.markdown-content h1 {
    font-size: 2rem;
    margin-bottom: 1rem;
    color: var(--text-primary);
    border-bottom: 2px solid var(--primary-color);
    padding-bottom: 0.5rem;
}

.markdown-content h2 {
    font-size: 1.5rem;
    margin-top: 2rem;
    margin-bottom: 1rem;
    color: var(--text-primary);
}

.markdown-content h3 {
    font-size: 1.25rem;
    margin-top: 1.5rem;
    margin-bottom: 0.75rem;
    color: var(--text-primary);
}

.markdown-content p {
    margin-bottom: 1rem;
    line-height: 1.8;
}

.markdown-content ul, .markdown-content ol {
    margin-bottom: 1rem;
    padding-left: 2rem;
}

.markdown-content li {
    margin-bottom: 0.5rem;
}

.markdown-content strong {
    color: var(--primary-color);
    font-weight: 600;
}

.markdown-content code {
    background-color: var(--bg-secondary);
    padding: 0.2rem 0.4rem;
    border-radius: var(--radius-sm);
    font-family: "SF Mono", Monaco, "Cascadia Code", monospace;
    font-size: 0.875rem;
}

.markdown-content pre {
    background-color: var(--bg-secondary);
    padding: 1rem;
    border-radius: var(--radius-md);
    overflow-x: auto;
    margin-bottom: 1rem;
}

.markdown-content table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 1rem;
}

.markdown-content th, .markdown-content td {
    border: 1px solid var(--border-color);
    padding: 0.75rem;
    text-align: left;
}

.markdown-content th {
    background-color: var(--bg-secondary);
    font-weight: 600;
}

/* 图表区 */
.charts-section {
    padding: 3rem 0;
    background-color: var(--bg-primary);
}

.section-title {
    font-size: 2rem;
    font-weight: 700;
    text-align: center;
    margin-bottom: 0.5rem;
}

.section-subtitle {
    text-align: center;
    color: var(--text-secondary);
    margin-bottom: 2rem;
}

.charts-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(500px, 1fr));
    gap: 2rem;
}

.chart-container {
    background-color: var(--bg-primary);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-lg);
    padding: 1.5rem;
    box-shadow: var(--shadow-sm);
}

.chart-container.full-width {
    grid-column: 1 / -1;
}

.chart {
    min-height: 400px;
}

/* 页脚 */
.footer {
    background-color: var(--bg-primary);
    border-top: 1px solid var(--border-color);
    padding: 2rem 0;
    text-align: center;
    color: var(--text-secondary);
    font-size: 0.875rem;
}

/* 响应式设计 */
@media (max-width: 768px) {
    .hero-title {
        font-size: 1.75rem;
    }

    .hero-subtitle {
        font-size: 1rem;
    }

    .metrics-grid {
        grid-template-columns: 1fr;
    }

    .charts-grid {
        grid-template-columns: 1fr;
    }

    .nav-links {
        gap: 1rem;
    }

    .tab-button {
        padding: 0.75rem 1rem;
        font-size: 0.875rem;
    }
}

/* 平滑滚动 */
html {
    scroll-behavior: smooth;
}
'''

    def _get_javascript_code(self, analysis_md, insights_md, metrics_json, charts_json):
        """获取 JavaScript 代码"""
        return f'''
// 数据
const metrics = {metrics_json};
const chartConfigs = {charts_json};
const analysisMarkdown = `{analysis_md}`;
const insightsMarkdown = `{insights_md}`;

// 初始化
document.addEventListener('DOMContentLoaded', function() {{
    initTabs();
    renderMarkdown();
    renderCharts();
    initSmoothScroll();
}});

// Tab 切换
function initTabs() {{
    const tabButtons = document.querySelectorAll('.tab-button');
    const tabContents = document.querySelectorAll('.tab-content');

    tabButtons.forEach(button => {{
        button.addEventListener('click', () => {{
            const tabId = button.getAttribute('data-tab');

            // 移除所有 active 类
            tabButtons.forEach(btn => btn.classList.remove('active'));
            tabContents.forEach(content => content.classList.remove('active'));

            // 添加 active 类
            button.classList.add('active');
            document.getElementById(`${{tabId}}-content`).classList.add('active');

            // 更新 URL hash
            window.location.hash = tabId;
        }});
    }});

    // 根据 URL hash 激活对应的 tab
    const hash = window.location.hash.slice(1);
    if (hash === 'insights') {{
        document.querySelector('[data-tab="insights"]').click();
    }}
}}

// 渲染 Markdown
function renderMarkdown() {{
    // 配置 marked
    marked.setOptions({{
        breaks: true,
        gfm: true
    }});

    // 渲染综合分析
    const analysisContent = document.querySelector('#analysis-content .markdown-content');
    analysisContent.innerHTML = marked.parse(analysisMarkdown);

    // 渲染行动指南
    const insightsContent = document.querySelector('#insights-content .markdown-content');
    insightsContent.innerHTML = marked.parse(insightsMarkdown);
}}

// 渲染图表
function renderCharts() {{
    // 图表 ID 映射
    const chartMap = {{
        'conversion_by_type': 'chart-conversion-by-type',
        'views_vs_conversions': 'chart-views-vs-conversions',
        'conversion_by_hour': 'chart-conversion-by-hour',
        'duration_distribution': 'chart-duration-distribution',
        'heatmap_hour_conversion': 'chart-heatmap-hour-conversion'
    }};

    // 渲染每个图表
    Object.keys(chartMap).forEach(configKey => {{
        const elementId = chartMap[configKey];
        const config = chartConfigs[configKey];

        if (config) {{
            try {{
                // 解析配置
                const data = JSON.parse(config.data);
                const layout = JSON.parse(config.layout);
                const plotConfig = JSON.parse(config.config);

                // 自定义布局
                layout.autosize = true;
                layout.margin = {{ l: 60, r: 40, t: 60, b: 60 }};
                layout.font = {{ family: 'Arial, sans-serif', size: 12 }};

                // 渲染图表
                Plotly.newPlot(elementId, data, layout, plotConfig);

                // 响应式调整
                window.addEventListener('resize', () => {{
                    Plotly.Plots.resize(elementId);
                }});
            }} catch (e) {{
                console.error(`渲染图表失败: ${{configKey}}`, e);
                document.getElementById(elementId).innerHTML =
                    '<div style="padding: 2rem; text-align: center; color: #ef4444;">图表加载失败</div>';
            }}
        }}
    }});
}}

// 平滑滚动
function initSmoothScroll() {{
    document.querySelectorAll('.nav-link').forEach(link => {{
        link.addEventListener('click', function(e) {{
            e.preventDefault();
            const targetId = this.getAttribute('href').slice(1);
            const targetElement = document.getElementById(targetId);

            if (targetElement) {{
                const navbarHeight = document.querySelector('.navbar').offsetHeight;
                const targetPosition = targetElement.offsetTop - navbarHeight - 20;

                window.scrollTo({{
                    top: targetPosition,
                    behavior: 'smooth'
                }});
            }}
        }});
    }});
}}
'''

    def run(self, output_filename='tiktok_analysis_report.html'):
        """
        运行完整的生成流程

        Args:
            output_filename: 输出文件名
        """
        print("=" * 60)
        print("TikTok 数据分析 HTML 报告生成器")
        print("=" * 60)

        # 1. 提取图表配置
        self.load_chart_configs()

        # 2. 加载 Markdown 报告
        self.load_markdown_reports()

        # 3. 计算核心指标
        self.calculate_metrics()

        # 4. 生成 HTML
        output_file = self.base_dir / output_filename
        self.generate_html(output_file)

        print("=" * 60)
        print("✅ 报告生成完成！")
        print(f"📄 文件位置: {output_file}")
        print("=" * 60)

        return output_file


def main():
    """主函数"""
    # 获取脚本所在目录的父目录（case1-tiktok-analysis）
    script_dir = Path(__file__).parent
    base_dir = script_dir.parent

    # 创建生成器
    generator = HTMLReportGenerator(base_dir)

    # 运行生成流程
    output_file = generator.run()

    # 提示用户如何打开
    print("\n💡 提示:")
    print(f"   在浏览器中打开: open {output_file}")
    print(f"   或直接双击文件: {output_file}")


if __name__ == '__main__':
    main()

