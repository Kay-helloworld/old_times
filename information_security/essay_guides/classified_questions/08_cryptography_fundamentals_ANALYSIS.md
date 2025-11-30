# 密碼學基礎 完整題目解析 - 申論題答題框架

這份文件針對**密碼學基礎**相關題目提供詳盡的申論題答題架構，涵蓋對稱/非對稱加密、雜湊函數、數位簽章、PKI 公開金鑰基礎建設、SSL/TLS 等核心考點。

---

## 📊 題目總覽

### 題目統計表

| 統計項目 | 數量 |
|---------|------|
| **分析考卷總數** | **11 份（104-114年）** |
| **密碼學相關題目** | **18 題** |
| **高考三級+近三年出現次數** | 12 次 |
| **重要性排名** | **No. 3** |

### 題型分類表

| 題型 | 占比 | 代表題目 | 難度 |
|------|------|---------|------|
| **加密演算法（對稱/非對稱）** | 35% | RSA、AES 原理與應用 | ⭐⭐⭐⭐ |
| **雜湊函數與完整性** | 20% | SHA、碰撞問題 | ⭐⭐⭐ |
| **數位簽章** | 25% | 簽章產生與驗證、不可否認性 | ⭐⭐⭐⭐ |
| **PKI 基礎建設** | 15% | CA、RA、CRL 架構 | ⭐⭐⭐ |
| **SSL/TLS 混合式加密** | 10% | Handshake 流程、會話金鑰 | ⭐⭐⭐⭐⭐ |

**難度星級說明**：
- ⭐⭐⭐ = 基礎必考（定義、基本原理）
- ⭐⭐⭐⭐ = 進階重要（運作流程、實務應用）
- ⭐⭐⭐⭐⭐ = 新興熱門（混合式加密、零信任架構）

---

## 🎯 申論題答題黃金架構

### 架構 1：加密演算法題型

```
第一部分：定義與分類 (15%)
├─ 清楚定義該加密類型
├─ 說明與其他類型的差異
└─ 闡述主要用途

第二部分：運作原理 (50%)
├─ 詳細說明加解密流程
├─ 公式或演算法說明（可選）
├─ 繪製流程圖或示意圖
└─ 舉例說明實際應用

第三部分：安全特性與比較 (20%)
├─ 列舉優點與缺點
├─ 與其他方法比較
└─ 說明適用情境

第四部分：實務應用 (15%)
├─ 實際應用場景（HTTPS、Email）
├─ 常見演算法（RSA、AES）
└─ 安全性建議
```

### 架構 2：數位簽章/PKI 題型

```
第一部分：定義與目的 (15%)
├─ 定義關鍵術語
├─ 說明為何需要（問題背景）
└─ 主要功能與目標

第二部分：元件/流程說明 (50%)
├─ PKI：列舉五大元件與功能
├─ 數位簽章：產生與驗證流程
├─ 繪製架構圖或流程圖
└─ 關鍵步驟詳解

第三部分：安全特性 (20%)
├─ 完整性（Integrity）
├─ 身分鑑別（Authentication）
├─ 不可否認性（Non-repudiation）
└─ 機密性（Confidentiality，可選）

第四部分：實務應用與挑戰 (15%)
├─ 實際應用案例
├─ 可能面臨的挑戰
└─ 解決方案或最佳實務
```

---

## 📚 【核心知識】完全解析

### 一、加密演算法分類

#### 對稱式加密 vs 非對稱式加密

| 比較項目 | 對稱式加密 | 非對稱式加密 |
|---------|-----------|------------|
| **金鑰數量** | 1 把（共用） | 2 把（公鑰+私鑰） |
| **加解密金鑰** | 相同 | 不同（公鑰加密、私鑰解密） |
| **速度** | ✅ **快**（適合大量資料） | ❌ 慢（約慢 1000 倍） |
| **金鑰分配** | ⚠️ **困難**（需安全通道） | ✅ 容易（公鑰公開） |
| **常見演算法** | AES, DES, 3DES, ChaCha20 | RSA, ECC, ElGamal |
| **適用場景** | 資料傳輸加密、磁碟加密 | 金鑰交換、數位簽章 |
| **實例** | 檔案加密、VPN 通道 | HTTPS 握手、Email 簽章 |

**記憶口訣**：
- **對稱**：「一把鑰匙開一鎖」→ 快但難分配
- **非對稱**：「公鑰上鎖、私鑰開鎖」→ 慢但易分配

---

### 二、雜湊函數（Hash Function）特性

**定義**：將任意長度的輸入，轉換為固定長度的輸出（雜湊值/摘要）。

**四大特性**：

| 特性 | 說明 | 用途 |
|------|------|------|
| **單向性（One-way）** | 無法從雜湊值反推原始資料 | 密碼儲存 |
| **固定長度** | 不論輸入多長，輸出長度固定（如 SHA-256 = 256 bits） | 資料完整性驗證 |
| **抗碰撞性（Collision Resistance）** | 極難找到兩個不同輸入產生相同雜湊值 | 防偽造 |
| **雪崩效應（Avalanche Effect）** | 輸入改變 1 bit，輸出應改變約 50% bits | 偵測竄改 |

**常見演算法比較**：

| 演算法 | 輸出長度 | 安全性 | 狀態 | 應用 |
|--------|---------|-------|------|------|
| **MD5** | 128 bits | ❌ 已破解 | ⛔ **棄用** | （僅用於非安全性用途，如檔案校驗） |
| **SHA-1** | 160 bits | ⚠️ 碰撞可能 | ⛔ **即將棄用** | Git（逐步淘汰中） |
| **SHA-256** | 256 bits | ✅ 安全 | ✅ **推薦** | 區塊鏈、憑證、密碼雜湊 |
| **SHA-3** | 可變 | ✅ 安全 | ✅ 最新標準 | 高安全需求場景 |
| **bcrypt** | - | ✅ 安全 | ✅ **密碼專用** | 密碼儲存（含鹽值+成本因子） |

---

### 三、數位簽章核心原理

**數位簽章 = 雜湊函數 + 非對稱式加密**

**流程對比**：

```
加密傳輸（保護機密性）：
發送者 → 用接收者【公鑰】加密 → 接收者用【私鑰】解密

數位簽章（保護完整性+鑑別）：
發送者 → 用自己【私鑰】簽署 → 接收者用發送者【公鑰】驗證
```

**記憶口訣**：
- **加密傳輸**：「公鑰加密、私鑰解密」→ 只有接收者能讀
- **數位簽章**：「私鑰簽署、公鑰驗證」→ 證明是我發的

---

### 四、PKI 五大元件

```
PKI 架構圖：

使用者 (End User)
    ↓ (申請憑證)
RA (註冊管理中心)
    ↓ (審核通過)
CA (憑證管理中心) → 簽發憑證 → Certificate (數位憑證)
    ↓ (撤銷憑證)
CRL (憑證撤銷列表)
    ↓
Repository (憑證儲存庫) ← 使用者查詢
```

**元件功能速記**：
- **CA**：簽發與撤銷憑證（信任根源）
- **RA**：前端審核員（驗證身分）
- **Certificate**：網路身分證（含公鑰+簽章）
- **CRL**：黑名單（已失效憑證）
- **Repository**：公開目錄（LDAP/HTTP）

---

### 五、SSL/TLS 混合式加密

**為何需要混合式**？

| 需求 | 非對稱式 | 對稱式 | 混合式（TLS） |
|------|---------|-------|-------------|
| **安全金鑰交換** | ✅ | ❌ | ✅ 用非對稱交換金鑰 |
| **快速資料傳輸** | ❌ | ✅ | ✅ 用對稱加密資料 |
| **身分驗證** | ✅ | ❌ | ✅ 用憑證驗證 |

**TLS Handshake 簡化流程**：

```
1. Client Hello → Server（支援的加密套件）
2. Server Hello → Client（選定的加密套件）
3. Server → 傳送數位憑證（含公鑰）
4. Client 驗證憑證
5. Client → 產生「預主金鑰」，用 Server 公鑰加密傳送
6. Server 用私鑰解密，雙方推導出「會話金鑰」
7. ✅ 後續通訊使用會話金鑰（對稱式加密）
```

---

### 【題型一】資訊安全三大元素與密碼學應用

#### 📖 原題 (112年高考三級)

> **題目**：
> 1. 請說明機密性，並說明如何應用非對稱式密碼學達成。
> 2. 請說明完整性，並說明其主要演算法暨應注意事項。

#### 🎯 答題架構分析

1.  **機密性**：定義 -> 非對稱應用 (公鑰加密、私鑰解密)。
2.  **完整性**：定義 -> 雜湊演算法 (SHA) -> 注意事項 (碰撞、雪崩)。

#### 📊 評分建議 (預估配分 25 分)

**第一小題：機密性與非對稱加密（12 分）**

**機密性定義（3 分）**
- 定義說明（2 分）
  - 只有授權者可存取（1 分）
  - 防止未授權洩漏（1 分）
- 重要性說明（1 分）

**非對稱式密碼學應用（9 分）**
- 基本機制（4 分）
  - 公鑰加密概念（2 分）
  - 私鑰解密概念（2 分）
- 運作流程（3 分）
  - 發送者使用接收者公鑰加密（1 分）
  - 接收者用私鑰解密（1 分）
  - 第三者無法解密（1 分）
- 實際應用範例（2 分）
  - RSA 演算法（1 分）
  - 實務案例（Email 加密、HTTPS）（1 分）

**第二小題：完整性與雜湊演算法（13 分）**

**完整性定義（3 分）**
- 定義說明（2 分）
  - 確保資料未被竄改（1 分）
  - 可偵測異動（1 分）
- 重要性說明（1 分）

**雜湊演算法說明（6 分）**
- 雜湊特性（3 分）
  - 單向性（1 分）
  - 固定長度輸出（1 分）
  - 微小變更產生巨大差異（1 分）
- 常見演算法（3 分）
  - SHA-256（2 分）
  - MD5（已棄用）（1 分）

**注意事項（4 分）**
- 碰撞問題（2 分）
  - 碰撞定義（1 分）
  - 為何要避免碰撞（1 分）
- 雪崩效應（1 分）
  - 說明概念
- 演算法選擇（1 分）
  - 避免使用 MD5、SHA-1

**答題提示**：
- ✅ 要說明**公鑰加密、私鑰解密**的機制
- ✅ 舉**實際應用範例**（Email、HTTPS）
- ✅ 雜湊要提到**單向性**與**碰撞問題**
- ✅ 說明為何 **MD5 已不安全**
- ⚠️ 兩小題分開作答，架構要清楚


**第二部分：三種弱點與防禦 (12 分)**

每個弱點 4 分：
- 弱點說明 (1.5 分)
- 攻擊範例 (1 分)
- 防禦措施 (1.5 分)

**建議選擇**：
- ✅ **A01 - Broken Access Control**（2021 新榜首，必考）
- ✅ **A03 - Injection**（經典弱點）
- ✅ **A07 - Identification & Authentication Failures**（實務常見）

**第三部分：SAST vs DAST (8 分)**
- SAST 定義與特性 (3 分)
- DAST 定義與特性 (3 分)
- 差異對比與適用時機 (2 分)

**答題提示**：
- ✅ 必須提及 OWASP Top 10:2021 的版本（若題目未指定年份）
- ✅ 弱點舉例需包含「技術原理」與「實際案例」
- ✅ SAST/DAST 要強調「測試時機」的差異
- ⚠️ 避免只列出 Top 10 清單而不解釋


#### ✍️ 標準答案示範

**解答**：

**一、機密性 (Confidentiality) 與非對稱式密碼學應用**

### 1. 機密性定義

**機密性（Confidentiality）** 是資訊安全三大要素（CIA Triad）之一，定義為：

> **確保資訊僅能被授權的使用者、實體或程序存取，防止未經授權的洩漏或揭露。**

**重要性**：
- **個人隱私保護**：個資法要求保護個人資料不外洩
- **商業機密保護**：防止商業機密、客戶資料外洩
- **國家安全**：機密文件、軍事情報的保護
- **合規要求**：GDPR、HIPAA 等法規要求

**機密性的威脅範例**：
- 資料外洩（Data Breach）：駭客入侵竊取客戶資料
- 竊聽（Eavesdropping）：網路傳輸被攔截
- 內部洩密（Insider Threat）：員工洩漏機密
- 社交工程（Social Engineering）：騙取敏感資訊

---

### 2. 非對稱式密碼學達成機密性

**非對稱式密碼學（Asymmetric Cryptography）**，又稱公開金鑰密碼學（Public Key Cryptography），利用**一對金鑰**（公鑰+私鑰）來達成機密性。

#### 運作機制：

**金鑰特性**：
- **公開金鑰（Public Key）**：可公開散佈，任何人都可取得
- **私密金鑰（Private Key）**：必須保密，僅持有者擁有
- **數學關聯**：兩把金鑰在數學上相關，但無法從公鑰推導出私鑰

**加密傳輸流程**：

```
情境：Alice 要傳送機密訊息給 Bob

步驟 1：金鑰產生
Bob → 產生一對金鑰（Public Key 公開，Private Key 保密）

步驟 2：公鑰分發
Bob → 將 Public Key 發布在公開目錄（或傳給 Alice）

步驟 3：加密
Alice → 取得 Bob 的 Public Key
Alice → 用 Bob 的 Public Key 加密訊息 M
      Ciphertext = Encrypt(Bob_PublicKey, M)

步驟 4：傳輸
Alice → 將密文 (Ciphertext) 透過不安全通道傳送給 Bob

步驟 5：解密
Bob → 用自己的 Private Key 解密密文
    M = Decrypt(Bob_PrivateKey, Ciphertext)

結果：
✅ 只有 Bob 能用私鑰解密，確保機密性
✅ 即使密文被攔截，攻擊者無法解密（沒有 Bob 的私鑰）
```

---

#### 為何能確保機密性？

1. **私鑰獨有性**：
   - 私鑰只有 Bob 擁有，其他人無法取得
   - 即使公鑰被所有人知道，也無法反推出私鑰

2. **單向陷門函數（Trapdoor Function）**：
   - 用公鑰加密很容易
   - 但不知道私鑰的情況下，解密在計算上不可行（需數百年運算）
   - 知道私鑰的情況下，解密很容易

3. **第三方無法解密**：
   - 攻擊者可能截獲密文
   - 但沒有私鑰，無法還原明文
   - 暴力破解在現有運算能力下不可行

---

#### 實際應用範例

**範例 1：Email 加密（PGP/GPG）**

```
場景：Alice 要寄機密 Email 給 Bob

1. Bob 產生金鑰對，將公鑰上傳到金鑰伺服器
2. Alice 撰寫 Email，選擇「加密」功能
3. Email 軟體自動：
   - 從金鑰伺服器下載 Bob 的公鑰
   - 用 Bob 的公鑰加密 Email 內容
4. 加密後的 Email 僅 Bob 能用私鑰解密閱讀

保護內容：
✅ Email 正文
✅ 附件檔案
✅ 敏感資訊

實際工具：
- PGP (Pretty Good Privacy)
- GPG (GNU Privacy Guard)
- S/MIME (Email 加密標準)
```

**範例 2：HTTPS 網站連線**

```
場景：使用者瀏覽器連線到銀行網站

1. 銀行網站持有數位憑證（含公鑰）
2. 瀏覽器取得銀行的公鑰
3. 瀏覽器產生「會話金鑰」(Session Key)，用銀行公鑰加密傳送
4. 只有銀行能用私鑰解密，取得會話金鑰
5. 後續通訊使用會話金鑰進行對稱式加密（效能考量）

保護內容：
✅ 登入帳號密碼
✅ 信用卡資訊
✅ 個人資料
✅ 交易記錄

技術標準：
- TLS 1.2 / 1.3 (Transport Layer Security)
- RSA 或 ECDHE 金鑰交換
```

**範例 3：雲端儲存加密**

```
場景：公司將機密文件上傳到雲端

1. 公司產生金鑰對，私鑰保存在公司內部
2. 文件上傳前，用公司的公鑰加密
3. 加密後的文件上傳到雲端（如 AWS S3）
4. 即使雲端服務商或駭客取得檔案，也無法解密
5. 只有公司員工用私鑰才能解密

優點：
✅ 零信任（Zero Trust）架構
✅ 即使雲端被入侵，資料仍受保護
```

---

#### 常見非對稱式演算法

**1. RSA（Rivest-Shamir-Adleman）**

- **發明時間**：1977 年
- **安全基礎**：**大質數分解困難性**（Factorization Problem）
- **金鑰長度**：2048 bits（目前建議）、3072 bits（高安全）、4096 bits（極高安全）
- **應用**：SSL/TLS、Email 加密、程式碼簽章

**簡化原理**：
```
1. 選擇兩個大質數 p 和 q
2. 計算 n = p × q（公開）
3 產生公鑰 (e, n) 和私鑰 (d, n)
4. 加密：C = M^e mod n
5. 解密：M = C^d mod n

安全性：
已知 n 和 e，要計算 d 需要分解 n = p × q
若 n 夠大（2048 bits），分解需時數百萬年
```

**2. ECC（Elliptic Curve Cryptography，橢圓曲線密碼學）**

- **安全基礎**：**橢圓曲線離散對數問題**（ECDLP）
- **優勢**：金鑰長度短，安全性高
  - ECC 256 bits ≈ RSA 3072 bits（安全性相當）
- **應用**：行動裝置、IoT（運算資源有限）、比特幣

**比較**：

| 項目 | RSA 2048 | ECC 256 |
|------|---------|---------|
| **金鑰長度** | 2048 bits | 256 bits |
| **加密速度** | 慢 | 較快 |
| **記憶體需求** | 高 | 低 |
| **適用場景** | 傳統伺服器 | 行動裝置、IoT |

---

#### 優缺點與挑戰

**優點**：
- ✅ **金鑰分配容易**：公鑰可公開散佈，不需安全通道
- ✅ **不需預先共享金鑰**：不像對稱式需要事先交換共用金鑰
- ✅ **支援數位簽章**：同一組金鑰也可用於身分鑑別
- ✅ **擴展性佳**：N 個人通訊只需 N 對金鑰（對稱式需 N×(N-1)/2 把）

**缺點**：
- ❌ **速度慢**：約比對稱式慢 100-1000 倍
- ❌ **不適合大量資料**：加密影片、大檔案效能差
- ❌ **需要 PKI 基礎建設**：憑證管理、CRL 維護
- ❌ **計算資源需求高**：行動裝置電池消耗

**實務解決方案：混合式加密**
```
結合兩者優點：
1. 用非對稱式加密交換「會話金鑰」（一次性對稱金鑰）
2. 用對稱式加密加密實際資料（快速）
3. 典型應用：TLS/SSL、VPN
```

---

### 二、完整性 (Integrity) 與雜湊演算法

### 1. 完整性定義

**完整性（Integrity）** 是 CIA Triad 的第二要素，定義為：

> **確保資料在儲存、處理或傳輸過程中，未遭未經授權的竄改、破壞或刪除，且可偵測任何異動。**

**重要性**：
- **資料可靠性**：確保資料正確性
- **防止竄改**：偵測惡意修改
- **審計追蹤**：記錄變更歷史
- **法律效力**：電子文件的法律證據力

**完整性的威脅範例**：
- **中間人攻擊（MITM）**：傳輸過程中資料被竄改
- **惡意軟體**：病毒修改系統檔案
- **資料庫注入**：SQL Injection 竄改資料庫
- **人為疏失**：意外刪除或修改

---

### 2. 雜湊函數（Hash Function）

**定義**：
將任意長度的輸入（訊息），透過數學函數轉換為**固定長度**的輸出（雜湊值/摘要/指紋）。

**公式表示**：
```
h = Hash(M)

其中：
M = 原始訊息（任意長度）
h = 雜湊值（固定長度，如 256 bits）
Hash() = 雜湊函數（如 SHA-256）
```

---

### 3. 雜湊函數的主要演算法

#### SHA-2 系列（Secure Hash Algorithm 2）

**SHA-256**：
- **輸出長度**：256 bits (32 bytes)
- **設計者**：NSA（美國國家安全局）
- **發布時間**：2001 年
- **安全性**：✅ **目前安全**，無實際碰撞攻擊
- **應用**：
  - 區塊鏈（Bitcoin 挖礦）
  - 數位憑證（SSL/TLS）
  - 檔案完整性驗證
  - 密碼雜湊（需加鹽）

**SHA-512**：
- **輸出長度**：512 bits
- **安全性**：更高（適用於高敏感場景）
- **速度**：在 64-bit 處理器上比 SHA-256 快

---

#### SHA-3（Keccak）

- **輸出長度**：可變（224, 256, 384, 512 bits）
- **設計**：NIST 公開競賽選出（2012）
- **特色**：演算法結構與 SHA-2 完全不同（Sponge 結構）
- **狀態**：✅ 最新標準，作為 SHA-2 的備援

---

#### MD5 與 SHA-1（已棄用）

**MD5**：
- **輸出長度**：128 bits
- **狀態**：⛔ **已破解**（2004 年發現碰撞）
- **問題**：可在數分鐘內產生碰撞
- **僅適用**：非安全性用途（如 Bittorrent 檔案校驗）

**SHA-1**：
- **輸出長度**：160 bits
- **狀態**：⛔ **即將棄用**（2017 年 Google 實際產生碰撞）
- **Chrome 處置**：2017 年起對 SHA-1 憑證顯示不安全警告
- **Git 處置**：逐步遷移至 SHA-256

---

###  4. 雜湊函數的注意事項

#### (1) 抗碰撞性（Collision Resistance）

**定義**：
> 在計算上不可行找到兩個不同的輸入 M1 和 M2，使得 Hash(M1) = Hash(M2)

**為何重要**：
```
場景：合約簽署

1. 攻擊者準備兩份合約：
   - 合約 A（正常內容）：「支付 100 元」
   - 合約 B（惡意內容）：「支付 100 萬元」

2. 若雜湊函數有碰撞漏洞：
   - 攻擊者調整兩份合約（加入空白、不可見字元）
   - 使得 Hash(合約A) = Hash(合約B)

3. 攻擊流程：
   - 給受害者簽署合約 A 的雜湊值
   - 事後宣稱受害者簽署的是合約 B
   - 因為雜湊值相同，無法證明是哪一份

4. 若使用安全的雜湊（SHA-256）：
   - 無法產生碰撞
   - 每份合約有唯一的雜湊「指紋」
```

**碰撞攻擊實例**：
- **MD5 碰撞（2008）**：研究人員製作兩個不同的執行檔，雜湊值相同
  - 一個是正常軟體
  - 一個含有惡意程式
  - 可通過 MD5 完整性檢查
- **SHA-1 碰撞（2017，Google）**：SHAttered 攻擊
  - 產生兩個不同 PDF 檔，SHA-1 雜湊值相同
  - 運算成本：約 6500 年 CPU 時間

---

#### (2) 單向性（One-way / Preimage Resistance）

**定義**：
> 給定雜湊值 h，在計算上不可行找出訊息 M，使得 Hash(M) = h

**應用：密碼儲存**
```
問題：資料庫不應儲存明文密碼

❌ 錯誤做法：
User: alice, Password: password123（明文）
→ 資料庫被駭，所有密碼外洩

✅ 正確做法：
User: alice, Hash: e38ad214943da...（雜湊值）

登入驗證：
1. 使用者輸入：password123
2. 系統計算：Hash("password123") = e38ad214943da...
3. 比對資料庫中的雜湊值
4. 若相同 → 登入成功

即使資料庫外洩：
- 駭客只取得雜湊值
- 無法反推出明文密碼（單向性）
```

**但需注意**：
- ⚠️ 彩虹表攻擊（Rainbow Table）：預先計算常見密碼的雜湊
- ✅ 解決方案：**加鹽（Salt）**
```python
# 加鹽雜湊
password = "password123"
salt = "隨機產生的字串"  # 每個使用者不同
hashed = Hash(password + salt)

儲存：alice, Hash, Salt
驗證：Hash(使用者輸入 + Salt) == Hash?
```

---

#### (3) 雪崩效應（Avalanche Effect）

**定義**：
> 輸入改變微小（如 1 bit），輸出應產生約 50% bits 的變化

**範例（SHA-256）**：
```
輸入1：Hello
SHA-256: 185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969

輸入2：hello（僅第一個字母小寫）
SHA-256: 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824

觀察：
✅ 輸入只改 1 個字元
✅ 輸出完全不同（約 50% bits 改變）
```

**用途**：
- **偵測竄改**：檔案被修改 1 byte，雜湊值會完全不同
- **防止推測**：無法從雜湊值推測原始資料的內容

---

#### (4) 演算法選擇建議

**強烈建議使用**：
- ✅ **SHA-256**（通用首選）
- ✅ **SHA-3**（新系統、高安全需求）
- ✅ **bcrypt / Argon2**（密碼專用）

**避免使用**：
- ❌ **MD5**（已破解）
- ❌ **SHA-1**（即將棄用）

**特殊場景**：
- **區塊鏈**：SHA-256（Bitcoin）、Keccak（Ethereum）
- **密碼儲存**：bcrypt、PBKDF2、Argon2（含鹽值+運算成本）
- **檔案校驗**：SHA-256（安全）、MD5（僅校驗、非安全）

---

### 5. 完整性驗證實例

**範例 1：軟體下載驗證**
```
場景：從網站下載 Linux ISO 檔

1. 官網提供：
   ubuntu-22.04.iso (3.5 GB)
   SHA-256: a435...(完整雜湊值)

2. 使用者下載後驗證：
   $ sha256sum ubuntu-22.04.iso
   a435...(計算結果)

3. 比對雜湊值：
   ✅ 相同 → 檔案完整、未被竄改
   ❌ 不同 → 檔案損壞或被竄改（不應安裝）

防護：
✅ 防止下載過程中檔案損壞
✅ 防止駭客竄改檔案（植入後門）
```

**範例 2：Git 版本控制**
```
Git 使用 SHA-1（逐步遷移至 SHA-256）雜湊：

每次 commit（提交）：
1. Git 計算所有檔案的雜湊值
2. 產生唯一的 commit ID（如 a3f5d2...）
3. 任何檔案變更，commit ID 會改變

優點：
✅ 可偵測歷史記錄被竄改
✅ 每個版本有唯一「指紋」
```

---

**評分標準** (預估)：
- 機密性與非對稱應用：12分
- 完整性與雜湊特性：13分

---

#### 💡 補充說明

**1. RSA 演算法詳細說明**

**RSA 金鑰產生步驟**（簡化版）：

```
步驟 1：選擇質數
隨機選擇兩個大質數 p 和 q
例如：p = 61, q = 53

步驟 2：計算 n
n = p × q = 61 × 53 = 3233

步驟 3：計算歐拉函數 φ(n)
φ(n) = (p-1) × (q-1) = 60 × 52 = 3120

步驟 4：選擇公鑰指數 e
選擇 e，使得 1 < e < φ(n) 且 gcd(e, φ(n)) = 1
常用：e = 65537 (2^16 + 1)
範例簡化：e = 17

步驟 5：計算私鑰指數 d
d × e ≡ 1 (mod φ(n))
d = e^(-1) mod φ(n)
範例：d = 2753

結果：
公鑰：(e, n) = (17, 3233)
私鑰：(d, n) = (2753, 3233)
```

**加密與解密範例**：
```
明文訊息：M = 123

加密（用公鑰）：
C = M^e mod n
C = 123^17 mod 3233 = 337

解密（用私鑰）：
M = C^d mod n
M = 337^2753 mod 3233 = 123  ← 還原！

數學保證：
(M^e)^d ≡ M (mod n)
```

---

**2. 雜湊函數 vs MAC vs 數位簽章**

| 比較項目 | 雜湊函數 | MAC | 數位簽章 |
|---------|---------|-----|---------|
| **需要金鑰** | ❌ 否 | ✅ 對稱金鑰 | ✅ 私鑰 |
| **驗證完整性** | ✅ |✅ | ✅ |
| **驗證身分** | ❌ | ✅（共享金鑰者） | ✅（公鑰驗證） |
| **不可否認性** | ❌ | ❌ | ✅ **是** |
| **應用** | 檔案校驗 | 訊息鑑別 | 法律文書、電子商務 |
| **範例** | SHA-256 | HMAC | RSA Signature |

**MAC (Message Authentication Code) 說明**：
```
定義：使用共享金鑰的雜湊函數

HMAC (Hash-based MAC)：
MAC = HMAC(Key, Message)

發送：
1. 發送者計算 MAC =  HMAC(SharedKey, Message)
2. 傳送 Message + MAC

驗證：
1. 接收者計算 MAC' = HMAC(SharedKey, Message)
2. 比對 MAC == MAC'?
3. 相同 → 完整性 + 來源驗證

優點：
✅ 比數位簽章快
❌ 需要預先共享金鑰
❌ 無不可否認性（雙方都可產生 MAC）
```

---

**3. 彩虹表攻擊與防禦**

**彩虹表（Rainbow Table）**：
```
原理：預先計算常見密碼的雜湊值

範例彩虹表（部分）：
password123 → e38ad214943da...
123456 → e10adc3949ba59a...
qwerty → d8578edf8458ce06...
...（數十億筆）

攻擊流程：
1. 駭客取得密碼雜湊值資料庫外洩
2. 查表找出對應的明文密碼
3. 幾秒鐘內破解（無需暴力破解）

防禦：加鹽（Salt）
```

**Salt 實作**：
```python
import hashlib
import os

# 產生隨機 Salt
salt = os.urandom(32)  # 32 bytes 隨機值

# 密碼 + Salt 後雜湊
password = "password123"
hashed = hashlib.sha256(salt + password.encode()).hexdigest()

# 儲存
database.store(username, salt, hashed)

# 驗證
input_password = user_input()
computed_hash = hashlib.sha256(salt + input_password.encode()).hexdigest()
if computed_hash == stored_hash:
    print("登入成功")

關鍵：
✅ 每個使用者使用不同的 salt
✅ Salt 足夠長（至少 16 bytes）
✅ Salt 需儲存在資料庫（明文也可）
```

---

**4. 密碼專用雜湊演算法**

**為何 SHA-256 不適合密碼儲存？**
```
問題：速度太快
- SHA-256 在現代 GPU 上，每秒可計算數十億次
- 駭客可快速暴力破解

數據：
GPU (NVIDIA RTX 4090)：
- SHA-256：~50 GH/s (每秒 500 億次)
- 8 字元純數字密碼：~1 秒破解
```

**解決方案：慢雜湊（Slow Hash）**

**bcrypt**：
```python
import bcrypt

# 設定成本因子（運算回合數）
cost_factor = 12  # 2^12 = 4096 回合

# 雜湊密碼（自動加鹽）
password = "mypassword"
hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt(cost_factor))

# 驗證
bcrypt.checkpw(input_password.encode(), hashed)  # True/False

特性：
✅ 自動加鹽
✅ 可調整成本（未來硬體變強可提高）
✅ 業界標準
```

**Argon2**（最新推薦）：
```
2015 年密碼雜湊競賽冠軍

優點：
✅ 抗 GPU 暴力破解
✅ 抗 ASIC 攻擊
✅ 可調整三種成本：
   - 時間成本（運算回合）
   - 記憶體成本（RAM 需求）
   - 平行度（CPU 核心數）

OWASP 推薦：
- Argon2id（Argon2 的混合版本）
```

---

**5. 區塊鏈中的雜湊應用**

**Bitcoin 工作量證明（Proof of Work）**：
```
挖礦（Mining）原理：

目標：找到一個 Nonce（隨機數），使得：
SHA-256(SHA-256(區塊資料 + Nonce)) < 目標值

範例：
區塊資料：交易記錄 + 前一區塊雜湊 + 時間戳
目標：雜湊值前 N 位必須是 0

嘗試：
Nonce = 1 → SHA-256(...) = 8a3f... ❌（不符合）
Nonce = 2 → SHA-256(...) = 7b2c... ❌
...
Nonce = 57942 → SHA-256(...) = 0000a3f... ✅（符合！）

特性：
✅ 找到 Nonce 很難（需大量運算）
✅ 驗證很容易（一次雜湊即可）
✅ 雪崩效應：區塊資料改變 → 需重新挖礦
```

---

**6. 實務工具與指令**

**產生檔案雜湊**：
```bash
# Linux / macOS
sha256sum file.txt
md5sum file.txt

# macOS（內建）
shasum -a 256 file.txt

# Windows (PowerShell)
Get-FileHash file.txt -Algorithm SHA256
```

**驗證下載檔案**：
```bash
# 下載後驗證
$ wget https://example.com/software.zip
$ wget https://example.com/software.zip.sha256
$ sha256sum -c software.zip.sha256
software.zip: OK  ← 驗證成功
```

**Python 雜湊運算**：
```python
import hashlib

# SHA-256
text = "Hello, World!"
hash_object = hashlib.sha256(text.encode())
hex_dig = hash_object.hexdigest()
print(hex_dig)  # 輸出：dffd6021bb2bd5b0af676290809ec3a53191dd81c7f70a4b28688a362182986f

# 檔案雜湊
def file_hash(filename):
    sha256_hash = hashlib.sha256()
    with open(filename,"rb") as f:
        for byte_block in iter(lambda: f.read(4096),b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()
```

---

**小結**：

**非對稱式密碼學**是現代網路安全的基石，透過公鑰/私鑰機制解決了對稱式加密的金鑰分配難題，廣泛應用於 HTTPS、Email 加密、數位簽章等場景。

**雜湊函數**則是確保資料完整性的核心技術，從檔案校驗到區塊鏈，從密碼儲存到數位簽章，都扮演關鍵角色。選擇安全的演算法（SHA-256、SHA-3）並正確使用（密碼加鹽、慢雜湊），是資安防護的基本功。

---

### 【題型二】SSL/TLS 資料傳輸安全

#### 📖 原題 (114年特考三級)

> **題目**：企業官網採用 HTTPS 通訊協定... 請說明在使用 SSL/TLS 通訊協定進行資料傳輸時，如何確保資料的安全性？並說明對稱和非對稱式加密演算法在此過程中的角色與功能。

#### 🎯 答題架構分析

說明 **混合式加密 (Hybrid)**：非對稱 (交換金鑰) + 對稱 (傳輸資料)。

#### 📊 評分建議 (預估配分 25 分)

**SSL/TLS 安全性確保（6 分）**
- 混合式加密概念（3 分）
  - 結合對稱與非對稱（2 分）
  - 為何需要混合（1 分）
- 安全性目標（3 分）
  - 機密性（1 分）
  - 完整性（1 分）
  - 身分驗證（1 分）

**非對稱式加密角色（9 分）**

**角色說明（3 分）**
- 身分驗證（1.5 分）
- 金鑰交換（1.5 分）

**功能詳解（6 分）**
- 憑證驗證（2 分）
  - Server 傳送憑證（1 分）
  - Client 驗證身分（1 分）
- 金鑰交換機制（4 分）
  - Client 產生對稱金鑰（1 分）
  - 用 Server 公鑰加密（2 分）
  - Server 用私鑰解密（1 分）

**對稱式加密角色（10 分）**

**角色說明（2 分）**
- 負責實際資料加密（1 分）
- 高效能傳輸（1 分）

**功能詳解（6 分）**
- 資料加密（3 分）
  - 使用協商的對稱金鑰（1 分）
  - 雙向加密通訊（2 分）
- 演算法舉例（3 分）
  - AES（2 分）
  - ChaCha20（1 分）

**混合式優勢（2 分）**
- 結合兩者優點（1 分）
  - 非對稱：安全金鑰交換
  - 對稱：快速資料傳輸
- 實務效益（1 分）

**答題提示**：
- ✅ 要說明**為何需要混合式**加密
- ✅ 清楚區分**非對稱（金鑰交換）**與**對稱（資料傳輸）**
- ✅ 舉**具體演算法**（RSA、AES）
- ✅ 說明**TLS Handshake**流程（加分）
- ⚠️ 避免只說一種加密方式


#### ✍️ 標準答案示範

**解答**：

SSL/TLS 採用 **混合式加密系統 (Hybrid Cryptosystem)**，結合了兩者的優點以確保安全性：

**1. 非對稱式加密 (Asymmetric Encryption)**
*   **角色**：負責 **身分驗證 (Authentication)** 與 **金鑰交換 (Key Exchange)**。
*   **功能**：
    *   Server 傳送數位憑證 (含公鑰) 給 Client，Client 驗證憑證確認 Server 身分。
    *   Client 利用 Server 的公鑰加密「預主金鑰 (Pre-master secret)」傳回給 Server，只有 Server 能用私鑰解密。
    *   雙方藉此安全地協商出共用的「會話金鑰 (Session Key)」。

**2. 對稱式加密 (Symmetric Encryption)**
*   **角色**：負責 **大量資料傳輸的加密 (Data Encryption)**。
*   **功能**：
    *   雙方使用協商好的 Session Key，透過 AES 等高效率演算法加密實際傳輸的網頁內容 (HTTP Payload)。
    *   **理由**：對稱式加解密速度遠快於非對稱式 (約快 1000 倍)，適合大流量傳輸。

**評分標準** (預估)：
*   非對稱式角色 (身分/金鑰)：12分
*   對稱式角色 (資料加密)：13分

---

#### � 補充說明

**1. TLS Handshake 詳細流程（TLS 1.2）**

**完整握手流程**：

```
客戶端（瀏覽器）                              伺服器（網站）

[1] Client Hello
    ├─ 支援的 TLS 版本（如 TLS 1.2）
    ├─ 支援的加密套件清單
    ├─ 隨機數 (Client Random)
    └─ 支援的壓縮方法
                        ──────────────────────────▶

                                                [2] Server Hello
                                                    ├─ 選定的 TLS 版本
                                                    ├─ 選定的加密套件
                                                    ├─ 隨機數 (Server Random)
                                                    └─ Session ID
                        ◀──────────────────────────
                                                
                                                [3] Certificate（憑證）
                                                    └─ 伺服器的數位憑證（含公鑰）
                        ◀──────────────────────────
                                                
                                                [4] Server Key Exchange（可選）
                                                    └─ Diffie-Hellman 參數（若使用 DHE/ECDHE）
                        ◀──────────────────────────
                                                
                                                [5] Server Hello Done
                        ◀──────────────────────────

[6] 憑證驗證
    ├─ 檢查憑證有效期
    ├─ 檢查憑證簽發者（CA）
    ├─ 檢查憑證撤銷狀態（OCSP/CRL）
    └─ 驗證伺服器身分

[7] Client Key Exchange
    ├─ 產生「預主金鑰」(Pre-master Secret)
    ├─ 用伺服器公鑰加密
    └─ 傳送給伺服器
                        ──────────────────────────▶

[8] 雙方推導會話金鑰
    Master Secret = PRF(Pre-master Secret, 
                        "master secret",
                        Client Random + Server Random)
    
    ├─ 客戶端加密金鑰
    ├─ 伺服器加密金鑰
    ├─ 客戶端 MAC 金鑰
    └─ 伺服器 MAC 金鑰

[9] Change Cipher Spec
    └─ 通知：後續訊息使用會話金鑰加密
                        ──────────────────────────▶

[10] Finished（加密）
     └─ 發送握手訊息的雜湊值（驗證完整性）
                        ──────────────────────────▶

                                                [11] Change Cipher Spec
                        ◀──────────────────────────
                                                
                                                [12] Finished（加密）
                        ◀──────────────────────────

[13] ✅ 握手完成，開始加密通訊
     └─ 後續所有 HTTP 流量使用對稱式加密（AES）
```

**時間消耗**：
- 握手過程：2 RTT（Round-Trip Time）
- 約 100-300 ms（視網路延遲）

---

**2. TLS 1.3 改進（2018 年發布）**

**主要變化**：

```
TLS 1.2 vs TLS 1.3 握手對比：

TLS 1.2:
Client Hello → Server Hello → Certificate → Key Exchange 
→ Change Cipher → Finished
總計：2 RTT

TLS 1.3（簡化）:
Client Hello（含金鑰分享）→ Server Hello + Certificate + Finished
總計：1 RTT  ← 快一倍！
```

**TLS 1.3 優勢**：

| 改進項目 | TLS 1.2 | TLS 1.3 |
|---------|---------|---------|
| **握手速度** | 2 RTT | **1 RTT**（快 50%） |
| **0-RTT 模式** | ❌ 不支援 | ✅ 重複連線可 0-RTT |
| **加密套件** | ~37 種（含不安全） | **僅 5 種**（全部安全） |
| **移除弱加密** | 支援 RC4, 3DES | ⛔ 全部移除 |
| **完美前向保密** | 可選 | ✅ **強制** (PFS) |
| **加密範圍** | 部分明文 | **全程加密**（連 Certificate 也加密） |

**TLS 1.3 強制要求**：
- ✅ 僅支援 AEAD 加密（AES-GCM, ChaCha20-Poly1305）
- ✅ 強制完美前向保密（Ephemeral Diffie-Hellman）
- ✅ 移除 RSA 金鑰交換（易受攻擊）

---

**3. 加密套件（Cipher Suite）選擇**

**加密套件格式**：
```
TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
  │    │     │      │    │   │    │
  │    │     │      │    │   │    └─ 雜湊演算法（SHA-384）
  │    │     │      │    │   └────── 加密模式（GCM）
  │    │     │      │    └────────── 加密長度（256 bits）
  │    │     │      └─────────────── 對稱加密（AES）
  │    │     └────────────────────── 身分認證（RSA）
  │    └──────────────────────────── 金鑰交換（ECDHE）
  └───────────────────────────────── 協定（TLS）
```

**常見加密套件安全性評級**：

**✅ 推薦（安全）**：
```
TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256
```
- ✅ 使用 ECDHE（完美前向保密）
- ✅ AES-GCM 或 ChaCha20（AEAD 加密）
- ✅ SHA-256 或更高

**⚠️ 不推薦**：
```
TLS_RSA_WITH_AES_128_CBC_SHA
```
- ❌ RSA 金鑰交換（無完美前向保密）
- ❌ CBC 模式（易受 BEAST、Lucky 13 攻擊）
- ❌ SHA-1（即將棄用）

**⛔ 禁止**：
```
TLS_RSA_WITH_RC4_128_MD5
TLS_RSA_WITH_3DES_EDE_CBC_SHA
```
- ⛔ RC4（已破解）
- ⛔ 3DES（過時）
- ⛔ MD5（已破解）

---

**4. 完美前向保密（Perfect Forward Secrecy, PFS）**

**定義**：
> 即使伺服器的私鑰在未來被洩漏，過去的通訊記錄仍無法被解密。

**運作原理**：

**不使用 PFS（RSA 金鑰交換）**：
```
問題：
1. Client 用 Server 公鑰加密「預主金鑰」
2. Server 用私鑰解密
3. 雙方推導會話金鑰

風險：
若駭客：
- 錄下所有加密流量（即使無法解密）
- 5 年後竊取伺服器私鑰
- 可解密所有歷史流量！
  └─ 預主金鑰 = Decrypt(私鑰, 加密的預主金鑰)
  └─ 會話金鑰 = PRF(預主金鑰, ...)
  └─ 明文 = Decrypt(會話金鑰, 加密流量)
```

**使用 PFS（ECDHE 金鑰交換）**：
```
每次連線產生臨時金鑰對：

連線 1：
Client 臨時私鑰 A1, 臨時公鑰 A1-pub
Server 臨時私鑰 B1, 臨時公鑰 B1-pub
→ 會話金鑰 K1 = ECDH(A1, B1-pub)
→ 連線結束後刪除 A1, B1

連線 2（新的臨時金鑰）：
Client 臨時私鑰 A2, 臨時公鑰 A2-pub
Server 臨時私鑰 B2, 臨時公鑰 B2-pub
→ 會話金鑰 K2 = ECDH(A2, B2-pub)
→ 連線結束後刪除 A2, B2

結果：
✅ 即使 Server 長期私鑰洩漏
✅ 臨時私鑰已刪除，無法重新計算會話金鑰
✅ 歷史流量無法解密
```

**實務建議**：
- ✅ 優先使用 TLS 1.3（強制 PFS）
- ✅ TLS 1.2 需選擇 ECDHE 或 DHE 套件
- ❌ 禁用 RSA 金鑰交換

---

**5. 常見 SSL/TLS 攻擊與防禦**

**攻擊 1：中間人攻擊（MITM）**

**攻擊情境**：
```
使用者 ←→ 駭客 ←→ 銀行網站
         (假冒)

1. 使用者以為連到銀行
2. 實際連到駭客的伺服器
3. 駭客轉發流量給真實銀行
4. 駭客可讀取/修改所有內容
```

**防禦：憑證驗證**
```
瀏覽器檢查：
1. 憑證是否由信任的 CA 簽發？
2. 憑證是否在有效期內？
3. 憑證的網域名稱是否匹配？
4. 憑證是否被撤銷（OCSP/CRL）？

若任一項失敗 → 顯示警告 ⚠️
```

---

**攻擊 2：SSL Stripping（降級攻擊）**

**攻擊方式**：
```
1. 使用者輸入：http://bank.com（HTTP）
2. 駭客攔截，維持 HTTP 連線
3. 駭客自己用 HTTPS 連到真實網站
4. 使用者看到 HTTP，以為正常

結果：
- 使用者與駭客間：HTTP（明文）
- 駭客與銀行間：HTTPS（加密）
- 駭客可竊取帳號密碼
```

**防禦：HSTS（HTTP Strict Transport Security）**
```
伺服器回應標頭：
Strict-Transport-Security: max-age=31536000; includeSubDomains

效果：
1. 瀏覽器記住：此網站只能用 HTTPS
2. 即使使用者輸入 http://，瀏覽器自動轉為 https://
3. 有效期 1 年

進階：HSTS Preload List
- 瀏覽器內建清單
- 初次訪問即強制 HTTPS
```

---

**攻擊 3：BEAST（Browser Exploit Against SSL/TLS）**

**影響**：TLS 1.0 使用 CBC 模式的加密套件  
**攻擊原理**：利用 CBC 模式的 IV（初始向量）可預測性  
**防禦**：
- ✅ 升級到 TLS 1.1+
- ✅ 使用 GCM 或 ChaCha20（非 CBC）

---

**攻擊 4：Heartbleed（心臟出血）**

**影響**：OpenSSL 嚴重漏洞（2014）  
**問題**：TLS Heartbeat 擴充功能的緩衝區溢位  
**後果**：
- 駭客可讀取伺服器記憶體
- 竊取私鑰、會話金鑰、使用者密碼

**修復**：
```bash
# 檢查 OpenSSL 版本
openssl version
# 若低於 1.0.1g → 立即更新

# 更新後必須：
1. 產生新的私鑰
2. 重新申請憑證
3. 撤銷舊憑證
4. 要求使用者修改密碼
```

---

**6. SSL/TLS 最佳實務**

**伺服器端設定**：

```nginx
# Nginx 範例
server {
    listen 443 ssl http2;
    server_name example.com;

    # 憑證路徑
    ssl_certificate /path/to/fullchain.pem;
    ssl_certificate_key /path/to/privkey.pem;

    # 僅支援 TLS 1.2 和 1.3
    ssl_protocols TLSv1.2 TLSv1.3;

    # 優先使用伺服器的加密套件順序
    ssl_prefer_server_ciphers on;

    # 安全的加密套件
    ssl_ciphers 'ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256';

    # 啟用 HSTS
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" always;

    # OCSP Stapling（加速憑證驗證）
    ssl_stapling on;
    ssl_stapling_verify on;

    # Session Cache（加速重複連線）
    ssl_session_cache shared:SSL:10m;
    ssl_session_timeout 10m;
}
```

---

**7. 實務工具與測試**

**檢測工具**：

**SSL Labs Server Test**：
```
網址：https://www.ssllabs.com/ssltest/

功能：
✅ 檢測憑證有效性
✅ 分析支援的協定版本
✅ 檢查加密套件安全性
✅ 檢測已知漏洞（Heartbleed、POODLE等）
✅ 給予安全評級（A+, A, B, C, F）

範例結果：
A+ → 完美設定
A  → 良好
B  → 可接受但有改進空間
C/F → 不安全，需立即修正
```

**命令列工具**：

```bash
# OpenSSL - 測試連線
openssl s_client -connect example.com:443 -tls1_3

# 查看憑證資訊
openssl s_client -connect example.com:443 < /dev/null | openssl x509 -noout -text

# 測試特定加密套件
openssl s_client -connect example.com:443 -cipher 'ECDHE-RSA-AES256-GCM-SHA384'

# nmap - 掃描支援的 TLS 版本
nmap --script ssl-enum-ciphers -p 443 example.com

# testssl.sh - 全面測試工具
./testssl.sh https://example.com
```

---

**8. Let's Encrypt 免費憑證**

**簡介**：
- 免費的 SSL/TLS 憑證頒發機構
- 自動化簽發與更新
- 支援萬用字元憑證（Wildcard）

**使用步驟（Certbot）**：

```bash
# 安裝 Certbot
sudo apt-get install certbot python3-certbot-nginx

# 自動取得憑證並設定 Nginx
sudo certbot --nginx -d example.com -d www.example.com

# 測試自動更新
sudo certbot renew --dry-run

# 設定自動更新（Cron）
0 3 * * * /usr/bin/certbot renew --quiet
```

**優點**：
- ✅ 完全免費
- ✅ 自動化申請與更新
- ✅ 受所有主流瀏覽器信任
- ✅ 推動全網 HTTPS 化

---

**9. 效能優化**

**Session Resumption（會話恢復）**：

```
問題：
每次連線都完整握手 → 2 RTT → 慢

解決方案 1：Session ID
Client 記住 Session ID
重新連線時傳送 Session ID
Server 識別後跳過握手 → 0 RTT（對稱加密部分）

解決方案 2：Session Ticket（推薦）
Server 加密會話狀態，傳給 Client
Client 保存 Ticket
重新連線時出示 Ticket
Server 解密驗證 → 恢復會話
```

**HTTP/2 與 HTTP/3**：
```
HTTP/1.1：每個資源一個 TCP 連線
HTTP/2：單一 TLS 連線，多路復用（Multiplexing）
HTTP/3：基於 QUIC，內建加密，更快握手
```

---

**10. 真實案例**

**案例 1：GitHub 棄用 TLS 1.0/1.1（2018）**
```
決策：
- 2018年2月 棄用 TLS 1.0/1.1
- 僅支援 TLS 1.2+

影響：
舊版瀏覽器無法訪問（如 IE 10、Android 4.3）

理由：
- PCI DSS 要求禁用 TLS 1.0
- BEAST 等攻擊威脅
```

**案例 2：台灣政府網站 HTTPS 化**
```
政策：
行政院資通安全處要求：
- 2020年底前，政府網站全面 HTTPS 化

實施：
✅ 內政部：https://www.moi.gov.tw
✅ 財政部：https://www.mof.gov.tw
✅ 健保署：https://www.nhi.gov.tw

檢測：
仍有部分網站使用 TLS 1.0 或弱加密套件
→ 需持續改善
```

---

**小結**：

SSL/TLS 的**混合式加密**是現代網路安全的基石：
- **非對稱式加密**解決金鑰分配與身分驗證
- **對稱式加密**提供高效的資料傳輸
- **TLS 1.3** 大幅提升速度與安全性
- **正確設定**（僅支援安全加密套件、啟用 HSTS、完美前向保密）至關重要

從瀏覽器的綠色鎖頭，到區塊鏈的加密通訊，SSL/TLS 保護著每一天數十億次的網路連線。

---


### 【題型三】PKI 公開金鑰基礎建設

#### 📖 原題 (108年特考三級)

> **題目**：公開金鑰基礎建設（Public Key Infrastructure，簡稱 PKI）涵蓋技術、管理與政策等層面，請說明其主要組成元件與功能。

#### 🎯 答題架構分析

列舉 CA, RA, CRL, Repository, Certificate 五大元件並說明功能。

#### 📊 評分建議 (預估配分 25 分)

**PKI 概述（3 分）**
- PKI 定義（2 分）
  - 公開金鑰基礎建設（1 分）
  - 涵蓋技術、管理、政策（1 分）
- PKI 目的（1 分）
  - 提供信任機制

**五大組成元件（20 分，各 4 分）**

**1. 憑證管理中心 (CA)（4 分）**
- 功能說明（3 分）
  - 簽發數位憑證（1 分）
  - 撤銷憑證（1 分）
  - 信任錨點（1 分）
- 重要性（1 分）
  - PKI 核心

**2. 註冊管理中心 (RA)（4 分）**
- 功能說明（3 分）
  - 身分驗證（2 分）
  - 審核申請（1 分）
- 與 CA 關係（1 分）
  - 前端審核角色

**3. 憑證撤銷列表 (CRL)（4 分）**
- 功能說明（3 分）
  - 列出已撤銷憑證（2 分）
  - 定期更新（1 分）
- 重要性（1 分）
  - 防止使用失效憑證

**4. 憑證儲存庫 (Repository)（4 分）**
- 功能說明（3 分）
  - 儲存憑證與 CRL（2 分）
  - 提供查詢服務（1 分）
- 存取方式（1 分）
  - LDAP、HTTP

**5. 數位憑證 (Certificate)（4 分）**
- 內容說明（3 分）
  - 包含公鑰（1 分）
  - 持有者資訊（1 分）
  - CA 簽章（1 分）
- 功能（1 分）
  - 證明公鑰歸屬

**PKI 運作流程（選答加分）（2 分）**
- 憑證申請流程（1 分）
- 憑證驗證流程（1 分）

**答題提示**：
- ✅ 五大元件都要**詳細說明**功能
- ✅ 要解釋**CA 與 RA 的分工**
- ✅ 說明**CRL 的重要性**（防止失效憑證使用）
- ✅ 可畫**PKI 架構圖**（加分）
- ⚠️ 避免只列名稱，要說明具體功能


#### ✍️ 標準答案示範

**解答**：

PKI 是一套由硬體、軟體、人員、政策與程序組成的架構，主要組成元件如下：

1.  **憑證管理中心 (Certificate Authority, CA)**：
    *   **功能**：PKI 的核心信任錨點 (Trust Anchor)。負責簽發 (Sign) 與撤銷 (Revoke) 數位憑證。CA 用自己的私鑰對使用者的公鑰簽章，證明其真實性。
2.  **註冊管理中心 (Registration Authority, RA)**：
    *   **功能**：負責前端的審核工作。驗證申請者的真實身分 (如檢查身分證)，核准後通知 CA 發證。
3.  **憑證撤銷清單 (Certificate Revocation List, CRL)**：
    *   **功能**：公布已失效或被撤銷的憑證序號清單 (如私鑰遺失或員工離職)，供使用者驗證憑證有效性。
4.  **數位憑證 (Digital Certificate)**：
    *   **功能**：網路上的身分證。包含：擁有者資訊、**公開金鑰**、有效期限、**CA 的數位簽章**。
5.  **憑證儲存庫 (Repository)**：
    *   **功能**：公開存放憑證與 CRL 的目錄服務 (如 LDAP)，供大眾查詢與下載。

**評分標準** (預估)：
*   五大元件名稱與功能正確：各 5 分，共 25 分。

---

#### 💡 補充說明

**1. PKI 完整運作流程**

**憑證申請與簽發流程**：

```
步驟 1：申請者產生金鑰對
Alice → 產生公鑰/私鑰對
      → 私鑰自己保管（絕不外傳）
      → 公鑰用於申請憑證

步驟 2：憑證簽署請求（CSR）
Alice → 建立 CSR (Certificate Signing Request)
      → CSR 包含：
         - 公鑰
         - 身分資訊（姓名、組織、Email）
         - 數位簽章（用 Alice 私鑰簽署，證明擁有對應私鑰）

步驟 3：身分驗證（RA）
Alice → 將 CSR 提交給 RA
RA → 驗證 Alice 身分：
     - 檢查實體文件（身分證、公司登記證）
     - 確認聯絡方式（Email、電話）
     - 審核申請合法性

步驟 4：核准與通知（RA → CA）
RA → 審核通過，通知 CA 簽發憑證
    → 將驗證結果與 CSR 轉交 CA

步驟 5：憑證簽發（CA）
CA → 檢視 CSR 與 RA 審核結果
   → 建立數位憑證：
      - 加入 Alice 的公鑰
      - 加入身分資訊
      - 加入有效期限
      - 加入憑證序號
   → 用 CA 的私鑰簽署憑證
   → 產生的憑證 = 網路身分證

步驟 6：憑證發放
CA → 將簽發的憑證傳給 Alice
   → 將憑證上傳到 Repository（公開目錄）

步驟 7：憑證使用
Alice → 在通訊中出示憑證
      → Bob 可用 CA 公鑰驗證憑證真偽
      → 確認 Alice 的公鑰確實屬於 Alice
```

---

**憑證驗證流程**：

```
Bob 收到 Alice 的憑證，驗證步驟：

步驟 1：檢查有效期限
→ 憑證是否在有效期內？
→ 若過期 → ❌ 拒絕

步驟 2：驗證 CA 簽章
→ 用 CA 的公鑰解密憑證簽章
→ 比對憑證內容的雜湊值
→ 若不符 → ❌ 憑證被竄改

步驟 3：檢查憑證鏈（Chain of Trust）
→ 追溯到根憑證（Root CA）
→ 確認整條憑證鏈有效

步驟 4：檢查撤銷狀態
→ 查詢 CRL 或 OCSP
→ 確認憑證未被撤銷
→ 若已撤銷 → ❌ 拒絕

步驟 5：驗證身分匹配
→ 憑證中的網域名稱是否與實際網站匹配？
→ 若不符 → ❌ 警告（可能是中間人攻擊）

✅ 全部檢查通過 → 信任此憑證
```

---

**2. 數位憑證格式：X.509**

**X.509 v3 憑證結構**（最常用）：

```
數位憑證 (X.509 v3)
├─ 版本 (Version): v3
├─ 序號 (Serial Number): 唯一識別碼
├─ 簽章演算法 (Signature Algorithm): SHA256-RSA
├─ 簽發者 (Issuer): CA 的識別資訊
│   └─ CN=GlobalSign Root CA
│   └─ O=GlobalSign
│   └─ C=BE
├─ 有效期限 (Validity)
│   ├─ Not Before: 2023-01-01 00:00:00
│   └─ Not After:  2024-01-01 23:59:59
├─ 主體 (Subject): 憑證持有者資訊
│   ├─ CN=www.example.com (Common Name)
│   ├─ O=Example Inc. (Organization)
│   ├─ OU=IT Department (Organizational Unit)
│   ├─ L=Taipei (Locality)
│   ├─ S=Taiwan (State)
│   └─ C=TW (Country)
├─ 主體公鑰資訊 (Subject Public Key Info)
│   ├─ 演算法: RSA 2048 bits
│   └─ 公鑰: [Base64 編碼的公鑰]
├─ 擴充欄位 (Extensions)  ← v3 新增
│   ├─ Key Usage: Digital Signature, Key Encipherment
│   ├─ Extended Key Usage: TLS Web Server Authentication
│   ├─ Subject Alternative Name: DNS:example.com, DNS:*.example.com
│   ├─ Authority Key Identifier: [CA 金鑰識別碼]
│   ├─ Subject Key Identifier: [此憑證金鑰識別碼]
│   ├─ CRL Distribution Points: http://crl.example.com/crl.pem
│   ├─ Authority Information Access:
│   │   ├─ OCSP: http://ocsp.example.com
│   │   └─ CA Issuers: http://cert.example.com/ca.crt
│   └─ Certificate Policies: [OID]
└─ 簽章 (Signature)
    ├─ 簽章演算法: SHA256-RSA
    └─ 簽章值: [CA 用私鑰簽署的雜湊值]
```

**查看憑證內容（OpenSSL）**：

```bash
# 查看憑證詳細資訊
openssl x509 -in certificate.crt -text -noout

# 輸出範例：
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            04:00:00:00:00:01:44:4e:f0:42:47
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: C = TW, O = TAIWAN-CA, CN = TWCA Global Root CA
        Validity
            Not Before: Jun  3 00:00:00 2023 GMT
            Not After : Jun  3 23:59:59 2024 GMT
        Subject: C = TW, O = Example Inc, CN = www.example.com.tw
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                RSA Public-Key: (2048 bit)
```

---

**3. CA 階層架構（Hierarchy）**

**三層架構**（企業常見）：

```
Root CA（根憑證管理中心）
├─ 最高信任錨點
├─ 私鑰離線保存（冷儲存，極度安全）
├─ 僅簽發中繼 CA 憑證
├─ 憑證有效期：20-30 年
└─ 範例：GlobalSign Root CA

   ↓ (簽發中繼 CA 憑證)

Intermediate CA（中繼憑證管理中心）
├─ 由 Root CA 簽發
├─ 日常簽發終端使用者憑證
├─ 私鑰可線上使用（較 Root CA 常用）
├─ 憑證有效期：5-10 年
├─ 可有多層中繼 CA
└─ 範例：GlobalSign Organization Validation CA

   ↓ (簽發終端憑證)

End-Entity Certificate（終端實體憑證）
├─ 網站 SSL 憑證
├─ Email 簽章憑證
├─ 個人身分憑證
├─ 憑證有效期：1-2 年（現多為 1 年）
└─ 範例：www.example.com 的 SSL 憑證
```

**為何需要階層架構？**

**優點**：

1. **安全性**：
   ```
   Root CA 私鑰離線保存 → 即使 Intermediate CA 被入侵
   → Root CA 仍安全 → 可撤銷 Intermediate CA
   → 重新簽發新的 Intermediate CA
   ```

2. **彈性**：
   ```
   不同用途使用不同 Intermediate CA：
   - OV CA（組織驗證）
   - EV CA（延伸驗證）
   - DV CA（網域驗證）
   ```

3. **效能**：
   ```
   分散簽發負載 → 多個 Intermediate CA 同時運作
   ```

---

**憑證鏈（Certificate Chain）**：

```
使用者信任 Root CA（瀏覽器內建）
   ↓ 驗證
Intermediate CA 憑證（由 Root CA 簽發）
   ↓ 驗證
End-Entity 憑證（由 Intermediate CA 簽發）

驗證流程：
1. 檢查 End-Entity 憑證
2. 用 Intermediate CA 公鑰驗證
3. 檢查 Intermediate CA 憑證
4. 用 Root CA 公鑰驗證
5. Root CA 在信任清單中 → ✅ 信任整條鏈
```

**完整憑證鏈範例**：

```bash
# 網站回傳的完整憑證鏈
openssl s_client -connect www.example.com:443 -showcerts

# 輸出：
---
Certificate chain
 0 s:CN = www.example.com
   i:CN = GlobalSign Organization Validation CA
 1 s:CN = GlobalSign Organization Validation CA
   i:CN = GlobalSign Root CA
 2 s:CN = GlobalSign Root CA  ← 根憑證
   i:CN = GlobalSign Root CA  ← 自簽憑證
---
```

---

**4. CRL（憑證撤銷列表）詳解**

**什麼時候需要撤銷憑證？**

```
情況 1：私鑰洩漏
→ 員工電腦被駭，私鑰外洩
→ 必須立即撤銷憑證

情況 2：員工離職
→ 員工擁有公司憑證
→ 離職後應撤銷其憑證

情況 3：資訊變更
→ 公司名稱變更
→ 網域名稱變更
→ 需撤銷舊憑證，申請新憑證

情況 4：CA 被入侵
→ CA 私鑰洩漏
→ 所有由該 CA 簽發的憑證都需撤銷

情況 5：憑證錯誤簽發
→ CA 誤簽發憑證給假冒者
→ 發現後立即撤銷
```

---

**CRL 格式與內容**：

```
Certificate Revocation List (CRL):
├─ 版本 (Version): v2
├─ 簽發者 (Issuer): CN=GlobalSign Root CA
├─ 上次更新時間 (This Update): 2024-01-15 00:00:00
├─ 下次更新時間 (Next Update): 2024-01-22 00:00:00
├─ 撤銷憑證清單 (Revoked Certificates):
│   ├─ 序號: 0x123456789ABCDEF
│   │   ├─ 撤銷時間: 2024-01-10 14:30:00
│   │   └─ 撤銷原因: Key Compromise (私鑰洩漏)
│   ├─ 序號: 0x987654321FEDCBA
│   │   ├─ 撤銷時間: 2024-01-12 09:15:00
│   │   └─ 撤銷原因: Affiliation Changed (員工離職)
│   └─ ...
└─ CRL 簽章 (Signature): [CA 簽章]
```

**撤銷原因代碼**：

| 代碼 | 原因 | 說明 |
|------|------|------|
| 0 | Unspecified | 未指定原因 |
| 1 | Key Compromise | **私鑰洩漏** |
| 2 | CA Compromise | **CA 被入侵** |
| 3 | Affiliation Changed | 組織關係變更（如員工離職） |
| 4 | Superseded | 憑證被取代（更新憑證） |
| 5 | Cessation Of Operation | 停止營運 |
| 6 | Certificate Hold | 暫時凍結（如調查中） |

---

**CRL 的問題與限制**：

**問題 1：檔案過大**
```
大型 CA 可能簽發數百萬張憑證
已撤銷憑證可能有數萬張
CRL 檔案大小：數 MB ~ 數十 MB
→ 下載耗時（尤其行動裝置）
```

**問題 2：更新延遲**
```
CRL 通常每週更新一次
若憑證週一被撤銷，CRL 週日才更新
→ 有 6 天的安全窗口期（攻擊者可利用）
```

**問題 3：隱私問題**
```
使用者需下載完整 CRL
→ CA 可追蹤使用者訪問了哪些網站
```

---

**5. OCSP（線上憑證狀態協定）**

**OCSP vs CRL**：

| 比較項目 | CRL | OCSP |
|---------|-----|------|
| **查詢方式** | 下載完整撤銷清單 | **即時查詢單一憑證** |
| **檔案大小** | 大（數 MB） | 小（幾 KB） |
| **即時性** | ❌ 延遲（每週更新） | ✅ **即時**（秒級） |
| **頻寬消耗** | 高 | 低 |
| **隱私** | ❌ 較差（需下載完整清單） | ⚠️ CA 知道使用者訪問網站 |
| **伺服器負載** | 低 | 高（需處理大量查詢） |

---

**OCSP 運作流程**：

```
步驟 1：瀏覽器收到憑證
Chrome → 收到 www.example.com 的憑證
       → 從憑證中取得 OCSP 伺服器網址
       → http://ocsp.example.com

步驟 2：建立 OCSP 請求
Chrome → 建立 OCSP Request
       → 包含：憑證序號、簽發者資訊

步驟 3：查詢 OCSP 伺服器
Chrome → POST 請求到 OCSP 伺服器
       POST http://ocsp.example.com
       Content-Type: application/ocsp-request
       [OCSP Request 內容]

步驟 4：OCSP 伺服器回應
OCSP Server → 查詢資料庫
            → 回應憑證狀態

OCSP Response:
{
  "certStatus": "good",  // 或 "revoked" 或 "unknown"
  "thisUpdate": "2024-01-15T10:30:00Z",
  "nextUpdate": "2024-01-15T10:35:00Z"
}

步驟 5：處理結果
Chrome → 解析 OCSP Response
       → 若 "good" → ✅ 繼續連線
       → 若 "revoked" → ❌ 顯示警告
       → 若查詢失敗 → ⚠️ 看瀏覽器策略
```

---

**OCSP Stapling（訂書機）**：

**問題**：
```
傳統 OCSP：
瀏覽器 → OCSP 伺服器（查詢）
→ 延遲（額外 RTT）
→ 隱私問題（CA 知道使用者訪問網站）
→ OCSP 伺服器可能當機（影響使用者連線）
```

**解決方案：OCSP Stapling**
```
伺服器定期查詢 OCSP，並將結果「釘」在 TLS 握手中：

TLS Handshake:
1. Client Hello
2. Server Hello
   ├─ Certificate
   └─ CertificateStatus（OCSP Response）← 釘上 OCSP 結果！

3. Client 驗證 OCSP Response
   → 無需額外查詢 OCSP 伺服器
   → 更快、更有隱私

優點：
✅ 加速連線（省去 OCSP 查詢）
✅ 保護隱私（無需告知 CA 訪問網站）
✅ 減輕 OCSP 伺服器負載
```

**Nginx 啟用 OCSP Stapling**：
```nginx
ssl_stapling on;
ssl_stapling_verify on;
ssl_trusted_certificate /path/to/chain.pem;
```

---

**6. 台灣 PKI 實務：自然人憑證與工商憑證**

**自然人憑證（MOICA）**：

```
簽發機構：內政部憑證管理中心（MOICA）
用途：
├─ 報稅（綜合所得稅）
├─ 健保卡網路註冊
├─ 戶政網路申請
├─ 勞保年金試算
└─ 各政府機關線上服務

技術規格：
├─ IC 卡形式（需讀卡機）
├─ 演算法：RSA 2048 bits
├─ 有效期限：5 年
└─ 憑證格式：X.509 v3

申請方式：
1. 攜帶身分證正本
2. 至戶政事務所臨櫃申請
3. 繳費：250 元（首次）、150 元（續卡）
4. 當場領取（含 PIN 碼）

使用情境：
申報綜合所得稅 →
插入自然人憑證 →
輸入 PIN 碼 →
用私鑰簽署申報資料 →
送出（具法律效力）
```

---

**工商憑證（GCA）**：

```
簽發機構：經濟部工商憑證管理中心（GCA）
用途：
├─ 公司設立登記
├─ 營業項目變更
├─ 電子發票簽章
├─ 政府電子採購
└─ B2B/B2G 交易

對象：
├─ 公司負責人
├─ 經理人
└─ 代理人

有效期限：2 年
費用：約 1000-2000 元
```

---

**台灣 CA 架構**：

```
GRCA（政府憑證總管理中心）
Government Root Certification Authority
├─ 由行政院國家資通安全會報技術服務中心管理
└─ 最高層級 Root CA

   ↓ 簽發

GCA（經濟部工商憑證管理中心）
├─ 簽發企業/組織憑證
└─ 工商憑證

MOICA（內政部憑證管理中心）
├─ 簽發個人憑證
└─ 自然人憑證

MOEACA（教育部憑證管理中心）
├─ 簽發教育機構憑證
└─ 教育人員憑證

TWCA（台灣網路認證公司）
├─ 民間 CA
└─ SSL 憑證、代碼簽章憑證
```

---

**7. 商業 CA 與憑證類型**

**憑證驗證等級**：

| 等級 | 類型 | 驗證內容 | 價格 | 綠色鎖頭 | 用途 |
|------|------|---------|------|---------|------|
| **DV** | Domain Validation | 僅驗證網域所有權 | 免費-低 | ✅ | 個人網站、部落格 |
| **OV** | Organization Validation | **驗證組織身分** | 中 | ✅ | 企業官網 |
| **EV** | Extended Validation | **嚴格驗證組織** | 高 | ✅ **綠色地址列**（舊版） | 金融、電商 |

**DV 憑證（網域驗證）**：
```
驗證方式：
- Email 驗證（發送確認信到 admin@example.com）
- DNS 驗證（新增 TXT 記錄）
- HTTP 驗證（上傳特定檔案）

簽發時間：數分鐘～數小時

範例：Let's Encrypt（免費）

憑證內容：
Subject: CN=www.example.com
→ 僅包含網域名稱，無組織資訊
```

**OV 憑證（組織驗證）**：
```
驗證方式：
- DV 驗證（網域所有權）
- 公司登記證明（商業登記）
- 電話確認（CA 致電公司）
- 鄧白氏編碼（Dun & Bradstreet）

簽發時間：3-5 個工作天

憑證內容：
Subject: CN=www.example.com
        O=Example Inc.
        L=Taipei
        C=TW
→ 包含組織名稱、地址
```

**EV 憑證（延伸驗證）**：
```
驗證方式：
- OV 全部驗證
- 律師意見書
- 法定代表人身分驗證
- 營運實體確認（實地訪查）

簽發時間：7-10 個工作天

費用：高（年費數萬元）

顯示效果（舊版瀏覽器）：
綠色地址列：[Example Inc. (TW)] https://www.example.com

新版瀏覽器：
點擊鎖頭 → 顯示完整組織資訊

用途：
銀行、電商、政府機關
```

---

**萬用字元憑證（Wildcard Certificate）**：

```
適用範圍：
CN=*.example.com

涵蓋：
✅ mail.example.com
✅ www.example.com
✅ api.example.com
❌ sub.api.example.com（次級子網域不涵蓋）
❌ example.com（根網域需另外指定）

優點：
- 單一憑證保護多個子網域
- 成本較低（vs 多張單一網域憑證）

缺點：
- 私鑰需在多台伺服器使用（安全風險）
- 若私鑰洩漏，所有子網域都受影響

價格：
約為單一網域憑證的 3-5 倍
```

---

**8. 實務工具與指令**

**產生 CSR（憑證簽署請求）**：

```bash
# 產生私鑰與 CSR
openssl req -new -newkey rsa:2048 -nodes \
  -keyout example.com.key \
  -out example.com.csr

# 互動式輸入：
Country Name (2 letter code) []:TW
State or Province Name []:Taiwan
Locality Name []:Taipei
Organization Name []:Example Inc
Organizational Unit Name []:IT Department
Common Name []:www.example.com
Email Address []:admin@example.com

# 產生檔案：
example.com.key  ← 私鑰（保密！）
example.com.csr  ← CSR（提交給 CA）
```

**查看 CSR 內容**：
```bash
openssl req -in example.com.csr -text -noout
```

**驗證憑證與私鑰匹配**：
```bash
# 計算憑證的公鑰指紋
openssl x509 -noout -modulus -in certificate.crt | openssl md5

# 計算私鑰的指紋
openssl rsa -noout -modulus -in private.key | openssl md5

# 若兩者相同 → 配對正確！
```

**檢查憑證鏈**：
```bash
# 驗證完整憑證鏈
openssl verify -CAfile ca-bundle.crt certificate.crt

# 輸出：
certificate.crt: OK  ← 驗證成功

# 若失敗：
error 20: unable to get local issuer certificate
→ 缺少中繼憑證
```

---

**9. PKI 安全事件案例**

**案例 1：DigiNotar CA 被入侵（2011）**

```
事件經過：
2011年7月 → DigiNotar（荷蘭 CA）被駭客入侵
駭客取得 CA 私鑰 → 偽造 *.google.com 憑證
用途：伊朗政府監控 Gmail 使用者（MITM 攻擊）

影響：
- 30 萬伊朗 Gmail 使用者遭監控
- DigiNotar 所有憑證被全球瀏覽器撤銷
- DigiNotar 公司宣告破產

教訓：
CA 是信任鏈的根基
一旦 CA 失守，整個 PKI 信任崩潰
```

**案例 2：Symantec 不當簽發憑證（2017）**

```
問題：
Symantec 未經驗證，簽發了 3 萬張憑證
違反 CA/Browser Forum 規範

Google 處置：
2017年 → 宣布逐步不信任 Symantec 憑證
Chrome 66（2018）→ 警告 Symantec 舊憑證
Chrome 70（2018）→ 完全不信任

結果：
Symantec 將 CA 業務賣給 DigiCert
所有 Symantec 憑證需重新簽發

教訓：
CA 必須嚴格遵守行業規範
大型瀏覽器廠商有權撤銷對 CA 的信任
```

---

**10. 未來趨勢：憑證透明度（Certificate Transparency, CT）**

**問題背景**：
```
傳統問題：
CA 可偷偷簽發憑證
受害者無法發現自己的網域被偽造憑證

範例：
駭客入侵 CA → 偽造 bank.com 憑證
銀行不知道 → 駭客用偽造憑證進行 MITM
```

**CT 解決方案**：

```
所有憑證必須記錄在「公開日誌」中

運作流程：
1. CA 簽發憑證
2. CA 將憑證提交到 CT Log（公開日誌）
3. CT Log 回傳 SCT（簽署憑證時間戳）
4. CA 將 SCT 嵌入憑證或 TLS 握手中
5. 瀏覽器驗證 SCT
   → 若無 SCT → 警告使用者

6. 網域擁有者可監控 CT Log
   → 發現異常憑證 → 立即撤銷

範例工具：
- crt.sh（搜尋 CT Log）
  https://crt.sh/?q=example.com
  → 列出所有 example.com 的憑證

- Facebook Certificate Monitor
  → 監控自家網域的憑證簽發
  → 發現異常立即警報
```

**Chrome CT 要求**：
```
2018年起：
Chrome 要求所有 EV 憑證必須包含 SCT
否則降級為 DV 顯示（失去綠色地址列）

2021年起：
所有公開信任的憑證都需 SCT
```

---

**小結**：

PKI 是網路信任的基礎架構，透過**五大元件**的協同運作：
- **CA** 簽發與撤銷憑證（信任根源）
- **RA** 驗證身分（前端把關）
- **Certificate** 證明公鑰歸屬（網路身分證）
- **CRL/OCSP** 撤銷憑證查詢（黑名單）
- **Repository** 公開儲存（憑證資料庫）

從 HTTPS 網站的綠色鎖頭，到報稅的自然人憑證，PKI 無處不在。理解其運作原理，是確保網路安全的關鍵。

---

---

### 【題型四】數位簽章原理與特性

#### 📖 原題 (105年高考三級)

> **題目**：請說明數位簽章 (Digital Signature) 之產生與驗證過程，以及其具備之安全特性。

#### 🎯 答題架構分析

1.  **定義**：數位簽章 = 訊息摘要 (Hash) + 非對稱加密 (Private Key)。
2.  **運作流程**：
    *   產生 (簽署)：Hash -> 私鑰加密。
    *   驗證：公鑰解密 -> Hash 比對。
3.  **安全特性**：完整性、鑑別性、不可否認性。

#### 📊 評分建議 (預估配分 25 分)

**數位簽章產生與驗證過程（15 分）**
- **產生過程 (Sign)（7 分）**
  1.  來源端將訊息 M 透過雜湊函數 H 產生摘要 H(M)。（3 分）
  2.  來源端使用自己的**私鑰 (Private Key)** 對 H(M) 進行加密，產生簽章 S。（4 分）
- **驗證過程 (Verify)（8 分）**
  1.  接收端收到訊息 M 與簽章 S。（2 分）
  2.  接收端使用來源端的**公鑰 (Public Key)** 解密 S，還原出摘要 H'(M)。（3 分）
  3.  接收端將收到的訊息 M 透過相同的雜湊函數 H 產生摘要 H(M)。（2 分）
  4.  比對 H'(M) 與 H(M) 是否相同。若相同，則驗證成功。（1 分）

**具備之安全特性（10 分）**
- **完整性 (Integrity)（3 分）**：雜湊值比對確保訊息未被竄改。
- **身分鑑別 (Authentication)（3 分）**：只有持有私鑰者能產生有效簽章。
- **不可否認性 (Non-repudiation)（4 分）**：私鑰由發送者獨有，無法抵賴曾發送過該訊息。

**答題提示**：
- ✅ 務必強調**私鑰簽署、公鑰驗證**（與加密傳輸相反）。
- ✅ 流程圖解會更加分。
- ✅ 提到**雜湊函數**在其中的角色（縮短運算長度、確保完整性）。

#### ✍️ 標準答案示範

**解答**：

**一、數位簽章產生與驗證過程**

數位簽章結合了**公開金鑰密碼學**與**雜湊函數**，運作流程如下：

**1. 簽章產生過程 (Signing)**
由發送者 (Sender) 執行：
1.  **計算摘要**：將原始訊息 $M$ 輸入雜湊函數 (如 SHA-256)，產生訊息摘要 $H(M)$。
2.  **私鑰加密**：使用發送者自己的**私鑰 ($K_{priv}$)** 對摘要 $H(M)$ 進行加密，產生的結果即為數位簽章 $S$。
    > 公式：$S = E(K_{priv}, H(M))$
3.  **傳送**：將原始訊息 $M$ 與數位簽章 $S$ 一併傳送給接收者。

**2. 簽章驗證過程 (Verifying)**
由接收者 (Receiver) 執行：
1.  **公鑰解密**：使用發送者的**公開金鑰 ($K_{pub}$)** 對簽章 $S$ 進行解密，還原出發送者計算的摘要 $H'(M)$。
    > 公式：$H'(M) = D(K_{pub}, S)$
2.  **計算摘要**：將收到的原始訊息 $M$ 輸入相同的雜湊函數，計算出新的摘要 $H(M)$。
3.  **比對**：比較 $H'(M)$ 與 $H(M)$。
    *   若兩者**相同**：證明訊息未被竄改且確由發送者簽署 (驗證成功)。
    *   若兩者**不同**：簽章無效 (驗證失敗)。

**二、數位簽章具備之安全特性**

1.  **完整性 (Integrity)**：
    由於雜湊函數具有抗碰撞性與雪崩效應，若訊息 $M$ 在傳輸過程中被竄改 (即使只改 1 bit)，接收端計算出的 $H(M)$ 將與解密後的 $H'(M)$ 不符，從而發現竄改。

2.  **身分鑑別 (Authentication)**：
    數位簽章必須使用發送者的**私鑰**產生。由於私鑰只有發送者擁有，若能用其公鑰成功解密並驗證，即證明該訊息確實源自該發送者。

3.  **不可否認性 (Non-repudiation)**：
    因為私鑰由發送者獨有且應妥善保管，發送者事後無法否認曾簽署並發送該訊息。此特性在法律與電子商務上極為重要。

---

#### 💡 補充說明

**1. 數位簽章詳細運作流程圖**

**完整流程視覺化**：

```
發送者端 (Alice)                                接收者端 (Bob)
─────────────────────                           ─────────────────

[1] 撰寫訊息
    M = "轉帳 100 萬給 Bob"

[2] 計算雜湊
    H(M) = SHA-256(M)
    結果：a3f5d2c1...（256 bits）

[3] 用私鑰簽署
    S = RSA-Sign(Alice_PrivateKey, H(M))
    數位簽章 S = b7e4f3a2...

[4] 傳送訊息與簽章
    傳送：M + S
                    ──────────────────────────▶
                                                [5] 收到訊息與簽章
                                                    M + S

                                                [6] 驗證簽章
                                                    H'(M) = RSA-Verify(Alice_PublicKey, S)
                                                    還原雜湊：a3f5d2c1...

                                                [7] 重新計算雜湊
                                                    H(M) = SHA-256(M)
                                                    計算結果：a3f5d2c1...

                                                [8] 比對雜湊值
                                                    H'(M) == H(M) ?
                                                    a3f5d2c1... == a3f5d2c1... ✅

                                                [9] 驗證成功
                                                    ✅ 訊息完整（未被竄改）
                                                    ✅ 確實來自 Alice
                                                    ✅ Alice 無法否認
```

---

**攻擊情境與防護**：

```
情境 1：中間人竄改訊息

原始訊息：M = "轉帳 100 萬"
簽章：S (用 Alice 私鑰簽署)

駭客攔截並竄改：
M' = "轉帳 1000 萬"  ← 竄改金額
簽章：S（維持不變）

Bob 驗證：
H'(M') = RSA-Verify(Alice_PublicKey, S)
→ 還原出原始雜湊值（對應原始訊息 M）

H(M') = SHA-256("轉帳 1000 萬")
→ 計算竄改後的雜湊值

H'(M') ≠ H(M')  ❌ 不相符
→ 驗證失敗，Bob 發現訊息被竄改
→ 拒絕交易

安全保證：
✅ 任何訊息變動都會導致雜湊值改變
✅ 簽章只對原始訊息有效
✅ 駭客無法重新簽署（沒有 Alice 私鑰）
```

---

**2. 數位簽章 vs 雜湊 vs MAC vs 加密**

**詳細對比表**：

| 技術 | 數位簽章 | 雜湊函數 | MAC | 對稱式加密 |
|------|---------|---------|-----|-----------|
| **需要金鑰** | ✅ 私鑰（簽署）<br>公鑰（驗證） | ❌ 不需要 | ✅ 共享金鑰 | ✅ 共享金鑰 |
| **確保完整性** | ✅ | ✅ | ✅ | ❌ |
| **確保機密性** | ❌ | ❌ | ❌ | ✅ |
| **身分鑑別** | ✅ **是**<br>（私鑰獨有） | ❌ | ⚠️ 部分<br>（僅限金鑰持有者） | ⚠️ 部分 |
| **不可否認性** | ✅ **是**<br>（法律效力） | ❌ | ❌ | ❌ |
| **可公開驗證** | ✅ **是**<br>（任何人可用公鑰驗證） | N/A | ❌<br>（需要金鑰） | ❌ |
| **運算速度** | ❌ 慢<br>（RSA 簽署） | ✅ 快 | ✅ 快 | ✅ 快 |
| **適用場景** | 合約、法律文件、軟體發布 | 檔案校驗、密碼儲存 | API 驗證、訊息驗證 | 資料傳輸 |
| **典型演算法** | RSA、DSA、ECDSA | SHA-256、SHA-3 | HMAC-SHA256 | AES |

**為何雜湊函數不夠？需要數位簽章**

```
情境：軟體下載

方案 1：僅提供雜湊值（不安全）
1. 官網提供：
   software.exe
   SHA-256: a3f5d2c1...

2. 問題：駭客可以：
   - 竄改 software.exe（植入後門）
   - 同時竄改網頁上的雜湊值
   - 使用者下載後驗證雜湊：✅ 通過（但已是惡意版本）

方案 2：使用數位簽章（安全）
1. 官網提供：
   software.exe
   software.exe.sig（數位簽章，用廠商私鑰簽署）

2. 駭客即使竄改：
   - 竄改 software.exe
   - 但無法產生有效的新簽章（沒有廠商私鑰）
   - 使用者驗證簽章：❌ 失敗
   - 系統警告：「此檔案可能已被竄改」

結論：
雜湊值可被攻擊者一併竄改
數位簽章需要私鑰才能產生，提供更強的保證
```

---

**MAC vs 數位簽章**：

```
MAC (Message Authentication Code)：

產生：
MAC = HMAC(SharedKey, Message)

驗證：
MAC' = HMAC(SharedKey, Message)
MAC == MAC' → 驗證成功

特性：
✅ 確保完整性
✅ 身分驗證（但雙方都可產生 MAC）
❌ 無不可否認性（發送者可抵賴）
❌ 無法向第三方證明

應用：
- API 請求驗證（AWS Signature）
- Cookie 完整性（HMAC-signed cookies）
- VPN/TLS 內部使用

數位簽章：

產生：
Signature = Sign(PrivateKey, Hash(Message))

驗證：
Hash' = Verify(PublicKey, Signature)
Hash' == Hash(Message) → 驗證成功

特性：
✅ 確保完整性
✅ 身分驗證（私鑰獨有）
✅ 不可否認性（具法律效力）
✅ 可向任何人證明

應用：
- 合約簽署
- 軟體發布
- 區塊鏈交易
- 電子郵件簽章
```

---

**3. 常見數位簽章演算法**

**RSA 簽章**：

```
金鑰產生：
與 RSA 加密相同
- 公鑰 (e, n)
- 私鑰 (d, n)

簽署：
S = M^d mod n（其中 M 為雜湊值）

驗證：
M = S^e mod n

特性：
✅ 廣泛支援
✅ 與加密使用相同基礎
❌ 金鑰長度大（2048-4096 bits）
❌ 速度較慢

安全建議：
- 最小金鑰長度：2048 bits
- 推薦：3072 bits
- 雜湊：SHA-256 或更高
- 填充：PSS（Probabilistic Signature Scheme）

範例工具：
OpenSSL, GPG, Windows CryptoAPI
```

---

**DSA (Digital Signature Algorithm)**：

```
特性：
- NIST 標準（FIPS 186）
- 僅用於簽章（無加密）
- 金鑰長度：1024-3072 bits

簽署過程：
1. 選擇隨機數 k
2. 計算 r = (g^k mod p) mod q
3. 計算 s = k^(-1) (H(m) + xr) mod q
4. 簽章 = (r, s)

安全性問題：
⚠️ k 必須真正隨機且不可重複使用
⚠️ 若 k 重複或可預測 → 私鑰可被計算出來

著名漏洞：
2010年 Sony PlayStation 3
- 使用固定的 k 值簽署
- 研究人員破解出私鑰
- 可自行簽署任意程式碼

現況：
⚠️ 較少使用，逐漸被 ECDSA 取代
```

---

**ECDSA (Elliptic Curve Digital Signature Algorithm)**：

```
特性：
✅ 橢圓曲線版本的 DSA
✅ 金鑰短但安全性相當
   - ECDSA 256 bits ≈ RSA 3072 bits (安全性)
✅ 速度快
✅ 適合行動裝置、IoT

常見曲線：
- P-256 (secp256r1) - NIST 標準
- P-384 (secp384r1)
- secp256k1 - Bitcoin 使用

簽章大小：
RSA-2048 簽章：256 bytes
ECDSA-256 簽章：64 bytes  ← 小 4 倍！

應用：
✅ Bitcoin / Ethereum (secp256k1)
✅ TLS 1.3
✅ Apple iOS 程式碼簽章
✅ 行動支付
```

**演算法比較表**：

| 項目 | RSA | DSA | ECDSA | EdDSA |
|------|-----|-----|-------|-------|
| **金鑰長度** | 2048-4096 bits | 2048-3072 bits | 256-384 bits | 256 bits |
| **簽章大小** | 256-512 bytes | ~320 bytes | 64 bytes | 64 bytes |
| **簽署速度** | 慢 | 中 | 快 | **最快** |
| **驗證速度** | 快 | 中 | 中 | 快 |
| **隨機數** | 不需要 | ⚠️ 需要（安全風險） | ⚠️ 需要 | ✅ 確定性（無風險） |
| **標準化** | ✅ 廣泛 | ✅ NIST | ✅ NIST | ⚠️ 較新 |
| **適用場景** | 通用 | 政府機關 | 行動裝置、區塊鏈 | 現代應用 |

**EdDSA (Edwards-curve Digital Signature Algorithm)**：

```
最新一代簽章演算法（2011）

優勢：
✅ 確定性（無需隨機數 k）
✅ 防止 k 重複使用漏洞
✅ 速度極快
✅ 抗旁道攻擊

常見變體：
- Ed25519（256 bits）← 最流行
- Ed448（448 bits）

應用：
✅ SSH (OpenSSH 6.5+)
✅ Signal 加密通訊
✅ Tor 網路
✅ 新一代區塊鏈（Solana、Cardano）

範例（Ed25519 簽章）：
公鑰：32 bytes
私鑰：32 bytes
簽章：64 bytes
速度：比 RSA-2048 快 10-30 倍
```

---

**4. 實務應用案例**

**應用 1：PDF 文件簽章**

```
場景：律師事務所簽署合約 PDF

步驟 1：準備憑證
律師 → 申請數位憑證（含私鑰）
CA → 簽發憑證（證明律師身分）

步驟 2：簽署 PDF
使用 Adobe Acrobat：
1. 開啟合約 PDF
2. 選擇「簽署」→「使用憑證」
3. 選擇律師憑證
4. 輸入 PIN 碼（保護私鑰）
5. 簽署完成

技術原理：
1. 計算 PDF 內容的雜湊值
2. 用律師私鑰簽署雜湊值
3. 將簽章嵌入 PDF（不改變內容）
4. 附加律師憑證（供驗證用）

步驟 3：驗證簽章
客戶開啟 PDF：
1. Adobe 自動驗證簽章
2. 檢查憑證是否由信任的 CA 簽發
3. 檢查憑證是否過期或撤銷
4. 驗證 PDF 內容未被修改

顯示結果：
✅「已簽署且所有簽章都有效」
   簽署者：林大律師
   簽署時間：2024-01-15 10:30
   憑證發行者：TWCA

若 PDF 被竄改：
❌「文件已被修改，至少一個簽章無效」

法律效力：
在台灣，符合《電子簽章法》
與實體簽章具同等效力
```

---

**應用 2：軟體程式碼簽章（Code Signing）**

```
場景：軟體公司發布 Windows 應用程式

為何需要？
問題：
- 使用者下載 EXE 檔
- Windows SmartScreen：「無法識別的應用程式」
- 使用者疑慮：這是病毒嗎？

解決：程式碼簽章

步驟 1：取得程式碼簽章憑證
公司 → 向 CA 申請（如 DigiCert、GlobalSign）
驗證：
- 公司合法性（商業登記）
- 鄧白氏編碼
- 電話確認
費用：年費約 $200-500 USD

步驟 2：簽署應用程式
使用 SignTool (Windows SDK)：

# 簽署單一檔案
signtool sign /f MyCert.pfx /p MyPassword /t http://timestamp.digicert.com MyApp.exe

# 查看簽章
signtool verify /pa /v MyApp.exe

步驟 3：使用者下載執行
Windows 檢查：
1. 驗證數位簽章
2. 檢查憑證是否信任
3. 檢查憑證是否撤銷
4. 驗證檔案完整性

結果：
✅ 簽章有效：
   - SmartScreen 通過
   - 顯示發行者資訊
   - 「此應用程式來自已驗證的發行者」

❌ 簽章無效或被竄改：
   - 嚴重警告
   - 建議不要執行

時間戳的重要性：
問題：憑證過期後，舊版軟體無法驗證？

解決：時間戳服務
/t http://timestamp.digicert.com

作用：
- CA 時間戳伺服器簽署「簽署時間」
- 證明：檔案在憑證有效期內簽署
- 結果：憑證過期後，簽章仍然有效

實例：
Microsoft Office 2010（2010 年簽署）
簽章憑證已過期（2015）
但因有時間戳 → Windows 仍信任
```

---

**應用 3：Email 數位簽章（S/MIME）**

```
協定：S/MIME (Secure/Multipurpose Internet Mail Extensions)

設定步驟：

1. 取得 Email 憑證
   - 向 CA 申請（如 Comodo、GlobalSign）
   - 免費選項：Actalis（個人用）
   - 憑證綁定 Email 地址

2. 安裝憑證
   - 憑證匯入 Outlook / Thunderbird
   - 私鑰儲存在本機或智慧卡

3. 傳送簽章 Email
   Outlook：
   - 撰寫郵件
   - 選項 → 簽署訊息
   - 傳送

4. 收件者驗證
   - 看到「已簽署」標記
   - 點擊可查看憑證詳情
   - 驗證簽署者身分

效果：
✅ 確認發件者身分（防網路釣魚）
✅ 確保 Email 內容未被竄改
✅ 不可否認性（法律證據）

限制：
❌ 需要雙方都支援 S/MIME
❌ 設定較複雜（一般使用者門檻高）

替代方案：PGP/GPG
- 去中心化（無需 CA）
- 開源、免費
- 技術門檻較高
```

---

**應用 4：區塊鏈交易簽章**

```
以 Bitcoin 為例：

交易簽章流程：

1. Alice 想轉帳 1 BTC 給 Bob

2. 建立交易 Tx：
   {
     "from": "Alice 的地址（公鑰雜湊）",
     "to": "Bob 的地址",
     "amount": 1 BTC,
     "input": "前一筆交易的輸出",
     "timestamp": "2024-01-15 10:30"
   }

3. 簽署交易：
   H = SHA-256(Tx)  // 計算交易雜湊
   S = ECDSA-Sign(Alice_PrivateKey, H)  // 用私鑰簽署

4. 廣播交易：
   Transaction = Tx + S + Alice_PublicKey
   → 廣播到 Bitcoin 網路

5. 礦工驗證：
   H' = ECDSA-Verify(Alice_PublicKey, S)
   H == H' ?  ✅ 簽章有效
   
   檢查：
   - Alice 的公鑰是否對應「from」地址
   - Alice 是否有足夠餘額
   - 交易是否重複（雙花檢測）

6. 打包進區塊：
   驗證成功 → 交易被打包進區塊鏈
   → 永久記錄，不可竄改

關鍵特性：
✅ 無需第三方（去中心化）
✅ 私鑰 = 資產控制權
✅ 交易公開可驗證
✅ 不可偽造、不可否認

安全性：
私鑰遺失 = 永久失去資產
私鑰外洩 = 資產被盜（無法追回）
→ 私鑰管理至關重要
```

---

**5. 台灣電子簽章法律規範**

**《電子簽章法》（2001年施行）**

```
核心定義：

第 2 條：
電子簽章：指依附於電子文件並與其相關連，
用以辨識及確認電子文件簽署人身分、資格
及電子文件真偽者。

第 4 條（安全電子簽章）：
符合下列條件者為安全電子簽章，推定為真正：
1. 簽章製作資料（私鑰），僅由簽署人專有控制
2. 簽章後之改變，能夠被發現
3. 簽署人身分，得以辨識

第 5 條（法律效力）：
依本法之電子簽章，其效力與簽名或蓋章同。
```

**憑證機構管理**：

```
主管機關：經濟部

認可的憑證機構：
1. 政府憑證總管理中心（GRCA）
   - 內政部憑證管理中心（MOICA）→ 自然人憑證
   - 經濟部工商憑證管理中心（GCA）→ 工商憑證

2. 民間憑證機構
   - 台灣網路認證公司（TWCA）
   - 中華電信
   - 政府電子採購網

責任與義務：
- CA 必須維持適當的財力及專業能力
- 提供 24 小時撤銷服務
- 保存簽發記錄至少 5 年
- 定期接受主管機關稽核
```

**實務應用**：

```
政府機關：
✅ 綜合所得稅網路申報（自然人憑證）
✅ 公司登記變更（工商憑證）
✅ 政府電子採購（廠商憑證）
✅ 健保卡註冊（自然人憑證）

司法案例：
最高法院 101 年台上字第 984 號判決：
「電子郵件附加數位簽章，
 若符合電子簽章法第 4 條規定，
 推定為真正，與親簽同」

注意事項：
1. 私鑰外洩應立即撤銷憑證
2. 憑證到期前應及時更新
3. 重要交易建議保留簽章紀錄
```

---

**6. 實務工具與操作**

**OpenSSL 數位簽章**：

```bash
# 1. 產生私鑰
openssl genpkey -algorithm RSA -out private_key.pem -pkeyopt rsa_keygen_bits:2048

# 2. 匯出公鑰
openssl rsa -pubout -in private_key.pem -out public_key.pem

# 3. 準備要簽署的檔案
echo "重要合約內容" > document.txt

# 4. 簽署檔案
openssl dgst -sha256 -sign private_key.pem -out document.sig document.txt

# 5. 驗證簽章
openssl dgst -sha256 -verify public_key.pem -signature document.sig document.txt

# 輸出：
Verified OK  ← 驗證成功

# 若檔案被竄改：
echo "竄改的內容" > document.txt
openssl dgst -sha256 -verify public_key.pem -signature document.sig document.txt

# 輸出：
Verification Failure  ← 驗證失敗
```

**GPG (GNU Privacy Guard) 數位簽章**：

```bash
# 1. 產生金鑰對
gpg --gen-key

# 互動式輸入：
# - 姓名
# - Email
# - 金鑰密碼

# 2. 列出金鑰
gpg --list-keys

# 3. 簽署檔案
gpg --sign document.txt
# 產生 document.txt.gpg（包含簽章）

# 或產生分離式簽章：
gpg --detach-sign document.txt
# 產生 document.txt.sig

# 4. 驗證簽章
gpg --verify document.txt.sig document.txt

# 5. 匯出公鑰（給他人驗證用）
gpg --export --armor alice@example.com > alice_pubkey.asc

# 6. 匯入他人公鑰
gpg --import bob_pubkey.asc

# 7. 簽署並加密 Email（Thunderbird + Enigmail）
# 自動整合 GPG
```

**Python 範例（使用 cryptography 庫）**：

```python
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend

# 1. 產生金鑰對
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
public_key = private_key.public_key()

# 2. 準備訊息
message = b"Important contract: Transfer 1M to Bob"

# 3. 簽署
signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

print(f"簽章長度：{len(signature)} bytes")  # 256 bytes for RSA-2048

# 4. 驗證
try:
    public_key.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("✅ 簽章驗證成功")
except:
    print("❌ 簽章驗證失敗")
```

---

**7. 數位簽章安全最佳實務**

**私鑰保護**：

```
威脅：私鑰洩漏 = 身分被偽造

防護措施：

1. 使用硬體安全模組（HSM）
   - USB Token（如 YubiKey）
   - 智慧卡
   - 企業級 HSM（如 Thales）
   優點：私鑰永不離開硬體

2. 密碼保護
   - 私鑰檔案加密
   - 使用強密碼（16+ 字元）
   - 啟用 2FA

3. 定期輪換
   - 企業：每 1-2 年更換金鑰
   - 個人：每 3-5 年
   - 舊金鑰安全銷毀

4. 存取控制
   - 最小權限原則
   - 稽核日誌
   - 多人授權（重要金鑰）

5. 備份與災難復原
   - 離線備份私鑰
   - 安全儲存位置（保險箱）
   - 測試還原程序
```

**簽章驗證注意事項**：

```
完整驗證檢查清單：

✅ 1. 簽章本身有效
   - 數學驗證通過
   - 雜湊值匹配

✅ 2. 憑證有效性
   - 在有效期內
   - 未被撤銷（檢查 CRL/OCSP）
   - 憑證鏈完整

✅ 3. 簽署者身分
   - 憑證主體是否正確
   - CN（Common Name）是否匹配預期

✅ 4. 使用目的
   - Key Usage 包含 "Digital Signature"
   - Extended Key Usage 符合用途

✅ 5. 時間戳
   - 簽署時間是否合理
   - 時間戳是否可信

常見陷阱：
❌ 只驗證簽章，不檢查憑證
❌ 忽略憑證撤銷狀態
❌ 信任自簽憑證（無 CA 驗證）
❌ 未檢查憑證用途限制
```

---

**8. 真實案例與啟示**

**案例 1：Stuxnet 蠕蟲（2010）**

```
事件：
史上最複雜的網路武器
目標：伊朗核設施

簽章偽造：
- Stuxnet 使用偷來的數位憑證簽署
- 憑證來自：
  1. Realtek Semiconductor（台灣 Realtek 公司）
  2. JMicron Technology（台灣 JMicron 公司）

攻擊者：
- 入侵台灣兩家公司
- 竊取程式碼簽章憑證私鑰
- 用於簽署惡意驅動程式

結果：
- Windows 信任這些簽章
- 惡意驅動成功載入
- 繞過安全檢查

教訓：
1. 程式碼簽章憑證是高價值目標
2. 必須強化私鑰保護（使用 HSM）
3. 憑證被盜應立即撤銷
4. 建議使用 EV 程式碼簽章（需 HSM）

後續：
- Realtek 和 JMicron 的憑證被撤銷
- 兩家公司重新審視安全政策
- 業界提升程式碼簽章安全標準
```

---

**案例 2：Adobe Flash Player 惡意簽章（2012）**

```
事件：
駭客組織竊取 Adobe 程式碼簽章憑證

經過：
2012 年 Adobe 被入侵
盜取：
- Flash Player 程式碼簽章私鑰
- 可簽署任意程式為「Adobe Systems」

攻擊：
- 簽署惡意軟體
- 利用使用者信任 Adobe
- 透過釣魚網站散播

Adobe 應對：
1. 立即撤銷被盜憑證
2. 重新簽發新憑證
3. 更新所有 Flash Player
4. 建議使用者檢查軟體來源

微軟配合：
- Windows Update 推送憑證撤銷
- SmartScreen 封鎖已知惡意檔案

教訓：
- 即使大公司也可能被入侵
- 憑證撤銷機制的重要性
- 使用者應檢查憑證有效性
- 不要僅依賴「已簽署」就信任
```

---

**小結**：

數位簽章是**網路世界的親筆簽名**，結合了：
- **雜湊函數**確保完整性
- **非對稱式加密**確保身分鑑別與不可否認性

從法律合約、軟體發布、Email 通訊到區塊鏈交易，數位簽章無處不在。正確使用數位簽章，並妥善保護私鑰，是數位時代不可或缺的安全技能。

---

## 🗂️ 歷屆精選題庫 (Selected Question Bank)

以下精選了歷年 (104-114) 具代表性的密碼學考題，供您延伸練習：

### 📌 加密演算法類 (Encryption Algorithms)

1. **109年高考三級** ⭐⭐⭐  
   **題目**：請比較對稱式加密與非對稱式加密之優缺點及適用時機。  
   **難度**：中  
   **考點**：對稱式 vs 非對稱式基本觀念  
   **提示**：從速度、金鑰管理、應用場景三個角度比較

2. **106年特考三級** ⭐⭐  
   **題目**：請說明 AES (Advanced Encryption Standard) 之主要特色 (區塊長度、金鑰長度)。  
   **難度**：易  
   **考點**：AES 規格  
   **答案重點**：區塊 128 bits、金鑰 128/192/256 bits、取代 DES

3. **112年高考三級** ⭐⭐⭐⭐  
   **題目**：請說明混合式加密 (Hybrid Encryption) 之運作原理，並舉例說明其在網路通訊之應用。  
   **難度**：中高  
   **考點**：混合式加密、SSL/TLS  
   **提示**：非對稱加密用於金鑰交換，對稱加密用於資料傳輸

4. **108年普考** ⭐⭐  
   **題目**：RSA 與 ECC (橢圓曲線密碼學) 相比，各有何優缺點？  
   **難度**：中  
   **考點**：非對稱式演算法比較  
   **答案重點**：金鑰長度、運算速度、應用場景

---

### 📌 數位簽章與 PKI 類

5. **113年四等** ⭐⭐⭐⭐⭐  
   **題目**：為何非對稱式密鑰須使用公鑰憑證 (Public Key Certificate)？  
   **難度**：高  
   **考點**：中間人攻擊、PKI 信任鏈  
   **答案重點**：防止公鑰被偽造、CA 信任機制、憑證驗證流程

6. **105年高考三級** ⭐⭐⭐⭐  
   **題目**：請說明數位簽章 (Digital Signature) 之產生與驗證過程，以及其具備之安全特性。  
   **難度**：中高  
   **考點**：數位簽章核心概念  
   **提示**：私鑰簽署、公鑰驗證；完整性、鑑別性、不可否認性

7. **104年特考三級** ⭐⭐⭐⭐⭐  
   **題目**：請說明雙重簽章 (Dual Signature) 在電子商務 (SET 協定) 之應用。  
   **難度**：高  
   **考點**：進階數位簽章應用  
   **答案重點**：分別對訂單資訊和付款資訊簽署、保護隱私

8. **108年特考三級** ⭐⭐⭐  
   **題目**：請說明 PKI 中憑證撤銷列表 (CRL) 與線上憑證狀態協定 (OCSP) 之差異。  
   **難度**：中  
   **考點**：憑證撤銷機制  
   **提示**：CRL 定期更新清單、OCSP 即時查詢

9. **111年高考三級** ⭐⭐⭐⭐  
   **題目**：請說明數位憑證 (Digital Certificate) 應包含哪些欄位資訊？並說明 CA (憑證管理中心) 之角色。  
   **難度**：中高  
   **考點**：X.509 憑證結構、CA 功能  
   **答案重點**：主體、公鑰、有效期、CA 簽章；CA 是信任錨點

---

### 📌 雜湊函數類

10. **110年普考** ⭐⭐⭐  
    **題目**：請說明雜湊函數 (Hash Function) 之特性及其在資安上之應用 (如密碼儲存)。  
    **難度**：中  
    **考點**：雜湊函數基本特性  
    **答案重點**：單向性、抗碰撞性、雪崩效應；應用於密碼儲存、完整性檢查

11. **107年高考三級** ⭐⭐⭐⭐  
    **題目**：請說明訊息鑑別碼 (MAC) 與數位簽章之差異。  
    **難度**：中高  
    **考點**：MAC vs 數位簽章  
    **提示**：MAC 使用對稱金鑰、無不可否認性；數位簽章使用非對稱金鑰、具法律效力

12. **109年特考三級** ⭐⭐⭐  
    **題目**：為何 MD5 和 SHA-1 雜湊函數不再被建議使用？應改用何種演算法？  
    **難度**：中  
    **考點**：雜湊函數安全性演進  
    **答案重點**：碰撞攻擊成功案例、改用 SHA-256 或 SHA-3

---

### 📌 SSL/TLS 與網路安全類

13. **112年特考三級** ⭐⭐⭐⭐⭐  
    **題目**：請說明 TLS 1.3 相較於 TLS 1.2 有哪些改進？  
    **難度**：高  
    **考點**：TLS 版本差異  
    **答案重點**：握手次數減少、強制 PFS、移除舊加密套件、加密範圍擴大

14. **110年高考三級** ⭐⭐⭐⭐  
    **題目**：請說明完美前向保密 (Perfect Forward Secrecy, PFS) 之原理及其重要性。  
    **難度**：中高  
    **考點**：PFS 機制  
    **提示**：使用臨時金鑰、私鑰洩漏不影響過去通訊

15. **106年普考** ⭐⭐⭐  
    **題目**：SSL/TLS 如何結合對稱式與非對稱式加密？請說明其運作流程。  
    **難度**：中  
    **考點**：混合式加密應用  
    **答案重點**：Handshake 使用非對稱、資料傳輸使用對稱

---

### 📌 進階應用與整合題

16. **113年高考三級** ⭐⭐⭐⭐⭐  
    **題目**：請說明區塊鏈技術如何運用密碼學技術 (雜湊函數、數位簽章) 確保資料安全與不可竄改性。  
    **難度**：高  
    **考點**：區塊鏈與密碼學  
    **答案重點**：區塊雜湊鏈接、交易數位簽章、工作量證明

17. **111年特考三級** ⭐⭐⭐⭐  
    **題目**：請說明零知識證明 (Zero-Knowledge Proof) 之概念及其在密碼學之應用。  
    **難度**：高  
    **考點**：進階密碼學概念  
    **提示**：證明知道某秘密但不洩露秘密本身

18. **107年特考三級** ⭐⭐⭐  
    **題目**：請說明同態加密 (Homomorphic Encryption) 之特性及應用場景。  
    **難度**：中高  
    **考點**：進階加密技術  
    **答案重點**：在加密狀態下進行運算、雲端隱私運算

---

## 💡 答題技巧總結

### 🎯 一、答題通用策略

#### 1. **時間分配原則**

```
假設總答題時間 100 分鐘，4 題申論題：

題目難易評估（閱讀 2 分鐘）
├─ 易題 (2 題)：各 20 分鐘 = 40 分鐘
├─ 中題 (1 題)：25 分鐘
└─ 難題 (1 題)：30 分鐘

預留時間：
- 檢查 3 分鐘
```

**策略**：
- ✅ 先做會的題目（建立信心、確保分數）
- ✅ 難題最後做（避免卡關浪費時間）
- ⚠️ 每題留 2-3 行空白（後續補充）

---

#### 2. **答題結構黃金公式**

**所有密碼學題目都適用的架構**：

```
【第一段】定義 + 目的 (10%)
→ 清楚說明技術是什麼、用來解決什麼問題

【第二段】核心原理/運作流程 (50%)
→ 詳細說明技術如何運作
→ 可用流程圖、步驟說明

【第三段】特性/優缺點 (20%)
→ 列舉技術的關鍵特性
→ 必要時說明優缺點

【第四段】應用實例 (15%)
→ 舉出實際應用場景
→ 展現實務理解

【第五段】總結 (5%)
→ 簡短總結技術重要性
```

**範例**（數位簽章題）：

```
✅ 好的開頭：
「數位簽章是結合雜湊函數與非對稱式加密的技術，
 用於確保訊息的完整性、身分鑑別與不可否認性。」

❌ 不好的開頭：
「數位簽章很重要。」（太籠統）
```

---

#### 3. **加分技巧**

**技巧 1：善用圖解**

```
流程類題目：畫流程圖
架構類題目：畫架構圖
比較類題目：畫表格

範例：TLS Handshake
Client          Server
  |--- Hello --->|
  |<-- Cert -----|
  |--- Key ----->|
  ✅ 圖解比純文字清楚 3 倍！
```

**技巧 2：使用專業術語**

```
❌ 「把資料弄亂」
✅ 「對資料進行雜湊運算 (Hashing)」

❌ 「看有沒有被改過」
✅ 「驗證資料完整性 (Integrity)」

❌ 「證明是你」
✅ 「提供身分鑑別 (Authentication)」
```

**技巧 3：舉實際案例**

```
純理論：「非對稱式加密可用於金鑰交換」
加分寫法：「非對稱式加密可用於金鑰交換，
         例如 HTTPS 的 TLS Handshake 中，
         伺服器使用 RSA 公鑰加密 Session Key」

展現實務理解 → 評分者印象深刻
```

---

### 🎯 二、各題型專屬技巧

#### 📘 加密演算法題型

**核心記憶口訣**：

```
對稱式加密：「一把鑰匙開一把鎖」
- 快速、大量資料
- 金鑰分配困難
- 代表：AES

非對稱式加密：「公開鎖、私有鑰」
- 慢速、少量資料
- 金鑰分配容易
- 代表：RSA、ECC

混合式加密：「兩者結合取長補短」
- 非對稱交換金鑰
- 對稱加密資料
- 代表：TLS
```

**必答要點**：
1. ✅ 定義與原理
2. ✅ 金鑰特性（長度、管理）
3. ✅ 優缺點（速度、安全性、應用）
4. ✅ 實際應用場景

**常見陷阱**：
- ❌ 只講優點不講缺點
- ❌ 沒說明「為何需要混合式加密」
- ❌ 忘記提金鑰長度建議

---

#### 📘 數位簽章 / PKI 題型

**記憶口訣**：

```
數位簽章：「私簽公驗」
- 簽署：私鑰加密雜湊值
- 驗證：公鑰解密比對
- 三大特性：完整、鑑別、不可否認

PKI 五大元件：「CA, RA, CRL, 憑證, Repository」
- CA：信任錨點（發證、撤銷）
- RA：前端審核（驗身分）
- CRL：黑名單（撤銷清單）
- 憑證：網路身分證（X.509）
- Repository：公開儲存庫
```

**必答要點**：
1. ✅ 運作流程（步驟化說明）
2. ✅ 安全特性（完整性、鑑別性、不可否認性）
3. ✅ 雜湊函數的角色
4. ✅ **特別強調「私鑰簽署、公鑰驗證」**（與加密相反）

**常見陷阱**：
- ❌ 搞混簽章與加密的金鑰使用方向
- ❌ 忘記提雜湊函數
- ❌ PKI 只列名稱沒說明功能

---

#### 📘 雜湊函數題型

**記憶口訣**：

```
雜湊函數四大特性「單抗雪固」：
- 單向性：無法反推
- 抗碰撞性：難找相同雜湊
- 雪崩效應：一位元變，全變
- 固定長度：輸出固定

常見應用「密整簽鏈」：
- 密碼儲存（+ Salt）
- 完整性檢查（檔案下載）
- 數位簽章（縮短長度）
- 區塊鏈（鏈接區塊）
```

**必答要點**：
1. ✅ 定義（固定長度輸出）
2. ✅ 四大特性（單向、抗碰撞、雪崩、固定長度）
3. ✅ 實際應用（至少 2 個）
4. ✅ 演算法選擇（SHA-256、避免 MD5/SHA-1）

**加分項**：
- 提到「Salt」防彩虹表攻擊
- 說明 MD5/SHA-1 棄用原因
- 舉出真實案例（Git 使用 SHA-1）

---

#### 📘 SSL/TLS 題型

**記憶口訣**：

```
TLS Handshake 簡化流程「你好-憑證-金鑰-開始」：
1. Client Hello（支援的加密套件）
2. Server Hello + Certificate（伺服器憑證）
3. Key Exchange（非對稱加密交換 Session Key）
4. Finished（切換到對稱加密通訊）

混合式加密「非對稱開場、對稱主戲」：
- 握手階段：非對稱加密（RSA/ECDHE）
- 資料傳輸：對稱加密（AES）
```

**必答要點**：
1. ✅ 混合式加密原理（為何需要）
2. ✅ Handshake 流程（簡化版至少 4 步驟）
3. ✅ 非對稱的角色（身分驗證、金鑰交換）
4. ✅ 對稱的角色（大量資料加密）

**加分項**：
- 提到 TLS 1.3 改進（0-RTT、強制 PFS）
- 說明 PFS 的重要性
- 提到加密套件選擇（ECDHE-AES-GCM）

---

### 🎯 三、分數取捨策略

#### 情境 1：時間不夠時

```
優先保證：
✅ 定義正確（10%）
✅ 核心原理/流程（50%）
✅ 關鍵特性（20%）

可以省略：
⚠️ 詳細案例（改成簡述）
⚠️ 進階技術細節

範例：
若時間不夠，「SSL/TLS」題目：
✅ 一定要寫：混合式加密原理、Handshake 基本流程
⚠️ 可以簡化：加密套件選擇、效能優化
❌ 可以省略：OCSP Stapling 詳細說明
```

---

#### 情境 2：題目不會時

```
策略：「寫相關概念也有分」

範例：不會「零知識證明」
❌ 完全空白（0 分）
✅ 寫：「零知識證明是密碼學的進階概念，
      能夠在不洩露秘密本身的情況下，
      證明知道某個秘密。類似於數位簽章，
      但提供更強的隱私保護...」（部分分）

原則：
- 從題目關鍵字聯想相關概念
- 寫出你知道的任何相關知識
- 至少展現你有基本理解
```

---

#### 情境 3：題目超綱時

```
策略：「回歸基本原理」

範例：題目問「量子密碼學」（超綱）
可以這樣答：
「量子密碼學是因應量子電腦威脅而發展的技術。
 傳統非對稱式加密（如 RSA）基於大數分解難題，
 但量子電腦可能破解。因此需要...
 - 抗量子演算法（如格密碼學）
 - 量子金鑰分發（QKD）...」

原則：
- 說明為何需要此技術
- 連結到已知的傳統技術
- 邏輯推理展現思考能力
```

---

### 🎯 四、考前最後衝刺

#### 必背核心公式與流程

**1. 數位簽章流程（30 秒複述）**：
```
簽署：Hash(訊息) → 私鑰加密 → 簽章
驗證：公鑰解密簽章 → 比對 Hash(訊息)
特性：完整性、鑑別性、不可否認性
```

**2. TLS Handshake（30 秒複述）**：
```
Client Hello → Server Certificate → Key Exchange → Finished
非對稱（握手）→ 對稱（資料傳輸）
```

**3. PKI 五大元件（20 秒複述）**：
```
CA（發證）、RA（驗身分）、CRL（黑名單）、
憑證（身分證）、Repository（公開儲存）
```

**4. 雜湊函數特性（20 秒複述）**：
```
單向性、抗碰撞性、雪崩效應、固定長度
應用：密碼儲存、完整性、數位簽章、區塊鏈
```

---

#### 考前 1 小時檢查清單

- [ ] 對稱 vs 非對稱優缺點表格
- [ ] 數位簽章完整流程（能畫圖）
- [ ] TLS Handshake 簡化流程
- [ ] PKI 五大元件與功能
- [ ] 雜湊函數四大特性
- [ ] MD5/SHA-1 為何棄用
- [ ] RSA vs ECC 差異
- [ ] MAC vs 數位簽章差異
- [ ] PFS 完美前向保密原理
- [ ] 台灣電子簽章法重點

---

## 🔗 參考資源

### 📚 官方標準文件

**NIST（美國國家標準與技術研究院）**：
- [FIPS 197: AES 標準](https://csrc.nist.gov/pubs/fips/197/final)  
  → 對稱式加密標準
- [FIPS 186-5: 數位簽章標準](https://csrc.nist.gov/pubs/fips/186-5/final)  
  → RSA、DSA、ECDSA 規範
- [NIST SP 800-52: TLS 指南](https://csrc.nist.gov/publications/detail/sp/800-52/rev-2/final)  
  → TLS 實作建議
- [NIST SP 800-57: 金鑰管理建議](https://csrc.nist.gov/publications/detail/sp/800-57-part-1/rev-5/final)  
  → 金鑰長度與生命週期
- [NIST SP 800-175B: 密碼學演算法指南](https://csrc.nist.gov/publications/detail/sp/800-175b/rev-1/final)  
  → 演算法選擇建議

**IETF（網際網路工程任務組）RFC**：
- [RFC 5246: TLS 1.2](https://datatracker.ietf.org/doc/html/rfc5246)
- [RFC 8446: TLS 1.3](https://datatracker.ietf.org/doc/html/rfc8446)
- [RFC 5280: X.509 憑證與 CRL 格式](https://datatracker.ietf.org/doc/html/rfc5280)
- [RFC 6960: OCSP 協定](https://datatracker.ietf.org/doc/html/rfc6960)
- [RFC 8017: RSA 密碼學規範](https://datatracker.ietf.org/doc/html/rfc8017)

---

### 🌐 線上學習資源

**互動式教學**：
- [Cryptography I - Stanford (Coursera)](https://www.coursera.org/learn/crypto)  
  → Dan Boneh 經典密碼學課程
- [Practical Cryptography for Developers](https://cryptobook.nakov.com/)  
  → 實務導向的密碼學教材
- [SSL/TLS 詳解 (Cloudflare)](https://www.cloudflare.com/learning/ssl/what-is-ssl/)  
  → TLS 原理與最佳實務

**影片課程**：
- [Computerphile - Cryptography Playlist](https://youtube.com/playlist?list=PLzH6n4zXuckpKAj1_88VS-8Z6yn9zX_P6)  
  → 密碼學概念影片（英文）
- [Khan Academy - Cryptography](https://www.khanacademy.org/computing/computer-science/cryptography)  
  → 基礎密碼學入門

---

### 🛠️ 實務工具與測試

**密碼學工具**：
- [OpenSSL 官方文件](https://www.openssl.org/docs/)  
  → 最常用的密碼學工具庫
- [GPG (GnuPG) 文件](https://gnupg.org/documentation/)  
  → PGP 實作，Email 加密與簽章

**SSL/TLS 測試**：
- [SSL Labs Server Test](https://www.ssllabs.com/ssltest/)  
  → 測試網站 SSL/TLS 設定
- [testssl.sh](https://github.com/drwetter/testssl.sh)  
  → 命令列 SSL/TLS 測試工具
- [Mozilla SSL Configuration Generator](https://ssl-config.mozilla.org/)  
  → 產生安全的 SSL 設定

**學習與練習**：
- [CryptoHack](https://cryptohack.org/)  
  → 密碼學挑戰題（CTF 形式）
- [Cryptopals Challenges](https://cryptopals.com/)  
  → 實作導向的密碼學練習

---

### 📖 推薦書籍

**中文書籍**：
- 《密碼學原理與實務》（陳志銘 著）  
  → 適合國考準備，理論與實務並重
- 《圖解密碼學與網路安全》  
  → 視覺化學習，適合初學者

**英文書籍**（進階）：
- *Understanding Cryptography* - Christof Paar  
  → 密碼學教科書，深入淺出
- *Cryptography Engineering* - Ferguson, Schneier, Kohno  
  → 實務密碼學設計
- *Applied Cryptography* - Bruce Schneier  
  → 密碼學聖經（偏理論）

---

### 🇹🇼 台灣在地資源

**政府機構**：
- [內政部憑證管理中心 (MOICA)](https://moica.nat.gov.tw/)  
  → 自然人憑證相關資訊
- [經濟部工商憑證管理中心 (GCA)](https://gca.nat.gov.tw/)  
  → 工商憑證申請與管理
- [台灣網路認證公司 (TWCA)](https://www.twca.com.tw/)  
  → 民間 CA、SSL 憑證

**法規文件**：
- [電子簽章法（全國法規資料庫）](https://law.moj.gov.tw/LawClass/LawAll.aspx?PCode=J0080037)  
  → 台灣電子簽章法律規範

**資安社群**：
- [HITCON（台灣駭客年會）](https://hitcon.org/)  
  → 密碼學與資安研討會
- [OWASP Taiwan](https://owasp.org/www-chapter-taiwan/)  
  → 應用安全社群

---

### 🔍 快速查詢工具

**演算法安全性查詢**：
- [Keylength.com](https://www.keylength.com/)  
  → 各機構建議的金鑰長度
- [CipherSuite Info](https://ciphersuite.info/)  
  → TLS 加密套件資訊查詢

**即時資安新聞**：
- [Schneier on Security](https://www.schneier.com/)  
  → Bruce Schneier 的資安部落格
- [The Hacker News](https://thehackernews.com/)  
  → 密碼學漏洞與攻擊新聞

---

### 📊 考試重點優先級

**必讀（考試必考）**：
⭐⭐⭐⭐⭐
- 對稱 vs 非對稱加密比較
- 數位簽章完整流程
- PKI 五大元件
- 雜湊函數特性與應用
- SSL/TLS 混合式加密

**重要（常考）**：
⭐⭐⭐⭐
- RSA vs ECC 比較
- TLS 1.3 改進
- CRL vs OCSP
- MAC vs 數位簽章
- 完美前向保密（PFS）

**進階（選讀）**：
⭐⭐⭐
- 零知識證明
- 同態加密
- 量子密碼學
- 區塊鏈密碼學應用

---

**祝您考試順利！🎓**

記住：密碼學考題重視**原理理解**勝過死背，理解「為什麼需要這個技術」比記住所有細節更重要。善用本文的答題架構與技巧，必能在考場上發揮實力！

---

**文件版本**：v1.0  
**最後更新**：2024年1月  
**維護者**：資通安全考試準備團隊
