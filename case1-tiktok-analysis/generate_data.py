#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TikTok 直播+短视频运营数据生成脚本

生成50条直播和短视频的完整数据,包含:
- 基础数据:video_id, title, publish_date, publish_hour, views, likes, comments, shares, duration, video_type, conversions
- 直播数据:live_uv, peak_online, avg_watch_time, gmv, order_conversion_rate
- 投流数据:ad_cost, cpm, roi
- 互动数据:danmu_count, gift_count, follow_conversion_rate
"""

import csv
import random
from datetime import datetime, timedelta

# 视频类型和对应的转化率范围
VIDEO_TYPES = {
    '教程': (0.0006, 0.0010),  # 6-10‱
    '测评': (0.0004, 0.0008),  # 4-8‱
    '好物推荐': (0.0003, 0.0007),  # 3-7‱
    '剧情': (0.0001, 0.0005),  # 1-5‱
}

# 标题模板
TITLE_TEMPLATES = {
    '教程': [
        '3分钟学会{}，新手也能零失败',
        '新手必看{}教程，手把手教你',
        '{}技巧大公开，学会这招就够了',
        '{}保姆级教程，看完就会',
        '5分钟掌握{}，超简单',
    ],
    '测评': [
        '{}深度测评，值不值得买？',
        '{}使用一个月后的真实感受',
        '{}真的值得买吗？实测告诉你',
        '{}全方位测评，优缺点都在这',
        '{}对比测评，哪个更好用？',
    ],
    '好物推荐': [
        '这个{}我用了3年，真的好用到哭',
        '{}好物分享，必买清单',
        '{}太好用了，强烈推荐',
        '{}宝藏好物，用过都说好',
        '{}必买清单，不买后悔',
    ],
    '剧情': [
        '今天又是{}的一天',
        '{}的日常，太真实了',
        '{}搞笑瞬间，笑死我了',
        '{}的一天，看完笑出声',
        '{}日常vlog，记录生活',
    ]
}

# 主题词
TOPICS = {
    '教程': ['做红烧肉', '化妆', '剪视频', '做PPT', '拍照', '修图', '做饭', '收纳', '理财', '英语'],
    '测评': ['iPhone 15 Pro', '小米14', '戴森吹风机', '空气炸锅', '扫地机器人', '洗碗机', 'AirPods', '机械键盘', '显示器', '护肤品'],
    '好物推荐': ['护肤品', '口红', '香水', '包包', '鞋子', '衣服', '零食', '厨具', '文具', '数码产品'],
    '剧情': ['打工人', '上班族', '学生党', '宝妈', '程序员', '设计师', '老师', '医生', '销售', '创业者']
}

def generate_title(video_type):
    """生成标题"""
    template = random.choice(TITLE_TEMPLATES[video_type])
    topic = random.choice(TOPICS[video_type])
    return template.format(topic)

def generate_data():
    """生成50条数据"""
    data = []
    start_date = datetime(2026, 1, 1)

    for i in range(1, 51):
        # 基础信息
        video_id = f'V{i:03d}'
        video_type = random.choice(list(VIDEO_TYPES.keys()))
        title = generate_title(video_type)

        # 发布时间(随机分布,但19:00-21:00更多)
        days_offset = random.randint(0, 59)
        publish_date = start_date + timedelta(days=days_offset)

        # 发布小时(19:00-21:00占40%,其他时段占60%)
        if random.random() < 0.4:
            publish_hour = random.choice([19, 20, 21])
        else:
            publish_hour = random.choice([h for h in range(24) if h not in [19, 20, 21]])

        # 播放量(19:00-21:00时段更高)
        if publish_hour in [19, 20, 21]:
            views = random.randint(20000, 50000)
        else:
            views = random.randint(5000, 20000)

        # 互动数据
        likes = int(views * random.uniform(0.05, 0.15))
        comments = int(views * random.uniform(0.01, 0.03))
        shares = int(views * random.uniform(0.005, 0.02))

        # 视频时长
        if video_type == '教程':
            duration = random.randint(30, 60)
        elif video_type == '测评':
            duration = random.randint(45, 90)
        elif video_type == '好物推荐':
            duration = random.randint(30, 60)
        else:  # 剧情
            duration = random.randint(15, 45)

        # 转化量
        conversion_rate = random.uniform(*VIDEO_TYPES[video_type])
        conversions = int(views * conversion_rate * random.uniform(0.7, 1.3))

        # 直播数据
        # 场观(UV) - 约为播放量的60-80%
        live_uv = int(views * random.uniform(0.6, 0.8))

        # 在线峰值 - 约为场观的5-15%
        peak_online = int(live_uv * random.uniform(0.05, 0.15))

        # 人均停留时长(秒) - 30-180秒
        avg_watch_time = random.randint(30, 180)

        # GMV(成交金额) - 转化量 × 客单价(50-200元)
        avg_price = random.randint(50, 200)
        gmv = conversions * avg_price

        # 下单转化率(%) - 转化量/场观
        order_conversion_rate = round((conversions / live_uv) * 100, 2) if live_uv > 0 else 0

        # 投流数据
        # 广告花费 - 根据视频类型不同
        if video_type == '教程':
            ad_cost = random.randint(300, 600)
        elif video_type == '测评':
            ad_cost = random.randint(500, 1000)
        elif video_type == '好物推荐':
            ad_cost = random.randint(200, 500)
        else:  # 剧情
            ad_cost = random.randint(100, 400)

        # CPM(千次观看成本) - 广告花费/播放量*1000
        cpm = round((ad_cost / views) * 1000, 2) if views > 0 else 0

        # ROI(投资回报率,%) - (GMV - 广告花费) / 广告花费 * 100
        roi = round(((gmv - ad_cost) / ad_cost) * 100, 2) if ad_cost > 0 else 0

        # 互动数据
        # 弹幕数 - 约为评论数的2-5倍
        danmu_count = int(comments * random.uniform(2, 5))

        # 礼物数 - 约为点赞数的1-3%
        gift_count = int(likes * random.uniform(0.01, 0.03))

        # 关注转化率(%) - 新增关注/场观
        new_followers = int(live_uv * random.uniform(0.01, 0.05))
        follow_conversion_rate = round((new_followers / live_uv) * 100, 2) if live_uv > 0 else 0

        # 添加数据
        data.append({
            'video_id': video_id,
            'title': title,
            'publish_date': publish_date.strftime('%Y-%m-%d'),
            'publish_hour': publish_hour,
            'views': views,
            'likes': likes,
            'comments': comments,
            'shares': shares,
            'duration': duration,
            'video_type': video_type,
            'conversions': conversions,
            'live_uv': live_uv,
            'peak_online': peak_online,
            'avg_watch_time': avg_watch_time,
            'gmv': gmv,
            'order_conversion_rate': order_conversion_rate,
            'ad_cost': ad_cost,
            'cpm': cpm,
            'roi': roi,
            'danmu_count': danmu_count,
            'gift_count': gift_count,
            'follow_conversion_rate': follow_conversion_rate,
        })

    return data

def save_to_csv(data, filename='tiktok_data.csv'):
    """保存到CSV文件"""
    fieldnames = [
        'video_id', 'title', 'publish_date', 'publish_hour',
        'views', 'likes', 'comments', 'shares', 'duration', 'video_type', 'conversions',
        'live_uv', 'peak_online', 'avg_watch_time', 'gmv', 'order_conversion_rate',
        'ad_cost', 'cpm', 'roi',
        'danmu_count', 'gift_count', 'follow_conversion_rate'
    ]

    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print(f'✅ 数据已生成: {filename}')
    print(f'📊 总记录数: {len(data)}')
    print(f'📋 字段数: {len(fieldnames)}')

if __name__ == '__main__':
    data = generate_data()
    save_to_csv(data)
