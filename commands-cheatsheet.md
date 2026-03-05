# 命令速查表

本文档提供 Claude Code 使用过程中常用的命令和快捷键,方便快速查找。

---

## 终端基础操作

### 复制和粘贴

**在 Warp 终端中**:
- **复制**: 选中文字后按 `Command + C`
- **粘贴**: 按 `Command + V`

**在系统终端(Terminal)中**:
- **复制**: 选中文字后按 `Command + C`
- **粘贴**: 按 `Command + V`
- **注意**: 有时需要用 `Command + Shift + C/V`

### 全选

- **Warp**: `Command + A`
- **Terminal**: `Command + A` (选中当前行)

### 移动光标

- `Control + A`: 移动到行首
- `Control + E`: 移动到行尾
- `Option + ←/→`: 按单词移动
- `←/→`: 按字符移动

### 删除文字

- `Delete`: 删除光标前的字符
- `Control + U`: 删除光标前的所有内容
- `Control + K`: 删除光标后的所有内容
- `Control + W`: 删除光标前的一个单词

### 历史命令

- `↑`: 查看上一条命令
- `↓`: 查看下一条命令
- `Control + R`: 搜索历史命令

### 中断和清屏

- `Control + C`: 停止当前正在运行的命令
- `Command + K` (Warp) 或 `Control + L` (Terminal): 清空屏幕

### 小技巧

- 在 Warp 中,你可以像在普通编辑器中一样使用鼠标选择和编辑
- 按 `Tab` 键可以自动补全文件名和命令
- 输入命令时不确定,可以按两次 `Tab` 查看可能的选项

---

## 文件和目录命令

### pwd - 我在哪里?

```bash
pwd
```

**作用**: 显示当前所在的文件夹路径
**类比**: 就像在Finder里查看当前文件夹的位置
**示例输出**: `/Users/你的用户名/Desktop`

### ls - 这里有什么?

```bash
ls
```

**作用**: 列出当前文件夹里的所有文件和子文件夹
**类比**: 就像在Finder里查看文件夹内容

**进阶用法**:
```bash
ls -la    # 显示隐藏文件和详细信息
ls -lh    # 显示文件大小(人类可读格式)
```

### cd - 去别的地方

```bash
cd Desktop
```

**作用**: 切换到另一个文件夹
**类比**: 就像在Finder里双击打开文件夹

**特殊路径**:
```bash
cd ~      # 回到用户主目录
cd ..     # 返回上一级目录
cd -      # 返回上一次所在的目录
```

### mkdir - 创建文件夹

```bash
mkdir my-project
```

**作用**: 创建一个新文件夹
**类比**: 就像在Finder里右键"新建文件夹"

**进阶用法**:
```bash
mkdir -p path/to/nested/folder    # 创建多级文件夹
```

### cat - 快速查看文件

```bash
cat README.md
```

**作用**: 在终端里显示文件内容
**类比**: 就像双击打开文本文件查看

**进阶用法**:
```bash
head README.md     # 查看文件前10行
tail README.md     # 查看文件后10行
```

### open - 打开文件或文件夹

```bash
open .                    # 在Finder中打开当前目录
open file.txt             # 用默认程序打开文件
open -a "TextEdit" file.txt    # 用指定程序打开文件
```

### 文件查找

```bash
find . -name "*.csv"      # 查找CSV文件
grep "关键词" file.txt    # 在文件中搜索关键词
```

---

## Claude Code 命令

### 启动和退出

```bash
claude                    # 启动 Claude Code
claude --version          # 查看版本号
```

**在 Claude Code 对话中**:
```bash
/exit                     # 退出 Claude Code
```

### 基础命令

```bash
/help                     # 查看帮助信息和所有可用命令
/clear                    # 清空当前对话历史(释放上下文空间)
/exit                     # 退出 Claude Code
```

**快捷键**:
- `↑/↓`: 查看和重用历史输入

### 会话管理

```bash
/init                     # 优化和初始化项目的 CLAUDE.md 配置文件
/resume                   # 恢复之前的会话(继续上次未完成的工作)
```

### 模型和性能

```bash
/model                    # 查看或切换使用的AI模型
/fast                     # 切换快速模式(使用相同模型但输出更快)
```

### 高级启动选项

```bash
# YOLO模式 - 跳过权限确认
claude --dangerously-skip-permissions

# 指定工作目录
claude --cwd /path/to/project
```

### 使用技巧

- 使用 `/init` 当你想为项目创建或优化 CLAUDE.md 配置时
- 使用 `/resume` 当你想继续之前的分析或项目时
- 使用 `/clear` 当对话太长影响理解时(但会丢失上下文)
- 使用 `/fast` 当你需要快速迭代时

---

## 快捷键大全

### Warp 终端

| 快捷键 | 功能 |
|--------|------|
| `Command + T` | 新建标签页 |
| `Command + W` | 关闭当前标签页 |
| `Command + K` | 清空屏幕 |
| `Command + ,` | 打开设置 |
| `Command + F` | 搜索 |
| `Command + D` | 分屏 |

### 系统终端(Terminal)

| 快捷键 | 功能 |
|--------|------|
| `Command + N` | 新建窗口 |
| `Command + T` | 新建标签页 |
| `Command + W` | 关闭当前标签页 |
| `Control + L` | 清空屏幕 |
| `Command + K` | 清空屏幕(另一种方式) |

### 通用快捷键

| 快捷键 | 功能 |
|--------|------|
| `Control + C` | 中断当前命令 |
| `Control + D` | 退出当前shell |
| `Control + Z` | 暂停当前命令 |
| `Control + A` | 移动到行首 |
| `Control + E` | 移动到行尾 |
| `Control + U` | 删除光标前的所有内容 |
| `Control + K` | 删除光标后的所有内容 |
| `Control + W` | 删除光标前的一个单词 |
| `Control + R` | 搜索历史命令 |
| `Tab` | 自动补全 |
| `↑/↓` | 浏览历史命令 |

---

## 常见问题速查

| 问题 | 解决方案 | 示例命令/提示 |
|------|---------|--------------|
| **Claude说找不到文件** | 检查文件是否存在,确认文件名拼写(注意大小写),使用绝对路径 | `ls -la` 或 `ls \| grep data` 或提示:"请读取 /Users/你的用户名/Desktop/project/data.csv" |
| **分析结果不符合预期** | 提供更多上下文信息,给出参考示例,明确说明哪里不对和期望是什么,分步调试逐个验证 | "请调整分析,我期望看到按月份分组的统计,而不是按天" |
| **生成的图表样式不满意** | 明确说明需要调整的样式细节 | "请调整图表样式:标题字号改为24px,颜色改为#2563eb,图例位置移到右侧,增加网格线" |
| **处理大文件很慢** | 先分析文件大小和结构,考虑分批处理,只读取需要的列,使用采样分析 | "请先分析文件大小,如果超过10MB,只读取前1000行进行采样分析" |
| **需要处理多个相似文件** | 让Claude写脚本批量处理 | "我有10个CSV文件(data1.csv到data10.csv),每个文件结构相同。请写一个脚本批量处理:读取所有文件,合并数据,统计总计,生成汇总报告" |
| **终端显示乱码** | 检查文件编码,使用UTF-8编码 | `file -I filename` 查看编码 |
| **权限不足** | 使用sudo或修改文件权限 | `sudo command` 或 `chmod +x file` |
| **命令找不到** | 检查是否安装,或添加到PATH | `which command` 检查命令位置 |

---

## 路径的概念

### 绝对路径

从根目录开始的完整路径

**示例**: `/Users/zhangsan/Desktop/my-project`
**类比**: 完整的家庭住址"北京市朝阳区XX街道XX号"

### 相对路径

相对于当前位置的路径

**示例**: `./data/report.csv` (当前文件夹下的data文件夹)
**类比**: 相对地址"隔壁楼3单元"

**特殊符号**:
- `.` - 当前目录
- `..` - 上一级目录
- `~` - 用户主目录
- `/` - 根目录

### 为什么重要?

Claude Code需要知道文件在哪里才能读取和处理。使用绝对路径最保险。

---

## 实用技巧

### 1. 使用Tab补全

输入文件名或命令的前几个字母,按 `Tab` 键自动补全:

```bash
cd Des[Tab]    # 自动补全为 cd Desktop/
cat data[Tab]  # 自动补全为 cat data.csv
```

### 2. 使用通配符

```bash
ls *.csv       # 列出所有CSV文件
rm temp*       # 删除所有以temp开头的文件
cp *.txt backup/    # 复制所有txt文件到backup文件夹
```

### 3. 管道和重定向

```bash
ls -la > files.txt           # 将输出保存到文件
cat file1.txt file2.txt > combined.txt    # 合并文件
grep "error" log.txt | wc -l    # 统计包含error的行数
```

### 4. 后台运行

```bash
command &      # 在后台运行命令
jobs           # 查看后台任务
fg             # 将后台任务调到前台
```

### 5. 命令组合

```bash
cd project && ls -la    # 切换目录并列出文件
mkdir new-folder && cd new-folder    # 创建并进入文件夹
```

---

## 安全提示

- ⚠️ 使用 `rm` 命令删除文件时要小心,删除后无法恢复
- ⚠️ 使用 `sudo` 命令时要确认操作,它有最高权限
- ⚠️ 不要随意执行不理解的命令
- ✅ 重要文件要备份
- ✅ 使用 `ls` 确认文件存在后再操作
- ✅ 使用 `pwd` 确认当前位置

---

**提示**: 将这个文档保存到你的项目文件夹,随时查阅。你也可以打印出来贴在电脑旁边。
