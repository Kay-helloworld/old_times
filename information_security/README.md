# 資通安全 (Information Security)

## 📚 資源概覽

本資料夾包含資通安全的考試資源與分析報告，涵蓋 **104-114年** 的考題。

## 📁 目錄結構

```
information_security/
├── exam_resources/
│   ├── original_pdfs/          # 原始PDF考題（46份）
│   ├── processed_text/         # 提取的文字檔案
│   ├── analysis_reports/       # 分析報告
│   │   └── infosec_comprehensive_analysis.md  # 綜合分析報告
│   └── topic_lists/
├── essay_guides/               # 申論題指南
│   ├── 01_security_management.md   # 資安管理制度 (25次)
│   ├── 02_network_security.md      # 網路安全 (21次)
│   ├── 03_network_fundamentals.md  # 資通網路基礎 (13次)
│   ├── 04_business_continuity.md   # 營運持續與復原 (10次)
│   ├── 05_cryptography.md          # 密碼學基礎 (10次)
│   ├── 06_system_security.md       # 系統與軟體安全 (6次)
│   ├── 07_emerging_tech.md         # 新興技術安全 (4次)
│   └── 08_laws_regulations.md      # 資安法令與規範 (3次)
└── practice_tools/             # 練習工具（待建立）
```

## 📖 申論題解析指南 (依重要性排序)

這些指南依照「高考三級+近三年」的考點頻率排序，建議依序閱讀：

1. [**資安管理制度**](essay_guides/01_security_management.md) ⭐⭐⭐⭐⭐
   - 核心：ISO 27001, 風險管理, 資安事件應變
2. [**網路安全**](essay_guides/02_network_security.md) ⭐⭐⭐⭐⭐
   - 核心：防火牆 (WAF/NGFW), DDoS, 零信任架構
3. [**資通網路基礎**](essay_guides/03_network_fundamentals.md) ⭐⭐⭐⭐
   - 核心：OSI/TCP模型, IP位址計算, 協定比較
4. [**營運持續與復原**](essay_guides/04_business_continuity.md) ⭐⭐⭐⭐
   - 核心：BCP/DRP, 備份策略 (3-2-1), RTO/RPO
5. [**密碼學基礎**](essay_guides/05_cryptography.md) ⭐⭐⭐
   - 核心：加解密演算法, 數位簽章, PKI
6. [**系統與軟體安全**](essay_guides/06_system_security.md) ⭐⭐⭐
   - 核心：SQL Injection, XSS, EDR/MDR
7. [**新興技術安全**](essay_guides/07_emerging_tech.md) ⭐⭐
   - 核心：IoT 安全, 雲端責任共有模型, 行動安全
8. [**資安法令與規範**](essay_guides/08_laws_regulations.md) ⭐⭐
   - 核心：資通安全管理法, 個資法

## 📊 考題分析報告

### 綜合分析報告

[**資通安全 - 歷屆考題綜合分析報告**](exam_resources/analysis_reports/infosec_comprehensive_analysis.md)

**分析維度**：

1. **全部考題** (46份) - 104-114年，所有等級
2. **近三年** (15份) - 112-114年
3. **高考三級/特考三級** (22份) - 所有年份的三級考試
4. **高考三級+近三年** (6份) - 最貼近當前高考趨勢

**七大考點分類**：
1. 密碼學基礎 (Cryptography)
2. 網路安全 (Network Security)
3. 系統與軟體安全 (System & Software Security)
4. 資安管理制度 (Security Management)
5. 營運持續與復原 (Business Continuity)
6. 資安法令與規範 (Laws & Regulations)
7. 新興技術安全 (Emerging Technologies)
8. **[NEW] 資通網路基礎 (Network Fundamentals)** - OSI、TCP/IP、IP位址計算

### 重點發現

根據分析報告，高考三級的重點領域（按重要性排序）：

1. **資安管理制度** (52次) - 佔全部49.1%
   - ISO 27001、ISMS
   - 風險管理、資產盤點

2. **網路安全** (35次) - 佔全部29.7%
   - 防火牆、IDS/IPS
   - VPN、SSL/TLS

3. **資通網路基礎** (26次) - **重要基礎**
   - OSI七層模型、TCP/IP
   - IP位址與子網計算
   - 路由與交換技術

4. **密碼學基礎** (29次) - 佔全部23.8%
   - AES、RSA等加密演算法
   - 數位簽章、PKI

5. **系統與軟體安全** (22次) - 佔全部36.1%
   - 應用程式安全、SQL Injection
   - 漏洞掃描、滲透測試

### 近三年趨勢

近三年考題（112-114年）佔比最高的類別：

- **網路安全**: 51.7% - 持續重要
- **密碼學基礎**: 50.0% - 持續重要
- **資安法令與規範**: 47.6% - 逐年增加
- **新興技術安全**: 41.2% - 雲端、IoT、零信任等新興主題

## 🔧 使用的分析工具

### PDF提取腳本

```bash
python3 shared_resources/scripts/extract_infosec_pdfs.py
```

### 分析腳本

```bash
python3 shared_resources/scripts/analyze_infosec_exams.py
```

## 📝 準備建議

基於分析結果，建議準備重點：

### 高考三級考生

1. **優先熟悉**：資安管理制度（ISO 27001、ISMS）
2. **深入理解**：網路安全技術（防火牆、IDS/IPS、VPN）
3. **掌握基礎**：密碼學原理與應用
4. **關注法規**：資通安全管理法、個資法

### 近期考試趨勢

- 雲端安全（AWS、Azure、容器安全）
- 零信任架構
- 資安法令遵循
- 事件回應與應變

## 📚 相關資源

- [主要README](../README.md) - 返回主目錄
- [資料庫應用](../database_application/) - 資料庫考題分析
- [資料結構](../data_structure/) - 資料結構考題

---

**最後更新**: 2025-11-26  
**考題涵蓋年份**: 104-114年（民國）  
**分析檔案數**: 46份
