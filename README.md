# 🎓 公務員考試準備系統

這是一個完整的多科目考試準備系統，目前包含**資料庫應用**、**資料結構**、**資通安全**、**資訊管理**等科目的考題分析與練習工具。

---

## 📂 專案結構

```
antigravity/
├── 📚 database_application/      # 資料庫應用（當前重點）
├── 📚 data_structure/           # 資料結構
├── 📚 information_security/     # 資通安全
├── 📚 information_management/   # 資訊管理
├── 🔧 shared_resources/         # 共用工具與資料集
├── dbpractice                   # SQLite 練習資料庫
├── history.json                 # 學習歷史記錄
└── README.md                    # 本文件
```

---

## 🎯 快速導航

### 資料庫應用（Database Application）

#### ⭐ 申論題解析（最常用！）

- 📖 [00_overview_114.md](database_application/essay_guides/00_overview_114.md) - 114年度完整解析
- 📖 [01_sql_queries.md](database_application/essay_guides/01_sql_queries.md) - SQL & 查詢
- 📖 [02_normalization.md](database_application/essay_guides/02_normalization.md) - 正規化
- 📖 [03_db_design.md](database_application/essay_guides/03_db_design.md) - 資料庫設計
- 📖 [04_indexing_storage.md](database_application/essay_guides/04_indexing_storage.md) - 索引與儲存
- 📖 [05_advanced_topics.md](database_application/essay_guides/05_advanced_topics.md) - 進階主題
- 📖 [06_security.md](database_application/essay_guides/06_security.md) - 資訊安全

#### 📊 考題資源

- **關鍵字分析**：[完整分析報告](database_application/exam_resources/analysis_reports/db_knowledge_analysis_v2.md)
- [題目列表](database_application/exam_resources/topic_lists/)
- [原始考題PDF](database_application/exam_resources/original_pdfs/db/)
- [處理後文字檔](database_application/exam_resources/processed_text/db/)

#### 🛠️ 練習工具

- [交易管理完整教材](database_application/practice_tools/transaction_practice/)
- [B樹練習](database_application/practice_tools/btree_practice/)
- [資料庫實作練習](database_application/practice_tools/db_hands_on/)
- [演算法練習題](database_application/practice_tools/algorithm_exercises/)

---

### 其他科目

#### 資料結構（Data Structure）

- 📊 **關鍵字分析**：[完整分析報告](data_structure/exam_resources/analysis_reports/data_structure_comprehensive_analysis.md)
- 📝 **原始考題**：[考題文字檔資料夾](data_structure/exam_resources/processed_text/)
- 📖 申論題解析：[essay_guides/](data_structure/essay_guides/)
- 🛠️ 練習工具：[practice_tools/](data_structure/practice_tools/)

#### 資通安全（Information Security）

- 📊 **關鍵字分析**：[完整分析報告](information_security/exam_resources/analysis_reports/infosec_comprehensive_analysis.md)
- 📝 **原始考題**：[考題文字檔資料夾](information_security/exam_resources/processed_text/)
- 📖 申論題解析：[essay_guides/](information_security/essay_guides/)
- 🛠️ 練習工具：[practice_tools/](information_security/practice_tools/)

#### 資訊管理（Information Management）

- 📊 **關鍵字分析**：[完整分析報告](information_management/exam_resources/analysis_reports/information_management_comprehensive_analysis.md)
- 📝 **原始考題**：[考題文字檔資料夾](information_management/exam_resources/processed_text/)
- 📖 申論題解析：[essay_guides/](information_management/essay_guides/)
- 🛠️ 練習工具：[practice_tools/](information_management/practice_tools/)

---

## 🔧 共用資源

### 工具腳本

位置：`shared_resources/scripts/`

- `analyze_db_exams.py` - 資料庫考題分析
- `find_sql_questions.py` - 搜尋 SQL 相關題目
- `find_normalization_questions.py` - 搜尋正規化題目
- `exam_manager.py` - 考題管理工具
- 其他工具腳本...

### 資料集

位置：`shared_resources/datasets/`

---

## 💡 使用方式

### 準備考試（最常見）

1. **打開對應科目的 `essay_guides/` 資料夾**

   ```
   例如：database_application/essay_guides/
   ```

2. **按編號順序閱讀申論解析**
   - 00 開頭 = 年度總覽
   - 01-06 = 各主題詳細解析

3. **需要時查閱統計分析**

   ```
   database_application/exam_resources/analysis_reports/
   ```

### 實作練習

1. **進入 `practice_tools/` 對應的主題**

   ```
   例如：database_application/practice_tools/transaction_practice/
   ```

2. **跟著練習指南操作**

### 搜尋特定題目

1. **查看題目列表**

   ```
   database_application/exam_resources/topic_lists/
   ```

2. **使用搜尋腳本**

   ```bash
   cd shared_resources/scripts/
   python3 find_sql_questions.py
   ```

---

## 📚 每個科目的統一結構

所有科目都遵循相同的組織結構：

```
[科目名稱]/
├── essay_guides/         # 申論題解析（最重要！）
│   ├── 00_overview.md   # 總覽
│   ├── 01_topic1.md     # 主題一
│   ├── 02_topic2.md     # 主題二
│   └── ...
│
├── exam_resources/       # 考題資源
│   ├── original_pdfs/   # 原始PDF
│   ├── processed_text/  # 文字檔
│   ├── topic_lists/     # 題目列表
│   └── analysis_reports # 統計分析
│
└── practice_tools/       # 練習工具
    ├── [主題1]/
    ├── [主題2]/
    └── ...
```

---

## 🎯 學習建議

### 資料庫應用

**建議順序**：

1. 先看 `00_overview_114.md` 了解整體趨勢
2. 依序學習各主題申論解析（01-06）
3. 配合 `practice_tools` 進行實作
4. 定期查閱統計分析，掌握考試重點

**重點主題**（依據歷年統計）：

1. ⭐⭐⭐ 交易管理（出題最多）
2. ⭐⭐⭐ 資料庫設計
3. ⭐⭐ 正規化
4. ⭐⭐ SQL 查詢

---

## 🔄 版本更新

### 2025-11-25

- ✅ 重新組織專案結構，支援多科目
- ✅ 完成資料庫應用全系列申論解析：
  - SQL與查詢、正規化
  - 資料庫設計、索引與儲存
  - 進階主題 (NoSQL, Big Data)
  - 資訊安全 (SQL Injection, Audit)

---

## 📞 需要幫助？

每個資料夾內都有 README.md 詳細說明該部分的使用方式。

---

**祝考試順利！💪**
