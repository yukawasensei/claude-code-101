# Mock数据设计方案

本文档说明教程中使用的示例数据的设计思路和生成规则。

---

## Case 1: TikTok 直播+短视频运营数据

### 数据规模

- **记录数**: 50条
- **时间范围**: 2026年1月-2月
- **数据类型**: 直播和短视频混合数据

### 字段设计

#### 基础字段(11个)

| 字段名 | 类型 | 说明 | 示例值 |
|--------|------|------|--------|
| video_id | 字符串 | 视频唯一标识 | V001, V002, ... |
| title | 字符串 | 视频标题 | "3分钟学会做红烧肉" |
| publish_date | 日期 | 发布日期 | 2026-01-05 |
| publish_hour | 整数 | 发布小时(0-23) | 19 |
| views | 整数 | 播放量 | 28500 |
| likes | 整数 | 点赞量 | 3420 |
| comments | 整数 | 评论量 | 285 |
| shares | 整数 | 分享量 | 570 |
| duration | 整数 | 视频时长(秒) | 180 |
| video_type | 字符串 | 视频类型 | 教程/测评/好物推荐/剧情 |
| conversions | 整数 | 成单量 | 35 |

#### 直播数据字段(5个)

| 字段名 | 类型 | 说明 | 示例值 |
|--------|------|------|--------|
| live_uv | 整数 | 场观(独立访客数) | 8500 |
| peak_online | 整数 | 在线峰值 | 1200 |
| avg_watch_time | 整数 | 人均停留时长(秒) | 420 |
| gmv | 浮点数 | 成交金额(元) | 15680.50 |
| order_conversion_rate | 浮点数 | 下单转化率(%) | 4.12 |

#### 投流数据字段(3个)

| 字段名 | 类型 | 说明 | 示例值 |
|--------|------|------|--------|
| ad_cost | 浮点数 | 广告花费(元) | 2500.00 |
| cpm | 浮点数 | 千次观看成本(元) | 87.72 |
| roi | 浮点数 | 投资回报率(%) | 527.22 |

#### 互动数据字段(3个)

| 字段名 | 类型 | 说明 | 示例值 |
|--------|------|------|--------|
| danmu_count | 整数 | 弹幕数 | 1250 |
| gift_count | 整数 | 礼物数 | 85 |
| follow_conversion_rate | 浮点数 | 关注转化率(%) | 12.5 |

### 数据生成规律

#### 1. 发布时间影响

**黄金时段(19:00-21:00)**:
- 播放量: 20,000 - 50,000
- 互动率: 较高(12-15%)
- 转化率: 较高

**其他时段**:
- 播放量: 5,000 - 20,000
- 互动率: 一般(8-12%)
- 转化率: 一般

**实现逻辑**:
```python
if publish_hour in [19, 20, 21]:
    views = random.randint(20000, 50000)
    engagement_rate = random.uniform(0.12, 0.15)
else:
    views = random.randint(5000, 20000)
    engagement_rate = random.uniform(0.08, 0.12)
```

#### 2. 视频类型影响

| 类型 | 转化率范围 | 播放量倾向 | 互动率 |
|------|-----------|-----------|--------|
| 教程 | 6-10‱ | 中等 | 高 |
| 测评 | 4-8‱ | 高 | 中 |
| 好物推荐 | 3-7‱ | 中等 | 中 |
| 剧情 | 1-5‱ | 高 | 低 |

**实现逻辑**:
```python
conversion_rates = {
    '教程': (0.06, 0.10),
    '测评': (0.04, 0.08),
    '好物推荐': (0.03, 0.07),
    '剧情': (0.01, 0.05)
}

video_type = random.choice(['教程', '测评', '好物推荐', '剧情'])
min_rate, max_rate = conversion_rates[video_type]
conversion_rate = random.uniform(min_rate, max_rate)
```

#### 3. 互动数据关系

**点赞量**:
```python
likes = int(views * random.uniform(0.05, 0.15))
```

**评论量**:
```python
comments = int(views * random.uniform(0.01, 0.03))
```

**分享量**:
```python
shares = int(views * random.uniform(0.005, 0.02))
```

**弹幕数(直播)**:
```python
danmu_count = int(live_uv * random.uniform(0.1, 0.2))
```

**礼物数(直播)**:
```python
gift_count = int(live_uv * random.uniform(0.005, 0.015))
```

#### 4. 转化规律

**基础转化**:
```python
base_conversions = int(views * conversion_rate)
```

**加入随机波动(±30%)**:
```python
conversions = int(base_conversions * random.uniform(0.7, 1.3))
```

**异常值(3-5个)**:
- 高播放低转化: 播放量高但转化率异常低
- 低播放高转化: 播放量低但转化率异常高

```python
# 创建3-5个异常值
if random.random() < 0.1:  # 10%概率
    if random.random() < 0.5:
        # 高播放低转化
        views = random.randint(30000, 50000)
        conversions = int(views * 0.01)  # 转化率仅1‱
    else:
        # 低播放高转化
        views = random.randint(5000, 10000)
        conversions = int(views * 0.15)  # 转化率高达15‱
```

#### 5. 直播数据规律

**场观(live_uv)**:
```python
live_uv = int(views * random.uniform(0.2, 0.4))
```

**在线峰值(peak_online)**:
```python
peak_online = int(live_uv * random.uniform(0.1, 0.2))
```

**人均停留时长(avg_watch_time)**:
```python
avg_watch_time = int(duration * random.uniform(0.3, 0.7))
```

**GMV**:
```python
gmv = conversions * random.uniform(300, 800)  # 客单价300-800元
```

**下单转化率**:
```python
order_conversion_rate = (conversions / live_uv) * 100
```

#### 6. 投流数据规律

**广告花费**:
```python
ad_cost = views * random.uniform(0.05, 0.15)  # 每次观看成本0.05-0.15元
```

**CPM(千次观看成本)**:
```python
cpm = (ad_cost / views) * 1000
```

**ROI**:
```python
roi = (gmv / ad_cost) * 100 if ad_cost > 0 else 0
```

### 标题示例

#### 教程类
- "3分钟学会做红烧肉"
- "新手必看的化妆教程"
- "手把手教你做Excel表格"
- "零基础学Python编程"
- "5分钟学会拍短视频"

#### 测评类
- "这款手机真的值得买吗?"
- "深度测评:XX扫地机器人"
- "使用一个月后的真实感受"
- "XX vs XX 对比测评"
- "百元耳机能有多好?"

#### 好物推荐类
- "这个神器太好用了!"
- "居家好物分享"
- "学生党必买清单"
- "提升幸福感的小物件"
- "我的日常好物推荐"

#### 剧情类
- "今天又是打工人的一天"
- "社恐人的日常"
- "搞笑瞬间合集"
- "当代年轻人的真实写照"
- "这也太真实了吧"

### 数据分布特征

#### 播放量分布
- 5,000-10,000: 30%
- 10,000-20,000: 40%
- 20,000-30,000: 20%
- 30,000-50,000: 10%

#### 转化率分布
- 1-3‱: 20%
- 3-5‱: 30%
- 5-7‱: 30%
- 7-10‱: 15%
- 10‱以上: 5%

#### 视频类型分布
- 教程: 36%
- 测评: 28%
- 好物推荐: 24%
- 剧情: 12%

#### 发布时间分布
- 黄金时段(19-21点): 40%
- 白天(9-18点): 35%
- 早晨(6-9点): 15%
- 深夜(22-24点): 10%

### 关键洞察设计

数据中设计了以下可发现的规律:

1. **黄金发布时间**: 晚上7-9点播放量比其他时段高80%
2. **最优内容类型**: 教程类转化率最高,是剧情类的2.5倍
3. **最优视频时长**: 30-45秒,完播率和转化率都最高
4. **投流ROI差异**: 教程类152%,剧情类仅70%
5. **高互动≠高转化**: 存在5个高互动但低转化的视频

### 数据生成脚本

完整的数据生成脚本位于:
```
case1-tiktok-analysis/generate_data.py
```

运行方式:
```bash
cd case1-tiktok-analysis
python3 generate_data.py
```

生成的数据文件:
```
case1-tiktok-analysis/tiktok_data.csv
```

---

## 数据质量保证

### 1. 真实性

- 数据范围符合真实运营场景
- 字段关系符合业务逻辑
- 异常值比例合理(10%左右)

### 2. 可分析性

- 包含足够的维度供分析
- 数据量适中(50条),不会太少也不会太多
- 包含明显的规律和洞察

### 3. 教学价值

- 数据设计支持教程中的所有分析维度
- 可以发现有价值的业务洞察
- 适合演示提示词编写和 skills 使用

---

## 扩展数据设计

如果需要更多数据或不同场景,可以参考以下设计:

### 场景2: 电商产品销售数据

**字段设计**:
- product_id, product_name, category
- price, cost, profit_margin
- sales_volume, revenue
- rating, review_count
- return_rate, customer_satisfaction

### 场景3: 用户行为数据

**字段设计**:
- user_id, session_id, timestamp
- page_path, action_type
- duration, scroll_depth
- device_type, browser
- conversion, revenue

### 场景4: 营销活动数据

**字段设计**:
- campaign_id, campaign_name, channel
- start_date, end_date
- budget, spend
- impressions, clicks, ctr
- conversions, cpa, roi

---

**提示**: 设计 mock 数据时,要确保数据既真实又有教学价值,包含明显的规律和洞察,方便学习者理解和实践。
