# 题库 ID 系统使用指南

**版本**：1.0  
**更新时间**：2026-03-23  
**状态**：✅ 已启用

---

## 📋 目录

1. [系统概述](#系统概述)
2. [题库 ID 规范](#题库 id 规范)
3. [核心文件](#核心文件)
4. [使用场景](#使用场景)
5. [脚本命令](#脚本命令)
6. [扩展功能](#扩展功能)

---

## 系统概述

### 改造前 vs 改造后

| 项目 | 改造前 ❌ | 改造后 ✅ |
|------|----------|----------|
| **题目索引** | 题 1、题 2...（文字） | java-001、coll-015...（ID） |
| **乱码问题** | 题目内容可能乱码 | ID 永远是 ASCII |
| **顺序依赖** | 题目顺序变化会混乱 | ID 唯一，不受顺序影响 |
| **元数据** | 无 | 难度、标签、模块 |
| **验证机制** | 无 | 自动验证 ID 有效性 |

---

## 题库 ID 规范

### ID 格式

```
{module}-{number}
```

**示例**：
- `java-001`：Java 基础篇第 1 题
- `coll-015`：集合框架篇第 15 题
- `jvm-023`：JVM 篇第 23 题

### 模块代码

| 代码 | 模块 | 题数 | ID 范围 |
|------|------|------|--------|
| `java` | Java 基础篇 | 66 题 | java-001 ~ java-066 |
| `coll` | 集合框架篇 | 37 题 | coll-001 ~ coll-037 |
| `jvm` | JVM 篇 | 60 题 | jvm-001 ~ jvm-060 |

**总计**：163 题

### 难度等级

| 等级 | 标识 | 说明 | 占比 |
|------|------|------|------|
| **基础** | ⭐ 基础 | 概念记忆、简单理解 | 35 题 (21%) |
| **进阶** | ⭐⭐ 进阶 | 原理分析、应用场景 | 70 题 (43%) |
| **提高** | ⭐⭐⭐ 提高 | 综合应用、深度理解 | 58 题 (36%) |

---

## 核心文件

### 1. 题库映射文件

**路径**：`.question-id-map.json`

**结构**：
```json
{
  "version": "1.0",
  "lastUpdate": "2026-03-23T20:50:00Z",
  "totalQuestions": 163,
  "modules": {
    "java": {"total": 66, "name": "Java 基础篇"},
    "coll": {"total": 37, "name": "集合框架篇"},
    "jvm": {"total": 60, "name": "JVM 篇"}
  },
  "questions": {
    "java-001": {
      "title": "Java 语言有哪些特点？",
      "module": "java",
      "difficulty": "⭐ 基础",
      "tags": ["Java 概述"],
      "status": "active"
    },
    "coll-015": {
      "title": "HashMap 的 hash 函数是怎么设计的？",
      "module": "coll",
      "difficulty": "⭐⭐ 进阶",
      "tags": ["HashMap", "哈希"],
      "status": "active"
    }
  }
}
```

**用途**：
- ID → 题目内容映射
- 难度筛选
- 标签筛选
- ID 有效性验证

---

### 2. 题库文件

**路径**：`Obsidian/40-Questions/`

```
Obsidian/40-Questions/
├── Java 基础篇 - 完整题库.md (66 题)
├── 集合框架篇 - 完整题库.md (37 题)
├── JVM 篇 - 完整题库.md (60 题)
└── _archived/ (归档的旧版本)
    └── Java 基础篇 -56 题.md
```

**题目格式**：
```markdown
### 【ID: java-001】题 1：Java 语言有哪些特点？

**答案：**
1. **面向对象**：封装、继承、多态
2. **跨平台性**：一次编译，处处运行（JVM）
...
```

---

### 3. 答题记录

**路径**：`memory/random-review/YYYY-MM-DD.md`

**格式**：
```markdown
| 题号 | 题目 ID | 题目 | 模块 | 得分 | 状态 |
|------|--------|------|------|------|------|
| 1 | java-052 | String 三兄弟区别 | Java 基础 | 4/5 | 🟢 |
| 2 | coll-019 | HashMap 结构 | 集合框架 | 4/5 | 🟢 |
```

**要求**：
- ✅ 必须包含题目 ID 列
- ✅ ID 格式：`{module}-{3 位数字}`
- ✅ 得分格式：`X/5` 或 `X.X/5`

---

## 使用场景

### 场景 1：日常随机复习

**命令**：
```powershell
cd C:\Users\11237\.openclaw-autoclaw\workspace\scripts
.\random-review-selector-enhanced.ps1
```

**输出**：
```
Random Review Selector (Enhanced)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Total questions: 163
  Java Basics: 66 questions
  Collections: 37 questions
  JVM: 60 questions

  Available questions: 138
  Selected 12 questions

  1. [java-052] String 三兄弟区别... [⭐⭐ 进阶]
  2. [coll-019] HashMap 结构... [⭐⭐ 进阶]
  ...
```

---

### 场景 2：针对薄弱项复习

**命令**：
```powershell
.\random-review-selector-enhanced.ps1 -PrioritizeWeaknesses
```

**效果**：
- 50% 题目来自薄弱项
- 50% 题目均衡分布到各模块

---

### 场景 3：按难度筛选

**命令**：
```powershell
# 只复习基础题
.\random-review-selector-enhanced.ps1 -Difficulty easy

# 只复习提高题
.\random-review-selector-enhanced.ps1 -Difficulty hard

# 所有难度混合
.\random-review-selector-enhanced.ps1 -Difficulty all
```

---

### 场景 4：同步复习状态

**命令**：
```powershell
.\sync-review-state-simple.ps1
```

**功能**：
1. 扫描 `memory/dialogs/` 目录下的答题记录
2. 提取题目 ID 和得分
3. 验证 ID 有效性（对比题库映射）
4. 更新 `.random-review-state.json`
5. 更新 `.context-snapshot.json`
6. 创建同步日志

**输出**：
```
Syncing review state (simple version)...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Scanning memory/dialogs/...
  Found 1 files

Extracting data...
  Processing: 2026-03-23-session-1.md
    Found: java-052
    Found: coll-019
    Score: 4.0/5

  Total questions: 12
  Average score: 4.0/5

Validating question IDs...
  ✅ All question IDs are valid

Updating .random-review-state.json...
  Updated state file

Sync completed!
  Questions: 12
  Average: 4.0/5
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 脚本命令

### 1. 随机选题脚本

**文件**：`random-review-selector-enhanced.ps1`

**参数**：

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `-QuestionCount` | int | 12 | 选题数量 |
| `-Difficulty` | string | all | 难度筛选 (all/easy/medium/hard) |
| `-PrioritizeWeaknesses` | switch | false | 薄弱项优先 |
| `-Force` | switch | false | 跳过同步检查 |
| `-AutoMode` | switch | false | 自动模式（自动同步） |

**示例**：
```powershell
# 基础用法
.\random-review-selector-enhanced.ps1

# 选择 20 题
.\random-review-selector-enhanced.ps1 -QuestionCount 20

# 薄弱项优先
.\random-review-selector-enhanced.ps1 -PrioritizeWeaknesses

# 只复习提高题
.\random-review-selector-enhanced.ps1 -Difficulty hard

# 自动模式（自动同步后选题）
.\random-review-selector-enhanced.ps1 -AutoMode
```

---

### 2. 同步脚本

**文件**：`sync-review-state-simple.ps1`

**功能**：
- 自动扫描答题记录
- 提取题目 ID 和得分
- 验证 ID 有效性
- 更新状态文件

**无参数**，直接运行：
```powershell
.\sync-review-state-simple.ps1
```

---

### 3. 题库映射生成脚本

**文件**：`create_question_map.py`（Python）

**功能**：
- 从题库文件提取题目
- 自动生成 ID 映射
- 估算难度等级
- 提取关键词标签

**运行**：
```bash
python3 /tmp/create_question_map.py
```

**输出**：`.question-id-map.json`

---

## 扩展功能

### 1. 难度筛选

**用途**：根据当前水平选择合适难度的题目

**场景**：
- 刚开始复习 → 只复习基础题
- 考前冲刺 → 只复习提高题
- 日常复习 → 混合难度

**命令**：
```powershell
# 基础题（适合入门）
.\random-review-selector-enhanced.ps1 -Difficulty easy

# 提高题（适合冲刺）
.\random-review-selector-enhanced.ps1 -Difficulty hard
```

---

### 2. 薄弱项优先

**用途**：自动识别薄弱项，优先复习

**原理**：
- 从 `.random-review-state.json` 读取薄弱项列表
- 选题时 50% 来自薄弱项
- 50% 均衡分布到各模块

**命令**：
```powershell
.\random-review-selector-enhanced.ps1 -PrioritizeWeaknesses
```

**输出示例**：
```
  Prioritizing weaknesses...
  Found 5 weakness questions
  Selected 5 weakness questions

  1. [coll-025] ConcurrentHashMap 原理... [⭐⭐⭐ 提高] ⚠️ 薄弱项
  2. [java-054] sleep vs wait... [⭐⭐ 进阶] ⚠️ 薄弱项
  ...
```

---

### 3. ID 有效性验证

**用途**：防止答题记录中出现无效 ID

**验证规则**：
- ID 必须存在于题库映射文件
- ID 格式必须是 `{module}-{3 位数字}`
- 模块代码必须是 `java`、`coll`、`jvm` 之一

**验证失败处理**：
```
Validating question IDs...
  ⚠️ Invalid ID: java-999
  ⚠️ Found 1 invalid question IDs
```

---

### 4. 标签系统（未来扩展）

**当前实现**：
- 自动从题目文本提取关键词
- 支持的标签：HashMap、并发、GC、JVM、集合、String、异常处理、反射、泛型

**未来扩展**：
- 手动添加标签
- 按标签筛选题目
- 标签云统计

**示例**（未来）：
```powershell
# 只复习 HashMap 相关题目
.\random-review-selector-enhanced.ps1 -Tag HashMap

# 只复习并发相关题目
.\random-review-selector-enhanced.ps1 -Tag 并发
```

---

## 常见问题

### Q1: 如何添加新题目？

**步骤**：
1. 在题库文件中添加题目，格式：
   ```markdown
   ### 【ID: java-067】题 67：新题目？
   
   **答案：**
   ...
   ```
2. 运行映射生成脚本：
   ```bash
   python3 /tmp/create_question_map.py
   ```
3. 验证新 ID 是否已加入映射文件

---

### Q2: 如何修改题目难度？

**方法 1**：手动编辑映射文件
```json
{
  "questions": {
    "java-001": {
      "difficulty": "⭐⭐ 进阶"  // 修改这里
    }
  }
}
```

**方法 2**：修改 Python 脚本的难度估算逻辑
```python
# 在 create_question_map.py 中修改难度规则
if q_num <= 20:  # 原来是 10
    difficulty = '⭐ 基础'
```

---

### Q3: 答题记录中出现无效 ID 怎么办？

**原因**：
- ID 拼写错误（如 `java-0001` 应该是 `java-001`）
- 题目已被删除
- 模块代码错误（如 `jav-001` 应该是 `java-001`）

**解决方法**：
1. 检查答题记录中的 ID
2. 对照题库映射文件验证
3. 修正错误的 ID
4. 重新运行同步脚本

---

### Q4: 如何重置排除列表？

**场景**：想重新复习所有题目

**方法**：编辑 `.random-review-state.json`
```json
{
  "excludeIds": [],  // 清空数组
  "todayQuestionIds": [],
  "completedRounds": 0
}
```

---

## 总结

### 核心优势

1. ✅ **ID 索引**：稳定、唯一、不受顺序影响
2. ✅ **难度分级**：支持按难度筛选
3. ✅ **标签系统**：支持按知识点筛选
4. ✅ **薄弱项优先**：智能推荐复习题目
5. ✅ **ID 验证**：自动检测无效 ID

### 下一步计划

1. 🔄 添加标签筛选功能
2. 🔄 支持按章节筛选
3. 🔄 生成复习统计报告
4. 🔄 支持题目收藏功能

---

**文档版本**：1.0  
**最后更新**：2026-03-23  
**维护者**：AI 助手
