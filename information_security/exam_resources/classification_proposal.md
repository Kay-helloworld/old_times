# 資通安全考題分類與關鍵字分析提案

## 1. 分類邏輯說明

經檢視 104 年至 114 年（含預測/模擬）之「資訊管理與資通安全」、「資通網路與安全」等考題，發現題目範疇廣泛，涵蓋了傳統的**資訊網路**、**資訊安全**技術，以及**資訊管理**與**新興科技**議題。

為了解決舊有分類邏輯錯誤的問題，本提案將考題重新歸納為 **8 大主題**。此分類方式不侷限於狹義的資安，而是將相關聯的基礎建設、管理制度與應用層面一併納入，以符合「複合型」與「時事型」考題的特性。

---

## 2. 建議分類架構與關鍵字

### 第一類：網路通訊原理 (Network Communication Principles)
此類別包含網路運作的基礎設施、協定與架構。
*   **核心關鍵字**: OSI Model, TCP/IP, UDP, IPv4/IPv6, Subnetting (子網路切割), DNS, DHCP, NAT, ARP, ICMP.
*   **路由與交換**: Routing Protocols (OSPF, BGP), Switching, VLAN, STP/RSTP.
*   **無線與行動網路**: 802.11 (Wi-Fi), 4G/5G, Mobile Networks, RFID, NFC.
*   **新興網路架構**: SDN (軟體定義網路), NFV, IoT (物聯網基礎傳輸).

### 第二類：資訊安全基礎與密碼學 (InfoSec Fundamentals & Cryptography)
此類別包含資安的核心理論與加密技術。
*   **資安三要素**: CIA (機密性、完整性、可用性), Non-repudiation (不可否認性).
*   **身分鑑別與存取控制**: Authentication (Biometrics, MFA, OTP), Authorization, Access Control Models (DAC, MAC, RBAC).
*   **密碼學技術**: Symmetric Encryption (AES, DES), Asymmetric Encryption (RSA, ECC), Hash Functions (SHA, MD5), Digital Signatures (數位簽章).
*   **金鑰管理**: PKI (公開金鑰基礎建設), Digital Certificates (數位憑證), SSL/TLS, Key Exchange (Diffie-Hellman).

### 第三類：網路安全與防禦技術 (Network Security & Defense)
此類別側重於防禦網路攻擊的設備與架構設計。
*   **防禦設備**: Firewall (Packet Filtering, Proxy, NGFW), IDS/IPS (入侵偵測/防禦), WAF (網頁應用程式防火牆), VPN (IPSec, SSL VPN).
*   **防禦架構**: DMZ, Honeypot (誘捕系統), Sandbox (沙箱), Network Segmentation.
*   **新興防禦概念**: Zero Trust Architecture (零信任架構), Micro-segmentation.
*   **攻擊緩解**: DDoS Defense, Traffic Analysis.

### 第四類：應用系統與網頁安全 (Application & Web Security)
此類別專注於軟體開發與網頁應用層面的安全。
*   **常見漏洞**: OWASP Top 10, SQL Injection, XSS (Cross-Site Scripting), CSRF, SSRF, Buffer Overflow.
*   **安全開發**: SSDLC (安全軟體開發生命週期), DevSecOps, Code Review (Static/Dynamic Analysis), Threat Modeling.
*   **資料庫安全**: Database Security, Inference, Aggregation.

### 第五類：惡意程式與攻擊手法 (Malware & Attack Vectors)
此類別分析駭客的攻擊手段與惡意軟體特性。
*   **惡意軟體**: Ransomware (勒索軟體), Virus, Worm, Trojan, Rootkit, Botnet.
*   **攻擊手法**: APT (進階持續性滲透攻擊), Zero-day Attack (零時差攻擊), Man-in-the-Middle (中間人攻擊), Replay Attack.
*   **社交工程**: Phishing (網路釣魚), Spear Phishing, Whaling, Social Engineering.

### 第六類：資安管理、法規與鑑識 (Security Management, Law & Forensics)
此類別涵蓋管理層面、合規性與事後調查。
*   **管理標準**: ISO 27001, ISMS (資訊安全管理制度), PDCA.
*   **風險管理**: Risk Assessment (Asset, Threat, Vulnerability), BIA (營運衝擊分析), BCP (營運持續計畫), DRP (災難復原計畫).
*   **法規與倫理**: 資通安全管理法, 個人資料保護法 (GDPR), 資訊倫理 (PAPA).
*   **數位鑑識**: Digital Forensics, Chain of Custody (監管鏈), Evidence Collection, Network Forensics.
*   **事件應變**: Incident Response (IR) Process, SIEM, SOC.

### 第七類：新興科技與雲端安全 (Emerging Tech & Cloud Security)
此類別探討新技術帶來的機會與安全挑戰。
*   **雲端運算**: Cloud Computing (NIST Definition), Service Models (IaaS, PaaS, SaaS), Deployment Models (Public, Private, Hybrid), Virtualization (VM vs Container), Cloud Security.
*   **區塊鏈與金融科技**: Blockchain, Smart Contracts, Fintech, Cryptocurrency.
*   **人工智慧**: AI Security, Machine Learning (Adversarial Attacks), Deepfake.
*   **其他**: Quantum Computing (Post-Quantum Cryptography).

### 第八類：資訊系統與管理 (Information Systems & Management)
此類別針對「資訊管理」考科中非純資安的議題（因考卷常合併出題）。
*   **資料管理**: Big Data (5V), Data Mining, Data Warehouse, Knowledge Management (KM).
*   **企業系統**: ERP, CRM, SCM, BI (商業智慧).
*   **系統開發與專案**: SDLC (Waterfall, Agile, DevOps), Project Management.
*   **電子商務**: E-Commerce Models (B2B, B2C, O2O), Digital Marketing.

---

## 3. 考題歸類範例 (Sample Mapping)

為驗證此分類的有效性，以下隨機抽取部分考題進行試歸類：

| 年份 | 考題代號 | 題目摘要 | 建議分類 | 關鍵字 |
| :--- | :--- | :--- | :--- | :--- |
| 104 | 104080_1512_Q1 | NIST 雲端運算五大特徵 | **7. 新興科技與雲端安全** | Cloud Computing, NIST |
| 104 | 104080_1512_Q3 | 網路鑑識與數位證據 | **6. 資安管理、法規與鑑識** | Network Forensics, Digital Evidence |
| 104 | 104080_1512_Q4 | 數位憑證與 Diffie-Hellman | **2. 資安基礎與密碼學** | Digital Certificate, Key Exchange |
| 105 | 105080_1612_Q4 | APT 攻擊流程與因應 | **5. 惡意程式與攻擊手法** | APT, Incident Response |
| 106 | 106090_1327_Q4 | 瀏覽器 SSL 檢查與 XSS | **4. 應用系統與網頁安全** | SSL, XSS, Browser Security |
| 107 | 107090_1511_Q3 | 物聯網 (IoT) 服務與攻擊防範 | **7. 新興科技與雲端安全** | IoT, Security |
| 108 | 108090_1512_Q3 | DDoS 攻擊處置 | **3. 網路安全與防禦技術** | DDoS, Incident Response |
| 109 | 109090_1510_Q3 | Stored vs Reflected XSS | **4. 應用系統與網頁安全** | XSS |
| 110 | 110090_1226_Q1 | 資通安全事件通報應變 | **6. 資安管理、法規與鑑識** | Incident Response, Law |
| 111 | 111090_2619_Q1 | TCP/IP 與 3-way handshake | **1. 網路通訊原理** | TCP, Handshake |
| 112 | 112200_2705_Q4 | 零信任架構 (ZTA) | **3. 網路安全與防禦技術** | Zero Trust |
| 113 | 113200_2106_Q3 | SQL Injection 與 Prepared Statements | **4. 應用系統與網頁安全** | SQL Injection |
| 114 | 114040_1206_Q2 | OWASP IoT Top 10 | **7. 新興科技與雲端安全** | IoT, OWASP |

## 4. 後續執行建議

若您同意此分類方式，後續將進行以下作業：
1.  建立對應的資料夾結構（或 Markdown 檔案結構）。
2.  撰寫自動化腳本，依據上述關鍵字將所有考題自動歸檔至對應類別。
3.  針對每個類別產出彙整後的考題集，供您複習使用。
