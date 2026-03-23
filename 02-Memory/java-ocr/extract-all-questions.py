#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
从 OCR 结果中提取所有题目
"""

import re
from pathlib import Path
from datetime import datetime

OCR_DIR = Path(r"C:\Users\11237\.openclaw-autoclaw\workspace\memory\java-ocr")
OUTPUT_DIR = OCR_DIR / "extracted"
OUTPUT_DIR.mkdir(exist_ok=True)

def extract_questions_from_file(ocr_file):
    """从 OCR 文件中提取题目"""
    if not ocr_file.exists():
        return []
    
    content = ocr_file.read_text(encoding='utf-8')
    questions = []
    
    # 模式：题 1：xxx 或 题 1.xxx
    pattern = r'题\s*(\d+)[：:.:]\s*(.+?)(?=\n题\s*\d+[：:.:]|\n##|\Z)'
    matches = re.findall(pattern, content, re.DOTALL)
    
    for q_num, q_text in matches:
        q_text = q_text.strip()
        lines = q_text.split('\n')
        question = lines[0][:300]
        
        questions.append({
            'num': int(q_num),
            'text': question,
            'full_text': q_text
        })
    
    return questions

def main():
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    
    print("=" * 60)
    print("Extracting questions from OCR")
    print("=" * 60)
    
    # 获取所有 OCR 文件
    ocr_files = list(OCR_DIR.glob("*-ocr.md"))
    print(f"Found {len(ocr_files)} OCR files")
    
    all_questions = {}
    
    for ocr_path in ocr_files:
        module_name = ocr_path.stem.replace("-ocr", "")
        print(f"\nProcessing: {module_name}")
        
        questions = extract_questions_from_file(ocr_path)
        all_questions[module_name] = questions
        print(f"  Extracted: {len(questions)} questions")
    
    # 生成报告
    report = []
    report.append("# PDF 题目完整清单（OCR 提取）")
    report.append("")
    report.append(f"生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append("")
    report.append("---")
    report.append("")
    
    # 统计
    report.append("## 总体统计")
    report.append("")
    report.append("| PDF 模块 | 题目数量 |")
    report.append("|---------|---------|")
    
    total = 0
    for module, questions in all_questions.items():
        report.append(f"| {module} | {len(questions)} 题 |")
        total += len(questions)
    
    report.append(f"| **总计** | **{total} 题** |")
    report.append("")
    report.append("---")
    report.append("")
    
    # 详细清单
    for module, questions in all_questions.items():
        report.append(f"## {module}")
        report.append("")
        
        if not questions:
            report.append("*暂无题目*")
            report.append("")
            continue
        
        for q in questions:
            report.append(f"### 题{q['num']}")
            report.append("")
            report.append(f"{q['text']}")
            report.append("")
        
        report.append("---")
        report.append("")
    
    # 保存
    output_file = OUTPUT_DIR / "完整题目清单.md"
    output_file.write_text('\n'.join(report), encoding='utf-8')
    
    print(f"\n{'=' * 60}")
    print("Completed!")
    print(f"Output: {output_file}")
    print(f"Total: {total} questions")
    print("=" * 60)

if __name__ == "__main__":
    main()
