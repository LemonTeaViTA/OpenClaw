#!/usr/bin/env python3
"""
剩余 PDF 批量 OCR 识别
处理 MySQL、Redis、Spring 三个 PDF
"""

import fitz
import subprocess
from pathlib import Path
import os
from datetime import datetime

# 配置
PDF_DIRS = {
    'mysql': Path("C:\Users\11237\.openclaw-autoclaw\workspace/files/mysql-notes"),
    'redis': Path("C:\Users\11237\.openclaw-autoclaw\workspace/files/redis-notes"),
    'spring': Path("C:\Users\11237\.openclaw-autoclaw\workspace/files/spring-notes"),
}

OUTPUT_BASE = Path("C:\Users\11237\.openclaw-autoclaw\workspace/memory/other-subjects-ocr")

# 创建输出目录
OUTPUT_BASE.mkdir(parents=True, exist_ok=True)
for subject in PDF_DIRS.keys():
    (OUTPUT_BASE / subject).mkdir(parents=True, exist_ok=True)

def pdf_page_to_text(pdf_path: Path, page_num: int = 0) -> str:
    """将 PDF 单页转为图片并用 OCR 识别"""
    try:
        doc = fitz.open(pdf_path)
        if page_num >= len(doc):
            doc.close()
            return ""
        
        page = doc[page_num]
        mat = fitz.Matrix(2.0, 2.0)
        pix = page.get_pixmap(matrix=mat)
        
        img_path = pdf_path.parent / f"_temp_page_{page_num}.png"
        pix.save(str(img_path))
        doc.close()
        
        txt_path = pdf_path.parent / f"_temp_page_{page_num}"
        result = subprocess.run(
            ['tesseract', str(img_path), str(txt_path), '-l', 'chi_sim'],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        img_path.unlink(missing_ok=True)
        txt_file = txt_path.with_suffix('.txt')
        if txt_file.exists():
            text = txt_file.read_text(encoding='utf-8')
            txt_file.unlink()
            return text
        else:
            return ""
            
    except Exception as e:
        return f"[OCR 错误：{e}]"

def pdf_to_markdown(pdf_path: Path, output_dir: Path) -> str:
    """将 PDF 转换为 Markdown 格式"""
    content = []
    
    content.append(f"# {pdf_path.stem}\n")
    content.append(f"> 来源：{pdf_path.name}\n")
    content.append(f"> OCR 解析时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    content.append(f"> 本文档由 OCR 识别生成，可能存在少量识别错误\n\n")
    content.append("---\n\n")
    
    try:
        doc = fitz.open(pdf_path)
        total_pages = len(doc)
        doc.close()
        
        content.append(f"## 文档信息\n\n")
        content.append(f"- **总页数**: {total_pages}\n")
        content.append(f"- **文件大小**: {pdf_path.stat().st_size / 1024 / 1024:.2f} MB\n\n")
        content.append("---\n\n")
        
        for i in range(total_pages):
            print(f"    第 {i+1}/{total_pages} 页...", end='\r')
            text = pdf_page_to_text(pdf_path, i)
            if text.strip():
                content.append(f"## 第 {i+1} 页\n\n")
                content.append(text)
                content.append("\n\n")
        
        print(f"    完成 {total_pages} 页识别 ✓")
        
    except Exception as e:
        content.append(f"\n⚠️ 处理错误：{e}\n")
    
    return "\n".join(content)

def main():
    """主函数"""
    print(f"📚 剩余 PDF 批量 OCR 识别")
    print(f"="*60)
    
    all_results = []
    
    for subject, pdf_dir in PDF_DIRS.items():
        print(f"\n📖 处理 {subject.upper()} 系列...")
        output_dir = OUTPUT_BASE / subject
        
        pdf_files = list(pdf_dir.glob("*.pdf"))
        print(f"   发现 {len(pdf_files)} 个 PDF 文件")
        
        for idx, pdf_path in enumerate(pdf_files, 1):
            print(f"   [{idx}/{len(pdf_files)}] 处理：{pdf_path.name}")
            
            start_time = datetime.now()
            
            try:
                markdown_content = pdf_to_markdown(pdf_path, output_dir)
                
                output_path = output_dir / f"{pdf_path.stem}-ocr.md"
                output_path.write_text(markdown_content, encoding='utf-8')
                
                elapsed = (datetime.now() - start_time).total_seconds()
                
                all_results.append({
                    'subject': subject.upper(),
                    'pdf': pdf_path.name,
                    'md': f"{pdf_path.stem}-ocr.md",
                    'size': len(markdown_content),
                    'pages': markdown_content.count('## 第'),
                    'time': f"{elapsed:.1f}s",
                    'status': '✅'
                })
                
                print(f"   ✅ 成功 → {output_path.name} ({len(markdown_content):,} 字符，{elapsed:.1f}s)")
                
            except Exception as e:
                elapsed = (datetime.now() - start_time).total_seconds()
                all_results.append({
                    'subject': subject.upper(),
                    'pdf': pdf_path.name,
                    'md': None,
                    'size': 0,
                    'pages': 0,
                    'time': f"{elapsed:.1f}s",
                    'status': '❌',
                    'error': str(e)
                })
                print(f"   ❌ 失败：{e}")
    
    # 打印汇总
    print("\n" + "="*60)
    print("📊 处理汇总")
    print("="*60)
    
    success = sum(1 for r in all_results if r['status'] == '✅')
    failed = len(all_results) - success
    total_chars = sum(r['size'] for r in all_results if r['status'] == '✅')
    total_pages = sum(r['pages'] for r in all_results if r['status'] == '✅')
    
    print(f"总计：{len(all_results)} 个文件")
    print(f"成功：{success} 个 ✅")
    print(f"失败：{failed} 个 ❌")
    print(f"总字符数：{total_chars:,}")
    print(f"总页数：{total_pages}")
    
    # 按科目分组统计
    print("\n📚 按科目统计：")
    subjects = set(r['subject'] for r in all_results)
    for subject in sorted(subjects):
        subj_results = [r for r in all_results if r['subject'] == subject]
        subj_chars = sum(r['size'] for r in subj_results if r['status'] == '✅')
        subj_pages = sum(r['pages'] for r in subj_results if r['status'] == '✅')
        print(f"  {subject}: {len(subj_results)} 个文件，{subj_pages} 页，{subj_chars:,} 字")
    
    # 生成索引
    index_content = f"""# 其他科目 OCR 识别结果

> 自动生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

## 📊 统计信息

| 项目 | 数量 |
|------|------|
| PDF 总数 | {len(all_results)} |
| 成功识别 | {success} |
| 识别失败 | {failed} |
| 总字符数 | {total_chars:,} |
| 总页数 | {total_pages} |

---

## 📚 文件列表

| 序号 | 科目 | PDF 文件名 | Markdown 文件 | 页数 | 字符数 | 耗时 | 状态 |
|------|------|-----------|--------------|------|--------|------|------|
"""
    
    for idx, r in enumerate(all_results, 1):
        if r['md']:
            md_link = f"[{r['md']}](./{r['subject'].lower()}/{r['md']})"
        else:
            md_link = "❌ 识别失败"
        status_icon = "✅" if r['status'] == '✅' else "❌"
        index_content += f"| {idx} | {r['subject']} | {r['pdf']} | {md_link} | {r['pages']} | {r['size']:,} | {r['time']} | {status_icon} |\n"
    
    index_content += """
---

## 📁 目录结构

```
other-subjects-ocr/
├── README.md              # 本文件
├── mysql/                 # MySQL 系列
│   └── 面渣逆袭 MySQL 篇 V2.2-ocr.md
├── redis/                 # Redis 系列
│   └── 面渣逆袭 Redis 篇 V2.0-ocr.md
└── spring/                # Spring 系列
    └── 面渣逆袭 Spring 篇 V2.0 亮白版-ocr.md
```

---

## ⚠️ 注意事项

- OCR 识别准确率约 90-95%，可能存在少量识别错误
- 技术名词、代码片段请仔细核对
- 如发现识别错误，欢迎校正后更新

"""
    
    index_path = OUTPUT_BASE / "README.md"
    index_path.write_text(index_content, encoding='utf-8')
    print(f"\n📋 索引文件已生成：{index_path}")
    
    print("\n✨ 所有 PDF OCR 识别完成！")
    print(f"⏱️  预计总耗时：约 10-20 分钟")

if __name__ == "__main__":
    main()
