#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TikTok 视频统计分析脚本
目标：深入分析视频类型、发布时间、时长、互动指标与转化的关系
"""

import pandas as pd
import numpy as np
import os

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

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

def analyze_video_types(df):
    """分析视频类型"""
    print("=" * 80)
    print("1. 视频类型分析")
    print("=" * 80)

    type_analysis = df.groupby('video_type').agg({
        'video_id': 'count',
        'views': ['sum', 'mean'],
        'conversions': ['sum', 'mean'],
        'conversion_rate': 'mean',
        'like_rate': 'mean',
        'share_rate': 'mean'
    }).round(2)

    type_analysis.columns = ['视频数量', '总播放量', '平均播放量', '总转化量', '平均转化量',
                             '平均转化率(%)', '平均点赞率(%)', '平均分享率(%)']

    print("\n各类型视频表现：")
    print(type_analysis.sort_values('总转化量', ascending=False))

    print("\n关键发现：")
    best_type = type_analysis['总转化量'].idxmax()
    best_rate_type = type_analysis['平均转化率(%)'].idxmax()
    print(f"  • 转化量最高：{best_type}（{type_analysis.loc[best_type, '总转化量']:.0f} 次转化）")
    print(f"  • 转化率最高：{best_rate_type}（{type_analysis.loc[best_rate_type, '平均转化率(%)']:.2f}%）")

def analyze_publish_time(df):
    """分析发布时间"""
    print("\n" + "=" * 80)
    print("2. 发布时间分析")
    print("=" * 80)

    hour_analysis = df.groupby('publish_hour').agg({
        'video_id': 'count',
        'conversions': ['sum', 'mean'],
        'conversion_rate': 'mean',
        'views': 'mean'
    }).round(2)

    hour_analysis.columns = ['视频数量', '总转化量', '平均转化量', '平均转化率(%)', '平均播放量']

    print("\n按发布时间统计（前 10 个时段）：")
    print(hour_analysis.sort_values('总转化量', ascending=False).head(10))

    # 识别黄金时段（转化量前 30%）
    threshold = hour_analysis['总转化量'].quantile(0.7)
    golden_hours = hour_analysis[hour_analysis['总转化量'] >= threshold].index.tolist()

    print(f"\n黄金发布时段（转化量前 30%）：{sorted(golden_hours)} 点")

    # 时段分类
    morning = df[df['publish_hour'].between(6, 11)]
    afternoon = df[df['publish_hour'].between(12, 17)]
    evening = df[df['publish_hour'].between(18, 23)]
    night = df[df['publish_hour'].between(0, 5)]

    print("\n时段对比：")
    print(f"  • 早晨 (6-11点): 平均转化 {morning['conversions'].mean():.1f}, 转化率 {morning['conversion_rate'].mean():.2f}%")
    print(f"  • 下午 (12-17点): 平均转化 {afternoon['conversions'].mean():.1f}, 转化率 {afternoon['conversion_rate'].mean():.2f}%")
    print(f"  • 晚间 (18-23点): 平均转化 {evening['conversions'].mean():.1f}, 转化率 {evening['conversion_rate'].mean():.2f}%")
    print(f"  • 深夜 (0-5点): 平均转化 {night['conversions'].mean():.1f}, 转化率 {night['conversion_rate'].mean():.2f}%")

def analyze_duration(df):
    """分析视频时长"""
    print("\n" + "=" * 80)
    print("3. 视频时长分析")
    print("=" * 80)

    # 创建时长区间
    df['duration_range'] = pd.cut(df['duration'],
                                   bins=[0, 60, 120, 180, 300],
                                   labels=['15-60秒', '60-120秒', '120-180秒', '180-300秒'])

    duration_analysis = df.groupby('duration_range').agg({
        'video_id': 'count',
        'conversions': ['sum', 'mean'],
        'conversion_rate': 'mean',
        'views': 'mean'
    }).round(2)

    duration_analysis.columns = ['视频数量', '总转化量', '平均转化量', '平均转化率(%)', '平均播放量']

    print("\n按时长区间统计：")
    print(duration_analysis)

    best_duration = duration_analysis['平均转化率(%)'].idxmax()
    print(f"\n最佳时长区间：{best_duration}（平均转化率 {duration_analysis.loc[best_duration, '平均转化率(%)']:.2f}%）")

def analyze_engagement(df):
    """分析互动指标"""
    print("\n" + "=" * 80)
    print("4. 互动指标与转化关系")
    print("=" * 80)

    # 计算相关系数
    engagement_cols = ['likes', 'comments', 'shares', 'like_rate', 'comment_rate', 'share_rate']
    correlations = df[engagement_cols + ['conversions']].corr()['conversions'].drop('conversions')

    print("\n互动指标与转化量的相关系数：")
    print(correlations.sort_values(ascending=False))

    # 高互动视频分析
    high_share = df[df['share_rate'] > df['share_rate'].quantile(0.75)]
    print(f"\n高分享率视频（前 25%）：")
    print(f"  • 数量：{len(high_share)} 条")
    print(f"  • 平均转化：{high_share['conversions'].mean():.1f}")
    print(f"  • 平均转化率：{high_share['conversion_rate'].mean():.2f}%")

    print("\n关键发现：")
    strongest = correlations.idxmax()
    print(f"  • 与转化最相关的指标：{strongest}（相关系数 {correlations[strongest]:.3f}）")

def analyze_top_performers(df):
    """分析高性能视频"""
    print("\n" + "=" * 80)
    print("5. 高转化视频分析")
    print("=" * 80)

    # Top 10 转化率
    top_rate = df.nlargest(10, 'conversion_rate')[['video_id', 'title', 'video_type',
                                                     'publish_hour', 'duration',
                                                     'views', 'conversions', 'conversion_rate']]

    print("\nTop 10 转化率视频：")
    print(top_rate.to_string(index=False))

    # Top 10 绝对转化量
    top_conversions = df.nlargest(10, 'conversions')[['video_id', 'title', 'video_type',
                                                        'publish_hour', 'duration',
                                                        'views', 'conversions', 'conversion_rate']]

    print("\n\nTop 10 转化量视频：")
    print(top_conversions.to_string(index=False))

    # 提取共同特征
    top_20 = df.nlargest(20, 'conversions')

    print("\n\nTop 20 高转化视频共同特征：")
    print(f"  • 主要类型：{top_20['video_type'].mode()[0]}（{(top_20['video_type'] == top_20['video_type'].mode()[0]).sum()} 条）")
    print(f"  • 平均时长：{top_20['duration'].mean():.0f} 秒")
    print(f"  • 常见发布时段：{top_20['publish_hour'].mode().tolist()}")
    print(f"  • 平均分享率：{top_20['share_rate'].mean():.2f}%")

    # 标题特征分析
    print("\n  • 标题特征：")
    title_patterns = {
        '数字型': top_20['title'].str.contains(r'\d+').sum(),
        '效果型': top_20['title'].str.contains('学会|零失败|好用|值得').sum(),
        '痛点型': top_20['title'].str.contains('如何|怎么|为什么').sum(),
        '对比型': top_20['title'].str.contains('vs|对比|测评').sum()
    }
    for pattern, count in sorted(title_patterns.items(), key=lambda x: x[1], reverse=True):
        if count > 0:
            print(f"    - {pattern}：{count} 条")

def main():
    """主函数"""
    print("=" * 80)
    print("TikTok 视频统计分析")
    print("=" * 80)
    print()

    # 加载数据
    df = load_and_prepare_data()

    # 执行各项分析
    analyze_video_types(df)
    analyze_publish_time(df)
    analyze_duration(df)
    analyze_engagement(df)
    analyze_top_performers(df)

    print("\n" + "=" * 80)
    print("统计分析完成！")
    print("=" * 80)
    print()

if __name__ == "__main__":
    main()
