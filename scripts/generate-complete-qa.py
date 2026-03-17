#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
重新生成题库 + 补充答案（最终版）
直接从 PDF 提取问答对，生成完整题库
"""

import fitz
import re
import sys
from pathlib import Path
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8')

PDF_DIR = Path(r"C:\Users\11237\.openclaw-autoclaw\workspace\files\java-notes\renamed")
OUTPUT_DIR = Path(r"C:\Users\11237\.openclaw-autoclaw\workspace\Obsidian\40-Questions")

def extract_qa_from_pdf(pdf_path):
    """从 PDF 提取问答对"""
    doc = fitz.open(pdf_path)
    full_text = ""
    
    for page in doc:
        full_text += page.get_text()
    
    doc.close()
    
    # 按行处理
    lines = full_text.split('\n')
    
    qa_pairs = []
    current_chapter = None
    current_q = None
    current_a = []
    
    for line in lines:
        line = line.strip()
        
        # 跳过页眉页脚
        if '⾯渣逆袭' in line or line.startswith('No.'):
            continue
        
        # 检测章节
        if re.match(r'^[⼀⼆三四五六七八九十⼤]+、\s*.+$', line):
            current_chapter = line
            continue
        
        # 检测问题
        if re.match(r'^\d+\..*[？?].*$', line):
            # 保存上一个
            if current_q and current_a:
                qa_pairs.append({
                    'chapter': current_chapter,
                    'question': current_q,
                    'answer': '\n'.join(current_a)
                })
            
            # 新问题
            current_q = re.sub(r'^\d+\.\s*', '', line)
            current_a = []
        elif current_q:
            # 收集答案
            if len(line) > 10 and '推荐阅读' not in line and 'Java 面试指南' not in line:
                current_a.append(line)
    
    # 保存最后一个
    if current_q and current_a:
        qa_pairs.append({
            'chapter': current_chapter,
            'question': current_q,
            'answer': '\n'.join(current_a)
        })
    
    return qa_pairs

def generate_markdown(module_name, qa_pairs):
    """生成带答案的 Markdown"""
    lines = []
    lines.append(f"# {module_name} - 完整面试题库（含答案）")
    lines.append("")
    lines.append(f"> 来源：面渣逆袭 {module_name} V2.1")
    lines.append(f"> 整理时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"> 题数：{len(qa_pairs)} 题")
    lines.append(f"> 状态：✅ 答案已补充")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    # 按章节组织
    chapters = {}
    for qa in qa_pairs:
        chapter = qa['chapter'] or "未分类"
        if chapter not in chapters:
            chapters[chapter] = []
        chapters[chapter].append(qa)
    
    for i, (chapter, qas) in enumerate(chapters.items(), 1):
        lines.append(f"## {i}. {chapter}")
        lines.append("")
        
        for j, qa in enumerate(qas, 1):
            lines.append(f"### 题{j}：{qa['question']}")
            lines.append("")
            lines.append("**答案：**")
            lines.append("")
            lines.append(qa['answer'])
            lines.append("")
            lines.append("---")
            lines.append("")
    
    return '\n'.join(lines)

def main():
    print("=" * 70)
    print("Generate Complete Q&A Files")
    print("=" * 70)
    print()
    
    modules = {
        "01-java-basics.pdf": "Java 基础篇",
        "02-jvm.pdf": "JVM 篇",
        "04-collection.pdf": "集合框架篇",
    }
    
    total = 0
    
    for pdf_file, module_name in modules.items():
        pdf_path = PDF_DIR / pdf_file
        if not pdf_path.exists():
            print(f"Skip: {pdf_file}")
            continue
        
        print(f"Processing: {module_name}")
        
        # 提取
        qa_pairs = extract_qa_from_pdf(pdf_path)
        total += len(qa_pairs)
        
        # 生成
        md_content = generate_markdown(module_name, qa_pairs)
        
        # 保存（覆盖旧文件）
        output_file = OUTPUT_DIR / f"{module_name} - 完整题库.md"
        output_file.write_text(md_content, encoding='utf-8')
        
        print(f"  Saved: {output_file.name} ({len(qa_pairs)} 题)")
        print()
    
    print("=" * 70)
    print(f"Total: {total} Q&A pairs")
    print("=" * 70)

if __name__ == "__main__":
    main()
