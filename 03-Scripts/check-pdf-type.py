#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
检查 PDF 类型（文字版 or 扫描版）
并测试文本提取效果
"""

import fitz  # PyMuPDF
from pathlib import Path

PDF_DIR = Path(r"C:\Users\11237\.openclaw-autoclaw\workspace\files\java-notes\renamed")

def check_pdf_type(pdf_path):
    """检查 PDF 类型"""
    doc = fitz.open(pdf_path)
    
    # 检查前 3 页
    text_pages = 0
    total_pages = min(len(doc), 3)
    
    for i in range(total_pages):
        page = doc[i]
        text = page.get_text()
        if len(text.strip()) > 100:  # 有足够文字
            text_pages += 1
    
    doc.close()
    
    # 判断类型
    if text_pages >= 2:
        return "文字版", "可以直接提取文本"
    else:
        return "扫描版", "需要 OCR 识别"

def extract_sample(pdf_path):
    """提取样本内容"""
    doc = fitz.open(pdf_path)
    page = doc[0]
    text = page.get_text()
    doc.close()
    return text[:500]

def main():
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    
    print("=" * 60)
    print("Checking PDF Type")
    print("=" * 60)
    print()
    
    pdf_files = list(PDF_DIR.glob("*.pdf"))
    
    for pdf_path in pdf_files:
        print(f"File: {pdf_path.name}")
        pdf_type, reason = check_pdf_type(pdf_path)
        print(f"   Type: {pdf_type}")
        print(f"   Note: {reason}")
        
        # 提取样本
        sample = extract_sample(pdf_path)
        if sample.strip():
            preview = sample.replace('\n', ' ')[:80]
            print(f"   Preview: {preview}...")
        print()
    
    print("=" * 60)

if __name__ == "__main__":
    main()
