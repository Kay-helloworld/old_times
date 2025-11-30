# 資料庫應用 - 知識點分析報告 (改進版 v2)

**分析檔案數量**: 74 份

**分析方法**: 按練習方式分類（上機實作 vs 紙筆推導 vs 理論概念）

**允許重複計算**: 複合題目會同時出現在多個分類（這是合理的）

---

## 📈 近三年趨勢分析 (112-114 vs 全部)

| 知識點類別 | 歷年全部 | 近三年 | 114年 | 近三年佔比 |
| :--- | :---: | :---: | :---: | :---: |
| 1. SQL實作 (SQL Practice) | 346 | 74 | 30 | 21.4% |
| 2. 資料庫設計 (DB Design) | 280 | 84 | 23 | 30.0% |
| 3. 正規化 (Normalization) | 414 | 99 | 28 | 23.9% |
| 4. 交易管理 (Transaction Management) | 506 | 196 | 107 | 38.7% |
| 5. 索引與儲存 (Indexing & Storage) | 62 | 13 | 3 | 21.0% |
| 6. 進階主題 (Advanced Topics) | 238 | 36 | 10 | 15.1% |
| 7. 資訊安全 (Security) | 22 | 6 | 6 | 27.3% |

---

## 📊 考試類型比較 (全部 vs 地特 vs 高考)

| 知識點類別 | 全部 | 地方政府 | 高考三級 |
| :--- | :---: | :---: | :---: |
| 1. SQL實作 (SQL Practice) | 346 | 56 | 40 |
| 2. 資料庫設計 (DB Design) | 280 | 53 | 44 |
| 3. 正規化 (Normalization) | 414 | 81 | 60 |
| 4. 交易管理 (Transaction Management) | 506 | 61 | 101 |
| 5. 索引與儲存 (Indexing & Storage) | 62 | 16 | 2 |
| 6. 進階主題 (Advanced Topics) | 238 | 22 | 55 |
| 7. 資訊安全 (Security) | 22 | 0 | 1 |

---

## 📝 詳細考點關鍵字

### 1. SQL實作 (SQL Practice)

```
CREATE TABLE, ALTER TABLE, DROP TABLE, PRIMARY KEY, FOREIGN KEY, REFERENCES, SELECT, INSERT, UPDATE, DELETE, JOIN, INNER JOIN, LEFT JOIN, RIGHT JOIN, GROUP BY, HAVING, ORDER BY, WHERE, DISTINCT, UNION, COUNT, SUM, AVG, MAX, MIN, VIEW, CREATE VIEW, 視圖, TRIGGER, 觸發器, STORED PROCEDURE, 預存程序, CURSOR, 游標, SUBQUERY, 子查詢, IN (SELECT, EXISTS
```

### 2. 資料庫設計 (DB Design)

```
ER Model, ERD, ER Diagram, 實體關係圖, Entity-Relationship, E-R Model, EER, Enhanced ER, Enhanced Entity, 擴充實體關係, Entity Type, 實體型態, Relationship Type, 關聯型態, Weak Entity, 弱實體, Identifying Relationship, Cardinality, 基數, Multiplicity, Participation, 參與, One-to-One, 1:1, 一對一, One-to-Many, 1:N, 一對多, Many-to-Many, M:N, 多對多, Supertype, Subtype, 超類別, 子類別, Specialization, 特殊化, Generalization, 一般化, ISA, is-a, Aggregation, 聚合, Composite Attribute, 複合屬性, Multivalued Attribute, 多值屬性, Derived Attribute, 衍生屬性, Mapping, 對映, Relational Schema, 關聯綱要
```

### 3. 正規化 (Normalization)

```
Normalization, 正規化, Normal Form, 1NF, First Normal Form, 第一正規, 2NF, Second Normal Form, 第二正規, 3NF, Third Normal Form, 第三正規, BCNF, Boyce-Codd, 4NF, Fourth Normal Form, Functional Dependency, 功能相依, FD, Partial Dependency, 部分相依, Transitive Dependency, 遞移相依, Multivalued Dependency, 多值相依, MVD, Closure, 封閉, Armstrong, Armstrong's Axioms, Candidate Key, 候選鍵, Prime Attribute, Non-Prime Attribute, Superkey, 超鍵, Decomposition, 分解, Lossless Join, 無失真, 無損連接, Dependency Preserving
```

### 4. 交易管理 (Transaction Management)

```
Transaction, 交易, 事務, ACID, Atomicity, Consistency, Isolation, Durability, 原子性, 一致性, 隔離性, 持久性, Concurrency Control, 並行, 並發, Schedule, 排程, Serial, Serializable, 可序列, Conflict Serializable, View Serializable, Lock, 鎖定, Locking, Shared Lock, S-Lock, Exclusive Lock, X-Lock, Two-Phase Locking, 2PL, 兩階段鎖, Deadlock, 死結, 死鎖, Wait-for Graph, Timestamp, 時間戳, Isolation Level, Read Uncommitted, Read Committed, Repeatable Read, Dirty Read, 髒讀, Non-Repeatable Read, Phantom Read, 幻讀, Lost Update, Recovery, 復原, Recover, Log, 日誌, Logging, Checkpoint, 檢查點, Undo, Redo, Write-Ahead Log, WAL, Commit, Rollback
```

### 5. 索引與儲存 (Indexing & Storage)

```
Index, 索引, Indexing, Clustered Index, 叢集索引, Non-Clustered Index, Secondary Index, B-Tree, B Tree, B樹, B+Tree, B+ Tree, B+樹, B*Tree, Hash Index, 雜湊索引, Hash Function, 雜湊函數, Bucket, 桶, Linear Hashing, Extendible Hashing, Storage, 儲存, File Organization, Heap File, 堆積檔, Sequential File, Buffer, 緩衝區, RAID, Striping, Mirroring, Parity
```

### 6. 進階主題 (Advanced Topics)

```
Distributed Database, 分散式資料庫, Fragmentation, 片段化, Replication, 複製, Two-Phase Commit, 2PC, CAP Theorem, NoSQL, Key-Value Store, Document Store, Column-Family, Graph Database, MongoDB, Redis, Cassandra, BASE, Eventually Consistent, Big Data, 大數據, Hadoop, MapReduce, Spark, HDFS, Data Lake, Data Warehouse, 資料倉儲, OLAP, OLTP, Data Mart, Star Schema, Snowflake Schema, Fact Table, Dimension Table, ETL, Data Mining, 資料探勘, Association Rule, 關聯規則, Classification, 分類, Clustering, 分群
```

### 7. 資訊安全 (Security)

```
Security, 資安, 安全性, Information Security, Encryption, 加密, Decryption, 解密, Cryptography, 密碼學, Symmetric, Asymmetric, Public Key, Private Key, Authentication, 認證, Authorization, 授權, Access Control, 存取控制, RBAC, DAC, MAC, Grant, Revoke, SQL Injection, SQL隱碼, Injection Attack, Prepared Statement, Parameterized Query, Audit, 稽核, Auditing
```

---

## 💡 說明

- **分類原則**: 按練習方式分類，而非傳統學術分類
- **重複計算**: 一個複合題可能同時包含SQL和設計，會被計算兩次
- **關鍵字選擇**: 更明確的詞彙，減少誤判
- **資料來源**: 僅限資料庫應用科目考卷，不含資料結構考卷
