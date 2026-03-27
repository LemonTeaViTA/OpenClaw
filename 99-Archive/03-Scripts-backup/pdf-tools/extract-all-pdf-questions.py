#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
提取所有 PDF 的完整题目清单（最终版）
按章节标题组织
"""

import fitz
import re
import sys
from pathlib import Path
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8')

PDF_DIR = Path(r"C:\Users\11237\.openclaw-autoclaw\workspace\files\java-notes\renamed")
OUTPUT_DIR = Path(r"C:\Users\11237\.openclaw-autoclaw\workspace\Obsidian\40-Questions")
OUTPUT_DIR.mkdir(exist_ok=True)

PDF_CONFIG = {
    "01-java-basics.pdf": {"name": "Java 基础篇", "output": "Java 基础篇 - 完整题库.md"},
    "02-jvm.pdf": {"name": "JVM 篇", "output": "JVM 篇 - 完整题库.md"},
    "03-concurrent.pdf": {"name": "并发编程篇", "output": "并发编程篇 - 完整题库.md"},
    "04-collection.pdf": {"name": "集合框架篇", "output": "集合框架篇 - 完整题库.md"},
    "05-mysql.pdf": {"name": "MySQL 篇", "output": "MySQL 篇 - 完整题库.md"},
    "06-redis.pdf": {"name": "Redis 篇", "output": "Redis 篇 - 完整题库.md"},
    "07-spring.pdf": {"name": "Spring 篇", "output": "Spring 篇 - 完整题库.md"},
}

def extract_questions_from_pdf(pdf_path):
    """从 PDF 提取题目"""
    doc = fitz.open(pdf_path)
    
    questions = []
    current_chapter = None
    chapter_num = 0
    
    for page_num, page in enumerate(doc):
        text = page.get_text()
        lines = text.split('\n')
        
        for line in lines:
            line = line.strip()
            
            # 跳过页眉页脚
            if '⾯渣逆袭' in line or line.startswith('No.'):
                continue
            
            # 检测大章节（如 "Java 概述"）
            if re.match(r'^[⼀⼆三四五六七八九十⼤]+、\s*.+$', line):
                chapter_num += 1
                current_chapter = line
                continue
            
            # 检测带编号的章节（如 "1. Java 概述"）
            if re.match(r'^\d+\.\s+[⼀⼆三四五六七八九十⼤ A-Za-z].+$', line) and not ('?' in line or '？' in line):
                if not current_chapter or line not in current_chapter:
                    chapter_num += 1
                    current_chapter = line
                continue
            
            # 检测题目（数字 + 点 + 问题 + 问号）
            q_match = re.match(r'^(\d+)\.([^0-9].*[？?].*)$', line)
            if q_match and current_chapter:
                q_num = int(q_match.group(1))
                q_text = q_match.group(2).strip()
                
                # 过滤
                if len(q_text) < 5 or len(q_text) > 300:
                    continue
                if 'Java 面试指南' in q_text:
                    continue
                if '推荐阅读' in q_text:
                    continue
                
                questions.append({
                    'chapter_num': chapter_num,
                    'chapter': current_chapter,
                    'num': q_num,
                    'text': q_text,
                    'page': page_num + 1
                })
    
    doc.close()
    
    # 去重
    seen = set()
    unique = []
    for q in questions:
        key = (q['chapter_num'], q['num'], q['text'][:50])
        if key not in seen:
            seen.add(key)
            unique.append(q)
    
    return sorted(unique, key=lambda x: (x['chapter_num'], x['num']))

def generate_markdown(module_name, questions):
    """生成 Markdown 文件"""
    lines = []
    lines.append(f"# {module_name} - 完整面试题库")
    lines.append("")
    lines.append(f"> 来源：面渣逆袭 {module_name} V2.1")
    lines.append(f"> 提取时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"> 题数：{len(questions)} 题")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    # 按章节组织
    chapters = {}
    for q in questions:
        chapter = f"{q['chapter_num']}. {q['chapter']}"
        if chapter not in chapters:
            chapters[chapter] = []
        chapters[chapter].append(q)
    
    for chapter, qs in chapters.items():
        lines.append(f"## {chapter}")
        lines.append("")
        
        for q in qs:
            lines.append(f"### 题{q['num']}：{q['text']}")
            lines.append("")
            lines.append("**答案：**")
            lines.append("")
            lines.append("*(待补充)*")
            lines.append("")
            lines.append("---")
            lines.append("")
    
    return '\n'.join(lines)

def main():
    print("=" * 70)
    print("Extract All PDF Questions (Final)")
    print("=" * 70)
    print()
    
    total_questions = 0
    results = {}
    
    for pdf_file, config in PDF_CONFIG.items():
        pdf_path = PDF_DIR / pdf_file
        if not pdf_path.exists():
            print(f"Skip: {pdf_file}")
            continue
        
        print(f"Processing: {config['name']}")
        
        # 提取
        questions = extract_questions_from_pdf(pdf_path)
        total_questions += len(questions)
        results[config['name']] = len(questions)
        
        # 生成 Markdown
        md_content = generate_markdown(config['name'], questions)
        
        # 保存
        output_file = OUTPUT_DIR / config['output']
        output_file.write_text(md_content, encoding='utf-8')
        
        print(f"  Saved: {config['output']} ({len(questions)} 题)")
        print()
    
    print("=" * 70)
    print("Summary:")
    for name, count in results.items():
        print(f"  {name}: {count} 题")
    print(f"Total: {total_questions} 题")
    print("=" * 70)

if __name__ == "__main__":
    main()
