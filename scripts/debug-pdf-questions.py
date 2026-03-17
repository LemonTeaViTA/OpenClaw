#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
调试：检查 PDF 实际格式
"""

import fitz
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

PDF_DIR = Path(r"C:\Users\11237\.openclaw-autoclaw\workspace\files\java-notes\renamed")
pdf_path = PDF_DIR / "01-java-basics.pdf"

doc = fitz.open(pdf_path)

print("Searching for questions in first 30 pages...")
print("=" * 70)

count = 0
for page_num in range(min(30, len(doc))):
    page = doc[page_num]
    text = page.get_text()
    lines = text.split('\n')
    
    for line in lines:
        line = line.strip()
        # 找问号结尾的行
        if '?' in line or '？' in line:
            if len(line) > 10 and len(line) < 200:
                print(f"P{page_num+1}: {line[:120]}")
                count += 1

print("=" * 70)
print(f"Found {count} potential questions")

doc.close()
