#!/usr/bin/env python3
"""
正式 OCR 识别 - 测试中文语言包效果
"""

import fitz
import subprocess
from pathlib import Path
import os

# 切换到 PDF 目录
os.chdir('/root/.openclaw/workspace/files/paismart-interview')

# 获取第一个 PDF 文件名
pdf_files = [f for f in os.listdir('.') if f.endswith('.pdf')]
pdf_name = pdf_files[0]
pdf_path = Path(pdf_name)

print(f"📄 测试文件：{pdf_name}")

# 1. PDF 转图片
doc = fitz.open(pdf_path)
page = doc[0]  # 第 1 页

# 渲染为图片（高分辨率）
mat = fitz.Matrix(2.0, 2.0)  # 2 倍缩放
pix = page.get_pixmap(matrix=mat)
img_path = "test_page_cn.png"
pix.save(img_path)
print(f"✅ 图片已保存：{img_path} (尺寸：{pix.width}x{pix.height})")

doc.close()

# 2. Tesseract OCR 识别（中文简体）
print("\n🔍 开始 OCR 识别（中文简体）...")
txt_path = "test_page_cn"
result = subprocess.run(
    ['tesseract', img_path, txt_path, '-l', 'chi_sim'],
    capture_output=True,
    text=True
)

if result.returncode == 0:
    txt_content = Path(txt_path + '.txt').read_text(encoding='utf-8')
    print(f"✅ OCR 识别成功！")
    print(f"\n📝 识别结果（前 2000 字符）：\n")
    print("="*60)
    print(txt_content[:2000])
    print("="*60)
    print(f"\n总字符数：{len(txt_content)}")
    print(f"\n✅ 中文识别效果良好！可以开始批量处理。")
else:
    print(f"❌ OCR 失败：{result.stderr}")
