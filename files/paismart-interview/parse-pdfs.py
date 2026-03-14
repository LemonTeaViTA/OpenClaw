#!/usr/bin/env python3
"""
派聪明项目 PDF 批量解析脚本
将所有 PDF 转换为 Markdown 格式，方便 AI 检索和学习
"""

import pdfplumber
import os
from pathlib import Path
from datetime import datetime

PDF_DIR = Path("/root/.openclaw/workspace/files/paismart-interview")
OUTPUT_DIR = Path("/root/.openclaw/workspace/memory/paismart-interview")

# 创建输出目录
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def pdf_to_markdown(pdf_path: Path) -> str:
    """将 PDF 转换为 Markdown 格式"""
    content = []
    
    with pdfplumber.open(pdf_path) as pdf:
        # 添加文件信息
        content.append(f"# {pdf_path.stem}\n")
        content.append(f"> 来源：{pdf_path.name}\n")
        content.append(f"> 解析时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        content.append(f"> 总页数：{len(pdf.pages)}\n\n")
        content.append("---\n\n")
        
        # 逐页解析
        for i, page in enumerate(pdf.pages, 1):
            text = page.extract_text()
            if text:
                content.append(f"## 第 {i} 页\n\n")
                content.append(text)
                content.append("\n\n")
    
    return "\n".join(content)

def main():
    """主函数"""
    pdf_files = list(PDF_DIR.glob("*.pdf"))
    
    print(f"📚 发现 {len(pdf_files)} 个 PDF 文件")
    print(f"📂 输出目录：{OUTPUT_DIR}\n")
    
    results = []
    
    for idx, pdf_path in enumerate(pdf_files, 1):
        print(f"[{idx}/{len(pdf_files)}] 解析：{pdf_path.name}")
        
        try:
            # 转换 PDF
            markdown_content = pdf_to_markdown(pdf_path)
            
            # 保存 Markdown
            output_path = OUTPUT_DIR / f"{pdf_path.stem}.md"
            output_path.write_text(markdown_content, encoding='utf-8')
            
            # 记录结果
            results.append({
                'pdf': pdf_path.name,
                'md': f"{pdf_path.stem}.md",
                'size': len(markdown_content),
                'status': '✅'
            })
            
            print(f"  ✅ 成功 → {output_path.name} ({len(markdown_content):,} 字符)")
            
        except Exception as e:
            results.append({
                'pdf': pdf_path.name,
                'md': None,
                'size': 0,
                'status': '❌',
                'error': str(e)
            })
            print(f"  ❌ 失败：{e}")
    
    # 打印汇总
    print("\n" + "="*60)
    print("📊 解析汇总")
    print("="*60)
    
    success = sum(1 for r in results if r['status'] == '✅')
    failed = len(results) - success
    
    print(f"总计：{len(results)} 个文件")
    print(f"成功：{success} 个 ✅")
    print(f"失败：{failed} 个 ❌")
    
    # 生成索引文件
    index_content = f"""# 派聪明项目面试题库 - 索引

> 自动生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
> 
> 本索引由 PDF 批量解析脚本生成，包含所有解析后的 Markdown 文件列表。

---

## 📊 统计信息

- **PDF 总数**: {len(results)}
- **成功解析**: {success}
- **解析失败**: {failed}

---

## 📚 文件列表

| 序号 | PDF 文件名 | Markdown 文件 | 字符数 | 状态 |
|------|-----------|--------------|--------|------|
"""
    
    for idx, r in enumerate(results, 1):
        md_link = f"[{r['md']}](./{r['md']})" if r['md'] else "❌ 解析失败"
        index_content += f"| {idx} | {r['pdf']} | {md_link} | {r['size']:,} | {r['status']} |\n"
    
    # 添加分类索引
    index_content += """
---

## 🗂️ 分类索引

### 项目概述
- 派聪明 rag 项目是什么.md
- 派聪明整体设计方案.md
- 派聪明需求分析.md
- 派聪明如何写简历.md

### 架构设计
- 架构设计面试题预测.md
- 派聪明库表设计.md

### 核心模块
- 文件上传解析设计方案.md
- 文件上传解析面试题预测.md
- 知识库检索设计方案.md
- 知识库检索面试题预测.md
- 聊天助手设计方案.md
- 聊天助手面试题预测.md
- 用户管理模块设计方案.md
- 用户管理面试题预测.md

### 技术深入
- ES 混合检索精讲.md
- Springsecurit 实现 RBAC.md
- Prompt 设计.md

### 面试真题
- 27 家面试题.md
- RAG 面试预测.md

---

## 📝 使用说明

1. **快速检索**: 使用 `grep` 或文本编辑器搜索关键词
2. **对照学习**: PDF 原文 + Markdown 对照阅读
3. **模拟面试**: 随机抽取题目进行练习

"""
    
    index_path = OUTPUT_DIR / "README.md"
    index_path.write_text(index_content, encoding='utf-8')
    print(f"\n📋 索引文件已生成：{index_path}")
    
    print("\n✨ 所有 PDF 解析完成！")

if __name__ == "__main__":
    main()
