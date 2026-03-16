#!/usr/bin/env python3
"""
测试 OCR 识别效果
"""

import fitz
import subprocess
from pathlib import Path
import os

# 切换到 PDF 目录
os.chdir('C:\Users\11237\.openclaw-autoclaw\workspace/files/paismart-interview')

# 获取第一个 PDF 文件名
pdf_files = [f for f in os.listdir('.') if f.endswith('.pdf')]
pdf_name = pdf_files[0]
pdf_path = Path(pdf_name)

print(f"📄 测试文件：{pdf_name}")
print(f"文件存在：{pdf_path.exists()}")

# 1. PDF 转图片
doc = fitz.open(pdf_path)
page = doc[0]  # 第 1 页

# 渲染为图片（高分辨率）
mat = fitz.Matrix(2.0, 2.0)  # 2 倍缩放
pix = page.get_pixmap(matrix=mat)
img_path = "test_page.png"
pix.save(img_path)
print(f"✅ 图片已保存：{img_path} (尺寸：{pix.width}x{pix.height})")

doc.close()

# 2. Tesseract OCR 识别
print("\n🔍 开始 OCR 识别...")
txt_path = "test_page"
result = subprocess.run(
    ['tesseract', img_path, txt_path, '-l', 'chi_sim+eng'],
    capture_output=True,
    text=True
)

if result.returncode == 0:
    txt_content = Path(txt_path + '.txt').read_text(encoding='utf-8')
    print(f"✅ OCR 识别成功！")
    print(f"\n📝 识别结果（前 1500 字符）：\n")
    print("="*60)
    print(txt_content[:1500])
    print("="*60)
    print(f"\n总字符数：{len(txt_content)}")
else:
    print(f"❌ OCR 失败：{result.stderr}")
    print(f"返回码：{result.returncode}")
    # 尝试默认语言
    print("\n尝试默认语言识别...")
    result2 = subprocess.run(
        ['tesseract', img_path, txt_path],
        capture_output=True,
        text=True
    )
    if result2.returncode == 0:
        txt_content = Path(txt_path + '.txt').read_text(encoding='utf-8')
        print(f"✅ 识别成功，前 1000 字符：\n{txt_content[:1000]}")
    else:
        print(f"❌ 也失败了：{result2.stderr}")
