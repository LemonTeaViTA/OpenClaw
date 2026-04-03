#!/usr/bin/env python3
"""
Java 八股文复习脚本
从所有题库篇章中随机抽选题目进行复习
支持每日混合复习、按篇章复习、薄弱题强化
"""

import random
import re
import json
from pathlib import Path
from datetime import datetime

# 题库路径
QUESTION_BANK_PATH = Path("/root/.openclaw/workspace/01-Obsidian/40-Questions")
PROGRESS_FILE = QUESTION_BANK_PATH / "复习进度记录.md"

# 篇章配置（7 大板块）
SECTIONS = {
    "java-basic": {
        "file": "Java 基础篇 - 完整题库.md",
        "prefix": "JAVA",
        "name": "Java 基础",
    },
    "collection": {
        "file": "集合框架篇 - 完整题库.md",
        "prefix": "COLLECTION",
        "name": "集合框架",
    },
    "concurrency": {
        "file": "并发编程篇 - 完整题库.md",
        "prefix": "CONCURRENCY",
        "name": "并发编程",
    },
    "jvm": {
        "file": "JVM 篇 - 完整题库.md",
        "prefix": "JVM",
        "name": "JVM",
    },
    "redis": {
        "file": "Redis 篇 - 完整题库.md",
        "prefix": "REDIS",
        "name": "Redis",
    },
    "mysql": {
        "file": "MySQL 篇 - 完整题库.md",
        "prefix": "MYSQL",
        "name": "MySQL",
    },
    "spring": {
        "file": "Spring 篇 - 完整题库.md",
        "prefix": "SPRING",
        "name": "Spring",
    },
}


def parse_questions(file_path: Path, prefix: str) -> list:
    """解析题库文件，提取所有题目"""
    if not file_path.exists():
        print(f"⚠️  文件不存在：{file_path}")
        return []
    
    content = file_path.read_text(encoding="utf-8")
    questions = []
    
    # 匹配题目格式：### PREFIX-X：题目内容 或 ### PREFIX-XXX: 题目内容
    # 支持两种格式：JAVA-1: 和 JAVA-001:
    pattern = rf"###\s+({prefix}-\d+)\s*[:：]\s*(.+?)(?=###|\Z)"
    matches = re.findall(pattern, content, re.DOTALL | re.IGNORECASE)
    
    for match in matches:
        q_id, q_text = match
        # 标准化 ID 格式（如 JAVA-1 → JAVA-001）
        id_parts = q_id.strip().split("-")
        if len(id_parts) == 2:
            try:
                num = int(id_parts[1])
                standardized_id = f"{id_parts[0].upper()}-{num:03d}"
            except:
                standardized_id = q_id.strip().upper()
        else:
            standardized_id = q_id.strip().upper()
        
        # 提取题目（第一行，去掉 **答案：** 等标记）
        lines = q_text.strip().split("\n")
        question_text = lines[0].strip()
        # 如果第一行是空的，找下一行
        if not question_text or "**答案**" in question_text:
            for line in lines[1:]:
                if line.strip() and "**答案**" not in line:
                    question_text = line.strip()
                    break
        
        questions.append({
            "id": standardized_id,
            "question": question_text,
            "full_text": q_text.strip(),
            "prefix": prefix,
            "file": file_path.name,
        })
    
    return questions


def load_progress() -> dict:
    """加载复习进度"""
    progress = {
        "reviewed": {},  # {id: {"score": 5, "date": "2026-04-03", "count": 1}}
        "weak": [],  # 薄弱题目 ID 列表
    }
    
    if not PROGRESS_FILE.exists():
        return progress
    
    content = PROGRESS_FILE.read_text(encoding="utf-8")
    
    # 简单解析复习记录
    # 实际应该更完善，这里先返回空
    # TODO: 完善进度解析逻辑
    
    return progress


def save_progress(progress: dict):
    """保存复习进度"""
    # TODO: 实现进度保存
    pass


def select_questions(mode: str, count: int, sections: list = None) -> list:
    """
    根据模式选择题目的
    
    Args:
        mode: 复习模式 (daily, section, weak, random)
        count: 题目数量
        sections: 指定篇章列表
    
    Returns:
        选中的题目列表
    """
    progress = load_progress()
    all_questions = []
    
    # 确定要加载的篇章
    if mode == "section" and sections:
        target_sections = sections
    else:
        target_sections = list(SECTIONS.keys())
    
    # 加载题目
    for section_key in target_sections:
        if section_key not in SECTIONS:
            continue
        
        config = SECTIONS[section_key]
        file_path = QUESTION_BANK_PATH / config["file"]
        questions = parse_questions(file_path, config["prefix"])
        all_questions.extend(questions)
    
    if not all_questions:
        print("❌ 未找到任何题目")
        return []
    
    # 根据模式过滤
    if mode == "daily":
        # 每日复习：优先未复习的
        unreviewed = [q for q in all_questions if q["id"] not in progress["reviewed"]]
        
        if len(unreviewed) >= count:
            # 从未复习的中随机选择
            selected = random.sample(unreviewed, min(count, len(unreviewed)))
        else:
            # 不足则混合已复习的
            reviewed = [q for q in all_questions if q["id"] in progress["reviewed"]]
            selected = unreviewed + random.sample(reviewed, min(count - len(unreviewed), len(reviewed)))
    
    elif mode == "weak":
        # 薄弱题强化
        weak_questions = [q for q in all_questions if q["id"] in progress["weak"]]
        if weak_questions:
            selected = random.sample(weak_questions, min(count, len(weak_questions)))
        else:
            print("⚠️  暂无薄弱题目，切换到每日复习模式")
            selected = select_questions("daily", count, sections)
    
    elif mode == "random":
        # 完全随机
        selected = random.sample(all_questions, min(count, len(all_questions)))
    
    else:
        # 默认每日复习
        selected = select_questions("daily", count, sections)
    
    return selected


def display_questions(questions: list, output_mode: str = "console"):
    """显示题目"""
    if output_mode == "console":
        print(f"\n📚 今日复习计划（{len(questions)} 题）\n")
        print("=" * 60)
        
        for i, q in enumerate(questions, 1):
            print(f"\n【第{i}题】{q['id']}")
            print(f"篇章：{SECTIONS.get(q['prefix'].lower(), {}).get('name', '未知')}")
            print(f"题目：{q['question']}")
            print("-" * 60)
        
        print("\n💡 请依次回答以上问题")
        print("   输入 'next' 查看下一题，输入 'answer <题号>' 查看解析")
    
    elif output_mode == "json":
        # 输出 JSON 格式（供其他程序使用）
        output = {
            "mode": "daily",
            "count": len(questions),
            "questions": [
                {
                    "id": q["id"],
                    "question": q["question"],
                    "prefix": q["prefix"],
                }
                for q in questions
            ],
            "timestamp": datetime.now().isoformat(),
        }
        print(json.dumps(output, ensure_ascii=False, indent=2))


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Java 八股文复习")
    parser.add_argument("--mode", choices=["daily", "section", "weak", "random"], 
                       default="daily", help="复习模式")
    parser.add_argument("--count", type=int, default=10, help="复习题目数量")
    parser.add_argument("--section", type=str, help="指定篇章（逗号分隔）")
    parser.add_argument("--output", choices=["console", "json"], 
                       default="console", help="输出模式")
    parser.add_argument("--save", action="store_true", help="保存到临时文件")
    
    args = parser.parse_args()
    
    # 解析篇章参数
    sections = None
    if args.section:
        sections = [s.strip() for s in args.section.split(",")]
    
    # 选择题目的
    selected = select_questions(args.mode, args.count, sections)
    
    if not selected:
        print("❌ 未选到任何题目")
        return
    
    # 显示题目
    display_questions(selected, args.output)
    
    # 保存到临时文件
    if args.save:
        output_file = Path("/tmp/java-review-questions.json")
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump({
                "mode": args.mode,
                "count": args.count,
                "sections": sections,
                "questions": selected,
                "timestamp": datetime.now().isoformat(),
            }, f, ensure_ascii=False, indent=2)
        
        print(f"\n📝 题目已保存到：{output_file}")
    
    # 显示统计
    print("\n📊 选题统计:")
    section_count = {}
    for q in selected:
        prefix = q["prefix"]
        section_count[prefix] = section_count.get(prefix, 0) + 1
    
    for prefix, count in section_count.items():
        section_name = SECTIONS.get(prefix.lower(), {}).get("name", prefix)
        print(f"  {section_name}: {count}题")


if __name__ == "__main__":
    main()
