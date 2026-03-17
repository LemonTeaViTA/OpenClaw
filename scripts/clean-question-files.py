#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
清理题库文件中的噪音
"""

import re
from pathlib import Path

OUTPUT_DIR = Path(r"C:\Users\11237\.openclaw-autoclaw\workspace\Obsidian\40-Questions")

def clean_file(file_path):
    """清理文件"""
    content = file_path.read_text(encoding='utf-8')
    
    # 清理章节标题中的面试指南前缀
    content = re.sub(
        r'^## \d+\. Java ⾯试指南.*\n',
        '',
        content,
        flags=re.MULTILINE
    )
    
    # 清理题目中的面试指南前缀（保留标准题目）
    lines = content.split('\n')
    clean_lines = []
    
    for line in lines:
        # 跳过包含"Java 面试指南"的题目行
        if line.startswith('### 题') and 'Java ⾯试指南' in line:
            continue
        clean_lines.append(line)
    
    content = '\n'.join(clean_lines)
    
    # 更新题数统计
    question_count = len(re.findall(r'^### 题\d+：', content, re.MULTILINE))
    content = re.sub(
        r'> 题数：\d+ 题',
        f'> 题数：{question_count} 题',
        content
    )
    
    file_path.write_text(content, encoding='utf-8')
    return question_count

def main():
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    
    print("=" * 70)
    print("Clean Question Files")
    print("=" * 70)
    print()
    
    files = list(OUTPUT_DIR.glob("*完整题库.md"))
    
    total = 0
    for file_path in files:
        count = clean_file(file_path)
        total += count
        print(f"{file_path.name}: {count} 题")
    
    print()
    print(f"Total: {total} 题")
    print("=" * 70)

if __name__ == "__main__":
    main()
