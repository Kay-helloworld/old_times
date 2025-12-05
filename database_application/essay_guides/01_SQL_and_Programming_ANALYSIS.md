# 01 SQL and Programming 完整題目解析 - 申論題答題框架

這份文件針對**01 SQL and Programming**相關題目提供詳盡的申論題答題架構。

---

## 📊 題目總覽

根據分析，在歷年資料庫應用考題中：

### 題目統計

| 統計項目 | 數量 |
|---------|------|
| **分析考卷總數** | **74 份** |
| **01 SQL and Programming相關題目** | **72 題** |
| **114年題目** | 9 題 |
| **重要性排名** | **No. 1 (最核心考點)** |

### 題型分類

| 題型 | 占比 | 代表題目 | 難度 |
|------|------|---------|------|
| **SQL語法實作** | 45% | SELECT、JOIN、GROUP BY | ⭐⭐⭐ |
| **View/Trigger/SP** | 20% | 定義、優缺點、使用時機 | ⭐⭐⭐⭐ |
| **資料庫設計+SQL** | 25% | ER Diagram → SQL | ⭐⭐⭐⭐ |
| **進階查詢** | 10% | 子查詢、關聯代數 | ⭐⭐⭐⭐⭐ |

**難度星級說明**:
- ⭐⭐⭐ = 基礎必考
- ⭐⭐⭐⭐ = 進階重要
- ⭐⭐⭐⭐⭐ = 新興熱門 (近三年大量出現)

---

## 🎯 申論題答題黃金架構

### 通用架構（適用所有SQL題）

```
第一部分：理解題意與資料結構 (15%)
├─ 列出所有相關資料表
├─ 標示主鍵（Primary Key）
├─ 標示外來鍵（Foreign Key）
└─ 確認需求條件

第二部分：SQL語法撰寫 (60%)
├─ 加註解說明思路
├─ 使用有意義的別名
├─ 適當的縮排和換行
└─ 分步驟說明（複雜查詢）

第三部分：驗證與優化（選答） (25%)
├─ 說明查詢邏輯
├─ 可能的優化方向
└─ 特殊情況處理
```

---



---

## 📚 【核心知識】完全解析



---

## 📝 實戰解析：精選題型詳解

---

### 【題型一】基礎SQL查詢 - JOIN與聚合函數

#### 📖 原題（114年高考第三題）

**完整題目**：

> **三、根據下列客戶訂單資料回答相關查詢SQL敘述，資料表格為：Customer(CID, Name), Orders(OID, CID, TotalAmount, OrderDate), Payment(PID, OID, AmountPaid)。（每小題 10 分，共 30 分）**
>
> **⑴** 在 OrderDate 為"2025.01.01"當天，所有客戶訂單總量排行，依總量由高到低列出客戶姓名與總量。
>
> **⑵** 找出截至 2025.01.01，曾有付款行為且總付款金額超過 10,000 的客戶姓名與其總付款金額。
>
> **⑶** 所有訂單但付款金額（AmountPaid）總和不足訂單金額（TotalAmount）的客戶名稱與欠款金額，並以欠款金額由高至低排序。

**資料表結構**：

- `Customer(CID, Name)` - 客戶表（CID為主鍵）
- `Orders(OID, CID, TotalAmount, OrderDate)` - 訂單表（OID為主鍵，CID為外來鍵）
- `Payment(PID, OID, AmountPaid)` - 付款表（PID為主鍵，OID為外來鍵）

---

#### 🎯 答題架構分析

這是**典型的多表JOIN + 聚合查詢**題型，每個子題需要：

1. **資料表分析**（先在草稿紙畫出關聯）
2. **SQL語法**（附註解）
3. **邏輯說明**（簡短）

---

#### ✍️ 標準答案示範

**問題一：2025-01-01當天客戶訂單總量排行**

**第一步：分析需求**

- 篩選條件：`OrderDate = '2025-01-01'`
- 需要的表：`Customer` + `Orders`
- 聚合：每個客戶的訂單總金額（`SUM(TotalAmount)`）
- 排序：由高到低（`DESC`）
- 輸出：客戶姓名、總金額

**第二步：撰寫SQL**

```sql
-- 查詢2025-01-01當天所有客戶的訂單總量，並依總量排序
SELECT 
    C.Name AS 客戶姓名,
    SUM(O.TotalAmount) AS 訂單總額
FROM 
    Customer C
    INNER JOIN Orders O ON C.CID = O.CID
WHERE 
    O.OrderDate = '2025-01-01'
GROUP BY 
    C.CID, C.Name
ORDER BY 
    訂單總額 DESC;
```

**第三步：邏輯說明**

1. 使用 `INNER JOIN` 連接 Customer 和 Orders（只保留有訂單的客戶）
2. `WHERE` 子句篩選特定日期
3. `GROUP BY` 按客戶分組
4. `SUM()` 計算每個客戶的訂單總額
5. `ORDER BY DESC` 依總額由高到低排序

**注意事項**：

- `GROUP BY` 必須包含 `C.CID` 和 `C.Name`（雖然CID已唯一識別，但Name也要列出）
- 若某客戶當天無訂單，則不會出現在結果中

---

**問題二：總付款金額超過10,000的客戶**

**第一步：分析需求**

- 需要的表：`Customer` + `Payment`（需透過Orders連接）
- 聚合：每個客戶的付款總額（`SUM(AmountPaid)`）
- 篩選：總付款 > 10,000
- 輸出：客戶姓名、總付款金額

**第二步：撰寫SQL**

```sql
-- 查詢總付款金額超過10,000的客戶
SELECT 
    C.Name AS 客戶姓名,
    SUM(P.AmountPaid) AS 總付款金額
FROM 
    Customer C
    INNER JOIN Orders O ON C.CID = O.CID
    INNER JOIN Payment P ON O.OID = P.OID
GROUP BY 
    C.CID, C.Name
HAVING 
    SUM(P.AmountPaid) > 10000
ORDER BY 
    總付款金額 DESC;
```

**第三步：邏輯說明**

1. 需要兩次 `INNER JOIN`：
   - Customer → Orders（透過CID）
   - Orders → Payment（透過OID）
2. `GROUP BY` 按客戶分組
3. **關鍵**：使用 `HAVING` 而非 `WHERE`
   - `WHERE` 用於篩選資料列（在聚合前）
   - `HAVING` 用於篩選群組（在聚合後）
4. 此題必須用 `HAVING` 因為條件是「總付款金額」，需先聚合才能判斷

---

**問題三：欠款客戶與欠款金額**

**第一步：分析需求**

- 需要計算：訂單總額 vs 付款總額
- 欠款金額 = 訂單總額 - 付款總額
- 篩選：欠款金額 > 0 的客戶

**第二步：撰寫SQL（方法一：使用JOIN）**

```sql
-- 查詢有欠款的客戶及欠款金額
SELECT 
    C.Name AS 客戶姓名,
    SUM(O.TotalAmount) AS 訂單總額,
    COALESCE(SUM(P.AmountPaid), 0) AS 已付款總額,
    SUM(O.TotalAmount) - COALESCE(SUM(P.AmountPaid), 0) AS 欠款金額
FROM 
    Customer C
    INNER JOIN Orders O ON C.CID = O.CID
    LEFT JOIN Payment P ON O.OID = P.OID
GROUP BY 
    C.CID, C.Name
HAVING 
    SUM(O.TotalAmount) - COALESCE(SUM(P.AmountPaid), 0) > 0
ORDER BY 
    欠款金額 DESC;
```

**第三步：邏輯說明**

1. **關鍵點**：使用 `LEFT JOIN` 而非 `INNER JOIN`
   - 原因：某些訂單可能完全沒有付款記錄
   - `LEFT JOIN` 確保所有訂單都會被考慮

2. **`COALESCE()` 函數**：
   - 當某訂單無付款記錄時，`SUM(P.AmountPaid)` 會是 `NULL`
   - `COALESCE(SUM(P.AmountPaid), 0)` 將 `NULL` 轉為 `0`

3. 計算欠款：訂單總額 - 已付款總額

4. `HAVING` 篩選出欠款 > 0 的客戶

---

**方法二：使用子查詢（進階寫法）**

```sql
-- 使用子查詢的進階寫法
SELECT 
    C.Name AS 客戶姓名,
    OrderTotal.總訂單額,
    COALESCE(PaymentTotal.總付款額, 0) AS 總付款額,
    OrderTotal.總訂單額 - COALESCE(PaymentTotal.總付款額, 0) AS 欠款金額
FROM 
    Customer C
    INNER JOIN (
        SELECT CID, SUM(TotalAmount) AS 總訂單額
        FROM Orders
        GROUP BY CID
    ) AS OrderTotal ON C.CID = OrderTotal.CID
    LEFT JOIN (
        SELECT O.CID, SUM(P.AmountPaid) AS 總付款額
        FROM Orders O
        INNER JOIN Payment P ON O.OID = P.OID
        GROUP BY O.CID
    ) AS PaymentTotal ON C.CID = PaymentTotal.CID
WHERE 
    OrderTotal.總訂單額 - COALESCE(PaymentTotal.總付款額, 0) > 0
ORDER BY 
    欠款金額 DESC;
```

**方法二優點**：

- 邏輯更清晰（先各自聚合，再JOIN）
- 效能可能較佳（視資料量而定）

---

#### 💡 答題技巧總結

**這種「多表JOIN + 聚合」題的得分關鍵**：

1. **JOIN類型選擇**：
   - `INNER JOIN`：只保留兩表都有的資料
   - `LEFT JOIN`：保留左表所有資料，右表無對應則為NULL
   - 選錯會導致結果不完整！

2. **聚合函數位置**：
   - `WHERE`：篩選原始資料（聚合前）
   - `HAVING`：篩選聚合結果（聚合後）
   - 題目若問「總額超過XX」，必用 `HAVING`

3. **NULL值處理**：
   - 使用 `COALESCE()` 或 `IFNULL()` 將NULL轉為0
   - 避免計算錯誤

4. **GROUP BY完整性**：
   - MySQL 5.7+ 預設開啟 `ONLY_FULL_GROUP_BY`
   - `SELECT` 的非聚合欄位都要出現在 `GROUP BY`

5. **加註解**：
   - 閱卷老師快速理解你的思路
   - 即使SQL有小錯誤，也能拿到部分分數

---

### 【題型二】View（視圖）- 定義與應用

#### 📖 原題（106年警察特考第三題）

**完整題目**：

> **三、在關聯式資料庫（Relational database）裡，資料庫管理者可以create "View"這種東西給使用者使用：**
>
> **⑴** 試問View 是什麼？（5 分）
>
> **⑵** 資料庫使用View 有什麼好處？（15 分）

---

#### 🎯 答題架構分析

這是**定義+優點列舉**型題目，需要：

1. **定義部分**（5分）：精確定義，加上特性說明
2. **優點部分**（15分）：至少列出5個優點，每個約3分

---

#### ✍️ 標準答案示範

**第一部分：View 的定義（5分）**

**定義**：

View（視圖、界視表）是一種**虛擬表格（Virtual Table）**，它是基於一個或多個基底資料表（Base Table）透過 SQL 查詢語句所定義的邏輯視圖。View 本身**不實際儲存資料**，而是在每次查詢時動態執行其定義的 SQL 語句，從基底表中提取資料。

**特性說明**：

- **虛擬性**：View 沒有實體的資料儲存空間，只儲存 SQL 定義
- **動態性**：每次查詢 View 時，會即時執行其定義的查詢，反映最新的基底表資料
- **可查詢性**：使用者可以像查詢一般資料表一樣查詢 View
- **部分可更新性**：某些簡單的 View 可以進行 INSERT、UPDATE、DELETE 操作，但有限制

**語法範例**：

```sql
-- 建立 View 的語法
CREATE VIEW view_name AS
SELECT column1, column2, ...
FROM table_name
WHERE condition;

-- 範例：建立顯示高薪員工的 View
CREATE VIEW HighSalaryEmployees AS
SELECT EmployeeID, Name, Salary, Department
FROM Employees
WHERE Salary > 50000;

-- 查詢 View（就像查詢一般資料表）
SELECT * FROM HighSalaryEmployees;
```

---

**第二部分：使用 View 的好處（15分）**

**優點一：簡化複雜查詢（Simplify Complex Queries）**

**說明**：

- 對於涉及多個資料表 JOIN、複雜條件篩選、聚合運算的查詢，可以建立 View 將複雜邏輯封裝起來
- 使用者只需查詢 View，無需每次都撰寫複雜的 SQL

**範例情境**：

假設要查詢「每個部門的平均薪資及員工人數」，需要這樣的複雜查詢：

```sql
-- 複雜查詢（每次都要寫）
SELECT 
    D.DepartmentName,
    COUNT(E.EmployeeID) AS EmployeeCount,
    AVG(E.Salary) AS AvgSalary
FROM 
    Departments D
    LEFT JOIN Employees E ON D.DepartmentID = E.DepartmentID
GROUP BY 
    D.DepartmentID, D.DepartmentName;
```

使用 View 後：

```sql
-- 建立 View
CREATE VIEW DepartmentSummary AS
SELECT 
    D.DepartmentName,
    COUNT(E.EmployeeID) AS EmployeeCount,
    AVG(E.Salary) AS AvgSalary
FROM 
    Departments D
    LEFT JOIN Employees E ON D.DepartmentID = E.DepartmentID
GROUP BY 
    D.DepartmentID, D.DepartmentName;

-- 使用者只需簡單查詢
SELECT * FROM DepartmentSummary
WHERE AvgSalary > 40000;
```

---

**優點二：提供資料安全性（Data Security）**

**說明**：

- View 可以隱藏敏感欄位，只顯示使用者應該看到的資料
- 透過 View 實施**欄位層級（Column-Level）** 和**資料列層級（Row-Level）** 的存取控制
- 不同使用者可以授予不同 View 的權限，而非直接存取基底表

**範例情境**：

員工資料表包含敏感資訊（薪資、身分證號），一般使用者不應看到：

```sql
-- 基底表（包含敏感資料）
Employees (EmployeeID, Name, Salary, SSN, Department, Email)

-- 建立「公開資訊」View（隱藏敏感欄位）
CREATE VIEW PublicEmployeeInfo AS
SELECT EmployeeID, Name, Department, Email
FROM Employees;

-- 一般使用者只能查詢 PublicEmployeeInfo
-- 無法看到 Salary 和 SSN
GRANT SELECT ON PublicEmployeeInfo TO general_user;
```

**資料列層級控制範例**：

```sql
-- 建立「本部門員工」View（使用者只能看到自己部門）
CREATE VIEW MyDepartmentEmployees AS
SELECT EmployeeID, Name, Email
FROM Employees
WHERE Department = (
    SELECT Department 
    FROM Employees 
    WHERE EmployeeID = CURRENT_USER()
);
```

---

**優點三：邏輯資料獨立性（Logical Data Independence）**

**說明**：

- 當基底表結構改變（例如：欄位名稱修改、資料表拆分）時，只需修改 View 的定義，應用程式無需修改
- 提供一個穩定的介面層（Interface Layer），隔離應用程式與實體資料庫結構的變動

**範例情境**：

假設公司決定將「員工」表拆分為「基本資料」和「薪資資料」兩表：

```sql
-- 原始設計（單一資料表）
Employees (EmployeeID, Name, Department, Salary)

-- 新設計（拆分為兩表）
EmployeeBasic (EmployeeID, Name, Department)
EmployeeSalary (EmployeeID, Salary)

-- 建立 View 維持原有介面
CREATE VIEW Employees AS
SELECT 
    B.EmployeeID,
    B.Name,
    B.Department,
    S.Salary
FROM 
    EmployeeBasic B
    INNER JOIN EmployeeSalary S ON B.EmployeeID = S.EmployeeID;

-- 應用程式仍可用原本的方式查詢
SELECT * FROM Employees WHERE Department = 'IT';
-- 完全不知道底層結構已改變！
```

---

**優點四：客製化資料呈現（Customized Data Presentation）**

**說明**：

- 不同使用者或應用程式可能需要不同格式或內容的資料
- View 可以重新組織、計算、格式化資料，提供客製化的呈現方式

**範例情境**：

```sql
-- 基底表（原始資料）
Orders (OrderID, OrderDate, TotalAmount, CustomerID)

-- View 1：月報表格式（供管理階層）
CREATE VIEW MonthlySalesReport AS
SELECT 
    YEAR(OrderDate) AS 年度,
    MONTH(OrderDate) AS 月份,
    COUNT(*) AS 訂單數量,
    SUM(TotalAmount) AS 銷售總額,
    AVG(TotalAmount) AS 平均訂單金額
FROM Orders
GROUP BY YEAR(OrderDate), MONTH(OrderDate);

-- View 2：客戶訂單歷史（供客服使用）
CREATE VIEW CustomerOrderHistory AS
SELECT 
    C.CustomerName,
    O.OrderID,
    O.OrderDate,
    O.TotalAmount,
    CASE 
        WHEN O.TotalAmount > 10000 THEN 'VIP客戶'
        WHEN O.TotalAmount > 5000 THEN '重要客戶'
        ELSE '一般客戶'
    END AS 客戶等級
FROM 
    Orders O
    INNER JOIN Customers C ON O.CustomerID = C.CustomerID;
```

---

**優點五：效能優化（在某些情況下）**

**說明**：

- 某些資料庫系統支援 **Materialized View（實體化視圖）**，會實際儲存查詢結果並定期更新
- 對於複雜且頻繁查詢的資料，使用 Materialized View 可大幅提升效能
- 一般 View 雖然不儲存資料，但可以作為查詢最佳化器（Query Optimizer）的提示

**Materialized View 範例**（Oracle、PostgreSQL 支援）：

```sql
-- 建立實體化視圖（實際儲存查詢結果）
CREATE MATERIALIZED VIEW ProductSalesSummary AS
SELECT 
    ProductID,
    SUM(Quantity) AS TotalQuantity,
    SUM(Amount) AS TotalRevenue
FROM Sales
GROUP BY ProductID;

-- 定期重新整理（例如：每天凌晨）
REFRESH MATERIALIZED VIEW ProductSalesSummary;

-- 查詢速度極快（因為已預先計算並儲存）
SELECT * FROM ProductSalesSummary WHERE TotalRevenue > 100000;
```

**注意**：一般 View（Virtual View）不會提升效能，每次查詢都會執行 SQL。但 Materialized View 可以。

---

**優點六：支援多種資料來源整合**

**說明**：

- View 可以整合多個不同的資料表，甚至來自不同資料庫的資料（透過 DB Link）
- 提供統一的查詢介面

**範例**：

```sql
-- 整合訂單、客戶、產品三個表
CREATE VIEW CompleteOrderInfo AS
SELECT 
    O.OrderID,
    C.CustomerName,
    C.ContactEmail,
    P.ProductName,
    OD.Quantity,
    OD.UnitPrice,
    OD.Quantity * OD.UnitPrice AS Subtotal
FROM 
    Orders O
    INNER JOIN Customers C ON O.CustomerID = C.CustomerID
    INNER JOIN OrderDetails OD ON O.OrderID = OD.OrderID
    INNER JOIN Products P ON OD.ProductID = P.ProductID;
```

---

**總結表格：View 的優點**

| 優點類別 | 主要效益 | 適用情境 |
|---------|---------|---------|
| **簡化複雜查詢** | 降低使用難度 | 多表JOIN、複雜聚合 |
| **資料安全性** | 隱藏敏感資料 | 不同權限等級的使用者 |
| **邏輯資料獨立性** | 隔離結構變動 | 資料庫重構、應用程式維護 |
| **客製化呈現** | 滿足不同需求 | 報表、不同部門使用 |
| **效能優化** | 加速查詢（Materialized View） | 複雜聚合查詢、大數據分析 |
| **資料整合** | 統一查詢介面 | 多表、跨資料庫查詢 |

---

#### 💡 答題技巧總結

**「定義+優點」題型的得分關鍵**：

1. **定義要精準**：
   - ✓ 「View 是虛擬表格，不實際儲存資料」
   - ✗ 「View 是一個東西可以看資料」

2. **優點要分點**：
   - 用 ⑴⑵⑶ 或項目符號清楚標示
   - 每個優點：名稱 + 說明 + 範例

3. **範例要具體**：
   - 寫出實際的 SQL 語法
   - 說明適用情境

4. **數量要充足**：
   - 15分的題目，至少列出5-6個優點
   - 每個優點約2-3分

---

### 【題型三】Trigger 與 Stored Procedure

#### 📖 原題（113年一般警察特考第四題）

**完整題目**：

> **四、闡述何謂預存程序（Store Procedure）與觸發程序（Trigger），以及敘述它們各自的優點？（15 分）**

---

#### 🎯 答題架構分析

這是**雙概念定義+優點比較**型題目：

1. **定義部分**（各3分，共6分）
2. **優點部分**（各4-5分，共9分）
3. **可選加分**：比較表格

---

#### ✍️ 標準答案示範

**第一部分：Stored Procedure（預存程序）的定義與優點**

**定義**：

預存程序（Stored Procedure，或稱「儲存程序」）是一組**預先編譯並儲存在資料庫伺服器**的 SQL 語句集合，可以接受參數（Parameters）、執行邏輯運算、並回傳結果。使用者可以像呼叫函數一樣呼叫預存程序，執行複雜的資料庫操作。

**特性**：

- 儲存在資料庫中（而非應用程式）
- 預先編譯，提升執行效率
- 可包含流程控制語句（IF、WHILE、CASE等）
- 可接受輸入參數、輸出參數
- 可回傳單一值或結果集

**語法範例**：

```sql
-- MySQL 範例：建立計算員工獎金的預存程序
DELIMITER //

CREATE PROCEDURE CalculateBonus(
    IN emp_id INT,                -- 輸入參數：員工編號
    IN performance_score DECIMAL(3,2),  -- 輸入參數：績效分數
    OUT bonus_amount DECIMAL(10,2)      -- 輸出參數：獎金金額
)
BEGIN
    DECLARE base_salary DECIMAL(10,2);
    
    -- 取得員工基本薪資
    SELECT Salary INTO base_salary
    FROM Employees
    WHERE EmployeeID = emp_id;
    
    -- 根據績效計算獎金
    IF performance_score >= 0.9 THEN
        SET bonus_amount = base_salary * 0.3;
    ELSEIF performance_score >= 0.7 THEN
        SET bonus_amount = base_salary * 0.2;
    ELSE
        SET bonus_amount = base_salary * 0.1;
    END IF;
    
    -- 記錄到獎金表
    INSERT INTO Bonuses(EmployeeID, Amount, Year)
    VALUES (emp_id, bonus_amount, YEAR(NOW()));
END //

DELIMITER ;

-- 呼叫預存程序
CALL CalculateBonus(1001, 0.85, @my_bonus);
SELECT @my_bonus AS '我的獎金';
```

**Stored Procedure 的優點**：

**⑴ 效能提升（Performance Improvement）**

- **預先編譯**：Stored Procedure 在第一次執行時會被編譯並儲存執行計畫（Execution Plan），後續呼叫直接使用，無需重新解析和編譯
- **減少網路傳輸**：複雜的多步驟操作只需傳送一次呼叫指令，而非多次SQL語句
- **範例**：

  ```sql
  -- 不使用 Stored Procedure：應用程式需傳送 5 次 SQL
  SELECT ... (100KB)
  UPDATE ... (50KB)
  INSERT ... (80KB)
  DELETE ... (30KB)
  SELECT ... (120KB)
  -- 總傳輸：380KB

  -- 使用 Stored Procedure：只傳送一次
  CALL ProcessOrder(1001);  -- 可能只有幾KB
  ```

**⑵ 程式碼重用與維護性（Code Reusability and Maintainability）**

- **中央化管理**：業務邏輯集中在資料庫，所有應用程式共用
- **修改方便**：業務邏輯改變時，只需修改 Stored Procedure，無需修改每個應用程式
- **範例情境**：
  - 假設「計算訂單折扣」的邏輯改變
  - **不用 SP**：需修改 Web、Mobile App、報表系統等所有程式
  - **用 SP**：只需修改資料庫中的一個 Stored Procedure

**⑶ 安全性提升（Enhanced Security）**

- **權限控制**：使用者只需執行 Stored Procedure 的權限，無需直接存取基底表
- **防止 SQL Injection**：參數化處理，自動過濾惡意輸入
- **範例**：

  ```sql
  -- 使用者只能呼叫此 SP，無法直接 UPDATE Salary
  CREATE PROCEDURE UpdateEmployeeSalary(
      IN emp_id INT,
      IN new_salary DECIMAL(10,2)
  )
  BEGIN
      -- 加入商業邏輯驗證
      IF new_salary > (SELECT Salary FROM Employees WHERE EmployeeID = emp_id) * 1.2 THEN
          SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = '薪資調整不得超過20%';
      ELSE
          UPDATE Employees SET Salary = new_salary WHERE EmployeeID = emp_id;
      END IF;
  END;

  -- 授權：使用者可執行 SP，但無法直接 UPDATE
  GRANT EXECUTE ON PROCEDURE UpdateEmployeeSalary TO employee_manager;
  REVOKE UPDATE ON Employees FROM employee_manager;
  ```

**⑷ 支援複雜商業邏輯（Complex Business Logic Support）**

- 可包含流程控制（IF、WHILE、CASE）、例外處理（TRY...CATCH）、交易控制（BEGIN TRANSACTION）
- **範例**：處理訂單的複雜流程

  ```sql
  CREATE PROCEDURE ProcessOrder(IN order_id INT)
  BEGIN
      DECLARE stock_available INT;
      DECLARE CONTINUE HANDLER FOR SQLEXCEPTION
      BEGIN
          ROLLBACK;
          INSERT INTO ErrorLog VALUES (NOW(), 'ProcessOrder failed');
      END;

      START TRANSACTION;
      
      -- 檢查庫存
      SELECT Stock INTO stock_available FROM Products 
      WHERE ProductID = (SELECT ProductID FROM Orders WHERE OrderID = order_id);
      
      IF stock_available > 0 THEN
          -- 扣除庫存
          UPDATE Products SET Stock = Stock - 1 
          WHERE ProductID = (SELECT ProductID FROM Orders WHERE OrderID = order_id);
          
          -- 更新訂單狀態
          UPDATE Orders SET Status = 'Confirmed' WHERE OrderID = order_id;
          
          -- 記錄出貨
          INSERT INTO Shipments(OrderID, ShipDate) VALUES (order_id, NOW());
          
          COMMIT;
      ELSE
          ROLLBACK;
      END IF;
  END;
  ```

---

**第二部分：Trigger（觸發程序）的定義與優點**

**定義**：

觸發程序（Trigger）是一種特殊的 Stored Procedure，會在特定的資料庫事件（Event）發生時**自動執行**，無需明確呼叫。Trigger 通常與資料表的 INSERT、UPDATE、DELETE 操作綁定，用於維護資料完整性、自動化作業、或稽核資料變更。

**特性**：

- **自動觸發**：由資料庫事件驅動，無需手動呼叫
- **透明性**：使用者不知道 Trigger 的存在
- **觸發時機**：BEFORE（操作前）或 AFTER（操作後）
- **觸發事件**：INSERT、UPDATE、DELETE

**語法範例**：

```sql
-- MySQL 範例：自動記錄薪資調整歷史
DELIMITER //

CREATE TRIGGER salary_audit_trigger
AFTER UPDATE ON Employees
FOR EACH ROW
BEGIN
    -- 只有薪資改變時才記錄
    IF OLD.Salary <> NEW.Salary THEN
        INSERT INTO SalaryAudit(
            EmployeeID,
            OldSalary,
            NewSalary,
            ChangeDate,
            ChangedBy
        ) VALUES (
            NEW.EmployeeID,
            OLD.Salary,
            NEW.Salary,
            NOW(),
            USER()
        );
    END IF;
END //

DELIMITER ;

-- 當執行以下 UPDATE 時，Trigger 自動記錄變更
UPDATE Employees SET Salary = 60000 WHERE EmployeeID = 1001;
-- SalaryAudit 表會自動新增一筆記錄
```

**Trigger 的優點**：

**⑴ 自動化資料完整性維護（Automated Data Integrity）**

- 自動檢查和強制執行商業規則
- 無需依賴應用程式邏輯，確保一致性
- **範例**：防止庫存為負數

  ```sql
  CREATE TRIGGER prevent_negative_stock
  BEFORE UPDATE ON Products
  FOR EACH ROW
  BEGIN
      IF NEW.Stock < 0 THEN
          SIGNAL SQLSTATE '45000' 
          SET MESSAGE_TEXT = '庫存不得為負數';
      END IF;
  END;
  ```

**⑵完整的稽核追蹤（Comprehensive Audit Trail）**

- 自動記錄所有資料變更，無法被遺漏或繞過
- 記錄誰（Who）、何時（When）、改了什麼（What）
- **範例**：完整的刪除記錄

  ```sql
  CREATE TRIGGER log_employee_deletion
  BEFORE DELETE ON Employees
  FOR EACH ROW
  BEGIN
      INSERT INTO EmployeeDeleteLog(
          EmployeeID,
          Name,
          DeletedDate,
          DeletedBy
      ) VALUES (
          OLD.EmployeeID,
          OLD.Name,
          NOW(),
          USER()
      );
  END;
  ```

**⑶ 連鎖更新（Cascading Updates）**

- 自動更新相關資料表，維持資料一致性
- **範例**：訂單新增時自動扣除庫存

  ```sql
  CREATE TRIGGER reduce_stock_on_order
  AFTER INSERT ON OrderDetails
  FOR EACH ROW
  BEGIN
      UPDATE Products
      SET Stock = Stock - NEW.Quantity
      WHERE ProductID = NEW.ProductID;
  END;
  ```

**⑷ 計算欄位自動更新（Automatic Computed Fields）**

- 自動計算和更新衍生欄位
- **範例**：訂單總額自動計算

  ```sql
  CREATE TRIGGER calculate_order_total
  AFTER INSERT ON OrderDetails
  FOR EACH ROW
  BEGIN
      UPDATE Orders
      SET TotalAmount = (
          SELECT SUM(Quantity * UnitPrice)
          FROM OrderDetails
          WHERE OrderID = NEW.OrderID
      )
      WHERE OrderID = NEW.OrderID;
  END;
  ```

---

**第三部分：Stored Procedure vs Trigger 比較**

| 比較項目 | Stored Procedure | Trigger |
|---------|-----------------|---------|
| **執行方式** | 手動呼叫（CALL） | 自動觸發 |
| **觸發時機** | 由應用程式決定 | 資料事件發生時（INSERT/UPDATE/DELETE） |
| **參數** | 可接受輸入/輸出參數 | 無參數（使用 OLD/NEW 存取資料） |
| **回傳值** | 可回傳結果集或輸出參數 | 無回傳值 |
| **使用情境** | 複雜商業邏輯、批次處理 | 資料完整性、稽核、自動化維護 |
| **透明性** | 使用者明確知道呼叫 SP | 使用者不知道 Trigger 存在 |
| **效能影響** | 可控制執行時機 | 每次資料變更都觸發，可能影響效能 |

---

**總結**：

- **Stored Procedure**：適合需要「主動呼叫」的業務邏輯，例如：月底結帳、批次更新、複雜報表
- **Trigger**：適合需要「被動觸發」的自動化作業，例如：稽核記錄、資料驗證、連動更新

**實務建議**：

- 兩者常搭配使用：Trigger 記錄變更，Stored Procedure 執行批次處理
- 過度使用 Trigger 可能導致效能問題和維護困難（Trigger 鏈）
- 商業邏輯應優先放在應用程式，只有必要的部分才放入 SP 或 Trigger

---

#### 💡 答題技巧總結

**「雙概念比較」題型的得分關鍵**：

1. **定義要區分**：
   - 強調兩者的核心差異（主動 vs 被動）

2. **優點要平衡**：
   - 分配篇幅，避免只寫一個

3. **範例要對比**：
   - 用相同情境展示兩者的不同用法

4. **表格加分**：
   - 比較表格讓閱卷老師印象深刻

---



---

## 📖 歷屆考題彙整連結

請參閱同目錄下的 `01_SQL_and_Programming.md` 檔案以查看完整歷屆考題。
