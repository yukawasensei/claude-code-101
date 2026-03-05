#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HTML 报告验证脚本

验证生成的 HTML 报告是否包含所有必要的元素。
"""

import os
import re
from pathlib import Path


def validate_html_report(html_file):
    """
    验证 HTML 报告的完整性

    Args:
        html_file: HTML 文件路径

    Returns:
        dict: 验证结果
    """
    print("=" * 60)
    print("HTML 报告验证")
    print("=" * 60)

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    results = {}

    # 1. 检查文件大小
    file_size = os.path.getsize(html_file)
    file_size_kb = file_size / 1024
    results['file_size'] = {
        'value': f"{file_size_kb:.1f} KB",
        'pass': file_size_kb < 500,  # 应该小于 500KB
        'expected': '< 500 KB'
    }

    # 2. 检查 CDN 链接
    plotly_cdn = 'cdn.jsdelivr.net/npm/plotly.js' in content
    marked_cdn = 'cdn.jsdelivr.net/npm/marked' in content
    results['cdn_links'] = {
        'value': f"Plotly: {plotly_cdn}, Marked: {marked_cdn}",
        'pass': plotly_cdn and marked_cdn,
        'expected': 'Both CDN links present'
    }

    # 3. 检查核心指标
    metrics_count = content.count('metric-card')
    results['metric_cards'] = {
        'value': metrics_count,
        'pass': metrics_count >= 4,
        'expected': '>= 4'
    }

    # 4. 检查 Tab 按钮
    tab_buttons = content.count('tab-button')
    results['tab_buttons'] = {
        'value': tab_buttons,
        'pass': tab_buttons >= 2,
        'expected': '>= 2'
    }

    # 5. 检查图表容器
    chart_containers = content.count('chart-container')
    results['chart_containers'] = {
        'value': chart_containers,
        'pass': chart_containers >= 5,
        'expected': '>= 5'
    }

    # 6. 检查 Markdown 渲染代码
    markdown_parse = content.count('marked.parse')
    results['markdown_rendering'] = {
        'value': markdown_parse,
        'pass': markdown_parse >= 2,
        'expected': '>= 2'
    }

    # 7. 检查图表渲染代码
    plotly_newplot = content.count('Plotly.newPlot')
    results['chart_rendering'] = {
        'value': plotly_newplot,
        'pass': plotly_newplot >= 1,
        'expected': '>= 1'
    }

    # 8. 检查图表配置数据
    chart_configs = [
        'conversion_by_type',
        'views_vs_conversions',
        'conversion_by_hour',
        'duration_distribution',
        'heatmap_hour_conversion'
    ]
    configs_found = sum(1 for config in chart_configs if config in content)
    results['chart_configs'] = {
        'value': configs_found,
        'pass': configs_found == 5,
        'expected': '5'
    }

    # 9. 检查响应式设计
    responsive_css = '@media' in content
    results['responsive_design'] = {
        'value': responsive_css,
        'pass': responsive_css,
        'expected': 'Media queries present'
    }

    # 10. 检查中文内容
    chinese_content = bool(re.search(r'[\u4e00-\u9fff]', content))
    results['chinese_content'] = {
        'value': chinese_content,
        'pass': chinese_content,
        'expected': 'Chinese characters present'
    }

    # 打印结果
    print("\n验证结果:")
    print("-" * 60)

    all_passed = True
    for test_name, result in results.items():
        status = "✅ PASS" if result['pass'] else "❌ FAIL"
        print(f"{status} | {test_name:25} | {result['value']:20} | 期望: {result['expected']}")
        if not result['pass']:
            all_passed = False

    print("-" * 60)

    if all_passed:
        print("\n🎉 所有验证通过！HTML 报告生成成功。")
    else:
        print("\n⚠️  部分验证失败，请检查报告。")

    print("=" * 60)

    return results, all_passed


def main():
    """主函数"""
    # 获取 HTML 文件路径
    script_dir = Path(__file__).parent
    base_dir = script_dir.parent
    html_file = base_dir / 'tiktok_analysis_report.html'

    if not html_file.exists():
        print(f"❌ 错误: HTML 文件不存在: {html_file}")
        print("请先运行 generate_html_report.py 生成报告。")
        return

    # 验证报告
    results, all_passed = validate_html_report(html_file)

    # 返回退出码
    exit(0 if all_passed else 1)


if __name__ == '__main__':
    main()
