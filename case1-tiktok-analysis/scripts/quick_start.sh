#!/bin/bash
# TikTok 数据分析 HTML 报告 - 快速启动脚本

set -e  # 遇到错误立即退出

echo "============================================================"
echo "TikTok 数据分析 HTML 报告 - 快速启动"
echo "============================================================"
echo ""

# 获取脚本所在目录
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BASE_DIR="$(dirname "$SCRIPT_DIR")"

# 切换到项目目录
cd "$BASE_DIR"

# 检查虚拟环境
if [ ! -d "venv" ]; then
    echo "❌ 错误: 虚拟环境不存在"
    echo "请先创建虚拟环境: python3 -m venv venv"
    exit 1
fi

# 激活虚拟环境
echo "📦 激活虚拟环境..."
source venv/bin/activate

# 检查依赖
echo "🔍 检查依赖..."
if ! python -c "import pandas" 2>/dev/null; then
    echo "⚠️  pandas 未安装，正在安装..."
    pip install pandas
fi

# 生成报告
echo ""
echo "🚀 生成 HTML 报告..."
python scripts/generate_html_report.py

# 验证报告
echo ""
echo "✅ 验证报告..."
python scripts/validate_html_report.py

# 询问是否打开报告
echo ""
read -p "是否在浏览器中打开报告？(y/n) " -n 1 -r
echo ""

if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "🌐 在浏览器中打开报告..."
    open tiktok_analysis_report.html
    echo "✅ 报告已在浏览器中打开"
else
    echo "📄 报告位置: $BASE_DIR/tiktok_analysis_report.html"
    echo "💡 手动打开: open tiktok_analysis_report.html"
fi

echo ""
echo "============================================================"
echo "✨ 完成！"
echo "============================================================"
