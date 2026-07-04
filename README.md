# 🎓 公務員考試準備系統

這是一個完整的多科目考試準備系統，目前包含**資料庫應用**、**資料結構**、**資通網路與安全**、**資訊管理**等科目的考題分析與練習工具。

> ℹ️ **科目說明**：「資通網路與安全」（含網路通訊與資訊安全）統一收錄於 `information_security/` 資料夾中管理。

---

## 📂 專案結構

```
antigravity/
├── 📚 database_application/      # 資料庫應用
├── 📚 data_structure/            # 資料結構
├── 📚 information_security/      # 資通網路與安全（含網路通訊）
├── 📚 information_management/    # 資訊管理
├── 🔧 shared_resources/          # 共用工具與資料集
├── dbpractice                    # SQLite 練習資料庫
├── history.json                  # 學習歷史記錄
└── README.md                     # 本文件
```

---

## 🎯 快速導航

### 資料庫應用（Database Application）

#### ⭐ 申論題解析（最常用！）

各分類題目（考題原文）：

- 📖 [01_SQL_and_Programming.md](database_application/essay_guides/01_SQL_and_Programming.md) - SQL語法與程式設計
- 📖 [02_Database_Design.md](database_application/essay_guides/02_Database_Design.md) - 資料庫設計（ER Model）
- 📖 [03_Normalization_Theory.md](database_application/essay_guides/03_Normalization_Theory.md) - 正規化理論
- 📖 [04_Transaction_Management.md](database_application/essay_guides/04_Transaction_Management.md) - 交易管理
- 📖 [05_Advanced_Systems.md](database_application/essay_guides/05_Advanced_Systems.md) - 進階系統（NoSQL、Big Data）
- 📖 [06_Administration_Security.md](database_application/essay_guides/06_Administration_Security.md) - 管理與安全（索引、備份）
- 📖 [07_Unclassified_Questions.md](database_application/essay_guides/07_Unclassified_Questions.md) - 未分類題目
- 📖 [local_gov_exam_questions.md](database_application/essay_guides/local_gov_exam_questions.md) - 地方特考歷年考題

各分類詳細解析（_ANALYSIS 檔案）：

- 📝 [01_SQL_and_Programming_ANALYSIS.md](database_application/essay_guides/01_SQL_and_Programming_ANALYSIS.md) - SQL解析與答題架構
- 📝 [02_Database_Design_ANALYSIS.md](database_application/essay_guides/02_Database_Design_ANALYSIS.md) - 資料庫設計解析
- 📝 [03_Normalization_Theory_ANALYSIS.md](database_application/essay_guides/03_Normalization_Theory_ANALYSIS.md) - 正規化解析（含Closure、候選鍵）
- 📝 [04_Transaction_Management_ANALYSIS.md](database_application/essay_guides/04_Transaction_Management_ANALYSIS.md) - 交易管理解析
- 📝 [05_Advanced_Systems_ANALYSIS.md](database_application/essay_guides/05_Advanced_Systems_ANALYSIS.md) - 進階系統解析
- 📝 [06_Administration_Security_ANALYSIS.md](database_application/essay_guides/06_Administration_Security_ANALYSIS.md) - 管理安全解析
- 📝 [資料庫建立與維護完整流程指南.md](database_application/essay_guides/資料庫建立與維護完整流程指南.md) - 建立到維護完整流程

#### 📊 考題資源

- **關鍵字分析**：[db_knowledge_analysis_v2.md](database_application/exam_resources/analysis_reports/db_knowledge_analysis_v2.md)
- [分類報告](database_application/essay_guides/classification_report.md)

---

### 資料結構（Data Structure）

#### ⭐ 申論題解析

- 📖 [exam_preparation_guide.md](data_structure/essay_guides/exam_preparation_guide.md) - 完整備考指南
- 📖 [01_tree_structures_analysis.md](data_structure/essay_guides/01_tree_structures_analysis.md) - 樹狀結構分析
- 📖 [02_graph_algorithms_analysis.md](data_structure/essay_guides/02_graph_algorithms_analysis.md) - 圖形演算法分析
- 📖 [local_gov_exam_questions.md](data_structure/essay_guides/local_gov_exam_questions.md) - 地方特考歷年考題
- 📖 [local_gov_112_113_analysis.md](data_structure/essay_guides/local_gov_112_113_analysis.md) - 112-113年解析
- 📖 [classified_questions/](data_structure/essay_guides/classified_questions/) - 分類題目資料夾

#### 📊 考題資源

- **關鍵字分析**：[data_structure_comprehensive_analysis.md](data_structure/exam_resources/analysis_reports/data_structure_comprehensive_analysis.md)

---

### 資通網路與安全（Information Security & Network）

> ℹ️ **說明**：本科目涵蓋「資通網路」與「資訊安全」兩大領域，統一在此管理。
> 網路通訊主題（OSI、TCP/IP、IP計算）收錄於分類 `01_network_communication`。

#### ⭐ 申論題解析（分類題目）

- 📖 [01_network_communication.md](information_security/essay_guides/classified_questions/01_network_communication.md) - 網路通訊基礎（OSI、TCP/IP）
- 📖 [01_network_communication_ANALYSIS.md](information_security/essay_guides/classified_questions/01_network_communication_ANALYSIS.md) - 網路通訊解析
- 📖 [02_network_security_defense.md](information_security/essay_guides/classified_questions/02_network_security_defense.md) - 網路安全防禦
- 📖 [02_network_security_defense_ANALYSIS.md](information_security/essay_guides/classified_questions/02_network_security_defense_ANALYSIS.md) - 網路安全解析
- 📖 [03_emerging_tech_cloud.md](information_security/essay_guides/classified_questions/03_emerging_tech_cloud.md) - 新興技術與雲端
- 📖 [03_emerging_tech_cloud_ANALYSIS.md](information_security/essay_guides/classified_questions/03_emerging_tech_cloud_ANALYSIS.md) - 新興技術解析
- 📖 [04_info_systems_management.md](information_security/essay_guides/classified_questions/04_info_systems_management.md) - 資訊系統管理
- 📖 [05_management_law_forensics.md](information_security/essay_guides/classified_questions/05_management_law_forensics.md) - 資安管理與法規
- 📖 [06_malware_attack_vectors.md](information_security/essay_guides/classified_questions/06_malware_attack_vectors.md) - 惡意程式與攻擊手法
- 📖 [07_app_web_security.md](information_security/essay_guides/classified_questions/07_app_web_security.md) - 應用程式與網站安全
- 📖 [08_cryptography_fundamentals.md](information_security/essay_guides/classified_questions/08_cryptography_fundamentals.md) - 密碼學基礎

#### 📋 歷年完整解析

- 📖 [112-113年地方政府特考三等_資通網路與安全_完整解析.md](information_security/essay_guides/112-113年地方政府特考三等_資通網路與安全_完整解析.md)
- 📖 [112年地方政府特考三等_資通網路與安全_完整解析.md](information_security/essay_guides/112年地方政府特考三等_資通網路與安全_完整解析.md)

#### 📊 考題資源

- **關鍵字分析**：[infosec_comprehensive_analysis.md](information_security/exam_resources/analysis_reports/infosec_comprehensive_analysis.md)

---

### 資訊管理（Information Management）

#### ⭐ 申論題解析

- 📖 [01_information_security_analysis.md](information_management/essay_guides/01_information_security_analysis.md) - 資訊安全管理
- 📖 [02_system_development_analysis.md](information_management/essay_guides/02_system_development_analysis.md) - 系統開發
- 📖 [03_data_analysis_bi_analysis.md](information_management/essay_guides/03_data_analysis_bi_analysis.md) - 資料分析與BI
- 📖 [04_cloud_emerging_tech_analysis.md](information_management/essay_guides/04_cloud_emerging_tech_analysis.md) - 雲端與新興技術
- 📖 [06_enterprise_management_analysis.md](information_management/essay_guides/06_enterprise_management_analysis.md) - 企業管理
- 📖 [sdlc_development_process_analysis.md](information_management/essay_guides/sdlc_development_process_analysis.md) - SDLC系統開發流程詳析
- 📖 [local_gov_exam_questions.md](information_management/essay_guides/local_gov_exam_questions.md) - 地方特考歷年考題
- 📖 [112年地方政府特考三等_資訊管理_完整解析.md](information_management/essay_guides/112年地方政府特考三等_資訊管理_完整解析.md)
- 📖 [113年地方政府特考三等_資訊管理_完整解析.md](information_management/essay_guides/113年地方政府特考三等_資訊管理_完整解析.md)
- 📖 [classified_questions/](information_management/essay_guides/classified_questions/) - 分類題目資料夾

#### 📊 考題資源

- **關鍵字分析**：[information_management_comprehensive_analysis.md](information_management/exam_resources/analysis_reports/information_management_comprehensive_analysis.md)

---

## 🔧 共用資源

### 工具腳本

位置：`shared_resources/scripts/`

各科目的 exam_resources 資料夾中也有各自的分析腳本（Python）。

---

## 💡 使用方式

### 準備考試（最常見）

1. **打開對應科目的 `essay_guides/` 資料夾**

   ```
   例如：database_application/essay_guides/
   ```

2. **依主題閱讀考題原文（無 _ANALYSIS 後綴）與解析（有 _ANALYSIS 後綴）**

3. **需要統計時查閱 `analysis_reports/`**

   ```
   database_application/exam_resources/analysis_reports/
   ```

---

## 📚 各科目的統一結構

```
[科目名稱]/
├── essay_guides/               # 申論題解析（最重要！）
│   ├── classified_questions/  # 依主題分類的題目與解析
│   ├── local_gov_exam_questions.md  # 地方特考歷年彙整
│   └── [年份]_完整解析.md     # 特定年份完整解析
│
├── exam_resources/             # 考題資源
│   ├── original_pdfs/         # 原始PDF
│   ├── processed_text/        # 文字檔
│   ├── topic_lists/           # 題目列表
│   └── analysis_reports/      # 統計分析
│
└── practice_tools/             # 練習工具
```

---

## 🎯 學習建議

### 資料庫應用（重點排序）

1. ⭐⭐⭐ SQL語法與程式設計（出題最多，約45%）
2. ⭐⭐⭐ 資料庫設計（ER Model，約30%）
3. ⭐⭐⭐ 正規化理論（FD、候選鍵、BCNF）
4. ⭐⭐ 交易管理（ACID、Lock）

### 資通網路與安全（重點排序）

1. ⭐⭐⭐ 資安管理制度（ISO 27001、ISMS）
2. ⭐⭐⭐ 網路安全（防火牆、IDS/IPS、零信任）
3. ⭐⭐⭐ 資通網路基礎（OSI、TCP/IP、IP計算）
4. ⭐⭐ 密碼學（AES、RSA、數位簽章）
5. ⭐⭐ 資安法規（資通安全管理法、個資法）

---

## 🔄 版本更新

### 2026-07-04

- ✅ 修正 README 中所有失效的超連結，對應實際檔案結構
- ✅ 說明「資通網路」已整合於 `information_security/` 中管理

### 2025-12-06

- ✅ 新增：資料庫建立與維護完整流程指南
- ✅ 新增：SDLC系統開發流程分析文件

### 2025-11-25

- ✅ 重新組織專案結構，支援多科目
- ✅ 完成資料庫應用全系列申論解析

---

**祝考試順利！💪**
