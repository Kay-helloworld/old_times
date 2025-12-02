# 地方政府特考三等 資料庫應用 完整題目解析 (112-113年)

這份文件針對**地方政府特考三等 (112-113年)** 的資料庫應用考題提供詳盡的申論題答題架構，涵蓋**ER Model 資料庫設計**、**SQL 語法與查詢**、**正規化 (Normalization)**、**關聯式代數**與**交易復原 (Recovery)** 等核心考點。

---

## 2. 📊 題目總覽

### 2.1 題目統計表
| 統計項目 | 數量 |
|---------|------|
| **分析考卷總數** | **2 份** (112年, 113年) |
| **總題數** | **9 題** |
| **涵蓋主題** | ER Model, SQL, 正規化, 交易處理, 關聯式代數 |
| **難度評估** | ⭐⭐⭐⭐ (偏重實務設計與 SQL 撰寫) |

### 2.2 題型分類表
| 題型 | 占比 | 代表題目 | 難度 |
|------|------|---------|------|
| **SQL 查詢與 DDL** | 35% | 建立學生表格, 教授薪資查詢, 航空旅客查詢 | ⭐⭐⭐ |
| **資料庫設計 (ER Model)** | 25% | 圖書館系統, 音樂串流平台 | ⭐⭐⭐⭐ |
| **正規化理論** | 15% | BCNF 判斷與分解, 2NF 定義 | ⭐⭐⭐⭐ |
| **交易管理 (Transaction)** | 15% | 延遲更新復原 (Deferred Update) | ⭐⭐⭐⭐ |
| **關聯式代數** | 10% | 航班查詢 | ⭐⭐⭐ |

**難度星級說明**：
- ⭐⭐⭐ = 基礎必考
- ⭐⭐⭐⭐ = 進階重要
- ⭐⭐⭐⭐⭐ = 新興熱門

---

## 3. 🎯 申論題答題黃金架構

```markdown
### 通用架構 (適用於資料庫題目)

第一部分：定義與背景 (15%)
├─ 定義關鍵術語 (如：BCNF, Entity, Primary Key)
├─ 說明設計目的 (如：為何需要正規化)
└─ 闡述假設前提 (如：ER Model 的基數假設)

第二部分：核心內容 (50%)
├─ 詳細設計圖/程式碼 (ER Diagram, SQL Query)
├─ 逐步推導過程 (正規化分解步驟, 交易 Log 追蹤)
├─ 範例資料驗證 (Table Instance)
└─ 關鍵邏輯說明

第三部分：比較分析 (20%)
├─ 優缺點分析 (如：延遲更新 vs 立即更新)
├─ 不同解法比較 (如：Subquery vs Join)
└─ 效能考量

第四部分：實務應用與延伸 (15%)
├─ 實際應用場景 (如：索引優化, 並行控制)
├─ 實作注意事項
└─ 延伸相關概念 (如：NoSQL)
```

---

## 4. 📚 【核心知識】完全解析

### 一、正規化 (Normalization) 判斷準則

| 正規形式 | 定義與條件 | 解決問題 |
|----------|------------|----------|
| **1NF** | 屬性值原子化 (Atomic), 無重複群 (Repeating Groups) | 資料結構化 |
| **2NF** | 符合 1NF + 非主鍵屬性完全相依於主鍵 (無部分相依) | 複合主鍵的部分相依 |
| **3NF** | 符合 2NF + 非主鍵屬性不遞移相依於主鍵 | 遞移相依 (Transitive Dependency) |
| **BCNF** | 符合 3NF + 所有決定因子 (Determinant) 皆為候選鍵 (Candidate Key) | 主屬性對鍵的相依 |

### 二、交易復原技術 (Recovery Techniques)

| 技術 | 寫入時機 | Undo 需要? | Redo 需要? |
|------|----------|------------|------------|
| **Deferred Update (延遲更新)** | Commit 時才寫入磁碟 | **No** (未 Commit 前不寫入) | **Yes** (Commit 後可能未寫入) |
| **Immediate Update (立即更新)** | 隨時可能寫入磁碟 | **Yes** (未 Commit 但已寫入) | **Yes** (Commit 後可能未寫入) |

### 三、SQL 常用語法速查

- **DDL (定義)**: `CREATE TABLE`, `ALTER TABLE`, `DROP TABLE`, `PRIMARY KEY`, `FOREIGN KEY`
- **DML (操作)**: `INSERT`, `UPDATE`, `DELETE`
- **Query (查詢)**: `SELECT`, `FROM`, `WHERE`, `GROUP BY`, `HAVING`, `ORDER BY`
- **Join**: `INNER JOIN`, `LEFT JOIN`, `NOT EXISTS`, `IN`

---

## 5. 📝 完整題目解析 (112年)

### 題目 1：圖書館系統 ER Model 設計

#### 📖 原題 (112年地方特考三等)

> **題目**：某圖書館有書籍 (ISBN, 書名...), 讀者 (ID, 姓名, 手機...), 館員 (ID, 姓名, 組別), 借閱紀錄, 書籍狀態檢查等資訊。
> 請設計 ER Schema，繪出 ER Diagram，標示基數比 (1:N, M:N) 與參與限制。(25 分)

#### 🎯 答題架構分析

1.  **實體識別 (Entities)**：書 (Book), 讀者 (Reader), 館員 (Librarian), 書籍狀態 (StatusCheck - 可能是弱實體或多值屬性, 視設計而定)。
2.  **關係識別 (Relationships)**：
    - 借閱 (Borrow): Reader - Book (M:N), 涉及 Librarian (服務組)。
    - 隸屬 (Belong): Librarian - Section (或屬性)。
    - 檢查 (Check): Book - Status (1:N 或 M:N)。
3.  **屬性定義**：ISBN (PK), ReaderID (PK), LibrarianID (PK) 等。
4.  **繪圖**：畫出矩形、菱形、橢圓，並標示 1, N, M 及雙線 (Total Participation)。

#### ✍️ 標準答案示範

**解答**：

**一、實體與屬性定義**
1.  **Book (書籍)**: <u>ISBN</u>, Title, Author, Publisher
2.  **Reader (讀者)**: <u>ReaderID</u>, Name, Phone (多值屬性/Multivalued)
3.  **Librarian (館員)**: <u>LibrarianID</u>, Name, Section (組別)
4.  **StatusCheck (狀態檢查)**: CheckDate, Description (此為弱實體，依附於 Book)

**二、關係定義**
1.  **Borrow (借閱)**:
    - 參與實體：Reader, Book, Librarian (三元關係 或 分解為二元)
    - 屬性：BorrowDate, ReturnDate
    - 基數：Reader (M) : Book (N) : Librarian (P) (一位讀者可借多書，一書可被多讀者借，由某館員處理)
    - 限制：只有 "服務組" 館員參與 (可在文字說明或以 Subclass 表示)。
2.  **HasStatus (檢查狀態)**:
    - 參與實體：Book (1) : StatusCheck (N)
    - 弱實體關係：StatusCheck 依賴 Book 存在。

**三、ER Diagram (文字描述結構)**
- **[Reader]** --(1,N)--> <Borrow> <--(0,N)-- **[Book]**
  - <Borrow> 連接 **[Librarian]** (0,N)
  - <Borrow> 屬性：BorrowDate, ReturnDate
- **[Book]** --(1,1)--> <Has> <--(0,N)-- **[[StatusCheck]]** (弱實體)
- **[Reader]** 屬性 Phone 為雙圈橢圓 (多值)。

*(考試時請繪製標準 ER 圖：實體用矩形，關係用菱形，屬性用橢圓，主鍵畫底線)*

#### 💡 補充說明
- **讀者參與限制**：題目提到 "從來沒有借書...不會記錄"，暗示 Reader 實體在資料庫中存在即代表有借書 (Total Participation in Borrow)? 或者是指 "潛在讀者" 不在資料庫中。若以資料庫觀點，已存在的 Reader 紀錄不一定隨時有借書 (Partial Participation)。但題目文意較偏向 "有借閱紀錄才建檔"，這在實務上較少見，通常先建檔再借書。答題時可假設一般情況，或依題目文字說明 "只有借過書才記錄" 可能指 Borrow 關係是 Reader 存在的必要條件。

---

### 題目 2：關聯式代數 (Relational Algebra)

#### 📖 原題 (112年地方特考三等)

> **題目**：機票資料庫 (旅客, 航班, 購票資訊)。
> (1) 查出 "臺北" 直飛 "洛杉磯" 的航班旅客護照與姓名。(10分)
> (2) 查出 "臺北" 出發航班的編號與乘客平均年齡。(10分)

#### 🎯 答題架構分析

1.  **Schema**:
    - Passenger(PID, Name, Phone, Age)
    - Flight(FID, Airline, DepTime, ArrTime, From, To)
    - Booking(PID, FID, Seat, Price)
2.  **查詢 (1)**: Selection (From='臺北', To='洛杉磯') -> Join Booking -> Join Passenger -> Project (PID, Name).
3.  **查詢 (2)**: Selection (From='臺北') -> Join Booking -> Join Passenger -> Group By FID -> Aggregate Average(Age). (需使用擴充關聯式代數 Grouping operator $\Im$).

#### ✍️ 標準答案示範

**解答**：

**(1) 臺北直飛洛杉磯的旅客**
$$
\pi_{PID, Name} (
  \sigma_{From='臺北' \land To='洛杉磯'} (Flight) \bowtie_{Flight.FID=Booking.FID} Booking \bowtie_{Booking.PID=Passenger.PID} Passenger
)
$$

**(2) 臺北出發航班及平均年齡**
$$
_{FID} \Im _{AVG(Age)} (
  ( \sigma_{From='臺北'} (Flight) \bowtie Booking \bowtie Passenger )
)
$$
*(註：$\Im$ 為 Grouping/Aggregation 運算子，左側為 Group By 屬性，右側為聚合函數)*

---

### 題目 3：SQL 查詢

#### 📖 原題 (112年地方特考三等)

> **題目**：承上題 Schema。
> (1) 查出 "從未" 搭乘過 "甲航空" 的旅客護照與姓名。(10分)
> (2) 查出乘客數 < 10 人的航班，列出航空公司、航班編號、人數。(10分)

#### 🎯 答題架構分析

1.  **查詢 (1)**: 差集概念 (All Passengers - Passengers who flew Airline '甲') 或 `NOT EXISTS` / `NOT IN`。
2.  **查詢 (2)**: `GROUP BY` FID, `HAVING COUNT(*) < 10`。

#### ✍️ 標準答案示範

**解答**：

**(1) 未搭乘過甲航空的旅客**
```sql
SELECT P.PID, P.Name
FROM Passenger P
WHERE P.PID NOT IN (
    SELECT B.PID
    FROM Booking B
    JOIN Flight F ON B.FID = F.FID
    WHERE F.Airline = '甲航空'
);
```

**(2) 乘客數低於 10 人的航班**
```sql
SELECT F.Airline, F.FID, COUNT(*) AS PassengerCount
FROM Flight F
JOIN Booking B ON F.FID = B.FID
GROUP BY F.Airline, F.FID
HAVING COUNT(*) < 10;
```

---

### 題目 4：交易復原 (Deferred Update)

#### 📖 原題 (112年地方特考三等)

> **題目**：5 個交易 (T1-T5)，延遲更新 (Deferred Update)。Checkpoint 時強迫儲存。
> Log: [Start T1], ..., [Commit T1], [Checkpoint], ..., [Commit T3], [Commit T2], Crash.
> 說明系統恢復時對 T1-T5 的處置 (Redo/Undo/No Action)。(25 分)

#### 🎯 答題架構分析

1.  **分析 Log 與 Checkpoint**：
    - Checkpoint 前 Commit: T1。
    - Checkpoint 後 Commit: T3, T2。
    - Crash 時未 Commit: T4, T5。
2.  **延遲更新 (Deferred Update) 規則**：
    - **NO-UNDO / REDO** 策略。
    - 未 Commit 的交易 (T4, T5)：因為是延遲更新，未 Commit 前不會寫入資料庫，故 **不需要 Undo** (或視為 Ignore)。
    - 已 Commit 的交易 (T1, T2, T3)：需確保寫入。
      - T1 在 Checkpoint 前 Commit 且 Checkpoint 強迫寫入，故 **不需要 Redo**。
      - T2, T3 在 Checkpoint 後 Commit，需 **Redo**。

#### ✍️ 標準答案示範

**解答**：

**恢復策略分析 (Deferred Update)**：
延遲更新協定下，交易直到 Commit 才會將更新寫入資料庫。因此：
- **未 Commit 的交易**：對資料庫無影響，**無需 Undo** (直接忽略)。
- **已 Commit 的交易**：需確保更新已寫入，需 **Redo**。

**各交易處置**：
1.  **T1**：在 Checkpoint 之前已 Commit (`[commit, T1]`)。Checkpoint 機制確保當時已 Commit 的資料寫入磁碟。**處置：No Action (忽略)**。
2.  **T2**：在 Checkpoint 之後 Commit (`[commit, T2]`)。**處置：Redo T2**。
3.  **T3**：在 Checkpoint 之後 Commit (`[commit, T3]`)。**處置：Redo T3**。
4.  **T4**：Crash 時尚未 Commit (無 `[commit, T4]`)。因延遲更新未寫入磁碟。**處置：No Action (或 Ignore)**。
5.  **T5**：Crash 時尚未 Commit (無 `[commit, T5]`)。**處置：No Action (或 Ignore)**。

---

### 題目 5：名詞解釋

#### 📖 原題 (112年地方特考三等)

> **題目**：(1) 第二正規化 (2NF) 定義。(5分) (2) 何謂 NoSQL。(5分)

#### ✍️ 標準答案示範

**解答**：

**(1) 第二正規化 (2NF)**
- **定義**：一個關聯表若符合 **第一正規化 (1NF)**，且其所有 **非主鍵屬性 (Non-key attributes)** 皆 **完全功能相依 (Fully Functionally Dependent)** 於主鍵，則稱符合 2NF。
- **白話**：消除非主鍵屬性對主鍵的「部分相依」。若主鍵是複合鍵 (A, B)，不可有屬性只依賴 A 或只依賴 B。

**(2) NoSQL (Not Only SQL)**
- **定義**：泛指非關聯式 (Non-Relational)、分散式、不保證 ACID (通常遵循 BASE 模型) 的資料庫系統。
- **特性**：
  - **Schema-less**：無固定綱要，彈性高。
  - **水平擴充 (Scale-out)**：易於分散式架構擴充。
  - **類型**：Key-Value (Redis), Document (MongoDB), Column-Family (Cassandra), Graph (Neo4j)。
- **適用**：大數據、高併發寫入、非結構化資料儲存。

---

## 6. 📝 完整題目解析 (113年)

### 題目 1：SQL DDL 建立表格

#### 📖 原題 (113年地方特考三等)

> **題目**：建立 `Student` 表格 (ID, Name, Major, Tel, Address)。定義資料型態與 Primary Key，並說明理由。(20 分)

#### 🎯 答題架構分析

1.  **SQL DDL**：`CREATE TABLE` 語法。
2.  **資料型態**：
    - ID: `CHAR(N)` 或 `VARCHAR` (學號通常固定長度)。
    - Name: `NVARCHAR` (支援中文)。
    - Major, Address: `NVARCHAR`。
    - Tel: `VARCHAR` (電話含區碼或符號，不參與運算，不用 INT)。
3.  **Primary Key**：選擇 ID (學號)。
4.  **理由**：唯一性 (Unique)、非空 (Not Null)、不變性。

#### ✍️ 標準答案示範

**解答**：

**SQL DDL 指令**：
```sql
CREATE TABLE Student (
    ID CHAR(10) NOT NULL,
    Name NVARCHAR(50) NOT NULL,
    Major NVARCHAR(50),
    Tel VARCHAR(20),
    Address NVARCHAR(100),
    CONSTRAINT PK_Student PRIMARY KEY (ID)
);
```

**主鍵選擇理由**：
選擇 **ID (學號)** 作為主鍵。
1.  **唯一性 (Uniqueness)**：每位學生的學號是獨一無二的，能區別不同學生 (即使同名同姓)。
2.  **非空性 (Not Null)**：學校規定學生必有學號。
3.  **穩定性**：學號一旦分發通常不會改變，適合做為關聯鍵值。

---

### 題目 2：SQL 查詢 (Professor & Teach)

#### 📖 原題 (113年地方特考三等)

> **題目**：Professor(ID, Name, Dept, Salary), Teach(ID, Course, Semester)。
> (1) 資工系薪水 > 10萬的教授名字。
> (2) 資管系教授於 1131 學期開設的課程。
> (3) 每個系的教授平均薪水與最高薪水。(30 分)

#### ✍️ 標準答案示範

**解答**：

**(1) 資工系高薪教授**
```sql
SELECT Name
FROM Professor
WHERE department = '資工系' AND salary > 100000;
```

**(2) 資管系 1131 學期課程**
```sql
SELECT T.course
FROM Professor P
JOIN Teach T ON P.ID = T.ID
WHERE P.department = '資管系' AND T.semester = 1131;
```

**(3) 各系平均與最高薪水**
```sql
SELECT department, AVG(salary) AS AvgSalary, MAX(salary) AS MaxSalary
FROM Professor
GROUP BY department;
```

---

### 題目 3：音樂串流平台 ER Model

#### 📖 原題 (113年地方特考三等)

> **題目**：歌曲 (編號, 歌名, 歌手, 作曲, 作詞, 類別), 會員 (編號, 姓名, 地址, 電話), 收聽紀錄 (會員, 歌曲, 時間)。
> 畫出 ER Diagram。(20 分)

#### 🎯 答題架構分析

1.  **實體**：Song, Member。
2.  **關係**：Listen (Member 收聽 Song, M:N, 屬性: DateTime)。
3.  **類別 (Category)**：題目說 "歌曲分為多個類別"，可設計為 Song 的屬性，或獨立實體 Category (若需管理類別資訊)。若一首歌屬於多類別，則需獨立實體與 M:N 關係。假設一首歌一類別或多類別，建議獨立實體較正規。
4.  **人員 (Artist)**：歌手、作曲、作詞。可作為 Song 的屬性，或獨立 Artist 實體。題目列為 Song 的記錄項目，若無詳細 Artist 資料，可視為屬性；但若要正規化，建議 Artist 為實體。這裡依題目 "記錄其..." 語氣，視為屬性較簡單，但視為實體較嚴謹。

#### ✍️ 標準答案示範

**解答**：

**ER Model 設計**：
1.  **Entities**:
    - **Song**: <u>SongID</u>, Title, Singer, Composer, Lyricist, Category (或獨立實體)
    - **Member**: <u>MemberID</u>, Name, Address, Phone
2.  **Relationships**:
    - **Listen (收聽)**:
      - 連接 Member 與 Song (M:N)。
      - 屬性：DateTime (收聽時間)。
      - 說明：一個會員可聽多首歌，一首歌可被多會員聽。

**ER Diagram (文字示意)**：
- **[Member]** --(0,N)--> <Listen> <--(0,N)-- **[Song]**
  - <Listen> 屬性：DateTime
- **[Song]** 屬性：SongID (PK), Title, Singer, ...

*(若使用 EER 或更細緻設計，可將 Category 獨立為實體，Singer/Composer 獨立為 Person 實體)*

---

### 題目 4：BCNF 正規化

#### 📖 原題 (113年地方特考三等)

> **題目**：表格 Register(ID, Name, Title, Credit, Grade)。PK=(ID, Title)。
> 資料範例顯示 ID->Name, Title->Credit。
> (1) 說明 BCNF 定義。
> (2) 說明未符合 BCNF 原因。
> (3) 正規化結果。(30 分)

#### 🎯 答題架構分析

1.  **相依性分析**：
    - ID -> Name (學號決定姓名)
    - Title -> Credit (課名決定學分，假設課名唯一)
    - (ID, Title) -> Grade (主鍵決定成績)
2.  **BCNF 定義**：所有功能相依 $X \to Y$ (非顯然)，$X$ 必須是 Superkey。
3.  **違規原因**：
    - `ID -> Name`：ID 是決定因子，但 ID 不是 PK (只是 PK 的一部分)，故違反 BCNF (也違反 2NF)。
    - `Title -> Credit`：Title 是決定因子，但 Title 不是 PK，違反 BCNF。
4.  **分解**：
    - Student(<u>ID</u>, Name)
    - Course(<u>Title</u>, Credit)
    - Grade(<u>ID, Title</u>, Grade)

#### ✍️ 標準答案示範

**解答**：

**(1) BCNF 定義**
一個關聯表 R 符合 BCNF，若且唯若對於 R 中所有非顯然的功能相依 (Non-trivial Functional Dependency) $X \to Y$，決定因子 $X$ 必須是 R 的 **候選鍵 (Candidate Key)** (或 Superkey)。

**(2) 未符合原因**
觀察表格與相依性：
- `ID -> Name` (學號決定姓名)
- `Title -> Credit` (課名決定學分數)
- PK 為 `(ID, Title)`。
**違規點**：
1.  `ID` 決定 `Name`，但 `ID` 只是 PK 的一部分，並非 Superkey。
2.  `Title` 決定 `Credit`，但 `Title` 只是 PK 的一部分，並非 Superkey。
故不符合 BCNF (事實上連 2NF 都不符合，因為有部分相依)。

**(3) 正規化結果**
將表格分解為三個子表，消除部分相依：
1.  **Student (學生表)**: (<u>ID</u>, Name)
2.  **Course (課程表)**: (<u>Title</u>, Credit)
3.  **Register (選課表)**: (<u>ID, Title</u>, Grade)

---

## 7. 💡 答題技巧總結

### 時間分配建議
- **SQL 撰寫 (每題 5-8 分鐘)**：先寫出 `SELECT`, `FROM`, `WHERE` 骨架，再填入條件與 Join。
- **ER Model (15-20 分鐘)**：畫圖佔時間，建議先在試題卷草繪實體與關係，確認無誤後再畫到答案卷。
- **正規化 (10-15 分鐘)**：務必寫出 "功能相依性 (FD)" 分析，這是得分關鍵。

### 分數取捨
- **SQL 題目**：CP 值最高，語法正確即滿分，優先作答。
- **交易復原**：邏輯固定 (Deferred vs Immediate)，只要判斷正確，分數全拿。
- **ER 設計**：主觀性較強，需注意題目隱含的限制 (如參與限制)，避免遺漏屬性。

---

## 8. 📚 參考資源

- **Database System Concepts** (Silberschatz, Korth, Sudarshan) - 資料庫聖經，正規化與交易章節必讀。
- **Fundamentals of Database Systems** (Elmasri, Navathe) - ER Model 與 EER 的權威參考。
- **SQLZoo / LeetCode Database** - 練習 SQL 語法的最佳平台。
