#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
直接从 PDF 提取文本（不依赖 OCR）
使用 pdfplumber
"""

import pdfplumber
from pathlib import Path

PDF_DIR = Path(r"C:\Users\11237\.openclaw-autoclaw\workspace\files\java-notes")
OUTPUT_DIR = Path(r"C:\Users\11237\.openclaw-autoclaw\workspace\memory\java-ocr\extracted")
OUTPUT_DIR.mkdir(exist_ok=True)

def extract_pdf_text(pdf_path):
    """提取 PDF 文本"""
    text = []
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            page_text = page.extract_text()
            if page_text:
                text.append(f"## 第{i+1}页\n\n{page_text}")
    return '\n\n'.join(text)

def main():
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    
    print("=" * 60)
    print("Extracting text from PDFs")
    print("=" * 60)
    
    pdf_files = list(PDF_DIR.glob("*.pdf"))
    print(f"Found {len(pdf_files)} PDF files\n")
    
    for pdf_path in pdf_files:
        print(f"Processing: {pdf_path.name}")
        try:
            text = extract_pdf_text(pdf_path)
            output_file = OUTPUT_DIR / f"{pdf_path.stem}-extracted.md"
            output_file.write_text(text, encoding='utf-8')
            print(f"  Extracted {len(text)} chars")
        except Exception as e:
            print(f"  Error: {e}")
        print()
    
    print("=" * 60)
    print("Done!")
    print("=" * 60)

if __name__ == "__main__":
    main()
