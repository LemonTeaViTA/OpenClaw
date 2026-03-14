#!/usr/bin/env python3
"""
测试 Java PDF 是否可以提取文字
"""

import pdfplumber
import os

os.chdir('/root/.openclaw/workspace/files/java-notes')

# 获取第一个 PDF
pdf_files = [f for f in os.listdir('.') if f.endswith('.pdf')]
print(f"发现 {len(pdf_files)} 个 PDF 文件")
print(f"文件列表：{pdf_files[:3]}...\n")

# 测试第一个
test_pdf = pdf_files[0]
print(f"测试文件：{test_pdf}")

with pdfplumber.open(test_pdf) as pdf:
    page = pdf.pages[0]
    text = page.extract_text()
    images = page.images
    
    print(f"\n第 1 页测试结果：")
    print(f"  文字数：{len(text) if text else 0:,} 字符")
    print(f"  图片数：{len(images)}")
    
    if text and len(text) > 500:
        print(f"\n✅ 这是文字版 PDF（有文本层）")
        print(f"   可以直接提取文字，不需要 OCR")
        print(f"\n前 300 字符预览：")
        print("-" * 60)
        print(text[:300])
        print("-" * 60)
    else:
        print(f"\n❌ 这是扫描版 PDF（图片格式）")
        print(f"   必须用 OCR 识别")
