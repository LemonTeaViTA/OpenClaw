#!/usr/bin/env python3
"""
GitHub 自动备份脚本
检测文件变更，自动 commit 并推送
"""

import subprocess
import json
from pathlib import Path
from datetime import datetime

# 仓库路径
REPO_PATH = Path("/root/.openclaw/workspace")

# 备份目录
BACKUP_DIRS = [
    "memory/",
    "01-Obsidian/40-Questions/",
    "skills/",
]

# 排除文件
EXCLUDE_PATTERNS = [
    "*.pyc",
    "__pycache__/",
    "*.log",
    ".tmp/",
    "*.swp",
]


def run_git(args, cwd=REPO_PATH):
    """执行 git 命令"""
    try:
        result = subprocess.run(
            ["git"] + args,
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result.returncode, result.stdout, result.stderr
    except Exception as e:
        return -1, "", str(e)


def check_status():
    """检查 git 状态"""
    print("🔍 检查仓库状态...\n")
    
    # git status
    code, out, err = run_git(["status", "--short"])
    
    if code != 0:
        print(f"❌ Git 错误：{err}")
        return None
    
    if not out.strip():
        print("✅ 没有变更需要提交")
        return []
    
    print("📝 变更文件:\n")
    files = []
    for line in out.strip().split("\n"):
        if line.strip():
            print(f"  {line}")
            # 提取文件名
            parts = line.split()
            if len(parts) >= 2:
                files.append(parts[-1])
    
    print(f"\n共 {len(files)} 个文件变更")
    return files


def get_diff_stats(files=None):
    """获取变更统计"""
    if files:
        code, out, err = run_git(["diff", "--stat"] + files)
    else:
        code, out, err = run_git(["diff", "--stat"])
    
    if code == 0 and out.strip():
        print("\n📊 变更统计:\n")
        print(out)
        
        # 解析统计
        lines = out.strip().split("\n")
        if len(lines) >= 2:
            last_line = lines[-1]
            # 格式：X files changed, Y insertions(+), Z deletions(-)
            return last_line
    
    return None


def add_files(files=None):
    """添加文件到暂存区"""
    if files:
        print(f"\n📦 添加 {len(files)} 个文件...")
        code, out, err = run_git(["add"] + files)
    else:
        print("\n📦 添加所有变更...")
        code, out, err = run_git(["add", "-A"])
    
    if code == 0:
        print("✅ 文件已添加")
        return True
    else:
        print(f"❌ 添加失败：{err}")
        return False


def commit(message: str):
    """提交变更"""
    print(f"\n💾 提交：{message}")
    
    code, out, err = run_git([
        "commit",
        "-m", message,
    ])
    
    if code == 0:
        print("✅ 提交成功")
        return True
    else:
        print(f"❌ 提交失败：{err}")
        return False


def push():
    """推送到远程"""
    print("\n🚀 推送到远程仓库...")
    
    code, out, err = run_git(["push", "origin", "HEAD"])
    
    if code == 0:
        print("✅ 推送成功")
        return True
    else:
        print(f"❌ 推送失败：{err}")
        return False


def generate_commit_message(files=None, auto=True):
    """生成提交信息"""
    if auto:
        # 自动生成
        date = datetime.now().strftime("%Y-%m-%d %H:%M")
        
        # 检测主要变更类型
        if files:
            has_memory = any("memory/" in f for f in files)
            has_questions = any("Questions" in f for f in files)
            has_skills = any("skills/" in f for f in files)
            
            if has_memory and has_questions:
                prefix = "📚 学习"
                desc = f"每日复习记录 {date[:10]}"
            elif has_skills:
                prefix = "✨ 技能"
                desc = "更新复习技能"
            else:
                prefix = "📝 笔记"
                desc = f"文件更新 {date[:10]}"
        else:
            prefix = "🔄 更新"
            desc = f"自动备份 {date}"
        
        message = f"{prefix}: {desc}"
        
        # 添加详细统计
        stats = get_diff_stats(files)
        if stats:
            message += f"\n\n{stats}"
        
        return message
    else:
        # 手动输入
        return input("请输入提交信息：")


def show_log(count=10):
    """显示提交历史"""
    print(f"\n📜 最近 {count} 条提交记录:\n")
    
    code, out, err = run_git([
        "log",
        f"-{count}",
        "--oneline",
        "--decorate",
    ])
    
    if code == 0:
        print(out)
    else:
        print(f"❌ 获取失败：{err}")


def backup_all(dry_run=False):
    """完整备份流程"""
    print("=" * 60)
    print("🔄 开始自动备份")
    print("=" * 60)
    
    # 1. 检查状态
    files = check_status()
    if not files:
        return True
    
    # 2. 显示统计
    get_diff_stats(files)
    
    if dry_run:
        print("\n⚠️  模拟运行（未实际提交）")
        return True
    
    # 3. 添加文件
    if not add_files(files):
        return False
    
    # 4. 生成提交信息并提交
    message = generate_commit_message(files, auto=True)
    print(f"\n📝 提交信息：{message}")
    
    if not commit(message):
        return False
    
    # 5. 推送
    if not push():
        return False
    
    print("\n" + "=" * 60)
    print("✅ 备份完成！")
    print("=" * 60)
    
    return True


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="GitHub 自动备份工具")
    parser.add_argument("--backup", action="store_true", help="完整备份流程")
    parser.add_argument("--status", action="store_true", help="检查变更状态")
    parser.add_argument("--commit", action="store_true", help="手动提交")
    parser.add_argument("-m", "--message", type=str, help="提交信息")
    parser.add_argument("--push", action="store_true", help="推送到远程")
    parser.add_argument("--log", action="store_true", help="查看提交历史")
    parser.add_argument("--count", type=int, default=10, help="提交历史数量")
    parser.add_argument("--summary", action="store_true", help="生成变更摘要")
    parser.add_argument("--date", type=str, default="today", help="日期")
    parser.add_argument("--dry-run", action="store_true", help="模拟运行")
    
    args = parser.parse_args()
    
    # 检查是否在 git 仓库中
    code, out, err = run_git(["rev-parse", "--git-dir"])
    if code != 0:
        print("❌ 当前目录不是 Git 仓库")
        return
    
    if args.backup:
        backup_all(dry_run=args.dry_run)
    
    elif args.status:
        check_status()
    
    elif args.commit:
        files = check_status()
        if files:
            add_files(files)
            message = args.message or generate_commit_message(files, auto=True)
            commit(message)
    
    elif args.push:
        push()
    
    elif args.log:
        show_log(args.count)
    
    elif args.summary:
        # 生成变更摘要
        print("📊 变更摘要生成中...")
        check_status()
    
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
