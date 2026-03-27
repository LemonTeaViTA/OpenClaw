#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""复制 PDF 文件并重命名为英文"""
import shutil
from pathlib import Path

src_dir = Path(r"C:\Users\11237\.openclaw-autoclaw\workspace\files\java-notes")
dst_dir = Path(r"C:\Users\11237\.openclaw-autoclaw\workspace\files\java-notes\renamed")
dst_dir.mkdir(exist_ok=True)

mapping = {
    "01": "01-java-basics.pdf",
    "02": "02-jvm.pdf",
    "03": "03-concurrent.pdf",
    "04": "04-collection.pdf",
}

for pdf in src_dir.glob("*.pdf"):
    prefix = pdf.stem[:2]
    if prefix in mapping:
        dst = dst_dir / mapping[prefix]
        shutil.copy2(pdf, dst)
        print(f"Copied: {pdf.name} -> {dst.name}")

# Also copy other subject PDFs
other_dirs = [
    (r"C:\Users\11237\.openclaw-autoclaw\workspace\files\mysql-notes", "05-mysql.pdf"),
    (r"C:\Users\11237\.openclaw-autoclaw\workspace\files\redis-notes", "06-redis.pdf"),
    (r"C:\Users\11237\.openclaw-autoclaw\workspace\files\spring-notes", "07-spring.pdf"),
]

for src_dir_path, dst_name in other_dirs:
    src = Path(src_dir_path)
    if src.exists():
        for pdf in src.glob("*.pdf"):
            dst = dst_dir / dst_name
            shutil.copy2(pdf, dst)
            print(f"Copied: {pdf.name} -> {dst.name}")

print("\nDone!")
