#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TikTok 视频数据探索脚本
目标：加载数据、检查数据质量、计算基础指标
"""

import pandas as pd
import numpy as np
import os

# 设置显示选项
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', 50)

def load_data():
    """加载 TikTok 视频数据"""
    # 获取数据文件路径
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(os.path.dirname(script_dir), 'tiktok_data.csv')

    print("=" * 80)
    print("TikTok 视频数据探索")
    print("=" * 80)
    print(f"\n正在加载数据：{data_path}\n")

    # 读取 CSV 文件
    df = pd.read_csv(data_path)

    return df

def explore_basic_info(df):
    """探索数据基本信息"""
    print("\n" + "=" * 80)
    print("1. 数据基本信息")
    print("=" * 80)

    print(f"\n数据形状：{df.shape[0]} 行 × {df.shape[1]} 列")
    print(f"数据时间范围：{df['publish_date'].min()} 至 {df['publish_date'].max()}")

    print("\n列名和数据类型：")
    print(df.dtypes)

    print("\n数据信息摘要：")
    df.info()

def check_data_quality(df):
    """检查数据质量"""
    print("\n" + "=" * 80)
    print("2. 数据质量检查")
    print("=" * 80)

    # 检查缺失值
    missing = df.isnull().sum()
    print("\n缺失值统计：")
    if missing.sum() == 0:
        print("✓ 无缺失值")
    else:
        print(missing[missing > 0])

    # 检查重复值
    duplicates = df.duplicated().sum()
    print(f"\n重复行数：{duplicates}")
    if duplicates == 0:
        print("✓ 无重复数据")

    # 检查异常值
    print("\n数值列范围检查：")
    numeric_cols = ['views', 'likes', 'comments', 'shares', 'duration', 'conversions']
    for col in numeric_cols:
        print(f"  {col}: 最小值={df[col].min()}, 最大值={df[col].max()}")

def show_sample_data(df):
    """显示样本数据"""
    print("\n" + "=" * 80)
    print("3. 样本数据")
    print("=" * 80)

    print("\n前 10 行数据：")
    print(df.head(10))

    print("\n后 10 行数据：")
    print(df.tail(10))

def calculate_statistics(df):
    """计算描述性统计"""
    print("\n" + "=" * 80)
    print("4. 描述性统计")
    print("=" * 80)

    print("\n数值列统计摘要：")
    print(df.describe())

    print("\n视频类型分布：")
    print(df['video_type'].value_counts())

    print("\n发布时间分布（按小时）：")
    hour_dist = df['publish_hour'].value_counts().sort_index()
    print(hour_dist)

def calculate_derived_metrics(df):
    """计算衍生指标"""
    print("\n" + "=" * 80)
    print("5. 衍生指标计算")
    print("=" * 80)

    # 计算互动率
    df['like_rate'] = (df['likes'] / df['views'] * 100).round(2)
    df['comment_rate'] = (df['comments'] / df['views'] * 100).round(2)
    df['share_rate'] = (df['shares'] / df['views'] * 100).round(2)
    df['conversion_rate'] = (df['conversions'] / df['views'] * 100).round(2)

    print("\n互动率统计（%）：")
    rate_cols = ['like_rate', 'comment_rate', 'share_rate', 'conversion_rate']
    print(df[rate_cols].describe())

    print("\n各视频类型平均指标：")
    type_metrics = df.groupby('video_type').agg({
        'views': 'mean',
        'conversions': 'mean',
        'conversion_rate': 'mean',
        'like_rate': 'mean',
        'share_rate': 'mean'
    }).round(2)
    print(type_metrics)

    return df

def main():
    """主函数"""
    # 加载数据
    df = load_data()

    # 探索基本信息
    explore_basic_info(df)

    # 检查数据质量
    check_data_quality(df)

    # 显示样本数据
    show_sample_data(df)

    # 计算描述性统计
    calculate_statistics(df)

    # 计算衍生指标
    df = calculate_derived_metrics(df)

    print("\n" + "=" * 80)
    print("数据探索完成！")
    print("=" * 80)
    print("\n关键发现：")
    print(f"  • 共分析 {len(df)} 条视频数据")
    print(f"  • 总播放量：{df['views'].sum():,}")
    print(f"  • 总转化量：{df['conversions'].sum():,}")
    print(f"  • 平均转化率：{df['conversion_rate'].mean():.2f}%")
    print(f"  • 视频类型：{df['video_type'].nunique()} 种")
    print()

if __name__ == "__main__":
    main()
