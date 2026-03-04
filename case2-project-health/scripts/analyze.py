#!/usr/bin/env python3
"""
Case 2数据分析示例
展示如何分析TaskFlow项目的数据
"""

import json
import csv
from datetime import datetime
from collections import Counter

def analyze_progress():
    """分析项目进度数据"""
    print("=" * 60)
    print("项目进度分析")
    print("=" * 60)
    print()

    with open('data/progress.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    weekly = data['weekly_progress']

    # 1. 团队速度趋势
    print("1. 团队速度趋势")
    print("-" * 60)
    for week in weekly:
        velocity = week['team_velocity']
        morale = week['team_morale']
        bar = "█" * velocity
        print(f"第{week['week']}周: {bar} {velocity} 任务/周 (士气: {morale})")
    print()

    # 2. Bug趋势
    print("2. Bug发现与修复趋势")
    print("-" * 60)
    for week in weekly:
        found = week['bugs_found']
        fixed = week['bugs_fixed']
        print(f"第{week['week']}周: 发现 {found:2d} 个, 修复 {fixed:2d} 个")
    print()

    # 3. 测试覆盖率
    print("3. 测试覆盖率变化")
    print("-" * 60)
    for week in weekly:
        coverage = week['test_coverage']
        percentage = int(coverage * 100)
        bar = "█" * (percentage // 5)
        print(f"第{week['week']}周: {bar} {percentage}%")
    print()

    # 4. 关键决策
    print("4. 关键决策")
    print("-" * 60)
    for decision in data['summary']['key_decisions']:
        print(f"第{decision['week']}周: {decision['decision']}")
        print(f"  原因: {decision['reason']}")
        print(f"  影响: {decision['impact']}")
        print()

def analyze_feedback():
    """分析用户反馈数据"""
    print("=" * 60)
    print("用户反馈分析")
    print("=" * 60)
    print()

    with open('data/user-feedback.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        feedbacks = list(reader)

    # 1. 反馈类型分布
    print("1. 反馈类型分布")
    print("-" * 60)
    types = Counter(f['feedback_type'] for f in feedbacks)
    for ftype, count in types.most_common():
        percentage = count / len(feedbacks) * 100
        bar = "█" * (count // 2)
        print(f"{ftype:8s}: {bar} {count:2d} ({percentage:.1f}%)")
    print()

    # 2. 优先级分布
    print("2. 优先级分布")
    print("-" * 60)
    priorities = Counter(f['priority'] for f in feedbacks)
    priority_order = ['高', '中', '低']
    for priority in priority_order:
        count = priorities[priority]
        percentage = count / len(feedbacks) * 100
        bar = "█" * (count // 2)
        print(f"{priority}: {bar} {count:2d} ({percentage:.1f}%)")
    print()

    # 3. 状态分布
    print("3. 处理状态分布")
    print("-" * 60)
    statuses = Counter(f['status'] for f in feedbacks)
    for status, count in statuses.most_common():
        percentage = count / len(feedbacks) * 100
        bar = "█" * (count // 2)
        print(f"{status:6s}: {bar} {count:2d} ({percentage:.1f}%)")
    print()

    # 4. 高优先级问题
    print("4. 高优先级问题（前5个）")
    print("-" * 60)
    high_priority = [f for f in feedbacks if f['priority'] == '高']
    for i, feedback in enumerate(high_priority[:5], 1):
        print(f"{i}. [{feedback['feedback_type']}] {feedback['content']}")
        print(f"   状态: {feedback['status']} | 日期: {feedback['date']}")
    print()

    # 5. 时间趋势
    print("5. 反馈时间分布")
    print("-" * 60)
    dates = [datetime.strptime(f['date'], '%Y-%m-%d') for f in feedbacks]
    weeks = [(d - min(dates)).days // 7 + 1 for d in dates]
    week_counts = Counter(weeks)

    for week in range(1, 9):
        count = week_counts.get(week, 0)
        bar = "█" * count
        print(f"第{week}周: {bar} {count:2d} 条")
    print()

def analyze_correlation():
    """分析数据关联性"""
    print("=" * 60)
    print("数据关联分析")
    print("=" * 60)
    print()

    # 加载数据
    with open('data/progress.json', 'r', encoding='utf-8') as f:
        progress = json.load(f)

    with open('data/user-feedback.csv', 'r', encoding='utf-8') as f:
        feedbacks = list(csv.DictReader(f))

    # 按周统计反馈
    dates = [datetime.strptime(f['date'], '%Y-%m-%d') for f in feedbacks]
    start_date = datetime(2026, 1, 1)
    weeks = [(d - start_date).days // 7 + 1 for d in dates]
    week_feedback_counts = Counter(weeks)

    print("1. 团队速度 vs 用户反馈数量")
    print("-" * 60)
    print("周次 | 团队速度 | 反馈数 | 士气")
    print("-" * 60)

    for week_data in progress['weekly_progress']:
        week = week_data['week']
        velocity = week_data['team_velocity']
        feedback_count = week_feedback_counts.get(week, 0)
        morale = week_data['team_morale']

        print(f"第{week}周 |    {velocity:2d}    |   {feedback_count:2d}   | {morale}")

    print()
    print("观察:")
    print("- 第3-4周：团队速度下降，用户反馈增多，士气下降")
    print("- 第5周后：团队速度恢复，反馈数量增加但类型改善")
    print("- 第7-8周：团队速度提升，反馈以建议为主")
    print()

    print("2. Bug数量 vs 测试覆盖率")
    print("-" * 60)
    print("周次 | Bug发现 | Bug修复 | 测试覆盖率")
    print("-" * 60)

    for week_data in progress['weekly_progress']:
        week = week_data['week']
        found = week_data['bugs_found']
        fixed = week_data['bugs_fixed']
        coverage = int(week_data['test_coverage'] * 100)

        print(f"第{week}周 |   {found:2d}    |   {fixed:2d}    |    {coverage:2d}%")

    print()
    print("观察:")
    print("- 测试覆盖率提升，bug发现数量先增后减")
    print("- 第4周bug数量达到峰值（23个）")
    print("- 第5周后bug修复率接近100%")
    print()

def generate_summary():
    """生成项目总结"""
    print("=" * 60)
    print("项目总结")
    print("=" * 60)
    print()

    with open('data/progress.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    summary = data['summary']

    print("最终成果:")
    print(f"  ✓ 完成任务: {summary['total_tasks_completed']} 个")
    print(f"  ✓ 修复Bug: {summary['total_bugs_fixed']}/{summary['total_bugs_found']} 个")
    print(f"  ✓ 测试覆盖率: {int(summary['final_test_coverage'] * 100)}%")
    print(f"  ✓ 用户满意度: {summary['final_user_satisfaction']}/10")
    print(f"  ✓ 按时交付: {'是' if summary['on_time_delivery'] else '否'}")
    print(f"  ✓ 预算状态: {summary['budget_status']}")
    print()

    print("经验教训:")
    for i, lesson in enumerate(summary['lessons_learned'], 1):
        print(f"  {i}. {lesson}")
    print()

def main():
    """主函数"""
    print()
    print("╔" + "═" * 58 + "╗")
    print("║" + " " * 15 + "TaskFlow项目数据分析" + " " * 23 + "║")
    print("╚" + "═" * 58 + "╝")
    print()

    # 1. 进度分析
    analyze_progress()

    # 2. 反馈分析
    analyze_feedback()

    # 3. 关联分析
    analyze_correlation()

    # 4. 项目总结
    generate_summary()

    print("=" * 60)
    print("分析完成！")
    print("=" * 60)
    print()
    print("提示:")
    print("  - 可以使用pandas进行更深入的数据分析")
    print("  - 可以使用matplotlib/seaborn进行数据可视化")
    print("  - 可以结合会议纪要进行定性分析")
    print()

if __name__ == "__main__":
    main()
