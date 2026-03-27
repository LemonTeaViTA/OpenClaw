#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
提取 PDF 目录结构 + 题目
"""

import fitz
import re
from pathlib import Path

PDF_DIR = Path(r"C:\Users\11237\.openclaw-autoclaw\workspace\files\java-notes\renamed")
OUTPUT_DIR = Path(r"C:\Users\11237\.openclaw-autoclaw\workspace\memory\pdf-extracted")

def analyze_pdf_structure(pdf_path):
    """分析 PDF 结构"""
    doc = fitz.open(pdf_path)
    
    chapters = []
    current_chapter = None
    questions = []
    
    for i, page in enumerate(doc):
        text = page.get_text()
        lines = text.split('\n')
        
        for line in lines:
            line = line.strip()
            
            # 检测章节标题（如 "1. Java 概述"）
            if re.match(r'^\d+\.\s+.+$', line):
                if current_chapter and questions:
                    chapters.append({
                        'title': current_chapter,
                        'questions': questions.copy()
                    })
                    questions = []
                current_chapter = line
                continue
            
            # 检测题目（如 "1. 什么是 Java？"）
            if current_chapter and re.match(r'^\d+\.\s+.+\?$', line):
                questions.append(line)
    
    # 添加最后一章
    if current_chapter and questions:
        chapters.append({
            'title': current_chapter,
            'questions': questions
        })
    
    doc.close()
    return chapters

def main():
    import sys
    import re
    sys.stdout.reconfigure(encoding='utf-8')
    
    print("=" * 70)
    print("PDF Structure Analysis")
    print("=" * 70)
    print()
    
    pdf_path = PDF_DIR / "01-java-basics.pdf"
    chapters = analyze_pdf_structure(pdf_path)
    
    print(f"Found {len(chapters)} chapters")
    print()
    
    total_questions = 0
    for chapter in chapters:
        q_count = len(chapter['questions'])
        total_questions += q_count
        print(f"{chapter['title']}: {q_count} 题")
        for q in chapter['questions'][:5]:
            print(f"  - {q[:60]}...")
        if q_count > 5:
            print(f"  ... 还有 {q_count - 5} 题")
        print()
    
    print(f"Total: {total_questions} 题")
    print("=" * 70)

if __name__ == "__main__":
    main()
