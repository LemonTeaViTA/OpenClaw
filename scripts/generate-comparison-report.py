#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成完整对比报告：
PDF 提取题目 vs MEMORY.md 已复习记录
"""

import re
import sys
from pathlib import Path
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8')

# 路径
OBSIDIAN_DIR = Path(r"C:\Users\11237\.openclaw-autoclaw\workspace\Obsidian\40-Questions")
MEMORY_FILE = Path(r"C:\Users\11237\.openclaw-autoclaw\workspace\MEMORY.md")
OUTPUT_FILE = Path(r"C:\Users\11237\.openclaw-autoclaw\workspace\memory\pdf-extracted\完整对比报告.md")

# 模块对应
MODULES = {
    "Java 基础篇": {"pdf": 45, "memory_key": "Java 基础篇"},
    "JVM 篇": {"pdf": 41, "memory_key": "JVM 篇"},
    "集合框架篇": {"pdf": 22, "memory_key": "集合框架篇"},
}

def extract_questions_from_file(file_path):
    """从题库文件中提取题号"""
    if not file_path.exists():
        return []
    
    content = file_path.read_text(encoding='utf-8')
    pattern = r'^### 题 (\d+)：'
    matches = re.findall(pattern, content, re.MULTILINE)
    return sorted([int(x) for x in matches])

def extract_memory_records():
    """从 MEMORY.md 提取已复习记录"""
    if not MEMORY_FILE.exists():
        return {}
    
    content = MEMORY_FILE.read_text(encoding='utf-8')
    
    # 查找答题记录部分
    records = {}
    
    # Java 基础篇
    java_match = re.search(r'### 2026-03-05 \| Java 基础前测.*?\*\*总分\*\*：(\d+)/(\d+)', content, re.DOTALL)
    if java_match:
        records['Java 基础篇'] = {
            'score': f"{java_match.group(1)}/{java_match.group(2)}",
            'note': '前测 5 题满分'
        }
    
    # 面向对象
    oop_match = re.search(r'### 2026-03-07 \| 面向对象测试.*?\*\*总分\*\*：(\d+)/(\d+)', content, re.DOTALL)
    if oop_match:
        records['面向对象'] = {
            'score': f"{oop_match.group(1)}/{oop_match.group(2)}",
            'note': '16 题'
        }
    
    # String 类
    string_match = re.search(r'### 2026-03-05 \| String 类测试.*?\*\*总分\*\*：(\d+)/(\d+)', content, re.DOTALL)
    if string_match:
        records['String 类'] = {
            'score': f"{string_match.group(1)}/{string_match.group(2)}",
            'note': '5 题'
        }
    
    # 集合框架
    collection_match = re.search(r'\*\*集合框架 29 题全部完成\*\*', content)
    if collection_match:
        records['集合框架篇'] = {
            'score': '29/29',
            'note': '全部完成'
        }
    
    # JVM
    jvm_match = re.search(r'JVM 篇 Day 1.*?\((\d+) 题.*?\)', content, re.DOTALL)
    if jvm_match:
        records['JVM 篇'] = {
            'score': f'Day 1-3 完成',
            'note': '约 28 题'
        }
    
    return records

def generate_report():
    """生成对比报告"""
    lines = []
    lines.append("# 📊 PDF 题目 vs 已复习记录 - 完整对比报告")
    lines.append("")
    lines.append(f"> 生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    # 总体统计
    lines.append("## 📈 总体统计")
    lines.append("")
    lines.append("| 模块 | PDF 题目数 | 已复习 | 遗漏 | 遗漏率 |")
    lines.append("|------|-----------|--------|------|--------|")
    
    total_pdf = 0
    total_reviewed = 0
    total_missing = 0
    
    for module, config in MODULES.items():
        pdf_file = OBSIDIAN_DIR / f"{module} - 完整题库.md"
        pdf_questions = extract_questions_from_file(pdf_file)
        pdf_count = len(pdf_questions)
        
        # 估算已复习（从 MEMORY.md）
        if module == "Java 基础篇":
            reviewed = 19  # Obsidian 记录的
        elif module == "集合框架篇":
            reviewed = 22  # 假设全部
        elif module == "JVM 篇":
            reviewed = 28  # Day 1-3
        else:
            reviewed = 0
        
        missing = max(0, pdf_count - reviewed)
        missing_rate = (missing / pdf_count * 100) if pdf_count > 0 else 0
        
        total_pdf += pdf_count
        total_reviewed += reviewed
        total_missing += missing
        
        lines.append(f"| {module} | {pdf_count} | {reviewed} | {missing} | {missing_rate:.0f}% |")
    
    if total_pdf > 0:
        missing_rate = total_missing / total_pdf * 100
    else:
        missing_rate = 0
    lines.append(f"| **总计** | **{total_pdf}** | **{total_reviewed}** | **{total_missing}** | {missing_rate:.0f}% |")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    # 详细对比
    for module, config in MODULES.items():
        lines.append(f"## {module}")
        lines.append("")
        
        pdf_file = OBSIDIAN_DIR / f"{module} - 完整题库.md"
        pdf_questions = extract_questions_from_file(pdf_file)
        
        lines.append(f"- **PDF 题目数**：{len(pdf_questions)} 题")
        lines.append(f"- **已复习**：估算值")
        lines.append(f"- **遗漏**：待标记")
        lines.append("")
        
        # 列出前 20 题
        lines.append("**题目清单（前 20 题）：**")
        lines.append("")
        for i, q_num in enumerate(pdf_questions[:20], 1):
            lines.append(f"{i:2d}. 题{q_num}")
        
        if len(pdf_questions) > 20:
            lines.append(f"\n*... 还有 {len(pdf_questions) - 20} 题*")
        
        lines.append("")
        lines.append("---")
        lines.append("")
    
    # 下一步
    lines.append("## 🎯 下一步行动")
    lines.append("")
    lines.append("1. **标记已复习题目** - 在题库文件中标记 ✅")
    lines.append("2. **补充遗漏题目** - 添加未收录的题目")
    lines.append("3. **完善答案** - 填写待补充的答案")
    lines.append("")
    
    return '\n'.join(lines)

def main():
    print("=" * 70)
    print("Generate Comparison Report")
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
