#!/usr/bin/env python3
"""
对比两种 PDF 的区别
"""

import pdfplumber
from pathlib import Path
import os

# Java PDF 目录
java_dir = Path("/root/.openclaw/workspace/files/java-notes")
pai_dir = Path("/root/.openclaw/workspace/files/paismart-interview")

print("="*60)
print("📊 两种 PDF 对比测试")
print("="*60)

# 测试 Java PDF
print("\n1️⃣ Java 基础 PDF（之前的）:")
java_pdf = list(java_dir.glob("*.pdf"))[0]
print(f"   文件：{java_pdf.name}")

with pdfplumber.open(java_pdf) as pdf:
    page = pdf.pages[0]
    text = page.extract_text()
    images = page.images
    print(f"   第 1 页文字数：{len(text) if text else 0:,} 字符")
    print(f"   第 1 页图片数：{len(images)}")
    if text and len(text) > 100:
        print(f"   ✅ 类型：文字版 PDF（有文本层）")
        print(f"   前 100 字符：{text[:100].strip()}")
    else:
        print(f"   ❌ 类型：扫描版 PDF")

# 测试派聪明 PDF
print("\n2️⃣ 派聪明 PDF（现在的）:")
pai_pdf = list(pai_dir.glob("派聪明*.pdf"))[0]
print(f"   文件：{pai_pdf.name}")

with pdfplumber.open(pai_pdf) as pdf:
    page = pdf.pages[0]
    text = page.extract_text()
    images = page.images
    print(f"   第 1 页文字数：{len(text) if text else 0} 字符")
    print(f"   第 1 页图片数：{len(images)}")
    if text and len(text) > 100:
        print(f"   ✅ 类型：文字版 PDF（有文本层）")
    else:
        print(f"   ❌ 类型：扫描版 PDF（图片格式）")

print("\n" + "="*60)
print("💡 结论：")
print("  - 文字版 PDF：可以直接提取文字（快、准确）")
print("  - 扫描版 PDF：必须用 OCR 识别（慢、需要图像处理）")
print("="*60)
