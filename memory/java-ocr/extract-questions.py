#!/usr/bin/env python3
"""
从 OCR 结果中提取题目清单
对比已有知识点，找出遗漏
"""

import re
from pathlib import Path

OCR_DIR = Path("/root/.openclaw/workspace/memory/java-ocr")
OUTPUT_FILE = OCR_DIR / "题目清单提取.md"

def extract_questions_from_ocr():
    """从 OCR 文件中提取题目"""
    
    # 读取 Java 基础 OCR
    java_ocr = OCR_DIR / "01-Java 基础 - 面渣逆袭 V2.1-ocr.md"
    
    if not java_ocr.exists():
        print(f"❌ 文件不存在：{java_ocr}")
        return []
    
    content = java_ocr.read_text(encoding='utf-8')
    
    # 提取题目（模式：题 X + 题目内容）
    questions = []
    
    # 模式 1: "题 1：xxx" 或 "题 1. xxx"
    pattern1 = r'题\s*(\d+)\s*[：:.]\s*(.+?)(?=\n题\s*\d+|\n##|\Z)'
    matches = re.findall(pattern1, content, re.DOTALL)
    
    for q_num, q_text in matches:
        q_text = q_text.strip().split('\n')[0][:200]  # 只取第一行
        questions.append({
            'num': int(q_num),
            'text': q_text,
            'source': 'OCR'
        })
    
    return questions

def get_existing_questions():
    """获取已有知识点清单中的题目"""
    
    # 这里从 MEMORY.md 和知识点清单中提取
    # 简化版：直接返回已记录的题目数
    return {
        'Java 概述': {'total': 6, 'reviewed': 0},
        '基础语法': {'total': 10, 'reviewed': 5},  # 已复习 5 题
        '面向对象': {'total': 16, 'reviewed': 16},
        'String 类': {'total': 8, 'reviewed': 5},  # 已复习 5 题
        '异常处理': {'total': 4, 'reviewed': 3},  # 已复习 3 题
        'IO 流': {'total': 6, 'reviewed': 0},
        '反射泛型注解': {'total': 6, 'reviewed': 0},
    }

def main():
    print("📋 提取 OCR 题目清单...")
    
    questions = extract_questions_from_ocr()
    
    print(f"\n✅ 从 OCR 中提取到 {len(questions)} 道题目")
    
    # 获取已有记录
    existing = get_existing_questions()
    
    # 计算总复习进度
    total_questions = sum(v['total'] for v in existing.values())
    total_reviewed = sum(v['reviewed'] for v in existing.values())
    
    print(f"\n📊 已有知识点清单：")
    print(f"  总题目数：{total_questions}")
    print(f"  已复习：{total_reviewed}")
    print(f"  未复习：{total_questions - total_reviewed}")
    print(f"  进度：{total_reviewed}/{total_questions} ({total_reviewed*100//total_questions}%)")
    
    print(f"\n⚠️  未复习的章节：")
    for chapter, data in existing.items():
        if data['reviewed'] < data['total']:
            print(f"  - {chapter}: {data['reviewed']}/{data['total']}")
    
    # 生成报告
    report = f"""# Java 基础篇 - 题目清单对比报告

> 生成时间：2026-03-14
> 来源：OCR 识别结果 vs 已有知识点清单

---

## 📊 总体对比

| 对比项 | OCR 识别 | 已有记录 | 差异 |
|--------|---------|---------|------|
| 总题目数 | {len(questions)} 题（待精确提取） | {total_questions} 题 | - |
| 已复习 | - | {total_reviewed} 题 | - |
| 未复习 | - | {total_questions - total_reviewed} 题 | **需补充** |

---

## ⚠️ 未复习的章节（需补充）

| 章节 | 已复习 | 总题目 | 待补充 | 优先级 |
|------|--------|--------|--------|--------|
| Java 概述 | 0 | 6 | 6 | 🔴 高 |
| 基础语法 | 5 | 10 | 5 | 🟡 中 |
| 面向对象 | 16 | 16 | 0 | ✅ 完成 |
| String 类 | 5 | 8 | 3 | 🟡 中 |
| 异常处理 | 3 | 4 | 1 | 🟡 中 |
| IO 流 | 0 | 6 | 6 | 🔴 高 |
| 反射泛型注解 | 0 | 6 | 6 | 🔴 高 |

---

## 📋 下一步行动

### 第 1 优先级（完全未复习）
1. **Java 概述**（6 题）
2. **IO 流**（6 题）
3. **反射泛型注解**（6 题）

### 第 2 优先级（部分复习）
1. **基础语法**（补充 5 题）
2. **String 类**（补充 3 题）
3. **异常处理**（补充 1 题 + 6 个知识点）

### 第 3 优先级（已完成，需巩固）
1. **面向对象**（16 题，部分薄弱项需二次复习）

---

## 📝 已记录的薄弱项（来自 MEMORY.md）

- 抽象类（2/5 → 4.8/5，已修复）
- 方法重载（2/5 → 5/5，已修复）
- 序列化（2/5 → 4.5/5，已修复）
- 异常体系（2.2/5 → 4/5，已修复）
- 编译时 vs 运行时（2/5 → 5/5，已修复）
- 文本存储本质（2.3/5 → 4/5，已修复）
- 反射操作 API（2/5 → 4/5，已修复）
- AIO 理解（3/5 → 5/5，已修复）

**修复率：100%（8/8）** 🎉

---

## 🎯 建议

1. **优先复习未复习章节**（Java 概述、IO 流、反射泛型注解）
2. **补充遗漏题目**（基础语法 5 题、String 类 3 题）
3. **巩固薄弱项**（虽然已修复，但需定期复习）

---

*报告由 OpenClaw 自动生成*
"""
    
    OUTPUT_FILE.write_text(report, encoding='utf-8')
    print(f"\n📄 对比报告已生成：{OUTPUT_FILE}")

if __name__ == "__main__":
    main()
