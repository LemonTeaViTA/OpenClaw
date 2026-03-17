#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
从 PDF 完整文本提取答案
补充到 Obsidian 题库文件
"""

import fitz
import re
import sys
from pathlib import Path
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8')

PDF_DIR = Path(r"C:\Users\11237\.openclaw-autoclaw\workspace\files\java-notes\renamed")
OBSIDIAN_DIR = Path(r"C:\Users\11237\.openclaw-autoclaw\workspace\Obsidian\40-Questions")

def extract_qa_from_pdf(pdf_path):
    """从 PDF 提取问答对"""
    doc = fitz.open(pdf_path)
    full_text = ""
    
    for page in doc:
        full_text += page.get_text()
    
    doc.close()
    
    # 清理
    lines = full_text.split('\n')
    clean_lines = []
    for line in lines:
        line = line.strip()
        if '⾯渣逆袭' in line or line.startswith('No.'):
            continue
        clean_lines.append(line)
    
    clean_text = '\n'.join(clean_lines)
    
    # 提取问答对
    qa_pairs = {}
    
    # 分割章节
    sections = re.split(r'\n(?=\d+\.\s*[^\d])', clean_text)
    
    for section in sections:
        lines = section.split('\n')
        current_q = None
        current_a = []
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # 检测问题（数字 + 点 + 问号）
            if re.match(r'^\d+\..*[？?].*$', line):
                # 保存上一个问答
                if current_q and current_a:
                    qa_pairs[current_q] = '\n'.join(current_a)
                
                current_q = re.sub(r'^\d+\.\s*', '', line)
                current_a = []
            elif current_q:
                # 收集答案
                if not line.startswith('推荐阅读') and 'Java 面试指南' not in line:
                    current_a.append(line)
        
        # 保存最后一个
        if current_q and current_a:
            qa_pairs[current_q] = '\n'.join(current_a)
    
    return qa_pairs

def update_obsidian_file(module_name, qa_pairs):
    """更新 Obsidian 题库文件"""
    file_path = OBSIDIAN_DIR / f"{module_name} - 完整题库.md"
    
    if not file_path.exists():
        print(f"Skip: {file_path.name} (not found)")
        return 0
    
    content = file_path.read_text(encoding='utf-8')
    
    # 替换答案
    updated = 0
    for question, answer in qa_pairs.items():
        # 查找题目
        pattern = rf'(### 题\d+：{re.escape(question[:50])}.*?\n\n\*\*答案：\*\*\n\n)\*\(\(待补充\)\*\)'
        match = re.search(pattern, content, re.DOTALL)
        
        if match:
            old_text = match.group(0)
            new_text = f"{match.group(1)}{answer}"
            content = content.replace(old_text, new_text)
            updated += 1
    
    # 保存
    file_path.write_text(content, encoding='utf-8')
    return updated

def main():
    print("=" * 70)
    print("Extract Answers from PDF and Update Obsidian")
    print("=" * 70)
    print()
    
    modules = {
        "01-java-basics.pdf": "Java 基础篇",
        "02-jvm.pdf": "JVM 篇",
        "04-collection.pdf": "集合框架篇",
    }
    
    total_updated = 0
    
    for pdf_file, module_name in modules.items():
        pdf_path = PDF_DIR / pdf_file
        if not pdf_path.exists():
            print(f"Skip: {pdf_file}")
            continue
        
        print(f"Processing: {module_name}")
        
        # 提取问答
        qa_pairs = extract_qa_from_pdf(pdf_path)
        print(f"  Extracted {len(qa_pairs)} Q&A pairs")
        
        # 更新 Obsidian
        updated = update_obsidian_file(module_name, qa_pairs)
        print(f"  Updated {updated} answers")
        total_updated += updated
        print()
    
    print("=" * 70)
    print(f"Total updated: {total_updated} answers")
    print("=" * 70)

if __name__ == "__main__":
    main()
