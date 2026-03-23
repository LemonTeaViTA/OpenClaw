#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
对比 Obsidian 已整理题目 vs PDF 提取题目
找出遗漏的题目
"""

import re
from pathlib import Path

# Obsidian 已整理题目
OBSIDIAN_FILE = Path(r"C:\Users\11237\.openclaw-autoclaw\workspace\Obsidian\40-Questions\Java 基础篇 -56 题.md")

# PDF 提取题目
PDF_QUESTIONS_FILE = Path(r"C:\Users\11237\.openclaw-autoclaw\workspace\memory\pdf-extracted\Java 基础篇-questions.md")

# 输出
OUTPUT_DIR = Path(r"C:\Users\11237\.openclaw-autoclaw\workspace\memory\pdf-extracted")

def extract_questions_from_markdown(md_file):
    """从 Markdown 文件中提取题号"""
    if not md_file.exists():
        return []
    
    content = md_file.read_text(encoding='utf-8')
    
    # 模式：### 题 X：
    pattern = r'### 题\s*(\d+)[：:]\s*'
    matches = re.findall(pattern, content)
    
    return sorted([int(x) for x in matches])

def extract_pdf_questions(q_file):
    """从 PDF 提取的题目文件中提取题号"""
    if not q_file.exists():
        return []
    
    content = q_file.read_text(encoding='utf-8')
    
    # 模式：### 题 X
    pattern = r'### 题\s*(\d+)'
    matches = re.findall(pattern, content)
    
    return sorted([int(x) for x in matches])

def main():
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    
    print("=" * 70)
    print("对比：Obsidian 已整理 vs PDF 提取")
    print("=" * 70)
    print()
    
    # 提取题号
    obsidian_nums = extract_questions_from_markdown(OBSIDIAN_FILE)
    pdf_nums = extract_pdf_questions(PDF_QUESTIONS_FILE)
    
    print(f"Obsidian 已整理：{len(obsidian_nums)} 题")
    print(f"  题号范围：{min(obsidian_nums)}-{max(obsidian_nums)}")
    print()
    
    print(f"PDF 提取：{len(pdf_nums)} 题")
    print(f"  题号范围：{min(pdf_nums)}-{max(pdf_nums)}")
    print()
    
    # 对比
    obsidian_set = set(obsidian_nums)
    pdf_set = set(pdf_nums)
    
    # PDF 有但 Obsidian 没有（遗漏）
    missing_in_obsidian = sorted(pdf_set - obsidian_set)
    
    # Obsidian 有但 PDF 没有（可能题号不一致）
    missing_in_pdf = sorted(obsidian_set - pdf_set)
    
    # 共同题目
    common = sorted(obsidian_set & pdf_set)
    
    print("=" * 70)
    print("对比结果")
    print("=" * 70)
    print()
    
    print(f"✅ 共同题目：{len(common)} 题")
    if common:
        print(f"  题号：{common[:20]}...")
    print()
    
    print(f"⚠️  PDF 有但 Obsidian 没有（可能遗漏）：{len(missing_in_obsidian)} 题")
    if missing_in_obsidian:
        print(f"  题号：{missing_in_obsidian[:30]}...")
        if len(missing_in_obsidian) > 30:
            print(f"  ... 还有 {len(missing_in_obsidian) - 30} 题")
    print()
    
    print(f"❓ Obsidian 有但 PDF 没有（题号不一致？）：{len(missing_in_pdf)} 题")
    if missing_in_pdf:
        print(f"  题号：{missing_in_pdf[:20]}...")
    print()
    
    # 生成报告
    report = []
    report.append("# 📋 题目对比报告")
    report.append("")
    report.append("## 统计")
    report.append("")
    report.append(f"- Obsidian 已整理：{len(obsidian_nums)} 题")
    report.append(f"- PDF 提取：{len(pdf_nums)} 题")
    report.append(f"- 共同题目：{len(common)} 题")
    report.append(f"- PDF 有但 Obsidian 没有：{len(missing_in_obsidian)} 题")
    report.append(f"- Obsidian 有但 PDF 没有：{len(missing_in_pdf)} 题")
    report.append("")
    report.append("---")
    report.append("")
    
    if missing_in_obsidian:
        report.append("## ⚠️ 可能遗漏的题目（PDF 有但 Obsidian 没有）")
        report.append("")
        report.append("题号：")
        for i in range(0, len(missing_in_obsidian), 10):
            batch = missing_in_obsidian[i:i+10]
            report.append(", ".join(map(str, batch)))
        report.append("")
    report.append("---")
    report.append("")
    
    if missing_in_pdf:
        report.append("## ❓ Obsidian 有但 PDF 没有（题号可能不一致）")
        report.append("")
        report.append("题号：")
        for i in range(0, len(missing_in_pdf), 10):
            batch = missing_in_pdf[i:i+10]
            report.append(", ".join(map(str, batch)))
        report.append("")
    
    report_file = OUTPUT_DIR / "对比报告-Obsidian-vs-PDF.md"
    report_file.write_text('\n'.join(report), encoding='utf-8')
    
    print(f"Saved: {report_file.name}")
    print()
    print("=" * 70)

if __name__ == "__main__":
    main()
