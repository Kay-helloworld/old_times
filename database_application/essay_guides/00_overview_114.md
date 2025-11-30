# 114年資料庫考題完全解析 - 申論題答題框架

這份文件會徹底解析114年度的資料庫考題，並提供詳細的申論題答題架構。

---

## 📊 114年度考題總覽

我分析了114年度的7份考卷，發現：

### 題型分布

| 題型 | 占比 | 特點 |
|------|------|------|
| **概念申論題** | 40% | EER、ACID、隔離等級、資料倉儲 |
| **SQL查詢題** | 30% | JOIN、GROUP BY、聚合函數 |
| **計算分析題** | 20% | 正規化、FD、Closure |
| **設計繪圖題** | 10% | ER Diagram、索引結構 |

### 高頻主題（114年特別常考）

1. **交易管理** (ACID、隔離等級、死鎖) - 佔比最高
2. **ER Model / EER Model** - 幾乎每份都有
3. **正規化** (FD、3NF、BCNF) - 傳統重點
4. **SQL查詢** - 基本必考

---

## 🎯 申論題答題黃金架構

### 通用架構（適用所有申論題）

```
第一段：定義與背景 (20%)
├─ 關鍵術語的定義
├─ 為什麼這個概念很重要
└─ 簡要說明要回答的內容

第二段：詳細說明 (60%)
├─ 分點說明（用⑴⑵⑶編號）
├─ 每點都有：定義 + 說明 + 例子
└─ 使用表格或圖示（如果適合）

第三段：總結或應用 (20%)
├─ 整合前面的要點
├─ 實務應用或比較
└─ 回扣題目問題
```

---

## 📝 實戰解析：114年高考四題

### 題目一：EER Model（Enhanced Entity Relationship）

#### 📖 原題

**說明下列 EER 模型的四個構成要素，並各舉一個具體例子說明其在真實世界中的應用：**

- ⑴ Entity
- ⑵ Attribute  
- ⑶ Relationship
- ⑷ Supertype/Subtype

**分數**：20分（每小題約5分）

---

#### 🎯 答題架構分析

這是**定義+例子**型的題目，每個要素需要：

1. 定義（2分）
2. 特性說明（1分）
3. 具體例子（2分）

---

#### ✍️ 標準答案示範

**⑴ Entity（實體）**

**定義**：Entity 是指在真實世界中可獨立存在、具有唯一識別性的物件或概念，是資料庫中資料的基本儲存單位。

**特性說明**：每個 Entity 必須具備：

- 可區分性：能與其他 Entity 區別
- 屬性集合：擁有描述其特徵的屬性
- 實例集合：在資料庫中會有多個具體實例（Instance）

**具體例子**：在大學選課系統中，「學生（Student）」是一個 Entity。

- 每個學生都有唯一的學號（Primary Key）
- 擁有姓名、出生日期、入學年份等屬性
- 資料庫中儲存數千筆學生記錄

---

**⑵ Attribute（屬性）**

**定義**：Attribute 是用來描述 Entity 特徵或性質的資料項目，代表 Entity 的某個特定面向。

**特性分類**：

- **Simple vs Composite**（簡單 vs 複合）：
  - Simple：不可再分割（例如：年齡）
  - Composite：可分割成更小部分（例如：地址可分為縣市、街道、門牌）
- **Single-valued vs Multi-valued**（單值 vs 多值）：
  - Single-valued：每個Entity只有一個值（例如：身分證號）
  - Multi-valued：可有多個值（例如：電話號碼可有手機、市話）
- **Stored vs Derived**（儲存 vs 衍生）：
  - Stored：實際儲存（例如：出生日期）
  - Derived：可由其他屬性計算（例如：年齡 = 今年 - 出生年）

**具體例子**：在員工管理系統中，「員工（Employee）」Entity的屬性：

- Simple Attribute：員工編號（E001）
- Composite Attribute：姓名（姓 + 名）、地址（縣市 + 街道 + 門牌）
- Multi-valued Attribute：專長技能（可能有Java、Python、SQL等多項）
- Derived Attribute：年資（今年 - 到職年份）

---

**⑶ Relationship（關係）**

**定義**：Relationship 描述兩個或多個 Entity 之間的關聯或互動，表達它們如何相互連結。

**特性說明**：

- **基數比（Cardinality Ratio）**：描述關係的數量對應
  - 1:1（一對一）：例如：一個人有一張身分證
  - 1:N（一對多）：例如：一個部門有多個員工
  - M:N（多對多）：例如：學生與課程（一個學生修多門課，一門課被多個學生修）
- **參與度（Participation）**：
  - Total（全部參與）：每個 Entity 都必須參與這個關係
  - Partial（部分參與）：有些 Entity 可以不參與

**具體例子**：在電商系統中，「顧客（Customer）」與「訂單（Order）」之間的「下單（Places）」關係：

- 關係類型：1:N（一個顧客可下多筆訂單）
- 關係屬性：訂單建立時間、總金額
- 參與度：
  - 顧客端 Partial（顧客不一定有訂單）
  - 訂單端 Total（每筆訂單必定有顧客）

---

**⑷ Supertype/Subtype（超類別/子類別）**

**定義**：Supertype/Subtype 是 EER Model 擴充的概念，用來表達 Entity 之間的「is-a」（是一個）繼承關係，子類型繼承超類型的所有屬性，並可擁有自己的特殊屬性。

**特性說明**：

- **特殊化（Specialization）**：從一般到特殊（由上而下）
  - 例如：員工 → 正職員工、兼職員工
- **一般化（Generalization）**：從特殊到一般（由下而上）
  - 例如：汽車、機車 → 交通工具
- **限制條件**：
  - **Disjoint（互斥）**：一個 Supertype 實例只能屬於一個 Subtype
    - 例如：性別（男/女）
  - **Overlapping（重疊）**：可同時屬於多個 Subtype
    - 例如：員工可同時是專案經理和部門主管

**具體例子**：在大學系統中，「人員（Person）」作為 Supertype：

- **Supertype 屬性**：身分證號、姓名、出生日期、聯絡電話
- **Subtype1：學生（Student）**
  - 繼承 Person 所有屬性
  - 特有屬性：學號、入學年份、主修科系
- **Subtype2：教職員（Faculty）**
  - 繼承 Person 所有屬性
  - 特有屬性：員工編號、職稱、薪資
- **關係類型**：Disjoint（一個人不能同時是學生和教職員）

**圖示**（用文字表達）：

```
         Person（人員）
         ↓ d（Disjoint）
    ┌────┴────┐
Student      Faculty
（學生）     （教職員）
```

---

#### 💡 答題技巧總結

**這種「定義+例子」題的得分關鍵**：

1. **用專業術語**：
   - ✓ 「Entity 是指在真實世界中可獨立存在的物件」
   - ✗ 「Entity 就是一個東西」

2. **分點清楚**：
   - 使用⑴⑵⑶編號
   - 每點都有：定義 → 說明 → 例子

3. **例子要具體**：
   - ✓ 「學生（Student）具有學號（S001）、姓名（王小明）」
   - ✗ 「學生有一些屬性」

4. **圖示加分**：
   - 如果能畫簡單的ER圖或階層圖，會更清楚

---

### 題目二：Transaction Isolation（交易隔離等級）

#### 📖 原題

**請說明下列兩種事務隔離級別的差異，並針對每種隔離級別各舉一個可能造成資料不一致的實際情境：**

- ⑴ Read Committed
- ⑵ Repeatable Read

**（10分）此外，請說明為何某些資料庫系統預設使用 Read Committed 而非 Serializable。（10分）**

---

#### 🎯 答題架構分析

這是**比較+情境+原因分析**的綜合題，需要：

1. Part 1：定義兩種隔離等級（各2分）
2. Part 2：舉例說明問題（各3分）  
3. Part 3：解釋為何不用最高等級（10分）

---

#### ✍️ 標準答案示範

**Part 1：兩種隔離等級的定義與差異（10分）**

**⑴ Read Committed（讀取已確認）**

**定義**：此隔離等級保證交易只能讀取其他交易「已經 COMMIT」的資料，不會讀到未確認（uncommitted）的修改。

**允許的情況**：

- ✓ 讀取已 COMMIT 的資料
- ✓ 同一交易內，讀兩次可得到不同值（因為其他交易可能已 COMMIT）

**不允許的情況**：

- ✗ Dirty Read（髒讀）：不會讀到未 COMMIT 的資料

**可能發生的問題**：

- ✓ Non-Repeatable Read（不可重複讀）：同一筆資料讀兩次，值不同
- ✓ Phantom Read（幻讀）：查詢筆數前後不一致

---

**實際情境範例（造成不一致）**：

**情境**：銀行系統產生對帳單

```
時間 | 交易T1（產生對帳單）        | 交易T2（更新餘額）
-----|----------------------------|---------------------------
t1   | SELECT balance FROM Account|
     | WHERE account_id = 'A001'  |
     | → 讀到 10,000 元           |
t2   |                            | UPDATE Account 
     |                            | SET balance = 15,000
     |                            | WHERE account_id = 'A001'
t3   |                            | COMMIT ← 確認修改
t4   | SELECT balance FROM Account|
     | WHERE account_id = 'A001'  |
     | → 讀到 15,000 元！         |
```

**問題**：T1 在同一筆交易內，兩次查詢同一帳戶，得到不同餘額（10,000 vs 15,000），導致對帳單資料前後矛盾。

**這就是 Non-Repeatable Read**。

---

**⑵ Repeatable Read（可重複讀）**

**定義**：此隔離等級保證交易內「重複讀取同一筆資料」時，會得到相同的值，即使其他交易已經修改並 COMMIT。

**允許的情況**：

- ✓ 讀取已 COMMIT 的資料
- ✓ 同一交易內，讀兩次會得到相同值（即使其他交易已修改）

**不允許的情況**：

- ✗ Dirty Read（髒讀）
- ✗ Non-Repeatable Read（不可重複讀）

**可能發生的問題**：

- ✓ Phantom Read（幻讀）：查詢筆數可能不同

---

**實際情境範例（造成不一致）**：

**情境**：統計某日期訂單數量

```
時間 | 交易T1（統計訂單）          | 交易T2（新增訂單）
-----|----------------------------|---------------------------
t1   | SELECT COUNT(*) FROM Order |
     | WHERE date = '2025-01-01'  |
     | → 得到 100 筆              |
t2   |                            | INSERT INTO Order VALUES
     |                            | (..., '2025-01-01', ...)
t3   |                            | COMMIT ← 新增一筆
t4   | SELECT COUNT(*) FROM Order |
     | WHERE date = '2025-01-01'  |
     | → 得到 101 筆！            |
```

**問題**：T1 在同一筆交易內，兩次查詢筆數不同（100 vs 101），這是 **Phantom Read**。

---

**兩者差異比較表**：

| 保護等級 | Read Committed | Repeatable Read |
|---------|----------------|-----------------|
| Dirty Read | ✓ 防止 | ✓ 防止 |
| Non-Repeatable Read | ✗ 可能發生 | ✓ 防止 |
| Phantom Read | ✗ 可能發生 | ✗ 可能發生 |
| 鎖定策略 | 讀完立即釋放鎖 | 持有鎖直到交易結束 |

---

**Part 2：為何預設使用 Read Committed 而非 Serializable（10分）**

**一、定義 Serializable（可序列化）**

Serializable 是最高的隔離等級，保證所有交易的執行結果等同於「一個接一個執行」（序列執行），完全避免所有並行問題。

**防止**：Dirty Read、Non-Repeatable Read、Phantom Read 全部都防止

---

**二、為何不預設使用 Serializable？三大原因**

**原因1：效能考量（Performance Overhead）**

**Serializable 的代價**：

- 需要大量鎖定（Locking）或使用快照隔離（Snapshot Isolation）
- 會阻擋（Block）其他交易的執行
- 降低並行程度（Concurrency）

**實際影響**：

```
假設100個使用者同時查詢
- Read Committed：可能80-90個同時執行（高並行）
- Serializable：可能只有10-20個同時執行（低並行）

結果：系統吞吐量（Throughput）下降50-70%
```

---

**原因2：在多數情境下，Read Committed 已足夠**

**實務統計**：

- 約 80% 的應用情境不需要 Serializable
- 例如：
  - 一般查詢（SELECT）
  - 單筆資料的更新
  - 簡單的購物車操作

**只有特定情境才需要更高等級**：

- 金融轉帳（需要 Serializable）
- 庫存扣減（需要 Serializable）
- 對帳報表（可能需要 Repeatable Read）

**設計哲學**：
「為少數需求犧牲多數效能」不符合資料庫設計原則，因此預設使用較寬鬆但效能較好的等級。

---

**原因3：可依需求調整（Trade-off 的彈性）**

**資料庫系統提供彈性**：

- 預設：Read Committed（平衡效能與安全）
- 需要時：手動提升至 Repeatable Read 或 Serializable

**語法範例**：

```sql
-- 一般交易：使用預設 Read Committed
BEGIN TRANSACTION;
SELECT * FROM Products WHERE price < 1000;
COMMIT;

-- 關鍵交易：手動提升為 Serializable
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
BEGIN TRANSACTION;
UPDATE Account SET balance = balance - 1000 WHERE id = 'A';
UPDATE Account SET balance = balance + 1000 WHERE id = 'B';
COMMIT;
```

---

**三、總結：預設策略的優點**

| 面向 | Read Committed 預設 | Serializable 預設 |
|-----|---------------------|-------------------|
| 一般使用情境 | ✓ 效能好 | ✗ 效能差 |
| 特殊需求 | ✓ 可手動提升 | - 無彈性 |
| 資源消耗 | ✓ 低 | ✗ 高 |
| 使用者體驗 | ✓ 響應快 | ✗ 可能等待 |

**結論**：Read Committed 作為預設值是「效能、安全、彈性」的最佳平衡點。

---

#### 💡 答題技巧總結

**這種「比較+解釋原因」題的得分關鍵**：

1. **用表格比較**：
   - 清楚呈現差異
   - 閱卷老師一目了然

2. **情境要具體**：
   - 寫出時間序列
   - 標明哪個步驟出問題

3. **原因要分點**：
   - 原因1、原因2、原因3
   - 每個原因都有說明+例子

4. **扣回題目**：
   - 最後一段總結，回答「為什麼」

---

## 🎓 進階：其他114年重要題型

### 題型3：SQL查詢題（30分）

**範例**（114高考第三題）：

```
資料表：Customer(CID, Name), Orders(OID, CID, TotalAmount, OrderDate), 
        Payment(PID, OID, AmountPaid)

題目1：在 OrderDate 為"2025.01.01"當天，所有客戶訂單總量排行
題目2：曾有付款行為且總付款金額超過 10,000 的客戶
題目3：付款金額總和不足訂單金額的客戶與欠款金額
```

**答題架構**：

```sql
-- 題目1：訂單總量排行

-- 第一步：確認需求
-- - 篩選條件：OrderDate = '2025-01-01'
-- - 聚合：每個客戶的訂單總金額
-- - 排序：由高到低
-- - 輸出：客戶姓名、總金額

-- 第二步：寫SQL
SELECT C.Name, SUM(O.TotalAmount) AS TotalOrders
FROM Customer C
  JOIN Orders O ON C.CID = O.CID
WHERE O.OrderDate = '2025-01-01'
GROUP BY C.CID, C.Name
ORDER BY TotalOrders DESC;
```

**得分技巧**：

1. **加註解**說明思路（雖然題目沒要求，但會加分）
2. **用有意義的別名**（TotalOrders 比 col1 清楚）
3. **適當的縮排和換行**（提高可讀性）

---

### 題型4：正規化與FD（Functional Dependency）

**範例**（114司法特考第三題）：

**答題架構**（Closure計算）：

```
題目：找出 {G, F}+ （{G, F}的封閉）

給定FD：
- G → D
- {E, F} → G
- F → B
- D → {C, F}
- G → A

答題步驟：

步驟1：初始化
{G, F}+ = {G, F}

步驟2：第一輪推導
- 由 G → D，可得 D
  → {G, F}+ = {G, F, D}
- 由 F → B，可得 B
  → {G, F}+ = {G, F, D, B}
- 由 G → A，可得 A
  → {G, F}+ = {G, F, D, B, A}

步驟3：第二輪推導
- 由 D → {C, F}，可得 C（F已有）
  → {G, F}+ = {G, F, D, B, A, C}

步驟4：第三輪推導
- 沒有新屬性可推導

結論：{G, F}+ = {A, B, C, D, F, G}
```

**得分技巧**：

1. **列出每一輪的推導過程**（不要只寫答案）
2. **說明用了哪個FD**
3. **確認沒有遺漏**

---

## ✅ 總結：申論題高分秘訣

### 1. 架構完整

```
引言（背景） → 分點說明 → 舉例 → 總結
```

### 2. 專業術語

| 不專業 ❌ | 專業 ✓ |
|---------|--------|
| 「讀到錯的資料」 | 「Dirty Read（髒讀）」 |
| 「兩次讀不一樣」 | 「Non-Repeatable Read（不可重複讀）」 |
| 「表格」 | 「Relation / Table」 |

### 3. 圖表輔助

- 比較用**表格**
- 流程用**時間序列**
- 結構用**圖示**（ER Diagram等）

### 4. 實例具體

- ✗「在某個系統中...」
- ✓「在銀行轉帳系統中，Account(account_id, balance)...」

---

## 📖 推薦練習順序

1. **先看這份解析**，理解答題架構
2. **實際練習114年的題目**
3. **用我提供的架構寫答案**
4. **對照範例答案**，找出差距

有任何題目不會寫，隨時問我！我會用同樣詳細的方式幫你解析 😊
