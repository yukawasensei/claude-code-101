#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TikTok 视频可视化生成脚本
目标：生成 5 个交互式 Plotly 图表（HTML 格式）
"""

import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import os

def load_and_prepare_data():
    """加载并准备数据"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(os.path.dirname(script_dir), 'tiktok_data.csv')

    df = pd.read_csv(data_path)

    # 计算衍生指标
    df['like_rate'] = (df['likes'] / df['views'] * 100).round(2)
    df['comment_rate'] = (df['comments'] / df['views'] * 100).round(2)
    df['share_rate'] = (df['shares'] / df['views'] * 100).round(2)
    df['conversion_rate'] = (df['conversions'] / df['views'] * 100).round(2)

    return df

def create_conversion_by_type(df, output_dir):
    """图表 1：各视频类型总转化量（柱状图）"""
    print("生成图表 1：各视频类型转化量...")

    type_conversions = df.groupby('video_type')['conversions'].sum().sort_values(ascending=False)

    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A']

    fig = go.Figure(data=[
        go.Bar(
            x=type_conversions.index,
            y=type_conversions.values,
            marker_color=colors,
            text=type_conversions.values,
            textposition='outside',
            texttemplate='%{text}',
            hovertemplate='<b>%{x}</b><br>转化量: %{y}<extra></extra>'
        )
    ])

    fig.update_layout(
        title='各视频类型总转化量对比',
        xaxis_title='视频类型',
        yaxis_title='总转化量',
        font=dict(family='Arial, sans-serif', size=14),
        hovermode='x',
        height=500,
        template='plotly_white'
    )

    output_path = os.path.join(output_dir, 'conversion_by_type.html')
    fig.write_html(output_path)
    print(f"  ✓ 已保存：{output_path}")

def create_views_vs_conversions(df, output_dir):
    """图表 2：播放量 vs 转化量（散点图）"""
    print("生成图表 2：播放量与转化量关系...")

    fig = px.scatter(
        df,
        x='views',
        y='conversions',
        color='video_type',
        size='conversion_rate',
        hover_data=['title', 'publish_hour', 'duration'],
        labels={
            'views': '播放量',
            'conversions': '转化量',
            'video_type': '视频类型',
            'conversion_rate': '转化率(%)'
        },
        title='播放量与转化量关系（气泡大小=转化率）',
        color_discrete_sequence=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A']
    )

    # 添加趋势线
    from scipy import stats
    slope, intercept, r_value, p_value, std_err = stats.linregress(df['views'], df['conversions'])
    line_x = np.array([df['views'].min(), df['views'].max()])
    line_y = slope * line_x + intercept

    fig.add_trace(go.Scatter(
        x=line_x,
        y=line_y,
        mode='lines',
        name=f'趋势线 (R²={r_value**2:.3f})',
        line=dict(color='gray', dash='dash')
    ))

    fig.update_layout(
        font=dict(family='Arial, sans-serif', size=14),
        height=600,
        template='plotly_white'
    )

    output_path = os.path.join(output_dir, 'views_vs_conversions.html')
    fig.write_html(output_path)
    print(f"  ✓ 已保存：{output_path}")

def create_conversion_by_hour(df, output_dir):
    """图表 3：发布时间与转化量（折线图）"""
    print("生成图表 3：发布时间与转化量...")

    hour_data = df.groupby('publish_hour').agg({
        'conversions': ['sum', 'mean'],
        'video_id': 'count'
    }).reset_index()

    hour_data.columns = ['hour', 'total_conversions', 'avg_conversions', 'video_count']

    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # 平均转化量
    fig.add_trace(
        go.Scatter(
            x=hour_data['hour'],
            y=hour_data['avg_conversions'],
            mode='lines+markers',
            name='平均转化量',
            line=dict(color='#FF6B6B', width=3),
            marker=dict(size=8)
        ),
        secondary_y=False
    )

    # 视频数量
    fig.add_trace(
        go.Bar(
            x=hour_data['hour'],
            y=hour_data['video_count'],
            name='视频数量',
            marker_color='#E8E8E8',
            opacity=0.5
        ),
        secondary_y=True
    )

    # 标记峰值时段
    peak_hours = hour_data.nlargest(3, 'avg_conversions')
    for _, row in peak_hours.iterrows():
        fig.add_annotation(
            x=row['hour'],
            y=row['avg_conversions'],
            text=f"{row['avg_conversions']:.1f}",
            showarrow=True,
            arrowhead=2,
            arrowcolor='#FF6B6B',
            font=dict(size=12, color='#FF6B6B')
        )

    fig.update_layout(
        title='各发布时间平均转化量（标注峰值时段）',
        xaxis_title='发布时间（小时）',
        font=dict(family='Arial, sans-serif', size=14),
        height=500,
        template='plotly_white',
        hovermode='x unified'
    )

    fig.update_yaxes(title_text='平均转化量', secondary_y=False)
    fig.update_yaxes(title_text='视频数量', secondary_y=True)

    output_path = os.path.join(output_dir, 'conversion_by_hour.html')
    fig.write_html(output_path)
    print(f"  ✓ 已保存：{output_path}")

def create_duration_distribution(df, output_dir):
    """图表 4：视频时长分布（直方图）"""
    print("生成图表 4：视频时长分布...")

    # 创建时长区间
    df['duration_range'] = pd.cut(df['duration'],
                                   bins=[0, 60, 120, 180, 300],
                                   labels=['15-60秒', '60-120秒', '120-180秒', '180-300秒'])

    duration_stats = df.groupby('duration_range').agg({
        'video_id': 'count',
        'conversion_rate': 'mean'
    }).reset_index()
    duration_stats.columns = ['duration_range', 'count', 'avg_conversion_rate']

    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # 视频数量
    fig.add_trace(
        go.Bar(
            x=duration_stats['duration_range'].astype(str),
            y=duration_stats['count'],
            name='视频数量',
            marker_color='#4ECDC4',
            text=duration_stats['count'],
            textposition='outside'
        ),
        secondary_y=False
    )

    # 平均转化率
    fig.add_trace(
        go.Scatter(
            x=duration_stats['duration_range'].astype(str),
            y=duration_stats['avg_conversion_rate'],
            mode='lines+markers',
            name='平均转化率(%)',
            line=dict(color='#FF6B6B', width=3),
            marker=dict(size=12),
            yaxis='y2'
        ),
        secondary_y=True
    )

    fig.update_layout(
        title='视频时长分布与转化率',
        xaxis_title='视频时长区间',
        font=dict(family='Arial, sans-serif', size=14),
        height=500,
        template='plotly_white',
        hovermode='x unified'
    )

    fig.update_yaxes(title_text='视频数量', secondary_y=False)
    fig.update_yaxes(title_text='平均转化率(%)', secondary_y=True)

    output_path = os.path.join(output_dir, 'duration_distribution.html')
    fig.write_html(output_path)
    print(f"  ✓ 已保存：{output_path}")

def create_heatmap_hour_conversion(df, output_dir):
    """图表 5：发布时间 × 视频类型转化率热力图"""
    print("生成图表 5：时间-类型转化率热力图...")

    # 创建透视表
    pivot_data = df.pivot_table(
        values='conversion_rate',
        index='video_type',
        columns='publish_hour',
        aggfunc='mean'
    ).fillna(0)

    # 创建热力图
    fig = go.Figure(data=go.Heatmap(
        z=pivot_data.values,
        x=pivot_data.columns,
        y=pivot_data.index,
        colorscale='RdYlGn',
        text=np.round(pivot_data.values, 2),
        texttemplate='%{text}%',
        textfont={"size": 10},
        colorbar=dict(title='转化率(%)')
    ))

    fig.update_layout(
        title='各视频类型在不同发布时间的转化率热力图',
        xaxis_title='发布时间（小时）',
        yaxis_title='视频类型',
        font=dict(family='Arial, sans-serif', size=14),
        height=500,
        template='plotly_white'
    )

    output_path = os.path.join(output_dir, 'heatmap_hour_conversion.html')
    fig.write_html(output_path)
    print(f"  ✓ 已保存：{output_path}")

def main():
    """主函数"""
    print("=" * 80)
    print("TikTok 视频数据可视化生成")
    print("=" * 80)
    print()

    # 加载数据
    df = load_and_prepare_data()

    # 确定输出目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(os.path.dirname(script_dir), 'visualizations')

    # 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)

    # 生成各个图表
    create_conversion_by_type(df, output_dir)
    create_views_vs_conversions(df, output_dir)
    create_conversion_by_hour(df, output_dir)
    create_duration_distribution(df, output_dir)
    create_heatmap_hour_conversion(df, output_dir)

    print("\n" + "=" * 80)
    print("可视化生成完成！")
    print("=" * 80)
    print(f"\n共生成 5 个交互式图表，保存在：{output_dir}")
    print("\n可在浏览器中打开以下文件查看：")
    print("  1. conversion_by_type.html - 各类型转化量对比")
    print("  2. views_vs_conversions.html - 播放量与转化量关系")
    print("  3. conversion_by_hour.html - 发布时间与转化量")
    print("  4. duration_distribution.html - 视频时长分布")
    print("  5. heatmap_hour_conversion.html - 时间-类型转化率热力图")
    print()

if __name__ == "__main__":
    main()
