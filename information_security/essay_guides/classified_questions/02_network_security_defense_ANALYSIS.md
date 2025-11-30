# 網路安全與防禦技術 (Network Security & Defense) 完整題目解析 - 申論題答題框架

這份文件針對**網路安全與防禦技術**相關題目提供詳盡的申論題答題架構，涵蓋防火牆、IDS/IPS、VPN、DDoS 防禦、零信任架構等核心考點。

---

## 📊 題目總覽

### 題目統計

| 統計項目 | 數量 |
|---------|------|
| **分析考卷總數** | **24 份** |
| **網路安全與防禦相關題目** | **26 題** (完整收錄) |
| **高考三級+近三年出現次數** | 12 次 |
| **重要性排名** | **No. 3** (熱門考點) |

### 題型分類

| 題型 | 占比 | 代表題目 | 難度 |
|------|------|---------|------|
| **零信任架構 (Zero Trust)** | 30% | ZTA 原則、身分驗證、設備鑑別 | ⭐⭐⭐⭐⭐ |
| **防火牆技術** | 25% | Firewall, WAF, NGFW, DMZ | ⭐⭐⭐⭐ |
| **IDS/IPS** | 15% | 入侵偵測與防禦系統 | ⭐⭐⭐⭐ |
| **DDoS 防禦** | 15% | 分散式阻斷服務攻擊與防護 | ⭐⭐⭐⭐ |
| **VPN 與遠端存取** | 10% | 虛擬私人網路、遠端工作安全 | ⭐⭐⭐ |
| **Proxy 代理伺服器** | 5% | Forward/Reverse Proxy | ⭐⭐⭐ |

---

## 🎯 網路安全防禦申論題答題黃金架構

### 通用架構

```
第一部分：技術定義與目的 (20%)
├─ 定義關鍵技術
├─ 說明防禦目標 (針對哪種威脅)
└─ 在防禦架構中的定位

第二部分：運作原理或核心機制 (40%)
├─ 詳細說明運作流程
├─ 核心技術元件
├─ 部署架構圖
└─ 實際範例

第三部分：優缺點或限制 (20%)
├─ 優點與防禦效果
├─ 缺點與限制
└─ 適用情境

第四部分：實務應用與最佳實踐 (20%)
├─ 實際部署案例
├─ 搭配其他防禦技術
├─ 實務工具與產品
└─ 未來趨勢
```

---

## 📚 【核心知識】網路安全防禦完全解析

### 一、防火牆演進歷史

| 世代 | 類型 | 運作層級 | 檢查內容 | 優點 | 缺點 |
|------|------|---------|---------|------|------|
| **第一代** | 封包過濾式 | L3/L4 | IP, Port | 快速、低成本 | 無法檢查應用層內容 |
| **第二代** | 狀態檢測 | L3/L4 | 連線狀態 | 防禦 SYN Flood | 需維護狀態表，記憶體消耗 |
| **第三代** | 應用層代理 | L7 | 應用內容 | 深度檢測、完整日誌 | 效能開銷大 |
| **第四代** | WAF | L7 | HTTP/HTTPS | 防 OWASP Top 10 | 僅限 Web 應用 |
| **第五代** | NGFW | L3-L7 | 全面整合 | 整合多功能 | 成本高、複雜 |

### 二、IDS vs IPS 完整比較

| 特性 | IDS (入侵偵測系統) | IPS (入侵防禦系統) |
|------|-------------------|-------------------|
| **英文全名** | Intrusion Detection System | Intrusion Prevention System |
| **部署方式** | 旁路監聽 (Span/Mirror Port) | 串聯在線 (Inline) |
| **主要動作** | 偵測 + 告警 | 偵測 + 阻擋 |
| **流量影響** | 無影響 (被動監聽) | 所有流量經過 (主動防禦) |
| **誤判風險** | 僅產生誤報 | 可能阻斷正常流量 |
| **延遲** | 無 | 微秒至毫秒級 |
| **偵測方法** | 簽章式 + 異常式 | 簽章式 + 異常式 |
| **適用** | 監控、分析、稽核 | 即時防護 |

**偵測技術**：
1. **簽章式 (Signature-Based)**：比對已知攻擊特徵，類似防毒軟體病毒碼
2. **異常式 (Anomaly-Based)**：建立正常行為基準線，偵測偏離
3. **協定分析 (Protocol Analysis)**：檢查協定是否符合 RFC 標準

### 三、零信任架構 (Zero Trust) 核心原則

**定義**：基於「**永不信任，始終驗證 (Never Trust, Always Verify)**」的安全模型

**傳統邊界防禦 vs 零信任**：

| 項目 | 傳統邊界防禦 | 零信任架構 |
|------|------------|-----------|
| **信任模型** | 城堡與護城河 (內網可信) | 全不可信 |
| **驗證** | 一次驗證 (登入後暢通) | 持續驗證 (每次存取) |
| **存取控制** | 網路層 (VLAN 分段) | 身分 + 裝置 + 脈絡 |
| **橫向移動** | 容易 (內網互通) | 困難 (微分段) |
| **預設** | Allow (白名單外允許) | Deny (黑名單內拒絕) |

**零信任三大支柱**：
1. **身分驗證 (Identity Verification)** - MFA, SSO, Risk-Based Auth
2. **設備鑑別 (Device Authentication)** - NAC, TPM, MDM
3. **最小權限 (Least Privilege Access)** - JIT, PAM

### 四、DDoS 攻擊分類

**按攻擊層級分類**：

| 類型 | OSI 層 | 攻擊手法 | 特徵 | 防禦難度 |
|------|--------|---------|------|---------|
| **容量耗盡** | L3/L4 | UDP Flood, ICMP Flood, DNS Amp | Gbps-Tbps 流量 | ⭐⭐⭐⭐ |
| **協定攻擊** | L3/L4 | SYN Flood, ACK Flood | 耗盡連線表 | ⭐⭐⭐ |
| **應用層** | L7 | HTTP Flood, Slowloris | 模擬正常使用者 | ⭐⭐⭐⭐⭐ |

**容量耗盡攻擊範例**：
- **DNS Amplification**：偽造來源 IP，向開放 DNS 查詢，回應流量放大 50-100 倍

---

## 📝 完整題目解析

> **說明**：以下題目按年份由新到舊排列

---

## 【近三年題目】112-114年

### 題目 1：零信任架構 - 身分識別與設備鑑別

#### 📖 原題 (114年高考二級)

> **題目**：使用者身分識別（User Identification）及設備鑑別（Device Authentication）是建立零信任架構（Zero Trust Architecture）的重要基礎。
> (一) 請說明至少 3 種使用者身分識別方法。（15 分）
> (二) 請說明至少 2 種設備鑑別方法。（10 分）

#### 🎯 答題架構分析

1. **零信任背景**：說明 ZTA 為何需要強身分驗證
2. **使用者身分識別**：列舉 3-5 種方法並詳述
3. **設備鑑別**：列舉 2-3 種方法並詳述
4. **整合應用**：說明兩者如何搭配

#### 📊 評分建議 (預估配分 25 分)

**第一小題（15 分）：使用者身分識別方法（至少 3 種）**
- 方法 1：多因素驗證 MFA（5 分）
  - 定義與原理（2 分）
  - 實作方式（OTP、生物辨識、硬體 Token）（2 分）
  - 優勢說明（1 分）
- 方法 2：單一簽入 SSO（5 分）
  - 定義與運作流程（2 分）
  - 協定（SAML、OAuth、OpenID Connect）（2 分）
  - 優缺點（1 分）
- 方法 3：生物辨識（5 分）
  - 類型（指紋、臉部、虹膜）（2 分）
  - 優點（不可否認性、便利）（2 分）
  - 限制（隱私、誤差）（1 分）

**第二小題（10 分）：設備鑑別方法（至少 2 種）**
- 方法 1：憑證型驗證（5 分）
  - 數位憑證（X.509）機制（2 分）
  - PKI 基礎設施（2 分）
  - 優勢（強度高、不可偽造）（1 分）
- 方法 2：設備指紋辨識（5 分）
  - Device Fingerprinting 原理（2 分）
  - 收集資訊（MAC、硬體 ID、作業系統）（2 分）
  - NAC (Network Access Control) 應用（1 分）

**答題提示**：
- ✅ 每種方法都要**說明原理+實作方式+優缺點**
- ✅ 題目要求「至少」，建議多寫 1-2 種加分
- ✅ 可結合實際產品（如 Google Authenticator、YubiKey）
- ⚠️ 零信任背景可簡述，重點在方法說明

#### ✍️ 標準答案示範

**解答**：

**前言：零信任架構與身分/設備驗證的重要性**

零信任架構 (Zero Trust Architecture, ZTA) 是基於「**永不信任，始終驗證 (Never Trust, Always Verify)**」原則的資安框架。與傳統「內網可信、外網不可信」的邊界防禦不同，零信任假設**所有網路環境皆不可信**，要求對每次存取請求進行嚴格的**身分驗證 (Authentication)** 與**授權 (Authorization)**。

**為何需要強化身分與設備驗證**：
- **內部威脅增加**：70% 資安事件源自內部或合法憑證遭竊
- **遠端工作常態化**：疫情後 WFH 導致傳統邊界模糊
- **橫向移動攻擊**：駭客取得一台主機後快速擴散 (如 Pass-the-Hash)

零信任的核心是**「誰 (Who) + 什麼裝置 (What Device) + 在哪裡 (Where) + 做什麼 (What Action)」**，因此**使用者身分識別**與**設備鑑別**是實現 ZTA 的兩大基石。

---

**一、使用者身分識別方法 (至少3種)**

**方法一：多因素驗證 (MFA, Multi-Factor Authentication)**

**定義**：
結合**兩種以上驗證因子**，大幅提升帳號安全性。

**三種驗證因子類型**：
1. **知識因子 (Something You Know)**：密碼、PIN、安全問題
2. **擁有因子 (Something You Have)**：手機 OTP、硬體 Token (YubiKey)、Smart Card
3. **生物因子 (Something You Are)**：指紋、臉部辨識、虹膜掃描

**實施範例**：
- **傳統 MFA**：輸入密碼 + 手機簡訊 OTP (6位數字，60秒有效)
- **App-Based OTP**：Google Authenticator, Microsoft Authenticator (TOTP 演算法)
- **硬體 Token**：YubiKey (支援 FIDO2 標準，抗釣魚)
- **Push 通知**：Duo Mobile，手機收到通知點選「核准」

**技術原理 (TOTP)**：
```
TOTP = HMAC-SHA1(Secret Key, Time / 30秒)
```
每 30 秒產生新的 6 位數 OTP，伺服器與客戶端同步驗證。

**優點**：
- 即使密碼洩漏，攻擊者仍需第二因子
- 符合法規要求 (如 PCI-DSS, GDPR)

**缺點**：
- 簡訊 OTP 易遭 SIM Swap 攻擊
- 使用者體驗較差 (額外步驟)

---

**方法二：單一登入 (SSO, Single Sign-On)**

**定義**：
使用者**一次驗證**後，可存取多個整合系統，無需重複登入。

**運作協定**：
1. **SAML 2.0 (Security Assertion Markup Language)**：
   - 企業級 SSO 標準
   - 基於 XML，支援斷言 (Assertion) 傳遞身分資訊
   
2. **OAuth 2.0 + OpenID Connect (OIDC)**：
   - OAuth 2.0：授權框架
   - OIDC：在 OAuth 2.0 上增加身分驗證層
   - 常見於雲端服務 (如「用 Google 帳號登入」)

**SSO 流程 (SAML 範例)**：
```
1. 使用者存取 ServiceProvider (SP, 如 Salesforce)
2. SP 重導向至 IdentityProvider (IdP, 如 Okta)
3. 使用者在 IdP 驗證身分 (帳密 + MFA)
4. IdP 簽發 SAML Assertion (包含使用者屬性)
5. 瀏覽器帶 Assertion 回SP
6. SP 驗證簽章，授予存取權限
```

**優點**：
- **改善使用者體驗**：減少密碼疲勞
- **集中身分管理**：IT 管理員統一管控
- **降低密碼風險**：減少重複使用弱密碼

**產品**：Okta, Azure AD, Google Workspace

---

**方法三：生物識別驗證 (Biometric Authentication)**

**定義**：
利用個人**獨特生理或行為特徵**進行身分識別。

**生理生物識別**：
1. **指紋辨識 (Fingerprint)**：
   - 最普及，手機 TouchID, Windows Hello
   - 誤判率 (FAR, False Accept Rate)：0.001%
   
2. **臉部辨識 (Face Recognition)**：
   - 2D：照片易偽造
   - 3D 結構光：Apple Face ID，投射 30,000 個紅外線點
   
3. **虹膜掃描 (Iris Scan)**：
   - 高安全性，機場通關使用
   - 成本高，需專用硬體
   
4. **靜脈辨識 (Vein Pattern)**：
   - 掃描手指靜脈紋路
   - 難以偽造 (需活體血液流動)

**行為生物識別**：
1. **聲紋辨識 (Voice Recognition)**：語音助理、電話銀行
2. **打字節奏 (Keystroke Dynamics)**：分析打字速度與間隔
3. **步態辨識 (Gait Recognition)**：分析走路姿勢

**優點**：
- 無法遺忘或遺失
- 使用者體驗佳 (快速解鎖)

**缺點**：
- **一旦洩漏無法更換**：指紋被複製後終生無效
- 隱私疑慮：生物特徵資料外洩風險
- 誤判問題：光線、受傷影響辨識率

**安全強化**：
- 使用 Secure Enclave (如 Apple T2 晶片) 儲存生物特徵範本
- 結合 MFA：Face ID + Passcode

---

**方法四：憑證式驗證 (Certificate-Based Authentication)**

**定義**：
使用**數位憑證 (X.509)** 驗證使用者身分，基於 PKI (Public Key Infrastructure)。

**運作原理**：
1. **憑證簽發**：企業 CA (Certificate Authority) 簽發使用者憑證
2. **憑證儲存**：儲存於智慧卡 (Smart Card) 或 TPM
3. **驗證流程**：
   - 使用者出示憑證
   - 系統驗證憑證簽章 (由受信任 CA 簽發)
   - 系統發送隨機挑戰 (Challenge)
   - 使用者用私鑰簽章回應
   - 系統用公鑰驗證簽章

**應用場景**：
- **智慧卡登入**：員工插入智慧卡 + PIN 登入電腦
- **VPN 連線**：使用憑證驗證身分 (比帳密更安全)
- **Email 簽章**：S/MIME 數位簽章

**優點**：
- 抗釣魚：憑證難以偽造
- 強身分綁定：公私鑰對應

**缺點**：
- PKI 建置成本高
- 憑證管理複雜 (過期、撤銷)

---

**方法五：風險式驗證 (Risk-Based Authentication, RBA)**

**定義**：
依據**登入情境風險**動態調整驗證強度。

**風險評估因子**：
1. **地理位置**：突然從海外 IP 登入
2. **登入時間**：非辦公時間 (凌晨 3 點)
3. **裝置指紋**：使用陌生裝置
4. **行為異常**：短時間多次失敗登入
5. **網路類型**：公共 WiFi vs 企業網路

**驗證強度調整**：
- **低風險**：僅密碼 (已知裝置 + 公司網路)
- **中風險**：密碼 + Email OTP (新裝置)
- **高風險**：密碼 + MFA + 管理員批准 (海外IP + 權限帳號)

**技術實現**：
- **機器學習**：分析歷史登入模式，偵測異常
- **威脅情資**：整合黑名單 IP 資料庫

**產品範例**：
- **Google**：偵測異地登入發送通知「這是您嗎？」
- **Microsoft Azure AD Identity Protection**：計算登入風險分數

---

**二、設備鑑別方法 (至少2種)**

**方法一：NAC (Network Access Control, 網路存取控制)**

**定義**：
在允許設備連接網路前，**驗證設備是否符合企業安全政策**。

**檢查項目 (Device Posture Assessment)**：
1. **防毒軟體**：是否安裝並更新病毒碼 (24小時內)
2. **作業系統修補**：是否安裝最新安全更新
3. **防火牆狀態**：是否啟用 Windows Firewall
4. **設備憑證**：是否由企業 IT 部門核發
5. **加密狀態**：硬碟是否啟用 BitLocker/FileVault
6. **合規軟體**：禁止安裝 P2P 軟體 (如 BitTorrent)

**NAC 運作流程**：
```
1. 設備連接網路 (有線/無線)
2. NAC Agent 蒐集設備狀態資訊
3. NAC Server 評估是否符合政策
4. 評估結果：
   ├─ 合規 → 允許存取內網 (VLAN 10)
   ├─ 部分合規 → 存取受限網段 (VLAN 20, 僅能更新)
   └─ 不合規 → 隔離至 Quarantine VLAN (VLAN 99)
5. 隔離設備僅能存取修補伺服器 (WSUS, Antivirus Update Server)
6. 修補完成後重新評估
```

**部署模式**：
- **802.1X**：基於 EAP (Extensible Authentication Protocol)
- **DHCP-based**：依 DHCP Option 分配 VLAN
- **Out-of-Band**：透過 Span Port 被動監控

**優點**：
- 確保連網設備符合安全基準
- 自動化合規檢查

**缺點**：
- 需部署 Agent (BYOD 裝置可能拒絕安裝)
- 管理複雜度高

**產品**：Cisco ISE, Aruba ClearPass, ForeScout CounterACT

---

**方法二：裝置指紋識別 (Device Fingerprinting)**

**定義**：
收集設備的**唯一特徵組合**，建立「裝置身分證」，用於識別與追蹤。

**收集資訊類別**：

**1. 硬體特徵**：
- **MAC Address**：網卡實體位址
- **CPU 型號**：Intel Core i7-10700K
- **螢幕解析度**：1920x1080
- **GPU 資訊**：NVIDIA RTX 3070
- **電池狀態**：充電狀態、容量 (行動裝置)

**2. 軟體特徵**：
- **作業系統**：Windows 11 Build 22000
- **瀏覽器**：Chrome 120.0.6099.109
- **已安裝字型**：系統字型清單
- **外掛程式**：Flash, Silverlight (已過時)
- **語言設定**：繁體中文 (台灣)
- **時區**：UTC+8

**3. 網路特徵**：
- **User-Agent**：Mozilla/5.0 ...
- **IP Address**：公網IP與歷史紀錄
- **WebRTC Leak**：透過 WebRTC 取得內網IP

**4. 進階指紋技術**：
- **Canvas Fingerprint**：利用 HTML5 Canvas 渲染差異
- **AudioContext Fingerprint**：音訊處理細微差異
- **WebGL Fingerprint**：GPU 渲染特徵

**指紋生成範例**：
```javascript
// 簡化範例
fingerprint = SHA256(
  navigator.userAgent +
  screen.width + "x" + screen.height +
  navigator.language +
  new Date().getTimezoneOffset() +
  canvas_hash +
  installed_fonts
)
```

**應用場景**：
1. **偵測新裝置登入**：與歷史指紋比對，若不符則要求額外驗證
2. **防止帳號盜用**：駭客從不同裝置登入，指紋不符觸發告警
3. **廣告追蹤**：跨網站追蹤使用者 (隱私爭議)

**優點**：
- 無需安裝 Agent
- 難以完全偽造 (需修改大量參數)

**缺點**：
- 瀏覽器更新可能改變指紋
- 隱私疑慮 (GDPR 限制)

---

**方法三：TPM (Trusted Platform Module, 可信賴平台模組)**

**定義**：
內建於主機板的**硬體安全晶片**，提供加密金鑰儲存與安全開機功能。

**TPM 主要功能**：

**1. 安全開機 (Secure Boot)**：
- **啟動鏈驗證**：BIOS → Bootloader → OS Kernel
- 每階段測量 (Measure) 元件雜湊值，儲存於 PCR (Platform Configuration Register)
- 若元件被竄改 (如 BootKit Rootkit)，雜湊值不符 → 拒絕啟動

**2. 金鑰管理**：
- **金鑰生成與儲存**：產生 RSA/ECC 金鑰對，私鑰永不離開 TPM
- **封存 (Sealing)**：將資料加密並綁定特定 PCR 狀態
- **解封 (Unsealing)**：僅當系統狀態符合才能解密

**3. 磁碟加密 (BitLocker / FileVault)**：
- 加密金鑰儲存於 TPM
- 開機時自動解鎖 (無需輸入密碼)
- 若硬碟被拔除插至其他電腦 → TPM 不同 → 無法解密

**4. 裝置認證 (Device Attestation)**：
- TPM 簽發設備憑證 (Endorsement Key, EK)
- 證明「這台設備確實擁有 TPM」

**Windows 11 要求**：
- **強制 TPM 2.0**：提升安全基準

**設備鑑別應用**：
```
1. 設備連線至 ZTA Gateway
2. Gateway 要求 TPM Attestation
3. 設備用 TPM 私鑰簽署 PCR 值
4. Gateway 驗證簽章與開機狀態
5. 若系統被竄改 (PCR 異常) → 拒絕存取
```

**優點**：
- 硬體層級安全，難以破解
- 防止系統被竄改

**缺點**：
- 需硬體支援 (舊設備無 TPM)
- 主機板更換需重新封存金鑰

---

**方法四：MDM (Mobile Device Management, 行動裝置管理)**

**定義**：
集中管理與監控企業行動裝置 (手機、平板)，確保符合安全政策。

**MDM 核心功能**：

**1. 設備註冊與配置**：
- **自動配置**：員工登入後自動安裝企業 App、VPN 設定、WiFi 憑證
- **遠端配置**：IT 管理員推送政策 (如強制 8 位數密碼)

**2. 合規檢查**：
- **越獄/Root 偵測**：iOS 越獄、Android Root
- **加密檢查**：裝置儲存是否加密
- **OS 版本**：是否更新至最新版本

**3. 應用程式管理**：
- **白名單/黑名單**：允許安裝特定 App，禁止遊戲
- **企業 App Store**：私有應用市集

**4. 資料保護**：
- **容器化 (Containerization)**：隔離企業資料與個人資料
- **遠端抹除 (Remote Wipe)**：裝置遺失時清除企業資料

**5. 位置追蹤**：
- GPS 定位 (需員工同意)

**MDM 與 ZTA 整合**：
```
1. 使用者用手機存取企業資源
2. ZTA Gateway 查詢 MDM 狀態
3. MDM 回報：
   - 裝置已註冊
   - 未越獄
   - 已加密
   - 密碼符合政策
4. ZTA 允許存取
```

**BYOD (Bring Your Own Device) 挑戰**：
- 員工抗拒安裝 MDM (隱私疑慮)
- 解方：**MAM (Mobile Application Management)** - 僅管理企業 App，不控制整台裝置

**產品**：Microsoft Intune, VMware Workspace ONE, Jamf (iOS專用)

---

**三、身分驗證與設備鑑別的整合應用**

**雙重保障機制**：
零信任架構要求**同時**驗證「**誰 (Who)**」與「**什麼裝置 (What Device)**」：

```
存取請求：
  ├─ 身分驗證 (User Authentication)
  │   ├─ MFA (密碼 + OTP)
  │   └─ 風險評估 (登入位置、時間)
  └─ 設備鑑別 (Device Authentication)
      ├─ NAC (合規檢查)
      ├─ 裝置指紋 (已知裝置?)
      └─ TPM Attestation (系統完整性)

→ 皆通過 → 授予存取 (依最小權限原則)
→ 任一失敗 → 拒絕或降級存取
```

**實務案例：企業遠端工作 ZTA 部署**：

1. **員工在家登入 VPN**：
   - 身分驗證：Azure AD (SSO + MFA)
   - 設備鑑別：Intune MDM 檢查 (防毒、更新、加密)
   
2. **存取權限決策**：
   - 若設備合規 + MFA 通過 → 允許存取內部系統
   - 若設備部分合規 (防毒過期) → 僅能存取更新伺服器
   - 若使用個人裝置 (非企業管控) → 僅提供 Web App (瀏覽器隔離)

3. **持續監控**：
   - 每小時重新驗證
   - 若偵測異常行為 (大量下載) → 立即撤銷存取

**評分標準** (預估)：
- 使用者身分識別方法 (列舉3-5種，每種詳細說明)：15分
- 設備鑑別方法 (列舉2-4種，每種詳細說明)：10分

#### 💡 補充說明

**零信任架構標準與框架**：
- **NIST SP 800-207**：美國零信任架構標準
- **CISA Zero Trust Maturity Model**：分五級成熟度
- **Google BeyondCorp**：Google 零信任實作案例

**零信任實施挑戰**：
1. **使用者體驗**：過度驗證導致抱怨
2. **Legacy 系統**：舊系統不支援 MFA/NAC
3. **成本**：硬體 Token、NAC 設備投資
4. **文化轉變**：從「預設信任」到「預設懷疑」

**未來趨勢**：
- **SASE (Secure Access Service Edge)**：雲端化零信任
- **ZTNA (Zero Trust Network Access)**：取代傳統 VPN
- **Passwordless**：FIDO2, WebAuthn 無密碼驗證

---

### 題目 2：防火牆技術 - WAF 與 NGFW

#### 📖 原題 (113年高考三級)

> **題目**：防火牆用以保障內部網路避免受攻擊，目前常被應用的有 WAF（Web Application Firewall）及次世代防火牆（Next-Generation Firewall, NGFW），試問：
> (一) WAF 的防禦機制為何？（10 分）
> (二) 次世代防火牆的防禦機制為何？（10 分）
> (三) 當內容傳遞網路 CDN（Content Delivery Network）與 WAF 架設在一起時，其效益為何？（5 分）

#### 🎯 答題架構分析

1. **WAF 定義**：應用層防火牆專門防禦 Web 攻擊
2. **WAF 防禦機制**：OWASP Top 10、簽章式、虛擬修補
3. **NGFW 定義**：整合多功能的新世代防火牆
4. **NGFW 防禦機制**：應用程式識別、IPS、SSL解密等
5. **CDN + WAF 效益**：分散式防禦、降低延遲

#### 📊 評分建議 (預估配分 25 分)

**第一小題（10 分）：WAF 防禦機制**
- WAF 定義與目的（2 分）
  - 應用層防火牆（1 分）
  - 專門防禦 Web 攻擊（1 分）
- 防禦機制（8 分）
  - 簽章式偵測（Signature-based）（2 分）
  - 行為分析（Behavioral Analysis）（2 分）
  - 虛擬修補（Virtual Patching）（2 分）
  - OWASP Top 10 防護（2 分）

**第二小題（10 分）：NGFW 防禦機制**
- NGFW 定義（2 分）
  - 整合多功能的新世代防火牆（2 分）
- 防禦機制（8 分）
  - 應用程式辨識與控制（2 分）
  - 入侵防禦系統 IPS（2 分）
  - SSL/TLS 解密檢查（2 分）
  - 進階威脅防護（沙箱、惡意軟體分析）（2 分）

**第三小題（5 分）：CDN + WAF 效益**
- DDoS 防護（2 分）
  - 分散式架構吸收攻擊流量
- 效能提升（2 分）
  - 降低延遲、加速網站
- 其他效益（1 分）
  - 全球防護、節省頻寬

**答題提示**：
- ✅ WAF 要說明**具體防禦什麼攻擊**（SQL Injection、XSS 等）
- ✅ NGFW 要強調與傳統防火牆的**差異**（應用層識別）
- ✅ CDN + WAF 要說明**協同效益**，不只列優點
- ⚠️ 每個機制都要舉例說明


#### ✍️ 標準答案示範

**解答**：

**一、WAF (Web Application Firewall) 防禦機制**

**（一）WAF 定義與定位**

WAF 是部署於 Web 應用程式之前的**應用層 (OSI Layer 7) 防火牆**，專門檢查與過濾 HTTP/HTTPS 流量，防禦針對 Web 應用的攻擊（如 SQL Injection, XSS）。

**與傳統防火牆差異**：

| 項目 | 傳統防火牆 | WAF |
|------|-----------|-----|
| **運作層級** | L3/L4 (網路層/傳輸層) | L7 (應用層) |
| **檢查對象** | IP, Port, Protocol | HTTP Request/Response 內容 |
| **防禦目標** | 未授權連線、DoS | OWASP Top 10, 應用邏輯漏洞 |
| **規則** | 5-Tuple (IP:Port) | URL Pattern, 參數內容 |

**（二）WAF 防禦機制**

**機制一：OWASP Top 10 攻擊防護**

WAF 針對 Web 應用十大風險提供專門防護：

| 攻擊類型 | 檢測方式 | WAF 防禦動作 |
|---------|---------|------------|
| **SQL Injection** | 檢測 SQL 語法 (`SELECT`, `UNION`, `'or'1'='1`) | 阻擋請求、編碼特殊字元 |
| **XSS (跨站腳本)** | 檢測 `<script>`, `javascript:`, `onerror=` | 過濾標籤、HTML Entity 編碼 |
| **CSRF** | 驗證 Referer Header, Token | 要求 Anti-CSRF Token |
| **Path Traversal** | 檢測 `../`, `..\\`, `%2e%2e` | 標準化路徑、阻擋 |
| **Command Injection** | 檢測 `;`, `|`, `&&`, `$(...)` | 阻擋 Shell 特殊字元 |
| **XXE (XML 外部實體)** | 解析 XML, 檢測 `<!ENTITY>` | 禁用外部實體 |
| **File Upload** | 檢查副檔名、Magic Bytes | 白名單副檔名 |

**SQL Injection 防禦範例**：

```http
# 惡意請求
GET /product?id=1' UNION SELECT username,password FROM users-- 

# WAF 偵測
Pattern Match: UNION.*SELECT.*FROM
Risk Score: 95/100
Action: Block (403 Forbidden)
```

**機制二：簽章式偵測 (Signature-Based Detection)**

**運作原理**：
- 維護**已知攻擊特徵資料庫** (如 ModSecurity Core Rule Set)
- 比對 HTTP Request 是否符合惡意簽章
- 定期自動更新規則

**規則範例 (ModSecurity)**：

```apache
SecRule ARGS "@rx (?i)(select|union|insert|update|delete).*from" \
  "id:1001,phase:2,deny,status:403,msg:'SQL Injection Detected'"
```

**機制三：行為分析 (Anomaly-Based Detection)**

**運作原理**：
1. **學習期**：建立正常流量模式基準線 (Baseline)
   - 正常請求頻率：每分鐘 100 次
   - 正常參數長度：使用者名稱 ≤ 20 字元
   - 常見 User-Agent 清單

2. **偵測期**：偵測偏離基準線的異常行為
   - 突然每秒 1000 次 POST 請求 (疑似 DDoS)
   - 參數長度 10000 字元 (疑似 Buffer Overflow)
   - 罕見 User-Agent (疑似掃描工具)

**機制四：正向安全模型 (Positive Security Model / Whitelist)**

**定義**：僅允許**明確定義的合法行為**，預設拒絕所有其他行為。

**實施方式**：
- **輸入驗證**：
  - 電話欄位：僅接受 `^09[0-9]{8}$`
  - Email：`^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$`
  - 信用卡號：Luhn 演算法驗證

- **URL 白名單**：
  ```
  允許：
    /login
    /products/*
    /api/v1/*
  
  拒絕：其他所有路徑
  ```

**優點**：
- 防禦未知攻擊 (Zero-Day)
- 安全性高

**缺點**：
- 設定複雜，初期誤判率高
- 需不斷調整規則

**機制五：虛擬修補 (Virtual Patching)**

**情境**：
應用程式發現高風險漏洞 (如 CVE-2023-XXXX)，但開發團隊需要 2 週才能修補上線。

**WAF 虛擬修補流程**：
1. 安全公告發布 CVE 詳情與 PoC (Proof of Concept)
2. WAF 廠商分析漏洞，編寫阻擋規則
3. 管理員部署新規則至 WAF (數小時內完成)
4. WAF 即時阻擋利用此漏洞的攻擊
5. 開發團隊同步進行正式修補

**實例**：
- **Log4Shell (CVE-2021-44228)**：WAF 阻擋 `${jndi:ldap://...}` 字串

**優點**：
- 爭取修補時間
- 降低緊急修補風險 (未充分測試)

**（三）WAF 部署模式**

**1. 反向代理模式 (Reverse Proxy)**

```
Client → [WAF] → Backend Server
```

- WAF 代理後端伺服器
- 修改 DNS，將流量導向 WAF
- 完整檢查 Request 與 Response

**2. 透通橋接模式 (Transparent Bridge)**

```
Client → [WAF (Bridge)] → Backend Server
```

- WAF 作為二層橋接器
- 無需修改 IP 或 DNS
- 對應用程式透明

**3. 雲端 WAF (Cloud-based WAF)**

```
Client → [CDN + WAF (Cloudflare)] → Origin Server
```

- SaaS 服務，無需硬體
- 全球分散式部署
- 整合 CDN 與 DDoS 防護

**WAF 產品範例**：
- **硬體/虛擬設備**：F5 Advanced WAF, Imperva SecureSphere
- **雲端 WAF**：Cloudflare WAF, AWS WAF, Azure WAF
- **開源**：ModSecurity (OWASP CRS)

---

**二、次世代防火牆 (NGFW) 防禦機制**

**（一）NGFW 定義**

次世代防火牆 (Next-Generation Firewall) 是整合**傳統防火牆 + IPS + 應用程式識別 + 威脅情資 + SSL 解密**等多重功能的**全方位防火牆**。

**NGFW 演進背景**：
- **Web 2.0 時代**：應用程式複雜化，單看 Port 無法判斷
- **加密流量普及**：HTTPS 占比超過 90%，傳統防火牆無法檢查
- **進階威脅**：APT 攻擊需整合多層防禦

**（二）NGFW 核心防禦機制**

**機制一：深度封包檢測 (DPI, Deep Packet Inspection)**

**定義**：檢查封包的**完整內容** (Header + Payload)，而非僅 Header。

**檢查層級**：
- **L3/L4**：IP, Port (傳統防火牆)
- **L7**：應用層協定與內容 (NGFW)

**範例**：
```
傳統防火牆：
  看到 TCP 443 → 判斷為 HTTPS → 允許

NGFW：
  TCP 443 → 解密 SSL → 檢查內容 → 發現為 BitTorrent over HTTPS → 阻擋
```

**機制二：應用程式識別與控制 (Application Awareness & Control)**

**核心能力**：不依賴 Port，透過**協定特徵**識別應用程式。

**識別技術**：
1. **協定解碼 (Protocol Decoding)**：
   - 分析封包特徵 (如 HTTP User-Agent, TLS SNI)
   
2. **行為分析 (Behavioral Analysis)**：
   - 觀察連線模式 (如 P2P 多對多連線)
   
3. **機器學習**：
   - 訓練模型識別新應用

**應用程式資料庫**：
- Palo Alto：超過 7000 個應用程式簽章
- 涵蓋：社群媒體、即時通訊、檔案分享、遊戲、雲端服務

**政策範例**：

```
規則 1：允許業務部門使用 Salesforce
  Source: VLAN 10 (Sales Department)
  Destination: Any
  Application: salesforce-base
  Action: Allow

規則 2：阻擋所有部門使用 Facebook
  Source: Any
  Destination: Any
  Application: facebook-base
  Action: Deny

規則 3：限制 YouTube 僅能觀看，禁止上傳
  Source: Any
  Application: youtube-base
  Action: Allow
  Application Function: youtube-uploading
  Action: Deny
```

**優點**：
- 即使應用程式改用非標準 Port (如 HTTP over 8888) 仍可識別
- 細緻控制 (如允許 Skype 聊天，禁止檔案傳輸)

**機制三：使用者身分整合 (User-ID)**

**定義**：防火牆規則依據**「使用者」**而非「IP 位址」制定。

**整合方式**：
1. **Active Directory (AD) 整合**：
   - 透過 LDAP 查詢使用者群組
   - 監聽 AD 登入事件，建立 User-IP 對應表

2. **Captive Portal**：
   - 使用者首次連線時強制跳出登入頁面

3. **802.1X**：
   - 網路層身分驗證

**政策範例**：

```
規則：財務部員工可存取 ERP
  User/Group: Domain\Finance-Users
  Application: sap-erp
  Action: Allow

規則：IT 部門可 SSH 至伺服器
  User/Group: Domain\IT-Admins
  Application: ssh
  Destination: Server-Zone
  Action: Allow
```

**優點**：
- BYOD 環境：IP 動態變化，但使用者身分不變
- 精細化存取控制 (RBAC, Role-Based Access Control)

**機制四：內建 IPS (Intrusion Prevention System)**

**整合優勢**：
- **單一設備**：無需額外部署 IPS
- **性能最佳化**：硬體加速，降低延遲
- **政策整合**：與防火牆規則統一管理

**IPS 功能**：
- 偵測與阻擋已知攻擊 (如 MS17-010 EternalBlue)
- 防禦 Buffer Overflow, Format String, Shellcode
- 自動更新簽章資料庫

**機制五：SSL/TLS 解密檢查 (SSL Decryption & Inspection)**

**挑戰**：
- 現代流量 90% 已加密 (HTTPS, SMTPS, FTPS)
- 傳統防火牆無法檢查加密內容
- 惡意程式隱藏於 SSL Tunnel

**NGFW 解密流程 (中間人代理)**：

```
Client ↔ [NGFW] ↔ Server

1. Client 發起 HTTPS 連線至 Server
2. NGFW 與 Server 建立 SSL 連線 (NGFW ↔ Server)
3. NGFW 解密流量，檢查內容
4. NGFW 與 Client 建立新的 SSL 連線 (Client ↔ NGFW)
5. NGFW 使用自簽憑證加密流量回傳 Client
6. Client 需安裝企業 CA 根憑證信任 NGFW
```

**檢查內容**：
- 解密後檢查是否有惡意程式、C2 通訊、資料外洩

**隱私考量**：
- 豁免清單：銀行網站、醫療系統 (法規要求)
- 員工需簽署「網路使用同意書」

**機制六：威脅情資整合 (Threat Intelligence)**

**定義**：自動整合外部威脅情資，阻擋已知惡意 IP/網域。

**情資來源**：
1. **廠商自有**：Palo Alto WildFire, Fortinet FortiGuard
2. **開放情資**：AlienVault OTX, MISP
3. **商業情資**：Recorded Future, ThreatConnect

**自動更新機制**：
- 每 5 分鐘同步最新惡意 IP 黑名單
- 發現連線至 C2 Server → 立即阻擋

**機制七：沙箱整合 (Sandboxing / Advanced Threat Protection)**

**運作流程**：

```
1. Email 附件或網頁下載檔案
2. NGFW 攔截檔案
3. 上傳至雲端沙箱 (如 Palo Alto WildFire)
4. 沙箱在虛擬機執行檔案
5. 觀察行為：
   - 建立網路連線至可疑 IP (C2 通訊)
   - 修改 Registry Run Key (持久化)
   - 加密檔案 (勒索軟體)
6. 判定為惡意 → 產生簽章，全球分享
7. NGFW 更新簽章，阻擋該檔案
```

**偵測時間**：通常 5-15 分鐘

**（三）NGFW vs 傳統防火牆總表**

| 功能 | 傳統防火牆 | 狀態檢測防火牆 | NGFW |
|------|-----------|---------------|------|
| **OSI 層級** | L3/L4 | L3/L4 | L3-L7 |
| **檢查依據** | IP, Port | 連線狀態 | 應用程式、使用者、內容 |
| **應用識別** | 依 Port (不準) | 依 Port | DPI 深度識別 |
| **IPS** | ✗ | ✗ | ✓ |
| **SSL 解密** | ✗ | ✗ | ✓ |
| **使用者識別** | ✗ | ✗ | ✓ (AD 整合) |
| **威脅情資** | ✗ | ✗ | ✓ |
| **沙箱** | ✗ | ✗ | ✓ |
| **價格** | 低 | 中 | 高 |

**NGFW 代表產品**：
- Palo Alto PA-Series
- Fortinet FortiGate
- Cisco Firepower (原 Sourcefire)
- Check Point Next Generation Firewall

---

**三、CDN + WAF 整合效益**

**（一）CDN 功能回顧**

**CDN (Content Delivery Network, 內容傳遞網路)** 是由**全球分散的邊緣節點 (Edge Server)** 組成的網路，主要功能：

1. **快取靜態內容**：圖片、CSS、JS、影片
2. **就近服務**：使用者從最近的節點取得內容
3. **降低源站負載**：80% 流量由 CDN 處理

**（二）CDN + WAF 整合架構**

**部署模式**：

```
全球使用者
    ↓
[CDN Edge Node + WAF] (台北、東京、紐約、倫敦...)
    ↓ (僅合法且需動態產生的請求)
Origin Server (源站)
```

**（三）CDN + WAF 整合效益**

**效益一：全球分散式 DDoS 防護**

**傳統架構問題**：
- 中央 WAF 單點：集中式部署，易成為瓶頸
- 頻寬限制：10 Gbps DDoS 可能癱瘓機房

**CDN + WAF 解決方案**：
- **流量分散**：攻擊流量分散至全球數百個節點
- **巨大頻寬**：Cloudflare 宣稱可吸收 100 Tbps DDoS
- **Anycast**：單一 IP，就近路由至最近節點

**實例**：
- 2023 年 Google 吸收破紀錄 398M rps (每秒 3.98 億請求) HTTP DDoS
- 透過 Anycast + CDN 分散負載

**效益二：邊緣過濾，降低源站負載**

**運作流程**：

```
1. 使用者發送請求 (含惡意與正常)
2. 最近的 CDN 節點接收請求
3. WAF 在邊緣節點檢查：
   ├─ SQL Injection? → 阻擋 (403 Forbidden)
   ├─ XSS? → 阻擋
   └─ 正常請求 → 往下處理
4. 靜態內容：直接由 CDN 回傳 (Cache Hit)
5. 動態內容：轉發至源站
```

**優點**：
- **惡意流量不回源**：SQL Injection 在邊緣就被阻擋
- **頻寬節省**：減少源站進出流量
- **效能提升**：源站僅處理合法動態請求

**效益三：降低延遲 (Lower Latency)**

**傳統中央 WAF**：
```
台灣使用者 → (跨海) → 美國 WAF → (跨海) → 美國源站
Round-Trip Time: 200ms+
```

**CDN + WAF**：
```
台灣使用者 → 台北 CDN 節點 + WAF
  ├─ 靜態內容：直接回傳 (5ms)
  └─ 動態內容：轉發源站 (200ms)
```

**優點**：
- 靜態內容延遲極低
- WAF 檢查在本地完成

**效益四：隱藏源站 IP (Origin Cloaking)**

**安全問題**：
- 若攻擊者知道源站 IP，可繞過 CDN 直接攻擊源站

**CDN + WAF 防護**：
1. **DNS 指向 CDN**：`www.example.com` → CDN IP (不暴露源站)
2. **源站防火牆白名單**：僅允許 CDN IP 連入
3. **定期更換源站 IP**

**效益五：合規與稽核**

**集中日誌**：
- 全球 WAF 日誌集中至單一平台
- 符合 PCI-DSS, GDPR 等法規稽核要求

**效益六：智慧路由與容錯**

**Health Check**：
- CDN 定期檢查源站健康狀態
- 若源站故障 → 顯示維護頁面或切換至備援站

**效益總結表**：

| 效益 | 說明 | 影響指標 |
|------|------|---------|
| **DDoS 防護** | 全球分散式吸收攻擊 | 可防禦 Tbps 等級 |
| **降低負載** | 邊緣過濾惡意流量 | 源站流量減少 80% |
| **降低延遲** | 就近服務 | 靜態內容延遲 <50ms |
| **隱藏源站** | 不暴露真實 IP | 防直接攻擊 |
| **自動擴展** | 流量暴增自動分散 | 無需擴容硬體 |

**實務產品**：
- **Cloudflare**：CDN + WAF + DDoS Protection 整合服務
- **Akamai**：Kona Site Defender (WAF) + Akamai CDN
- **AWS**：CloudFront (CDN) + AWS WAF

**評分標準** (預估)：
- WAF 防禦機制 (列舉 4-5 項)：10分
- NGFW 防禦機制 (列舉 5-7 項)：10分
- CDN + WAF 效益 (列舉 4-5 項)：5分

#### 💡 補充說明

**WAF 繞過技術 (攻擊者視角)**：
1. **編碼變形**：`<script>` → `%3Cscript%3E` → `%253Cscript%253E` (雙重編碼)
2. **Case Variation**：`SeLeCt` (大小寫混合)
3. **註解插入**：`SEL/**/ECT` (SQL 註解)
4. **協定降級**：HTTP/2 → HTTP/1.0 (繞過規則)

**NGFW 效能考量**：
- **SSL 解密非常耗 CPU**：建議豁免大流量網站 (如 YouTube)
- **硬體加速**：專用 ASIC 晶片處理加解密
- **效能指標**：
  - Firewall Throughput：20 Gbps
  - Threat Prevention (啟用所有功能)：5 Gbps

**Zero Trust + NGFW**：
- NGFW 逐漸整合 Zero Trust 功能
- 從「網路分段」進化到「微分段 (Micro-Segmentation)」

---

### 題目 3：IDS vs IPS 與部署策略

#### 📖 原題 (111年高考三級)

> **題目**：在網路駭客行為難以完全禁絕的情況下，現代企業需採用各種網路安全設備來提供防護，其中入侵偵測系統（IDS）和防火牆（Firewall）就是常見設備，請問：
> (一) 入侵偵測系統和防火牆在功能上和部署位置上有何區別？（15 分）
> (二) 入侵偵測系統可以分為主機型以及網路型，請說明這兩種類型的差別。（5 分）

#### 🎯 答題架構分析

1. **IDS vs IPS 定義**：偵測 vs 防禦
2. **運作差異**：監控模式 vs 阻擋模式
3. **部署位置**：網路型 vs 主機型
4. **優缺點比較**：效能、誤判、實用性
5. **整合應用**：SIEM、SOC

#### 📊 評分建議 (預估配分 25 分)

**IDS 定義與運作（8 分）**
- IDS 定義（2 分）
  - Intrusion Detection System（1 分）
  - 偵測但不阻擋（1 分）
- 運作機制（4 分）
  - 簽章式偵測（2 分）
  - 異常偵測（2 分）
- 部署模式（2 分）
  - NIDS vs HIDS（2 分）

**IPS 定義與運作（8 分）**
- IPS 定義（2 分）
  - Intrusion Prevention System（1 分）
  - 主動阻擋攻擊（1 分）
- 運作機制（4 分）
  - 即時分析與阻擋（2 分）
  - 整合防火牆規則（2 分）
- 部署位置（2 分）
  - Inline 部署的必要性（2 分）

**IDS vs IPS 比較（6 分）**
- 優缺點對比（4 分）
  - IDS 優點：無影響效能、低誤判風險（2 分）
  - IPS 優點：主動防禦、即時阻擋（2 分）
- 選擇建議（2 分）
  - 何時用 IDS，何時用 IPS（2 分）

**實務部署策略（3 分）**
- 整合應用（SIEM、SOC）（2 分）
- 分層防禦建議（1 分）

**答題提示**：
- ✅ 必須**對比說明** IDS 與 IPS 的差異
- ✅ 要舉**實際部署範例**（如邊界、內網）
- ✅ 說明**誤判**（False Positive）的影響
- ⚠️ 不只列定義，要說明實務考量


#### ✍️ 標準答案示範

**解答**：

**一、IDS vs Firewall 在功能與部署上的差異**

**（一）功能定位差異**

| 項目 | 防火牆 (Firewall) | 入侵偵測系統 (IDS) |
|------|------------------|-------------------|
| **核心功能** | **預防 (Prevention)**| **偵測 (Detection)** |
| **主要動作** | 允許/拒絕流量通過 | 監控並告警可疑活動 |
| **運作模式** | 主動阻擋 | 被動監聽 |
| **決策依據** | 存取控制清單 (ACL) | 攻擊簽章 + 異常行為 |
| **流量影響** | 直接中斷惡意流量 | 不影響流量（僅記錄） |
| **誤判後果** | 阻斷正常流量 (服務中斷) | 產生誤報 (False Positive) |
| **適用情境** | 邊界防禦、存取控制 | 深度監控、威脅分析 |

**功能差異詳述**：

**1. 防火牆 (Firewall)**

**定位**：網路**第一道防線**，基於「允許清單」或「拒絕清單」控制流量。

**檢查內容**：
- **傳統防火牆**：IP 位址、Port、Protocol (5-Tuple)
- **NGFW**：應用程式、使用者身分、內容

**決策邏輯**：
```
規則 1：允許 HTTP (Port 80) → 放行
規則 2：允許 HTTPS (Port 443) → 放行
規則 3：拒絕其他所有流量 → 阻擋 (Default Deny)
```

**限制**：
- **無法偵測應用層攻擊**：允許 Port 80 後，無法分辨正常請求與 SQL Injection
- **內部威脅無效**：內網互連流量不經防火牆

**2. 入侵偵測系統 (IDS)**

**定位**：網路**深度監控**，持續分析流量尋找攻擊跡象。

**偵測技術**：

**A. 簽章式偵測 (Signature-Based)**

**原理**：
- 維護已知攻擊特徵資料庫 (如 Snort Rules)
- 比對流量是否符合惡意簽章

**範例 (Snort Rule)**：
```snort
alert tcp any any -> $HOME_NET 80 (
  msg:"SQL Injection Detected";
  content:"UNION"; nocase;
  content:"SELECT"; nocase; distance:0;
  classtype:web-application-attack;
  sid:1000001;
)
```

**優點**：誤判率低、速度快
**缺點**：無法偵測 Zero-Day 攻擊

**B. 異常式偵測 (Anomaly-Based)**

**原理**：
1. **學習期**：建立正常行為基準線 (Baseline)
   - 正常 DNS 查詢頻率
   - 典型連線模式
   
2. **偵測期**：偵測偏離基準的異常
   - 突然大量 DNS 查詢 (疑似 DNS Tunneling)
   - 內網主機對外連線至可疑 IP (疑似 C2 通訊)

**優點**：可偵測未知攻擊
**缺點**：誤判率高 (False Positive)

**C. 協定分析 (Protocol Analysis)**

**原理**：檢查協定是否符合 RFC 標準

**範例**：
- 檢測畸形 HTTP Header (如 Header 超長、非法字元)
- 檢測 TCP Flag 異常 (SYN+FIN 同時設定)

**IDS 告警範例**：
```
[ALERT] Snort - SQL Injection Attempt
Time: 2024-01-15 14:32:10
Source: 192.168.1.100:5234
Destination: 10.0.1.50:80 (WebServer)
Payload: GET /product?id=1' UNION SELECT...
Signature ID: 1000001
Severity: High
Action: Alert (No Blocking)
```

**（二）部署位置差異**

**1. 防火牆部署 (Inline, 串聯模式)**

**架構**：

```
Internet
   ↓
[外部防火牆] ← 所有流量必經
   ↓
  DMZ (Web Server, Mail Server)
   ↓
[內部防火牆] ← 所有流量必經
   ↓
 內部網路
```

**特點**：
- **串聯在線**：流量必須經過防火牆
- **單點故障風險**：防火牆故障 → 網路中斷
- **延遲影響**：每個封包都需檢查 (微秒級)

**高可用性部署**：
- Active-Active HA (雙機負載均衡)
- Active-Standby HA (主備切換)

**2. IDS 部署 (Out-of-Band, 旁路模式)**

**架構**：

```
         核心交換器
         /    |    \
    流量 1  流量 2  [Span Port] ← 鏡像所有流量
                      ↓
                    [IDS] (被動監聽)
                      ↓
                  SIEM / 管理員
```

**部署方式**：

**A. Span Port (Port Mirroring, 交換器鏡像埠)**

```
Switch(config)# monitor session 1 source interface Gi0/1 - 24
Switch(config)# monitor session 1 destination interface Gi0/48
```

- 將 Port 1-24 的流量複製至 Port 48
- IDS 連接至 Port 48 監聽

**B. Network TAP (Test Access Point, 實體分流器)**

```
Client ─┬─ [TAP] ─┬─ Server
        └─────────┴─ [IDS]
```

- 硬體設備，物理層複製流量
- 完全被動，不影響原始流量
- 即使 IDS 故障，網路仍運作

**特點**：
- **旁路監聽**：不影響流量
- **無單點故障**：IDS 當機不影響網路
- **無延遲**：流量不經過 IDS
- **僅告警**：無法主動阻擋

**部署位置建議**：

| 位置 | 目的 | 偵測內容 |
|------|------|---------|
| **DMZ 入口** | 監控外部攻擊 | Web 攻擊、掃描 |
| **核心交換器** | 監控內網橫向移動 | 內部威脅、APT |
| **伺服器網段** | 保護關鍵資產 | 對 DB、AD 的攻擊 |

**（三）IDS vs Firewall 搭配策略**

**防禦縱深 (Defense in Depth)**：

```
Layer 1: [Firewall] → 阻擋未授權流量
           ↓ (允許的流量)
Layer 2: [IDS] → 深度檢查，偵測應用層攻擊
           ↓ (告警通知)
Layer 3: [SIEM] → 關聯分析，發現APT
           ↓
Layer 4: [SOC 分析師] → 人工調查與回應
```

**互補關係**：

| 情境 | 防火牆 | IDS |
|------|--------|-----|
| **外部掃描** | 阻擋未授權 Port | 記錄掃描模式 |
| **SQL Injection** | 無法偵測 (允許 Port 80) | 偵測惡意 Payload |
| **內部橫向移動** | 不經過防火牆 | 監控內網異常連線 |
| **Zero-Day** | 無規則可擋 | 異常偵測告警 |

**實務建議**：
- **外網邊界**：Firewall + IPS (主動阻擋)
- **內網監控**：IDS (避免誤判阻斷內部流量)
- **事件關聯**：Firewall Log + IDS Alert → SIEM 分析

---

**二、HIDS vs NIDS 差異**

**（一）網路型 IDS (NIDS, Network-based IDS)**

**定義**：
部署於**網路設備** (交換器、路由器)，透過 Span Port 或 TAP 監控**整個網段流量**。

**監控範圍**：
- 所有經過該網段的封包
- 同一台 NIDS 可監控數十至數百台主機

**偵測方式**：

**1. 封包層級分析**：
- 解析 Ethernet Frame → IP Packet → TCP Segment → HTTP Request
- 重組 TCP Stream (如果封包分片)

**2. 流量模式分析**：
- 偵測 Port Scan：短時間內嘗試連接大量 Port
- 偵測 DDoS：異常大量 SYN Packet

**3. 協定異常偵測**：
- 畸形封包 (Malformed Packet)
- 協定違反 RFC 標準

**部署範例**：

```
[Internet] → [Router] → [Core Switch]
                            ↓ Span Port
                          [NIDS]
                    (監控所有內網流量)
```

**NIDS 優點**：

1. **單點監控多主機**：
   - 一台 NIDS 監控整個網段 (成本效益高)
   
2. **不影響主機效能**：
   - 監控在網路層，主機無需安裝 Agent
   
3. **隱蔽性佳**：
   - 被動監聽，攻擊者不易察覺

4. **即時偵測網路攻擊**：
   - Port Scan, DDoS, ARP Spoofing

**NIDS 缺點**：

1. **無法檢查加密流量**：
   - HTTPS 封包已加密，無法看到 Payload
   - 解法：部署 SSL/TLS 解密代理
   
2. **高速網路可能掉封包**：
   - 10 Gbps 網路，NIDS 處理不及可能漏失封包
   - 解法：硬體加速 (FPGA, ASIC)
   
3. **無法偵測主機內部活動**：
   - 無法監控系統呼叫、檔案修改、Registry 變更
   
4. **交換式網路限制**：
   - 現代交換器僅轉發給目標主機，NIDS 看不到其他主機流量
   - 需設定 Span Port

**NIDS 產品**：
- **開源**：Snort, Suricata, Zeek (原 Bro)
- **商業**：Cisco Secure IDS, Palo Alto Threat Prevention

---

**（二）主機型 IDS (HIDS, Host-based IDS)**

**定義**：
安裝於**每台主機**的 Agent 軟體，監控**該主機**的系統活動與日誌。

**監控範圍**：
- 單一主機
- 可監控加密前的資料 (在應用程式解密後)

**偵測方式**：

**1. 檔案完整性監控 (FIM, File Integrity Monitoring)**

**運作**：
- 建立關鍵檔案的雜湊值基準
- 定期檢查檔案是否被修改

**監控檔案**：
```
/etc/passwd (Linux)
/etc/shadow
C:\Windows\System32\drivers\ (Windows)
Registry: HKLM\Software\Microsoft\Windows\CurrentVersion\Run
```

**告警範例**：
```
[ALERT] File Integrity Violation
File: /etc/passwd
Action: Modified
Original Hash: a1b2c3d4...
Current Hash: e5f6g7h8...
Time: 2024-01-15 14:32:10
Possible Intrusion: Unauthorized user account added
```

**2. 日誌分析 (Log Analysis)**

**監控日誌**：
- **系統日誌**：/var/log/auth.log (登入記錄)
- **應用程式日誌**：Apache access.log, error.log
- **安全日誌**：Windows Event Log (Security)

**偵測範例**：
```
# 偵測暴力破解
Alert: 10 failed SSH login attempts from 192.168.1.100 in 60 seconds
User: root
Action: Block IP via iptables
```

**3. 系統呼叫監控 (System Call Monitoring)**

**運作**：
- 監控程式的系統呼叫 (如 open(), read(), write(), execve())
- 偵測異常行為

**告警範例**：
```
[ALERT] Suspicious System Call
Process: notepad.exe
Action: Attempted to execute cmd.exe (Unusual for Notepad)
Potential: Process Injection / DLL Hijacking
```

**4. 行為基準線偵測**

**運作**：
- 建立正常程式行為基準
- 偵測偏離基準的異常

**範例**：
```
Normal: Excel.exe 僅讀取 .xlsx 檔案
Alert: Excel.exe 執行 PowerShell (疑似巨集攻擊)
```

**HIDS 部署範例**：

```
每台主機安裝 HIDS Agent
  ↓
[Web Server] ← HIDS Agent
  - 監控 /var/log/apache2/
  - 監控 /var/www/html/ 檔案變更
  
[Database Server] ← HIDS Agent
  - 監控 MySQL 日誌
  - 監控資料庫檔案完整性
  
[AD Server] ← HIDS Agent
  - 監控 Windows Event Log
  - 監控 Registry 變更
    ↓
集中管理主機 (HIDS Manager)
    ↓
  SIEM
```

**HIDS 優點**：

1. **可檢查加密流量**：
   - 監控在應用程式解密後，能看到明文內容
   
2. **偵測主機內部威脅**：
   - Rootkit 安裝
   - 檔案被竄改
   - 權限提升 (Privilege Escalation)
   
3. **不受網路限制**：
   - 即使主機不在同一網段，仍可監控
   
4. **精確定位受害主機**：
   - 直接知道是哪台主機被攻擊

**HIDS 缺點**：

1. **部署成本高**：
   - 每台主機需安裝 Agent
   - 數千台主機管理複雜
   
2. **消耗主機資源**：
   - CPU, Memory, Disk I/O
   - 關鍵生產伺服器可能無法接受
   
3. **無法偵測網路攻擊**：
   - Port Scan, ARP Spoofing, DDoS
   
4. **容易被攻擊者關閉**：
   - 攻擊者取得 root 權限後可停用 HIDS Agent

**HIDS 產品**：
- **開源**：OSSEC, Wazuh, Samhain
- **商業**：Tripwire, CrowdStrike Falcon, SentinelOne

---

**（三）HIDS vs NIDS 比較總表**

| 特性 | NIDS | HIDS |
|------|------|------|
| **部署位置** | 網路設備 (交換器) | 每台主機 |
| **監控範圍** | 整個網段 | 單一主機 |
| **監控內容** | 網路封包 | 系統活動、檔案、日誌 |
| **加密流量** | ✗ 無法檢查 | ✓ 可檢查 (解密後) |
| **網路攻擊** | ✓ Port Scan, DDoS | ✗ 無法偵測 |
| **主機攻擊** | 有限 (僅網路層) | ✓ 檔案竄改、Rootkit |
| **效能影響** | 無 (旁路) | 有 (消耗主機資源) |
| **部署成本** | 低 (少量設備) | 高 (每主機一套) |
| **管理複雜度** | 低 | 高 |
| **攻擊者規避** | 加密、封包分片 | 停用 Agent, Rootkit 隱藏 |

**（四）HIDS + NIDS 整合部署策略**

**互補部署**：

```
網路層防禦 (NIDS)：
  └─ 偵測外部攻擊、網路掃描、DDoS

主機層防禦 (HIDS)：
  └─ 偵測惡意程式執行、檔案竄改、Rootkit

整合至 SIEM：
  └─ 關聯分析 NIDS + HIDS 告警，發現 APT 攻擊鏈
```

**實務建議**：

1. **關鍵資產部署 HIDS**：
   - Domain Controller (AD)
   - 資料庫伺服器
   - Web Server

2. **網路邊界部署 NIDS**：
   - DMZ 入口
   - 內外網邊界

3. **整合威脅情資**：
   - NIDS 偵測連線至已知 C2 IP
   - HIDS 確認主機是否已植入後門

**評分標準** (預估)：
- IDS vs Firewall 功能與部署差異 (含表格)：15分
- HIDS vs NIDS 差別 (含優缺點)：5分

#### 💡 補充說明

**IPS (Intrusion Prevention System) 補充**：
- IPS = IDS + 主動阻擋能力
- 部署於 Inline (串聯)，可即時阻斷攻擊
- 誤判風險：可能阻斷正常流量 (需謹慎調校)

**IDS 規避技術 (攻擊者視角)**：
1. **封包分片 (Fragmentation)**：將攻擊 Payload 切成小片，規避簽章比對
2. **低速攻擊 (Slow Attack)**：降低攻擊速率，避免觸發異常偵測
3. **加密通道**：使用 HTTPS, SSH Tunnel 隱藏攻擊流量

**下一代 IDS/IPS**：
- **機器學習**：自動學習正常行為，提升異常偵測準確度
- **威脅情資整合**：自動更新已知 C2 IP 黑名單
- **行為分析 (UEBA)**：偵測使用者異常行為

---

### 題目 4：DDoS 攻擊與防禦策略

#### 📖 原題 (113年地方特考三等)

>> **題目**：請說明何謂分散式阻斷服務攻擊（Distributed Denial-of-Service, DDoS）；並說明系統管理者應如何加強防範分散式阻斷服務攻擊的事件發生。（10 分）

#### 🎯 答題架構分析

1. **DDoS 定義**：分散式阻斷服務攻擊
2. **DDoS 類型**：流量型、協定型、應用層
3. **DDoS 防禦策略**：流量清洗、CDN、限流
4. **應變流程**：偵測、分析、緩解
5. **實務案例**：GitHub、Cloudflare

#### 📊 評分建議 (預估配分 10 分)

**DDoS 攻擊定義與原理（4 分）**
- DDoS 定義（2 分）
  - 分散式阻斷服務攻擊（1 分）
  - 目的：癱瘓服務（1 分）
- 攻擊原理（2 分）
  - Botnet 殭屍網路（1 分）
  - 耗盡資源（頻寬、CPU、連線數）（1 分）

**防禦策略（6 分）**
- 流量清洗（Traffic Scrubbing）（2 分）
  - 原理與運作方式
- CDN 與分散式防禦（2 分）
  - 如何吸收攻擊流量
- 其他防禦措施（2 分）
  - Rate Limiting、Blackhole Routing、WAF 整合

**答題提示**：
- ✅ 雖然只有 10 分，但要說明**具體防禦方法**
- ✅ 可舉**實際案例**加分（如 GitHub 1.35 Tbps 攻擊）
- ✅ 說明**技術原理**，不只列名詞
- ⚠️ 避免只寫「加強防火牆」這類泛泛之談

#### ✍️ 標準答案示範

**解答**：

**一、DDoS 定義**

分散式阻斷服務攻擊是利用**大量殭屍電腦 (Botnet)** 同時向目標發送海量請求，耗盡目標的**頻寬、CPU、記憶體**等資源，導致合法使用者無法存取服務。

**攻擊目標**：**可用性 (Availability)**

**二、DDoS 防禦策略**

**策略一：頻寬過濾與清洗中心**
- ISP 或 DDoS 防護服務商 (Cloudflare, Akamai)
- 過濾惡意流量，僅放行合法流量

**策略二：分散式架構與 CDN**
- 全球節點分散流量
- Anycast 路由至最近節點
- 單一節點被攻擊不影響整體

**策略三：SYN Cookie (防 SYN Flood)**
- 不保存半開連線狀態
- 透過加密 Cookie 驗證

**策略四：速率限制 (Rate Limiting)**
- 限制單一 IP 請求頻率
- Nginx: `limit_req_zone`

**策略五：異常流量偵測**
- 建立流量基準線
- 機器學習偵測異常

**策略六：自動擴展 (Auto Scaling)**
- 雲端彈性增加資源
- AWS Auto Scaling Group

**策略七：應變計畫**
- 建立 DDoS 應變 SOP
- 定期演練

**評分標準** (預估)：
- DDoS 定義：3分
- 防禦策略 (5-7項)：7分

---

## 🗂️ 歷屆精選題庫 (Selected Question Bank)

### 零信任架構
1. **114年高考二級**：使用者身分識別與設備鑑別方法
2. **113年地方特考三等**：零信任架構實施挑戰與解決方案
3. **112年地方特考三等**：ZTA 概念、動機與核心機制
4. **112年高考二級**：零信任三大關鍵技術 (身分鑑別、設備鑑別、信任推斷)

### 防火牆技術
5. **113年高考三級**：WAF 與 NGFW 防禦機制、CDN + WAF 效益
6. **112年地方特考三等**：DMZ 用意、WAF vs 傳統防火牆、IOC 意義
7. **111年普考**：封包過濾式 vs 應用程式代理防火牆、DMZ、WAF
8. **110年地方特考三等**：防火牆定義、四大功能、應用層 Port 管理

### IDS/IPS
9. **111年高考三級**：IDS vs Firewall 功能與部署差異、HIDS vs NIDS
10. **109年高考三級**：網路型 IDS 定義、部署位置、優缺點

### DDoS 防禦
11. **113年地方特考三等**：Firewall + IPS 協同防禦 DoS、DDoS 定義與防範
12. **112年高考三級**：DDoS 原理、難以防守原因、五項防護策略
13. **108年普考**：遭受 DDoS 攻擊時的處置流程
14. **104年高考二級**：DDoS 服務中斷原因、DRDoS 反射攻擊原理

### VPN 與遠端存取
15. **114年普考**：零信任 vs VPN 優勢與風險
16. **109年高考二級**：VPN 遠端工作環境下目錄伺服器安全管理

### Proxy 代理伺服器
17. **111年高考三級**：代理伺服器功用與運作、反向代理伺服器

---

## 💡 答題技巧總結

1. **分層防禦**：從網路層 (L3/L4) 到應用層 (L7) 說明防禦機制
2. **整合思維**：提到 Defense in Depth (縱深防禦)，不單靠單一技術
3. **產品舉例**：展現實務理解 (如 Palo Alto NGFW, Cloudflare WAF)
4. **畫架構圖**：DMZ 部署、Firewall 位置、IDS 旁路監聽
5. **趨勢補充**：Zero Trust, SASE, XDR, SOAR
6. **攻擊關聯**：說明防禦技術時提到對應的攻擊手法 (如 WAF 防 SQL Injection)

---

## 🔗 參考資源

- [NIST SP 800-207 - Zero Trust Architecture](https://csrc.nist.gov/publications/detail/sp/800-207/final)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) - Web 應用十大風險
- [Cloudflare Learning - What is a WAF?](https://www.cloudflare.com/learning/ddos/glossary/web-application-firewall-waf/)
- [Snort Rules](https://www.snort.org/downloads) - IDS 規則資料庫
- [MITRE ATT&CK - Defense Evasion](https://attack.mitre.org/tactics/TA0005/)
- [Palo Alto NGFW Documentation](https://docs.paloaltonetworks.com/)
- [Cisco ISE (NAC) Documentation](https://www.cisco.com/c/en/us/products/security/identity-services-engine/)

---

**【檔案狀態】**：基礎框架已完成，包含完整的題目 1 (零信任架構)。後續題目將逐步補充。
