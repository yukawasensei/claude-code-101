import csv
import random
from datetime import datetime, timedelta

# 视频标题库
titles = [
    "3分钟学会做红烧肉，新手也能零失败",
    "这个护肤品我用了3年，真的好用到哭",
    "月薪5000如何存下第一个10万？",
    "iPhone 15 Pro深度测评，值不值得买？",
    "懒人早餐合集，5分钟搞定营养早餐",
    "这样收纳衣柜，空间瞬间大一倍",
    "职场新人必看！5个Excel技巧提升效率",
    "小户型改造前后对比，太震撼了",
    "平价好物推荐，学生党必入",
    "健身3个月身材对比，坚持就有收获",
    "这个化妆技巧让我年轻5岁",
    "副业分享：我如何月入过万",
    "旅行vlog｜成都3天2夜美食攻略",
    "书单推荐｜10本改变我人生的书",
    "家常菜教程｜番茄炒蛋的正确做法",
    "数码测评｜AirPods Pro 2代值得升级吗",
    "穿搭分享｜小个子女生显高技巧",
    "理财入门｜基金定投真的能赚钱吗",
    "护肤误区｜这5个习惯让你越来越丑",
    "效率工具｜这个App让我工作效率翻倍",
    "美食探店｜上海必吃的10家餐厅",
    "读书笔记｜《原则》精华总结",
    "运动日常｜跑步1年的身体变化",
    "好物分享｜我的桌面好物清单",
    "剧情短片｜社恐打工人的一天",
    "技能分享｜零基础学会剪辑视频",
    "省钱攻略｜每月省下2000的秘诀",
    "测评对比｜小米vs华为，谁更值得买",
    "生活vlog｜独居女生的周末日常",
    "学习方法｜如何高效备考通过考试",
    "家居好物｜提升幸福感的10件小物",
    "职场干货｜如何写出让老板满意的PPT",
    "美妆教程｜日常淡妆只需5步",
    "投资理财｜普通人如何开始理财",
    "美食教程｜手把手教你做蛋糕",
    "数码开箱｜最新款iPad使用体验",
    "穿搭灵感｜秋冬穿搭公式分享",
    "时间管理｜我如何做到早起不痛苦",
    "护肤routine｜我的晚间护肤步骤",
    "效率神器｜这些工具让我下班更早",
    "探店打卡｜北京网红咖啡店合集",
    "读书分享｜每天读书30分钟的改变",
    "健身教程｜在家也能练出马甲线",
    "好物种草｜我的包包里都有什么",
    "搞笑剧情｜当代年轻人的真实写照",
    "技能教学｜10分钟学会做表格",
    "省钱妙招｜这样买东西能省一半钱",
    "产品测评｜戴森吹风机真的值吗",
    "日常记录｜一个人的晚餐时光",
    "干货分享｜新媒体运营必备技能"
]

# 视频类型
video_types = ["教程", "测评", "好物推荐", "剧情"]

# 转化率配置（万分之）
conversion_rates = {
    "教程": (60, 100),
    "测评": (40, 80),
    "好物推荐": (30, 70),
    "剧情": (10, 50)
}

# 生成数据
data = []
start_date = datetime(2026, 1, 1)

for i in range(50):
    video_id = f"V{str(i+1).zfill(3)}"
    title = titles[i]

    # 发布日期（随机分布在2个月内）
    days_offset = random.randint(0, 58)
    publish_date = start_date + timedelta(days=days_offset)

    # 发布小时（模拟真实发布习惯）
    hour_weights = {
        range(7, 9): 5,    # 早高峰
        range(12, 14): 10,  # 午休
        range(19, 22): 15,  # 晚高峰（黄金时段）
        range(22, 24): 8,   # 深夜
    }
    hour_pool = []
    for hour_range, weight in hour_weights.items():
        hour_pool.extend(list(hour_range) * weight)
    publish_hour = random.choice(hour_pool + list(range(0, 24)))

    # 根据发布时间决定播放量基数
    if 19 <= publish_hour <= 21:  # 黄金时段
        views = random.randint(20000, 50000)
    elif publish_hour in [12, 13, 21, 22, 23]:  # 次优时段
        views = random.randint(10000, 25000)
    else:  # 普通时段
        views = random.randint(1000, 15000)

    # 视频类型
    video_type = random.choice(video_types)

    # 互动数据
    like_rate = random.uniform(0.05, 0.15)
    comment_rate = random.uniform(0.01, 0.03)
    share_rate = random.uniform(0.005, 0.02)

    likes = int(views * like_rate)
    comments = int(views * comment_rate)
    shares = int(views * share_rate)

    # 视频时长（15秒-5分钟）
    duration = random.choice([15, 30, 45, 60, 90, 120, 180, 240, 300])

    # 转化量
    min_rate, max_rate = conversion_rates[video_type]
    conversion_rate = random.uniform(min_rate, max_rate) / 10000
    conversions = int(views * conversion_rate * random.uniform(0.7, 1.3))

    data.append({
        "video_id": video_id,
        "title": title,
        "publish_date": publish_date.strftime("%Y-%m-%d"),
        "publish_hour": publish_hour,
        "views": views,
        "likes": likes,
        "comments": comments,
        "shares": shares,
        "duration": duration,
        "video_type": video_type,
        "conversions": conversions
    })

# 添加几个异常值用于教学
# 1. 超级爆款
data[5]["views"] = 120000
data[5]["likes"] = int(120000 * 0.18)
data[5]["conversions"] = int(120000 * 0.012)

# 2. 低播放高转化（精准流量）
data[15]["views"] = 5000
data[15]["conversions"] = int(5000 * 0.015)

# 3. 高播放低转化
data[25]["views"] = 45000
data[25]["conversions"] = int(45000 * 0.002)

# 写入CSV
with open('tiktok_data.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)

print("✅ TikTok数据已生成：tiktok_data.csv")
print(f"📊 总计 {len(data)} 条视频记录")
print(f"📅 时间跨度：{data[0]['publish_date']} 至 {data[-1]['publish_date']}")
