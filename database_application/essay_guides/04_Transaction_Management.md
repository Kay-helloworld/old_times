# 04 Transaction Management

總題數: 38

---

### 題目 1 (114年)

**來源**: `114年公務人員特種考試司法人員、法務部調查局調查人員、海岸巡防人員考試及等 別：三等考試.txt`
**關鍵字**: read, lock, item, write, unlock...

二、假設資料庫對交易（Transaction）採用基本的兩階段鎖（basic two-phrase
locking）的機制，在這種機制下有可能產生死鎖（deadlock）。假設
read_item(X) 代表交易對資料項目 X 讀取，write_item(X) 代表交易對資
料項目 X 寫入新值，read_lock(X) 代表交易對 X 下 read_lock，
write_lock(X) 代表交易對 X 下 write_lock，其餘類推。T1、T2 兩個交
易原先期待進行的內容如下表左右兩欄。實際上系統不是序列化（Serial）
排程，而是將交易交織進行。假設在兩個交易交織進行的α排程
（Schedule），T2 在時戳（Timestamp）為1000 時開始，T1 在時戳為1010
時開始。在這個α排程下，系統偵測到有死鎖產生的可能。
請繪出其可能導致死鎖的等待圖（wait-for graph），其中必須標註等待
的資源。（5 分）
在上述α排程下，資料庫管理系統有死鎖預防機制（deadlock prevention
scheme）以避免死鎖，下列各種不同機制，請說明每個交易分別會發
生的情況。
⑴採 Wait-die。（5 分）
⑵採 Wound-wait。（5 分）
⑶採 No waiting。（5 分）
⑷採 Cautious waiting。（5 分）
T1 T2
read_lock(A); read_lock(C);
read_item(A); read_item(C);
read_lock(B);
read_item(B);
B:=5A*20000;
write_lock(C);
read_item(C);
write_lock(A);
A:=A+C;
write_item(A);
unlock(C);
unlock(B);
C:=B-5000*C;
write_item(C);
unlock(A);
unlock(B);
unlock(C);
代號：41550
頁次：3－3

---

### 題目 2 (114年)

**來源**: `114年公務人員特種考試警察人員、一般警察人員、國家安全局國家安全情報人員、移民行政人員考試及114年特種考試退除役軍人轉任公務人員考試試題考 試 別：一般警察人員考試等 別：三等考試.txt`
**關鍵字**: 資料, 10, T1, T6, 假設...

四、假設現有如下資料庫交易時間軸，請分別就時間點 5 及 10，說明system
failure 時，採用 log-base immediate update 資料庫更新方法時，T1~T6 是
否需 redo or undo。（12 分）
Failure Time T1 T2 T3 T4 T5 T6
5
10
代號：30440
頁次：4－4

---

### 題目 3 (114年)

**來源**: `114年公務人員特種考試警察人員、一般警察人員、國家安全局國家安全情報人員、移民行政人員考試及114年特種考試退除役軍人轉任公務人員考試試題考 試 別：一般警察人員考試等 別：三等考試.txt`
**關鍵字**: 2PL, Concurrency, Control, OCC, MVCC...

五、請列表分別說明資料庫同步控制 Two-Phase Locking(2PL), Timestamp
Ordering(TO), Optimistic Concurrency Control(OCC), Multi-version
Concurrency Control(MVCC) 等方法，是否需要加鎖，及是否可避免
deadlock。（8 分）
2PL TO OCC MVCC
是否需要加鎖
是否可避免deadlock

---

### 題目 4 (114年)

**來源**: `114年公務人員高等考試三級考試試題考試時間：2 小時 座號：.txt`
**關鍵字**: Read, 資料, Committed, 10, 說明...

二、請說明下列兩種事務隔離級別的差異，並針對每種隔離級別各舉一個可
能造成資料不一致的實際情境：⑴Read Committed, ⑵Repeatable Read。
（10 分）此外，請說明為何某些資料庫系統預設使用Read Committed而非
Serializable。（10 分）

---

### 題目 5 (114年)

**來源**: `114年公務人員高等考試三級考試試題考試時間：2 小時 座號：.txt`
**關鍵字**: ACID, 性質, 15, 帳戶, 餘額...

四、請說明資料庫交易處理中的ACID意義與其四大性質（Atomicity, Consistency,
Isolation, Durability）分別意義為何，（15 分）並針對下列交易衝突情境，
指出可能違反的ACID 性質與造成的後果，情境：T1 在更新帳戶 A 餘額
後尚未提交（commit），T2 同時讀取帳戶 A 的餘額並執行轉帳。（15 分）

---

### 題目 6 (114年)

**來源**: `114年公務、關務人員升官等考試、114年交通事業郵政、港務人員升資考試試題.txt`
**關鍵字**: 備份, 闡述, 差異備, WAL, Log...

四、闡述備份與復原策略中的「完整備份、差異備份、交易日誌（WAL/Log）
備份」三者的差異與搭配方式，並概述災難復原（DR）兩個 R 指標。
（20 分）

---

### 題目 7 (113年)

**來源**: `113 年公務人員特種考試司法人員、法務部調查局等 別：三等考試.txt`
**關鍵字**: 資料, 硬碟, 交易, 記憶體, 時間序...

三、假設一個交易（transaction）有五種基本運算，分別是⑴begin（T）：交易
T 開始；⑵read（Y , y）：將硬碟資料項 Y 讀到主記憶體變數 y；⑶write
（y , Y）：將主記憶體變數 y 寫到硬碟資料項 Y；⑷commit（T）：交易 T
提交，表示 T 成功結束；⑸rollback（T）：交易 T 被駁回。
假設資料庫紀錄檔（database log）中用五種方式記錄交易的運算，分別
為：⑴[start, T]：交易T 開始；⑵[read, T, Y]：交易T 讀取資料項Y；⑶
[write, T, Y ,更新前的值, 更新後的值]：交易T 更新資料項Y；⑷[commit,
T]：交易T 提交；⑸[rollback, T]：交易T 被駁回。
在 WAL（Write-Ahead Logging）機制下，考慮交易T0、T1、T2 和 T3 四
個交易及以下的排程，
假設資料項之初始值 X=100、Y=425 和 Z=800，且記憶體夠大，作業系
統不主動將記憶體緩衝區的資料或 LOG 紀錄寫回硬碟，回答以下問題。
（每小題 10 分，共 30 分）
執行時間序 8 之後（時間序 9 之前），記憶體和硬碟中資料項和紀錄
檔的內容各為何？
執行時間序 16 之後（時間序 17 之前），記憶體和硬碟中資料項和紀
錄檔的內容各為何？
發生系統當機，系統復原後硬碟中資料項X、Y 和Z 的值為何？
代號：41550
頁次：3－3

---

### 題目 8 (113年)

**來源**: `113年公務人員特種考試關務人員、身心障礙人員考試及113年國軍上校以上軍官轉任公務人員考試試題考 試 別：關務人員考試等 別：三等考試.txt`
**關鍵字**: 排程, 循序, 四筆, 執行, 具備...

四、假設現有如下 T1, T2, T3, T4 四筆交易同步存取帳號資料 x, y ，請以
conflict equivalent 的觀念，繪圖說明這四筆交易的執行排程，並說明這四
筆交易是否具備排程循序性（serializability）？如果具備排程循序性，則此
四筆交易的執行順序應為何，才不會出現衝突？如果不具備排程循序性，
則衝突的 cycle 有那些？（20 分）
註：R 表示讀取，W 表示寫入

---

### 題目 9 (112年)

**來源**: `112年公務人員高等考試三級考試試題考試時間： 2 小時 座號：.txt`
**關鍵字**: read, write, transaction, Schedule, 行程...

三、給予下列二個行程（Schedules）A與B，請用一圖形演算法，利用行程中
的讀（Read）與寫（Write）動作（Operations）構成圖形，圖形邊（Edge）
上標示讀寫的資料項目（Data Items），以此演算法論述A與B兩行程是否
具序列性（Serializability）？如具序列性，請寫出對等序列行程（Equivalent
Serial Schedule）。（25分）
(a) transaction T1 transaction T2 transaction T3
Time
read(X);
write(X);
read(Y);
write(Y);
read(Z);
read(Y);
write(Y);
read(X);
write(X);
read(Y);
read(Z);
write(Y);
write(Z);
Schedule A
(b) transaction T1 transaction T2 transaction T3
Time
read(X);
write(X);
read(Y);
write(Y);
read(Z);
read(Y);
write(Y);
read(X);
write(X);
read(Y);
read(Z);
write(Y);
write(Z);
Schedule B

---

### 題目 10 (112年)

**來源**: `112 年特種考試地方政府公務人員考試試題等 別：三等考試考試時間：2 小時 座號：.txt`
**關鍵字**: item, T3, write, read, transaction...

四、有 5 個交易（transactions）T1, T2, T3, T4, T5，在被執行時，形成以下的
程序（schedule ），假設該資料庫管理系統的恢復機制（recovery
mechanism）使用的是延遲更新協定（deferred update protocol）。並且假
設系統在查核點時（checkpoint），會使所有正在執行的交易工作暫停，
將已經完成的交易（committed transaction）的結果，強迫儲存（force write）
到二線儲存器（secondary storage）。請說明這5 個交易在系統當機後，重
新恢復時，各需要對這5 個交易作什麼處置，並說明理由。（25 分）
[start-transaction, T1]
[read_item, T1, A]
[start-transaction, T3]
[read_item, T3, C]
[write_item, T1, A, 10]
[start-transaction, T4]
[read_item, T4, D]
[commit, T1]
[write_item, T3, C, 20]
[checkpoint]
[read_item, T3, E]
[write_item, T4, D, 30]
[start-transaction, T2]
[write_item, T3, E, 40]
[commit, T3]
[read_item, T2, B]
[start-transaction, T5]
[write_item, T2, B, 50]
[read_item, T5, G]
[commit, T2]
[read_item, T4, H]
[write_item, T5, G, 60]
← system crash

---

### 題目 11 (112年)

**來源**: `112年公務人員特種考試司法人員、法務部調查局調查人員、海岸巡防人員、移民行政人員考試及112年未具擬任職務任用資格者取得法官遴選資格考試試題等 別：三等考試.txt`
**關鍵字**: 資料, 紀錄, Update, undo, redo...

四、請以 Log-Based Recovery 資料復原模式為例，就如下的交易紀錄進行程
序，以表格說明 Deferred Update 及 Immediate Update （包括 undo/redo
及 undo/no-redo 兩種更新模式），在 t5 or t9 時間點，發生非毀滅性系統
故障（兩個時間的系統故障屬獨立事件），T1~T6 交易紀錄應採取那種動
作，來進行資料的復原？（20 分）

---

### 題目 12 (112年)

**來源**: `112年公務人員特種考試警察人員、一般警察人員、國家安全局國家安全情報人員考試及112年特種考試交通事業鐵路人員、退除役軍人轉任公務人員考試試題考 試 別：國家安全情報人員考試等 別：三等考試.txt`
**關鍵字**: 管理系, 明資料, 統為, 什麼, 並行...

一、請先說明資料庫管理系統為什麼需要做「並行控制」（Concurrency
Control），並請定義並行控制所使用的「兩階段鎖定協定」（Two-Phase
Locking Protocol）。（20 分）

---

### 題目 13 (111年)

**來源**: `111年公務人員特種考試關務人員、身心障礙人員考試及111年國軍上校以上軍官轉任公務人員考試試題考 試 別：關務人員考試等 別：三等考試.txt`
**關鍵字**: 異動, ACID, 四個, 關聯式, 資料...

三、關聯式資料庫系統在實作異動處理（Transaction Processing）時，大多希望
能符合 ACID 四個特性以確保資料庫內容的正確性。假設一個異動欲從 P
帳戶轉 1000 元到 Q 帳戶，其中包含的六個指令如下表所示。請以該異動
具體說明 ACID 所代表的四個要求分別為何？若沒有達到該要求會造成
什麼不良的影響？（20 分）

---

### 題目 14 (111年)

**來源**: `111年公務人員特種考試司法人員、法務部調查局調查人員、海岸巡防人員、移民行政人員考試及111年未具擬任職務任用資格者取得法官遴選資格考試試題等 別：三等考試.txt`
**關鍵字**: 機制, 請定, 並行, 10, 義多...

四、請定義多使用者資料庫系統（multi-user database systems）中所使用的
並行控制（concurrency control）機制。（10 分）
鎖定（locking）機制為最常使用的一種並行控制機制，請定義之。
（10 分）

---

### 題目 15 (110年)

**來源**: `110年公務人員特種考試警察人員、一般警察人員、國家安全局國家安全情報人員考試及110年特種考試交通事業鐵路人員、退除役軍人轉任公務人員考試試題考 試 別：一般警察人員考試等 別：三等考試.txt`
**關鍵字**: transactions, 排程, 三個, conflict, 執行...

二、假設現有如下 T1, T2, T3 三個 transactions，同步存取資料 X, Y , Z，請以
conflict equivalent 的觀念，繪圖說明這三個 transactions 的執行排程，是
否具備排程循序性（serializability）？如果具備排程循序性，則此三個
transactions 的執行順序應為何，才不會出現 conflict？如果不具備排程循
序性，則衝突的cycle 有那些？（20 分）
註：R 表示讀取，W 表示寫入

---

### 題目 16 (110年)

**來源**: `110 年特種考試地方政府公務人員考試試題等 別：三等考試考試時間：2 小時 座號：.txt`
**關鍵字**: 敘述, 難題, 何謂, 資料, 讀取...

四、在多使用者多工的資料庫管理系統（Database Management System ），多
個交易（Transactions）在同步執行（Concurrently Performed ）時，有可
能發生資料讀取之難題（issue）。請回答下列相關問題：
請敘述何謂交易？（4 分）
請敘述何謂更新遺失（Lost Updates）的難題？（4 分）
請敘述何謂讀到髒資料（Dirty Read）的難題？（4 分）
請敘述何謂無法重複讀取（Non-Repeatable Read）難題？（4 分）
同步控制方法（Concurrency Control Method ）可運用來解決前述的難
題。其中有一種以鎖為基礎之協定（Lock-Based Protocol），請敘述其
運作機制。（4 分）
代號：34230
頁次：3－3

---

### 題目 17 (110年)

**來源**: `110年公務人員特種考試司法人員、法務部調查局調查人員、海岸巡防人員、移民行政人員考試及110年未具擬任職務任用資格者取得法官遴選資格考試試題等 別：三等考試.txt`
**關鍵字**: 資料, 處理, 何謂, Transaction, 行程...

三、在資料庫處理，交易處理的資料庫存取指令（Access Operations）包括那
些？何謂交易（Transactions）？何謂行程（Schedules）？一行程由多個
交易組成，一行程的執行會產生那些問題？在資料庫管理系統（DBMS）
的並行控制和回復機制要強制交易處理達到那些特性（Desirable
Properties of Transactions）？請論述之。（25 分）

---

### 題目 18 (110年)

**來源**: `110年公務人員特種考試司法人員、法務部調查局調查人員、海岸巡防人員、移民行政人員考試及110年未具擬任職務任用資格者取得法官遴選資格考試試題等 別：三等考試.txt`
**關鍵字**: item, read, write, Schedule, T1...

四、給予下列四個行程 A、B、C、D，依優先序圖形（Precedence Graph ），
請論述那一行程不具序列性（Serializability）。（25 分）
Schedule A Schedule B
T1 T2 T1 T2
read_item(Y);
Y:=Y-N;
write_item(Y);
read_item(X);
X:=X+N;
write_item(X);
read_item(Y);
Y:=Y+M;
write_item(Y);
read_item(Y);
Y:=Y-N;
write_item(Y);
read_item(X);
X:=X+N;
write_item(X);
read_item(Y);
Y:=Y+M;
write_item(Y);
Schedule C Schedule D
T1 T2 T1 T2
read_item(Y);
Y:=Y-N;
write_item(Y);
read_item(X);
X:=X+N;
write_item(X);
read_item(Y);
Y:=Y+M;
write_item(Y);
read_item(Y);
Y:=Y-N;
write_item(Y);
read_item(X);
X:=X+N;
write_item(X);
read_item(Y);
Y:=Y+M;
write_item(Y);
TimeTime
TimeTime

---

### 題目 19 (110年)

**來源**: `110年公務人員高等考試三級考試試題考試時間：2 小時 座號：.txt`
**關鍵字**: 資料, Lock, 機制, 項目, 鎖定...

四、資料庫系統中，經常使用「鎖」（Lock）的機制來進行交易處理（Transaction
Processing）中的併行控制（Concurrency Control），而該機制允許某個資
料項目（Data Item）被「共享鎖」（Shared Lock）或「排他鎖」（Exclusive
Lock）鎖定。請問這兩種不同鎖定的模式，對一個資料項目的使用方式
所造成的限制各自為何？另外，資料項目可以小到一筆資料列（Tuple）
或紀錄（Record），也可以大到涵蓋一整個表格或資料庫。請分析資料項
目的大小對系統的效能影響為何？（20 分）

---

### 題目 20 (109年)

**來源**: `109年公務人員特種考試關務人員、身心障礙人員考試及109年國軍上校以上軍官轉任公務人員考試試題考 試 別：關務人員考試等 別：三等考試.txt`
**關鍵字**: TS, 時間, 進行, Read, Write...

四、假設現有下列兩個 transactions 同步存取資料 X, Y，請繪製表格說明，
不同時間標記點，如果讀寫動作被允許進行，系統對資料 X, Y 所記
錄的 R_TS（讀取的時間標記）及 W_TS（寫入的時間標記）為何？
如果讀寫動作不被允許進行，請說明原因及系統會作出的回應為何？
註：系統進行時序如下列左圖，解答表格參考下列右圖。（20 分）
Time
1
2
3
4
5
6
7
8
9
T1 T2
Begin
Read(Y)
Read(X)
Write(X)
Write(Y)
Commit
Begin
Read(X)
Write(X)
Commit
TS(T1)=？？, TS(T2)=？？
Time Data R_TS W_TS
1 X
Y
2 X
Y

---

### 題目 21 (109年)

**來源**: `109年特種考試地方政府公務人員考試試題等 別：三等考試考試時間：2小時 座號：.txt`
**關鍵字**: 技術, 同步控制, 資料, 實作, 環境...

三、在資料庫的實作及環境中，同步控制（Concurrency Control ）在交易
（Transactions）處理是很重要的技術，請論述兩階段鎖定（Two-phase
Locking）與時戳（Timestamps）技術及其不同處。（20分）

---

### 題目 22 (109年)

**來源**: `109年公務人員特種考試司法人員、法務部人員、海岸巡防人員及移民行政人員考試試題等 別：三等考試.txt`
**關鍵字**: T1, T2, read, write, 排程...

二、在資料庫的交易（Transaction）管理中何謂序列排程（Serial Schedule）？
符合序列排程對資料庫有何影響？又何謂可循序列排程（Serializable
Schedule）？兩者關係為何？（10分）
在同步控制中結果等價（Result Equivalent ）與衝突等價（Conflict
Equivalent）意義上有何差異？並請說明下列二個排程是否具備衝突等
價及說明原因，其中 T1與 T2代表不同的兩個交易，read()代表讀取資
料，write()代表寫入資料，→代表事件執行先後順序。（15分）
Schedule A: T1:read(x) → T1:read(y) → T2:read(x) → T1:write(x) →
T1:write(y) → T2:write(x) → T1:commit → T2:read(y) →
T2:write(y) →T2:commit
Schedule B: T1:read(x) → T1:read(y) → T1:write(x) → T2:read(x) →
T1:write(y) → T2:read(y) → T1:commit → T2:write(x) →
T2:write(y) →T2:commit
代號：41450
60350
頁次：2－2

---

### 題目 23 (109年)

**來源**: `109年公務人員特種考試司法人員、法務部人員、海岸巡防人員及移民行政人員考試試題等 別：三等考試.txt`
**關鍵字**: 資料, 過程, 交易, NoSQL, 設計...

四、NoSQL 一般用來代表分散式非關聯式資料庫的統稱，其為現代半結構和
非結構式資料的理想資料庫。已知關聯式資料庫採用的交易
（Transaction）設計，讓資料存取或異動過程中不會受到干擾，為確保交
易是正確可靠的，所以 SQL 執行必須具備⑴確保交易作為最小運作單位
（Atomicity）、⑵異動過程確保整體資料庫的一致性（Consistency）、⑶執
行多筆交易時能隔離交易中的資料不受其他交易影響（Isolation），以及
⑷交易過程不會變動原始資料的持久性（Durability）。請問 NoSQL 是否
適用相同的設計特性？其在資料庫完整性的概念為何？（25分）

---

### 題目 24 (108年)

**來源**: `108年公務人員特種考試關務人員、身心障礙人員考試及108年國軍上校以上軍官轉任公務人員考試試 題考試別 ： 關務人員考試等別 ： 三等考試.txt`
**關鍵字**: 處理, 當資料, 庫系統, 發生, 處理常...

三、當資料庫系統發生故障時，回復處理常採用交易記錄回復處理 （Log-based
Recovery）。試說明此種回復處理方式的原理以及運作過程。（25 分）
代號： 10440
頁次： 2－2

---

### 題目 25 (108年)

**來源**: `108年特種考試地方政府公務人員考試試題等 別：三等考試考試時間：2 小時 座號：.txt`
**關鍵字**: 時間, 戳記, 項目, TS, write...

三、假設某資料庫管理系統採用時間戳記（Timestamp）來管理並行控制
（Concurrency Control），它採用的不是基本的時間戳記排序，而是修改
版的 Thomas 的編寫規則（Write Rule ）。假設某交易 T 的時間戳記是
10010，請問下列情況，資料庫管理系統會如何處理？（每小題 5 分，
共 20 分）
欲寫某項目 X 時，得知 X 已有寫的時間戳記 write_TS（X）是 10015
欲寫某項目 X 時，得知 X 已有讀的時間戳記 read_TS（X）是10012
欲讀某項目 X 時，得知 X 已有寫的時間戳記 write_TS（X）是 10020
欲讀某項目 X 時，得知 X 已有寫的時間戳記 write_TS（X）是 10005
代號：34230
頁次：3－3

---

### 題目 26 (108年)

**來源**: `108年公務人員高等考試三級考試試題考試時間： 2 小時 座號：.txt`
**關鍵字**: 並行, 時程, 兩階段, 鎖定, 執行...

四、兩階段鎖定（Two-Phase Locking）技術可以用來做並行控制（Concurrency
Control），請詳細說明符合兩階段鎖定協定的交易應遵循的規範為何？
時程（Schedule）是指多個交易（Transaction）並行（Concurrency）執
行時，各交易內的操作（Operation）間的執行順序。請以此觀點說明若
所有交易都遵循兩階段鎖定協定撰寫，則這些交易並行執行時，時程必
定是什麼時程？並說明為何遵循這種 時程執行可以達到並行控制的目
的？（20 分）

---

### 題目 27 (108年)

**來源**: `108年公務、關務人員升官等考試、108年交通事業郵政、公路、港務人員升資考試試題.txt`
**關鍵字**: 交易, 循序, 共時, 二筆, read...

五、有關交易管理中並行控制（concurrency control）的主要目的，是維持各
別不同交易在共時情況下，在完成後仍然保有可循序性（serializability），
用以保證交易的正確無誤。（每小題 10 分，共20 分）
請說明何謂交易的可循序性？並用以下交易1 與交易2 二筆交易所進
行的動作，具體舉例在何種共時狀況下會違反可循序性，造成問題。
請您提出一種控制機制可以保證共時交易的可循序性。並請使用該控
制機制，以交易1 與交易 2 二筆交易為例，簡要說明如何達成共時交
易的可循序性。
交易 1 交易 2
read(x) read(x)
x = x + 1000 if x >=100
write(x) x = x - 100
Commit write(x)
Commit

---

### 題目 28 (107年)

**來源**: `107年公務人員高等考試三級考試試題 代號：36370 全一張考試時間： 2 小時 座 號 ：.txt`
**關鍵字**: 排程, 循序, 執行, 序列, 同步...

四、假設現有如圖三個transactions 同步存取資料A, B, C，請使用conflict equivalent 說明
圖中同步執行的非序列排程（ non-serial schedule ），是否具有排程循序性
（serializability）；如果具備排程循序性，執行結果可以等同於三個Transactions 的那
種序列排程；如果不具排程循序性，衝突的cycle 為何？（15 分）

---

### 題目 29 (107年)

**來源**: `107年公務人員特種考試警察人員、一般警察人員考試及107年 特種考試交通事業鐵路人員考試試題 代號：30540 全一張考試別 ： 一般警察人員考試等別 ： 三等考試.txt`
**關鍵字**: 變化, Read, 分散式, 管理系, 10...

四、星羽公司為因應全球佈局，在各個國家使用不同的管理資訊系統，採用了分散式資
料庫管理系統，公司為掌握營運狀況，整合各系統資料庫進行分析。
請詳細說明分散式資料庫管理系統的特性。(10 分)
兩個交易P1 與 P2 各包括數個不同的操作，將這兩個交易按照時間先後順序輪流進
入 CPU 執行，請寫出下表P1，P2 與 DB 值的變化。（10 分）
時間 P 1 P 2 P 1 值的變化 P 2 值的變化 DB 值的變化
t0   E=16、F=5、G=3
t1 Read(F)
t2 F=E-G
t3  Read(F)
t4  F=E+G
t5 Write(F)
t6  Write(F)
t7  Read(G)
t8 Read(E)

---

### 題目 30 (107年)

**來源**: `107年特種考試地方政府公務人員考試試題等 別：三等考試考試時間： 2 小時 座號：.txt`
**關鍵字**: 資料, 分散式, 透明度, 管理系, 庫系統...

五、分散式資料庫系統的優點是擁有透明度（Transparency），請寫出三種
分散式資料庫的透明度並說明之。（8 分）
為確保資料庫交易（ Transactions）能正確被執行，資料庫管理系統
（DBMS）的並行控制（Concurrency Control）與回復方式（Recovery
Methods）應具備那四項特性（Properties）？請說明之。（12 分）

---

### 題目 31 (106年)

**來源**: `106年公務人員高等考試三級考試試題 代號：26070 全一張考試時間：2 小時 座 號 ：.txt`
**關鍵字**: 資料, 管理系, 系統, 動作, 故障...

四、有關資料庫中交易（transaction）管理之永久性（Durability, Permanency）特性，為一
旦交易全部執行，且經過確認（Commit）後，即使未來發生系統當機或毀損，其對
資料庫所做的變更則永遠有效。為能從各種故障回復，當交易進行中，系統常以維
護一個日誌（Log），來提供交易錯誤或故障時，所需的復原資訊。若交易被正常完
成時，資料庫管理系統（database management system）會進行交易Commit 動作，否
則將對此交易進行 Rollback 動作。試問資料庫管理系統將如何動作，即便是資料庫
管理系統正處理日誌（Log）資料時，系統發生故障了，也能確保上述交易管理之永
久性。（6 分）當系統故障時，系統如何處理？（4 分）

---

### 題目 32 (106年)

**來源**: `106年公務人員特種考試警察人員、一般警察人員考試及 106 年特種考試交通事業鐵路人員、退除役軍人轉任公務人員考試試題考試別 ： 一般警察人員考試.txt`
**關鍵字**: 單元性, 一致性, 交易, 特性, Transaction...

三、交易（Transaction）是資料庫的邏輯工作單元，由一或多個運算所構成。交易有四個
基本特性，統稱為 ACID 特性，其中 A 代表單元性（Atomicity）、C 代表一致性
（Consistency）。請分別說明交易的單元性與一致性。（20 分）

---

### 題目 33 (106年)

**來源**: `106年公務人員特種考試關務人員考試、106年公務人員特種考試身心障礙人員考試及106年國軍上校以上軍官轉任公務人員考試試題.txt`
**關鍵字**: Transaction, 執行, Begin, Read, Write...

四、有一個交易執行程序（Transaction execution schedule），記錄了二筆交易（transactions）
的執行步驟如下：（每小題10 分，共 20 分）
Time Transaction A Transaction B
1 Begin（A）
2  Begin （B）
3  Read（X）
4 Read（X）
5 X = X + 5
6 Write（X）
7 End（A）
8  Write （X）
9  End（B）
請問這執行會導致怎樣的資料更新問題（update anomaly），並說明問題是在那個時
間點，如何發生的？
什麼是二階段鎖定協定（Two-Phase Locking Protocol）？若使用二階段鎖定協定，
會怎樣執行這二個交易？

---

### 題目 34 (105年)

**來源**: `105年公務人員特種考試司法人員、法務部人員、海岸巡防人員及移民行政人員考試試題.txt`
**關鍵字**: 執行, 庫系統, Tf, 時間, 系統...

三、假設有4 筆同步執行的交易（transactions），其執行狀態如下圖，其中，「 」代表交
易開始執行，「 」代表該交易執行中，「 」代表該交易正常結束執行；Tc1 與 Tc2 表
示資料庫系統執行檢查的兩個時間點（checkpoint），Tf 則是表示在該時間點時，資
料庫系統發生故障（system failure）。請問要用何種機制，來達成資料庫系統的回復
（Recovery）？請詳細說明此機制如何運作，以及分別在各時間點上，應該進行那
些事項與訊息紀錄，並說明每一筆交易在發生系統故障（Tf）後，該進行何種動作？
（25 分）

---

### 題目 35 (105年)

**來源**: `105年公務人員特種考試司法人員、法務部人員、海岸巡防人員及移民行政人員考試試題考試別 ： 調查人員.txt`
**關鍵字**: 試述, 名詞, 意涵, 每小題, 25...

一、請試述下列名詞之意涵：（每小題5 分，共 25 分）
實體完整性（Entity Integrity）
兩階段鎖定（Two Phase Locking, 2PL）
部分功能相依（Partial Functional Dependency）
開放資料庫互連（Open Database Connectivity, ODBC）
樂觀並行控制（Optimistic Concurrency Control）

---

### 題目 36 (105年)

**來源**: `105年公務人員特種考試司法人員、法務部人員、海岸巡防人員及移民行政人員考試試題考試別 ： 調查人員.txt`
**關鍵字**: 庫系統, 失敗, 發生, 種類, 當資料...

三、當資料庫系統發生失敗（failure）後，必須重新回到一個已知的正確狀態，稱之為復
原（Recovery），請問資料庫系統發生失敗的種類，可分為那幾種？而面對各種不同
種類的失敗，復原資料庫系統的方法為何？（25 分）

---

### 題目 37 (104年)

**來源**: `104年特種考試地方政府公務人員考試試題 代號：34330 全一張等別 ： 三等考試.txt`
**關鍵字**: 商品, 購買, 最小, 編號, T100...

一、下列為包含五筆交易之交易資料庫，在購買的商品欄位中，每一個英文字母代表一
種商品，例如編號T100 的交易購買M、O、N、K、E、Y 六種商品。
交易編號    購買的商品
T100 {M, O, N, K, E, Y}
T200 {D, O, N, K, E, Y}
T300 {M, A, K, E}
T400 {M, U, C, K, Y}
T500 {C, O, K, I, E}
關聯規則的形式為A⇒B，其中A 與B 皆為商品的集合（例如{M, K}），表示如果顧
客買了A 集合的商品就會買B 集合的商品。假設最小支持度與最小信賴度分別為60%
與 80%，請找出所有滿足最小支持度與最小信賴度的關聯規則。（20 分）

---

### 題目 38 (104年)

**來源**: `104年公務人員高等考試三級考試試題 代號：26870考試時間： 2 小時 座 號 ：.txt`
**關鍵字**: 執行, 過程, Read, Write, T1...

五、線上交易處理（Online Transaction Processing ）是資料庫系統中的一個重要功能，請
回答下列各題：（每小題5 分，共 20 分）
定義什麼是一個交易（Transaction）？它必須滿足那四個特性？
何謂並行控制（Concurrency Control ）？資料庫中若無並行控制的機制，則可能
會產生什麼問題？
何謂兩階段鎖定（Two-Phase Locking）？其目的為何？
圖四為兩個交易 T1 及 T2 的執行過程（Schedule），假設交易執行的過程中有實
施兩階段鎖定，請問這個執行過程（ Schedule）的結果是順利執行完畢，或是發
生死結狀態（Deadlock）？
T1 T2
Read(A)
A:=A-50
Write(A)
Read(B)
B:=B-10
Write(B)
Read(A)
A:=A+10
Write(A)
Read(B)
B:=B+50
Write(B)
圖四、交易 T1、T2 的執行過程（指令的上下位置表示執行時間的先後，上面的指令比下面的
指令先發生）

---

