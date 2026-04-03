#!/usr/bin/env python3
"""
Java 八股文复习脚本
从题库中随机抽选题目进行复习
"""

import random
import re
import json
from pathlib import Path
from datetime import datetime

# 题库路径
QUESTION_BANK_PATH = Path("/root/.openclaw/workspace/01-Obsidian/40-Questions/Java 八股文题库")
PROGRESS_FILE = Path("/root/.openclaw/workspace/01-Obsidian/40-Questions/复习进度记录.md")

# 篇章映射
SECTIONS = {
    "java-basic": "01-Java 基础篇.md",
    "collection": "02-集合框架篇.md",
    "concurrency": "03-并发编程篇.md",
    "jvm": "04-JVM 篇.md",
    "redis": "05-Redis 篇.md",
    "mysql": "06-MySQL 篇.md",
    "spring": "07-Spring 篇.md",
}

# ID 前缀映射
ID_PREFIXES = {
    "java-basic": "JAVA",
    "collection": "COLLECTION",
    "concurrency": "CONCURRENCY",
    "jvm": "JVM",
    "redis": "REDIS",
    "mysql": "MYSQL",
    "spring": "SPRING",
}


def parse_questions(file_path: Path) -> list:
    """解析题库文件，提取所有题目"""
    if not file_path.exists():
        return []
    
    content = file_path.read_text(encoding="utf-8")
    questions = []
    
    # 匹配题目格式：### ID: 题目内容
    pattern = r"###\s+([A-Z]+-\d+):\s*(.+?)(?=###|\Z)"
    matches = re.findall(pattern, content, re.DOTALL)
    
    for match in matches:
        q_id, q_text = match
        questions.append({
            "id": q_id.strip(),
            "question": q_text.strip().split("\n")[0],  # 只取第一行作为题目
            "file": file_path.name,
        })
    
    return questions


def load_progress() -> dict:
    """加载复习进度"""
    if not PROGRESS_FILE.exists():
        return {"reviewed": [], "mastered": [], "weak": []}
    
    content = PROGRESS_FILE.read_text(encoding="utf-8")
    progress = {
        "reviewed": [],
        "mastered": [],
        "weak": [],
    }
    
    # 简单解析，实际应该更完善
    # 这里只是示例
    return progress


def select_questions(mode: str, count: int, section: str = None) -> list:
    """根据模式选择题目的"""
    progress = load_progress()
    questions = []
    
    if mode == "section" and section:
        # 指定篇章
        if section in SECTIONS:
            file_path = QUESTION_BANK_PATH / SECTIONS[section]
            questions = parse_questions(file_path)
    elif mode == "weak":
        # 薄弱题目
        # 从 progress["weak"] 中获取
        questions = []  # TODO: 实现薄弱题目获取
    else:
        # 每日复习或随机 - 混合所有篇章
        for section_file in SECTIONS.values():
            file_path = QUESTION_BANK_PATH / section_file
            questions.extend(parse_questions(file_path))
    
    # 过滤已复习的题目（根据模式）
    if mode in ["daily", "random"]:
        # 优先选择未复习的
        unreviewed = [q for q in questions if q["id"] not in progress["reviewed"]]
        if len(unreviewed) >= count:
            questions = unreviewed
        else:
            # 不足则混合已复习的
            questions = unreviewed + [q for q in questions if q["id"] in progress["reviewed"]]
    
    # 随机选择
    selected = random.sample(questions, min(count, len(questions)))
    return selected


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Java 八股文复习")
    parser.add_argument("--mode", choices=["daily", "section", "weak", "random"], 
                       default="daily", help="复习模式")
    parser.add_argument("--count", type=int, default=10, help="复习题目数量")
    parser.add_argument("--section", choices=list(SECTIONS.keys()), 
                       help="指定篇章")
    parser.add_argument("--output", choices=["console", "feishu", "wecom"], 
                       default="console", help="输出模式")
    
    args = parser.parse_args()
    
    # 选择题目的
    selected = select_questions(args.mode, args.count, args.section)
    
    # 输出题目
    print(f"\n📚 今日复习计划（{len(selected)} 题）\n")
    print("=" * 60)
    
    for i, q in enumerate(selected, 1):
        print(f"\n【第{i}题】{q['id']}")
        print(f"题目：{q['question']}")
        print("-" * 60)
    
    print("\n💡 请依次回答以上问题，回答后输入 'next' 继续")
    
    # 保存到临时文件供后续使用
    output_file = Path("/tmp/java-review-questions.json")
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump({
            "mode": args.mode,
            "count": args.count,
            "questions": selected,
            "timestamp": datetime.now().isoformat(),
        }, f, ensure_ascii=False, indent=2)
    
    print(f"\n📝 题目已保存到：{output_file}")


if __name__ == "__main__":
    main()
