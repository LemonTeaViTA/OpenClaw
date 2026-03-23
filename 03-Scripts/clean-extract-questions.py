#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
清理 PDF 提取的题目
去重 + 过滤噪音
"""

import fitz
import re
from pathlib import Path

PDF_DIR = Path(r"C:\Users\11237\.openclaw-autoclaw\workspace\files\java-notes\renamed")
OUTPUT_DIR = Path(r"C:\Users\11237\.openclaw-autoclaw\workspace\memory\pdf-extracted")

def extract_clean_questions(pdf_path):
    """提取并清理题目"""
    doc = fitz.open(pdf_path)
    full_text = ""
    
    for page in doc:
        full_text += page.get_text()
    
    doc.close()
    
    # 清理文本
    lines = full_text.split('\n')
    clean_lines = []
    
    for line in lines:
        line = line.strip()
        
        # 跳过页眉页脚
        if line.startswith('⾯渣逆袭') or line.startswith('No.'):
            continue
        
        # 跳过太短的行
        if len(line) < 5:
            continue
        
        clean_lines.append(line)
    
    clean_text = '\n'.join(clean_lines)
    
    # 提取题目（改进模式）
    questions = []
    
    # 模式：题号 + 问题（排除面试题前缀）
    pattern = r'(?:^|\n)(\d+)[.、]\s*([^⾯Java 推荐阅读符号整数]+?)(?=\n\d+[.、]|\n##|\Z)'
    matches = re.findall(pattern, clean_text, re.DOTALL)
    
    for q_num, q_text in matches:
        q_text = q_text.strip()
        
        # 过滤噪音
        if len(q_text) < 10:
            continue
        if q_text.startswith('Java 面试指南'):
            continue
        if q_text.startswith('推荐阅读'):
            continue
        if '符号位' in q_text or '整数部分' in q_text:
            continue
        
        questions.append({
            'num': int(q_num),
            'text': q_text[:200]
        })
    
    # 去重（按题号 + 前 50 字）
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
    print("Clean Question Extraction")
    print("=" * 70)
    print()
    
    pdf_path = PDF_DIR / "01-java-basics.pdf"
    questions = extract_clean_questions(pdf_path)
    
    print(f"Extracted {len(questions)} unique questions")
    print()
    
    # 保存
    output_file = OUTPUT_DIR / "Java 基础篇-clean-questions.md"
    
    lines = ["# Java 基础篇 - 完整题目清单（清理版）", "", f"共 {len(questions)} 题", "", "---", ""]
    
    for q in questions:
        lines.append(f"### 题{q['num']}")
        lines.append("")
        lines.append(q['text'])
        lines.append("")
        lines.append("---")
        lines.append("")
    
    output_file.write_text('\n'.join(lines), encoding='utf-8')
    
    print(f"Saved: {output_file.name}")
    print()
    
    # 预览前 20 题
    print("前 20 题预览：")
    for q in questions[:20]:
        print(f"  题{q['num']}：{q['text'][:60]}...")
    
    print()
    print("=" * 70)

if __name__ == "__main__":
    main()
