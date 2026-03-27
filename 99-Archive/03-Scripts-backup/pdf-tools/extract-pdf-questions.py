#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
从 PDF 提取完整文本 + 题目清单（改进版）
"""

import fitz
import re
from pathlib import Path
from datetime import datetime

PDF_DIR = Path(r"C:\Users\11237\.openclaw-autoclaw\workspace\files\java-notes\renamed")
OUTPUT_DIR = Path(r"C:\Users\11237\.openclaw-autoclaw\workspace\memory\pdf-extracted")
OUTPUT_DIR.mkdir(exist_ok=True)

PDF_CONFIG = {
    "01-java-basics.pdf": {"name": "Java 基础篇", "pages": 95},
    "02-jvm.pdf": {"name": "JVM 篇", "pages": 95},
    "03-concurrent.pdf": {"name": "并发编程篇", "pages": 177},
    "04-collection.pdf": {"name": "集合框架篇", "pages": 63},
    "05-mysql.pdf": {"name": "MySQL 篇", "pages": 302},
    "06-redis.pdf": {"name": "Redis 篇", "pages": 261},
    "07-spring.pdf": {"name": "Spring 篇", "pages": 180},
}

def extract_pdf_text(pdf_path):
    """提取 PDF 完整文本"""
    doc = fitz.open(pdf_path)
    text_pages = []
    
    for i, page in enumerate(doc):
        page_text = page.get_text()
        text_pages.append(f"## 第{i+1}页\n\n{page_text}")
    
    doc.close()
    return '\n'.join(text_pages)

def extract_questions_v2(text):
    """改进版：提取题目"""
    questions = []
    
    # 模式 1: "1. 什么是 Java？" 或 "1、什么是 Java？"
    pattern1 = r'^(\d+)[.、]\s*(.+?)(?=\n\d+[.、]|\n##|\Z)'
    matches = re.findall(pattern1, text, re.MULTILINE | re.DOTALL)
    
    for q_num, q_text in matches:
        q_text = q_text.strip().split('\n')[0][:500]
        questions.append({
            'num': int(q_num),
            'text': q_text,
            'source': 'pattern1'
        })
    
    # 模式 2: "题 1：xxx"
    pattern2 = r'题\s*(\d+)[：:.:]\s*(.+?)(?=\n题\s*\d+|\n##|\Z)'
    matches = re.findall(pattern2, text, re.DOTALL)
    
    for q_num, q_text in matches:
        q_text = q_text.strip().split('\n')[0][:500]
        questions.append({
            'num': int(q_num),
            'text': q_text,
            'source': 'pattern2'
        })
    
    # 去重（按题号）
    seen = set()
    unique = []
    for q in questions:
        key = (q['num'], q['text'][:50])
        if key not in seen:
            seen.add(key)
            unique.append(q)
    
    return sorted(unique, key=lambda x: x['num'])

def main():
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    
    print("=" * 70)
    print("PDF Text Extraction + Question Analysis (v2)")
    print("=" * 70)
    print()
    
    all_results = {}
    
    for pdf_file, config in PDF_CONFIG.items():
        pdf_path = PDF_DIR / pdf_file
        if not pdf_path.exists():
            print(f"Skip: {pdf_file}")
            continue
        
        print(f"Processing: {config['name']}")
        
        # 提取文本
        full_text = extract_pdf_text(pdf_path)
        
        # 保存完整文本
        text_file = OUTPUT_DIR / f"{config['name']}-full-text.md"
        text_file.write_text(full_text, encoding='utf-8')
        print(f"  Saved: {text_file.name} ({len(full_text):,} chars)")
        
        # 提取题目
        questions = extract_questions_v2(full_text)
        
        # 保存题目清单
        q_lines = []
        for q in questions:
            q_lines.append(f"### 题{q['num']}\n\n{q['text']}\n")
        
        q_file = OUTPUT_DIR / f"{config['name']}-questions.md"
        q_file.write_text('\n'.join(q_lines), encoding='utf-8')
        print(f"  Extracted: {len(questions)} questions")
        
        all_results[config['name']] = {
            'pdf': pdf_file,
            'pages': config['pages'],
            'total_chars': len(full_text),
            'total_questions': len(questions),
            'questions': questions
        }
        
        print()
    
    # 生成报告
    print("Generating report...")
    report = generate_report(all_results)
    report_file = OUTPUT_DIR / "对比报告-v2.md"
    report_file.write_text(report, encoding='utf-8')
    print(f"Saved: {report_file.name}")
    
    print()
    print("=" * 70)
    print("Completed!")
    print("=" * 70)

def generate_report(all_results):
    """生成对比报告"""
    report = []
    report.append("# 📚 PDF 提取文本 + 题目对比报告 (v2)")
    report.append("")
    report.append(f"> 生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append("> 来源：PyMuPDF 直接提取")
    report.append("")
    report.append("---")
    report.append("")
    
    # 统计
    report.append("## 📊 总体统计")
    report.append("")
    report.append("| PDF 模块 | 页数 | 字符数 | 题目数 |")
    report.append("|---------|------|--------|--------|")
    
    total = 0
    for module, data in all_results.items():
        report.append(f"| {module} | {data['pages']} | {data['total_chars']:,} | {data['total_questions']} |")
        total += data['total_questions']
    
    report.append(f"| **总计** | - | - | **{total}** |")
    report.append("")
    report.append("---")
    report.append("")
    
    # 详细
    for module, data in all_results.items():
        report.append(f"## {module}")
        report.append("")
        report.append(f"- **PDF**: {data['pdf']}")
        report.append(f"- **题目数**: {data['total_questions']}")
        report.append(f"- **完整文本**: `{module}-full-text.md`")
        report.append(f"- **题目清单**: `{module}-questions.md`")
        report.append("")
        
        # 预览前 10 题
        qs = data['questions'][:10]
        if qs:
            report.append("**前 10 题：**")
            report.append("")
            for q in qs:
                report.append(f"- 题{q['num']}：{q['text'][:60]}...")
            report.append("")
        
        report.append("---")
        report.append("")
    
    return '\n'.join(report)

if __name__ == "__main__":
    main()
