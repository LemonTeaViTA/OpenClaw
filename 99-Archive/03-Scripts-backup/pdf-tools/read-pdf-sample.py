#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
读取 PDF 前 10 页内容
"""

import fitz
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

PDF_DIR = Path(r"C:\Users\11237\.openclaw-autoclaw\workspace\files\java-notes\renamed")

pdf_path = PDF_DIR / "01-java-basics.pdf"
doc = fitz.open(pdf_path)

for i in range(min(10, len(doc))):
    page = doc[i]
    text = page.get_text()
    print(f"\n{'='*70}")
    print(f"Page {i+1}")
    print('='*70)
    lines = text.split('\n')[:20]
    for line in lines:
        if line.strip():
            preview = line.replace('\n', ' ')[:100]
            print(preview)

doc.close()
