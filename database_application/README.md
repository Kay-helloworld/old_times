# 📚 資料庫應用 - 考試準備資料

這個資料夾包含**資料庫應用**科目的所有考試準備資料，包括申論題解析、考題資源、練習工具等。

---

## 📖 申論題解析（Essay Guides）

**位置**：`essay_guides/`

這是**最重要、最常用**的資料！包含所有主題的詳細申論題解析：

| 檔案 | 主題 | 狀態 | 說明 |
|------|------|------|------|
| [00_overview_114.md](essay_guides/00_overview_114.md) | 114年度總覽 | ✅ | 114年考題完整解析與答題框架 |
| [01_sql_queries.md](essay_guides/01_sql_queries.md) | SQL & 查詢 | ✅ | JOIN、聚合函數、View、Trigger |
| [02_normalization.md](essay_guides/02_normalization.md) | 正規化 | ✅ | FD、Closure、候選鍵、2NF/3NF/BCNF |
| [03_db_design.md](essay_guides/03_db_design.md) | 資料庫設計 | ⏳ | ER Model、EER、關聯綱要設計 |
| [04_indexing_storage.md](essay_guides/04_indexing_storage.md) | 索引與儲存 | ⏳ | B樹、B+樹、Hash、RAID |
| [05_advanced_topics.md](essay_guides/05_advanced_topics.md) | 進階主題 | ⏳ | 分散式DB、NoSQL、Big Data、OLAP |
| [06_security.md](essay_guides/06_security.md) | 資訊安全 | ⏳ | 加密、授權、存取控制、SQL Injection |

✅ = 已完成　⏳ = 製作中

---

## 📊 考題資源（Exam Resources）

**位置**：`exam_resources/`

### 原始考題PDF

- **位置**：`exam_resources/original_pdfs/db/`
- **內容**：104-114年所有資料庫應用考題PDF檔案（74份）

### 處理後文字檔

- **位置**：`exam_resources/processed_text/db/`
- **內容**：從PDF提取的文字檔，方便搜尋和分析

### 題目列表

- **位置**：`exam_resources/topic_lists/`
- **檔案**：
  - `sql_questions_list.txt` - 105題 SQL 相關題目
  - `normalization_questions_list.txt` - 55題正規化題目
  - （其他主題列表陸續新增）

### 統計分析報告

- **位置**：`exam_resources/analysis_reports/`
- **檔案**：
  - `db_knowledge_analysis.md` - 知識點統計分析
  - `trend_analysis.md` - 考題趨勢分析  
  - `knowledge_analysis.md` - 整體分析報告

---

## 🛠️ 練習工具（Practice Tools）

**位置**：`practice_tools/`

### 交易管理完整教材

- **位置**：`practice_tools/transaction_practice/`
- **內容**：
  - 學習計畫、概念解析
  - 詳細教材（Part 1 & 2）
  - 完整案例研究
  - 操作指南、練習題

### B樹練習

- **位置**：`practice_tools/btree_practice/`
- **內容**：
  - 112年、114年 B樹考題
  - Python實作與詳細解析

### 資料庫實作練習

- **位置**：`practice_tools/db_hands_on/`
- **內容**：
  - DBeaver 視覺化教學
  - 資料庫練習指南
  - Demo SQL腳本
  - 練習管理工具

### 演算法練習題

- **位置**：`practice_tools/algorithm_exercises/`
- **內容**：
  - 二項式係數、成績輸入、佇列、圖論、雜湊等Python練習題

---

## 📈 知識點統計（基於74份考題）

| 知識點 | 歷年總計 | 近三年 | 114年 | 重要度 |
|-------|---------|--------|-------|--------|
| 資料庫設計 | 697次 | 139次 | 46次 | ⭐⭐⭐⭐⭐ |
| 交易管理 | 323次 | 126次 | 73次 | ⭐⭐⭐⭐⭐ |
| SQL & 查詢 | 261次 | 45次 | 19次 | ⭐⭐⭐⭐ |
| 正規化 | 238次 | 49次 | 12次 | ⭐⭐⭐⭐ |
| 進階主題 | 111次 | 23次 | 7次 | ⭐⭐⭐ |
| 索引與儲存 | 30次 | 5次 | 3次 | ⭐⭐ |
| 資訊安全 | 13次 | 2次 | 2次 | ⭐⭐ |

---

## 🎯 學習建議

### 第一階段：掌握核心主題（優先度最高）

1. **交易管理** - 佔分最重！
   - 先看：`essay_guides/` 中的交易管理部分（待完成）
   - 再練：`practice_tools/transaction_practice/` 完整教材

2. **資料庫設計** - 幾乎必考！
   - 學習：ER Model、EER Model
   - 練習：從需求畫出 ER Diagram

3. **正規化** - 傳統重點！
   - 精讀：`essay_guides/02_normalization.md`
   - 重點：功能相依（FD）推導

4. **SQL查詢** - 基本功！
   - 精讀：`essay_guides/01_sql_queries.md`
   - 練習：JOIN、GROUP BY、子查詢

### 第二階段：進階主題

5. **索引與儲存** - B樹必考
   - 練習：`practice_tools/btree_practice/`

6. **進階主題** - Big Data、NoSQL
   - 了解基本概念即可

7. **資訊安全** - 較少考，但有出現趨勢
   - 重點：存取控制、SQL Injection

---

## 🔍 如何使用這個資料夾

### 情境一：準備考試複習

```
1. 進入 essay_guides/
2. 按 00-06 順序閱讀
3. 重點主題多看幾次
```

### 情境二：查找特定題目

```
1. 進入 exam_resources/topic_lists/
2. 找到對應的題目列表
3. 查看題目內容
```

### 情境三：實作練習

```
1. 進入 practice_tools/[主題]/
2. 跟著教學操作
3. 完成練習題
```

### 情境四：查看統計分析

```
1. 進入 exam_resources/analysis_reports/
2. 閱讀知識點分析
3. 掌握考試趨勢
```

---

## 📞 需要幫助？

- 查看主專案的 [README.md](../README.md)
- 每個子資料夾都有詳細說明

---

**加油！資料庫應用拿高分！💪**
