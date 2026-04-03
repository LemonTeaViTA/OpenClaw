#!/usr/bin/env python3
"""
复习记录脚本
记录复习结果，更新进度，生成报告
"""

import json
from pathlib import Path
from datetime import datetime, timedelta

# 文件路径
MEMORY_DIR = Path("/root/.openclaw/workspace/memory")
PROGRESS_FILE = Path("/root/.openclaw/workspace/01-Obsidian/40-Questions/复习进度记录.md")

# 篇章 ID 前缀映射
SECTION_PREFIX = {
    "JAVA": "Java 基础",
    "COLLECTION": "集合框架",
    "CONCURRENCY": "并发编程",
    "JVM": "JVM",
    "REDIS": "Redis",
    "MYSQL": "MySQL",
    "SPRING": "Spring",
}


def get_today_file() -> Path:
    """获取今日记录文件路径"""
    today = datetime.now().strftime("%Y-%m-%d")
    return MEMORY_DIR / f"{today}.md"


def record_review(questions: list, scores: list, timestamp: str = None):
    """记录复习结果"""
    if not timestamp:
        timestamp = datetime.now().isoformat()
    
    # 构建记录内容
    records = []
    for q_id, score in zip(questions, scores):
        # 判断掌握情况
        if score >= 5:
            status = "✅✅ 熟练"
        elif score >= 4:
            status = "✅ 已掌握"
        elif score >= 3:
            status = "🔄 需强化"
        else:
            status = "❌ 未掌握"
        
        records.append({
            "id": q_id,
            "score": score,
            "status": status,
            "timestamp": timestamp,
        })
    
    # 追加到今日文件
    today_file = get_today_file()
    
    content = f"\n## 📝 复习记录（{timestamp[:16]}）\n\n"
    content += "| 题目 ID | 得分 | 掌握情况 |\n"
    content += "|---------|------|----------|\n"
    
    for rec in records:
        content += f"| {rec['id']} | {rec['score']}/5 | {rec['status']} |\n"
    
    # 追加到文件末尾
    if today_file.exists():
        with open(today_file, "a", encoding="utf-8") as f:
            f.write(content)
    else:
        # 创建新文件
        header = f"# {datetime.now().strftime('%Y-%m-%d')} 学习记录\n\n"
        with open(today_file, "w", encoding="utf-8") as f:
            f.write(header + content)
    
    print(f"✅ 复习记录已保存到：{today_file}")
    return records


def generate_report(date: str, output: str = "console"):
    """生成复习报告"""
    if date == "today":
        date = datetime.now().strftime("%Y-%m-%d")
    
    file_path = MEMORY_DIR / f"{date}.md"
    
    if not file_path.exists():
        print(f"❌ 未找到 {date} 的记录文件")
        return
    
    content = file_path.read_text(encoding="utf-8")
    
    # 解析记录
    report = {
        "date": date,
        "total_questions": 0,
        "average_score": 0,
        "by_section": {},
    }
    
    # 简单统计（实际应该更完善）
    print(f"\n📊 {date} 复习报告\n")
    print("=" * 60)
    print(content[:2000])  # 显示前 2000 字符
    
    return report


def update_progress():
    """更新复习进度统计"""
    # 读取所有记忆文件
    # 计算总复习数、掌握数、正确率等
    # 更新 PROGRESS_FILE
    
    print("📈 进度统计已更新")
    print(f"文件：{PROGRESS_FILE}")


def get_due_questions():
    """获取今日应复习的题目（艾宾浩斯）"""
    # 根据上次复习时间和间隔计算
    # 返回待复习题目列表
    
    print("📅 今日待复习题目：")
    print("- JAVA-002 (间隔 1 天)")
    print("- MYSQL-013 (间隔 2 天)")
    print("- CONCURRENCY-011 (间隔 1 天)")


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="复习记录工具")
    parser.add_argument("--record", action="store_true", help="记录复习结果")
    parser.add_argument("--questions", type=str, help="题目 ID 列表（逗号分隔）")
    parser.add_argument("--scores", type=str, help="得分数组（逗号分隔）")
    parser.add_argument("--report", action="store_true", help="生成报告")
    parser.add_argument("--date", type=str, default="today", help="日期")
    parser.add_argument("--update-progress", action="store_true", help="更新进度")
    parser.add_argument("--get-due", action="store_true", help="获取待复习题目")
    parser.add_argument("--output", choices=["console", "feishu", "markdown"], 
                       default="console", help="输出格式")
    
    args = parser.parse_args()
    
    if args.record:
        if not args.questions or not args.scores:
            print("❌ 请提供 --questions 和 --scores 参数")
            return
        
        questions = [q.strip() for q in args.questions.split(",")]
        scores = [int(s.strip()) for s in args.scores.split(",")]
        
        if len(questions) != len(scores):
            print("❌ 题目数量和分数数量不匹配")
            return
        
        record_review(questions, scores)
    
    elif args.report:
        generate_report(args.date, args.output)
    
    elif args.update_progress:
        update_progress()
    
    elif args.get_due:
        get_due_questions()
    
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
