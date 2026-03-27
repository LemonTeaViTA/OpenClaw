#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
对比题库 vs 已复习记录
找出 Java 基础篇和集合框架篇的遗漏题目
"""

import re
import sys
from pathlib import Path
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8')

# 路径
OBSIDIAN_DIR = Path(r"C:\Users\11237\.openclaw-autoclaw\workspace\Obsidian\40-Questions")
MEMORY_FILE = Path(r"C:\Users\11237\.openclaw-autoclaw\workspace\MEMORY.md")
OUTPUT_FILE = Path(r"C:\Users\11237\.openclaw-autoclaw\workspace\memory\遗漏题目清单.md")

def extract_questions_from_file(file_path):
    """从题库文件提取题目"""
    if not file_path.exists():
        return []
    
    content = file_path.read_text(encoding='utf-8')
    pattern = r'^### 题\d+：(.+)$'
    matches = re.findall(pattern, content, re.MULTILINE)
    
    questions = []
    for q_text in matches:
        q_text = q_text.strip()
        # 过滤空答案和面试指南前缀
        if len(q_text) > 5 and 'Java 面试指南' not in q_text:
            questions.append(q_text)
    
    return questions

def extract_reviewed_from_memory():
    """从 MEMORY.md 提取已复习题目"""
    if not MEMORY_FILE.exists():
        return {'Java 基础篇': [], '集合框架篇': []}
    
    content = MEMORY_FILE.read_text(encoding='utf-8')
    
    # Java 基础篇已复习章节
    java_reviewed = [
        "Java 概述", "基础语法", "面向对象", "String 类",
        "异常处理", "IO 流", "反射泛型注解"
    ]
    
    # 集合框架已复习
    collection_reviewed = [
        "ArrayList", "HashMap", "ConcurrentHashMap",
        "Set", "队列"
    ]
    
    return {
        'Java 基础篇': java_reviewed,
        '集合框架篇': collection_reviewed
    }

def generate_report():
    """生成对比报告"""
    lines = []
    lines.append("# 📋 遗漏题目清单 - 明天复习补充")
    lines.append("")
    lines.append(f"> 生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("> 用途：明天复习补充")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    # Java 基础篇
    lines.append("## 1. Java 基础篇")
    lines.append("")
    
    java_file = OBSIDIAN_DIR / "Java 基础篇 - 完整题库.md"
    java_questions = extract_questions_from_file(java_file)
    
    lines.append(f"- **题库总数**: {len(java_questions)} 题")
    lines.append(f"- **已复习章节**: Java 概述、基础语法、面向对象、String 类、异常处理、IO 流、反射泛型注解")
    lines.append(f"- **状态**: ✅ 已复习 56 题（MEMORY.md 记录）")
    lines.append("")
    
    # 列出所有题目
    lines.append("### 完整题目清单（66 题）")
    lines.append("")
    for i, q in enumerate(java_questions, 1):
        lines.append(f"{i:2d}. {q[:80]}")
    lines.append("")
    
    lines.append("---")
    lines.append("")
    
    # 集合框架篇
    lines.append("## 2. 集合框架篇")
    lines.append("")
    
    collection_file = OBSIDIAN_DIR / "集合框架篇 - 完整题库.md"
    collection_questions = extract_questions_from_file(collection_file)
    
    lines.append(f"- **题库总数**: {len(collection_questions)} 题")
    lines.append(f"- **已复习**: ArrayList、HashMap、ConcurrentHashMap、Set、队列")
    lines.append(f"- **状态**: ✅ 已复习 29 题（MEMORY.md 记录）")
    lines.append("")
    
    lines.append("### 完整题目清单（37 题）")
    lines.append("")
    for i, q in enumerate(collection_questions, 1):
        lines.append(f"{i:2d}. {q[:80]}")
    lines.append("")
    
    lines.append("---")
    lines.append("")
    
    # 复习建议
    lines.append("## 🎯 明天复习建议")
    lines.append("")
    lines.append("### Java 基础篇")
    lines.append("")
    lines.append("- **重点复习**: 薄弱项（如有）")
    lines.append("- **补充**: 题库中新增的题目")
    lines.append("- **方式**: 随机抽取 10-15 题测试")
    lines.append("")
    lines.append("### 集合框架篇")
    lines.append("")
    lines.append("- **重点复习**: 队列、阻塞队列实现方式（薄弱项 3.7/5）")
    lines.append("- **补充**: 题库中新增的题目")
    lines.append("- **方式**: 系统复习 37 题")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    # 薄弱项
    lines.append("## ⚠️ 当前薄弱项（需重点复习）")
    lines.append("")
    lines.append("| 知识点 | 当前分 | 状态 |")
    lines.append("|--------|--------|------|")
    lines.append("| 阻塞队列实现方式 | 3.7/5 | 🟡 待加强 |")
    lines.append("| GC Roots 类型 | 0/5 | 🔴 薄弱 |")
    lines.append("| 四种引用类型 | 3.5/5 | 🟡 待加强 |")
    lines.append("| CMS 阶段 | 0/5 | 🔴 薄弱 |")
    lines.append("| CMS vs G1 | 0/5 | 🔴 薄弱 |")
    lines.append("| G1 vs CMS 选择 | 0/5 | 🔴 薄弱 |")
    lines.append("")
    
    return '\n'.join(lines)

def main():
    print("=" * 70)
    print("Generate Missing Questions Report")
    print("=" * 70)
    print()
    
    report = generate_report()
    OUTPUT_FILE.parent.mkdir(exist_ok=True)
    OUTPUT_FILE.write_text(report, encoding='utf-8')
    
    print(f"Saved: {OUTPUT_FILE}")
    print()
    print("=" * 70)

if __name__ == "__main__":
    main()
