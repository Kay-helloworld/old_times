# 資料庫考題關鍵字分析報告

## 1. 高頻關鍵字統計 (Top 50)

| 排名 | 關鍵字 | 出現次數 |
|---|---|---|
| 1 | 資料 | 194 |
| 2 | SQL | 78 |
| 3 | BASE | 57 |
| 4 | Schema | 45 |
| 5 | 編號 | 44 |
| 6 | AI | 43 |
| 7 | 說明 | 43 |
| 8 | Entity | 38 |
| 9 | Relationship | 35 |
| 10 | 關聯式 | 32 |
| 11 | Attribute | 28 |
| 12 | Transaction | 28 |
| 13 | 表格 | 28 |
| 14 | BCNF | 27 |
| 15 | 實體 | 27 |
| 16 | 系統 | 26 |
| 17 | 屬性 | 21 |
| 18 | 時間 | 20 |
| 19 | 設計 | 20 |
| 20 | 規化 | 20 |
| 21 | 主鍵 | 20 |
| 22 | Data | 20 |
| 23 | 名稱 | 18 |
| 24 | 定義 | 18 |
| 25 | 查詢 | 17 |
| 26 | Relational | 16 |
| 27 | 處理 | 15 |
| 28 | 管理系 | 15 |
| 29 | Functional Dependency | 15 |
| 30 | ID | 14 |
| 31 | 交易 | 14 |
| 32 | Database | 14 |
| 33 | Log | 14 |
| 34 | 課程 | 13 |
| 35 | NoSQL | 13 |
| 36 | Model | 13 |
| 37 | 記錄 | 13 |
| 38 | 學生 | 12 |
| 39 | 3NF | 12 |
| 40 | 員工 | 12 |
| 41 | Key | 11 |
| 42 | database | 11 |
| 43 | Locking | 11 |
| 44 | Normalization | 11 |
| 45 | 訂單 | 10 |
| 46 | 數量 | 10 |
| 47 | 相關 | 10 |
| 48 | Name | 10 |
| 49 | 型式 | 10 |
| 50 | 執行 | 10 |

## 2. 題目與關鍵字清單 (前 50 題範例)

### 1. 105年特種考試地方政府公務人員考試試題 代號：34030 全一張等別 ： 三等考試.txt - 一、
**關鍵字**: 編號, 廠商, 藥妝, 訂單, 顧客, 商品, 資料, 供應, 名稱, Key, Attribute, Schema

```text
一、美美藥妝店委託軟體公司建置管理資訊系統，資料庫的資料需求如下：
z 顧客：一個顧客有一個顧客編號、顧客姓名、顧客住址、手機號碼。每個顧客編
號是唯一的，一個顧客每次可購買數件藥妝商品。
z 藥妝商品：每一件藥妝商品有一個藥妝商品編號、藥妝名稱、藥妝種類、單價、
廠商編號。一件藥妝商品的藥妝商品編號是唯一的。
z 供應商：每一個廠商有一個廠商編號、廠商名稱、廠商住址、廠商電話。每一個
供應商的廠...
```

### 2. 105年特種考試地方政府公務人員考試試題 代號：34030 全一張等別 ： 三等考試.txt - 二、
**關鍵字**: 教師, 授課, 資料, 教室, 上課, 課程, 考試, 編號, 時間, 假設, BCNF, BASE

```text
二、巨人電腦補習班有個關聯式資料庫（Relational Database），兩個資料表為授課A、授
課 B，資料表綱要如下所示：
授課 A（教師編號、教師姓名、授課時間、授課教室），功能相依性的假設為：每位
教師姓名都不一樣，教師授課皆在教室內，教師在任何一個上課時段內只在一
間教室上課。
授課 B（教師編號、授課時間、授課教室、課程），功能相依性的假設為：每位教師
可授多門課程，但一門課程只由...
```

### 3. 105年特種考試地方政府公務人員考試試題 代號：34030 全一張等別 ： 三等考試.txt - 三、
**關鍵字**: 客戶, 書籍, 編號, 訂單, 資料, 數量, 表記, 電話, 姓名, 付款, SQL, Attribute, Schema, BASE

```text
三、3Q 出版社販售中英文教科書，系統的關聯式資料庫（Relational Database）包含：書
籍、客戶、訂單三個資料表（Table）。書籍資料表記錄書籍編號、書籍名稱、書籍單
價；客戶資料表記錄客戶編號、客戶姓名、客 戶地址、客戶電話；訂單資料表記錄
訂單編號、訂單日期、是否付款、書籍編號、 數量、客戶編號，每筆訂單只有一位
下訂單的客戶。這三個資料表的關聯綱要（Relational S...
```

### 4. 105年特種考試地方政府公務人員考試試題 代號：34030 全一張等別 ： 三等考試.txt - 四、
**關鍵字**: 資料, 關聯式, 聯式, 庫資料, 網路, 興起, 帶動, 現象, 篩選, 幫助, SQL, NoSQL

```text
四、網路興起帶動巨量資料現象，經過資料的整理、篩選及分析，可以幫助企業經營做
決策，關聯式資料庫在資料結構設計上十分費 工，造成傳統關聯式查詢相對緩慢，
NoSQL 資料庫因應而生。
請說明關聯式資料庫與NoSQL 資料庫的差異。（10 分）
若員工資料有：員工編號、姓名、身分證字號、年齡、部門、職稱、薪資，請列
出關聯式資料庫資料表與NoSQL 資料庫資料表。（15 分）...
```

### 5. 106年特種考試地方政府公務人員考試試題 代號：33630 全一頁等別 ： 三等考試考試時間 ： 2 小時 座 號 ：.txt - 一、
**關鍵字**: 試述, 名詞, 意涵, 小題, Integrity, Rule, Location, independence, distributed, database, Entity, Locking, Distributed Database, BASE

```text
一、請試述下列名詞之意涵：（每小題5 分，共 20 分）
Entity Integrity Rule
Location independence in a distributed database
SSA: Segment Search Arguments in the Hierarchical Database Model
Two Phase Locking Protocol...
```

### 6. 106年特種考試地方政府公務人員考試試題 代號：33630 全一頁等別 ： 三等考試考試時間 ： 2 小時 座 號 ：.txt - 二、
**關鍵字**: 課程, 學生, 修過, 姓名, COURSE, CreditHour, Score, 找出, 下列, 大學, SQL

```text
二、一個大學課程關聯資料庫包含下列關係：（每小題5 分，共20 分）
STUDENT(S#, Sname, Saddress, D#), TEACHER(T#, Tname, Taddress, D#),
COURSE(C#, Cname, CreditHour), TAKE_COURSE(S#, C#, Score),
OFFER(T#, C#, Classroom)
寫出下列查詢的SQL 描述...
```

### 7. 106年特種考試地方政府公務人員考試試題 代號：33630 全一頁等別 ： 三等考試考試時間 ： 2 小時 座 號 ：.txt - 三、
**關鍵字**: 設計, 醫生, 醫院, 對應, 相關, 資料, 查詢, 姓名, 病患, 電子, SQL

```text
三、一家醫院欲設計電子病歷系統，但對應窗口並無相關資訊技術，僅開出如下規格：
[醫生資料]: 姓名, 科別, 年資, [ 門診資料]: 診別, 時間, 主治醫生, [ 病患]: 姓名, 個
人資料, 另外也須紀錄[就診記錄]。
請根據想像設計一更完整的簡易醫院就診記錄查詢系統關聯資料庫，需能夠回答
的查詢，並繪出相關ER diagram。（10 分）
請根據你設計的資料庫寫出下列相對應的SQ...
```

### 8. 106年特種考試地方政府公務人員考試試題 代號：33630 全一頁等別 ： 三等考試考試時間 ： 2 小時 座 號 ：.txt - 四、
**關鍵字**: 分解, 滿足, lossless, join, 寫出, scheme, functional, dependencies, BC, CD, 3NF, BCNF

```text
四、如果scheme R = (A, B, C, D, E)，並滿足以下所有的functional dependencies
A→BC, CD→E, B→D, E→A
假設我們分解（decomposition）R 成為(A, B, C), (A, D, E)。證明這是一個lossless-join
分解。（10 分）
寫出一個lossless-join 分解使得R 分解後滿足BCNF。（10 ...
```

### 9. 106年特種考試地方政府公務人員考試試題 代號：33630 全一頁等別 ： 三等考試考試時間 ： 2 小時 座 號 ：.txt - 五、
**關鍵字**: 叢集, 解釋, 意義

```text
五、請解釋叢集索引與非叢集索引的意義與差別。（10 分）...
```

### 10. 106年公務人員特種考試警察人員、一般警察人員考試及 106年特種考試交通事業鐵路人員、退除役軍人轉任公務人員考試試題.txt - 一、
**關鍵字**: 教師, 編號, 系別, 電話, 號碼, 姓名, 助教, 底線, 屬性, key, SQL, Attribute, BASE

```text
一、有一個關聯式資料庫（Relational database ），內有下列兩個關聯（Relation），畫有實
底線的屬性（Attribute）為主鍵（Primary key），畫有虛底線的屬性為外來鍵（Foreign
key） ：
教師(教師編號, 姓名,系別,電話,研究室號碼,專長)
助教(助教編號,姓名,系別,電話,實驗室號碼,年級,教師編號)
試寫出 SQL 指令，以查詢出教師編號小於...
```

### 11. 106年公務人員特種考試警察人員、一般警察人員考試及 106年特種考試交通事業鐵路人員、退除役軍人轉任公務人員考試試題.txt - 二、
**關鍵字**: 處理, Relations, 資料, 規化, 資料庫, 設計, 過程, Normal, Form, 進行, BCNF

```text
二、在資料庫設計過程中，假設所有 Relations 都已處於第一正規形式（ First Normal
Form），若要使資料庫所有的Relations 都能處於Boyce-Codd Normal Form（BCNF 正
規形式）
則在資料庫設計過程所進行的正規化，可能需要處理這些 Relations 的那些資料狀
態？試舉例加以說明。（10 分）
試對前述所舉例，需要處理的資料狀態，進行正規...
```

### 12. 106年公務人員特種考試警察人員、一般警察人員考試及 106年特種考試交通事業鐵路人員、退除役軍人轉任公務人員考試試題.txt - 三、
**關鍵字**: 資料, 關聯式, Relational, database, create, 試問, 使用者, 使用, 管理者, View, BASE

```text
三、在關聯式資料庫（Relational database）裡，資料庫管理者可以create “View”這種東西
給使用者使用：
試問View 是什麼？（5 分）
資料庫使用View 有什麼好處？（15 分）...
```

### 13. 106年公務人員特種考試警察人員、一般警察人員考試及 106年特種考試交通事業鐵路人員、退除役軍人轉任公務人員考試試題.txt - 四、
**關鍵字**: 考試, 人員, index, 資料, 公務, 鐵路, 警察, 關聯式, Relational, database, Attribute, Index, BASE

```text
四、在關聯式資料庫（Relational database ）系統，使用者可以對 Relation 的 Attribute 建
index。試詳細說明：
建 index 可以獲得那些好處？（10 分）
建 index 需要付出那些代價？（10 分）
106年公務人員特種考試警察人員、一般警察
人員考試及 106年特種考試交通事業鐵路
人員、退除役軍人轉任公務人員考試試題
代號：70750 全一...
```

### 14. 106年公務人員特種考試警察人員、一般警察人員考試及 106年特種考試交通事業鐵路人員、退除役軍人轉任公務人員考試試題.txt - 五、
**關鍵字**: 資料, TEST, ID, 關聯式, Relational, database, Relation, 稱為, 主鍵, Primary, BASE

```text
五、有一個關聯式資料庫（Relational database ），其內有下列之關聯（Relation），關聯名
稱為 TEST，主鍵（Primary key）為ID。試問這個資料在使用上，有怎樣的問題或困
擾存在？（20 分）
TEST
ID Name Class Score Dept
01 N1 211 85 07
N2 312 90 01
05 N7 325 70 02
07 N5 512 ...
```

### 15. 114年公務人員特種考試司法人員、法務部調查局調查人員、海岸巡防人員考試及等 別：三等考試.txt - 一、
**關鍵字**: 實體, 供應, 裝備, 購買, 資訊, 調查, 代號, min, max, 新增, Entity, Relationship

```text
一、為設計某調查局資料庫，其簡化情境如下：各調查團隊（Team）有其編
號（TID）、名稱（Name），他們均會向供應商（Supplier）購買裝備
（Equipment）；供應商有其代號（SID），裝備有其編號（Eno）。每次的
購買會記錄其時間（Time），每次購買只有一個供應商，亦即不會由多個
供應商聯合提供；每次最多買 20 種裝備，每種裝備可能買若干數量
（Quantity）。下圖為實體...
```

### 16. 114年公務人員特種考試司法人員、法務部調查局調查人員、海岸巡防人員考試及等 別：三等考試.txt - 二、
**關鍵字**: read, lock, item, write, unlock, 機制, 排程, 交易, 假設, 資料, Transaction, Locking, Deadlock, Timestamp, AI

```text
二、假設資料庫對交易（Transaction）採用基本的兩階段鎖（basic two-phrase
locking）的機制，在這種機制下有可能產生死鎖（deadlock）。假設
read_item(X) 代表交易對資料項目 X 讀取，write_item(X) 代表交易對資
料項目 X 寫入新值，read_lock(X) 代表交易對 X 下 read_lock，
write_lock(X) 代表交...
```

### 17. 114年公務人員特種考試司法人員、法務部調查局調查人員、海岸巡防人員考試及等 別：三等考試.txt - 三、
**關鍵字**: 請以, 推導, 封閉, Prime, attributes, 功能, 找出, 分解, 設計, 調查, Attribute, Schema, 3NF

```text
三、為設計一個調查局的關聯式資料庫，假設有 R(A, B, C, D, E, F, G)，各屬
性均無多值（Multi-Value）現象，其功能相依如下：
FD1：G→D
FD2：{E, F}→G
FD3：F→B
FD4：D→{C, F}
FD5：G→A
請以功能相依的推導，找出{G, F}的封閉（Closure），即{G, F}+。（4 分）
請以功能相依的推導與找屬性封閉的方法，找出 R ...
```

### 18. 114年公務人員特種考試司法人員、法務部調查局調查人員、海岸巡防人員考試及等 別：三等考試.txt - 四、
**關鍵字**: TS, 屬性, Name, Salary, Job, Performance, 資料, 紀錄, 機制, 強制, Security, Access Control

```text
四、某機構使用安全機制設計資料庫，採用相較傳統作法更為嚴格的強制存
取控制（Mandatory Access Control ）機制。使用者的安全許可與資料物
件安全等級均分為四級，由高至低為 Top Secret（TS）、Secret（S）、
Confidential（C）、Unclassified（U），並採行常用的Bell-LaPadula 模式。
請分別舉例說明此模式下的「簡單安全屬性特...
```

### 19. 111年公務人員高等考試三級考試試題考試時間：2 小時 座號：.txt - 一、
**關鍵字**: 產品, 編號, 員工, 表格, 資料, 研發, 價格, 參與, 主鍵, 品名, SQL, Schema

```text
一、某一家高科技公司的關聯式資料庫包含員工、產品及研發三個表格。員
工表格記錄員工基本資料，包含員工編號、員工姓名；產品表格記錄產
品基本資料，包含產品編號、產品名稱、產品價格；研發表格記錄那些
員工參與研發那些產品的資料。這三個表格的關聯綱要（Relational
Schema）如下所示：
員工（員工編號、員工姓名）
產品（產品編號、產品名稱、產品價格）
研發（員工編號、產品編號）
加底線的屬性...
```

### 20. 111年公務人員高等考試三級考試試題考試時間：2 小時 座號：.txt - 二、
**關鍵字**: 限制, 互斥性, Model, Constraint, 父型態, 實例, 子型, Specialization, 定義, 宣告, Entity, Relationship, ER Model, EER Model, AI

```text
二、擴充實體關係模型（Extended Entity-Relationship Model, EER Model）中
的父子型態關係（Supertype/Subtype Relationship）需要宣告兩個主要的
限制：完整性限制（Completeness Constraint）與互斥性限制（Disjointness
Constraint）。（每小題 10 分，共 20 分）
完整性限制宣告父...
```

### 21. 111年公務人員高等考試三級考試試題考試時間：2 小時 座號：.txt - 三、
**關鍵字**: 資料, 資料表, 名稱, 屬性, 主鍵, 規化, 型式, 關聯式, Relational, Table

```text
三、Z(P, Q, R, S) 是一個關聯式資料表（Relational Table）的綱要，Z 為資料
表的名稱，P、Q、R、S 為資料表的四個屬性，P 為資料表的主鍵與唯一
的候選鍵。此外，該資料表有下列功能相依：（每小題 15 分，共30 分）
P Q, R, S
Q S
資料表 Z 符合第幾正規型式？原因為何？
將資料表 Z 正規化到適當的正規型式，寫出正規化之後每一個資料表
的綱...
```

### 22. 111年公務人員高等考試三級考試試題考試時間：2 小時 座號：.txt - 四、
**關鍵字**: 學習, 監督, Learning, 分類, 分群, 機器, Machine, 任務, 可區, 分為, Machine Learning

```text
四、機器學習（Machine Learning）主要任務可區分為監督式學習（Supervised
Learning）與非監督式學習（Unsupervised Learning），監督式學習包括分
類（Classification）與迴歸（Regression），非監督式學習最常用的是分群
（Clustering）。（每小題 10 分，共 20 分）
分類與迴歸要預測的值最主要的差異為何？
分類...
```

### 23. 104 年公務人員特種考試司法人員、法務部調查海岸巡防人員及移民行政人員考試試題.txt - 一、
**關鍵字**: borrower, customer, loan, 實體, Diagram, mapping, 對映, 決定, 成關, 聯式, Entity, Relationship, Schema

```text
一、對於下列實體－關係圖（ Entity-Relationship Diagram ），borrower 代表兩個實
體 customer 與 loan 之間的關係。這個關係可以是多 對多、多對一或一對一對
映（mapping）。請分別就這三種對映，決定如何將 borrower、customer 與 loan 轉
成關聯式綱目（Relational Schema）並標示其主鍵（Primary Ke...
```

### 24. 104 年公務人員特種考試司法人員、法務部調查海岸巡防人員及移民行政人員考試試題.txt - 二、
**關鍵字**: 參考, Referential, Integrity, Constraint, 舉例, 說明, 限制, 完整性, 作用, AI

```text
二、何謂參考完整性限制（ Referential-Integrity Constraint ）？這個限制的作用為何？
請舉例說明之。（20 分）...
```

### 25. 104 年公務人員特種考試司法人員、法務部調查海岸巡防人員及移民行政人員考試試題.txt - 三、
**關鍵字**: 說明, 階段, 協定, Two, Phase, Commit, Protocol, 達到, 運作, 交付, Two-Phase Commit

```text
三、何謂兩階段交付協定（ Two-Phase Commit Protocol ）？請說明它要達到的目的，
並詳細說明它的運作。（25 分）...
```

### 26. 104 年公務人員特種考試司法人員、法務部調查海岸巡防人員及移民行政人員考試試題.txt - 四、
**關鍵字**: customer, 說明, loan, 分散式, 資料, Semi, join, 用來, Join, 時間

```text
四、在分散式資料庫裡，半合併運算（ Semi-join）被用來降低合併運算（ Join）之處理
時間。請說明半合併運算之運算模式，並說明為何它能降低合併運算之處理時間。
（25 分）
customer-name customer-street
customer-id customer-city
customer borrower loan
loan-number amount...
```

### 27. 107年公務人員高等考試三級考試試題 代號：36370 全一張考試時間： 2 小時 座 號 ：.txt - 一、
**關鍵字**: 醫師, 科別, 人員, 代號, 科系, 資料, 護理, 時段, 系統, 病患, BCNF

```text
一、請為如下的醫療院所設計符合BCNF 且考量OO 的 EER data model，model 中請註明
合適的 primary/foreign/candidate keys ，資料表間的關聯亦請適當地說明彼此間的
maximum/minimum cardinality。註：不需要用到的資料不必列入。（30 分）
• 假設一位醫師或護理人員只會屬於一個科別，但可以支援其它科別的門診
• 假設某一...
```

### 28. 107年公務人員高等考試三級考試試題 代號：36370 全一張考試時間： 2 小時 座 號 ：.txt - 二、
**關鍵字**: 醫療, nID, 資料, pID, mID, 次數, 推拿, MedicalRecord, ref, 相關, SQL

```text
二、假設現有如下推拿就醫資訊的關連式資料庫，請使用SQL 回答相關的子問題。
Naprapathist(nID
, name, speciality)
Patient(pID, name, gender, birthday)
MedicalItem(mID, subject, description, charge)
MedicalRecord(mID, nID, pID, dateTime, e...
```

### 29. 107年公務人員高等考試三級考試試題 代號：36370 全一張考試時間： 2 小時 座 號 ：.txt - 三、
**關鍵字**: ID, Name, CandidateID, CandidateName, Introduction, Birthday, Score, oteID, BB, 資料, RDB, BCNF, Key-Value

```text
三、請將如下的投票物件陣列Key-Value資料，以符合BCNF 的RDB 資料表來表示。（15 分）
假設：一個ID 只能投一票
[{’CandidateID’: ’C01’, ’CandidateName’: ’Mary Wang’,
’Introduction’: ’Rock’, ’Birthday’: ’2000/01/01’, ’Score’: ’2’,
’V oteID’:[ {’ID...
```

### 30. 107年公務人員高等考試三級考試試題 代號：36370 全一張考試時間： 2 小時 座 號 ：.txt - 四、
**關鍵字**: 排程, 循序, 執行, 序列, 設現, transactions, 資料, conflict, equivalent, 說明, Transaction

```text
四、假設現有如圖三個transactions 同步存取資料A, B, C，請使用conflict equivalent 說明
圖中同步執行的非序列排程（ non-serial schedule ），是否具有排程循序性
（serializability）；如果具備排程循序性，執行結果可以等同於三個Transactions 的那
種序列排程；如果不具排程循序性，衝突的cycle 為何？（15 分）...
```

### 31. 107年公務人員高等考試三級考試試題 代號：36370 全一張考試時間： 2 小時 座 號 ：.txt - 五、
**關鍵字**: 銷售, 金額, Map, Reduce, 年度, 電商, 資料, 國別, 解說, 運算

```text
五、以跨國電商年度銷售資料（國別、日期、銷售金額…）為例，圖解說明 Map-Reduce
的運算架構，並說明Map, Shuffle, 跟 Reduce 是如何分工而得到年度區域（如亞洲、
歐洲、非洲、美洲、大洋洲）的總銷售金額？（20 分）...
```

### 32. 107年公務人員特種考試司法人員、法務部人員、海岸巡防人員及移民行政人員考試試題等 別：三等考試.txt - 一、
**關鍵字**: 資料, 試說, 員工, 儲存, oriented, Database, 鍵值, 資料表, 網路, 文件, SQL, NoSQL, Big Data, Key-Value, BASE

```text
一、在大數據（Big Data）時代，NoSQL資料庫已經是最常被使用的資料儲存解決
方案，而在各種NoSQL資料庫中，文件式資料庫（Document-oriented Database）
及鍵值式資料庫（Key-Value-oriented Database）為目前最常被使用的資料庫：
試說明文件式資料庫及鍵值式資料庫的資料儲存特性。（16 分）
若某一傳統關聯式資料庫有以下員工資料表，試說...
```

### 33. 107年公務人員特種考試司法人員、法務部人員、海岸巡防人員及移民行政人員考試試題等 別：三等考試.txt - 二、
**關鍵字**: 資料, 傳統, 關聯式, Relational, 進展, 說明, 庫列, 實例, 特性, SQL, NoSQL, NewSQL

```text
二、資料庫從傳統關聯式（Relational）持續進展至最近的NoSQL 及 NewSQL
等新一代資料庫，試說明此三種資料庫的特性，並針對每一種資料庫列
舉三個實例。（25 分）...
```

### 34. 107年公務人員特種考試司法人員、法務部人員、海岸巡防人員及移民行政人員考試試題等 別：三等考試.txt - 三、
**關鍵字**: 磁碟, 技術, 資料, 遺失, 代號, 分成, 特性, 描述, 做法, 可用, AI

```text
三、磁碟陣列RAID 技術可用來提供容錯功能，以避免資料遺失，其做法可以
分成很多種等級，試描述這些不同等級RAID 的特性及優缺點。（20 分）
代號：41250
61050
頁次：2－2...
```

### 35. 107年公務人員特種考試司法人員、法務部人員、海岸巡防人員及移民行政人員考試試題等 別：三等考試.txt - 四、
**關鍵字**: 供應, 貨品, 付款, 資料, 系統, 帳單, 實體, 企業, 計畫, 開發

```text
四、某企業計畫開發一套資料庫應用系統，其需求如下所述：
需儲存供應其貨品的供應商相關資料，包含有供應商編號、名稱、地
址、聯繫人姓名及電話號碼。
對於每次貨品供應，需建立一個帳單以儲存此次供應的日期、金額、
付款期限以及有關說明。
每筆帳單的付款，可以在不同的時間以不同的方式支付（例如：現金、
支票、信用卡），並記錄每次付款的日期及方式。
每個供應商可以多次供應貨品，唯每日最多只能供貨一次...
```

### 36. 114年公務人員特種考試警察人員、一般警察人員、國家安全局國家安全情報人員、移民行政人員考試及114年特種考試退除役軍人轉任公務人員考試試題考 試 別：一般警察人員考試等 別：三等考試.txt - 一、
**關鍵字**: 單位, 代號, 案件, 受理, 人員, 資料, 假設, 時間, 報案, 查詢, BCNF

```text
一、請設計符合BCNF且考量OO（物件導向）的Enhanced-ER(EER)data model，
可以滿足如下受（處）理案件證明案管理的需求，model 中需註明合適的
primary/foreign key，及資料表彼此關聯的maximum/minimum cardinality。
（30 分）
註：題目中不需要用到的資料，請不要列入到資料表中。
假設：各受理單位代號具有唯一性，受理單位名稱...
```

### 37. 114年公務人員特種考試警察人員、一般警察人員、國家安全局國家安全情報人員、移民行政人員考試及114年特種考試退除役軍人轉任公務人員考試試題考 試 別：一般警察人員考試等 別：三等考試.txt - 二、
**關鍵字**: Clinic, ID, No, 醫師, 診所, 金額, Doctor, 自費, 業績, PK, SQL, AI

```text
二、假設現有如下連鎖診所醫師服務點數紀錄的關連式資料庫，請使用 SQL
回答下列子問題。（每小題 5 分，共 20 分）
Clinic(Clinic_No, name, area) PK: Clinic_No
Doctor(ID, name, gender, issuing_date, specialty, hire_date, Clinic_No) PK: ID
FK: Clinic_No re...
```

### 38. 114年公務人員特種考試警察人員、一般警察人員、國家安全局國家安全情報人員、移民行政人員考試及114年特種考試退除役軍人轉任公務人員考試試題考 試 別：一般警察人員考試等 別：三等考試.txt - 三、
**關鍵字**: 代號, 行員, 銀行, 幣別, 時間, 匯率, 數量, 金額, 資料, 分行, RDB, BCNF, JSON

```text
三、請以符合 BCNF 的 RDB 資料表來表示如下 json 格式的銀行換匯資料，
正規化後的資料表欄位，需同時註明 primary/foreign keys ，並將資料填
入正規化後的資料表內。（30 分）
[{"銀行代號":"B01","分行代號":"x01","行員代號":"E01","行員名字":"Bob",
"幣別":"USD","換匯時間":"1140502-100000","匯率"...
```

### 39. 114年公務人員特種考試警察人員、一般警察人員、國家安全局國家安全情報人員、移民行政人員考試及114年特種考試退除役軍人轉任公務人員考試試題考 試 別：一般警察人員考試等 別：三等考試.txt - 四、
**關鍵字**: 資料, 時間, T1, T6, 設現, 說明, system, failure, 採用, log, Log, Undo, Redo, BASE, AI

```text
四、假設現有如下資料庫交易時間軸，請分別就時間點 5 及 10，說明system
failure 時，採用 log-base immediate update 資料庫更新方法時，T1~T6 是
否需 redo or undo。（12 分）
Failure Time T1 T2 T3 T4 T5 T6
5
10
代號：30440
頁次：4－4...
```

### 40. 114年公務人員特種考試警察人員、一般警察人員、國家安全局國家安全情報人員、移民行政人員考試及114年特種考試退除役軍人轉任公務人員考試試題考 試 別：一般警察人員考試等 別：三等考試.txt - 五、
**關鍵字**: Concurrency, Control, OCC, 加鎖, deadlock, 是否, 同步控制, 避免, 說明, 資料, Concurrency Control, Locking, Two-Phase Locking, 2PL, Deadlock, Timestamp, Optimistic Concurrency Control, MVCC

```text
五、請列表分別說明資料庫同步控制 Two-Phase Locking(2PL), Timestamp
Ordering(TO), Optimistic Concurrency Control(OCC), Multi-version
Concurrency Control(MVCC) 等方法，是否需要加鎖，及是否可避免
deadlock。（8 分）
2PL TO OCC MVCC
是否需要加鎖
是否...
```

### 41. 113年公務人員特種考試警察人員、一般警察人員、國家安全局國家安全情報人員及移民行政人員考試試題考 試 別：一般警察人員考試等 別：三等考試.txt - 一、
**關鍵字**: 管理系, 資料, 闡述, Database, Management, System, 舉出, 功能, BASE

```text
一、闡述資料庫管理系統（Database Management System）的功能，另外舉出
三種常用的資料庫管理系統。（15 分）...
```

### 42. 113年公務人員特種考試警察人員、一般警察人員、國家安全局國家安全情報人員及移民行政人員考試試題考 試 別：一般警察人員考試等 別：三等考試.txt - 二、
**關鍵字**: 資料, 分散式, 闡述, 特點, 優缺點, 集中式

```text
二、請闡述分散式資料庫與集中式資料庫的特點與各自的優缺點。（15 分）...
```

### 43. 113年公務人員特種考試警察人員、一般警察人員、國家安全局國家安全情報人員及移民行政人員考試試題考 試 別：一般警察人員考試等 別：三等考試.txt - 三、
**關鍵字**: Read, 解釋, 資料庫, 領域, Composite, Dirty, 幻讀, Phantom, 下列, Attribute

```text
三、請解釋下列資料庫領域之專有名詞：
複合屬性（Composite Attribute）（5 分）
髒讀（Dirty Read）（5 分）
幻讀（Phantom Read）（5 分）...
```

### 44. 113年公務人員特種考試警察人員、一般警察人員、國家安全局國家安全情報人員及移民行政人員考試試題考 試 別：一般警察人員考試等 別：三等考試.txt - 四、
**關鍵字**: 程序, 闡述, 何謂, 預存, Store, Procedure, 觸發, 敘述, 優點, Trigger

```text
四、闡述何謂預存程序（Store Procedure）與觸發程序（Trigger），以及敘述
它們各自的優點？（15 分）...
```

### 45. 113年公務人員特種考試警察人員、一般警察人員、國家安全局國家安全情報人員及移民行政人員考試試題考 試 別：一般警察人員考試等 別：三等考試.txt - 五、
**關鍵字**: 闡述, 界視, VIEW, 優缺點, 代號, 用途, View

```text
五、請闡述界視表（VIEW）的用途與優缺點。（15 分）
代號：30540
頁次：2－2...
```

### 46. 113年公務人員特種考試警察人員、一般警察人員、國家安全局國家安全情報人員及移民行政人員考試試題考 試 別：一般警察人員考試等 別：三等考試.txt - 六、
**關鍵字**: Product, Sales, table, Supplier, ID, name, S003, amount, SELECT, SupplyID, SQL

```text
六、資料庫內有三個表格，分別是 Product、Sales_table、Supplier。這三個表
的欄位名稱與資料紀錄如下：
Product Table
ID name SupplyID
P001 玄天花 S001
P002 仙草 S003
P003 吉梗 S002
P006 辣椒 S001
P007 富士蘋果 S003
P008 岡山羊 S002
P009 台南牛肉 S003
Sales_ta...
```

### 47. 114年公務人員高等考試三級考試試題考試時間：2 小時 座號：.txt - 一、
**關鍵字**: 說明, EER, Enhanced, 構成, 應用, Supertype, Subtype, 下列, 例子, 要素, Entity, Attribute, Relationship

```text
一、說明下列 EER 模型（Enhanced Entity Relationship ）的四個構成要素，
並各舉一個具體例子說明其在真實世界中的應用⑴Entity, ⑵Attribute,
⑶Relationship, ⑷Supertype/Subtype。（20 分）...
```

### 48. 114年公務人員高等考試三級考試試題考試時間：2 小時 座號：.txt - 二、
**關鍵字**: Read, 隔離, 級別, 資料, Committed, 事務, 差異, 實際, Repeatable, 說明

```text
二、請說明下列兩種事務隔離級別的差異，並針對每種隔離級別各舉一個可
能造成資料不一致的實際情境：⑴Read Committed, ⑵Repeatable Read。
（10 分）此外，請說明為何某些資料庫系統預設使用Read Committed而非
Serializable。（10 分）...
```

### 49. 114年公務人員高等考試三級考試試題考試時間：2 小時 座號：.txt - 三、
**關鍵字**: 金額, 客戶, 訂單, 總量, 付款, 資料, CID, OID, TotalAmount, OrderDate, SQL, AI

```text
三、根據下列客戶訂單資料回答相關查詢SQL敘述，資料表格為：Customer(CID,
Name), Orders(OID, CID, TotalAmount, OrderDate), Payment(PID, OID,
AmountPaid)。（每小題 10 分，共 30 分）
在 OrderDate 為“2025.01.01”當天，所有客戶訂單總量排行，依總量由
高到低列出客戶姓名與總量。
...
```

### 50. 114年公務人員高等考試三級考試試題考試時間：2 小時 座號：.txt - 四、
**關鍵字**: 意義, 性質, 帳戶, 餘額, 情境, 說明, 資料, 處理, 衝突, 違反, ACID, Atomicity, Consistency, Isolation, Durability

```text
四、請說明資料庫交易處理中的ACID意義與其四大性質（Atomicity, Consistency,
Isolation, Durability）分別意義為何，（15 分）並針對下列交易衝突情境，
指出可能違反的ACID 性質與造成的後果，情境：T1 在更新帳戶 A 餘額
後尚未提交（commit），T2 同時讀取帳戶 A 的餘額並執行轉帳。（15 分）...
```


## 3. 建議的初步分類架構 (基於關鍵字群聚)

*(此部分由 AI 根據統計結果後續分析生成)*
