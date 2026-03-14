#!/usr/bin/env python3
"""
测试 OCR 识别效果
将 PDF 第 1 页转为图片，然后用 Tesseract 识别
"""

import fitz  # PyMuPDF
import subprocess
import os
from pathlib import Path

PDF_DIR = Path("/root/.openclaw/workspace/files/paismart-interview")
TEST_PDF = PDF_DIR / "派聪明 rag 项目是什么.pdf"
OUTPUT_IMG = PDF_DIR / "test_page.png"
OUTPUT_TXT = PDF_DIR / "test_page.txt"

# 1. PDF 转图片
print(f"📄 打开 PDF: {TEST_PDF.name}")
doc = fitz.open(TEST_PDF)
page = doc[0]  # 第 1 页

# 渲染为图片（高分辨率）
mat = fitz.Matrix(2.0, 2.0)  # 2 倍缩放
pix = page.get_pixmap(matrix=mat)
pix.save(str(OUTPUT_IMG))
print(f"✅ 图片已保存：{OUTPUT_IMG}")

doc.close()

# 2. Tesseract OCR 识别
print("\n🔍 开始 OCR 识别...")
result = subprocess.run(
    ['tesseract', str(OUTPUT_IMG), str(OUTPUT_TXT.with_suffix('')), '-l', 'chi_sim+eng'],
    capture_output=True,
    text=True
)

if result.returncode == 0:
    print(f"✅ OCR 识别成功！")
    # 读取结果
    txt_content = OUTPUT_TXT.read_text(encoding='utf-8')
    print(f"\n📝 识别结果（前 1000 字符）：\n")
    print("="*60)
    print(txt_content[:1000])
    print("="*60)
    print(f"\n总字符数：{len(txt_content)}")
else:
    print(f"❌ OCR 失败：{result.stderr}")
    # 尝试只用英文
    print("\n尝试只用英文识别...")
    result2 = subprocess.run(
        ['tesseract', str(OUTPUT_IMG), str(OUTPUT_TXT.with_suffix('')), '-l', 'eng'],
        capture_output=True,
        text=True
    )
    if result2.returncode == 0:
        txt_content = OUTPUT_TXT.read_text(encoding='utf-8')
        print(f"✅ 英文 OCR 成功，前 500 字符：\n{txt_content[:500]}")
